#MELODYHUB CODE

#example music
#TITLE --- ARTIST --- GENRE --- MOOD
#Happy --- Pharrell Williams --- Pop --- happy
#Hey Barbara --- IV of Spades --- Funk --- happy
#Can't Stop the Feeling! --- Justin Timberlake --- Pop --- happy
#Ere --- Juan Carlos --- Pop --- sad
#Someone Like You --- Adele --- Pop --- sad
#The Scientist --- Coldplay --- Rock --- sad
#Kiss The Rain --- Yiruma --- Classical --- focused
#Runaway --- AURORA --- Pop --- focused
#Bad --- wave to earth --- jazz --- focused
#Billie Jean --- Michael Jackson --- Pop --- party
#Enter Sandman --- Metallica --- Metal --- party
#Dancing Queen --- Abba --- Disco --- party
#Shape of You --- Ed Sheeran --- Pop --- chill
#Espresso --- Sabrina Carpenter --- Funk ---chill
#Golden Hour --- JVKE --- Pop --- chill

music_list = []

valid_genres = [
    "Pop", "Rock", "Rap", "Metal", "R&B", "Funk", "Jazz",
    "Blues", "Country", "Classical", "Reggae", "EDM", "Disco"
]
valid_moods = ["happy", "sad", "focused", "party", "chill"]

def display_music(index, music):
    print(f"{index}. {music['title']} by {music['artist']} - Genre: {music['genre']}, Mood: {music['mood']}")

print("\nWelcome to MelodyHub!")

while True:
    print("\n[1] Add Music")
    print("[2] View Stored Music")
    print("[3] Generate Playlist")
    print("[4] Remove Music")
    print("[5] Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        print("\n--- Add Music ---")
        title = input("Enter music title: ")
        artist = input("Enter artist name: ")

        print("-Choose genre (Pop, Rock, Rap, Metal, R&B, Funk, Jazz, Blues, Country, Classical, Reggae, EDM, Disco)")
        while True:
            genre = input("Enter genre: ").title()
            if genre in valid_genres:
                break
            else:
                print("Invalid genre. Please choose from the list.")

        while True:
            mood = input("Enter mood tag (happy, sad, focused, party, chill): ").lower()
            if mood in valid_moods:
                break
            else:
                print("Invalid mood. Please enter a valid mood.")

        music = {
            "title": title,
            "artist": artist,
            "genre": genre,
            "mood": mood
        }
        music_list.append(music)
        print("\nMusic added successfully!")

    elif choice == "2":
        print("\n--- Stored Music ---")
        if music_list:
            sorted_music_list = sorted(music_list, key=lambda x: x['title'].lower())
            for i, music in enumerate(sorted_music_list, 1):
                display_music(i, music)
        else:
            print("No music stored yet.")

    elif choice == "3":
        print("\n--- Generate Playlist ---")
        if not music_list:
            print("No music stored in inventory.")
            continue

        print("Select mood:")
        print("[1] Happy")
        print("[2] Sad")
        print("[3] Focused")
        print("[4] Party")
        print("[5] Chill")

        mood_choice = input("Choose a mood (1-5): ")
        mood_map = {"1": "happy", "2": "sad", "3": "focused", "4": "party", "5": "chill"}

        selected_mood = mood_map.get(mood_choice)
        if selected_mood:
            playlist = [s for s in music_list if s["mood"] == selected_mood]
            if playlist:
                print(f"\n--- {selected_mood.capitalize()} Playlist ---")
                for i, music in enumerate(playlist, 1):
                    print(f"{i}. {music['title']} by {music['artist']} - Genre: {music['genre']}")
            else:
                print(f"\nNo music found with mood: {selected_mood}")
        else:
            print("Invalid mood selection.")

    elif choice == "4":
        print("\n--- Remove Music ---")
        if music_list:
            for i, music in enumerate(music_list, 1):
                print(f"{i}. {music['title']} by {music['artist']}")
            try:
                music_to_remove = int(input("Enter the number of the music to remove: "))
                if 1 <= music_to_remove <= len(music_list):
                    removed = music_list.pop(music_to_remove - 1)
                    print(f"\nRemoved '{removed['title']}' by {removed['artist']}.")
                else:
                    print("Invalid number.")
            except ValueError:
                print("\nPlease enter a valid number.")
        else:
            print("No music available to remove.")

    elif choice == "5":
        print("\nThank you for using MelodyHub! Keep the vibes going!\n")
        break

    else:
        print("\nInvalid option. Please select 1-5.")
