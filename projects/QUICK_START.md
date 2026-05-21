# Quick Start Guide - Todo App 🚀

Get started with the Todo Application in 2 minutes!

## 1. Download the App

```bash
cd projects/
ls todo_app.py
```

## 2. Run the Application

```bash
python todo_app.py
```

You'll see:
```
🚀 Welcome to Todo List Application!

==================================================
📝 TODO LIST APPLICATION
==================================================
1.  View all tasks
2.  View pending tasks
3.  View completed tasks
...
```

## 3. Try These Actions

### Add Your First Task
```
👉 Enter your choice (1-13): 4
📌 Task title: Learn Python
Priority (default: Normal): High
Due date (optional, format: YYYY-MM-DD): 2025-06-30
✅ Added: Learn Python
```

### View Your Tasks
```
👉 Enter your choice (1-13): 1
📋 All Tasks:
  1. ○ 🟠 [High] Learn Python (Due: 2025-06-30)
```

### Complete a Task
```
👉 Enter your choice (1-13): 5
📌 Task number to complete: 1
✅ Task marked as complete!
```

### Check Your Progress
```
👉 Enter your choice (1-13): 11

📊 Statistics:
  Total tasks: 1
  ✅ Completed: 1
  ⏳ Pending: 0
  Progress: 100.0%
```

### Exit
```
👉 Enter your choice (1-13): 13
👋 Goodbye! Your tasks have been saved.
```

---

## 4. Your Data is Saved!

A file called `tasks.json` is created automatically. Your tasks persist even after you close the app.

```json
[
  {
    "title": "Learn Python",
    "priority": "High",
    "completed": true,
    "created_date": "2025-05-21 14:30:00",
    "due_date": "2025-06-30"
  }
]
```

---

## Common Tasks

| What to Do | Menu Choice |
|-----------|------------|
| Add a task | 4 |
| See all tasks | 1 |
| Mark task complete | 5 |
| Delete a task | 7 |
| Find a task | 8 |
| See your progress | 11 |
| Save to Excel | 12 |

---

## Tips

💡 **Priority Tips:**
- 🔴 Critical - Do immediately
- 🟠 High - Do today
- 🟡 Normal - Do soon
- 🟢 Low - Can wait

💡 **Pro Tips:**
- View pending tasks (option 2) to focus on what's left
- Use search (option 8) to quickly find tasks
- Export to CSV (option 12) to use in Excel

---

That's it! Start adding tasks and tracking your progress! 📝✨
