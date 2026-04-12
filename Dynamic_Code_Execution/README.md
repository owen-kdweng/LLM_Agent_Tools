# Dynamic Code Execution

This repository is used to demonstrate same example of `Dynamic Code Execution`. 
This folder currently provides three common methods. Demonstrates how to dynamically generate and execute another piece of Python code during Python execution.


## Project Structure
Dynamic_Code_Execution
│   subprocess_method.py
│   runpy_method.py
│   exec_method.py
└── temp_code.py


## Comparison of Methods

| Method | Execution Context | Isolation Level | Safety | Performance | Use Cases |
|--------|------------------|----------------|--------|------------|----------|
| `exec()` | Same process | Low | Low | Fast | Quick testing, simple demos, small code snippets |
| `runpy.run_path()` | Same process (file-based) | Medium-Low | Medium-Low | Fast | Executing external scripts, better code organization |
| `subprocess.run()` | Separate process | High | Higher | Slower | Production use, LLM code execution, sandbox-like behavior |