def find_max_min(S,index=0):
    if index==len(S)-1:
        return S[index],S[index]
    min = S[index]
    max = S[index]
    if min > find_max_min(S,index+1)[0] and max > find_max_min(S,index+1)[1]:
        return find_max_min(S,index+1)[0],max
    elif min < find_max_min(S,index+1)[0] and max > find_max_min(S,index+1)[1]:
        return min,max
    elif min >find_max_min(S,index+1)[0] and max < find_max_min(S,index+1)[1]:
        return find_max_min(S,index+1)[0],find_max_min(S,index+1)[1]
    else:
        return min,find_max_min(S,index+1)[1]

S=[1,-2,3,4,-771,99]
print(find_max_min(S,0))


