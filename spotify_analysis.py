# Import necessary libraries
import pandas as pd
from IPython.display import display

# Set display options for better readability
pd.options.display.max_rows = 16

# Load the dataset into a DataFrame
spotify_data = pd.read_csv(
    "Popular_Spotify_Songs.csv",
    header=0,
    usecols=["Song_Name", "Artist_Name", "Date", "Streams"]  
)

# Ensure 'Streams' is numeric 
spotify_data["Streams"] = spotify_data["Streams"].replace({',': ''}, regex=True).astype(int)

# Format the "Streams" for display 
spotify_data["Formatted_Streams"] = spotify_data["Streams"].apply(lambda x: f"{x:,}")

# Define menu options
options = [
    "Show Sample Data",
    "Find Artist",
    "Help",
    "Top 10 Streamed Songs",
    "Bottom 10 Streamed Songs",
    "List All Song Names",
    "Exit",
]

def display_options():
    # Display the menu options.
    print("\nAvailable Options:")
    for idx, option in enumerate(options, start=1):
        print(f"{idx}. {option}")

def get_user_selection():
    # Prompt the user for their menu selection.
    while True:
        try:
            selection = int(input("\nSelect an option (1-7): "))
            if 1 <= selection <= len(options):
                return selection
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def find_artist():
    # Search for a specific artist in the dataset.
    artist_name = input("Enter the artist's name: ").title()
    matching_artists = spotify_data[spotify_data["Artist_Name"].str.contains(artist_name, na=False)]
    if matching_artists.empty:
        print(f"No results found for '{artist_name}'.")
    else:
        display(matching_artists)

def show_help():
    # Display help information.
    print("Refer to the README file for instructions.")

def execute_choice(selection):
    # Execute the function based on user selection.
    if selection == 1:
        print(spotify_data.head())  # Show sample data
    elif selection == 2:
        find_artist()
    elif selection == 3:
        show_help()
    elif selection == 4:
        display(spotify_data.nlargest(10, "Streams"))  # Top 10 streamed songs
    elif selection == 5:
        display(spotify_data.nsmallest(10, "Streams"))  # Bottom 10 streamed songs
    elif selection == 6:
        display(spotify_data["Song_Name"])  # List all song names
    elif selection == 7:
        print("Exiting the program. Goodbye!")
        exit()

# Main execution loop
if __name__ == "__main__":
    while True:
        display_options()
        user_selection = get_user_selection()
        execute_choice(user_selection)
