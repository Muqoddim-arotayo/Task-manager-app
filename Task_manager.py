from Database import my_Con
from Database import my_Cursor
from tabulate import tabulate
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

class TaskManager :
    def __init__(self):
        self.choice = "1"
        # my_Cursor.execute("CREATE TABLE Task_table (Task_id INT AUTO_INCREMENT PRIMARY KEY, Title VARCHAR(40), Description VARCHAR(40), Status VARCHAR(40), Priority VARCHAR(40))")
        
    def display_menu(self):
        print(f"""{Fore.WHITE}{Style.BRIGHT}\n===== TO-DO LIST MENU =====\n1. Add Task\n2. View Tasks\n3. Update Task\n4. Delete Task\n5. Mark Task as Completed\n""")
        self.choice = input("What task do you want to perform >> ")
        self.handle_choice()
        
    def handle_choice(self):
        choice = self.choice
        if choice == "1":
            print(f"{Fore.YELLOW}\nRedirecting to Add task page...")
            self.add_task()
        elif choice == "2":
            print(f"{Fore.YELLOW}\nRedirecting to view task page...")
            self.view_task()
        elif choice == "3":
            print(f"{Fore.YELLOW}\nRedirecting to update task page...")
            self.update_task()
        elif choice == "4":
            print(f"{Fore.YELLOW}\nRedirecting to Delete task page...")
            self.delete_task()
        elif choice == "5":
            # havent created function
            print(f"{Fore.YELLOW}\nRedirecting to Mark task page...")
        else:
            self.view_task()

    def add_task(self):
        title = input("\nEnter the Task Title >> ")
        description = input("\nEnter the Task description >> ")
        status = input("\nEnter the Task Status [pending, in progress, completed] >> ")
        priority = input("\nEnter the task priority [high, medium, low] >> ")
        my_query = "INSERT INTO Task_table (Title, Description, Status, Priority) VALUES (%s,%s,%s,%s)"
        val = (title, description, status, priority)
        my_Cursor.execute(my_query, val)
        my_Con.commit()
        self.view_task()
        self.display_menu()
    
    def view_task(self):
        table = []
        header = ["Task id","Title", "Description", "Status", "Priority"]
        my_Cursor.execute("SELECT * FROM Task_table")
        for row in my_Cursor:
            task_id, title, description, status, priority = row
            if status.lower() == "completed":
                status = f"{Fore.GREEN}Completed{Style.RESET_ALL}"
            elif status.lower() == "pending":
                status = f"{Fore.YELLOW}Pending{Style.RESET_ALL}"
            else :
                status = f"{Fore.CYAN}In progress{Style.RESET_ALL}"
            if priority.lower() == "high":
                priority = f"{Fore.RED}High{Style.RESET_ALL}"
            elif priority.lower() == "medium":
                priority = f"{Fore.YELLOW}Medium{Style.RESET_ALL}"
            else:
                priority = f"{Fore.GREEN}High{Style.RESET_ALL}"
            table.append([task_id, title, description, status, priority])
            print(row)
            print("\n")
        print(tabulate(table, headers=header, tablefmt="fancy_grid"))
        self.display_menu() 


    def update_task(self):
        update_id = input("\nEnter the Id of the task you want to update >> ")
        update_type = input("\nEnter wnat you want to update >> ")
        update_value = input("\nEnter the new value >> ")
        if update_type not in ["Title", "Description", "Status", "Priority"]:
            print(f"{Fore.YELLOW}\nInvalid column name!")
            self.update_task()
        else : 
            my_query = f"UPDATE Task_Table SET {update_type} = %s WHERE std_id = %s"
            val = ( update_value, update_id)
            my_Cursor.execute(my_query, val)
            my_Con.commit()
            print(my_Cursor.rowcount, "record updated")
            self.view_task() 
            self.display_menu()



    def delete_task(self):
        delete_option = input("Delete Table [1], Delete specific value [2] >> ")
        if delete_option == "1":
            my_Cursor.execute("DROP TABLE Task_Table")
            my_Con.commit()
            print(f"{Fore.GREEN}Table deleted successfully...")
            self.display_menu()
        elif delete_option == "2":
            task_id = input("Enter the ID of the task to delete >> ")
            my_query = "DELETE FROM Task_table WHERE Task_id = %s"
            val = (task_id,)
            my_Cursor.execute(my_query, val)
            my_Con.commit()
            print(f"{Fore.GREEN}Task {task_id} deleted successfully ...")
            self.display_menu()
        else:
            print(f"{Fore.YELLOW}Invalid input")  
            self.display_menu()

my_task_manager = TaskManager()
my_task_manager.display_menu()
