from add_task import Task


# here i will implment the differen functionalties of theto do list and put them in the view task section/ module
class ToDoList:
    def __init__(self):
        self.tasks= []

    # add tasks and its variables to the list created 
    def add_task(self, add_task, priority_level, categorise, due_date):
        new_task= Task(add_task, priority_level, categorise, due_date )
        self.tasks.append(new_task)

    # list out the task in view format includs task, prioty level, categor, etc..
    def view_task(self):
      for i, v_task in enumerate(self.tasks):
        if v_task.completed:
          completed_task = "✖️"
        else:
           completed_task = "☑️"
        print(f"{i+1}. {v_task.add_task} | {v_task.priority_level} | {v_task.categorise} | {v_task.due_date} | {completed_task}")
        
    # make sure correct index of task is completed, when taks is completed mark it complete should show ith the purple tick emoji
    def mark_as_done(self, indx):
       if 0 <= indx < len(self.tasks):
          self.tasks[indx].completed = True 
    
    # same thing just remove using pop    
    def delete_task(self, indx):
       if 0 <= indx < len(self.tasks):
          self.tasks.pop(indx)

    # create new list and add all the tasks that are not completed
    def clear_completed_task(self):
      new_tasks= []
      for task in self.tasks:
         if not task.completed:
            new_tasks.append(task)
      self.tasks = new_tasks

    # filter by category or prioirty level 

    def categorise(self, categorise):
      return [task for task in self.tasks if task.categorise == categorise]
 
    def priortiy_level(self, priority_level):
       return [task for task in self.tasks if task.priorty_level == priority_level]



