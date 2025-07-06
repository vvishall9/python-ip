def fibo (n):
    a,b = 0,1
    fibo_seq = []
    for i in range(n):
        fibo_seq.append(a)
        a ,b = b , a+b
    return fibo_seq

a = int(input("Enter a number: "))
fibo_number= fibo(a)
print (f"Fibonacci series of {a} is: ",fibo_number)