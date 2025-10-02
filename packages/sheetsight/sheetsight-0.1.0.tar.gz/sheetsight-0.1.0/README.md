# Sheetsight Python Client

A simple Python client for the [Sheetsight](https://sheetsight.ai) search API.

## Installation

```bash
pip install sheetsight
```

## Quick Start

```python
from sheetsight_py import SheetsightClient

# Initialize client with your API key
client = SheetsightClient(api_key="your_api_key_here")

# Search for ESP32 power consumption information
results = client.search("ESP32 power consumption", max_results=5)

# Print results
print(f"Found {results['total_results']} results across {results['total_parts']} parts")

for group in results['grouped_results']:
    part = group['part']
    manufacturer = group['manufacturer']
    print(f"\n{part['partNumber']} by {manufacturer['displayName']}")
    print(f"Description: {part['description']}")
    print(f"Matches: {group['matchCount']}")

    # Show best match content
    if group['bestMatch']:
        content_preview = group['bestMatch']['content'][:200]
        print(f"Content: {content_preview}...")
```

## API Reference

### SheetsightClient

#### Constructor

```python
SheetsightClient(api_key: str, base_url: Optional[str] = None, timeout: Optional[float] = None)
```

- `api_key`: Your Sheetsight API key (get from [dashboard](https://sheetsight.ai/dashboard))
- `base_url`: Base URL for the API (defaults to `https://sheetsight.ai`)
- `timeout`: Request timeout in seconds (defaults to 30)

#### Methods

##### `search(query, max_results=20, group_by_part=True, **kwargs)`

Convenience method for searching with simplified parameters.

##### `global_search(search_query, options=None)`

Full-featured search method with all available options.

**Options:**

- `maxResults`: Maximum number of results (1-50, default: 20)
- `maxMatchesPerPart`: Maximum matches per part (1-10, default: 3)
- `includePartInfo`: Include part information (default: True)
- `groupByPart`: Group results by part (default: True)

## Context Manager Support

```python
with SheetsightClient(api_key="your_key") as client:
    results = client.search("ESP32")
    # Client automatically closes when exiting context
```

## Error Handling

```python
from sheetsight_py import SheetsightClient, AuthenticationError, APIError

try:
    client = SheetsightClient(api_key="invalid_key")
    results = client.search("ESP32")
except AuthenticationError:
    print("Invalid API key")
except APIError as e:
    print(f"API error: {e}")
```

## License

[MIT](./LICENSE)

## Contributing

Contributions are welcome! Whether it's bug fixes, feature additions, or documentation improvements, we appreciate your help in making this project better. For major changes or new features, please open an issue first to discuss what you would like to change.
