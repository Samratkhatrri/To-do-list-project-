from view_task import ToDoList
from datetime import datetime

# Making to-do list, will be using multiple files functions etc; OOP 
# Add a 'Add task', 'View task', 'Mark taks as done', 'delete task', 'Clear completed taks', 'Categorise tasks', 'due date remindes'
# Add tasks--> User enters text/taks and decription if needed--> Due date --> priority level of the taks
# View taks--> show all tasks--> status done or not done--> priorty of the tasks and the due date
# Mark as done -->user can selsect tasks and mark it as completed will show up completed or status completed in 'view tasks' when this happenes 
# Delete taks--> user cna delete tasks
# clear completed tasks--> all the completed or status done tasks can be removed from viw tasks and the databse 
#categorise tasks--> categorise tasks in certain categories such as school, work etc; might have to add it to the  'add a task' part
# due date and reminders-->track which takss are overdue and upcomng 
#
# Some thoughts: which functionalities tie into other functionalties, if mark as done should be integrated as seperate or into view tasks, same with delete tasks
# Some thoughts: If i should have allfdunctionalites in view tasks ui (terminal), so only need add taks, view tasks and due date reminders ???


# add the input (ui of terminal) insode the main and add different functionaltoes nside other files

def main ():
  
  to_do_list = ToDoList()
  
#   print then enter user input choice have a list of all the functinalties like 1.add task, 2.virw taks/ manage, 6.exit tasks 
  print("\n1) Add Task \n2) View Tasks/ Manage Tasks \n3) Exit tasks")
  choice= input("Enter Choice: ").strip()

  if choice == '1':
    titleTask= input("Task: ")
    categoryTask= input("Category: ")

    while True:
        dueDate= input("Due Date (dd/mm//yyyy): ")
        try:
           date_time= datetime.strptime(dueDate, "%d/%m/%Y")
           break
        except ValueError:
          print("Invalid format. Please enter the date in dd/mm/yyyy format")

    to_do_list.add_task(titleTask, categoryTask, date_time)

  elif choice == '2':
     print("New feature coming soon")

  else:
     print("New feature coming soon")

 


  
 
# inside viweing task can filter through priorty or category category, mark as done, delete tasks, cleaar all completed tasks

if __name__ == "__main__":
  main()