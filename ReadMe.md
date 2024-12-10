Pandas CSV Analysis Project:  Spotify_Analysis

This is a simple Python script that uses the Pandas library to analyze a dataset of popular Spotify songs. The dataset contains information about song names, artists, release dates, and the number of streams. I got the dataset from Kaggle, and it’s called “Top Spotify Songs.” The script has a menu that lets you explore and filter the data in different ways.

How to Run
1. Make sure you have Python installed.
2. You’ll need Pandas. If you don’t have it, install it by running `pip install pandas` in your terminal or command prompt.
3. Download the dataset `Popular_Spotify_Songs.csv` and put it in the same folder as this script.
4. Open the script in VS Code.
5. Run the script and follow the on-screen menu.
6. To bring up the menu, open up a terminal window and type: python .\spotify_analysis.py and hit enter.
7. The menu comes up and then you can select your option.
8. After making your selection the menu will come back up, you need to scroll above the menu, to see your previous results.

What It Does
- The program has a menu with 7 options:
1. Show Sample Data
2. Find Artist
3. Help
4. Top 10 Streamed Songs
5. Bottom 10 Streamed Songs
6. List All Song Names
7. Exit
Notes
•	Some options (like searching artists) use filters, so it’ll show results that match the name you type. For example, typing "Taylor Swift" will bring up all songs where her name appears.
•	If you don’t input the right stuff (like a number from the menu), the program will just ask again until it gets something valid.  
•	After entering your option besides artist, you may have to scroll up in the terminal to find your results. If 2 is selected then you will enter your artist and the results will then be above the new menu that appears.

Things to Know
•	This is kind of a simple project, but it helped me learn how to use Pandas. It’s not perfect, so there might be bugs.
•	The script is designed for basic exploration of the data. If you want more advanced analysis, you’ll probably need to add to the list of stuff yourself, but this is just a basic csv pandas code for this project.

Issues I Had
•	Figuring out how to let the user input stuff like artist names without crashing the program if they typed something weird.
•	Making the streams column look nice with commas.
•	I used what we learned in class, but I also got help from W3Schools.



