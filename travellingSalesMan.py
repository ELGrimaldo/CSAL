class WeightedGraph:
    def __init__(self, nodes: list) -> None:
        self.nodes = nodes
        self.costMatrix = [ [0]*len(nodes) for i in range(len(nodes))]
        

    def addCost(self, node_A: int, node_B: int, cost: int) -> None|str:
        for i in self.costMatrix:
            if (node_A in self.nodes) and (node_B in self.nodes):
                self.costMatrix[self.nodes.index(node_A)][self.nodes.index(node_B)] = cost
                self.costMatrix[self.nodes.index(node_B)][self.nodes.index(node_A)] = cost
                
            else:   
                return "Input node not in List of nodes"


    # def getAdjacencyList(self) -> dict:
    #     adjacencyList = {}
    #     for node_X in range(0, len(self.nodes)):
    #         for node_Y in range(0, len(self.nodes)):
    #             if self.costMatrix[node_X][node_Y] != 0:
 #                 if self.nodes[node_X] in adjacencyList:
    #                     adjacencyList[self.nodes[node_X]].append(self.nodes[node_Y])
    #                 else:
    #                     adjacencyList[self.nodes[node_X]] = [self.nodes[node_Y]]

         # return adjacencyList

    def paths(self, nodes): # Permutation
        if len(nodes) == 1:
            return [nodes]
    
        perms = self.paths(nodes[1:])
        char = nodes[0]
        result = []
    
        for perm in perms:
            for i in range(len(perm) + 1):
                result.append(perm[:i] + char + perm[i:])
    
        return result
    
    
    def getMinPath(self, startNode):
        nodes = self.nodes
        nodes.pop(nodes.index(startNode))
        nodes = ''.join(str(node) for node in nodes)
        
        paths = self.paths(nodes)
        newPath = []
        for path in paths:  
            newPath.append(f'{startNode}'+path+f'{startNode}')
                

        paths_Weights = {}
        
        for path in newPath:
            paths_Weights[path] = ["", 0]
            
            for i in range(0, len(path)-1):
                
                current = int(path[i])
                next = int(path[i+1])
                if (self.costMatrix[current-1][next-1]) != 0:
                    paths_Weights[path][0] += "{} + ".format((self.costMatrix[current-1][next-1]))
                    paths_Weights[path][1] += (self.costMatrix[current-1][next-1])
                
        weights = []
        for key, values in paths_Weights.items():
            weights.append(paths_Weights[key][1])


        minimun = min(weights)
        for key, values in paths_Weights.items():
            if paths_Weights[key][1] == minimun:
                # print("Minimum weight cycle: \n", paths_Weights[key][0][:-2], "=", paths_Weights[key][1])
                return paths_Weights[key][1]
                
    

a = WeightedGraph([1,2,3,4])
a.addCost(1, 2, 10)
a.addCost(1, 4, 20)
a.addCost(1, 3, 15)
a.addCost(2, 4, 25)
a.addCost(2, 3, 35)
a.addCost(3, 4, 30)
# print(a.getMinPath(1))

graph = WeightedGraph([1,2,3,4,5])
graph.addCost(1, 5, 75)
graph.addCost(1, 4, 100)
graph.addCost(1, 3, 300)
graph.addCost(1, 2, 100)
graph.addCost(2, 5, 125)
graph.addCost(2, 4, 75)
graph.addCost(2, 3, 50)
graph.addCost(3, 5, 125)
graph.addCost(3, 4, 100)
graph.addCost(4, 5, 50)
result = graph.getMinPath(1)

# print("Minimum weight cycle: \n", paths_Weights[key][0][:-2], "=", paths_Weights[key][1])