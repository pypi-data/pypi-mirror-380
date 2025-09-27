# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.22.0] - 2025-09-27

### Added

- **Web Workers Support**: Full support for Web Workers with Python function calls
- **Service Workers Support**: Register and manage Service Workers
- **Shared Workers Support**: Create and manage Shared Workers
- **Worker Context Detection**: Automatic detection of worker vs main thread context
- **Worker Python Functions**: Call Python functions directly from workers
- **Worker Management**: Create, terminate, and manage worker instances
- **Cross-Worker Communication**: Seamless communication between workers and main thread

### New Functions

- `eel.createWorker(scriptUrl, options)` - Create a new Web Worker
- `eel.terminateWorker(worker)` - Terminate a specific worker
- `eel.terminateAllWorkers()` - Terminate all workers
- `eel.registerServiceWorker(scriptUrl, options)` - Register a Service Worker
- `eel.unregisterServiceWorker()` - Unregister all Service Workers
- `eel.createSharedWorker(scriptUrl, name)` - Create a Shared Worker
- `eel.isWorker()` - Check if running in worker context
- `eel.isMainThread()` - Check if running in main thread
- `eel.getWorkerCount()` - Get number of active workers

### Technical Details

- Enhanced `eel.js` with worker context detection
- Automatic eel context propagation to workers
- Promise-based worker communication
- Support for all Python functions in worker context
- Message passing system for cross-thread communication

### Examples

```javascript
// Create a worker
const worker = eel.createWorker("worker.js");

// In worker.js - call Python functions
const result = await eel.some_python_function()();

// Service Worker registration
eel.registerServiceWorker("/sw.js");

// Shared Worker
const sharedWorker = eel.createSharedWorker("shared-worker.js", "my-worker");
```

### Breaking Changes

- None (fully backward compatible)

## [0.21.0] - 2025-09-26

### Added

- **External URL Support**: New `external_url` parameter in `eel.start()` function
- **Vite HMR Integration**: Full support for Hot Module Replacement with Vite
- **Modern Development Workflow**: Support for TypeScript, SCSS, PostCSS, and other modern tools
- **WebSocket Server**: Dedicated WebSocket server for Python ↔ JavaScript communication
- **Backward Compatibility**: All existing Eel functionality preserved
- **Enhanced Documentation**: Comprehensive README with examples and troubleshooting
- **PyPI Support**: Full support for `pip` and `uv` package managers
- **Type Hints**: Improved type annotations throughout the codebase

### Changed

- **Architecture**: Modified to support dual-server architecture (external web server + Eel WebSocket server)
- **JavaScript Client**: Updated `eel.js` to handle external URL connections
- **Browser Integration**: Enhanced browser modules to support external URLs
- **Error Handling**: Improved WebSocket error handling and debugging

### Technical Details

- Added `external_url` parameter to `eel.start()` function
- Modified `_start_external_websocket_server()` for external URL mode
- Updated `show()` function to handle external URLs
- Enhanced `browsers.py` to support full URL parsing
- Improved `eel.js` WebSocket connection logic
- Added comprehensive type definitions in `types.py`

### Examples

```python
# Traditional Eel (still works)
import vit3l as eel
eel.init('web')
eel.start('index.html')

# New: External URL mode
import vit3l as eel
eel.init('web')
eel.start('http://localhost:5173', external_url='http://localhost:5173')
```

### Breaking Changes

- None (fully backward compatible)

### Migration Guide

No migration required. Existing code continues to work unchanged.

## [0.18.2] - 2024-12-01

### Original Eel Release

- Base functionality from original Eel project
- Python ↔ JavaScript communication via WebSocket
- Multiple browser support (Chrome, Edge, Electron)
- Static file serving
- Function exposure and calling

---

## Installation

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

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

MIT License - see [LICENSE](LICENSE) file for details.
