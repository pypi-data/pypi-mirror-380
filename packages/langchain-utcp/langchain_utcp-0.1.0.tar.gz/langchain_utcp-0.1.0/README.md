# Langchain-UTCP

**Langchain-UTCP** is a production-ready Python library that provides a seamless and secure integration between the Universal Tool Calling Protocol (UTCP) and LangChain.

This library acts as a robust adapter, using the official [`python-utcp`](https://github.com/universal-tool-calling-protocol/python-utcp) SDK to load UTCP manuals and execute tools, and then seamlessly presents them as native LangChain `Tool` objects for use in your agents and chains.

## Key Features

- **Correct SDK Integration**: Uses the official `UtcpClient.create(config=...)` factory pattern for maximum compatibility.
- **Seamless LangChain Integration**: Converts UTCP tools into LangChain `StructuredTool` objects automatically.
- **Configuration Driven**: Pass a standard UTCP configuration dictionary to load any combination of manuals and providers.
- **Asynchronous First**: Designed for modern, high-performance AI applications.

## Installation

```bash
pip install langchain-utcp
