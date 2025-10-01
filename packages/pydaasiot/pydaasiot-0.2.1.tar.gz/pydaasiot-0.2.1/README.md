# pydaasiot

[![PyPI version](https://img.shields.io/pypi/v/pydaasiot.svg)](https://pypi.org/project/pydaasiot/)
[![Python versions](https://img.shields.io/pypi/pyversions/pydaasiot.svg)](https://pypi.org/project/pydaasiot/)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux-blue.svg)](#-supported-platforms)
[![License](https://img.shields.io/pypi/l/pydaasiot.svg)](LICENSE)

**pydaasiot** are the official Python bindings for the **DaaS‑IoT SDK**.  
They expose the full power of the Device‑as‑a‑Service paradigm directly into Python, making it easy to integrate IoT communication primitives, overlay networking and time synchronization into Python applications.

---

## 🌐 Overview

The **DaaS‑IoT SDK** is a high‑performance library designed for distributed IoT environments.  
It provides an overlay communication model on top of TCP/IP, with support for multiple drivers and precise ATS (Accurate Time Synchronization) mechanisms.

The Python package `pydaasiot` allows developers and researchers to access these capabilities without writing C++ code, simplifying prototyping and integration into data pipelines, experiments and services.

---

## ✨ Main Features

- Initialization and management of **DaaS‑IoT nodes**.
- Add and configure network drivers (currently **INET4** and **Bluetooth**; more drivers such as Serial, USB, UART, MQTT are planned).  
- Send and receive packets between devices.  
- Retrieve and manage ATS synchronization parameters.  
- Cross‑platform: distributed as prebuilt wheels for **Windows (MSVC)** and **Linux (manylinux2014)**.  

---

## 🚀 Installation

Install from PyPI with:

```bash
pip install pydaasiot
```

Wheels are available for Python 3.9 – 3.12.  
`pip` will automatically choose the correct wheel for your OS and Python version.

---

## 🧪 Quick Example

```python
import pydaasiot

# Initialize a DaaS-IoT node
node = pydaasiot.Node()
node.init()

# Add a network driver (example: IPv4 link)
node.add_driver(2, "127.0.0.1:5000")

# Send a packet
node.push(b"Hello from Python")

# Receive packets (non-blocking)
packets = node.pull()
print("Received:", packets)

# Access ATS parameters
ats = node.get_sync_params()
print("ATS:", ats)
```

---

## 🖥️ Supported Platforms

- **Windows** (x86_64, MSVC)
- **Linux** (x86_64, manylinux2014)

macOS support is planned for a future release.

---

## 📚 Documentation

- Full SDK documentation: [GitHub repository](https://github.com/your-org/pydaasiot)  
- Examples: available in the repository under `examples/` (not included in the PyPI package).  

---

## 🔧 Development

Development is organized into feature branches for specific platforms.  
The `main` branch is cross‑platform and serves as the source for official PyPI releases.  
Tagged versions (`vX.Y.Z`) trigger CI pipelines that build wheels for Windows and Linux and publish them to PyPI.

---

## 🤝 Contributing

Contributions are welcome! Please use GitHub issues and pull requests to propose improvements or report bugs.

---

## 📄 License

Released under the terms of the **MIT License**.  
See the [LICENSE](LICENSE) file for details.
