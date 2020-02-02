def norm(v):
    num = 0
    for i in v:
        num += i**2
    return num**0.5
v = [1,2,3,4]
result = norm(v)
print(result)