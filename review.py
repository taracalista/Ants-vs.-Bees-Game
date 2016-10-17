class Monster:
	vampire = {2: 'scary'}
	def werewolf(self):
		return self.vampire[2]

class Blob(Monster):
	vampire = {2: 'night'}
	def __init__(self , ghoul):
		vampire = {2: 'frankenstein'}
		self.witch = ghoul.vampire
		self.witch[3] = self

spooky = Blob(Monster)
spooky.werewolf = lambda self: Monster.vampire[2]

def get_info(login, info_dict)