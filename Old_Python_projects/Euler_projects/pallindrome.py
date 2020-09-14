palindromes=[]
for n in range(10,100):
    for m in range(10,100):
        a=m*n
        if str(a)==str(a)[::-1]:
            palindromes.append(a)

print(max(palindromes))





