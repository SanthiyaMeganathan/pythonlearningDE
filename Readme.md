1. Syntax & Structure
Python is designed for readability. Unlike other languages, it uses whitespace to define the structure of the system.

Indentation is Mandatory: Instead of using curly brackets { }, Python uses indentation (usually 4 spaces) to define code blocks.

Dynamic Typing: You do not need to declare a data type (e.g., int or string). Python’s interpreter is "intelligent" enough to infer the type at runtime.

String Literals: Anything enclosed in single (') or double (") quotes is treated as a String.

2. Variable Management
Assignment Intelligence: Python follows a "Last-In, First-Out" logic for variable updates.

Python
x = 10
x = "hello"
print(x)  # Output: hello
The None Type: You can initialize a variable with None to represent the absence of a value or a null state.

Introspection: Use the type() function to identify the data type of any object in the system.

🏗️ Scope & Lifetime (LEGB Rule)
The "Life" of a variable is determined by its scope. Python searches for variables in a specific hierarchical order:

L (Local): Variables defined inside a function. They cannot be accessed outside.

E (Enclosing): Variables in the local scope of nested functions (a function inside a function).

G (Global): Variables defined at the top level of the script.

B (Built-in): Special keywords and functions pre-loaded in Python (e.g., print, len).