# Day 8-9: Lists & Methods 📋

## 📖 Learning Objectives
- Understand list creation and access
- Master common list methods
- Use list comprehensions
- Work with list slicing

---

## 📚 Creating Lists

### Basic List Creation
```python
# Create lists
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
empty = []

print(fruits)        # Output: ['apple', 'banana', 'cherry']
print(type(fruits))  # Output: <class 'list'>
```

### Accessing Elements
```python
fruits = ["apple", "banana", "cherry"]

print(fruits[0])     # Output: apple (first element)
print(fruits[1])     # Output: banana (second element)
print(fruits[-1])    # Output: cherry (last element)
print(fruits[-2])    # Output: banana (second from last)
```

### List Slicing
```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[2:5])      # Output: [2, 3, 4]
print(numbers[:3])       # Output: [0, 1, 2]
print(numbers[5:])       # Output: [5, 6, 7, 8, 9]
print(numbers[::2])      # Output: [0, 2, 4, 6, 8]
print(numbers[::-1])     # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

---

## 🔧 Common List Methods

### append() - Add element to end
```python
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)  # Output: ['apple', 'banana', 'cherry']
```

### insert() - Add element at specific position
```python
fruits = ["apple", "cherry"]
fruits.insert(1, "banana")
print(fruits)  # Output: ['apple', 'banana', 'cherry']
```

### extend() - Add multiple elements
```python
fruits = ["apple", "banana"]
fruits.extend(["cherry", "date"])
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'date']
```

### remove() - Remove by value
```python
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)  # Output: ['apple', 'cherry']
```

### pop() - Remove by index (returns value)
```python
fruits = ["apple", "banana", "cherry"]
removed = fruits.pop(1)
print(removed)  # Output: banana
print(fruits)   # Output: ['apple', 'cherry']
```

### clear() - Remove all elements
```python
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)   # Output: []
```

### index() - Find position of element
```python
fruits = ["apple", "banana", "cherry"]
position = fruits.index("banana")
print(position)  # Output: 1
```

### count() - Count occurrences
```python
numbers = [1, 2, 2, 3, 2, 4]
count = numbers.count(2)
print(count)  # Output: 3
```

### sort() - Sort in place
```python
numbers = [3, 1, 4, 1, 5, 9]
numbers.sort()
print(numbers)  # Output: [1, 1, 3, 4, 5, 9]

# Reverse sort
numbers.sort(reverse=True)
print(numbers)  # Output: [9, 5, 4, 3, 1, 1]
```

### reverse() - Reverse order
```python
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)  # Output: [5, 4, 3, 2, 1]
```

### copy() - Create a copy
```python
original = [1, 2, 3]
copy_list = original.copy()
copy_list.append(4)
print(original)   # Output: [1, 2, 3]
print(copy_list)  # Output: [1, 2, 3, 4]
```

---

## 💡 Looping Through Lists

### for Loop
```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
# Output: apple, banana, cherry
```

### with enumerate()
```python
fruits = ["apple", "banana", "cherry"]

for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
# Output: 0: apple, 1: banana, 2: cherry
```

### List Comprehension
```python
# Create a list of squares
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(squares)  # Output: [1, 4, 9, 16, 25]

# With condition
even_squares = [x**2 for x in numbers if x % 2 == 0]
print(even_squares)  # Output: [4, 16]
```

---

## 💪 Practice Exercises

### Exercise 1: List Operations
```python
# Create a list of 5 numbers
# Add a number to the end
# Insert a number at position 2
# Remove the first element
# Print the final list
```

### Exercise 2: Shopping List
```python
# Create a shopping list
# Add 5 items
# Remove an item
# Check if "milk" is in the list
# Print how many items you have
```

### Exercise 3: List Statistics
```python
# Ask user for 5 numbers
# Calculate sum, average, max, min
# Display all statistics
```

### Exercise 4: Reverse and Sort
```python
# Create a list of random numbers
# Sort in ascending order
# Sort in descending order
# Reverse the order
# Print all three versions
```

### Exercise 5: Remove Duplicates
```python
# Create a list with duplicate numbers
# Remove duplicates while keeping order
# Print original and cleaned list
```

---

## 🎯 Daily Checklist
- [ ] Create and access lists
- [ ] Use list slicing
- [ ] Master common list methods
- [ ] Loop through lists with for and enumerate
- [ ] Understand list comprehensions
- [ ] Completed all 5 exercises

---

## 💾 Save Your Code
Create folder `exercises/day8-9/` and save all exercises
