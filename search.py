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
    Search the deepest sns in the search tree first.

    # Your search algorithm needs to return a list of actions that reaches the
    # goal. Make sure to implement a graph search algorithm.

    # To get started, you might want to try some of these simple commands to
    # understand the search problem that is being passed in:

    # print "Start:", problem.getStartState()
    # print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    # print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"

    #Frontier= F
    #current= It stores the path
    #v= It have the value of set of visited nodes
    #s= sucessor
    #cs= childnode
    #nw= newdirection
    #sn=startnode
    #In dfs, there is stack is used to store where set and array is used for storing visited nodes and path. Depending upon that it check
    # all the the condition first and then depends upon condition it returns or add the new path till it reaches the goal stage.


    F = util.Stack()
    current = [] #here, store the search route from the start node to the destination.
    v =set() #a collection of visited nodes
    sn =problem.getStartState()
    F.push((sn,current)) #Incorporate the route and the node into the stack.

    flag= True
    while flag:
        if F.isEmpty():
            return []
        #When I remove a stack item, I take the node and add it to the visited set.
        sn,current=F.pop()
        v.add(sn)
        if problem.isGoalState(sn): # Return the search path if the goal has been reached.
            return current
        s=problem.getSuccessors(sn) #take the successors of the current node/state
        for i in s:  # i[0]:next_state  i[1]:action  i[2]:cost
            cs =i[0]
            if cs not in v: #See whether the successor or child hasn't been visited
                nw=list(current) #copy the previous path list into the new one.
                path = i[1]
                is_visted = i[0]
                nw.append(path)
                F.push((is_visted, nw)) # Insert the path and node onto the stack.

    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

# Abbreviations
dfs = depthFirstSearch()
