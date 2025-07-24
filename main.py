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
  while True:
    
  
    #   print then enter user input choice have a list of all the functinalties like 1.add task, 2.virw taks/ manage, 6.exit tasks 
    print("\nWelcome to To Do List App")
    print("1) Add Task")
    print("2) View tasks/Manage tasks") 
    print("3) Exit Task")
    choice= input("\nEnter Choice: ").strip()

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
      while True:
        print("--- Your Tasks ---")
        to_do_list.view_task()
        print("\na) Mark task as done")
        print("b) Delete Task")
        print("c) Clear completed tasks")
        print("d) Back to Main menu")

        select_action = input("\nChoose action a/b/c/d: ").strip().lower()

        if select_action == 'a':
          indx= int(input("Enter Task number to mark as complete: ")) - 1
          to_do_list.mark_as_done(indx)

        elif select_action == 'b':
          indx= int(input("Enter Task number to delete: ")) - 1
          to_do_list.delete_task(indx)

        elif select_action == 'c':
          to_do_list.clear_completed_task()

        elif select_action == 'd':
          break

        else: 
          print("Invalid input. Please try again")

    elif choice == '3':
      print("Thank you for using TO DO LIST, Goodbye")
      break
    
    else: 
      print("Invalid input. Try again.")

# inside viweing task can filter through priorty or category category, mark as done, delete tasks, cleaar all completed tasks

if __name__ == "__main__":
  main()