from project.task import Task
class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task) -> str:
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"

        self.tasks.append(new_task)

        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str) -> str:
        try:
            task_instance = next(filter(lambda x: x.name == task_name,self.tasks))
            task_instance.completed = True
            return f"Completed task {task_name}"

        except StopIteration:
            return f"Could not find task with the name {task_name}"

    def clean_section(self) -> str:
        completed_tasks = []

        for task in self.tasks:
            if task.completed:
                completed_tasks.append(task)
                self.tasks.remove(task)

        return f"Cleared {len(completed_tasks)} tasks."

    def view_section(self) -> str:
        section_data = []
        section_data.append(f"Section {self.name}:")
        section_data.extend([t.details() for t in self.tasks])

        return '\n'.join(section_data)


