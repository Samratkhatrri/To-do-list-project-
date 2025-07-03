

# using oop we will set different object such as add_task, category, due date etc; when a user decides to add a task
class Task:
    def __init__ (self, title, category, due_date):
        self.title = title # string 
        self.category = category  # string 
        self.due_date = due_date # date 
        self.completed= False





