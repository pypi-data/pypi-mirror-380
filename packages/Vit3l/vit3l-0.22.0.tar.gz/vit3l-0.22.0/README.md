# Vit3l

[![PyPI version](https://img.shields.io/pypi/v/Vit3l?style=for-the-badge)](https://pypi.org/project/Vit3l/)
[![PyPI Downloads](https://img.shields.io/pypi/dm/Vit3l?style=for-the-badge)](https://pypistats.org/packages/vit3l)
![Python](https://img.shields.io/pypi/pyversions/Vit3l?style=for-the-badge)
[![License](https://img.shields.io/pypi/l/Vit3l.svg?style=for-the-badge)](https://pypi.org/project/Vit3l/)

**Vit3l** is a fork of [Eel](https://github.com/python-eel/Eel) that adds support for external web servers, enabling modern development workflows with Vite HMR (Hot Module Replacement).

## What's New

- **External URL Support**: Connect to any external web server (Vite, Webpack, etc.)
- **Vite HMR**: Full support for Hot Module Replacement
- **Modern Development**: Use TypeScript, SCSS, PostCSS, and other modern tools
- **Backward Compatible**: All existing Eel functionality preserved
- **WebSocket Communication**: Python ↔ JavaScript communication via WebSocket

## 📦 Installation

### Using pip

```bash
pip install Vit3l
```

### Using uv (recommended)

```bash
uv add Vit3l
```

### With Jinja2 templates

```bash
pip install Vit3l[jinja2]
# or
uv add "Vit3l[jinja2]"
```

## 🎯 Quick Start

### Traditional Eel (still works)

```python
import vit3l as eel

eel.init('web')
eel.start('index.html')  # Runs on localhost:8000
```

### New: External URL Mode

```python
import vit3l as eel

@eel.expose
def say_hello(name):
    return f'Hello {name}!'

eel.init('web')
eel.start('http://localhost:5173', external_url='http://localhost:5173')
```

### JavaScript (same as Eel)

```javascript
const result = await eel.say_hello("World")();
console.log(result); // "Hello World!"
```

## Vite Integration

### 1. Setup Vite project

```bash
npm create vite@latest my-eel-app
cd my-eel-app
npm install
```

### 2. Configure Vite (`vite.config.js`)

```javascript
import { defineConfig } from "vite";

export default defineConfig({
  server: {
    port: 5173,
    cors: true,
  },
});
```

### 3. Add Eel to HTML

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Vite + Vit3l</title>
  </head>
  <body>
    <h1>Hello from Vite + Vit3l!</h1>
    <button onclick="callPython()">Call Python</button>

    <!-- Connect to Eel WebSocket server -->
    <script src="http://localhost:8000/eel.js"></script>
    <script>
      function callPython() {
        eel.say_hello("from Vite!")();
      }
    </script>
  </body>
</html>
```

### 4. Python script

```python
import vit3l as eel

@eel.expose
def say_hello(message):
    print(f"Hello {message}")
    return f"Python received: {message}"

eel.init('src')  # Your Vite source folder
eel.start('http://localhost:5173', external_url='http://localhost:5173')
```

### 5. Run both servers

```bash
# Terminal 1: Vite dev server
npm run dev

# Terminal 2: Python script
python app.py
```

### Examples

```python
# External URL with custom settings
eel.start(
    'http://localhost:5173',
    external_url='http://localhost:5173',
    mode='chrome',
    port=8000,
    block=True
)

# Multiple URLs
eel.start(
    'http://localhost:5173',
    'http://localhost:3000',
    external_url='http://localhost:5173'
)
```

### External URL Mode

1. **Vite Server**: Serves static files with HMR on port 5173
2. **Eel WebSocket Server**: Runs on port 8000 for Python ↔ JavaScript communication
3. **Browser**: Connects to both servers
4. **Result**: Modern development with full Eel functionality

## Troubleshooting

### WebSocket Connection Issues

```javascript
// Check WebSocket status in browser console
console.log("WebSocket state:", eel._websocket.readyState);
// 0 = CONNECTING, 1 = OPEN, 2 = CLOSING, 3 = CLOSED
```

### CORS Errors

Ensure Vite is configured with CORS enabled:

```javascript
// vite.config.js
export default defineConfig({
  server: {
    cors: true,
  },
});
```

### Port Conflicts

Change Eel WebSocket port if 8000 is occupied:

```python
eel.start('http://localhost:5173', external_url='http://localhost:5173', port=8001)
```

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Acknowledgments

- Original [Eel](https://github.com/python-eel/Eel) project by Chris Knott
