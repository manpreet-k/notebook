# search.py
# ---------
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


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
        Search the deepest nodes in the search tree first.

        Your search algorithm needs to return a list of actions that reaches the
        goal. Make sure to implement a graph search algorithm.

        To get started, you might want to try some of these simple commands to
        understand the search problem that is being passed in:

        print "Start:", problem.getStartState()
        print "Is the start a goal?", problem.isGoalState(problem.getStartState())
        print "Start's successors:", problem.getSuccessors(problem.getStartState())
        """
    return commonSearch(problem, util.Stack(), "dfs")

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    return commonSearch(problem, util.Queue(), "bfs")

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    return commonSearch(problem, util.PriorityQueue(), "ucs")

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    return commonSearch(problem, util.PriorityQueue(), "astar", heuristic)

def commonSearch(problem, frontier, search_type, heuristic=nullHeuristic):
    """
    Search the node based on the frontier and the search_type
    """
    visited = set()
    start_state = (problem.getStartState(), [], 0)

    if search_type is "ucs":
        frontier.push(start_state, 0)  # priority for start state is 0
    elif search_type is "astar":
        # priority for start state is calculated by heuristic()
        frontier.push(start_state, 0 + heuristic(start_state[0], problem))
    else:  # bfs, dfs
        frontier.push(start_state)

    while not frontier.isEmpty():
        pos, path, cost = frontier.pop()  # pop the correct state from the frontier

        if problem.isGoalState(pos):
            return path  # return the path calculated so far

        # if the coordinates have already been visited once, ignore them. Otherwise add it to the visited set
        if pos not in visited:
            visited.add(pos)

            # for each of the successor of the current position in the game state
            for child_state, child_direction, child_cost in problem.getSuccessors(pos):
                node_path = path + [child_direction]  # add the successor direction to the already calculated path
                node_cost = cost + child_cost  # add the successor cost to the already calculated cost
                node_state = (child_state, node_path, node_cost)

                # push the successor state onto the frontier
                if search_type is "ucs":
                    frontier.push(node_state, node_cost)
                elif search_type is "astar":
                    frontier.push(node_state, node_cost + heuristic(child_state, problem))
                else:  # bfs, dfs
                    frontier.push(node_state)

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
