try:
    x=[]
    #input takes n number from user
    n=int(input("Enter n number "))
    #for loop for append the items to list
    for i in range(0,n):
        e=int(input())
        x.append(e)
    an=[]
    #for loop iteration to performing operation with single item
    for j in x:
        for k in range(1,10):
            if j%k==0:
                an.append(k)
    one=an.count(1)
    two=an.count(2)
    three=an.count(3)
    four=an.count(4)
    five=an.count(5)
    six=an.count(6)
    seven=an.count(7)
    eight=an.count(8)
    nine=an.count(9)
    #final answer
    answ={1:one,2:two,3:three,4:four,5:five,6:six,7:seven,8:eight,9:nine}
    print(answ)
#catch block
except ValueError:
    print("Please Enter valid number")    