import runpy

code = """
print("Hello from subprocess!")
"""

with open("Dynamic_Code_Execution/temp_code.py", "w") as f:
    f.write(code)

runpy.run_path("Dynamic_Code_Execution/temp_code.py")