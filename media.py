import webbrowser

'''
Define the class 'Movie' with the __init__ function and describe the parameter values it takes.
Create the function 'show_trailer' to open the YouTube trailer for the Movie class.
'''
class Movie():
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)

