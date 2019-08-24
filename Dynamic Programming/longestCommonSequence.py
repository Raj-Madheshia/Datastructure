"""
For more references and to understand logic behind the code..
https://www.techiedelight.com/longest-common-subsequence/
"""
def LCS(s1, s2, m,n):
    if m ==0 or n ==0:
        return 0

    if s1[m-1] == s2[n-1]:
        return LCS(s1, s2, m-1, n-1) + 1

    return max(LCS(s1, s2, m-1, n), LCS(s1, s2, m, n-1))

a = "ABCBDAB"
b = "BDCABA"

print(LCS(a,b, len(a), len(b)))


