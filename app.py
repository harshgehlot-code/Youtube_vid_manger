
import sqlite3

conn = sqlite3.connect('youtube_videos.db')

cursor = conn.cursor()

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
''')

def  list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def Add_videos(name, time):
    cursor.execute("INSERT INTO videos(name, time) VALUES (?, ?)", (name, time))
    conn.commit()
    
def update_videos(video_id, new_name, new_time):
        cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
        conn.commit()

def delete_videos(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    conn.commit()

def main():

    while True:
        print("\n Youtube video | Enter your chioce: ")
        print("1.List all videos: ")
        print("2. Add video: ")
        print("3. Update video: ")
        print("4. Delete video: ")
        print("5. Exit: ")

        choice = input("Enter your choice number: ")

        if choice == '1':
           list_videos()
        elif choice == '2':
            name = input("Enter the name of videos: ")
            time = input("Enter the time of videos: ")
            Add_videos( name, time)
        elif choice == '3':
            video_id = input("Enter videos Id to update: ")
            name = input("Enter the name of video: ")
            time = input("Enter the time of video: ")
            update_videos(video_id, name, time)
        elif choice == '4':
            video_id = input("Enter the video Id to be Delete: ")
            delete_videos(video_id)
        elif choice == '5':
            break
        else :
            print("Invalid choice. Please try again.")

    conn.close()

if __name__ == "__main__":
    main()