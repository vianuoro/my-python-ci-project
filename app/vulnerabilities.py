import os
import ast

# --- VULNERABLE EXAMPLES ---

# 1. Arbitrary Code Execution via eval()
# eval() is designed for expressions. An attacker can use __import__ to 
# reach the 'os' module and run system commands.
print("--- Running eval() exploit ---")
vulnerable_input_eval = "__import__('os').getlogin()" 
# In a real attack, this might be: "__import__('os').system('rm -rf /')"
result = eval(vulnerable_input_eval)
print(f"User identified via eval: {result}\n")


# 2. Arbitrary Code Execution via exec()
# exec() allows multi-line Python code. This example creates a dummy 
# file on the system, simulating a data breach or system modification.
print("--- Running exec() exploit ---")
vulnerable_input_exec = """
import os
with open('pwned.txt', 'w') as f:
    f.write('This system has a vulnerability.')
print('Malicious file "pwned.txt" created successfully.')
"""
exec(vulnerable_input_exec)


# --- SECURE ALTERNATIVE ---

# 3. Using ast.literal_eval() for safety
# This will only evaluate literal structures (strings, numbers, tuples, lists, dicts)
# It will raise a ValueError if you try to pass code or system commands.
print("\n--- Running Secure Alternative ---")
safe_input = "{'status': 'success', 'data': [1, 2, 3]}"
try:
    data = ast.literal_eval(safe_input)
    print(f"Safely parsed data: {data}")
    
    # This would fail safely:
    # ast.literal_eval("__import__('os').system('ls')") 
except (ValueError, SyntaxError) as e:
    print(f"Blocked malicious input: {e}")
