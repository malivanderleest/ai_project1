# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

from asyncio.windows_events import NULL
from searchAgents import PositionSearchProblem
import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first
    [2nd Edition: p 75, 3rd Edition: p 87]

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm
    [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    done = set()
    stack = util.Stack()
    startP = problem.getStartState()
    startNode = ((startP, []))
    stack.push(startNode)

    while not stack.isEmpty():
        currentState, action = stack.pop()
        if problem.isGoalState(currentState):
            return action
        if currentState not in done:
            done.add(currentState)
            for n in problem.getSuccessors(currentState):
                if n[0] not in done:
                    stack.push((n[0], action+[n[1]]))


def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    [2nd Edition: p 73, 3rd Edition: p 82]
    """
    queue = util.Queue()
    done = set()
    startP = problem.getStartState()
    queue.push((startP, []))
    while not queue.isEmpty():
        currentState, action = queue.pop()
        if problem.isGoalState(currentState):
            return action
        if currentState not in done:
            done.add(currentState)
            for n in problem.getSuccessors(currentState):
                if n[0] not in done:
                    queue.push((n[0], action+[n[1]]))


def uniformCostSearch(problem):
    
    ucs_queue = util.PriorityQueue()
    ucs_queue.push(problem.getStartState(), 0)
    actions = []
    current_cost = 0
    #(successor, action, stepCost)

    while not ucs_queue.isEmpty():
        current_state = ucs_queue.pop() #pops lowest priority node
        
        if start == False: #not start node
            current_cost = current_state[2]
            current_action = current_state[1]
            current_state = current_state[0]

            if problem.isGoalState(current_state):
                return actions

            successors = problem.getSuccessors(current_state)
            actions.append(current_action)

        start = False
        print("STATE ", current_state)
        
    
        for state in successors: 
            ucs_queue.push(state, (current_cost + state[2]))

    return actions

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
