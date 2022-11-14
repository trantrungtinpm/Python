from collections import namedtuple

Colour = namedtuple("Colour", ["red", "blue", "green"])

background_colour = Colour(red=100, blue=160, green=243)
snake_colour = Colour(red=34, blue=0, green=134)
food_colour = Colour(red=0, blue=112, green=183)
text_colour = Colour(red=160, blue=232, green=56)
quit_colour = Colour(red=255, blue=0, green=0)
