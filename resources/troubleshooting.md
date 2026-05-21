# Troubleshooting & Common Errors 🐛

Solutions to common Python errors you'll encounter.

---

## 🔴 SyntaxError

### Missing Colon
```python
# ❌ Error
if x > 5
    print(x)

# ✅ Fixed
if x > 5:
    print(x)
```

### Indentation Error
```python
# ❌ Error
for i in range(5):
print(i)

# ✅ Fixed
for i in range(5):
    print(i)
```

### Mismatched Quotes
```python
# ❌ Error
text = "Hello'

# ✅ Fixed
text = "Hello"
```

---

## 🔴 NameError

### Undefined Variable
```python
# ❌ Error
print(x)  # x doesn't exist

# ✅ Fixed
x = 5
print(x)
```

### Typo in Variable Name
```python
# ❌ Error
name = "Alice"
print(Name)  # Wrong case!

# ✅ Fixed
name = "Alice"
print(name)
```

---

## 🔴 TypeError

### Wrong Data Type Operation
```python
# ❌ Error
"5" + 5

# ✅ Fixed
int("5") + 5
# or
"5" + str(5)
```

### Forgot Parentheses on Function
```python
# ❌ Error
text = "hello"
upper = text.upper  # No parentheses!

# ✅ Fixed
upper = text.upper()
```

### Wrong Argument Type
```python
# ❌ Error
list = [1, 2, 3]
list.insert("a", 1)  # First arg must be int

# ✅ Fixed
list.insert(0, 1)
```

---

## 🔴 IndexError

### Index Out of Range
```python
# ❌ Error
list = [1, 2, 3]
print(list[5])

# ✅ Fixed
print(list[2])  # Last element
print(list[-1])
```

### Empty Sequence
```python
# ❌ Error
list = []
first = list[0]

# ✅ Fixed
if list:
    first = list[0]
else:
    print("List is empty")
```

---

## 🔴 KeyError

### Missing Dictionary Key
```python
# ❌ Error
person = {"name": "Alice"}
print(person["age"])

# ✅ Fixed
print(person.get("age", "Unknown"))
print(person.get("age"))  # Returns None
```

---

## 🔴 ValueError

### Invalid Literal for Conversion
```python
# ❌ Error
age = int("abc")

# ✅ Fixed
try:
    age = int("25")
except ValueError:
    print("Invalid number!")
```

### Unpacking Wrong Number of Values
```python
# ❌ Error
a, b = [1, 2, 3]

# ✅ Fixed
a, b, c = [1, 2, 3]
a, *rest = [1, 2, 3]  # a=1, rest=[2,3]
```

---

## 🔴 FileNotFoundError

### File Doesn't Exist
```python
# ❌ Error
with open("missing.txt") as f:
    content = f.read()

# ✅ Fixed
from pathlib import Path

file_path = Path("data.txt")
if file_path.exists():
    content = file_path.read_text()
else:
    print("File not found!")
```

---

## 🔴 AttributeError

### Object Has No Attribute
```python
# ❌ Error
x = 5
print(x.upper())  # int doesn't have .upper()

# ✅ Fixed
text = "hello"
print(text.upper())
```

### Misspelled Method
```python
# ❌ Error
list = [3, 1, 2]
list.sort()
print(list.sorted())  # Wrong method!

# ✅ Fixed
list.sort()
print(list)
```

---

## 🔴 ImportError

### Module Not Installed
```python
# ❌ Error
import numpy  # Not installed

# ✅ Fixed
# Install first:
# pip install numpy
import numpy as np
```

### Wrong Import Path
```python
# ❌ Error
from os import missing_thing

# ✅ Fixed
from os import path
from os import listdir
```

---

## 🔴 IndentationError

### Inconsistent Indentation
```python
# ❌ Error
if x > 5:
    print("big")
  print("done")

# ✅ Fixed
if x > 5:
    print("big")
print("done")
```

---

## 🟡 LogicError (Not Python Errors, But Logic Issues)

### Infinite Loop
```python
# ❌ Error
while True:
    print("Forever!")
    # No break or exit!

# ✅ Fixed
while True:
    print("Forever!")
    break
```

### Off-by-One Error
```python
# ❌ Error
for i in range(1, 10):  # 1 to 9, not 10
    print(i)

# ✅ Fixed
for i in range(1, 11):  # 1 to 10
    print(i)
```

### Mutable Default Argument
```python
# ❌ Error (Common Bug!)
def add_item(item, list=[]):
    list.append(item)
    return list

add_item(1)        # [1]
add_item(2)        # [1, 2] - Unexpected!

# ✅ Fixed
def add_item(item, list=None):
    if list is None:
        list = []
    list.append(item)
    return list
```

---

## 🛠️ Debugging Techniques

### Print Debugging
```python
x = 10
print(f"DEBUG: x = {x}")

# Conditional print
DEBUG = True
if DEBUG:
    print(f"Value: {x}")
```

### Using Python Debugger
```python
import pdb

x = 10
pdb.set_trace()  # Program pauses here
print(x)
# In debugger: p x, n (next), c (continue)
```

### Python 3.7+ Breakpoint
```python
x = 10
breakpoint()  # Program pauses here
print(x)
```

### Check Types
```python
print(type(x))
print(isinstance(x, int))
print(isinstance(x, (int, float)))
```

---

## 📋 Error Handling Best Practices

### Catch Specific Errors
```python
# ❌ Too Broad
try:
    result = int(input())
except:
    print("Error!")

# ✅ Specific
try:
    result = int(input())
except ValueError:
    print("Please enter a number!")
except KeyboardInterrupt:
    print("Cancelled by user")
```

### Always Provide Feedback
```python
# ❌ Silent Failure
try:
    file = open("data.txt")
except:
    pass

# ✅ Inform User
try:
    file = open("data.txt")
except FileNotFoundError:
    print("Error: File not found. Creating new file...")
    file = open("data.txt", "w")
```

---

## 🎯 Debugging Checklist

When you get an error:
1. [ ] Read the full error message
2. [ ] Find the line number with the problem
3. [ ] Check variable names and types
4. [ ] Verify indentation
5. [ ] Test with simple example
6. [ ] Check documentation
7. [ ] Print intermediate values
8. [ ] Use debugger if needed

---

## 🆘 Getting Help

1. **Read the error message carefully** - It usually tells you what's wrong
2. **Google the error** - Add "Python" to your search
3. **Check documentation** - [docs.python.org](https://docs.python.org/)
4. **Stack Overflow** - Search before asking
5. **Ask in communities** - Reddit r/learnprogramming, Discord, etc.

---

## 💡 Prevention Tips

- [ ] Use a code editor with syntax highlighting
- [ ] Enable linting (pylint, flake8)
- [ ] Use type hints (optional but helpful)
- [ ] Write tests as you code
- [ ] Use meaningful variable names
- [ ] Add comments for complex logic
- [ ] Break code into functions
- [ ] Run code frequently while developing

Good luck debugging! 🐛✨
