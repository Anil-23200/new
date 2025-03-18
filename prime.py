n=int(input("Enter a numbet:"))
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        print(f"{n} is not prime number")
        break
else:
     print(f"{n} is prime number")    