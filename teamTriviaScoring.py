class Team(object):
	"""
	A team participating in trivia with a score.  Trivia teams have the following properties:

	Attributes:
		name: A string representing the team's name.
		points: A float tracking the current sum of the trivia team's points.
	"""

	def __init__(self, name, points=0.0):
		"""
		Return a team object whose name is *name* and starting points is *points*.
		"""
		self.name = name
		self.points = points

	def roundPoints(self, amount):
		"""
		Return the total points after adding *amount* roundPoints.
		"""
		self.points += amount
		return self.points

	def __repr__(self):
		"""
		Tell Python to display object class Team a certain way.
		"""
		return '{}: {}'.format(self.name,
									self.points)
def getKey(team):
	"""
	Return the score from object class Team.
	Facilitates sorting for scoreboard function.
	"""
	return team.points

def scoreboard(list_teams):
	"""
	A function for ranking the teams from worst to best after each round.
	"""
	x = sorted(list_teams, key=getKey)
	print(x)



#initialize team names
katie = Team('Team Birthday')
deeznuts = Team('RyGuy and Mikey')
allie = Team('Emily and Allie')
danna = Team('Lt. Dan and AnnaZ')
libby = Team('Libby')
mitch = Team('Mitch Connolly and Becca')
claire = Team('Claire and Brian')

teamList = [katie, deeznuts, allie, danna, libby, mitch, claire]

scoreboard(teamList)

#All objects are now initialized.  
#Looking at the teamTrivia_Scores.csv, we can add points on a per round basis.
#To add scores, 
#	e.g. katie.roundPoints(sum[0,10,0,4,8,1,1])
#To look at the updated scoreboard,
	#scoreboard(teamList)
#The best score will be listed last.

