""" To print:
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
6 6 6 6 6 6
7 7 7 7 7 7 7
8 8 8 8 8 8 8 8
9 9 9 9 9 9 9 9 9
10 10 10 10 10 10 10 10 10 10 """

num = int(input("Enter the number:"))
for i in range (1,num+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print() 