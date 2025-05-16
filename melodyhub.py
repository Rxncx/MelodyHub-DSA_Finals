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

# MelodyHub: A simple terminal-based music inventory and playlist generator.

# List that stores all the added music
music_list = []

# Valid options for genre and mood, used for validation
VALID_GENRES = [
    "Pop", "Rock", "Rap", "Metal", "R&B", "Funk", "Jazz",
    "Blues", "Country", "Classical", "Reggae", "EDM", "Disco"
]
VALID_MOODS = ["happy", "sad", "focused", "party", "chill"]

def display_music(i, music):
    """Display a formatted line of music information."""
    print(f"{i}. {music['title']} by {music['artist']} - Genre: {music['genre']}, Mood: {music['mood']}")

def display_menu():
    """
    Show the main menu options to the user.
    This runs every time the user completes an action and returns to the main menu.
    """
    print("\n[1] Add Music")
    print("[2] View Stored Music")
    print("[3] Generate Playlist")
    print("[4] Remove Music")
    print("[5] Exit")

def add_music():
    """
    Allow the user to add a music entry.
    The function asks for title, artist, genre, and mood.
    It validates genre and mood before adding the entry to the music list.
    """
    # Prompting user for music details
    print("\n--- Add Music ---")
    title = input("Enter music title: ")
    artist = input("Enter artist name: ")

    # Validating genre
    print("-Choose genre (Pop, Rock, Rap, Metal, R&B, Funk, Jazz, Blues, Country, Classical, Reggae, EDM, Disco)")
    while True:
        genre_input = input("Enter genre: ").strip()
        if genre_input.lower() in [g.lower() for g in VALID_GENRES]: # checking if genre is valid and converting to lowercase for comparison.
            genre = next(g for g in VALID_GENRES if g.lower() == genre_input.lower()) # use correct casing from VALID_GENRES
            break # if genre is valid, break the loop.
        else:
            print("Invalid genre. Please choose from the list.") # notifying the user that genre is invalid.

    # Validating mood
    while True:
        mood_input = input("Enter mood tag (happy, sad, focused, party, chill): ").strip()
        if mood_input.lower() in [m.lower() for m in VALID_MOODS]: # checking if mood is valid and converting to lowercase for comparison.
            mood = next(m for m in VALID_MOODS if m.lower() == mood_input.lower()) # use correct casing from VALID_MOODS
            break # if mood is valid, break the loop.
        else:
            print("Invalid mood. Please enter a valid mood.") # notifying the user that mood is invalid.

    # Add the validated music entry to the list
    music = {
        "title": title,
        "artist": artist,
        "genre": genre,
        "mood": mood
    }
    music_list.append(music)
    print("\nMusic added successfully!") # notifying the user that music has been added.

def view_stored_music():
    """
    Show all the stored music in alphabetical order by title.
    If the list is empty, notify the user.
    """
    print("\n--- Stored Music ---")
    if music_list:
        # Sort alphabetically by title (case-insensitive)
        sorted_music = sorted(music_list, key=lambda x: x['title'].lower())
        for i, music in enumerate(sorted_music, 1):
            display_music(i, music)
    else:
        print("No music stored yet.") # notifying the user that no music is stored yet.

def generate_playlist():
    """
    Generate and display a playlist based on the user's mood selection.
    Shows matching songs if available. If not, displays appropriate messages.
    """
    print("\n--- Generate Playlist ---")
    if not music_list: # checking if music list is empty.
        print("No music stored in inventory.") #notifying the user that no music is stored yet.
        return # if music list is empty, return to the main menu of generate playlist.

    # Ask user to select a mood
    print("Select mood:")
    print("[1] Happy")
    print("[2] Sad")
    print("[3] Focused")
    print("[4] Party")
    print("[5] Chill")

    mood_map = {"1": "happy", "2": "sad", "3": "focused", "4": "party", "5": "chill"}
    mood_choice = input("Choose a mood (1-5): ") # prompting the user to choose a mood.
    selected_mood = mood_map.get(mood_choice) # mapping the mood choice to the corresponding mood.

    if selected_mood:
        # Filter songs that match the selected mood and sort alphabetically by title
        playlist = sorted(
            [m for m in music_list if m['mood'] == selected_mood],
            key=lambda x: x['title'].lower()
        )
        if playlist:
            print(f"\n--- {selected_mood.capitalize()} Playlist ---")
            for i, music in enumerate(playlist, 1): # enumerating the playlist.
                print(f"{i}. {music['title']} by {music['artist']} - Genre: {music['genre']}")
        else:
            print(f"\nNo music found with mood: {selected_mood}") # notifying the user that no music is found with the selected mood.
    else:
        print("\nInvalid mood selection.") # notifying the user that mood selection is invalid.

def remove_music():
    """
    Display all stored music and let the user remove one by number.
    Handles invalid numbers and empty list situations.
    """
    print("\n--- Remove Music ---")
    if music_list:
        for i, music in enumerate(music_list, 1): # enumerating the music list.
            print(f"{i}. {music['title']} by {music['artist']}") # displaying the music list.
        try:
            music_to_remove = int(input("Enter the number of the music to remove: ")) # prompting the user to enter the number of the music to remove.
            if 1 <= music_to_remove <= len(music_list): # checking if the entered number is valid.
                removed = music_list.pop(music_to_remove - 1) # removing the music from the list.
                print(f"\nRemoved '{removed['title']}' by {removed['artist']}.") # notifying the user that music has been removed.
            else:
                print("\nInvalid number.") # notifying the user that the entered number is invalid.
        except ValueError:
            print("\nPlease enter a valid number.") # notifying the user that the entered value is not a number.
    else:
        print("No music available to remove.") # if music list is empty, notifying the user that no music is available to remove.

def main():
    """
    The main loop of the program.
    Keeps running until the user chooses to exit (option 5).
    Handles routing to all features based on the user's input.
    """
    print("\nWelcome to MelodyHub!")
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ") # prompting the user to choose an option.

        if choice == "1":
            add_music()
        elif choice == "2":
            view_stored_music()
        elif choice == "3":
            generate_playlist()
        elif choice == "4":
            remove_music()
        elif choice == "5":
            print("\nThank you for using MelodyHub! Keep the vibes going!\n") # notifying the user that they are exiting the program.
            break
        else:
            print("Invalid option. Please select 1-5.") # notifying the user that the entered option is invalid.

main()
