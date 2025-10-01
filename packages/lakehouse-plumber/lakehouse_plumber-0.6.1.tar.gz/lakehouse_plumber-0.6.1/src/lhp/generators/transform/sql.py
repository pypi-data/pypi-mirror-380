"""SQL transformation generator for LakehousePlumber."""

from pathlib import Path
from ...core.base_generator import BaseActionGenerator
from ...models.config import Action
from ...utils.operational_metadata import OperationalMetadata


class SQLTransformGenerator(BaseActionGenerator):
    """Generate SQL transformation actions."""

    def __init__(self):
        super().__init__()
        self.add_import("import dlt")

    def generate(self, action: Action, context: dict) -> str:
        """Generate SQL transform code."""
        # Get SQL query from action
        sql_query = self._get_sql_query(action, context.get("spec_dir"), context)

        # Determine if this creates a view or table
        is_final_target = context.get("is_final_target", False)
        target_table = context.get("target_table")

        # Handle operational metadata
        flowgroup = context.get("flowgroup")
        preset_config = context.get("preset_config", {})
        project_config = context.get("project_config")

        # Initialize operational metadata handler
        operational_metadata = OperationalMetadata(
            project_config=(
                project_config.operational_metadata if project_config else None
            )
        )

        # Update context for substitutions
        if flowgroup:
            operational_metadata.update_context(flowgroup.pipeline, flowgroup.flowgroup)

        # Resolve metadata selection
        selection = operational_metadata.resolve_metadata_selection(
            flowgroup, action, preset_config
        )
        metadata_columns = operational_metadata.get_selected_columns(
            selection or {}, "view"
        )

        # Get required imports for metadata
        metadata_imports = operational_metadata.get_required_imports(metadata_columns)
        for import_stmt in metadata_imports:
            self.add_import(import_stmt)

        template_context = {
            "action_name": action.name,
            "target_view": action.target,
            "sql_query": sql_query,
            "source_refs": self._extract_source_refs(action.source),
            "is_final_target": is_final_target,
            "target_table": target_table,
            "description": action.description or f"SQL transform: {action.name}",
            "add_operational_metadata": bool(metadata_columns),
            "metadata_columns": metadata_columns,
        }

        return self.render_template("transform/sql.py.j2", template_context)

    def _get_sql_query(self, action: Action, spec_dir: Path = None, context: dict = None) -> str:
        """Get SQL query from action configuration."""
        sql_content = None
        
        if action.sql:
            sql_content = action.sql.strip()
        elif action.sql_path:
            sql_file = Path(action.sql_path)
            if not sql_file.is_absolute() and spec_dir:
                sql_file = spec_dir / sql_file

            if not sql_file.exists():
                raise FileNotFoundError(f"SQL file not found: {sql_file}")

            sql_content = sql_file.read_text().strip()
        else:
            raise ValueError(f"SQL transform '{action.name}' must have sql or sql_path")
        
        # Apply substitutions to the SQL content if substitution_manager is available
        if context and "substitution_manager" in context:
            substitution_mgr = context["substitution_manager"]
            sql_content = substitution_mgr._process_string(sql_content)
            
            # Track secret references if they exist
            secret_refs = substitution_mgr.get_secret_references()
            if "secret_references" in context and context["secret_references"] is not None:
                context["secret_references"].update(secret_refs)
        
        return sql_content

    def _extract_source_refs(self, source) -> list:
        """Extract source references for DLT read calls."""
        if isinstance(source, str):
            return [source]
        elif isinstance(source, list):
            return source
        else:
            return []
