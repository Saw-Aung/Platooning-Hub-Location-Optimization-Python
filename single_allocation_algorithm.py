
import localsolver
import sys

if len(sys.argv) < 2:
    print("Usage: python My_model.py inputFile [outputFile]") # time limit is not added here.
    # When the node number is 40, even time limit will be set, it cannot give the feasible answer
    #print("Usage: python facility_location.py inputFile [outputFile] [timeLimit]")
    sys.exit(1)

def read_integers(filename):
    with open(filename) as f:
        return [int(elem) for elem in f.read().split()]
    
with localsolver.LocalSolver() as ls:
    # Read instance data
    file_it = iter(read_integers(sys.argv[1]))

    # Number of locations

    n= 50

    # Number of facilites
    p= 2

    # Discounted factor
    dis_factor= 0.8


    # Distance or cost data from i to j
    D = [[next(file_it) for j in range(n)] for i in range(n)]

    # Quantity from i to j
    Q = [[next(file_it) for j in range(n)] for i in range(n)]
    
    cost = [None]*n
    for i in range(n): # i and j are nodes. k and l are hubs
        cost[i]= [None]*n
        for j in range(n):
            cost[i][j]= [None]*n
            for k in range(n):
                cost[i][j][k]=[None]*n
                for m in range(n):
                    cost[i][j][k][m]= D[i][k] + dis_factor*D[k][m]+ D[m][j]
                    
                    
    # Optimized model declaration
    mdl= ls.model

    # Binary variables
    X = [[mdl.bool() for i in range(n)]for k in range(n)]
    Z= [[[[mdl.bool() for i in range(n)]for j in range(n)]for k in range(n)]for m in range(n)]
    # Z= [None]*n
    # for i in range(n):
    #     Z[i]=[None]*n
    #     for j in range(n):
    #         Z[i][j]=[None]*n
    #         for k in range(n):
    #             Z[i][j][k]=[None]*n
    #             for m in range(n):
    #                 mdl.constraint(Z[i][j][k][m]>=0)
    
    
    # Constraints
    # Assigned to desired number of hubs
    hubs= mdl.sum(X[k][k] for k in range(n))
    mdl.constraint(hubs == p)
    
    
    for i in range(n):
        mdl.constraint(mdl.sum(X[i][k] for k in range(n))==1)
        
    for i in range(n):
        for k in range(n):
            mdl.constraint(X[i][k]<=X[k][k])
             
             
    # X and Z constraint
    for i in range(n):
        for j in range(n):
            for k in range(n):
                mdl.constraint(mdl.sum(Z[i][j][k][m] for m in range(n))==X[i][k])
                    
                    
    for i in range(n):
        for j in range(n):
            for m in range(n):
                mdl.constraint(mdl.sum(Z[i][j][k][m] for k in range(n))==X[j][m])
    
    Obj_cost = mdl.sum(cost[i][j][k][m]*Q[i][j]*Z[i][j][k][m] for i in range(n) for j in range(n) for k in range(n) for m in range(n))
    
    mdl.minimize(Obj_cost)
    mdl.close()
    
    # if len(sys.argv) >= 4: ls.param.time_limit = int(sys.argv[3])
    # else: ls.param.time_limit = 20
    
    ls.solve()  
    
    