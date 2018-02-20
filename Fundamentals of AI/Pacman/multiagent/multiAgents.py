# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        # weight for food for the evaluation function
        food_weight = 7

        # weight for ghost for the evaluation function
        ghost_weight = 8

        # calculate distance between the current position and each of the food
        food_dist = [manhattanDistance(newPos, food) for food in newFood.asList()]

        # calculate distance between the current position and the ghost
        ghost_dist = manhattanDistance(newPos, newGhostStates[0].getPosition())

        score = successorGameState.getScore()

        if ghost_dist > 0:
            score -= ghost_weight/ghost_dist  # move away from the ghost

        if len(food_dist) > 0:
            score += food_weight/min(food_dist)  # closest food

        return score

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game

          gameState.isWin():
            Returns whether or not the game state is a winning state

          gameState.isLose():
            Returns whether or not the game state is a losing state
        """
        return self.max_value(gameState, 1, gameState.getNumAgents() - 1)

    def max_value(self, state, depth, total):
        """
            minimax for max agent
        """
        if state.isWin() or state.isLose():
            return self.evaluationFunction(state)

        v = -9999999
        for action in state.getLegalActions(0):
            successor = state.generateSuccessor(0, action)
            tmp = self.min_value(successor, depth, 1, total)

            if tmp > v:
                v = tmp
                agent_action = action

        if depth > 1:
            return v

        return agent_action  # terminal max returns actions

    def min_value(self, state, depth, current, total):
        """
            minimax for min agent
        """
        if state.isWin() or state.isLose():
            return self.evaluationFunction(state)

        v = 9999999
        actions = state.getLegalActions(current)

        for action in actions:
            successor = state.generateSuccessor(current, action)

            if current != total:
                v = min(v, self.min_value(successor , depth, current + 1, total))
            else:
                if depth < self.depth:
                    v = min(v, self.max_value(successor, depth + 1, total))
                else:
                    v = min(v, self.evaluationFunction(successor))

        return v


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        return self.max_value(gameState, 1, gameState.getNumAgents() - 1, -9999999, 9999999)

    def max_value(self, state, depth, total, alpha, beta):
        """
          alpha-beta pruning for max agent
        """
        if state.isWin() or state.isLose():
            return self.evaluationFunction(state)

        v = -9999999

        for action in state.getLegalActions(0):
            successor = state.generateSuccessor(0, action)
            tmp = self.min_value(successor, depth, 1, total, alpha, beta)

            if tmp > v:
                v = tmp
                agent_action = action

            # prune
            if v > beta:
                return v
            alpha = max(alpha, v)

        if depth > 1:
            return v

        return agent_action  # terminal max returns actions

    def min_value(self, state, depth, current, total, alpha, beta):
        """
          alpha-beta pruning for min agent
        """
        if state.isWin() or state.isLose():
            return self.evaluationFunction(state)

        v = 9999999
        for action in state.getLegalActions(current):
            successor = state.generateSuccessor(current, action)

            if current != total:
                tmp = self.min_value(successor, depth, current + 1, total, alpha, beta)
            else:
                if depth < self.depth:
                    tmp = self.max_value(successor, depth + 1, total, alpha, beta)
                else:
                    tmp = self.evaluationFunction(successor)

            if tmp < v:
                v = tmp

            # prune
            if v < alpha:
                return v

            beta = min(beta, v)

        return v


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        return self.max_value(gameState, 1, gameState.getNumAgents() - 1)

    def max_value(self, state, depth, total):
        """
            expectimax max agent function
        """
        if state.isWin() or state.isLose():
            return self.evaluationFunction(state)

        v = -9999999

        for action in state.getLegalActions(0):
            successor = state.generateSuccessor(0, action)
            tmp = self.expected_value(successor, depth, 1, total)

            if tmp > v:
                v = tmp
                agent_action = action

        if depth > 1:
            return v

        return agent_action  # terminal max returns actions

    def expected_value(self, state, depth, current, total):
        """
          expectimax min agent function
        """
        if state.isWin() or state.isLose():
            return self.evaluationFunction(state)

        actions = state.getLegalActions(current)

        v = 0
        probability = 1.0 / len(actions)

        for action in actions:
            successor = state.generateSuccessor(current, action)
            if current != total:
                v += probability * self.expected_value(successor, depth, current + 1, total)
            else:
                if depth < self.depth:
                    v += probability * self.max_value(successor, depth + 1, total)
                else:
                    v += probability * self.evaluationFunction(successor)

        return v

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    newPos = currentGameState.getPacmanPosition()
    newFood = currentGameState.getFood()
    newGhostStates = currentGameState.getGhostStates()

    # weight for food for the evaluation function
    food_weight = 7

    # weight for ghost for the evaluation function
    ghost_weight = 8

    # calculate distance between the current position and each of the food
    food_dist = [manhattanDistance(newPos, x) for x in newFood.asList()]

    # calculate distance between the current position and the ghost
    v = 0
    for ghost in newGhostStates:
        ghost_dist = manhattanDistance(newPos, ghost.getPosition())
        if ghost_dist > 0:
            if ghost.scaredTimer > 0:  # if the ghost is scared, go towards it
                v += ghost_weight / ghost_dist
            else:
                v -= ghost_weight / ghost_dist  # if the ghost is not scared, move away from it

    score = currentGameState.getScore()

    if v != 0:
        score += v

    if len(food_dist):
        score += food_weight / min(food_dist)  # closest food

    return score

# Abbreviation
better = betterEvaluationFunction

