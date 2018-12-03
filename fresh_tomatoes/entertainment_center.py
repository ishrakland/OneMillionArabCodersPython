import media
import fresh_tomatoes
toy_story = media.Movie("Toy story",
	"A story of a boyand his toys",
	"https://upload.wikimedia.org/wikipedia/sco/b/b0/Avatar-Teaser-Poster.jpg",
	"https://www.youtube.com/watch?v=-9ceBgWV8io")

# print toy_story.storyline

avatar=media.Movie("avatar",
	"A story of avatar",
	"https://vignette.wikia.nocookie.net/disney/images/8/80/Toy_Story_-_Poster.jpg/revision/latest/scale-to-width-down/320?cb=20150108180742",
	"https://www.youtube.com/watch?v=-9ceBgWV8io") 

print toy_story.storyline
#avatar.show_trailer()
movies=[toy_story, avatar,toy_story, avatar,toy_story, avatar]
fresh_tomatoes.open_movies_page(movies)
print avatar.x