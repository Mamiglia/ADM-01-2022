cube = lambda x: x**3# complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci number
    res = [0,1]
    for _ in range(n-2):
        res.append(res[-1] + res[-2])
    return res[:n]
        

