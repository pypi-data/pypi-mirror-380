"""Network request monitoring and display commands."""

from typing import List

from webtap.app import app
from webtap.commands._errors import check_connection
from webtap.commands._tips import get_tips


@app.command(
    display="markdown",
    truncate={"ReqID": {"max": 12, "mode": "end"}, "URL": {"max": 60, "mode": "middle"}},
    transforms={"Size": "format_size"},
    fastmcp=[{"type": "resource", "mime_type": "application/json"}, {"type": "tool"}],
)
def network(state, limit: int = 20, filters: List[str] = None, no_filters: bool = False) -> dict:  # pyright: ignore[reportArgumentType]
    """Show network requests with full data.

    As Resource (no parameters):
        network             # Returns last 20 requests with enabled filters

    As Tool (with parameters):
        network(limit=50)                    # More results
        network(filters=["ads"])            # Specific filter only
        network(no_filters=True, limit=50)  # Everything unfiltered

    Args:
        limit: Maximum results to show (default: 20)
        filters: Specific filter categories to apply
        no_filters: Show everything unfiltered (default: False)

    Returns:
        Table of network requests with full data
    """
    # Check connection
    if error := check_connection(state):
        return error

    # Get filter SQL from service
    if no_filters:
        filter_sql = ""
    elif filters:
        filter_sql = state.service.filters.get_filter_sql(use_all=False, categories=filters)
    else:
        filter_sql = state.service.filters.get_filter_sql(use_all=True)

    # Get data from service
    results = state.service.network.get_recent_requests(limit=limit, filter_sql=filter_sql)

    # Build rows with FULL data
    rows = []
    for row in results:
        rowid, request_id, method, status, url, type_val, size = row
        rows.append(
            {
                "ID": str(rowid),
                "ReqID": request_id or "",  # Full request ID
                "Method": method or "GET",
                "Status": str(status) if status else "-",
                "URL": url or "",  # Full URL
                "Type": type_val or "-",
                "Size": size or 0,  # Raw bytes
            }
        )

    # Build response with developer guidance
    warnings = []
    if limit and len(results) == limit:
        warnings.append(f"Showing first {limit} results (use limit parameter to see more)")

    # Get tips from TIPS.md with context
    tips = None
    if rows:
        example_id = rows[0]["ID"]
        tips = get_tips("network", context={"id": example_id})

    # Build response elements manually to add filter tip
    elements = []
    elements.append({"type": "heading", "content": "Network Requests", "level": 2})

    for warning in warnings or []:
        elements.append({"type": "alert", "message": warning, "level": "warning"})

    if rows:
        elements.append(
            {"type": "table", "headers": ["ID", "ReqID", "Method", "Status", "URL", "Type", "Size"], "rows": rows}
        )
    else:
        elements.append({"type": "text", "content": "_No data available_"})

    if f"{len(rows)} requests":
        elements.append({"type": "text", "content": f"_{len(rows)} requests_"})

    # Always show filter tip demonstrating both type AND domain filtering
    elements.append(
        {
            "type": "alert",
            "message": "Tip: Reduce noise with filters by type or domain. Example: `filters('update', {'category': 'api-only', 'mode': 'include', 'types': ['XHR', 'Fetch'], 'domains': ['*/api/*', '*/graphql/*']})`",
            "level": "info",
        }
    )

    if tips:
        elements.append({"type": "heading", "content": "Next Steps", "level": 3})
        elements.append({"type": "list", "items": tips})

    return {"elements": elements}
