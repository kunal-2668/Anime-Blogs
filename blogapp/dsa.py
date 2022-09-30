def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

print(recur_factorial(9))

l = [21323,2323,2434,45,32,4,543,4353]

for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i] < l[j]:
            l[i],l[j] = l[j],l[i]

print(l)