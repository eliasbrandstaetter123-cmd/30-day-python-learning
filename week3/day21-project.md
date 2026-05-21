# Week 3 Project: Todo App with File Storage 📝

## 📋 Project Overview

Build a **Todo Application** that manages tasks with file storage. Users can add, complete, delete, and save tasks to a file.

## 🎯 Features to Implement

### Level 1: Basic (Days 15-16)
- [ ] **Add Task** - Add new todo items
- [ ] **View Tasks** - Display all tasks
- [ ] **Delete Task** - Remove a task
- [ ] **Save Tasks** - Save to file
- [ ] **Load Tasks** - Load from file

### Level 2: Intermediate (Days 17-18)
- [ ] **Mark Complete** - Toggle task completion
- [ ] **Task Status** - Show completed vs incomplete
- [ ] **Error Handling** - Handle file errors gracefully
- [ ] **Auto-save** - Save after each change

### Level 3: Advanced (Days 19-20)
- [ ] **Task Priority** - Add priority levels
- [ ] **Due Dates** - Add task dates
- [ ] **Task Search** - Find tasks by keyword
- [ ] **Sort Tasks** - Sort by date or priority
- [ ] **Task Class** - Use OOP for tasks

---

## 🔧 Project Structure

```python
# todo_app.py

from datetime import datetime
from pathlib import Path

class Task:
    def __init__(self, title, priority="Normal"):
        self.title = title
        self.priority = priority
        self.completed = False
        self.created_date = datetime.now()
    
    def complete(self):
        self.completed = True
    
    def __str__(self):
        status = "✓" if self.completed else "○"
        return f"{status} [{self.priority}] {self.title}"

class TodoApp:
    def __init__(self, filename="tasks.txt"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()
    
    def add_task(self, title, priority="Normal"):
        task = Task(title, priority)
        self.tasks.append(task)
        self.save_tasks()
        print(f"Added: {title}")
    
    def view_tasks(self):
        if not self.tasks:
            print("No tasks!")
            return
        
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")
    
    def complete_task(self, index):
        if 0 < index <= len(self.tasks):
            self.tasks[index - 1].complete()
            self.save_tasks()
            print("Task marked as complete!")
    
    def delete_task(self, index):
        if 0 < index <= len(self.tasks):
            task = self.tasks.pop(index - 1)
            self.save_tasks()
            print(f"Deleted: {task.title}")
    
    def save_tasks(self):
        pass
    
    def load_tasks(self):
        pass
    
    def main_menu(self):
        while True:
            print("\n=== Todo App ===")
            print("1. View Tasks")
            print("2. Add Task")
            print("3. Complete Task")
            print("4. Delete Task")
            print("5. Exit")
            
            choice = input("Choice: ")
            
            if choice == "1":
                self.view_tasks()
            elif choice == "2":
                title = input("Task: ")
                priority = input("Priority (Low/Normal/High): ") or "Normal"
                self.add_task(title, priority)
            elif choice == "3":
                self.view_tasks()
                idx = int(input("Task number: "))
                self.complete_task(idx)
            elif choice == "4":
                self.view_tasks()
                idx = int(input("Task number: "))
                self.delete_task(idx)
            elif choice == "5":
                print("Goodbye!")
                break

if __name__ == "__main__":
    app = TodoApp()
    app.main_menu()
```

---

## 📝 Implementation Steps

### Step 1: Task Class
```python
from datetime import datetime

class Task:
    def __init__(self, title, priority="Normal"):
        self.title = title
        self.priority = priority
        self.completed = False
        self.created_date = datetime.now()
    
    def complete(self):
        self.completed = True
    
    def __str__(self):
        status = "✓" if self.completed else "○"
        return f"{status} [{self.priority}] {self.title}"
```

### Step 2: Save Tasks to File
```python
def save_tasks(self):
    try:
        with open(self.filename, "w") as file:
            for task in self.tasks:
                line = f"{task.title}|{task.priority}|{task.completed}\n"
                file.write(line)
        print("Tasks saved!")
    except IOError as e:
        print(f"Error saving: {e}")
```

### Step 3: Load Tasks from File
```python
def load_tasks(self):
    try:
        if not Path(self.filename).exists():
            return
        
        with open(self.filename, "r") as file:
            for line in file:
                parts = line.strip().split("|")
                if len(parts) == 3:
                    title, priority, completed = parts
                    task = Task(title, priority)
                    task.completed = completed == "True"
                    self.tasks.append(task)
        print(f"Loaded {len(self.tasks)} tasks")
    except IOError as e:
        print(f"Error loading: {e}")
```

### Step 4: Main Menu Loop
```python
def main_menu(self):
    while True:
        print("\n=== Todo App ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Choice: ")
        
        if choice == "1":
            self.view_tasks()
        elif choice == "2":
            title = input("Task: ")
            priority = input("Priority (Low/Normal/High): ") or "Normal"
            self.add_task(title, priority)
        elif choice == "3":
            self.view_tasks()
            try:
                idx = int(input("Task number: "))
                self.complete_task(idx)
            except ValueError:
                print("Invalid number!")
        elif choice == "4":
            self.view_tasks()
            try:
                idx = int(input("Task number: "))
                self.delete_task(idx)
            except ValueError:
                print("Invalid number!")
        elif choice == "5":
            print("Goodbye!")
            break
```

---

## 🧪 Testing

### Test Cases
```python
# Test 1: Add tasks
app = TodoApp()
app.add_task("Buy milk", "High")
app.add_task("Study Python", "Normal")
app.add_task("Walk dog", "Low")

# Test 2: View
app.view_tasks()

# Test 3: Complete
app.complete_task(1)

# Test 4: Delete
app.delete_task(2)

# Test 5: Save/Load
app.save_tasks()
# Restart app...
app2 = TodoApp()
app2.view_tasks()  # Should show saved tasks
```

---

## ✨ Enhanced Features (Optional)

### Statistics
```python
def get_stats(self):
    total = len(self.tasks)
    completed = sum(1 for t in self.tasks if t.completed)
    return f"Total: {total}, Completed: {completed}"
```

### Clear Completed
```python
def clear_completed(self):
    self.tasks = [t for t in self.tasks if not t.completed]
    self.save_tasks()
```

### Export to CSV
```python
def export_csv(self, filename="tasks.csv"):
    import csv
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Priority", "Completed"])
        for task in self.tasks:
            writer.writerow([task.title, task.priority, task.completed])
```

---

## 📚 Skills Practiced

✅ Object-Oriented Programming  
✅ File handling (read/write)  
✅ Exception handling  
✅ List operations  
✅ Date/time basics  
✅ Menu-driven programs

---

## 🎯 Project Checklist

- [ ] Task class implemented
- [ ] Add task functionality
- [ ] View tasks functionality
- [ ] Complete task functionality
- [ ] Delete task functionality
- [ ] Save to file working
- [ ] Load from file working
- [ ] Error handling implemented
- [ ] No crashes on invalid input
- [ ] Clean, readable code
- [ ] Saved to `week3/projects/todo_app.py`
- [ ] Committed to repository

---

## 💾 File Structure
```
exercises/day21-project/
├── todo_app.py
├── tasks.txt (created by app)
└── README.md
```

Good luck! 🚀
