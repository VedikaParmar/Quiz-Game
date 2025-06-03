print("Welcome to the Quiz")
score=0
name=str(input("Enter Your Name here : "))

fi=open('Q1.txt','r')
print(fi.read())
op=str(input("Enter your option here :"))
if(op=='b' or op=='B'):
    score+=100
    
fi=open('Q2.txt','r')
print(fi.read())
op=str(input("Enter your option here :"))
if(op=='c' or op=='C'):
    score+=100
    
fi=open('Q3.txt','r')
print(fi.read())
op=str(input("Enter your option here :"))
if(op=='c' or op=='C'):
    score+=100
    
fi=open('Q4.txt','r')
print(fi.read())
op=str(input("Enter :"))
if(op=='d' or op=='D'):
    score+=100
    
fi=open('Q5.txt','r')
print(fi.read())
op=str(input("Enter :"))
if(op=='b' or op=='B'):
    score+=100

fi=open('Q6.txt','r')
print(fi.read())
op=str(input("Enter your option here :"))
if(op=='d' or op=='D'):
    score+=100

fi=open('Q7.txt','r')
print(fi.read())
op=str(input("Enter your option here :"))
if(op=='c' or op=='C'):
    score+=100

fi=open('Q8.txt','r')
print(fi.read())
op=str(input("Enter your option here :"))
if(op=='b' or op=='B'):
    score+=100

fi=open('Q9.txt','r')
print(fi.read())
op=str(input("Enter your option here :"))
if(op=='c' or op=='C'):
    score+=100

fi=open('Q10.txt','r')
print(fi.read())
op=str(input("Enter your option here :"))
if(op=='d' or op=='D'):
    score+=100
print(score)
