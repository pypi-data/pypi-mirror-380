# COB AI

Python client for the COB SharePoint search API.

## Installation

```bash
pip install cob-ai
```

## Usage

### Basic Search

```python
from cob_ai import COB

# Initialize the client (uses COB_APIKEY environment variable)
client = COB()

# Basic search
results = client.search("your search query")
print(results)
```

### Advanced Search Options

```python
# Search with custom parameters
results = client.search(
    question="prefab wandelementen in de noordtunnel",
    top_n=10,                    # Number of results (default: 8)
    sort="newest_first",         # Sort by date: "newest_first" or "oldest_first"
    show_full_summary=True       # Show both short and full summaries
)

# Access individual results
for result in results.results:
    print(f"Document: {result.filename}")
    print(f"Tunnel: {result.tunnel}")
    print(f"Short summary: {result.short_summary}")
    print(f"Full summary: {result.summary}")
    print(f"NEN Tag: {result.NEN_tag}")
    print(f"Date: {result.date}")
```

### Search Results Format

The search results display includes:
- 📄 Document filename
- Tunnel information, document type, and date
- 📝 Document summary (short or both short + full)
- NEN2767 classification tags
- 📄 **Document bekijken** | 📁 **Map openen** (clickable links)

### Sync Operations

```python
# Start a sync and wait for completion
client.start_sync(wait_for_completion=True)

# Start sync in background
client.start_sync(wait_for_completion=False)

# Check sync status
status = client.status()
print(status)

# Legacy sync method (backward compatibility)
client.sync(wait=True)
```

## Configuration

Configure using environment variables:

- `COB_APIKEY`: Your API key for authentication

Or pass directly to the client:

```python
client = COB(apikey="your-api-key", apiurl="https://custom-api-url.com")
```

## Data Models

### SearchResult
- `doc_id`: Document UUID
- `filename`: Document filename
- `sharepoint_link`: Direct link to document
- `sharepoint_folder_link`: Link to containing folder
- `short_summary`: Brief document summary
- `summary`: Full detailed summary
- `doc_type`: Document type (e.g., "pdf")
- `tunnel`: Tunnel name (e.g., "Noordtunnel")
- `tunnel_object`: Specific tunnel object/component
- `NEN_tag`: NEN2767 classification
- `date`: Document date

### NENTagResponse
- `main_category`: Main NEN classification
- `subcategory`: Optional subcategory

## Requirements

- Python 3.8+
- requests >= 2.25.0
- attrs >= 23.1.0
- python-dotenv

## License

MIT License