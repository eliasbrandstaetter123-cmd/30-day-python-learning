"""
Unit Tests for Todo Application
Tests all major features and functionality
Run with: python test_todo_app.py
"""

import unittest
import json
import os
from pathlib import Path
from todo_app import Task, TodoApp


class TestTask(unittest.TestCase):
    """Tests for Task class"""
    
    def setUp(self):
        """Create a fresh task for each test"""
        self.task = Task("Test Task", "High", "2025-06-01")
    
    def test_task_creation(self):
        """Test task is created correctly"""
        self.assertEqual(self.task.title, "Test Task")
        self.assertEqual(self.task.priority, "High")
        self.assertEqual(self.task.due_date, "2025-06-01")
        self.assertFalse(self.task.completed)
    
    def test_task_completion(self):
        """Test marking task complete"""
        self.assertFalse(self.task.completed)
        self.task.complete()
        self.assertTrue(self.task.completed)
    
    def test_task_mark_incomplete(self):
        """Test marking task incomplete"""
        self.task.complete()
        self.assertTrue(self.task.completed)
        self.task.mark_incomplete()
        self.assertFalse(self.task.completed)
    
    def test_priority_emoji(self):
        """Test emoji generation for priorities"""
        self.assertEqual(Task("t", "Critical").get_priority_emoji(), "🔴")
        self.assertEqual(Task("t", "High").get_priority_emoji(), "🟠")
        self.assertEqual(Task("t", "Normal").get_priority_emoji(), "🟡")
        self.assertEqual(Task("t", "Low").get_priority_emoji(), "🟢")
    
    def test_to_dict(self):
        """Test converting task to dictionary"""
        task_dict = self.task.to_dict()
        self.assertEqual(task_dict["title"], "Test Task")
        self.assertEqual(task_dict["priority"], "High")
        self.assertIn("created_date", task_dict)


class TestTodoApp(unittest.TestCase):
    """Tests for TodoApp class"""
    
    def setUp(self):
        """Create app with test file"""
        self.test_filename = "test_tasks.json"
        self.app = TodoApp(self.test_filename)
        self.app.tasks = []  # Start with clean slate
    
    def tearDown(self):
        """Clean up test file"""
        if Path(self.test_filename).exists():
            os.remove(self.test_filename)
    
    def test_add_task(self):
        """Test adding a task"""
        result = self.app.add_task("Buy milk", "Normal")
        self.assertTrue(result)
        self.assertEqual(len(self.app.tasks), 1)
        self.assertEqual(self.app.tasks[0].title, "Buy milk")
    
    def test_add_empty_task(self):
        """Test adding empty task is rejected"""
        result = self.app.add_task("", "Normal")
        self.assertFalse(result)
        self.assertEqual(len(self.app.tasks), 0)
    
    def test_complete_task(self):
        """Test completing a task"""
        self.app.add_task("Test", "Normal")
        self.assertFalse(self.app.tasks[0].completed)
        self.app.complete_task(1)
        self.assertTrue(self.app.tasks[0].completed)
    
    def test_mark_incomplete_task(self):
        """Test marking task incomplete"""
        self.app.add_task("Test", "Normal")
        self.app.complete_task(1)
        self.app.mark_incomplete(1)
        self.assertFalse(self.app.tasks[0].completed)
    
    def test_delete_task(self):
        """Test deleting a task"""
        self.app.add_task("Task 1", "Normal")
        self.app.add_task("Task 2", "Normal")
        self.assertEqual(len(self.app.tasks), 2)
        self.app.delete_task(1)
        self.assertEqual(len(self.app.tasks), 1)
        self.assertEqual(self.app.tasks[0].title, "Task 2")
    
    def test_search_tasks(self):
        """Test searching for tasks"""
        self.app.add_task("Learn Python", "High")
        self.app.add_task("Buy milk", "Normal")
        self.app.add_task("Python project", "High")
        
        # Search should find 2 tasks with "Python"
        results = [t for t in self.app.tasks if "Python" in t.title]
        self.assertEqual(len(results), 2)
    
    def test_get_statistics(self):
        """Test getting statistics"""
        self.app.add_task("Task 1", "High")
        self.app.add_task("Task 2", "Normal")
        self.app.add_task("Task 3", "Low")
        self.app.complete_task(1)
        self.app.complete_task(2)
        
        # Count tasks
        total = len(self.app.tasks)
        completed = sum(1 for t in self.app.tasks if t.completed)
        pending = total - completed
        
        self.assertEqual(total, 3)
        self.assertEqual(completed, 2)
        self.assertEqual(pending, 1)
    
    def test_clear_completed(self):
        """Test clearing completed tasks"""
        self.app.add_task("Task 1", "Normal")
        self.app.add_task("Task 2", "Normal")
        self.app.complete_task(1)
        
        self.assertEqual(len(self.app.tasks), 2)
        self.app.clear_completed()
        self.assertEqual(len(self.app.tasks), 1)
        self.assertEqual(self.app.tasks[0].title, "Task 2")
    
    def test_save_and_load_tasks(self):
        """Test saving and loading tasks"""
        self.app.add_task("Task 1", "High", "2025-06-01")
        self.app.add_task("Task 2", "Low")
        self.app.complete_task(1)
        self.app.save_tasks()
        
        # Create new app and load
        new_app = TodoApp(self.test_filename)
        
        self.assertEqual(len(new_app.tasks), 2)
        self.assertEqual(new_app.tasks[0].title, "Task 1")
        self.assertTrue(new_app.tasks[0].completed)
        self.assertEqual(new_app.tasks[1].priority, "Low")
    
    def test_invalid_task_index(self):
        """Test invalid task index handling"""
        self.app.add_task("Task", "Normal")
        # Should not crash
        self.app.complete_task(99)
        self.app.delete_task(99)
    
    def test_priority_sorting(self):
        """Test sorting by priority"""
        self.app.add_task("Low priority", "Low")
        self.app.add_task("Critical", "Critical")
        self.app.add_task("High", "High")
        self.app.add_task("Normal", "Normal")
        
        priority_order = {"Critical": 0, "High": 1, "Normal": 2, "Low": 3}
        sorted_tasks = sorted(self.app.tasks,
                            key=lambda t: priority_order.get(t.priority, 99))
        
        self.assertEqual(sorted_tasks[0].priority, "Critical")
        self.assertEqual(sorted_tasks[1].priority, "High")
        self.assertEqual(sorted_tasks[2].priority, "Normal")
        self.assertEqual(sorted_tasks[3].priority, "Low")
    
    def test_export_csv(self):
        """Test exporting to CSV"""
        self.app.add_task("Task 1", "High", "2025-06-01")
        self.app.add_task("Task 2", "Low")
        
        csv_file = "test_export.csv"
        self.app.export_to_csv(csv_file)
        
        # Check file was created
        self.assertTrue(Path(csv_file).exists())
        
        # Clean up
        if Path(csv_file).exists():
            os.remove(csv_file)
    
    def test_pending_vs_completed(self):
        """Test filtering pending vs completed tasks"""
        self.app.add_task("Task 1", "Normal")
        self.app.add_task("Task 2", "Normal")
        self.app.add_task("Task 3", "Normal")
        self.app.complete_task(1)
        self.app.complete_task(3)
        
        pending = [t for t in self.app.tasks if not t.completed]
        completed = [t for t in self.app.tasks if t.completed]
        
        self.assertEqual(len(pending), 1)
        self.assertEqual(len(completed), 2)


class TestIntegration(unittest.TestCase):
    """Integration tests for complete workflows"""
    
    def setUp(self):
        """Create app with test file"""
        self.test_filename = "test_integration.json"
        self.app = TodoApp(self.test_filename)
        self.app.tasks = []
    
    def tearDown(self):
        """Clean up test file"""
        if Path(self.test_filename).exists():
            os.remove(self.test_filename)
    
    def test_complete_workflow(self):
        """Test complete user workflow"""
        # Add tasks
        self.app.add_task("Learn Python", "High", "2025-06-01")
        self.app.add_task("Buy groceries", "Normal")
        self.app.add_task("Walk dog", "Low")
        
        self.assertEqual(len(self.app.tasks), 3)
        
        # Complete some tasks
        self.app.complete_task(1)
        self.app.complete_task(3)
        
        # Check statistics
        completed = sum(1 for t in self.app.tasks if t.completed)
        pending = sum(1 for t in self.app.tasks if not t.completed)
        
        self.assertEqual(completed, 2)
        self.assertEqual(pending, 1)
        
        # Save
        self.app.save_tasks()
        
        # Create new app and verify
        new_app = TodoApp(self.test_filename)
        self.assertEqual(len(new_app.tasks), 3)
        self.assertTrue(new_app.tasks[0].completed)
        self.assertFalse(new_app.tasks[1].completed)
        self.assertTrue(new_app.tasks[2].completed)


def run_tests():
    """Run all tests"""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    suite.addTests(loader.loadTestsFromTestCase(TestTask))
    suite.addTests(loader.loadTestsFromTestCase(TestTodoApp))
    suite.addTests(loader.loadTestsFromTestCase(TestIntegration))
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_tests()
    if success:
        print("\n✅ All tests passed!")
    else:
        print("\n❌ Some tests failed!")
