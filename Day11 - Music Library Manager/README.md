Objective:
Practice reading and writing JSON files in Python, building and navigating nested dictionaries and lists, aggregating data, and writing filtered results to output files.

Instructions:

Create a file called music.json by copying the data below.
Read the JSON file using the json module and store all records in a variable called library.
Build a dictionary called artists where each key is an artist name and the value is a list of dictionaries, each containing: title, genre, duration_seconds, plays.
Calculate the total plays and total listening time (in seconds) for each artist. Store results in a dictionary called stats.
Find and display the artist with the most total plays.
Find and display the most popular genre by total plays across all songs.
Filter all songs with more than 200 plays and store them in a list called popular_songs.
Display the top 3 songs by plays.
Save a file called popular_songs.json containing only the popular songs, written as a valid JSON file.
Save a file called artist_report.txt with artists sorted by total plays (highest first), formatted as: Artist | Plays: X | Listening time: Xh Xm Xs.