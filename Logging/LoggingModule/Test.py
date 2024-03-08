import inspect


def getinfo():
        print(inspect.stack()[1])
        print("getinfo method from ansh class")
