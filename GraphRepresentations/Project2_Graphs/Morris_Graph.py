# Garrett Morris
# Project 2: Graph Representation
# CMPS 5243: Advanced Algorithm Analysis
# April 26, 2020
# Description: This project reads in sets of vertices that are connected
# to each other. It takes this data and creates a python list of all the pairs;
# this data structure is called 'vertPairs'.
# It uses this list of pairs to create a list of all of the vertices 
# in alphabetical/numeric order; this data structure is called 'vertices'. 
# Using these two data structures, an adjacency list is made and then printed.
# The program then uses 'vertPairs' and 'vertices'and # creates 
# an adjacency matrix. The adjacency matrix is then printed out.


# Psuedocode for Adjacency List creation:
# Read vertices U, V from the file
# Store these pairs in python list format (ex: [U, V])
# These singular lists are stored in a greater list of lists
# Using this list, a list of all the vertices 
# in alphabetical/numeric order is created
# for each vertice in the list of vertices, 
#     create a new list with this vertice as the 0th element
# end for loop
# for each pair of vertices (U, V)
#     for each vertice in list of vertices
#         find the list which starts with U
#         add V to this list
#         add U to V's list
# end for loop
# return the adjacency list

# Psuedocode for Adjacency Matrix creation:
# Read vertices U, V from the file
# Store these pairs in python list format (ex: [U, V])
# These singular lists are stored in a greater list of lists
# Using this list, a list of all the vertices
# in alphabetical/numeric order is created
# Create 2D array (M) with first row and first column as vertices
# all empty slots have a 0.
# For each pair of vertices (U,V)
    # find the row whose header is U
    # find the column whose header is V
    # assign Matrix[U,V] the value of 1
    # find the row whose header is V
    # find the column whose header is U
    # assign Matrix[V,U] the value of 1
# end for loop
    



import sys #used for redirecting output

# function that returns a sorted list of all vertices
def verticeList(vertPairs):
    v = []  # list that holds a list of each vertice and its adjacencies
    for pair in vertPairs:
        aCheck = False
        bCheck = False
        a = pair[0]
        b = pair[1]
        for val in v:
            if val == a:
                aCheck = True
            if val == b:
                bCheck = True
        if aCheck == False:
            v.append(a)
        if bCheck == False:
            v.append(b)
    return v

# function that returns an adjacency list given a list of vertice pairs
def makeAdjList(verticeList, vertPairs):
    adjList = [] 
    for v in verticeList: #iterate through all vertices
        adjList.append([v]) #create a list for each vertice
    for e in vertPairs: #iterate through all vertice pairs
        #boolean that checks if value has been added to adj list
        present = False 
        for v in adjList: #iterate through all verticess in the adjacency list
            #when you find the correct row for the given vertex
            if e[0] == v[0]: 
                for a in v: 
                    if e[1] == a: #check if it is in the adj list already
                        present = True
                if present == False:
                    v.append(e[1]) # add it to the adj list
                    for v in adjList:
                        if e[1] == v[0]:
                            v.append(e[0]) # add to the other value's adj list
    return adjList

# this function prints the adjacency list in a clean manner
def printAdjList(adjList):
    print("Vertices         Adjacent")
    for a in adjList:
        for v in a:
            if v == a[0]:
                output = str(v) + "                "
            else:
                output += (" " + str(v))
        print(output)
    print("\n")

# function that returns an adjacency matrix given a list of vertice pairs
def makeAdjMatrix(verticeList, vertPairs, length):
    # creates an adjacency matrix full of 0's
    adjMatrix = [[0 for x in range(length+1)] for y in range(length+1)]
    # the primary purpose of this for loop is to properly
    # set up the adjacency matrix with correct row and column tags
    for x in range(length):  # iterate through all values in each adj matrix row
        if x == 0:  # set the final value in the adj matrix
            adjMatrix[length][0] = verticeList[length-1]
            for v in range(length):  # iterate through all values in the adj list
                if v == 0:  # set first value of adj matrix to be blank
                    adjMatrix[x][v] = ' '
                    # set the final value of the first row to correct value
                    adjMatrix[x][v+length] = verticeList[length-1]
                else:  # first value in each row is set to a vertice
                    adjMatrix[0][v] = verticeList[v-1]
        else:
            adjMatrix[x][0] = verticeList[x-1]
    # the purpose of this for loop is to correctly assign each slot in
    # the adjacency matrix
    for pair in vertPairs:  # iterate through each pair of vertices
        r = pair[0]  # sets correct row value
        c = pair[1] # sets correct column value
        for row in adjMatrix:  # iterate through each row in the adj mat
            if row[0] == r:  # finds correct row for this slot
                #this for loop finds the final value for the slot
                #that we are going to evaluate and see if we need
                #to change it to a 1 from a 0
                for slot in range(len(adjMatrix[0])):
                    if c == adjMatrix[0][slot]:
                        row[slot] = 1
            if row[0] == c:  # finds correct row for this slot
                #this for loop finds the final value for the slot
                #that we are going to evaluate and see if we need
                #to change it to a 1 from a 0
                for slot in range(len(adjMatrix[0])):
                    if r == adjMatrix[0][slot]:
                        row[slot] = 1
    return adjMatrix

# this function prints the adjacency matrix in a clean manner
def printAdjMatrix(adjMatrix):
    space = " "
    for row in adjMatrix:
        for x in range(len(row)):
            diff = 3-len(str(row[x]))
            if diff == 1:
                print(str(row[x]) + space),
            elif diff == 2:
                print(str(row[x]) + space + space),
        print("\n")
    print("\n")

##################################
########## Main Program ##########
##################################

# declaration of lists that will hold vertice pairs
vertPairs = []
vertPairs2 = []
vertPairs3 = []

# read vertice pairs from input file and store in a list
with open("vertPairs.txt", "r") as f:
    for line in f: # iterate through each line in the input file
        line = line.strip()
        pair = line.split()
        if len(line) > 0: # skip empty lines
            vertPairs.append(pair) # add pair to list
# read vertice pairs from input file and store in a list
with open("vertPairs2.txt", "r") as f:
    for line in f:  # iterate through each line in the input file
        line = line.strip()
        pair = line.split()
        if len(line) > 0:  # skip empty lines
            pair[0] = int(pair[0])
            pair[1] = int(pair[1])
            vertPairs2.append(pair)  # add pair to list
# read vertice pairs from input file and store in a list
with open("vertPairs3.txt", "r") as f:
    for line in f:  # iterate through each line in the input file
        line = line.strip()
        pair = line.split()
        if len(line) > 0:  # skip empty lines
            pair[0] = int(pair[0])
            pair[1] = int(pair[1])
            vertPairs3.append(pair)  # add pair to list

# declares sorted list of all vertices in graph
vertices = sorted(verticeList(vertPairs))
vertices2 = sorted(verticeList(vertPairs2))
vertices3 = sorted(verticeList(vertPairs3))

# create adjacency lists for all data sets
adjList1 = makeAdjList(vertices, vertPairs)
adjList2 = makeAdjList(vertices2, vertPairs2)
adjList3 = makeAdjList(vertices3, vertPairs3)

# print all adjacency lists to outputfile
sys.stdout = open('MorrisProject2Graph_AdjList.txt', 'w+')
print("Garrett Morris")
print("Project 2: Graph Representation")
print("CMPS 5243: Advanced Algorithm Analysis")
print("April 26, 2020\n\n\n")
print("Data Set 1")
printAdjList(adjList1)
print("Data Set 2")
printAdjList(adjList2)
print("Data Set 3")
printAdjList(adjList3)

# create adjacency matrices for all data sets
adjMatrix1 = makeAdjMatrix(vertices, vertPairs, len(vertices))
adjMatrix2 = makeAdjMatrix(vertices2, vertPairs2, len(vertices2))
adjMatrix3 = makeAdjMatrix(vertices3, vertPairs3, len(vertices3))

# print all adjacency matrices to outputfile
sys.stdout = open('MorrisProject2Graph_AdjMatrix.txt', 'w+')
print("Garrett Morris")
print("Project 2: Graph Representation")
print("CMPS 5243: Advanced Algorithm Analysis")
print("April 26, 2020\n\n\n")
print("Data Set 1")
printAdjMatrix(adjMatrix1)
print("Data Set 2")
printAdjMatrix(adjMatrix2)
print("Data Set 3")
printAdjMatrix(adjMatrix3)

