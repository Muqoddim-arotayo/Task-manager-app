from Database import my_Con
from Database import my_Cursor
from tabulate import tabulate
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

class TaskManager :
    def __init__(self):
        pass
        # my_Cursor.execute("CREATE TABLE Task_table (Task_id INT AUTO_INCREMENT PRIMARY KEY, Title VARCHAR(40), Description VARCHAR(40), Status VARCHAR(40), Priority VARCHAR(40))")
        

    def add_task(self):
        title = input("Enter the Task Title >> ")
        description = input("Enter the Task description >> ")
        status = input("Enter the Task Status >> ")
        priority = input("Enter the task priority [high, medium, low] >> ")
        # if priority.lower == "high":

        my_query = "INSERT INTO Task_table (Title, Description, Status, Priority) VALUES (%s,%s,%s,%s)"
        val = (title, description, status, priority)
        my_Cursor.execute(my_query, val)
        self.view_task()
    
    def view_task(self):
        table = []
        header = ["Title", "Description", "Status", "Priority"]
        my_Cursor.execute("SELECT * FROM Task_table")
        for row in my_Cursor:
            table.append(row)
            print(row)
        my_Cursor.close()
        print(tabulate(table, headers=header, tablefmt="fancy_grid"))


    def update_task(self):
        update_id = input("Enter the Id of the task you want to update >> ")
        update_type = input("Enter wnat you want to update >> ")
        update_value = input("Enter the new value >> ")
        my_query = "UPDATE Task_Table SET %s = %s WHERE std_id = %s"
        val = (update_type, update_value, update_id)
        my_Cursor.execute(my_query, val)
        print(my_Cursor.rowcount, "record updated")
        self.view_task()



    def delete_task(self):
        delete_option = input("Delete Table [1], Delete specific value [2] >> ")
        if delete_option == "1":
            pass
        elif delete_option == "2":
            my_Cursor.execute("DROP TABLE Task_Table")
            print(f"{Fore.GREEN}Table deleted successfully...")
        else:
            print(f"{Fore.YELLOW}Invalid input")
    def mark_as_complete():
        pass

    def set_priority():
        pass

my_task_manager = TaskManager()
my_task_manager.add_task()