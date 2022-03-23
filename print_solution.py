#!/usr/bin/env python3
import gurobipy as gp
from gurobipy import GRB


def printSolution(model, x, n):
    if model.status == GRB.OPTIMAL:
        print('\n' + ('-' * 80) + '\nCost: %g' % model.ObjVal)
        
        # bfs to print the route(s)
        print("Route(s):")
        queue = []
        visited = []
        for s in range(n): 
            if s not in visited:
                visited.append(s)
                queue.append(s)
                sep = "\t"
                while queue:
                    v = queue.pop(0)
                    print(sep + str(v+1), end='')
                    sep = " -> "
                    for u in range(n):
                        if u not in visited and x[v, u].X > 0.0001:
                            visited.append(u)
                            queue.append(u)
                        elif x[v, u].X > 0.0001:
                            print(sep + str(u+1), end='')
                print()
