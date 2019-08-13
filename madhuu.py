a = 360
b = 380
for n in range(a, b + 1):
   order = len(str(n))
   sum = 0
   temp = n
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if n == sum:
       print(n)
