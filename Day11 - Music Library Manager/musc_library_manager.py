import json

with open("music.json") as f:
    library = json.load(f)
    artists = {}
    stats = {}
    for artist in library:
        name = artist["artist"]
        title = artist["title"]
        genre = artist["genre"]
        duration = int(artist["duration_seconds"])
        plays = int(artist["plays"])
        artist_info = {
            "title": title,
            "genre": genre,
            "duration": duration,
            "plays": plays,
        }
        if name not in artists:
            artists[name] = [artist_info]
        else:
            artists[name].append(artist_info)

    for (
        key,
        element,
    ) in artists.items():  # key = Arctic Monkeys / elemento = list of song
        for element in element:  # song
            counter = 0
            if key not in stats:
                counter_duration = element["duration"]
                counter_plays = element["plays"]
                stats[key] = {
                    "total_duration": counter_duration,
                    "total_plays": counter_plays,
                }
            else:
                stats[key]["total_duration"] += element["duration"]
                stats[key]["total_plays"] += element["plays"]

    most_total_plays_name = ""
    most_total_plays_counter = 0
    for name, info in stats.items():
        if info["total_plays"] > most_total_plays_counter:
            most_total_plays_counter = info["total_plays"]
            most_total_plays_name = name

    best_genre = {}
    for name, info in artists.items():
        for song in info:
            if song["genre"] not in best_genre:
                best_genre[song["genre"]] = song["plays"]
            else:
                best_genre[song["genre"]] += song["plays"]
    sorted_best_genre = sorted(best_genre.items(), key=lambda x: x[1], reverse=True)
    print(
        f"Most popular genre is {sorted_best_genre[0][0]} with {sorted_best_genre[0][1]} plays!"
    )

    popular_songs = []
    for name, info in artists.items():
        for song in info:
            if song["plays"] > 200:
                popular_songs.append({"title": song["title"], "plays": song["plays"]})
    sorted_popular_song = sorted(popular_songs, key=lambda x: x["plays"], reverse=True)
    print(
        "Best songs are: "
        + ", ".join(song["title"] for song in sorted_popular_song[:3])
    )


with open("popular_songs.json", "w") as file:
    json.dump(popular_songs, file, indent=4)

with open("artist_report.txt", "w") as file:
    artist_report = []
    for name, info in artists.items():
        for specific in info:
            artist_report.append(
                {
                    "artist": name,
                    "plays": specific["plays"],
                    "duration": specific["duration"],
                }
            )
    sorted_artist_report = sorted(artist_report, key=lambda x: x["plays"], reverse=True)
    for song in sorted_artist_report:
        h = song["duration"] // 3600
        m = (song["duration"] % 3600) // 60
        s = song["duration"] % 60
        file.write(
            f"{song['artist']} | Plays: {song['plays']} | Listening time: {h}h {m}m {s}s\n"
        )
