def mostConsecutive(l: list[int]) -> int:
    l.sort()
    cons: int = 0
    tmpCons: int = 0
    for i in range(len(l) - 1):
        if l[i] + 1 == l[i + 1]:
            tmpCons += 1
        else:
            cons = max(tmpCons + 1, cons)
            tmpCons = 0
            
    cons = max(tmpCons, cons)
    return cons


data = []
with open("C:\\Users\\olesy\\MyPythonProjects\\dz.py\\test.txt", "rt") as f:
    line = f.readline()
    data = list(map(int, line.split()))
data.sort()    
print(data)
print(mostConsecutive(data))
