arr = [2]
for num in range(2, 1000000):
   if num > 1:
       for i in arr:
           if (num % i) == 0:
               break
       else:
           arr.append(num)
           # print(num)
f = open("primes.txt","a")

f.write(str(arr))
f.close()