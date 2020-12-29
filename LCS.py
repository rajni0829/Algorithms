# Q2 Longest Common Subsequence


first = input('First String: ')
second = input('Second String: ')

n = len(first)
m = len(second)

ar = [[0] * (n+1) for _ in range(m+1)]

# FILL
for i in range(1, m+1):
    for j in range(1, n+1):
        if first[j-1] != second[i-1]:
            ar[i][j] = max(ar[i-1][j], ar[i][j-1])
        else:
            ar[i][j] = 1+ar[i-1][j-1]
# length of longest common sub sequence is at ar[m][n]

lcs = ''

i = m
j = n
while i > 0 and j > 0:
    if first[j-1] == second[i-1]:
        lcs = first[j-1] + lcs
        i -= 1
        j -= 1
    else:
        if ar[i-1][j] > ar[i][j-1] or ar[i-1][j] == ar[i][j-1]:
            i -= 1
        else:
            j -= 1

print("\n--> Length of LCS for '{}' and '{}': {} is {}".format(first,second,lcs,ar[m][n]))
print("\n")
