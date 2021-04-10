import matplotlib.pyplot as p






def drawsgraph():
    print("enter number of points you have to plot:")
    no=int(input())
    ls1=[]
    ls2=[]
    i=1

    while(i<=no):
        print("enter the x"+str(i)+ " value:")
        s=int(input())
        ls1.append(s)
        print("enter the y" + str(i) + "value:")
        k = int(input())
        ls2.append(k)
        i+=1
    p.title("Simple Graph",color="red")
    p.xlabel("x-axis")
    p.ylabel("y-axis")
    p.plot(ls1,ls2)
    p.show()
def bargraph():
    print("how many values bargraph you have to draw:")
    d=int(input())
    i=1
    ls3=[]
    ls4=[]
    while(i<=d):
        print("enter name of "+str(i)+"value:")
        name=input()
        ls3.append(name)
        print("enter " + str(i) + "value:")
        val=int(input())
        ls4.append(val)
        i+=1
    t=input("enter title:")
    p.title(t)
    xl=input("enter x- label:")
    p.xlabel(xl)
    yl=input("enter y-label:")
    p.ylabel(yl)

    p.bar(ls3,ls4)
    p.show()
def piechart():
    print("enter number of data values you have to enter:")
    data=int(input())
    ls6=[]
    ls7=[]
    i=1
    while(i<=data):

        nam=input("enter " + str(i)+ " name:")
        ls6.append(nam)
        val=int(input("enter" +str(i)+ "value:"))
        ls7.append(val)
        i+=1
    m = input("enter title for pie chart:")
    p.title(m)
    p.pie(ls7,labels=ls6,radius=1,startangle=180)
    p.legend()
    p.show()



while True:
    print("which type of graph would you like to draw:")
    print("1.simple graph")
    print("2.bar graph")
    print("3.pie chart")
    a=int(input("Enter Your Choice:"))
    if(a==1):
        drawsgraph()
    elif(a==2):
        bargraph()
    elif(a==3):
        piechart()
    else:
        print("please enter valid choice")