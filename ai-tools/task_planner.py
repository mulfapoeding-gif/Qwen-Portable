"""
Task Planning and Decomposition Tool
Breaks down complex tasks into manageable steps
"""

from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime
import json

@dataclass
class Task:
    """Represents a single task step"""
    id: int
    title: str
    description: str
    estimated_minutes: int
    dependencies: List[int]
    status: str = "pending"  # pending, in_progress, completed, blocked
    notes: str = ""

class TaskPlanner:
    """Breaks down complex requests into actionable tasks"""
    
    def __init__(self):
        self.tasks: List[Task] = []
        self.project_name = ""
        self.created_at = datetime.now()
    
    def create_plan(self, project_name: str, goal: str, context: str = "") -> List[Task]:
        """
        Create a task plan from a goal
        This would normally call an LLM, but we'll create a template structure
        """
        self.project_name = project_name
        self.tasks = []
        
        # Template for common project types
        if "web scraper" in goal.lower() or "scrape" in goal.lower():
            self.tasks = self._create_scraper_plan(goal)
        elif "api" in goal.lower():
            self.tasks = self._create_api_plan(goal)
        elif "dashboard" in goal.lower() or "ui" in goal.lower():
            self.tasks = self._create_ui_plan(goal)
        else:
            self.tasks = self._create_generic_plan(goal)
        
        return self.tasks
    
    def _create_scraper_plan(self, goal: str) -> List[Task]:
        """Create plan for web scraper project"""
        return [
            Task(1, "Research", "Research target website structure and robots.txt", 30, []),
            Task(2, "Setup", "Set up Python environment and install dependencies", 15, []),
            Task(3, "Basic Scraper", "Implement basic page fetching and parsing", 60, [1, 2]),
            Task(4, "Data Extraction", "Implement data extraction logic", 45, [3]),
            Task(5, "Error Handling", "Add error handling and retry logic", 30, [4]),
            Task(6, "Testing", "Test on sample pages and verify output", 30, [4, 5]),
            Task(7, "Optimization", "Add rate limiting and optimizations", 20, [6]),
        ]
    
    def _create_api_plan(self, goal: str) -> List[Task]:
        """Create plan for API project"""
        return [
            Task(1, "Research", "Research API documentation and endpoints", 30, []),
            Task(2, "Setup", "Set up environment and install HTTP library", 15, []),
            Task(3, "Authentication", "Implement authentication (if required)", 30, [1, 2]),
            Task(4, "Basic Client", "Create basic API client with GET requests", 45, [2, 3]),
            Task(5, "Full CRUD", "Implement all required endpoints", 60, [4]),
            Task(6, "Error Handling", "Add error handling and validation", 30, [5]),
            Task(7, "Testing", "Test all endpoints with sample data", 30, [5, 6]),
        ]
    
    def _create_ui_plan(self, goal: str) -> List[Task]:
        """Create plan for UI/dashboard project"""
        return [
            Task(1, "Design", "Plan UI layout and components", 30, []),
            Task(2, "Setup", "Set up framework (Gradio/Streamlit/etc)", 20, []),
            Task(3, "Layout", "Create basic layout structure", 45, [1, 2]),
            Task(4, "Components", "Implement individual components", 60, [3]),
            Task(5, "Integration", "Connect components to data/backend", 60, [4]),
            Task(6, "Styling", "Add styling and polish", 30, [5]),
            Task(7, "Testing", "Test all interactions", 30, [5, 6]),
        ]
    
    def _create_generic_plan(self, goal: str) -> List[Task]:
        """Create generic plan for any project"""
        return [
            Task(1, "Research", "Research requirements and gather information", 30, []),
            Task(2, "Planning", "Plan approach and identify dependencies", 20, [1]),
            Task(3, "Setup", "Set up environment and dependencies", 20, [2]),
            Task(4, "Implementation", "Implement core functionality", 90, [3]),
            Task(5, "Testing", "Test and verify functionality", 30, [4]),
            Task(6, "Refinement", "Refine and optimize", 30, [5]),
        ]
    
    def get_progress(self) -> dict:
        """Get current progress"""
        total = len(self.tasks)
        completed = sum(1 for t in self.tasks if t.status == "completed")
        pending = sum(1 for t in self.tasks if t.status == "pending")
        in_progress = sum(1 for t in self.tasks if t.status == "in_progress")
        
        total_minutes = sum(t.estimated_minutes for t in self.tasks)
        completed_minutes = sum(t.estimated_minutes for t in self.tasks if t.status == "completed")
        
        return {
            "project": self.project_name,
            "total_tasks": total,
            "completed": completed,
            "in_progress": in_progress,
            "pending": pending,
            "percent_complete": round(completed / total * 100) if total > 0 else 0,
            "time_estimated_minutes": total_minutes,
            "time_completed_minutes": completed_minutes,
        }
    
    def display_plan(self) -> str:
        """Display formatted plan"""
        progress = self.get_progress()
        
        output = []
        output.append(f"\n{'='*60}")
        output.append(f"📋 Project: {progress['project']}")
        output.append(f"{'='*60}")
        output.append(f"Progress: {progress['percent_complete']}% complete")
        output.append(f"Time Estimate: {progress['time_estimated_minutes']} minutes")
        output.append(f"\nTasks:")
        
        for task in self.tasks:
            status_icon = {
                "pending": "○",
                "in_progress": "◐",
                "completed": "●",
                "blocked": "⊘"
            }.get(task.status, "○")
            
            deps = f" (depends on: {', '.join(map(str, task.dependencies))})" if task.dependencies else ""
            output.append(f"\n  {status_icon} Task {task.id}: {task.title}")
            output.append(f"      {task.description}")
            output.append(f"      ⏱️  ~{task.estimated_minutes} min{deps}")
        
        output.append(f"\n{'='*60}\n")
        
        return "\n".join(output)
    
    def to_json(self) -> str:
        """Export plan to JSON"""
        return json.dumps([{
            "id": t.id,
            "title": t.title,
            "description": t.description,
            "estimated_minutes": t.estimated_minutes,
            "dependencies": t.dependencies,
            "status": t.status
        } for t in self.tasks], indent=2)


# CLI interface
if __name__ == "__main__":
    import sys
    
    planner = TaskPlanner()
    
    if len(sys.argv) < 2:
        print("Usage: python task_planner.py \"project goal\"")
        print("Example: python task_planner.py \"Build a web scraper\"")
        sys.exit(1)
    
    goal = " ".join(sys.argv[1:])
    project_name = goal[:50] + "..." if len(goal) > 50 else goal
    
    tasks = planner.create_plan(project_name, goal)
    print(planner.display_plan())
