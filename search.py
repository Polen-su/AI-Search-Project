# search.py

import util

class SearchProblem:
    def getStartState(self):
        util.raiseNotDefined()

    def isGoalState(self, state):
        util.raiseNotDefined()

    def getSuccessors(self, state):
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        util.raiseNotDefined()

def tinyMazeSearch(problem):
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    expanded = set()
    fringe = util.Stack()
    fringe.push((problem.getStartState(), [], 0))

    while not fringe.isEmpty():
        curState, curMoves, curCost = fringe.pop()
        if curState not in expanded:
            expanded.add(curState)
            if problem.isGoalState(curState):
                return curMoves
            for state, direction, cost in problem.getSuccessors(curState):
                fringe.push((state, curMoves + [direction], curCost + cost))

    return []

def breadthFirstSearch(problem):
    expanded = set()
    fringe = util.Queue()
    fringe.push((problem.getStartState(), [], 0))

    while not fringe.isEmpty():
        curState, curMoves, curCost = fringe.pop()
        if curState not in expanded:
            expanded.add(curState)
            if problem.isGoalState(curState):
                return curMoves
            for state, direction, cost in problem.getSuccessors(curState):
                fringe.push((state, curMoves + [direction], curCost + cost))

    return []

def uniformCostSearch(problem):
    expanded = set()
    fringe = util.PriorityQueue()
    fringe.push((problem.getStartState(), [], 0), 0)

    while not fringe.isEmpty():
        curState, curMoves, curCost = fringe.pop()
        if curState not in expanded:
            expanded.add(curState)
            if problem.isGoalState(curState):
                return curMoves
            for state, direction, cost in problem.getSuccessors(curState):
                fringe.push((state, curMoves + [direction], curCost + cost), curCost + cost)

    return []

def nullHeuristic(state, problem=None):
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    expanded = set()
    fringe = util.PriorityQueue()
    fringe.push((problem.getStartState(), [], 0), 0)

    while not fringe.isEmpty():
        curState, curMoves, curCost = fringe.pop()
        if curState not in expanded:
            expanded.add(curState)
            if problem.isGoalState(curState):
                return curMoves
            for state, direction, cost in problem.getSuccessors(curState):
                h = heuristic(state, problem)
                fringe.push((state, curMoves + [direction], curCost + cost), curCost + cost + h)

    return []

bfs = breadthFirstSearch
dfs = depthFirstSearch
ucs = uniformCostSearch
astar = aStarSearch
