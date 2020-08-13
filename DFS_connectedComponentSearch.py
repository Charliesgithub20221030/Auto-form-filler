from copy import deepcopy
import numpy as np

# m = [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1]]

# relationship list
s = [
    {1,2},
    {2,3},
    {3,4},
    {5,6},
    {6,7,8,9},
    {1,10},
    {'A','F','G'},
    {'E','H'},
    {'A','T'},
    {'H',10}
]





def initMatrix(n):
    """等同 np.zeros(n,n).tolist()
    盡量不用套件，以免打包出錯
    """
    m = []
    for _ in range(n):
        t = []
        for __ in range(n):
            t.append(0)
        m.append(t)
    return m

def fillWithSet(adjMatrix, connectionSet, elementToId):
    """
    adjMatrix : zero matrix
    connectionSet : set of element
    elementToId : map element to index (row and col)
    """
    indices = [elementToId[s] for s in connectionSet]
    for i in indices:
        for j in indices:
            adjMatrix[i][j]=1
    return adjMatrix

def setsToMatrix(sets):
    # 打成 unique element list
    allElements = []
    for subset in sets:
        if len(subset) > 0:
            for s in subset:
                allElements.append(s)
    allElements = sorted(list(set(allElements)) , key = lambda x: str(x))

    # build zero matrix
    num_elements = len(allElements)
    adjMatrix = initMatrix(num_elements)

    # build element id table
    elementToId = dict(zip(allElements, range(num_elements)))

    # build inverse table (the same as indexed list)
    idToElement = allElements

    for connectionSet in sets:
        adjMatrix = fillWithSet(adjMatrix, connectionSet, elementToId)
    return adjMatrix, idToElement



def getSiblings(m , index):
    siblings = []
    for i,isConnected in enumerate(m[index]):
        if i == index:
            continue
        if isConnected==1:
            siblings.append(i)
    return siblings


def getConnectedCompSets(m , idToElement):

    connectedCompSets = []
    for i in range(len(m)):

        q = [i]
        connectedCompSet = set()

        while q != []:
            vIndex = q.pop()
            connectedCompSet.add(idToElement[vIndex])
            # print('add ', vIndex)
            unvisitedSiblings = [v for v in getSiblings(m , vIndex) if idToElement[v] not in connectedCompSet]
            q += unvisitedSiblings

        if connectedCompSet not in connectedCompSets:
            connectedCompSets.append(connectedCompSet)
    return connectedCompSets


# printBlockSet(m)
adjMatrix, idToElement = setsToMatrix(s)


print(np.array(adjMatrix))

print(getConnectedCompSets(adjMatrix , idToElement))