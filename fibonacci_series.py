# fibonacci series
# 0 1 1 2 3 5 8 13 21 34
# 0+1=1, 1+1=2 , 1+2=3 ,2+3=5, 3+5=8


# for i in range(1,11):
#     print(i, end = " ")

def fibonacci_seq(n):
    a = 0 #first number
    b = 1 #second number
    if n == 1:
        print(a)
    elif n ==2:
        print(a,b)
    else:
        print(a,b, end = " ")
        for i in range(n-2):
            c = a + b # c=1,2,3
            a = b #a=1,1,2
            b = c # b = 1,2,3
            print(b, end = " ")
fibonacci_seq(10)


# Output
$ python 08fibonacci_series.py 
0 1 1 2 3 5 8 13 21 34 
