from pymongo import MongoClient
from bson import ObjectId

# Not A Good Idea To Include ID And Password Here:
client = MongoClient("mongodb+srv://new_user_101:Cb8dL5sZTx7Dnt3F@cluster0.l4jty4i.mongodb.net/")
try:
    client.admin.command('ping')
    print("Connected successfully!")
except Exception as e:
    print(e)

db = client["ytmanager"]
video_collection = db["videos"]


def list_of_videos():
    for video in video_collection.find():
        print(f"ID: {video.get('_id')} Name: {video.get('name')} And Time: {video.get('time')}")

def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})

def update_video(video_id, new_name, new_time):
    try:
        video_collection.update_one(
            {'_id': ObjectId(video_id)},
            {"$set": {"name": new_name, "time": new_time}}
        )
    except:
        print("Invalid Video ID")

def delete_video(video_id):
    video_collection.delete_one({'_id': ObjectId(video_id)})

def main():
    while True:
        print("\n-----X YouTube Video Mangae X-----")
        print("*** Select Your Choice ***")
        print("1. List of all YouTube Videos")
        print("2. Add YouTube Video")
        print("3. Update YouTube Video Detail")
        print("4. Delete YouTube Video")
        print("5. Exit The App\n")
        choice = input("Enter Your Choice: ")

        if choice == '1':
            list_of_videos()
        elif choice == '2':
            name = input("Enter Video Name: ")
            time = input("Enter Video Time: ")
            add_video(name, time)
        elif choice == '3':
            video_id = input("Enter Video ID To Update: ")
            name = input("Enter Video Name: ")
            time = input("Enter Video Time: ")
            update_video(video_id, name, time)
        elif choice == '4':
            video_id = input("Enter Video ID To Delete: ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid Choice!")

if __name__ == "__main__":
    main()