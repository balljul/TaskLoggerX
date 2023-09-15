#COMMAND LINE TO-DO LIST APPLICATION IN PYTHON
#PACKET BY DEEPANSHU MITTAL

#import argparse and datetime libraries
import argparse
from datetime import date

today = date.today()

#open the two text files to keep record of todo and done tasks
tf=open("todo.txt","r+")
df=open("done.txt","r+")

todo_data= tf.readlines()
done_todo_data= df.readlines()
c=len(done_todo_data)
p=len(todo_data)

#defining the arguments which will be passed to the parser
my_parser = argparse.ArgumentParser()
my_parser.add_argument('input1',
                       action='store', type=str, nargs='?',
                       default='default')
my_parser.add_argument('input2',
                       action='store', type=str,
                       nargs='?',
                       default='-1')

args = my_parser.parse_args()

#in case of user needs help about instructions
if(args.input1 == 'default' or args.input1 == 'help'):
    print("Usage :-")
    print('python todo.py add "todo item"  # Add a new todo')
    print('python todo.py ls               # Show remaining todos')
    print('python todo.py del NUMBER       # Delete a todo')
    print('python todo.py done NUMBER      # Complete a todo')
    print('python todo.py help             # Show usage')
    print('python todo.py report           # Statistics')

#in case uder want to get a report of previous tasks
elif(args.input1 == 'report'):
    print(today.strftime("%Y-%m-%d")+' Pending : '+str(p)+' Completed : '+str(c))

#in case of user wants to know remaining tasks
elif(args.input1 == 'ls' and p>0):
    for i in range(p,0,-1):
        line= todo_data[i-1].strip()
        print('['+str(i)+'] '+line)

#in case of user wants to know remaining tasks but todo list is empty
elif(args.input1 == 'ls'):
    print("There are no pending todos!")

#in case user want to add a new todo
elif(args.input1 == 'add' and args.input2 !='-1'):
    tf.write(args.input2+"\n")
    print('Added todo: "'+(args.input2)+'"')

#in case user want to add a new todo but forgot to paas the required todo task in the instruction
elif(args.input1 == 'add' and args.input2 == '-1'):
    print("Error: Missing todo string. Nothing added!")

#in case user want to delete the specific todo
elif(args.input1 == 'del' and args.input2!='-1' and int(args.input2) <= p and int(args.input2)>0):
    todo_data.remove(todo_data[int(args.input2)-1])
    tf.truncate(0)
    tf.seek(0)
    for line in todo_data:
        line= line.strip()
        tf.write(line+"\n")
    print('Deleted todo #'+(args.input2))

#in case user want to delete the specific todo but forgot to pass the required todo number
elif(args.input1 =='del' and args.input2 == '-1'):
    print("Error: Missing NUMBER for deleting todo.")

#in case user want to delete the specific todo but it doesn't occur in todo list
elif(args.input1 == 'del'):
    print("Error: todo #"+ str(int(args.input2)) +" does not exist. Nothing deleted.")

#in case user wants to mark a todo as done
elif(args.input1 == 'done' and args.input2!='-1' and int(args.input2) <= p and int(args.input2)>0):
    line= todo_data[int(args.input2)-1]
    df.write("x "+today.strftime("%Y-%m-%d")+" "+todo_data[int(args.input2)-1])
    todo_data.remove(todo_data[int(args.input2)-1])
    tf.truncate(0)
    tf.seek(0)
    for line in todo_data:
        line= line.strip()
        tf.write(line+"\n")
    print('Marked todo #'+(args.input2)+' as done.')

#in case user wants to mark a todo as done but forgot to pass the required todo number
elif(args.input1 =='done' and args.input2 == '-1'):
    print("Error: Missing NUMBER for marking todo as done.")

#in case user wants to mark a todo as done but passed an incorrect todo number
elif(args.input1 == 'done'):
    print("Error: todo #"+ str(int(args.input2)) +" does not exist.")

tf.close()
df.close()
