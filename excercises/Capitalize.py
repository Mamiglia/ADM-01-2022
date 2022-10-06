

# Complete the solve function below.
def solve(s):
    W = []
    for w in s.split(" "):
        W.append(w.capitalize())
        
    return " ".join(W)

