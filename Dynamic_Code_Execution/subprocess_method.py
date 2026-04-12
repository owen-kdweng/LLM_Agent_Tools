import subprocess

code = """
i=0
while True:
    print(f"Hello from subprocess! {i}")
    i+=1
"""

with open("Dynamic_Code_Execution/temp_code.py", "w") as f:
    f.write(code)

# 執行
subprocess.run(
    ["python", "Dynamic_Code_Execution/temp_code.py"], 
    timeout=3,
    env={"PATH": ""}
)
