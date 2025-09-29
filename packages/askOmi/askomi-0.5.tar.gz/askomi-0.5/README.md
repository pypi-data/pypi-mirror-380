# askOmi

AI-powered HTML response generator with inline and separate file output options.

## Features

- **AI-Powered Responses**: Uses Google's Gemini AI to generate intelligent responses
- **Flexible Output Options**: 
  - Generate responses in separate HTML files
  - Add responses inline to existing HTML files
- **Easy Integration**: Simple Python functions for quick implementation
- **Beautiful Styling**: Professional HTML output with modern CSS

## Installation

```bash
pip install askOmi
```

## Quick Start

```python
from askOmi import askOmi, html, inline_html

# Get AI response as text
response = askOmi("What is Python programming?")

# Generate separate HTML file
html("What is Python programming?")

# Add response to existing file or create new one
inline_html("What is Python programming?", "my_page.html")
```

## Functions

### `askOmi(error)`
Returns AI-generated response as plain text.

**Parameters:**
- `error` (str): Your question or prompt

**Returns:**
- `str`: AI-generated response

### `html(error)`
Creates a separate HTML file (`output.html`) with the AI response.

**Parameters:**
- `error` (str): Your question or prompt

### `inline_html(error, filename="index.html")`
Adds AI response to an existing HTML file or creates a new one.

**Parameters:**
- `error` (str): Your question or prompt
- `filename` (str, optional): Target HTML file (default: "index.html")

**Features:**
- If file doesn't exist: Creates new HTML file with styled layout
- If file exists: Appends styled response to existing content

### `get(error, style="inline")`
Returns HTML content as a string instead of writing to a file. Perfect for using directly in Python code!

**Parameters:**
- `error` (str): Your question or prompt
- `style` (str): "inline" for appending style, "full" for complete HTML document

**Returns:**
- `str`: HTML content as string

### `destroy()`
Cleans up installed packages and generated files.

## Examples

### Basic Usage
```python
from askOmi import askOmi

# Get text response
answer = askOmi("How do I learn programming?")
print(answer)
```

### Generate HTML File
```python
from askOmi import html

# Creates output.html with styled response
html("What are the best programming languages for beginners?")
```

### Inline HTML Generation
```python
from askOmi import inline_html

# Create new file or add to existing one
inline_html("What is machine learning?", "tutorial.html")
inline_html("How does AI work?", "tutorial.html")  # Appends to same file
```

### Get HTML as String (NEW!)
```python
from askOmi import get

# Get HTML content as string (perfect for web apps!)
html_content = get("What is Python programming?", style="inline")

# Use in Flask/Django or any web framework
from flask import render_template_string
template = f'''
<!DOCTYPE html>
<html>
<head><title>My App</title></head>
<body>
    <h1>Welcome</h1>
    {html_content}
</body>
</html>
'''

# Get full HTML document
full_html = get("What is web development?", style="full")
```

## Requirements

- Python 3.8+
- Google Generative AI API key

## API Key Setup

The package uses Google's Gemini AI. Make sure you have a valid API key. The current implementation includes a hardcoded key, but for production use, consider using environment variables:

```python
import os
from askOmi import askOmi

# Set your API key as environment variable
os.environ['GEMINI_API_KEY'] = 'your-api-key-here'
```

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

If you encounter any issues or have questions, please open an issue on GitHub.
