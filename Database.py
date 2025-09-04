import pymysql as pyms
import os   
from dotenv import load_dotenv
load_dotenv()  

db_password = os.getenv("DB_PASS")  

my_Con = pyms.connect(host='127.0.0.1', user='root', passwd=db_password, db="TaskManager")
my_Cursor = my_Con.cursor()
 


