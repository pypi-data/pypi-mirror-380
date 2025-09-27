# infcraft

A simple and lightweight Python wrapper for the unofficial `infiniteback.org` API, used for the game Infinite Craft.

## Installation

Install the package directly from PyPI:

```bash
pip install infcraft
```

## Usage

The module provides a single function, `pair`, which takes two elements and returns the crafted result.

```python
import infcraft

try:
    # Combine two elements
    result = infcraft.pair("Water", "Fire")
    
    if result:
        print(f"Result: {result.name}")
        print(f"Emoji: {result.emoji}")

    # Example 2
    steam = infcraft.pair("Water", "Fire")
    engine = infcraft.pair(steam.name, "Fire")
    
    if engine:
        print(f"Crafted '{engine.name}' {engine.emoji}")

except infcraft.InfCraftError as e:
    print(f"An API error occurred: {e}")

```

The `pair` function returns a `CraftResult` object which has two attributes: `.name` and `.emoji`.

## Error Handling

The module will raise an `infcraft.InfCraftError` if there is a network problem, an HTTP error status code, or if the API returns an invalid response.

