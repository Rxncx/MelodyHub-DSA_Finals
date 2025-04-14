songs = []

while True:
    print("\nWelcome to MelodyHub!")
    print("[1] Add Music")
    print("[2] View Stored Music")
    print("[3] Generate Playlist")
    print("[4] Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        print("\n--- Add Music ---")
        title = input("Enter song title: ")
        artist = input("Enter artist name: ")
        genre = input("Enter genre: ")
        mood = input("Enter mood tag (happy, sad, focused, party, etc.): ")

        song = {
            "title": title,
            "artist": artist,
            "genre": genre,
            "mood": mood.lower()
        }
        songs.append(song)
        print("Music added successfully!")

    elif choice == "2":
        print("\n--- Stored Music ---")
        if songs:
            for i, song in enumerate(songs, 1):
                print(f"{i}. {song['title']} by {song['artist']} - Genre: {song['genre']}, Mood: {song['mood']}")
        else:
            print("No music stored yet.")

    elif choice == "3":
        print("\n--- Generate Playlist ---")
        print("Select mood:")
        print("[1] Happy")
        print("[2] Sad")
        print("[3] Focused")
        print("[4] Party")

        mood_choice = input("Choose a mood (1-4): ")
        mood_map = {"1": "happy", "2": "sad", "3": "focused", "4": "party"}

        selected_mood = mood_map.get(mood_choice)
        if selected_mood:
            playlist = [s for s in songs if s["mood"] == selected_mood]
            if playlist:
                print(f"\n--- {selected_mood.capitalize()} Playlist ---")
                for i, song in enumerate(playlist, 1):
                    print(f"{i}. {song['title']} by {song['artist']} - Genre: {song['genre']}")
            else:
                print(f"No songs found with mood: {selected_mood}")
        else:
            print("Invalid mood selection.")

    elif choice == "4":
        print("\nThank you for using MelodyHub! Keep the vibes going!")
        break
    else:
        print("Invalid option. Please select 1-4.")
