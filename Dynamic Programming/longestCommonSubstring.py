def LCSubstring(s1, s2, m,n):
    lookup = [[0 for x in range(n+1)] for x in range(m+1)]
    """
    The main purpose of doing m+1 and n+1 is not to get any error in
    below for loop during first iteration
    """
    maxlen =0
    endIndex=m
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                lookup[i][j] = lookup[i-1][j-1]+1
                if lookup[i][j] >maxlen:
                    maxlen =  lookup[i][j]
                    endIndex = i
    print(maxlen, endIndex)
    return s1[endIndex - maxlen: maxlen]

a = "ABC"
b = "BCDABCAAD"
print(LCSubstring(a,b, len(a), len(b)))
                    
