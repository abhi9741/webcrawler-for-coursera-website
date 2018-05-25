import sqlite3

class employee :
    def __init__(self,first,last,salary):
        self.first=first
        self.last=last
        self.salary=salary


conn = sqlite3.connect("employee.db")
c=conn.cursor()

# c.execute("""CREATE TABLE employees(first text,last text,salary integer)""")
# c.execute("INSERT INTO employees VALUES('abhi','reddy',40000)")
c.execute("SELECT * FROM employees WHERE first='abhi'")
print(c.fetchall())
conn.commit()
c.close()
