# TO-DO LIST

task = []
def done_task(task_index):
    if task_index<=len(task):
        print(f"{task_index}.{task[task_index-1]['task']} -> [{'PENDING' if task[0]['done'] else 'DONE'}]")
        task[task_index-1]['done']=True
    else:
        print(f"NO TASK EXIST AT POSITION {task_index}")
def delete_task(remove_index):
    print(f"{task[remove_index-1]['task']} HAS BEEN DELETED FROM THE TO-DO LIST.")
    task.pop(remove_index-1)
def add_task(tasks):
    task.append({'task':tasks,"done":False})
    print(f"YOUR TASK {tasks} IS ADDED IN THE LIST.")
def show_task():
    if task:
        print("YOUR T0-DO LIST:")
        for i,j  in enumerate(task):
            status = "DONE" if j['done'] else 'PENDING'
            print(f"{i+1}.{j['task']} -> [{status}]")
    else:
        print("YOUR TO-DO LIST IS EMPTY.")        


def main():
    print("=================YOUR TO-DO LIST================")
    while(True):
        print("PRESS 1 TO ADD TASK.")
        print("PRESS 2 TO DELETE TASK.")
        print("PRESS 3 TO SHOW TASK.")
        print("PRESS 4 TO MARK TASK DONE.")
        print("PRESS 0 TO QUIT.")
    
        choice= int(input("ENTER YOUR CHOICE:"))
        if choice == 1:
            task= input("ENTER THE TASK YOU WANT TO ADD:")
            add_task(task)
        elif choice == 0:
            print("======THANKS FOR USING OUR TO-DO LIST======")
            break 
        elif choice == 3:
           show_task()
   
        elif choice == 2:
            index = int(input("ENTER THE TASK NO. YOU WANT TO DELETE."))
            delete_task(index)  

        elif choice == 4:
            mark = int(input("ENTER WHICH TASK YOU WANT TO MARK AS DONE:"))
            done_task(mark)
      

main()