import sys
from collections import OrderedDict
class MapReduce:
    def __init__(self):
        self.intermediate = OrderedDict()
        self.result = []
   

    def emitIntermediate(self, key, value):
        self.intermediate.setdefault(key, [])       
        self.intermediate[key].append(value)

    def emit(self, value):
        self.result.append(value) 

    def execute(self, data, mapper, reducer):
        for record in data:
            mapper(record)

        for key in self.intermediate:
            reducer(key, self.intermediate[key])

        self.result.sort()
        for item in self.result:
            print item

mapReducer = MapReduce()

def mapper(record):
    #Start writing the Map code here
    arr = record.strip().split(',')
    if arr[0]=='Department':
        mapReducer.emitIntermediate(arr[1], arr[2])
    if arr[0]=='Employee':
        mapReducer.emitIntermediate(arr[2], '$'+arr[1])

def reducer(key, list_of_values):
    #Start writing the Reduce code here
    arr = sorted(list_of_values)
    name=arr[0][1:]
    for e in arr[1:]:
        mapReducer.emit((key, name, e))
    
            
if __name__ == '__main__':
    inputData = []
    for line in sys.stdin:
        inputData.append(line)
    mapReducer.execute(inputData, mapper, reducer)
