import webbrowser 
class Movie():
    """ This class provides a way to store many movies with their related information"""
    def __init__(self, movie_title, movie_storyline, movie_poster, movie_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_youtube
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
