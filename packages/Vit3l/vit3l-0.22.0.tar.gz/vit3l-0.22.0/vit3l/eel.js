eel = {
  _host: window.location.origin,
  _isWorker:
    typeof WorkerGlobalScope !== "undefined" &&
    self instanceof WorkerGlobalScope,
  _workerInstances: new Set(),
  _workerMessageHandlers: new Map(),

  set_host: function (hostname) {
    eel._host = hostname;
  },

  // Worker support functions
  createWorker: function (scriptUrl, options = {}) {
    const worker = new Worker(scriptUrl, options);
    eel._workerInstances.add(worker);

    // Set up message handling for the worker
    worker.addEventListener("message", function (event) {
      eel._handleWorkerMessage(worker, event.data);
    });

    // Send eel context to worker
    worker.postMessage({
      type: "eel_init",
      eelContext: {
        _host: eel._host,
        _py_functions: eel._py_functions,
        _start_geometry: eel._start_geometry,
      },
    });

    return worker;
  },

  terminateWorker: function (worker) {
    if (eel._workerInstances.has(worker)) {
      eel._workerInstances.delete(worker);
      worker.terminate();
    }
  },

  terminateAllWorkers: function () {
    eel._workerInstances.forEach((worker) => {
      worker.terminate();
    });
    eel._workerInstances.clear();
  },

  _handleWorkerMessage: function (worker, data) {
    if (data.type === "eel_call") {
      // Handle function call from worker
      const { callId, functionName, args } = data;
      if (eel._py_functions && eel._py_functions.includes(functionName)) {
        try {
          // Call the Python function through the main thread
          if (typeof eel[functionName] === "function") {
            eel[functionName](...args)(
              (result) => {
                worker.postMessage({
                  type: "eel_response",
                  callId: callId,
                  result: result,
                  success: true,
                });
              },
              (error) => {
                worker.postMessage({
                  type: "eel_response",
                  callId: callId,
                  error: error.message || error,
                  success: false,
                });
              }
            );
          } else {
            throw new Error(`Function ${functionName} not available`);
          }
        } catch (error) {
          worker.postMessage({
            type: "eel_response",
            callId: callId,
            error: error.message || error,
            success: false,
          });
        }
      } else {
        worker.postMessage({
          type: "eel_response",
          callId: callId,
          error: `Function ${functionName} not found in Python functions`,
          success: false,
        });
      }
    }
  },

  // Worker-side eel functions (for use inside workers)
  _workerEel: null,
  _workerCallbacks: new Map(),
  _workerCallId: 0,

  _initWorkerEel: function (eelContext) {
    eel._workerEel = {
      _host: eelContext._host,
      _py_functions: eelContext._py_functions,
      _start_geometry: eelContext._start_geometry,
      _exposed_functions: {},
      _callbacks: new Map(),
      _callId: 0,
    };

    // Set up message handling for worker
    self.addEventListener("message", function (event) {
      const data = event.data;
      if (data.type === "eel_init") {
        eel._initWorkerEel(data.eelContext);
      } else if (data.type === "eel_response") {
        eel._handleWorkerResponse(data);
      }
    });
  },

  _handleWorkerResponse: function (data) {
    const { callId, result, error, success } = data;
    if (eel._workerCallbacks.has(callId)) {
      const callback = eel._workerCallbacks.get(callId);
      eel._workerCallbacks.delete(callId);

      if (success) {
        callback.resolve(result);
      } else {
        callback.reject(new Error(error));
      }
    }
  },

  // Expose functions for worker context
  expose: function (f, name) {
    if (eel._isWorker && eel._workerEel) {
      // In worker context
      if (name === undefined) {
        name = f.toString();
        let i = "function ".length,
          j = name.indexOf("(");
        name = name.substring(i, j).trim();
      }
      eel._workerEel._exposed_functions[name] = f;
    } else {
      // In main context
      if (name === undefined) {
        name = f.toString();
        let i = "function ".length,
          j = name.indexOf("(");
        name = name.substring(i, j).trim();
      }
      eel._exposed_functions[name] = f;
    }
  },

  // Worker-specific functions for calling Python from workers
  _workerCallPython: function (functionName, args = []) {
    if (!eel._isWorker || !eel._workerEel) {
      throw new Error("This function can only be called from a Web Worker");
    }

    const callId = ++eel._workerCallId;
    return new Promise((resolve, reject) => {
      eel._workerCallbacks.set(callId, { resolve, reject });

      // Send message to main thread
      self.postMessage({
        type: "eel_call",
        callId: callId,
        functionName: functionName,
        args: args,
      });
    });
  },

  // Create worker-specific Python function calls
  _createWorkerPythonFunction: function (functionName) {
    return function (...args) {
      return eel._workerCallPython(functionName, args);
    };
  },

  guid: function () {
    return eel._guid;
  },

  // These get dynamically added by library when file is served
  /** _py_functions **/
  /** _start_geometry **/

  _guid: ([1e7] + -1e3 + -4e3 + -8e3 + -1e11).replace(/[018]/g, (c) =>
    (
      c ^
      (crypto.getRandomValues(new Uint8Array(1))[0] & (15 >> (c / 4)))
    ).toString(16)
  ),

  _exposed_functions: {},

  _mock_queue: [],

  _start_geometry: {
    // Initialize with default geometry
    default: {
      size: null,
      position: null,
    },
    pages: {},
  },

  _mock_py_functions: function () {
    if (!eel._py_functions || eel._py_functions.length === 0) {
      return; // No Python functions available yet
    }

    for (let i = 0; i < eel._py_functions.length; i++) {
      let name = eel._py_functions[i];
      if (eel._isWorker && eel._workerEel) {
        // In worker context, create worker-specific function
        eel[name] = eel._createWorkerPythonFunction(name);
      } else {
        // In main context, use original logic
        eel[name] = function () {
          let call_object = eel._call_object(name, arguments);
          eel._mock_queue.push(call_object);
          return eel._call_return(call_object);
        };
      }
    }
  },

  _import_py_function: function (name) {
    let func_name = name;
    if (eel._isWorker && eel._workerEel) {
      // In worker context, create worker-specific function
      eel[name] = eel._createWorkerPythonFunction(name);
    } else {
      // In main context, use original logic
      eel[name] = function () {
        let call_object = eel._call_object(func_name, arguments);
        if (eel._websocket && eel._websocket.readyState === WebSocket.OPEN) {
          eel._websocket.send(eel._toJSON(call_object));
        } else {
          // WebSocket not ready, add to mock queue
          eel._mock_queue.push(call_object);
        }
        return eel._call_return(call_object);
      };
    }
  },

  _call_number: 0,

  _call_return_callbacks: {},

  _call_object: function (name, args) {
    let arg_array = [];
    for (let i = 0; i < args.length; i++) {
      arg_array.push(args[i]);
    }

    let call_id = (eel._call_number += 1) + Math.random();
    return { call: call_id, name: name, args: arg_array };
  },

  _sleep: function (ms) {
    return new Promise((resolve) => setTimeout(resolve, ms));
  },

  _toJSON: function (obj) {
    return JSON.stringify(obj, (k, v) => (v === undefined ? null : v));
  },

  _call_return: function (call) {
    return function (callback = null) {
      if (callback != null) {
        eel._call_return_callbacks[call.call] = { resolve: callback };
      } else {
        return new Promise(function (resolve, reject) {
          eel._call_return_callbacks[call.call] = {
            resolve: resolve,
            reject: reject,
          };
        });
      }
    };
  },

  _position_window: function (page) {
    if (!eel._start_geometry || !eel._start_geometry["default"]) {
      return; // No geometry data available
    }

    let size = eel._start_geometry["default"].size;
    let position = eel._start_geometry["default"].position;

    if (eel._start_geometry.pages && page in eel._start_geometry.pages) {
      size = eel._start_geometry.pages[page].size;
      position = eel._start_geometry.pages[page].position;
    }

    if (size != null) {
      window.resizeTo(size[0], size[1]);
    }

    if (position != null) {
      window.moveTo(position[0], position[1]);
    }
  },

  _init: function () {
    // Try to initialize Python functions, but don't fail if they're not ready yet
    eel._mock_py_functions();

    // Check if we're in a worker context
    if (eel._isWorker) {
      // In worker, wait for initialization message
      self.addEventListener("message", function (event) {
        const data = event.data;
        if (data.type === "eel_init") {
          eel._initWorkerEel(data.eelContext);
        } else if (data.type === "eel_response") {
          eel._handleWorkerResponse(data);
        }
      });
      return;
    }

    // Main thread initialization
    document.addEventListener("DOMContentLoaded", function (event) {
      let page = window.location.pathname.substring(1);
      eel._position_window(page);

      // Determine WebSocket address based on current host
      let websocket_addr;
      if (eel._host === window.location.origin) {
        // Normal mode - use current host
        websocket_addr = (eel._host + "/eel").replace("http", "ws");
      } else {
        // External URL mode - use the configured host (Eel WebSocket server)
        websocket_addr = (eel._host + "/eel").replace("http", "ws");
      }
      websocket_addr += "?page=" + page;
      console.log("Connecting to WebSocket:", websocket_addr);
      eel._websocket = new WebSocket(websocket_addr);

      eel._websocket.onopen = function () {
        console.log("WebSocket connected successfully");

        // Re-initialize Python functions now that we have the connection
        eel._mock_py_functions();

        for (let i = 0; i < eel._py_functions.length; i++) {
          let py_function = eel._py_functions[i];
          eel._import_py_function(py_function);
        }

        while (eel._mock_queue.length > 0) {
          let call = eel._mock_queue.shift();
          eel._websocket.send(eel._toJSON(call));
        }
      };

      eel._websocket.onerror = function (error) {
        console.error("WebSocket error:", error);
      };

      eel._websocket.onclose = function (event) {
        console.log("WebSocket closed:", event.code, event.reason);
      };

      eel._websocket.onmessage = function (e) {
        let message = JSON.parse(e.data);
        if (message.hasOwnProperty("call")) {
          // Python making a function call into us
          if (message.name in eel._exposed_functions) {
            try {
              let return_val = eel._exposed_functions[message.name](
                ...message.args
              );
              eel._websocket.send(
                eel._toJSON({
                  return: message.call,
                  status: "ok",
                  value: return_val,
                })
              );
            } catch (err) {
              debugger;
              eel._websocket.send(
                eel._toJSON({
                  return: message.call,
                  status: "error",
                  error: err.message,
                  stack: err.stack,
                })
              );
            }
          }
        } else if (message.hasOwnProperty("return")) {
          // Python returning a value to us
          if (message["return"] in eel._call_return_callbacks) {
            if (message["status"] === "ok") {
              eel._call_return_callbacks[message["return"]].resolve(
                message.value
              );
            } else if (
              message["status"] === "error" &&
              eel._call_return_callbacks[message["return"]].reject
            ) {
              eel._call_return_callbacks[message["return"]].reject(
                message["error"]
              );
            }
          }
        } else {
          throw "Invalid message " + message;
        }
      };
    });
  },

  // Service Worker support
  registerServiceWorker: function (scriptUrl, options = {}) {
    if ("serviceWorker" in navigator) {
      return navigator.serviceWorker
        .register(scriptUrl, options)
        .then(function (registration) {
          console.log("Service Worker registered successfully:", registration);
          return registration;
        })
        .catch(function (error) {
          console.error("Service Worker registration failed:", error);
          throw error;
        });
    } else {
      throw new Error("Service Workers are not supported in this browser");
    }
  },

  unregisterServiceWorker: function () {
    if ("serviceWorker" in navigator) {
      return navigator.serviceWorker
        .getRegistrations()
        .then(function (registrations) {
          return Promise.all(
            registrations.map((registration) => registration.unregister())
          );
        });
    }
  },

  // Shared Worker support
  createSharedWorker: function (scriptUrl, name = "") {
    if (typeof SharedWorker !== "undefined") {
      const worker = new SharedWorker(scriptUrl, name);
      eel._workerInstances.add(worker.port);

      // Set up message handling for the shared worker
      worker.port.addEventListener("message", function (event) {
        eel._handleWorkerMessage(worker.port, event.data);
      });

      // Send eel context to shared worker
      worker.port.postMessage({
        type: "eel_init",
        eelContext: {
          _host: eel._host,
          _py_functions: eel._py_functions,
          _start_geometry: eel._start_geometry,
        },
      });

      return worker;
    } else {
      throw new Error("Shared Workers are not supported in this browser");
    }
  },

  // Utility functions for workers
  isWorker: function () {
    return eel._isWorker;
  },

  isMainThread: function () {
    return !eel._isWorker;
  },

  getWorkerCount: function () {
    return eel._workerInstances.size;
  },
};

eel._init();

if (typeof require !== "undefined") {
  // Avoid name collisions when using Electron, so jQuery etc work normally
  window.nodeRequire = require;
  delete window.require;
  delete window.exports;
  delete window.module;
}
