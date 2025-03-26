def scanFile(path: str) -> dict[int, list[int]]:
    studs = dict() # dictionary: key - studentId, value - set of done tasks
    with open(path, "rt") as f:
        line = f.readline()
        line = f.readline()
        while line:
            studentId, task = map(int, line.split())
            if studentId in studs.keys():
                if not (task in studs[studentId]):
                    studs[studentId].append(task)
            else:
                studs[studentId] = list()
                studs[studentId].append(task)

            line = f.readline()

    return studs


def solve(studs: dict[list[int]]) -> tuple[int, int]:
    studentId: int = list(studs.keys())[0]
    tasksAmt: int = mostConsecutive(studs[studentId])
    for id in studs.keys():
        tasks = studs[id]
        tmpTasks = mostConsecutive(tasks)
        if tmpTasks > tasksAmt:
            tmpTasks = tasksAmt
            studentId = id
        elif tmpTasks == tasksAmt:
            if id < studentId:
                studentId = id
    return studentId, tasksAmt


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
    cons = max(tmpCons + 1, cons)
    return cons


# path = "C:\\Users\\olesy\\MyPythonProjects\\dz.py\\"
path = "C:\\Users\\olesy\\Desktop\\Новая папка\\"
path += "3.txt"

studs: dict[int, list] = scanFile(path)

studentId, tasksAmt = solve(studs)

print(studentId, tasksAmt)
