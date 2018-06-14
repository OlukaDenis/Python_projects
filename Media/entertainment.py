import media
import fresh_tomatoes

black_panther = media.Movie("Black Panther",
                        "A boy who has toys and travelled from time to time",
                        "https://i.redd.it/8vim9yvff1901.jpg",
                        "https://www.youtube.com/watch?v=xjDjIWPwcPU")
#print (toy_story.title+". "+toy_story.storyline)

tomb_raider= media.Movie("Tomb Raider",
                        "A marine alien on the planet",
                        "https://static.gamespot.com/uploads/original/1557/15576725/3326663-tomb-raider-poster-alicia-vikander.jpg",
                        "https://www.youtube.com/watch?v=3KkhD0MnaJU")
#print (avatar.title+". "+avatar.storyline)
#avatar.show_trailer()

maze_runner= media.Movie("Maze Runner, Death Cure",
                        "A real reality show",
                        "https://cdn.flickeringmyth.com/wp-content/uploads/2017/12/Maze-Runner-Death-Cure-poster-5.jpg",
                        "https://www.youtube.com/watch?v=4-BTxXm8KSg")
infinty_war= media.Movie("Avengers infinity war",
                        "The war between avengers and an alien",
                        "http://oyster.ignimgs.com/wordpress/stg.ign.com/2018/04/avengers-infinity-war-imax.jpg",
                        "https://www.youtube.com/watch?v=6ZfuNTqbHE8")

pacific_rising= media.Movie("Pacific Rim Uprising",
                        "The war between humans and aliens",
                        "http://www.pacificrimmovie.co.uk/images/posters/Pacific-Rim-Uprising-Poster-02.jpg",
                        "https://www.youtube.com/watch?v=_EhiLLOhVis")

coco= media.Movie("Coco",
                        "The war between humans and aliens",
                        "https://ohmy.disney.com/wp-content/uploads/2017/09/Coco_Payoff_IG_Jpeg_v7-1.jpg",
                        "https://www.youtube.com/watch?v=Rvr68u6k5sI")

movies = [black_panther, tomb_raider, maze_runner, infinty_war, pacific_rising, coco]
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.__doc__)
