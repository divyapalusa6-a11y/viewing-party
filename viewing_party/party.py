# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating): # if there is no title, genre, or rating, return None
    if not title or not genre or rating is None:
        return None
    return {
        "title": title,
        "genre": genre,
        "rating": rating
    }
def add_to_watched(user_data, movie):
    watched_list = []
    # adds a movie to the user's watched list by the key "watched"
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    # adds a movie to the user's watchlist by the key "watchlist"
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    # checks if the movie is in the user's watchlist, and if it is, removes it from the watchlist and adds it to the watched list
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            return user_data
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

