import json

def load_data():
    try:
        with open ("youtube.txt", "r") as file:
            test = json.load(file)
            # print(test)
            return test
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def data_save_helper(videos):
    with open ("youtube.txt", "w") as file:
        json.dump(videos, file)

def list_all_video(videos):
    print("\n")
    print("*" * 100)
    print("---List Of Your All Videos---")
    for index, video in enumerate(videos, start = 1):
        print(f"{index}. Name: {video['Name']}, || Duration: {video['Time']}")
    print("*" * 100)

def add_video(videos):
    name = input("Enter Video Name: ")
    time = input("Enter Video Time: ")
    videos.append({'Name' : name, 'Time' : time})
    data_save_helper(videos)

def update_video(videos):
    list_all_video(videos)
    index = int(input("Enter The Index Value Of The Video You Want To Update: "))
    if 1<= index <= len(videos):
        name = input("Enter The Name Of The Video: ")
        time = input("Enter The Time Of The Video: ")
        videos[index - 1] = {'Name': name, 'Time': time}
        data_save_helper(videos)
    else:
        print("Invalid Index Selected")

def delete_video(videos):
    list_all_video(videos)
    index = int(input("Enter The Video Number You Want To Delete: "))
    if 1<= index <= len(videos):
        del videos[index - 1]
        data_save_helper(videos)
    else:
        print("Invalid Index Selected")

    print(f"Index No: {index} Video Is Deleted Sucessfully!")

def main():
    videos = load_data()
    while True:
        print("\n-----X YouTube Video Mangae X-----")
        print("*** Select Your Choice ***")
        print("1. List of all YouTube Videos")
        print("2. Add YouTube Video")
        print("3. Update YouTube Video Detail")
        print("4. Delete YouTube Video")
        print("5. Exit The App\n")
        choice = input("Enter Your Choice: ")
        # print(videos)

        match choice:
            case '1':
                list_all_video(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break        
            case _:
                print("Invalid Choice")

if __name__ == "__main__":
    main()