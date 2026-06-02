# MCP Fundamentals – Python MCP Server

## Overview

This project is a simple MCP (Model Context Protocol) server built using the MCP Python SDK (`FastMCP`). The purpose of this project is to understand MCP fundamentals, including:

* MCP Client and Server architecture
* Tool registration and discovery
* Tool invocation
* MCP Inspector usage
* JSON-RPC based communication
* MCP lifecycle (`initialize`, `tools/list`, `tools/call`)

This project is intended for learning MCP architecture before moving into MCP Gateways, Agent Security, Authentication, Authorization, and Policy Enforcement.

---

## Technology Stack

* Python 3.x
* MCP Python SDK
* MCP Inspector

---

## Project Structure

```text
mcp-project/
│
├── server.py
├── venv/
└── README.md
```
## Available Tools

### hello

Returns a greeting message.

Input:

```text
name: string
```

Example:

```text
Karthikha
```

Output:

```text
Hello Karthikha
```

---

### add

Adds two numbers.

Input:

```text
a: integer
b: integer
```

Example:

```text
a = 10
b = 20
```

Output:

```text
30
```

---

### current_time

Returns the current system date and time.

Input:

```text
No input required
```

Output:

```text
2026-06-02 10:30:00
```

---

## Installation

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install MCP SDK

```bash
pip install mcp
```

Verify installation:

```bash
pip show mcp
```

---

## Running the MCP Server

Run the server using MCP Inspector:

```bash
mcp dev server.py
```

Expected output:

```text
Starting MCP inspector...
Proxy server listening on localhost
MCP Inspector is up and running
```

A browser window will open automatically.

---

## Testing Tools

### Connect to Server

1. Open MCP Inspector.
2. Click Connect.
3. Wait for successful initialization.

The Inspector will send:

```text
initialize
```

The server will respond with its capabilities.

---

### Discover Available Tools

The Inspector automatically sends:

```text
tools/list
```

The server responds with:

```text
hello
add
current_time
```

---

### Invoke a Tool

When a tool is selected and executed, the Inspector sends:

```text
tools/call
```

Example:

```text
Tool: add
a = 10
b = 20
```

The server executes:

```python
add(10, 20)
```

Response:

```text
30
```

---

## MCP Architecture

```text
+----------------+
| MCP Inspector  |
|    (Client)    |
+--------+-------+
         |
         | JSON-RPC
         |
         v
+----------------+
|  MCP Server    |
|   (FastMCP)    |
+--------+-------+
         |
         |
         v
+----------------+
| MCP Tools      |
| hello()        |
| add()          |
| current_time() |
+----------------+
```

---

## MCP Message Flow

### Step 1 – Initialize

Client:

```text
initialize
```

Server:

```text
Returns capabilities
```

---

### Step 2 – Tool Discovery

Client:

```text
tools/list
```

Server:

```text
Returns available tools
```

---

### Step 3 – Tool Execution

Client:

```text
tools/call
```

Server:

```text
Executes selected tool
```

Response:

```text
Returns tool result
```

---

## Learning Outcomes

Through this project, the following MCP concepts were explored:

* MCP Client and Server communication
* MCP Tool registration
* Tool discovery using `tools/list`
* Tool execution using `tools/call`
* MCP Inspector integration
* FastMCP abstraction layer
* Basic understanding of MCP architecture
* Introduction to JSON-RPC communication

---

## Future Work

Planned next steps:

* Study MCP Specification in detail
* Explore JSON-RPC messages manually
* Set up an MCP Gateway
* Implement request interception
* Add authentication and authorization
* Develop policy enforcement filters
* Explore Agent Security architecture
