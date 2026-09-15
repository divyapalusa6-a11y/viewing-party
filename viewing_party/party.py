# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating): # if there is no title, genre, or rating, return None
    movie_dict = {}
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
def get_unique_watched(user_data):
    user_movies_list = set() # creates a set of movies with the unique movies that the user has watched, but their friends have not
    friend_movies_list = set()
    only_user_watched = [] # creates a list of movies with the unique movies that the user has watched, but their friends have not
    
    for movie in user_data["watched"]:
        user_movies_list.add(movie["title"])
        
    for friend in user_data["friends"]:
        for friend_movie in friend["watched"]:
            friend_movies_list.add(friend_movie["title"])
    only_user_watched_set = list(user_movies_list - friend_movies_list)
    for movie in user_data["watched"]:
        if movie["title"] in only_user_watched_set:
            only_user_watched.append(movie)
    return only_user_watched

def get_friends_unique_watched(user_data):
    
    user_movies_list = set()
    friend_movies_list = set()
    only_friends_watched = [] 
    # creates a list of movies with the unique movies that the user's friends have watched, but the user has not
    for movie in user_data["watched"]:
        user_movies_list.add(movie["title"])
    for friend in user_data["friends"]:
        for friend_movie in friend["watched"]:
            friend_movies_list.add(friend_movie["title"])
    only_friends_watched_set = list(friend_movies_list - user_movies_list)

    for friend in user_data["friends"]:
        for friend_movie in friend["watched"]:
            if friend_movie["title"] in only_friends_watched_set and friend_movie not in only_friends_watched:
                only_friends_watched.append(friend_movie)            
    return only_friends_watched

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

