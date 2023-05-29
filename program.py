from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfilename

firstEmployee = []
employeeSSN = 0
employeeIndex = 0

def cls():
    print("\n" * 50)

def employeeFormattedInfo(name, ssn, phone, email, salary):
    print("")
    print('-----------------{0:s}------------------------------'.format(name))
    print('SSN: {0:s}'.format(ssn))
    print('Phone: {0:s}'.format(phone))
    print('Salary: ${0:s}'.format(salary))
    print("------------------------------------------------------")
    print("")

def viewEmployeeInfo():
    cls()
    print("--------------------------------------------------------------------")
    print("                         View all employees in the system\n")
    print("--------------------------------------------------------------------")
    print("")
    if len(firstEmployee) == 0:
        print("                      No employees in the list.\n")
    else:
        for i in range(0, len(firstEmployee)):
            line = firstEmployee[i].split(',')
            employeeFormattedInfo(line[0], line[1], line[2], line[3], line[4])
    input('Press any key to go back to the main menu:')
    cls()

def addEmployeeToList():
    cls()
    print("-----------------------------------------------------------------")
    print("")
    print("                 Add Employee Info")
    print("")
    print("-----------------------------------------------------------------")
    print("")
    try:
        name = input('Name: ')
        ssn = input('SSN: ')
        phone = input('Phone: ')
        email = input('Email: ')
        salary = input('Employee salary: ')
        line = name + ',' + ssn + ',' + phone + ',' + email + ',' + salary
        firstEmployee.append(line)
    except:
        cls()
        addEmployeeToList()
    print("\nEmployee info has been successfully added")
    print("------------------------------------------------------------------")
    print("")
    try:
        option = input('Enter q/Q to return to the main menu, or any other key to add employee: ')
        if option.lower() == "q":
            cls()
        else:
            cls()
            addEmployeeToList()
    except:
        cls()
        addEmployeeToList()

def printOptions():
    print("-------------------Employee Management System-------------------")
    print('There are ({0:d}) employees in the system'.format(len(firstEmployee)))
    print("\n--------------------------------------------------------------")
    print("1. View all employees \n")
    print("2. Add new employee \n")
    print("3. Add multiple employees \n")
    print("4. Seaerch SSN \n")
    print("5. Edit\n")
    print("6. To export file\n")
    print("8 to import\n")
    try:
        answer = int(input('Please enter your option number: '))
    except ValueError:
        print("Not a number")
        return 100
    print("")
    print("----------------------------------------------------------------")
    return answer

def searchEmployeeBySSN(isForEdit):
    cls()
    print("----------------------------------------------------------------")
    print("                            Search employee by SSN")
    print("\n---------------------------------------------------------------")
    if len(firstEmployee) == 0:
        input("\n        no employee in the list.\n")
        cls()
    else:
        try:
            ssn = input('please enter q/Q to exit or enter a new employee SSN: ')
            global employeeSSN
            employeeSSN = ssn
            if ssn.lower() == "q":
                return 0
            for i, line in enumerate(firstEmployee):
                if line.split(',')[1] == ssn:
                    global employeeIndex
                    employeeIndex = i
                    employeeFormattedInfo(line[0], line[1], line[2], line[3], line[4])
                    break
            else:
                print("\n               can not find an employee with the info you provided.\n")
                return 0
        except ValueError:
            searchEmployeeBySSN(0)
        try:
            if (isForEdit == 0):
                option = input('enter q/Q or any key')
                if option.lower() == "q":
                    cls()
                else:
                    searchEmployeeBySSN(0)
        except:
            cls()


def editEmployeeInfo():
    cls()
    result = searchEmployeeBySSN(1)
    if result != 0:
        name = input('name: ')
        ssn = input('SSN: ')
        phone = input('phone: ')
        email = input('email: ')
        salary = input('employee sal.: ')
        del firstEmployee[employeeIndex]
        line = name+',' +employeeSSN +',' +phone +',' +email +','
        firstEmployee.insert(employeeIndex, line)
        input("\nEmployee info has been updated")

def to_export():
    file = asksaveasfile(mode='w', defaultextension=".txt")
    if file is None:
        return
    for employee in firstEmployee:
        file.write(employee + "\n")
    file.close()

def to_import():
    file = askopenfilename(defaultextension=".txt")
    if file is None:
        return
    with open(file, "r") as f:
        lines = f.readlines()
        for line in lines:
            firstEmployee.append(line.strip())
def add_five():
    lstName = []
    lstEmployees = []
    counter = 0
    while counter < 5:
        print("-----------------------------------------------------------------------------\n")
        print('                         Number of Employees ({0:d})'.format(counter))
        print("-----------------------------------------------------------------------------\n")
        name = input('Enter employee name: ')
        lstName.insert(counter, name)
        ssn = input('enter employee SSN: ')
        phone = input('enter employee email: ')
        email = input('enter employee email: ')
        salary = input('enter employee salary: $ ')
        line = name + ',' + ssn + ',' + phone + ',' + email + ',' + salary
        lstEmployees.insert(counter, line)
        counter = counter + 1
        if counter > 5:
            break
        else:
            continue

    while True:
        print("-------------------------------------------------------------------------------\n")
        print(" enter 1 to display {0:s}'s info ".format(lstName[0]))
        print(" enter 2 to display {0:s}'s info)".format(lstName[1]))
        print(" enter 3 to display {0:s}'s info)".format(lstName[2]))
        print(" enter 4 to display {0:s}'s info)".format(lstName[3]))
        print(" enter 5 to display {0:s}'s info)".format(lstName[4]))
        index = input()
        if index in ['1', '2', '3', '4', '5']:
            print(lstEmployees[int(index) - 1])
        else:
            break

while True:
    cls()
    mode = printOptions()
    if mode == 1:
        cls()
        viewEmployeeInfo()
    if mode == 2:
        cls()
        addEmployeeToList()
    if mode ==3:
        cls()
        employee_info()
    if mode ==4:
        cls()
        searchEmployeeBySSN(0)
    if mode ==5:
        cls()
        editEmployeeInfo()
    if mode ==6:
        cls()
        to_export()
    if mode ==7:
        cls()
        to_import()
    if mode ==8:
        cls()
        add_five()
