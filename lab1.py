# Variables representing the movie
movie_title = "Inception"
movie_rating = 3
popularity_score = 72.65

# Recommendation based on rating and popularity
if movie_rating >= 4 and popularity_score > 80:
    print("Highly recommended")
elif movie_rating >= 3 and popularity_score > 70:
    print("I recommend it. It is good")
elif movie_rating <= 2 and popularity_score > 60:
    print("You should check it out!")
elif movie_rating <= 2 and popularity_score < 50:
    print("Don't watch it. It is a waste of time")
