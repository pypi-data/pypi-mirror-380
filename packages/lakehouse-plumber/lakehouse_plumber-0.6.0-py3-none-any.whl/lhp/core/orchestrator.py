"""Main orchestration for LakehousePlumber pipeline generation."""

import logging
import os
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple, Set
from collections import defaultdict
from dataclasses import dataclass

# Service imports
from .services.flowgroup_discoverer import FlowgroupDiscoverer
from .services.flowgroup_processor import FlowgroupProcessor
from .services.code_generator import CodeGenerator
from .services.pipeline_validator import PipelineValidator
from .services.generation_planning_service import GenerationPlanningService

# Component imports (for service initialization)
from ..parsers.yaml_parser import YAMLParser
from ..presets.preset_manager import PresetManager
from .template_engine import TemplateEngine
from .project_config_loader import ProjectConfigLoader
from ..utils.substitution import EnhancedSubstitutionManager
from .action_registry import ActionRegistry
from .validator import ConfigValidator
from .secret_validator import SecretValidator
from .dependency_resolver import DependencyResolver
from .state_manager import StateManager
from .factories import OrchestrationDependencies
from .commands import CommandRegistry, CommandContext, CommandResult
from .layers import BusinessLayer
from ..utils.formatter import format_code
from ..models.config import FlowGroup, Action, ActionType
from ..utils.error_formatter import LHPError, ErrorCategory
from ..utils.smart_file_writer import SmartFileWriter
from ..utils.version import get_version


@dataclass
class GenerationAnalysis:
    """Rich result object containing all generation analysis information."""
    
    # Core results
    pipelines_needing_generation: Dict[str, Dict]  # What CLI currently needs
    pipelines_up_to_date: Dict[str, int]         # pipeline_name -> file_count
    
    # Context information  
    has_global_changes: bool
    global_changes: List[str]
    include_tests_context_applied: bool
    
    # Summary statistics
    total_new_files: int
    total_stale_files: int
    total_up_to_date_files: int
    
    # Detailed information (for verbose mode)
    detailed_staleness_info: Dict[str, Any]
    
    def has_work_to_do(self) -> bool:
        """Check if any generation work needs to be done."""
        return len(self.pipelines_needing_generation) > 0
    
    def get_generation_reason(self, pipeline_name: str) -> str:
        """Get the reason why a pipeline needs generation."""
        if pipeline_name in self.pipelines_needing_generation:
            info = self.pipelines_needing_generation[pipeline_name]
            if info.get("reason"):
                return info["reason"]
            
            reasons = []
            if "new" in info and len(info["new"]) > 0:
                reasons.append(f"{len(info['new'])} new")
            if "stale" in info and len(info["stale"]) > 0:
                reasons.append(f"{len(info['stale'])} stale")
            return ", ".join(reasons) if reasons else "unknown"
        return "up-to-date"


class ActionOrchestrator:
    """
    Main orchestration for pipeline generation (Service-based architecture).
    
    Implements the business layer interface and coordinates specialized services
    for discovery, processing, generation, and validation while maintaining 
    the same public API for backward compatibility.
    """

    def __init__(self, project_root: Path, enforce_version: bool = True, 
                 dependencies: OrchestrationDependencies = None):
        """
        Initialize orchestrator with service composition and dependency injection.

        Args:
            project_root: Root directory of the LakehousePlumber project
            enforce_version: Whether to enforce version requirements (default: True)
            dependencies: Optional dependency container for injection (uses defaults if None)
        """
        self.project_root = project_root
        self.enforce_version = enforce_version
        self.dependencies = dependencies or OrchestrationDependencies()
        self.logger = logging.getLogger(__name__)

        # Initialize core components (still needed for services)
        self.yaml_parser = YAMLParser()
        self.preset_manager = PresetManager(project_root / "presets")
        self.template_engine = TemplateEngine(project_root / "templates")
        self.project_config_loader = ProjectConfigLoader(project_root)
        self.action_registry = ActionRegistry()
        self.config_validator = ConfigValidator(project_root)
        self.secret_validator = SecretValidator()
        self.dependency_resolver = DependencyResolver()

        # Load project configuration
        self.project_config = self.project_config_loader.load_project_config()

        # Initialize services with component dependencies
        self.discoverer = FlowgroupDiscoverer(project_root, self.project_config_loader)
        self.processor = FlowgroupProcessor(
            self.template_engine, self.preset_manager,
            self.config_validator, self.secret_validator
        )
        self.generator = CodeGenerator(
            self.action_registry, self.dependency_resolver,
            self.preset_manager, self.project_config, project_root
        )
        self.validator = PipelineValidator(
            project_root, self.config_validator, self.secret_validator
        )
        self.planning_service = GenerationPlanningService(
            project_root, self.discoverer
        )
        self.command_registry = CommandRegistry()

        # Enforce version requirements if specified and enabled
        if self.enforce_version:
            self._enforce_version_requirements()

        self.logger.info(
            f"Initialized ActionOrchestrator with service-based architecture: {project_root}"
        )
        if self.project_config:
            self.logger.info(
                f"Loaded project configuration: {self.project_config.name} v{self.project_config.version}"
            )
        else:
            self.logger.info("No project configuration found, using defaults")

    def _enforce_version_requirements(self) -> None:
        """Enforce version requirements if specified in project config."""
        # Skip if no project config or no version requirement
        if not self.project_config or not self.project_config.required_lhp_version:
            return
        
        # Check for bypass environment variable
        if os.environ.get("LHP_IGNORE_VERSION", "").lower() in ("1", "true", "yes"):
            self.logger.warning(
                f"Version requirement bypass enabled via LHP_IGNORE_VERSION. "
                f"Required: {self.project_config.required_lhp_version}"
            )
            return
        
        try:
            from packaging.version import Version
            from packaging.specifiers import SpecifierSet
        except ImportError:
            raise LHPError(
                category=ErrorCategory.CONFIG,
                code_number="006", 
                title="Missing packaging dependency",
                details="The 'packaging' library is required for version range checking but is not installed.",
                suggestions=[
                    "Install packaging: pip install packaging>=23.2",
                    "Or set LHP_IGNORE_VERSION=1 to bypass version checking",
                ],
            )
        
        required_spec = self.project_config.required_lhp_version
        actual_version = get_version()
        
        try:
            spec_set = SpecifierSet(required_spec)
            actual_ver = Version(actual_version)
            
            if actual_ver not in spec_set:
                raise LHPError(
                    category=ErrorCategory.CONFIG,
                    code_number="007",
                    title="LakehousePlumber version requirement not satisfied",
                    details=f"Project requires LakehousePlumber version '{required_spec}', but version '{actual_version}' is installed.",
                    suggestions=[
                        f"Install a compatible version: pip install 'lakehouse-plumber{required_spec}'",
                        f"Or update the project's version requirement in lhp.yaml if you intend to upgrade",
                        "Or set LHP_IGNORE_VERSION=1 to bypass version checking (not recommended for production)",
                    ],
                    context={
                        "Required Version": required_spec,
                        "Installed Version": actual_version,
                        "Project Name": self.project_config.name,
                    },
                )
        except Exception as e:
            if isinstance(e, LHPError):
                raise
            raise LHPError(
                category=ErrorCategory.CONFIG,
                code_number="008",
                title="Invalid version requirement specification",
                details=f"Could not parse version requirement '{required_spec}': {e}",
                suggestions=[
                    "Use valid PEP 440 version specifiers (e.g., '>=0.4.1,<0.5.0')",
                    "Check the required_lhp_version field in lhp.yaml",
                    "Examples: '==0.4.1', '~=0.4.1', '>=0.4.1,<0.5.0'",
                ],
            )

    def get_include_patterns(self) -> List[str]:
        """
        Get include patterns from project configuration.
        
        Returns:
            List of include patterns, or empty list if none specified
        """
        return self.discoverer.get_include_patterns()

    # ============================================================================
    # COMMAND PATTERN API - Alternative, highly testable interface
    # ============================================================================
    
    def execute_command(self, command_type: str, env: str, **kwargs) -> CommandResult:
        """
        Execute orchestration command using command pattern.
        
        This provides an alternative, more testable interface to the existing methods.
        Commands abstract the orchestration operations and can be easily mocked.
        
        Args:
            command_type: Type of command to execute ("generate", "validate", "analyze")
            env: Environment name
            **kwargs: Additional parameters for the command
            
        Returns:
            CommandResult with execution results
            
        Example:
            # Generate pipeline
            result = orchestrator.execute_command(
                "generate", "dev", 
                pipeline_identifier="my_pipeline",
                include_tests=True,
                output_dir=Path("generated/dev")
            )
            
            # Validate pipeline
            result = orchestrator.execute_command(
                "validate", "dev",
                pipeline_identifier="my_pipeline"  
            )
            
            # Analyze staleness
            result = orchestrator.execute_command(
                "analyze", "dev",
                pipeline_names=["pipeline1", "pipeline2"],
                include_tests=False
            )
        """
        # Create command context
        context = CommandContext(
            project_root=self.project_root,
            env=env,
            orchestrator=self,
            state_manager=kwargs.get('state_manager'),
            **kwargs
        )
        
        # Execute command through registry
        return self.command_registry.execute_command(command_type, context)
    
    def list_available_commands(self) -> List[str]:
        """List all available command types."""
        return self.command_registry.list_commands()
    
    def get_command_info(self, command_type: str) -> Optional[Dict[str, Any]]:
        """Get information about a specific command."""
        command = self.command_registry.get_command(command_type)
        if command:
            return {
                "name": command.name,
                "type": command_type,
                "class": command.__class__.__name__
            }
        return None

    # ============================================================================
    # BUSINESS LAYER INTERFACE IMPLEMENTATION
    # ============================================================================
    
    def create_generation_plan(self, env: str, pipeline_identifier: str, 
                              include_tests: bool, **kwargs):
        """Create generation plan based on business rules."""
        return self.planning_service.create_generation_plan(
            env=env,
            pipeline_identifier=pipeline_identifier,
            include_tests=include_tests,
            force=kwargs.get('force', False),
            specific_flowgroups=kwargs.get('specific_flowgroups'),
            state_manager=kwargs.get('state_manager')
        )
    
    def execute_generation_strategy(self, strategy_type: str, context: Any) -> Any:
        """Execute generation strategy based on business logic."""
        # Delegate to strategy factory and execution
        from .strategies import GenerationStrategyFactory
        strategy = GenerationStrategyFactory.create_strategy(
            force=(strategy_type == "force"),
            specific_flowgroups=getattr(context, 'specific_flowgroups', None),
            has_state_manager=bool(getattr(context, 'state_manager', None))
        )
        
        # Create flowgroups list from context
        all_flowgroups = self.discover_all_flowgroups()
        
        return strategy.filter_flowgroups(all_flowgroups, context)
    
    def validate_configuration(self, pipeline_identifier: str, env: str) -> tuple:
        """Validate configuration based on business rules."""
        return self.validate_pipeline_by_field(pipeline_identifier, env)

    def analyze_generation_requirements(self, env: str, pipeline_names: List[str], 
                                      include_tests: bool, force: bool = False,
                                      state_manager: Optional[StateManager] = None) -> GenerationAnalysis:
        """
        Analyze generation requirements including generation context awareness.
        
        This method centralizes all generation decision logic including:
        - Basic staleness detection (YAML, dependencies) 
        - Generation context staleness (include_tests parameter changes)
        - Force mode handling
        - Rich result data for CLI presentation
        
        Args:
            env: Environment to analyze
            pipeline_names: List of pipeline names to check
            include_tests: Current include_tests parameter
            force: Force regeneration flag
            state_manager: Optional state manager for staleness detection
            
        Returns:
            GenerationAnalysis object with structured results
        """
        # Initialize result structure
        pipelines_needing_generation = {}
        pipelines_up_to_date = {}
        total_new = 0
        total_stale = 0  
        total_up_to_date = 0
        
        # Handle force mode or no state tracking
        if force or not state_manager:
            for pipeline_name in pipeline_names:
                reason = "force" if force else "no_state_tracking"
                pipelines_needing_generation[pipeline_name] = {"reason": reason}
            
            return GenerationAnalysis(
                pipelines_needing_generation=pipelines_needing_generation,
                pipelines_up_to_date={},
                has_global_changes=False,
                global_changes=[],
                include_tests_context_applied=False,
                total_new_files=0,
                total_stale_files=0,
                total_up_to_date_files=0,
                detailed_staleness_info={}
            )
        
        # Get global staleness information
        staleness_info = state_manager.get_detailed_staleness_info(env)
        has_global_changes = bool(staleness_info.get("global_changes"))
        global_changes = staleness_info.get("global_changes", [])
        
        # If global changes detected, all pipelines need regeneration
        if has_global_changes:
            for pipeline_name in pipeline_names:
                pipelines_needing_generation[pipeline_name] = {"reason": "global_changes"}
            
            return GenerationAnalysis(
                pipelines_needing_generation=pipelines_needing_generation,
                pipelines_up_to_date={},
                has_global_changes=True,
                global_changes=global_changes,
                include_tests_context_applied=False,
                total_new_files=0,
                total_stale_files=0, 
                total_up_to_date_files=0,
                detailed_staleness_info=staleness_info
            )
        
        # Analyze each pipeline for staleness (including generation context)
        include_tests_stale_found = False
        
        for pipeline_name in pipeline_names:
            # Get basic staleness info
            generation_info = state_manager.get_files_needing_generation(env, pipeline_name)
            
            new_count = len(generation_info["new"])
            stale_count = len(generation_info["stale"]) 
            up_to_date_count = len(generation_info["up_to_date"])
            
            # Check for generation context staleness using planning service
            all_flowgroups = self.discover_flowgroups_by_pipeline_field(pipeline_name)
            generation_context_stale = self.planning_service.analyze_generation_context_staleness(
                all_flowgroups, env, include_tests, state_manager
            )
            
            # Include generation context stale flowgroups in stale count
            if generation_context_stale:
                include_tests_stale_found = True
                # Add context-stale flowgroups to the stale list
                for flowgroup_name in generation_context_stale:
                    self.logger.debug(f"Flowgroup {flowgroup_name} marked as stale due to generation context")
                stale_count += len(generation_context_stale)
            
            # Update totals
            total_new += new_count
            total_stale += stale_count
            total_up_to_date += up_to_date_count
            
            # Determine if pipeline needs generation
            if new_count > 0 or stale_count > 0:
                # Add generation context stale info to generation_info
                if generation_context_stale:
                    generation_info["context_stale"] = list(generation_context_stale)
                
                pipelines_needing_generation[pipeline_name] = generation_info
            else:
                pipelines_up_to_date[pipeline_name] = up_to_date_count
        
        return GenerationAnalysis(
            pipelines_needing_generation=pipelines_needing_generation,
            pipelines_up_to_date=pipelines_up_to_date,
            has_global_changes=False,
            global_changes=[],
            include_tests_context_applied=include_tests_stale_found,
            total_new_files=total_new,
            total_stale_files=total_stale,
            total_up_to_date_files=total_up_to_date,
            detailed_staleness_info=staleness_info
        )

    def generate_pipeline(
        self,
        pipeline_name: str,
        env: str,
        output_dir: Path = None,
        state_manager=None,
        force_all: bool = False,
        specific_flowgroups: List[str] = None,
        include_tests: bool = False,
    ) -> Dict[str, str]:
        """Generate complete pipeline from YAML configs.

        Args:
            pipeline_name: Name of the pipeline to generate
            env: Environment to generate for (e.g., 'dev', 'prod')
            output_dir: Optional output directory for generated files
            state_manager: Optional state manager for tracking generated files
            force_all: If True, generate all flowgroups regardless of changes
            specific_flowgroups: If provided, only generate these specific flowgroups

        Returns:
            Dictionary mapping filename to generated code content
        """
        self.logger.info(
            f"Generating pipeline '{pipeline_name}' for environment '{env}'"
        )

        # Discover and filter flowgroups using extracted method
        flowgroups = self._discover_and_filter_flowgroups(
            env=env,
            pipeline_identifier=pipeline_name,
            include_tests=include_tests,
            force_all=force_all,
            specific_flowgroups=specific_flowgroups,
            state_manager=state_manager,
            use_directory_discovery=True
        )

        # 2. Load substitution manager for environment
        substitution_file = self.project_root / "substitutions" / f"{env}.yaml"
        substitution_mgr = self.dependencies.create_substitution_manager(substitution_file, env)

        # 3. Initialize smart file writer
        smart_writer = self.dependencies.create_file_writer()

        # 4. Process all flowgroups first
        processed_flowgroups = []
        for flowgroup in flowgroups:
            self.logger.info(f"Processing flowgroup: {flowgroup.flowgroup}")

            try:
                # Process flowgroup
                processed_flowgroup = self.process_flowgroup(
                    flowgroup, substitution_mgr
                )
                processed_flowgroups.append(processed_flowgroup)

            except Exception as e:
                self.logger.debug(
                    f"Error processing flowgroup {flowgroup.flowgroup}: {e}"
                )
                raise

        # 5. Validate table creation rules across entire pipeline
        try:
            table_creation_errors = self.config_validator.validate_table_creation_rules(
                processed_flowgroups
            )
            if table_creation_errors:
                raise ValueError(
                    "Table creation validation failed:\n"
                    + "\n".join(f"  - {error}" for error in table_creation_errors)
                )
        except Exception as e:
            # Handle LHPError by converting to string (like the validator does)
            raise ValueError(f"Table creation validation failed:\n  - {str(e)}")

        # 6. Generate code for each processed flowgroup
        generated_files = {}

        for processed_flowgroup in processed_flowgroups:
            self.logger.info(
                f"Generating code for flowgroup: {processed_flowgroup.flowgroup}"
            )

            try:
                # Find source YAML for this flowgroup (needed for file tracking)
                source_yaml = self._find_source_yaml_for_flowgroup(processed_flowgroup)
                
                # Generate code
                code = self.generate_flowgroup_code(
                    processed_flowgroup, substitution_mgr, output_dir, state_manager, source_yaml, env, include_tests
                )

                # Format code
                formatted_code = format_code(code)

                # Check if content is empty BEFORE any file operations
                filename = f"{processed_flowgroup.flowgroup}.py"
                if not formatted_code.strip():
                    # Skip this flowgroup entirely - don't write files or track in state
                    self.logger.info(f"Skipping empty flowgroup: {processed_flowgroup.flowgroup} (no content to generate)")
                    continue  # Skip to next flowgroup

                # Only proceed with file operations if content exists
                # Store result (we know it's not empty at this point)
                generated_files[filename] = formatted_code

                # Write to output directory if specified
                if output_dir:
                    output_file = output_dir / filename
                    smart_writer.write_if_changed(output_file, formatted_code)

                    # Track the generated file in state manager
                    if state_manager and source_yaml:
                        # Generate context for parameter-sensitive hashing
                        has_test_actions = any(action.type == ActionType.TEST for action in processed_flowgroup.actions)
                        generation_context = f"include_tests:{include_tests}" if has_test_actions else ""
                        
                        state_manager.track_generated_file(
                            generated_path=output_file,
                            source_yaml=source_yaml,
                            environment=env,
                            pipeline=pipeline_name,
                            flowgroup=processed_flowgroup.flowgroup,
                            generation_context=generation_context,
                        )

            except Exception as e:
                self.logger.debug(
                    f"Error generating code for flowgroup {processed_flowgroup.flowgroup}: {e}"
                )
                raise

        # Save state after all files are generated
        if state_manager:
            state_manager.save()

        # Log smart file writer statistics
        if output_dir:
            files_written, files_skipped = smart_writer.get_stats()
            self.logger.info(
                f"Generation complete: {files_written} files written, {files_skipped} files skipped (no changes)"
            )

        return generated_files

    def discover_flowgroups(self, pipeline_dir: Path) -> List[FlowGroup]:
        """
        Discover all flowgroups in a specific pipeline directory.
        
        Args:
            pipeline_dir: Directory containing flowgroup YAML files
            
        Returns:
            List of discovered flowgroups
        """
        return self.discoverer.discover_flowgroups(pipeline_dir)

    def discover_all_flowgroups(self) -> List[FlowGroup]:
        """
        Discover all flowgroups across all directories in the project.

        Returns:
            List of all discovered flowgroups
        """
        return self.discoverer.discover_all_flowgroups()

    def discover_flowgroups_by_pipeline_field(self, pipeline_field: str) -> List[FlowGroup]:
        """Discover all flowgroups with a specific pipeline field across all directories.

        Args:
            pipeline_field: The pipeline field value to search for

        Returns:
            List of flowgroups with the specified pipeline field
        """
        all_flowgroups = self.discover_all_flowgroups()
        matching_flowgroups = []
        
        for flowgroup in all_flowgroups:
            if flowgroup.pipeline == pipeline_field:
                matching_flowgroups.append(flowgroup)
                self.logger.debug(
                    f"Found flowgroup '{flowgroup.flowgroup}' for pipeline '{pipeline_field}'"
                )
        
        return matching_flowgroups

    def validate_duplicate_pipeline_flowgroup_combinations(self, flowgroups: List[FlowGroup]) -> None:
        """Validate that there are no duplicate pipeline+flowgroup combinations.

        Args:
            flowgroups: List of flowgroups to validate

        Raises:
            ValueError: If duplicate combinations are found
        """
        errors = self.config_validator.validate_duplicate_pipeline_flowgroup(flowgroups)
        if errors:
            raise ValueError(f"Duplicate pipeline+flowgroup combinations found: {errors}")

    def generate_pipeline_by_field(
        self,
        pipeline_field: str,
        env: str,
        output_dir: Path = None,
        state_manager=None,
        force_all: bool = False,
        specific_flowgroups: List[str] = None,
        include_tests: bool = False,
    ) -> Dict[str, str]:
        """Generate complete pipeline from YAML configs using pipeline field.

        Args:
            pipeline_field: The pipeline field value to generate
            env: Environment to generate for (e.g., 'dev', 'prod')
            output_dir: Optional output directory for generated files
            state_manager: Optional state manager for tracking generated files
            force_all: If True, generate all flowgroups regardless of changes
            specific_flowgroups: If provided, only generate these specific flowgroups

        Returns:
            Dictionary mapping filename to generated code content
        """
        self.logger.info(
            f"Starting pipeline generation by field: {pipeline_field} for env: {env}"
        )

        # Validate no duplicate pipeline+flowgroup combinations
        all_flowgroups = self.discover_all_flowgroups()
        self.validate_duplicate_pipeline_flowgroup_combinations(all_flowgroups)

        # Discover and filter flowgroups using extracted method
        flowgroups = self._discover_and_filter_flowgroups(
            env=env,
            pipeline_identifier=pipeline_field,
            include_tests=include_tests,
            force_all=force_all,
            specific_flowgroups=specific_flowgroups,
            state_manager=state_manager,
            use_directory_discovery=False  # Use field-based discovery
        )

        # Set up output directory based on pipeline field
        if output_dir:
            pipeline_output_dir = output_dir / pipeline_field
            pipeline_output_dir.mkdir(parents=True, exist_ok=True)
        else:
            # For dry-run mode, don't create directories or write files
            pipeline_output_dir = None

        # Initialize substitution manager
        substitution_file = self.project_root / "substitutions" / f"{env}.yaml"
        substitution_mgr = self.dependencies.create_substitution_manager(substitution_file, env)

        generated_files = {}
        
        for flowgroup in flowgroups:
            self.logger.info(f"Processing flowgroup: {flowgroup.flowgroup}")
            
            try:
                # Process flowgroup
                processed_flowgroup = self.process_flowgroup(flowgroup, substitution_mgr)
                
                # Find source YAML for this flowgroup (needed for file tracking)
                source_yaml_path = self._find_source_yaml_for_flowgroup(flowgroup)
                
                # Generate code
                generated_code = self.generate_flowgroup_code(processed_flowgroup, substitution_mgr, pipeline_output_dir, state_manager, source_yaml_path, env, include_tests)
                
                # Format code with Black
                formatted_code = format_code(generated_code)
                
                # Check if content is empty BEFORE any file operations
                if not formatted_code.strip():
                    # Handle empty content - check for existing files to clean up
                    if pipeline_output_dir:
                        output_file = pipeline_output_dir / f"{flowgroup.flowgroup}.py"
                        if output_file.exists():
                            try:
                                # Delete existing file since flowgroup now generates empty content
                                output_file.unlink()
                                self.logger.info(f"Deleted empty flowgroup file: {output_file}")
                                
                                # Remove from state tracking
                                if state_manager:
                                    state_manager.remove_generated_file(output_file, env)
                                    # Clean up empty directories after file deletion
                                    state_manager.cleanup_empty_directories(env, [str(output_file)])
                            except Exception as e:
                                self.logger.error(f"Failed to delete empty flowgroup file {output_file}: {e}")
                                raise  # Fail fast as requested
                    
                    self.logger.info(f"Skipping empty flowgroup: {flowgroup.flowgroup} (no content to generate)")
                    continue  # Skip to next flowgroup
                
                # Only proceed with file operations if content exists
                # Save to file only if output directory is specified (not dry-run)
                if pipeline_output_dir:
                    output_file = pipeline_output_dir / f"{flowgroup.flowgroup}.py"
                    
                    # Use SmartFileWriter for efficient file writing
                    smart_writer = self.dependencies.create_file_writer()
                    smart_writer.write_if_changed(output_file, formatted_code)
                    
                    # Track the generated file in state manager if provided
                    if state_manager and source_yaml_path:
                        # Generate context for parameter-sensitive hashing
                        has_test_actions = any(action.type == ActionType.TEST for action in flowgroup.actions)
                        generation_context = f"include_tests:{include_tests}" if has_test_actions else ""
                        
                        state_manager.track_generated_file(
                            generated_path=output_file,
                            source_yaml=source_yaml_path,
                            environment=env,
                            pipeline=pipeline_field,  # Use pipeline field for state tracking
                            flowgroup=flowgroup.flowgroup,
                            generation_context=generation_context,
                        )
                    
                    self.logger.info(f"Generated: {output_file}")
                else:
                    # Dry-run mode: just log what would be generated
                    self.logger.info(f"Would generate: {flowgroup.flowgroup}.py")
                    
                # Add to generated_files (we know it's not empty at this point)
                generated_files[f"{flowgroup.flowgroup}.py"] = formatted_code
                
            except Exception as e:
                self.logger.error(f"Error generating flowgroup {flowgroup.flowgroup}: {e}")
                raise

        # Save state after all files are generated
        if state_manager:
            state_manager.save()

        # Note: Bundle synchronization is handled at the CLI level after all pipelines are processed
        # to ensure it sees the complete state of all generated files

        self.logger.info(f"Pipeline generation complete: {pipeline_field}")
        return generated_files

    def _find_source_yaml(
        self, pipeline_dir: Path, flowgroup_name: str
    ) -> Optional[Path]:
        """Find the source YAML file for a given flowgroup name.

        Args:
            pipeline_dir: Directory containing flowgroup YAML files
            flowgroup_name: Name of the flowgroup to find

        Returns:
            Path to the source YAML file, or None if not found
        """
        # Search both .yaml and .yml extensions
        for extension in ["*.yaml", "*.yml"]:
            for yaml_file in pipeline_dir.rglob(extension):
                try:
                    flowgroup = self.yaml_parser.parse_flowgroup(yaml_file)
                    if flowgroup.flowgroup == flowgroup_name:
                        return yaml_file
                except Exception as e:
                    self.logger.debug(f"Could not parse flowgroup {yaml_file}: {e}")

        return None

    def _find_source_yaml_for_flowgroup(self, flowgroup: FlowGroup) -> Optional[Path]:
        """Find the source YAML file for a given flowgroup.

        Args:
            flowgroup: The flowgroup to find the source YAML for

        Returns:
            Path to the source YAML file, or None if not found
        """
        pipelines_dir = self.project_root / "pipelines"
        
        if not pipelines_dir.exists():
            return None

        # Search both .yaml and .yml extensions
        for extension in ["*.yaml", "*.yml"]:
            for yaml_file in pipelines_dir.rglob(extension):
                try:
                    parsed_flowgroup = self.yaml_parser.parse_flowgroup(yaml_file)
                    if (parsed_flowgroup.pipeline == flowgroup.pipeline and 
                        parsed_flowgroup.flowgroup == flowgroup.flowgroup):
                        return yaml_file
                except Exception as e:
                    self.logger.debug(f"Could not parse flowgroup {yaml_file}: {e}")

        return None

    def process_flowgroup(self, flowgroup: FlowGroup, 
                         substitution_mgr: EnhancedSubstitutionManager) -> FlowGroup:
        """
        Process flowgroup: expand templates, apply presets, apply substitutions.
        
        Args:
            flowgroup: FlowGroup to process
            substitution_mgr: Substitution manager for the environment
            
        Returns:
            Processed flowgroup
        """
        return self.processor.process_flowgroup(flowgroup, substitution_mgr)

    # _apply_preset_config and _deep_merge methods moved to FlowgroupProcessor service

    def generate_flowgroup_code(self, flowgroup: FlowGroup, substitution_mgr: EnhancedSubstitutionManager,
                               output_dir: Optional[Path] = None, state_manager=None,
                               source_yaml: Optional[Path] = None, env: Optional[str] = None,
                               include_tests: bool = False) -> str:
        """
        Generate complete Python code for a flowgroup.
        
        Args:
            flowgroup: FlowGroup to generate code for
            substitution_mgr: Substitution manager for the environment
            output_dir: Output directory for generated files
            state_manager: State manager for file tracking
            source_yaml: Source YAML path for file tracking
            env: Environment name for file tracking
            include_tests: Whether to include test actions
            
        Returns:
            Complete Python code for the flowgroup
        """
        return self.generator.generate_flowgroup_code(
            flowgroup, substitution_mgr, output_dir, state_manager, 
            source_yaml, env, include_tests
        )

    def determine_action_subtype(self, action: Action) -> str:
        """
        Determine the sub-type of an action for generator selection.
        
        Args:
            action: Action to determine sub-type for
            
        Returns:
            Sub-type string for generator selection
        """
        return self.generator.determine_action_subtype(action)

    def build_custom_source_block(self, custom_sections: List[Dict]) -> str:
        """
        Build the custom source code block to append to flowgroup files.
        
        Args:
            custom_sections: List of dictionaries with custom source code info
            
        Returns:
            Formatted custom source code block with headers
        """
        return self.generator.build_custom_source_block(custom_sections)

    def _discover_and_filter_flowgroups(self, env: str, pipeline_identifier: str, 
                                       include_tests: bool, force_all: bool = False,
                                       specific_flowgroups: List[str] = None,
                                       state_manager=None, use_directory_discovery: bool = False) -> List[FlowGroup]:
        """
        Discover and filter flowgroups based on generation requirements.
        
        Centralizes the duplicate logic from both generation methods including:
        - Flowgroup discovery (by field or directory)
        - Smart generation filtering based on staleness
        - Generation context awareness
        - Specific flowgroup filtering
        
        Args:
            env: Environment name
            pipeline_identifier: Pipeline name or field value
            include_tests: Include test actions parameter
            force_all: Force all flowgroups flag
            specific_flowgroups: Optional list of specific flowgroups
            state_manager: Optional state manager for staleness detection
            use_directory_discovery: Use directory-based discovery vs field-based
            
        Returns:
            List of flowgroups that should be generated
        """
        # 1. Discover flowgroups
        if use_directory_discovery:
            pipeline_dir = self.project_root / "pipelines" / pipeline_identifier
            if not pipeline_dir.exists():
                raise ValueError(f"Pipeline directory not found: {pipeline_dir}")
            all_flowgroups = self.discoverer.discover_flowgroups(pipeline_dir)
        else:
            all_flowgroups = self.discover_flowgroups_by_pipeline_field(pipeline_identifier)
        
        if not all_flowgroups:
            if use_directory_discovery:
                raise ValueError(f"No flowgroups found in pipeline: {pipeline_identifier}")
            else:
                self.logger.warning(f"No flowgroups found for pipeline field: {pipeline_identifier}")
                return []
        
        # 2. Handle specific flowgroups filtering
        if specific_flowgroups:
            filtered_flowgroups = [fg for fg in all_flowgroups if fg.flowgroup in specific_flowgroups]
            self.logger.info(f"Generating specific flowgroups: {len(filtered_flowgroups)}/{len(all_flowgroups)}")
            return filtered_flowgroups
        
        # 3. Handle force mode
        if force_all:
            return all_flowgroups
        
        # 4. Handle smart generation with staleness detection
        if state_manager:
            return self._apply_smart_generation_filtering(
                all_flowgroups, env, pipeline_identifier, include_tests, state_manager
            )
        
        # 5. Fallback - generate all (no state management)
        return all_flowgroups
    
    def _apply_smart_generation_filtering(self, all_flowgroups: List[FlowGroup], 
                                        env: str, pipeline_identifier: str,
                                        include_tests: bool, state_manager) -> List[FlowGroup]:
        """Apply smart generation filtering based on staleness detection."""
        # Get basic staleness information
        generation_info = state_manager.get_files_needing_generation(env, pipeline_identifier)
        
        # Get flowgroups for new YAML files
        new_flowgroups = set()
        for yaml_path in generation_info["new"]:
            try:
                fg = self.yaml_parser.parse_flowgroup(yaml_path)
                new_flowgroups.add(fg.flowgroup)
            except Exception as e:
                self.logger.warning(f"Could not parse new flowgroup {yaml_path}: {e}")
        
        # Get flowgroups for stale files
        stale_flowgroups = {fs.flowgroup for fs in generation_info["stale"]}
        
        # Check for generation context changes using planning service
        generation_context_stale = self.planning_service.analyze_generation_context_staleness(
            all_flowgroups, env, include_tests, state_manager
        )
        stale_flowgroups.update(generation_context_stale)
        
        # Combine all flowgroups that need generation
        flowgroups_to_generate = new_flowgroups | stale_flowgroups
        
        if flowgroups_to_generate:
            # Filter to only include flowgroups that need generation
            filtered_flowgroups = [fg for fg in all_flowgroups if fg.flowgroup in flowgroups_to_generate]
            self.logger.info(f"Smart generation: processing {len(filtered_flowgroups)}/{len(all_flowgroups)} flowgroups")
            return filtered_flowgroups
        else:
            # Nothing to generate
            self.logger.info("Smart generation: no flowgroups need processing")
            return []

    def group_write_actions_by_target(self, write_actions: List[Action]) -> Dict[str, List[Action]]:
        """
        Group write actions by their target table.
        
        Args:
            write_actions: List of write actions
            
        Returns:
            Dictionary mapping target table names to lists of actions
        """
        return self.generator.group_write_actions_by_target(write_actions)

    def _sync_bundle_resources(self, output_dir: Optional[Path], environment: str) -> None:
        """Synchronize bundle resources after successful generation.
        
        Args:
            output_dir: Output directory for generated files (None for dry-run)
            environment: Environment name for generation
        """
        try:
            # Check if bundle support is enabled
            from ..utils.bundle_detection import should_enable_bundle_support
            
            if not should_enable_bundle_support(self.project_root):
                self.logger.debug("Bundle support disabled, skipping bundle synchronization")
                return
            
            # Import and create bundle manager
            from ..bundle.manager import BundleManager
            
            bundle_manager = BundleManager(self.project_root)
            
            # Perform synchronization 
            self.logger.debug(f"Starting bundle resource synchronization for environment: {environment}")
            bundle_manager.sync_resources_with_generated_files(output_dir, environment)
            self.logger.info("Bundle resource synchronization completed successfully")
            
        except ImportError as e:
            self.logger.debug(f"Bundle modules not available: {e}")
        except Exception as e:
            # Bundle errors should not fail the core generation process
            self.logger.warning(f"Bundle synchronization failed: {e}")
            self.logger.debug(f"Bundle sync error details: {e}", exc_info=True)

    def create_combined_write_action(self, actions: List[Action], target_table: str) -> Action:
        """
        Create a combined write action with individual action metadata preserved.
        
        Args:
            actions: List of write actions targeting the same table
            target_table: Full target table name
            
        Returns:
            Combined action with individual action metadata
        """
        return self.generator.create_combined_write_action(actions, target_table)

    def _extract_single_source_view(self, source) -> str:
        """Extract a single source view from various source formats.

        Args:
            source: Source configuration (string, list, or dict)

        Returns:
            Source view name as string
        """
        if isinstance(source, str):
            return source
        elif isinstance(source, list) and source:
            # Take first item from list
            first_item = source[0]
            if isinstance(first_item, str):
                return first_item
            elif isinstance(first_item, dict):
                database = first_item.get("database")
                table = (
                    first_item.get("table")
                    or first_item.get("view")
                    or first_item.get("name", "")
                )
                return f"{database}.{table}" if database and table else table
            else:
                return str(first_item)
        elif isinstance(source, dict):
            database = source.get("database")
            table = source.get("table") or source.get("view") or source.get("name", "")
            return f"{database}.{table}" if database and table else table
        else:
            return ""

    def _extract_source_views_from_action(self, source) -> List[str]:
        """Extract all source views from an action source configuration.

        Args:
            source: Source configuration (string, list, or dict)

        Returns:
            List of source view names
        """
        if isinstance(source, str):
            return [source]
        elif isinstance(source, list):
            result = []
            for item in source:
                if isinstance(item, str):
                    result.append(item)
                elif isinstance(item, dict):
                    database = item.get("database")
                    table = (
                        item.get("table") or item.get("view") or item.get("name", "")
                    )
                    if database and table:
                        result.append(f"{database}.{table}")
                    elif table:
                        result.append(table)
                else:
                    result.append(str(item))
            return result
        elif isinstance(source, dict):
            database = source.get("database")
            table = source.get("table") or source.get("view") or source.get("name", "")
            if database and table:
                return [f"{database}.{table}"]
            elif table:
                return [table]
            else:
                return []
        else:
            return []

    def validate_pipeline(
        self, pipeline_name: str, env: str
    ) -> Tuple[List[str], List[str]]:
        """Validate pipeline configuration without generating code.

        Args:
            pipeline_name: Name of the pipeline to validate
            env: Environment to validate for

        Returns:
            Tuple of (errors, warnings)
        """
        errors = []
        warnings = []

        try:
            pipeline_dir = self.project_root / "pipelines" / pipeline_name
            flowgroups = self._discover_flowgroups(pipeline_dir)

            substitution_file = self.project_root / "substitutions" / f"{env}.yaml"
            substitution_mgr = self.dependencies.create_substitution_manager(substitution_file, env)

            for flowgroup in flowgroups:
                try:
                    self.process_flowgroup(flowgroup, substitution_mgr)
                    # Validation happens in _process_flowgroup
                    # Note: Success validation does not generate warnings

                except Exception as e:
                    errors.append(f"Flowgroup '{flowgroup.flowgroup}': {e}")

        except Exception as e:
            errors.append(f"Pipeline validation failed: {e}")

        return errors, warnings

    def validate_pipeline_by_field(
        self, pipeline_field: str, env: str
    ) -> Tuple[List[str], List[str]]:
        """Validate pipeline configuration using pipeline field without generating code.

        Args:
            pipeline_field: The pipeline field value to validate
            env: Environment to validate for

        Returns:
            Tuple of (errors, warnings)
        """
        errors = []
        warnings = []

        try:
            # Discover flowgroups by pipeline field
            flowgroups = self.discover_flowgroups_by_pipeline_field(pipeline_field)
            
            if not flowgroups:
                errors.append(f"No flowgroups found for pipeline field: {pipeline_field}")
                return errors, warnings

            substitution_file = self.project_root / "substitutions" / f"{env}.yaml"
            substitution_mgr = self.dependencies.create_substitution_manager(substitution_file, env)

            for flowgroup in flowgroups:
                try:
                    self.process_flowgroup(flowgroup, substitution_mgr)
                    # Validation happens in _process_flowgroup
                    # Note: Success validation does not generate warnings

                except Exception as e:
                    errors.append(f"Flowgroup '{flowgroup.flowgroup}': {e}")

        except Exception as e:
            errors.append(f"Pipeline validation failed: {e}")

        return errors, warnings
