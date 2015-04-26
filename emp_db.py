import MySQLdb

def count():
	db=MySQLdb.connect("localhost","python","123456","testdb")
	cur=db.cursor()
	table="employee"
	query ="SELECT COUNT(emp_id) from `%s`" %(table)
	cur.execute(query)             
	res=cur.fetchone()
	total_rows=res[0] 
	return total_rows
	db.close

def db_in(fname,lname,salary,dept,desig,addr,age,gender):
	db=MySQLdb.connect("localhost","python","123456","testdb")
	cur=db.cursor()
	sql = "INSERT INTO employee(fname, lname, salary, dept, desig, addr, age, gender) VALUES ('%s', '%s', '%d', '%s', '%s', '%s', '%d', '%c' )" %(fname,lname,salary,dept,desig,addr,age,gender)
	try:
		cur.execute(sql)
		db.commit()
	except:
		db.rollback
	db.close

def disp(i):
	if(i==0):
		sql = "select * from employee"
	else:
		sql = "select * from employee where emp_id=%d"%(i)
	db=MySQLdb.connect("localhost","python","123456","testdb")
	cur=db.cursor()
	cur.execute(sql);
	row = cur.fetchone()
	while row is not None:
		print ", ".join([str(c) for c in row])
		row = cur.fetchone()
	cur.close()
	db.close()

choice=1
while choice!=0:
    print "1. New Entry"
    print "2. Display"
    print "3. Display All"
    print "4. Remove Employee"
    print "0 Exit"

    print "Enter you choice:",
    choice=input()
    if(choice==1):
        fname=raw_input("Enter First name of Employee: ")
	    lname=raw_input("Enter Last name of Employee: ")
        salary=input("Enter salary: ")
        dept=raw_input("Enter Department of the Employee: ")
        desig=raw_input("Enter Designation of the Employee: ")
        addr=raw_input("Enter Address of the Employee: ")
        age=input("Enter age of the Employee: ")
        gender=raw_input("Enter Gender of the Employee: ")
        db_in(fname,lname,salary,dept,desig,addr,age,gender)
    elif(choice==2):
		count=count()
		if(count==0):
			print "We dont have any data, Please fill in some"
		else:
			i=input("Enter ID of the Employee ")
			disp(i)
    elif(choice==3):
		count=count()
		if(count==0):
			print "We dont have any data, Please fill in some"
		else:
			disp(0)
    elif(choice==4):
		print "Exiting Bye..."
    elif(choice==0):
		print "Exiting Bye..."
    else:
		print "Wrong Choice....."        
