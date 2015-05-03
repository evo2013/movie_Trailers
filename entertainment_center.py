import media
import fresh_tomatoes

hunger_games = media.Movie("The Hunger Games: Catching Fire", 
			"In a dystopian future, each year two young representatives from 12 districts are selected by lottery to participate in The Hunger Games",
			"http://webagencydesign.org/movie_img/hgames.jpg",
			"https://www.youtube.com/watch?v=jyPnQw_Lqds")


frozen = media.Movie("Frozen",
	 	 "A Walt Disney film about newly crowned Queen Elsa who accidentally uses her power to turn things into ice to curse her home in infinite winter",
	 	 "http://webagencydesign.org/movie_img/frozen.jpg",
	 	 "https://www.youtube.com/watch?v=TbQm5doF_Uc")

tiger_dragon = media.Movie("Crouching Tiger Hidden Dragon",
	 	 "A timeless story that takes place in QING China when miracles were credible and spirits and gods were present in man's world",
	 	 "http://webagencydesign.org/movie_img/dragon.jpg",
	 	 "https://www.youtube.com/watch?v=iv_ed5VmoD8")

lawrence = media.Movie("Lawrence of Arabia",
	 	 "A film about the flamboyant and controversial British military figure, T. E. Lawrence, and his conflicted loyalties during his WW1 service in the Middle East",
	 	 "http://webagencydesign.org/movie_img/lawrence.jpg",
	 	 "https://www.youtube.com/watch?v=zmr1iSG3RTA")

ironman = media.Movie("Iron Man 3",
	 	 "A Marvel superhero story that pits brash-but-brilliant industrialist Tony Stark/Iron Man against an enemy whose reach knows no bounds",
	 	 "http://webagencydesign.org/movie_img/ironman.jpg ",
	 	 "https://www.youtube.com/watch?v=2CzoSeClcw0")

gandhi = media.Movie("Gandhi",
	 	 "The intriguing story about an extraordinary man who fought for a nonviolent, peaceful existence, and set an entire nation free",
	 	 "http://webagencydesign.org/movie_img/gandhi.jpg",
	 	 "https://www.youtube.com/watch?v=6oWqlb_TlLQ")

movies = [hunger_games, frozen, tiger_dragon, lawrence, ironman, gandhi]
fresh_tomatoes.open_movies_page(movies)
