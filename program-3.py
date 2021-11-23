try:
    #input takes from user
    x=int(input("Enter the number "))
    if(x%2!=0):
        x*=2
    else:
        #remove the one item from list
        x=(x*2)-2
    #for loop for iteraton
    for i in range(x):
        i+=1
        if(i%2==0):
            #skip the even numbers
            continue
        else:
            #printing odd numbers
            print(i,end=" ")
#catch block
except ValueError:
    print("Please Enter valid number")    