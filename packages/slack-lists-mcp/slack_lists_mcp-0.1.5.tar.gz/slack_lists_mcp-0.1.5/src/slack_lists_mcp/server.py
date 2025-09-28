"""FastMCP server for Slack Lists API operations."""

import logging
from typing import Any

import httpx
from fastmcp import Context, FastMCP

from slack_lists_mcp.config import get_settings
from slack_lists_mcp.slack_client import SlackListsClient

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize settings
settings = get_settings()

# Configure logging level from settings
logging.getLogger().setLevel(getattr(logging, settings.log_level.upper()))

# Initialize FastMCP server
mcp = FastMCP(
    name=settings.mcp_server_name,
    version=settings.mcp_server_version,
)

# Initialize Slack client
slack_client = SlackListsClient()


async def fetch_slack_documentation(url: str) -> dict[str, Any]:
    """Slack APIドキュメントをフェッチして解析する。

    Args:
        url: Slack APIドキュメントのURL

    Returns:
        解析されたドキュメント情報

    """
    try:
        async with httpx.AsyncClient(follow_redirects=True) as client:
            response = await client.get(url)
            response.raise_for_status()

            # HTMLコンテンツをそのまま返す（LLMが解析する）
            return {
                "url": str(response.url),  # リダイレクト後の最終URL
                "original_url": url,
                "status_code": response.status_code,
                "content_length": len(response.content),
                "html_content": response.text,
                "message": "ドキュメントが正常に取得されました",
            }
    except Exception as e:
        logger.error(f"ドキュメント取得エラー: {e}")
        return {
            "error": str(e),
            "url": url,
        }


@mcp.tool
async def add_list_item(
    initial_fields: list[dict[str, Any]],
    list_id: str | None = None,
    ctx: Context = None,
) -> dict[str, Any]:
    """Add a new item to a Slack list.

    IMPORTANT: Before using this tool, ALWAYS call get_schema_documentation to understand the correct field formats.
    If you encounter errors, call get_schema_documentation again to verify the correct format.

    Args:
        initial_fields: List of field dictionaries. Each field needs:
                       - column_id: The column ID
                       - Value in appropriate format (rich_text, user, date, select, checkbox, etc.)
        list_id: The ID of the list (optional, uses DEFAULT_LIST_ID env var if not provided)
                 When DEFAULT_LIST_ID is set, you can omit this parameter entirely
        ctx: FastMCP context (automatically injected)

    Returns:
        The created item or error information

    Example:
        initial_fields = [
            {
                "column_id": "Col123",
                "text": "Task Name"  # Plain text will be auto-converted to rich_text
            },
            {
                "column_id": "Col456",
                "checkbox": False
            },
            {
                "column_id": "Col789",
                "select": "OptABC123"  # Single value will be auto-wrapped in array
            },
            {
                "column_id": "Col012",
                "user": "U123456"  # Single user ID will be auto-wrapped in array
            }
        ]

        # Alternative: You can also provide the full rich_text format:
        {
            "column_id": "Col123",
            "rich_text": [{
                "type": "rich_text",
                "elements": [{
                    "type": "rich_text_section",
                    "elements": [{"type": "text", "text": "Task Name"}]
                }]
            }]
        }

    """
    try:
        # Use default list ID from environment if not provided
        if list_id is None:
            list_id = settings.default_list_id
            if list_id is None:
                return {
                    "success": False,
                    "error": "list_id is required. Either provide it as parameter or set DEFAULT_LIST_ID environment variable.",
                }

        if ctx:
            await ctx.info(
                f"Adding item to list {list_id} with {len(initial_fields)} fields",
            )

        result = await slack_client.add_item(
            list_id=list_id,
            initial_fields=initial_fields,
        )

        if ctx:
            await ctx.info(f"Successfully added item to list {list_id}")

        return {
            "success": True,
            "item": result,
        }

    except Exception as e:
        logger.error(f"Error adding item: {e}")
        if ctx:
            await ctx.error(f"Failed to add item: {e!s}")
            await ctx.info(
                "IMPORTANT: If you encounter format errors, call get_schema_documentation to verify the correct field formats before retrying."
            )
        return {
            "success": False,
            "error": str(e),
            "suggestion": "If you encounter format errors, call get_schema_documentation to verify the correct field formats before retrying.",
        }


@mcp.tool
async def update_list_item(
    cells: list[dict[str, Any]],
    list_id: str | None = None,
    ctx: Context = None,
) -> dict[str, Any]:
    """Update items in a Slack list.

    Use get_list_structure first to understand the column IDs and types.

    Args:
        cells: List of cell dictionaries. Each cell needs:
               - row_id: The item ID to update
               - column_id: The column ID
               - Value in appropriate format (rich_text, user, date, select, checkbox, etc.)
        list_id: The ID of the list (optional, uses DEFAULT_LIST_ID env var if not provided)
                 When DEFAULT_LIST_ID is set, you can omit this parameter entirely
        ctx: FastMCP context (automatically injected)

    Returns:
        Success status or error information

    Example:
        cells = [
            {
                "row_id": "Rec123",
                "column_id": "Col123",
                "text": "Updated Name"  # Plain text will be auto-converted to rich_text
            },
            {
                "row_id": "Rec123",
                "column_id": "Col456",
                "checkbox": True
            },
            {
                "row_id": "Rec123",
                "column_id": "Col789",
                "select": "OptXYZ456"  # Single value will be auto-wrapped in array
            },
            {
                "row_id": "Rec123",
                "column_id": "Col012",
                "user": "U789012"  # Single user ID will be auto-wrapped in array
            }
        ]

    """
    try:
        # Use default list ID from environment if not provided
        if list_id is None:
            list_id = settings.default_list_id
            if list_id is None:
                return {
                    "success": False,
                    "error": "list_id is required. Either provide it as parameter or set DEFAULT_LIST_ID environment variable.",
                }

        if ctx:
            await ctx.info(f"Updating items in list {list_id} with {len(cells)} cells")

        result = await slack_client.update_item(
            list_id=list_id,
            cells=cells,
        )

        if ctx:
            await ctx.info(f"Successfully updated items in list {list_id}")

        return result

    except Exception as e:
        logger.error(f"Error updating items: {e}")
        if ctx:
            await ctx.error(f"Failed to update items: {e!s}")
        return {
            "success": False,
            "error": str(e),
        }


@mcp.tool
async def delete_list_item(
    item_id: str,
    list_id: str | None = None,
    ctx: Context = None,
) -> dict[str, Any]:
    """Delete an item from a Slack list.

    Args:
        item_id: The ID of the item to delete
        list_id: The ID of the list containing the item (optional, uses DEFAULT_LIST_ID env var if not provided)
        ctx: FastMCP context (automatically injected)

    Returns:
        Deletion confirmation or error information

    """
    try:
        # Use default list ID from environment if not provided
        if list_id is None:
            list_id = settings.default_list_id
            if list_id is None:
                return {
                    "success": False,
                    "error": "list_id is required. Either provide it as parameter or set DEFAULT_LIST_ID environment variable.",
                }

        if ctx:
            await ctx.info(f"Deleting item {item_id} from list {list_id}")

        await slack_client.delete_item(
            list_id=list_id,
            item_id=item_id,
        )

        if ctx:
            await ctx.info(f"Successfully deleted item {item_id}")

        return {
            "success": True,
            "deleted": True,
            "item_id": item_id,
            "list_id": list_id,
        }

    except Exception as e:
        logger.error(f"Error deleting list item: {e}")
        if ctx:
            await ctx.error(f"Failed to delete item: {e!s}")
        return {
            "success": False,
            "error": str(e),
        }


@mcp.tool
async def get_list_item(
    item_id: str,
    list_id: str | None = None,
    ctx: Context = None,
    include_is_subscribed: bool = False,
) -> dict[str, Any]:
    """Get a specific item from a Slack list.

    Args:
        item_id: The ID of the item to retrieve
        list_id: The ID of the list containing the item (optional, uses DEFAULT_LIST_ID env var if not provided)
        include_is_subscribed: Whether to include subscription status
        ctx: FastMCP context (automatically injected)

    Returns:
        The item data including list metadata and subtasks or error information

    """
    try:
        # Use default list ID from environment if not provided
        if list_id is None:
            list_id = settings.default_list_id
            if list_id is None:
                return {
                    "success": False,
                    "error": "list_id is required. Either provide it as parameter or set DEFAULT_LIST_ID environment variable.",
                }

        if ctx:
            await ctx.info(f"Retrieving item {item_id} from list {list_id}")

        result = await slack_client.get_item(
            list_id=list_id,
            item_id=item_id,
            include_is_subscribed=include_is_subscribed,
        )

        if ctx:
            await ctx.info(f"Successfully retrieved item {item_id}")

        return {
            "success": True,
            "item": result.get("item", {}),
            "list_metadata": result.get("list", {}).get("list_metadata", {}),
            "subtasks": result.get("subtasks", []),
        }

    except Exception as e:
        logger.error(f"Error getting list item: {e}")
        if ctx:
            await ctx.error(f"Failed to get item: {e!s}")
        return {
            "success": False,
            "error": str(e),
        }


@mcp.tool
async def list_items(
    list_id: str | None = None,
    limit: int | None = 100,
    cursor: str | None = None,
    archived: bool | None = None,
    filters: dict[str, dict[str, Any]] | None = None,
    ctx: Context = None,
) -> dict[str, Any]:
    """List all items in a Slack list with optional filtering.

    Args:
        list_id: The ID of the list to retrieve items from (optional, uses DEFAULT_LIST_ID env var if not provided)
        limit: Maximum number of items to return (default: 100)
        cursor: Pagination cursor for next page
        archived: Whether to return archived items (True) or normal items (False/None)
        filters: Column filters. Keys are column IDs or keys, values are filter conditions.
                Example: {
                    "name": {"contains": "タスク"},
                    "Col09HEURLL6A": {"equals": "OptRCQF2AM6"},  # Status filter
                    "todo_completed": {"equals": True},  # Completed filter
                    "Col09H0PTP23Z": {"in": ["U123", "U456"]},  # Assignee filter
                }
                Supported operators: equals, not_equals, contains, not_contains, in, not_in
        ctx: FastMCP context (automatically injected)

    Returns:
        List of items with pagination info or error information

    """
    try:
        # Use default list ID from environment if not provided
        if list_id is None:
            list_id = settings.default_list_id
            if list_id is None:
                return {
                    "success": False,
                    "error": "list_id is required. Either provide it as parameter or set DEFAULT_LIST_ID environment variable.",
                }

        if ctx:
            filter_desc = f" with {len(filters)} filters" if filters else ""
            await ctx.info(f"Listing items from list {list_id}{filter_desc}")

        response = await slack_client.list_items(
            list_id=list_id,
            limit=limit or 100,
            cursor=cursor,
            archived=archived,
            filters=filters,
        )

        if ctx:
            await ctx.info(
                f"Retrieved {len(response.get('items', []))} items from list {list_id}",
            )

        return {
            "success": True,
            "items": response.get("items", []),
            "has_more": response.get("has_more", False),
            "next_cursor": response.get("next_cursor"),
            "total": response.get("total"),
        }

    except Exception as e:
        logger.error(f"Error listing items: {e}")
        if ctx:
            await ctx.error(f"Failed to list items: {e!s}")
        return {
            "success": False,
            "error": str(e),
        }


@mcp.tool
async def get_list_info(
    list_id: str | None = None,
    ctx: Context = None,
) -> dict[str, Any]:
    """Get information about a Slack list.

    Args:
        list_id: The ID of the list (optional, uses DEFAULT_LIST_ID env var if not provided)
        ctx: FastMCP context (automatically injected)

    Returns:
        The list information or error information

    """
    try:
        # Use default list ID from environment if not provided
        if list_id is None:
            list_id = settings.default_list_id
            if list_id is None:
                return {
                    "success": False,
                    "error": "list_id is required. Either provide it as parameter or set DEFAULT_LIST_ID environment variable.",
                }

        if ctx:
            await ctx.info(f"Retrieving information for list {list_id}")

        result = await slack_client.get_list(list_id=list_id)

        if ctx:
            await ctx.info("Successfully retrieved list information")

        return {
            "success": True,
            "list": result,
        }

    except Exception as e:
        logger.error(f"Error getting list info: {e}")
        if ctx:
            await ctx.error(f"Failed to get list info: {e!s}")
        return {
            "success": False,
            "error": str(e),
        }


@mcp.tool
async def get_list_structure(
    list_id: str | None = None,
    ctx: Context = None,
) -> dict[str, Any]:
    """Get the structure and column information of a Slack list.

    Args:
        list_id: The ID of the list (optional, uses DEFAULT_LIST_ID env var if not provided)
        ctx: FastMCP context (automatically injected)

    Returns:
        The list structure including columns and their configurations

    """
    try:
        # Use default list ID from environment if not provided
        if list_id is None:
            list_id = settings.default_list_id
            if list_id is None:
                return {
                    "success": False,
                    "error": "list_id is required. Either provide it as parameter or set DEFAULT_LIST_ID environment variable.",
                }

        if ctx:
            await ctx.info(f"Analyzing structure for list {list_id}")

        # Get list items to find any item ID, then use items.info to get schema
        items_response = await slack_client.list_items(
            list_id=list_id,
            limit=1,  # We just need one item to get the schema
        )

        # If we have any item, use items.info to get the full schema
        if items_response.get("items") and len(items_response["items"]) > 0:
            first_item = items_response["items"][0]
            item_id = first_item.get("id")

            # Get item info which includes list metadata with schema
            item_info_response = await slack_client.get_item(
                list_id=list_id,
                item_id=item_id,
            )

            # Extract schema from list metadata
            list_data = item_info_response.get("list", {})
            list_metadata = list_data.get("list_metadata", {})
            schema = list_metadata.get("schema", [])

            # Build column mapping from schema
            columns = {}
            for column in schema:
                col_id = column.get("id")
                if col_id:
                    columns[col_id] = {
                        "id": col_id,
                        "name": column.get("name"),
                        "key": column.get("key"),
                        "type": column.get("type"),
                        "is_primary": column.get("is_primary_column", False),
                        "options": column.get("options", {}),
                    }

            # Find the name/title column
            name_column = None
            for col_id, col_info in columns.items():
                if col_info.get("is_primary") or col_info.get("key") in [
                    "name",
                    "title",
                    "todo_name",
                ]:
                    name_column = col_id
                    break

            if ctx:
                await ctx.info(f"Found {len(columns)} columns in list schema")

            return {
                "success": True,
                "structure": {
                    "list_id": list_id,
                    "metadata": {
                        "name": list_data.get("name", "Unknown"),
                        "title": list_data.get("title", "Unknown"),
                        "description": list_metadata.get("description", ""),
                    },
                    "schema": schema,
                    "columns": columns,
                    "name_column": name_column,
                    "views": list_metadata.get("views", []),
                    "todo_mode": list_metadata.get("todo_mode", False),
                },
            }
        # No items in the list, try to get basic info
        if ctx:
            await ctx.info("List has no items, returning basic structure")

        return {
            "success": True,
            "structure": {
                "list_id": list_id,
                "message": "List is empty. Add items to see full structure.",
                "columns": {},
            },
        }

    except Exception as e:
        logger.error(f"Error getting list structure: {e}")
        if ctx:
            await ctx.error(f"Failed to get list structure: {e!s}")
        return {
            "success": False,
            "error": str(e),
        }


@mcp.tool
async def get_schema_documentation(
    api_method: str = "slackLists.items.create",
    ctx: Context = None,
) -> dict[str, Any]:
    """Slack Lists APIのスキーマ情報とドキュメントを取得する。

    Args:
        api_method: 取得したいAPIメソッド（例: slackLists.items.create）
        ctx: FastMCP context (automatically injected)

    Returns:
        スキーマ情報とドキュメントの詳細

    """
    try:
        if ctx:
            await ctx.info(f"スキーマ情報を取得中: {api_method}")

        # Slack APIドキュメントのURLを構築
        doc_url = f"https://docs.slack.dev/reference/methods/{api_method}"

        # ドキュメントをフェッチ
        doc_info = await fetch_slack_documentation(doc_url)

        if "error" in doc_info:
            error_msg = f"ドキュメント取得エラー: {doc_info['error']}"
            if ctx:
                await ctx.error(error_msg)
            return {
                "success": False,
                "error": error_msg,
            }

        if ctx:
            await ctx.info("スキーマ情報の取得が完了しました")

        return {
            "success": True,
            "api_method": api_method,
            "documentation_url": doc_info.get("url", doc_url),
            "original_url": doc_info.get("original_url", doc_url),
            "html_content": doc_info.get("html_content", ""),
            "content_length": doc_info.get("content_length", 0),
            "status_code": doc_info.get("status_code", 200),
            "message": "Slack APIドキュメントを取得しました。HTMLコンテンツをLLMが解析してスキーマ情報を抽出できます。",
        }

    except Exception as e:
        logger.error(f"スキーマ情報取得エラー: {e}")
        if ctx:
            await ctx.error(f"スキーマ情報の取得に失敗しました: {e!s}")
        return {
            "success": False,
            "error": str(e),
        }


# Add a resource to show server information
@mcp.resource("resource://server/info")
def get_server_info() -> dict[str, Any]:
    """Provides server configuration and status information."""
    return {
        "name": settings.mcp_server_name,
        "version": settings.mcp_server_version,
        "debug_mode": settings.debug_mode,
        "log_level": settings.log_level,
        "slack_api_timeout": settings.slack_api_timeout,
        "slack_retry_count": settings.slack_retry_count,
        "status": "running",
        "tools": [
            "add_list_item",
            "update_list_item",
            "delete_list_item",
            "get_list_item",
            "list_items",
            "get_list_info",
            "get_list_structure",
            "get_schema_documentation",
        ],
    }


# Add a prompt template for common list operations
@mcp.prompt("list-operations-guide")
def list_operations_guide() -> str:
    """Provides a guide for using Slack Lists operations."""
    return """
# Slack Lists Operations Guide

## IMPORTANT: DEFAULT_LIST_ID is automatically used!
When `DEFAULT_LIST_ID` environment variable is set, you can omit the `list_id` parameter from all tool calls. The system will automatically use the configured default list.

## IMPORTANT: Always start by getting list structure!
Before adding or updating items, use `get_list_structure` to understand the column IDs and types.

## Available Operations:

### 1. Get Schema Documentation
Use `get_schema_documentation` to fetch the latest Slack API documentation.
- Required: api_method (default: "slackLists.items.create")
- Returns: HTML content from Slack API docs that LLM can parse for field types and examples
- This provides the most up-to-date information about field formats

### 2. Get List Structure (REQUIRED FIRST)
Use `get_list_structure` to get column definitions for a list.
- Required: list_id
- Returns: Column IDs, names, types, and options needed for adding/updating items

### 3. Add Item to List
Use `add_list_item` to add a new item with raw field structure.
- Required: initial_fields
- Optional: list_id (uses DEFAULT_LIST_ID if not provided)
- initial_fields: Array of objects with column_id and appropriate value format

Example initial_fields:
```
[
  {
    "column_id": "Col123",
    "rich_text": [{
      "type": "rich_text",
      "elements": [{
        "type": "rich_text_section",
        "elements": [{"type": "text", "text": "Task Name"}]
      }]
    }]
  },
  {
    "column_id": "Col456",
    "user": ["U123456"]
  }
]
```

### 4. Update List Items
Use `update_list_item` to modify items with cell-based updates.
- Required: list_id, cells
- cells: Array of objects with row_id, column_id and appropriate value format

Example cells:
```
[
  {
    "row_id": "Rec123",
    "column_id": "Col123",
    "rich_text": [{
      "type": "rich_text",
      "elements": [{
        "type": "rich_text_section",
        "elements": [{"type": "text", "text": "Updated Task"}]
      }]
    }]
  },
  {
    "row_id": "Rec123",
    "column_id": "Col456",
    "checkbox": true
  }
]
```

### 5. Delete List Item
Use `delete_list_item` to remove an item from a list.
- Required: list_id, item_id

### 6. Get Specific Item
Use `get_list_item` to retrieve details of a specific item.
- Required: list_id, item_id
- Optional: include_is_subscribed
- Returns: item data, list metadata, and subtasks

### 7. List All Items with Filtering
Use `list_items` to retrieve all items in a list with filtering and pagination.
- Required: list_id
- Optional: limit, cursor, archived, filters
- Returns: items array, pagination info

**Filter Examples:**
```json
{
  "name": {"contains": "タスク"},
  "Col09HEURLL6A": {"equals": "OptRCQF2AM6"},
  "todo_completed": {"equals": true},
  "Col09H0PTP23Z": {"in": ["U123", "U456"]}
}
```

**Supported Filter Operators:**
- `equals`: Exact match
- `not_equals`: Not equal to value
- `contains`: Contains substring (case-insensitive)
- `not_contains`: Does not contain substring
- `in`: Value is in the provided list
- `not_in`: Value is not in the provided list

### 8. Get List Information
Use `get_list_info` to retrieve metadata about a list (not items).
- Required: list_id
- Returns: list metadata (name, description, channel, etc.)

## Field Type Formats:
- Text: `rich_text` - Array of rich text blocks
- User: `user` - Array of user IDs
- Date: `date` - Array of date strings (YYYY-MM-DD)
- Select: `select` - Array of option IDs
- Checkbox: `checkbox` - Boolean value
- Number: `number` - Array of numbers
- Email: `email` - Array of email addresses
- Phone: `phone` - Array of phone numbers
- Channel: `channel` - Array of channel IDs
- Rating: `rating` - Array of integers
- Timestamp: `timestamp` - Array of unix timestamps
- Attachment: `attachment` - Array of file IDs
- Link: `link` - Array of link objects with url property
- Reference: `reference` - Array of reference IDs

## Sort Options:
- sort_by: created_at, updated_at, due_date, priority
- sort_order: asc, desc

## Workflow:
1. Get schema documentation to understand field types (optional but recommended)
2. Get list structure to understand columns (omit list_id if DEFAULT_LIST_ID is set)
3. Build initial_fields with proper column_id and format
4. Add items to the list (omit list_id if DEFAULT_LIST_ID is set)
5. Update items using cells with row_id and column_id (omit list_id if DEFAULT_LIST_ID is set)
6. List items with filters to track progress (omit list_id if DEFAULT_LIST_ID is set)

## DEFAULT_LIST_ID Usage:
When DEFAULT_LIST_ID environment variable is configured, you can simplify all tool calls:

```python
# Instead of specifying list_id every time:
add_list_item(list_id="F1234567890", initial_fields=[...])

# You can simply use:
add_list_item(initial_fields=[...])

# Same applies to all other tools:
get_list_structure()  # Uses DEFAULT_LIST_ID
list_items()  # Uses DEFAULT_LIST_ID
update_list_item(cells=[...])  # Uses DEFAULT_LIST_ID
```
"""
