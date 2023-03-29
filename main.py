#WRITE YOUR CODE IN THIS FILE
def hasL(w):
    num = 0
    for i in range(0, len(w)):
        if w[i] == "l":
            num = num + 1
    if num > 0:
        return True
    else:
        return False
