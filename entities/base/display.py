import pygamepp as pgp
from vars import *

from entities.base.image import Image
from entities.base.sprite import Sprite

# les displays prennent une position, une couleur, une font et un contenu
# ce contenu peut être:
# soit une fonction qui prend l'objet Jeu en argument et dont le résultat est un objet qui soit transformable en str
# soit un objet qui soit transformable en str

# affiche un texte qui dans le jeu (position relative)
class Display(Sprite):
	def __init__(self, game, content, color, pos, font= None):
		Sprite.__init__(self, game, pos)
		self.game.groups["displays"].add(self)
		self.font = font
		if self.font is None:
			self.font = self.game.game_font
		self.content = content
		self.color = color
		if isinstance(self.content, type(lambda: None)):
			self.image = Image(self.font.render(self.content(self.game), True, self.color))
		else:
			self.image = Image(self.font.render(str(self.content), True, self.color))
		self.image.topleft = self.pos

	def update(self, pos= None, content= None):
		if pos is not None:
			self.pos = pos
		if content is not None:
			self.content = content
		if isinstance(self.content, type(lambda: None)):
			self.image.reset_surface(self.font.render(self.content(self.game), True, self.color))
		else:
			self.image = Image(self.font.render(str(self.content), True, self.color))
		self.image.topleft = self.pos

# affiche un texte sur l'écran (position fixe)
class FixDisplay(Display):
	def __init__(self, game, content, color, pos, font= None):
		Display.__init__(self, game, content, color, pos, font)
		self.game.groups["fix_displays"].add(self)

	def draw(self, surface, rpos= vec(0)):
		self.image.draw(surface)
