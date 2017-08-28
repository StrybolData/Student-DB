import math
import datetime
import csv

students = {}


def genie():


    while True:

        user_input = input("Please insert your command, cause your will is my command: ")
        user_input2= user_input.split()
        if (user_input.find('goaway')!= -1):
            return exit()
        else:
            dispatcher(user_input2)


def dispatcher(commands):
# takes a user command and then calls a corresponding function
#make a list of the commands
# if (cmd_in[0]=='add'):
# add_user(cmd_in[1],cmd_in[2],cmd_in[3])
    if commands[0] ==  'add':
        print ('I will add this master')
        addcomm(commands[1], commands[2], commands[3])
    if commands[0] ==  'delete':
        print ('I will try to delete this student master')
        delcomm(commands[1])
    if commands[0] ==  'average':
        print ('I will calculate the average student scores master')
        averagecomm()
    if commands[0] ==  'load':
        print ('These are your historical records master:')
        load_students(students)
    if commands[0] ==  'print':
        print ('I will print the DB master')
        printercomm()

def load_students(students):
    file1= open('filename.csv','r')
    csv_file= file1.read()
    print(students)
    csv_file.close()

def addcomm (name_student,job_student,python_exp):
    if name_student in students.keys():
        display_log()
        print('Sorry master, but this name already exists in the database')
    else:
        students[name_student] = (job_student, python_exp)
    display_log()
    save ()
    print("Added: ",name_student, job_student, python_exp )
    return

def delcomm (name_student):
    if name_student in students.keys():
        del students[name_student]
        display_log()
        save ()
        print(name_student, 'has been deleted from student database master')
    else:
        display_log()
        print('Sorry, this student is not present in the database master')
    print("Your student db now looks as follows:", students)
    return

def averagecomm ():
    print('Master, let me calculate the average of the python scores')
    scores = []
    for name_student in students.keys():
        scores.append (int(students[name_student][1]))
    #python_sum = sum(scores)
    amount_students=len(students)
    average_scores= (sum(scores)/amount_students)
    print ('----------')
    display_log()
    save ()
    print('the students average score is:', str(average_scores))
    print ('----------')
    return

#final = {}
#for k in dict1[0].Keys():
#    final[k] = sum(x[k] for x in dict1)
#return final

def display_log ():
     print ('----------')
     d_date = datetime.datetime.now()
     reg_format_date = d_date.strftime("%d-%m")
     reg_format_date2 = d_date.strftime("%I:%M:%S")
     print(reg_format_date + "|" +  reg_format_date2)
     return

def save ():
    with open('filename.csv', 'w', newline='') as csvfile:
       writer = csv.writer(csvfile, delimiter =";", quotechar ='/')
       for name_student in students.keys():
          writer.writerow([name_student, students[name_student][0], students[name_student][1]])
    print ('saved in csv file')
    return



def printercomm ():
    print ('----------')
    for name_student in students.keys():
        amount_student= str(len(students))
        display_log()
        print ("Your student db contains the following amount of students:", amount_student)
        min_score= str(min(students[name_student][1]))
        display_log()
        print("The lowers score is:", min_score)
        max_score= str(max(students[name_student][1]))
        display_log()
        print("The highest score is:", max_score)

    for name_student in students.keys():
        display_log()
        print(name_student, students[name_student], students[name_student][0], students[name_student][1])
    print ('----------')


