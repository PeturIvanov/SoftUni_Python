from to_do_list.task import Task
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


task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())


