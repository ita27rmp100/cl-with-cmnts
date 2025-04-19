import sys , os , sqlite3

# Create a connection to the SQLite database
connection = sqlite3.connect('history.db')
cursor = connection.cursor()

# create table history
try :
    cursor.execute('create table history (command varchar(255), comment varchar(100))')
except sqlite3.OperationalError:
    pass


args = sys.argv
args.pop(0)  # Remove the script name from the arguments
if len(args) == 0:
    print("No arguments provided.")
elif len(args) == 1 and args[0] == 'dh':
    cursor.execute('select * from history')
    data = cursor.fetchall()
    for row in data:
        print(row[0], row[1])
elif len(args) != 2 :
    print("Invalid number of arguments. Please provide a command and a comment.")
else:
    os.system(args[0])
    cursor.execute("insert into history values(?,?)", (args[0], args[1]))
    connection.commit()
    print("Command executed and logged.")
    cursor.execute('select * from history')