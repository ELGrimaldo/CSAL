
class knapsack:
    def __init__(self, objects: dict, knapsackWeight: int) -> None:
        self.objects = objects
        self.knapsackWeight = knapsackWeight
        self.objNames = [n for n in self.objects.keys()]
        
    
    def powerset(self):

        listsub = self.objNames
        subsets = []
        for i in range(2**len(listsub)):
            subset = []
            for k in range(len(listsub)):            
                if i & 1<<k:
                    subset.append(listsub[k])
            subsets.append(subset)        
        return subsets

    def getMaxWeightAndValue(self):
        subsets = self.powerset()
        table_dict = {}
        maxValue = 0
        for sub in subsets:
            s = {"TotalWeight": 0, "TotalValue": 0}    
            for item in sub:
                s["TotalWeight"] += self.objects[item]["weight"]
                s["TotalValue"] += self.objects[item]["value"]
            if s["TotalWeight"] < self.knapsackWeight:
                table_dict[str(sub)] = s
                if s["TotalValue"] > maxValue:
                    maxValue = s["TotalValue"]
        
        for keys in table_dict.keys():
            if table_dict[keys]["TotalValue"] == maxValue:
                print("Most Valuable Subset is: ", keys)
                print( "Total weight of: ", table_dict[keys]["TotalWeight"] )
                print( "Total Value of: ", table_dict[keys]["TotalValue"])

objects = {"item 1": {"weight": 7, "value": 42},
           "item 2": {"weight": 3, "value": 12},
           "item 3": {"weight": 4, "value": 40},
           "item 4": {"weight": 5, "value": 25}}

a = knapsack(objects, 10)
a.getMaxWeightAndValue()