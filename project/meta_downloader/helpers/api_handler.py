import tmdbsimple as tmdb

class APIHelper:
    tmdb.API_KEY = '454b6ca4172e455fe7a7d8395c10d6d9'

    def __init__(self):
        self.search = tmdb.Search()
        self.movies = tmdb.Movies()

    def get_movie_data(self, title):
        self.search.movie(query=title)
        return self.search.results
    
    def get_popular_movies(self):
        top_rated = self.movies.top_rated()['results']
        popular = self.movies.popular()['results']
        upcoming = self.movies.upcoming()['results']

        return top_rated + popular + upcoming
    
if __name__ == '__main__':
    test = APIHelper()

    # print(test.get_popular_movies()[0:10])
    print(test.get_movie_data('Alien'))