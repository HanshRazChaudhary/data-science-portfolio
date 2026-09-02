import json

def load_task():
    try:
        with open ("To_Do.txt", "r") as file:
            to_do_file = json.load(file)
            return to_do_file
    except(FileNotFoundError):
        return []

def task_saver(tasks):
    with open ("To_Do.txt", "w") as file:
        json.dump(tasks, file)

def all_of_your_task(tasks):
    print("\n")
    print("*" * 100)
    print("-----X Yours To Do Lists X-----")
    for index, task in enumerate (tasks, start = 1):
        print(f"{index}. Task: {task['Task']}")
    print("*" * 100)

def add_task(tasks):
    task_name = input("Enter Your Task: ")
    tasks.append({'Task': task_name})
    task_saver(tasks)

def delete_task(tasks):
    all_of_your_task(tasks)
    index = int(input("Enter The Number Of The Task You Want To Delete: "))
    if 1 <= index <= len(tasks):
        del tasks[index - 1]
        task_saver(tasks)
    else: 
        print("Invalid Index Selected, Try Again!")

    print(f"Task No: {index} Is Deleted Successfully!")



def main():
    tasks = load_task()
    while True:
        print("------ To Do List ------")
        print("1. View Task")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")
        print("\n")
        choice = input("Please Select Your Choice: ")

        match choice:
            case "1" :
                all_of_your_task(tasks)
            case "2" :
                add_task(tasks)
            case "3" :
                delete_task(tasks)
            case "4" :
                break
            case _ :
                print("Invalid Choice, Please Try Again!")

if __name__ == '__main__':
    main()