import numpy as np
import matplotlib.pyplot as plt


class Team(object):
	"""
	A team participating in trivia with a score.  Trivia teams have the following properties:

	Attributes:
		name: A string representing the team's name.
		roundNumber: What round are we on?
		pointsThisRound: A float representing the score from the present round.
		pointsTotal: A float representing the total score.
	"""

	def __init__(self, name, roundNumber = 0, pointsThisRound=0.0,pointsTotal = 0.0):
		"""
		Return a team object whose name is *name* and starting points is *points*.
		"""
		self.name = name
		self.roundNumber = roundNumber
		self.pointsThisRound = pointsThisRound
		self.pointsTotal = pointsTotal

	def roundPoints(self, amount):
		"""
		Return the total points after adding *amount* roundPoints.
		"""
		self.pointsThisRound = amount
		self.pointsTotal += amount
		return self.pointsTotal

	def __repr__(self):
		"""
		Tell Python to display object class Team a certain way.
		"""
		return '{}: {}, {}, {}'.format(self.name,
									self.roundNumber,
									self.pointsThisRound,
									self.pointsTotal)
def getKey(team):
	"""
	Return the score from object class Team.
	Facilitates sorting for scoreboard function.
	"""
	return team.pointsTotal

def scoreRound(list_teams, roundScore):
	"""
	list_teams: a list of teams playing trivia.
	roundScore: a list of scores for the teams playing trivia.  Presently, order matters.
	roundNumber: increment the round by one.
	Added a plot function to show the present round score (red) and total points (blue).
	Combined scoreboard function with scoreRound to reduce inputs.
	"""
	plt.close() #close the current figure
	for t, s in zip(list_teams, roundScore):
		t.roundPoints(s)
		t.roundNumber += 1
	plt.barh(*zip(*[(str(team.name), float(team.pointsTotal)) for team in list_teams]), color='blue', label='Total')
	plt.barh(*zip(*[(str(team.name), float(team.pointsThisRound)) for team in list_teams]), color='red', label='This Round')
	plt.legend(loc="lower right")

	x = sorted(list_teams, key=getKey) #originally from scoreboard function
	print(*x, sep="\n")

def undoScore(list_teams, roundScore):
	"""
	Undo last scoring in event of mistake. Inverse of score_a_round
	list_teams: a list of teams playing trivia.
	roundScore: a list of scores for the teams playing trivia.  Presently, order matters.
	roundNumber: increment the round by one.
	"""
	for t, s in zip(list_teams, roundScore):
		t.roundPoints(-s)
		t.roundNumber -= 1

#initialize team names
katie = Team('Team Birthday')
deeznuts = Team('RyGuy and Mikey')
allie = Team('Emily and Allie')
danna = Team('Lt. Dan and AnnaZ')
libby = Team('Libby')
mitch = Team('Mitch Connolly and Becca')
claire = Team('Claire and Brian')

teamList = [allie, danna, libby, deeznuts, katie, claire, mitch]

#actual scores
round1 =  [(0+10+0+4+0+1+1), (0+10+8+0+4+1+1), (8+10+0+0+0+1+1), (0+10+0+0+0+1+1), (0+10+0+4+8+1+1), (0+0+0+0+0+1+1),(8+10+0+0+4+1+1)]
round2 = [(0+10+6+8+0), (10+0+1+8+4),(2+0+8+6+1),(4+0+0+10+0),(6+8+10+4+1),(0+10+0+8+6),(1+10+8+6+4)]
round3 = [(4+6), (4+10+8+6), (6+8+10), (10+8), (10+8), (10+6), (2+10+8)]
round4 = [(10+4), 5, (10+8+3), (10+2+1+3), (5+4+2), (8+10+1), (3+5+4)]
round5 = [(10+6+5+3+1+4+9+8),(8+9+10+4+3+7+2+5),(3+4+6+8+1+10+9),(10+9+1+3+7+6+4+8+2),(4+2+10+3+7+6+5),(10+5+6+9+8+3),(4+1+7+3+5+10+2)]
round6 = [(13.5+7+6+15+2.5+2+12+0),(15+7+8+5+13.5+2+6+1.5),(4+9+3+3.5+15+2.5+2),(10+3+9+1.5+2+2.5+3.5),(15+6+7+8+13.5+1+4+5+1.5),(9+3.5+8+2.5+15+2+1+6+.5),(15+8+7+2.5+13.5+2+1.5+3+1)]
round7 =[30, -20, -50, 141.5, -90, -20, -80] #final jeopardy, negative scores indicate loss of points associated with wager.