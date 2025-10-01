"""Graph generation for Mouc."""

from __future__ import annotations

from enum import Enum
from typing import TYPE_CHECKING, Any

from . import styling

if TYPE_CHECKING:
    from .models import Entity, FeatureMap


class GraphView(Enum):
    """Types of graph views available."""

    ALL = "all"
    CRITICAL_PATH = "critical-path"
    FILTERED = "filtered"
    TIMELINE = "timeline"
    TIMEFRAME_COLORED = "timeframe-colored"


class GraphGenerator:
    """Generate dependency graphs in DOT format."""

    def __init__(self, feature_map: FeatureMap):
        """Initialize with a feature map."""
        self.feature_map = feature_map
        # Create styling context
        from . import styling

        self.styling_context = styling.create_styling_context(feature_map)

    def generate(
        self,
        view: GraphView = GraphView.ALL,
        target: str | None = None,
        tags: list[str] | None = None,
    ) -> str:
        """Generate a DOT graph based on the specified view."""
        if view == GraphView.ALL:
            return self._generate_all()
        if view == GraphView.CRITICAL_PATH:
            if not target:
                raise ValueError("Critical path view requires a target")
            return self._generate_critical_path(target)
        if view == GraphView.FILTERED:
            if not tags:
                raise ValueError("Filtered view requires tags")
            return self._generate_filtered(tags)
        if view == GraphView.TIMELINE:
            return self._generate_timeline()
        if view == GraphView.TIMEFRAME_COLORED:
            return self._generate_timeframe_colored()
        raise ValueError(f"Unknown view: {view}")

    def _generate_all(self) -> str:
        """Generate a complete graph with all entities."""
        lines = ["digraph FeatureMap {"]
        lines.append("  rankdir=LR;")
        lines.append("  node [shape=oval];")
        lines.append("")

        # Add all entities
        for entity in self.feature_map.entities:
            node_def = self._format_node(entity)
            lines.append(f"  {node_def}")
        lines.append("")

        # Add edges (unblocks direction)
        lines.append("  // Dependencies (unblocks direction)")
        for entity in self.feature_map.entities:
            for dep_id in entity.requires:
                edge_def = self._format_edge(dep_id, entity.id, "requires")
                lines.append(f"  {edge_def}")

        lines.append("}")
        return "\n".join(lines)

    def _generate_critical_path(self, target: str) -> str:
        """Generate a graph showing only the critical path to a target."""
        # Find all dependencies of the target
        dependencies = self._find_all_dependencies(target)
        dependencies.add(target)

        lines = ["digraph CriticalPath {"]
        lines.append("  rankdir=LR;")
        lines.append("  node [shape=oval];")
        lines.append("")

        # Add all nodes in the critical path
        for node_id in dependencies:
            entity = self.feature_map.get_entity_by_id(node_id)
            if not entity:
                continue

            node_def = self._format_node(entity)
            lines.append(f"  {node_def}")

        lines.append("")

        # Add edges only for nodes in the critical path (unblocks direction)
        for entity in self.feature_map.entities:
            if entity.id not in dependencies:
                continue
            for dep_id in entity.requires:
                if dep_id in dependencies:
                    edge_def = self._format_edge(dep_id, entity.id, "requires")
                    lines.append(f"  {edge_def}")

        lines.append("}")
        return "\n".join(lines)

    def _generate_filtered(self, tags: list[str]) -> str:
        """Generate a graph filtered by tags."""
        # Find all entities with matching tags
        matching_ids: set[str] = set()

        for entity in self.feature_map.entities:
            if any(tag in entity.tags for tag in tags):
                matching_ids.add(entity.id)

        # Also include direct dependencies/dependents
        expanded_ids: set[str] = matching_ids.copy()
        for node_id in matching_ids:
            expanded_ids.update(self._find_direct_connections(node_id))

        lines = ["digraph FilteredView {"]
        lines.append("  rankdir=LR;")
        lines.append("  node [shape=oval];")
        lines.append("")

        # Add nodes
        for node_id in expanded_ids:
            entity = self.feature_map.get_entity_by_id(node_id)
            if not entity:
                continue

            node_def = self._format_node(entity)
            lines.append(f"  {node_def}")

        lines.append("")

        # Add edges (unblocks direction)
        for entity in self.feature_map.entities:
            if entity.id not in expanded_ids:
                continue
            for dep_id in entity.requires:
                if dep_id in expanded_ids:
                    edge_def = self._format_edge(dep_id, entity.id, "requires")
                    lines.append(f"  {edge_def}")

        lines.append("}")
        return "\n".join(lines)

    def _find_all_dependencies(self, target: str) -> set[str]:
        """Find all transitive dependencies of a target."""
        dependencies: set[str] = set()
        to_process = [target]

        while to_process:
            current = to_process.pop()

            entity = self.feature_map.get_entity_by_id(current)
            if entity:
                for dep_id in entity.requires:
                    if dep_id not in dependencies:
                        dependencies.add(dep_id)
                        to_process.append(dep_id)

        return dependencies

    def _find_direct_connections(self, node_id: str) -> set[str]:
        """Find direct dependencies and dependents of a node."""
        connections: set[str] = set()

        # Find the entity and add its dependencies and dependents
        entity = self.feature_map.get_entity_by_id(node_id)
        if entity:
            connections.update(entity.requires)
            connections.update(entity.enables)

        return connections

    def _escape_label(self, label: str) -> str:
        """Escape special characters in DOT labels."""
        return label.replace('"', '\\"').replace("\n", "\\n")

    def _format_node(self, entity: Entity, override_style: dict[str, Any] | None = None) -> str:
        """Format a node with styling applied."""
        from . import styling

        label = self._escape_label(entity.name)

        # Get default style based on entity type
        default_style = self._get_default_node_style(entity)

        # Apply override style if provided (for view-specific styling)
        if override_style:
            default_style.update(override_style)

        # Apply user styling
        user_style = styling.apply_node_styles(entity, self.styling_context)

        # Merge styles (user overrides default)
        final_style = {**default_style, **user_style}

        # Build attribute string
        attrs = [f'label="{label}"']
        if "shape" in final_style:
            attrs.append(f"shape={final_style['shape']}")
        if "fill_color" in final_style:
            attrs.append("style=filled")
            attrs.append(f'fillcolor="{final_style["fill_color"]}"')
        if "text_color" in final_style:
            attrs.append(f'fontcolor="{final_style["text_color"]}"')
        if "border_color" in final_style:
            attrs.append(f'color="{final_style["border_color"]}"')
        if "border_width" in final_style:
            attrs.append(f"penwidth={final_style['border_width']}")
        if "fontsize" in final_style:
            attrs.append(f"fontsize={final_style['fontsize']}")
        if "fontname" in final_style:
            attrs.append(f'fontname="{final_style["fontname"]}"')

        return f"{entity.id} [{', '.join(attrs)}];"

    def _format_edge(self, from_id: str, to_id: str, edge_type: str) -> str:
        """Format an edge with styling applied."""
        from . import styling

        # Apply user styling
        user_style = styling.apply_edge_styles(from_id, to_id, edge_type, self.styling_context)

        # Build attribute string
        attrs: list[str] = []
        if "color" in user_style:
            attrs.append(f'color="{user_style["color"]}"')
        if "style" in user_style:
            attrs.append(f"style={user_style['style']}")
        if "penwidth" in user_style:
            attrs.append(f"penwidth={user_style['penwidth']}")
        if "arrowhead" in user_style:
            attrs.append(f"arrowhead={user_style['arrowhead']}")

        if attrs:
            return f"{from_id} -> {to_id} [{', '.join(attrs)}];"
        return f"{from_id} -> {to_id};"

    def _get_default_node_style(self, entity: Entity) -> dict[str, Any]:
        """Get default style for an entity based on type."""
        # Default colors by type
        color_map = {
            "capability": "lightblue",
            "user_story": "lightgreen",
            "outcome": "lightyellow",
        }

        return {"shape": "oval", "fill_color": color_map.get(entity.type, "white")}

    def _generate_timeline(self) -> str:
        """Generate a timeline graph grouped by timeframe."""
        # Group entities by timeframe
        timeframe_groups: dict[str, list[Entity]] = {}
        unscheduled: list[Entity] = []

        for entity in self.feature_map.entities:
            timeframe = entity.meta.get("timeframe")
            if timeframe:
                if timeframe not in timeframe_groups:
                    timeframe_groups[timeframe] = []
                timeframe_groups[timeframe].append(entity)
            else:
                unscheduled.append(entity)

        # Sort timeframes for consistent ordering
        sorted_timeframes = sorted(timeframe_groups.keys())

        lines = ["digraph Timeline {"]
        lines.append("  rankdir=LR;")
        lines.append("  node [shape=oval];")
        lines.append("")

        # Create subgraph clusters for each timeframe
        cluster_idx = 0
        for timeframe in sorted_timeframes:
            lines.append(f"  subgraph cluster_{cluster_idx} {{")
            lines.append(f'    label="{self._escape_label(timeframe)}";')
            lines.append("    style=filled;")
            lines.append("    fillcolor=lightgrey;")
            lines.append("")

            # Add entities in this timeframe
            for entity in timeframe_groups[timeframe]:
                node_def = self._format_node(entity)
                lines.append(f"    {node_def}")

            lines.append("  }")
            lines.append("")
            cluster_idx += 1

        # Add unscheduled entities if any
        if unscheduled:
            lines.append(f"  subgraph cluster_{cluster_idx} {{")
            lines.append('    label="Unscheduled";')
            lines.append("    style=dashed;")
            lines.append("")

            for entity in unscheduled:
                node_def = self._format_node(entity)
                lines.append(f"    {node_def}")

            lines.append("  }")
            lines.append("")

        # Add all edges (dependencies)
        lines.append("  // Dependencies")
        for entity in self.feature_map.entities:
            for dep_id in entity.requires:
                edge_def = self._format_edge(dep_id, entity.id, "requires")
                lines.append(f"  {edge_def}")

        lines.append("}")
        return "\n".join(lines)

    def _generate_timeframe_colored(self) -> str:
        """Generate a graph where node colors represent timeframes."""
        # Group entities by timeframe
        timeframe_groups: dict[str, list[Entity]] = {}
        unscheduled: list[Entity] = []

        for entity in self.feature_map.entities:
            timeframe = entity.meta.get("timeframe")
            if timeframe:
                if timeframe not in timeframe_groups:
                    timeframe_groups[timeframe] = []
                timeframe_groups[timeframe].append(entity)
            else:
                unscheduled.append(entity)

        # Sort timeframes for consistent ordering
        sorted_timeframes = sorted(timeframe_groups.keys())

        # Build a map of entity ID to color using sequential_hue
        entity_colors: dict[str, str] = {}
        for timeframe in sorted_timeframes:
            color = styling.sequential_hue(
                timeframe, sorted_timeframes, hue_range=(120, 230), lightness_range=(95, 70)
            )
            for entity in timeframe_groups[timeframe]:
                entity_colors[entity.id] = color

        # Unscheduled entities get gray
        for entity in unscheduled:
            entity_colors[entity.id] = "lightgray"

        lines = ["digraph TimeframeColored {"]
        lines.append("  rankdir=LR;")
        lines.append("  node [shape=oval];")
        lines.append("")

        # Add all nodes with colors based on timeframe
        for entity in self.feature_map.entities:
            color = entity_colors.get(entity.id, "white")
            node_def = self._format_node(entity, override_style={"fill_color": color})
            lines.append(f"  {node_def}")

        lines.append("")

        # Add edges (unblocks direction)
        lines.append("  // Dependencies")
        for entity in self.feature_map.entities:
            for dep_id in entity.requires:
                edge_def = self._format_edge(dep_id, entity.id, "requires")
                lines.append(f"  {edge_def}")

        lines.append("}")
        return "\n".join(lines)
