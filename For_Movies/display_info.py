from Movies_class import Movies,Movie
print("Welcome to our small project")


print("\n"*2)
try:
    movie_name=input("enter the movie name: ")
    movie=Movie(movie_name)
    movie.get_data()
    movie.get_title()
    movie.get_overview()
    movie.get_rating()
    movie.get_vote_count()
    movie.get_date()
    movie.format_data()
    show_more_info=input(f"do you want more information about any movie related to this move{movie_name}...(Yes or  No)")
    if show_more_info.lower()=="yes" or show_more_info.lower()=="y":
        movie=Movies(movie_name)
        movie.get_data()
        movie.get_title()
        movie.get_overview()
        movie.get_rating()
        movie.get_vote_count()
        movie.get_date()
        movie.format_data() 
except IndexError as err:
    print(f"the {movie_name} that you entered dose not exist on our list")