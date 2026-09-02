import sqlite3

con = sqlite3.connect("youtube_videos.db")

cursor = con.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
               )
''')

def list_of_videos():
    cursor.execute("SELECT * FROM videos")
    print("\n")
    print("*" * 100)
    for row in cursor.fetchall():
        print(row)
    print("*" * 100)

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    con.commit()

def update_video(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    con.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    con.commit()
    print("Selected Video Deleted Sucessfully")

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
    con.close()

if __name__ == "__main__":
    main()