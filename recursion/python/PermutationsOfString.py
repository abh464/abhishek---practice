def swap(str, i, j):
    str = list(str)
    str[i], str[j] = str[j], str[i]
    return ''.join(str)

def permutations_of_string(start, end, str):
    if start >= end:
        print("str: ",str)
        return 
    for i in range(start,end):
        str = swap(str,start,i)
        permutations_of_string(start+1,end,str)
        str = swap(str,start,i)

str = "abc"
permutations_of_string(0,len(str),str)