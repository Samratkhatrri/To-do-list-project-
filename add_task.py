

# using oop we will set different object such as add_task, category, due date etc; when a user decides to add a task
class Task:
    def __init__ (self, add_task, priority_level, categorise, due_date):
        self.add_task = add_task # string 
        self.priority_level = priority_level # string 
        self.categorise = categorise  # string 
        self.due_date = due_date # date 
        self.completed_task= False





