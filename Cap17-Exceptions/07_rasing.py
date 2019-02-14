
def functionName(level):
    if level < 1:
        raise Exception(level)
    return level

try:
    l = functionName()
    print("level=", l)
except Exception as e:
    print("Error in level argument:", e.args[0])

