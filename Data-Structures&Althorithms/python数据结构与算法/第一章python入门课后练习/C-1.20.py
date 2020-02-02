import random

def new_shuffle(S):
    temp = list()
    for i in range(len(S)):
            num = random.randint(0,len(S)-1)
            temp.append(S[num])
            S.remove(S[num])
    return temp
S=[1,2,3,4]
result = new_shuffle(S)
print(result)