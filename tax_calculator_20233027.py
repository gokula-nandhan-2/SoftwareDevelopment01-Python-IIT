gross=float(input("Enter your gross income :"))
in1=12500
in2=37500
in3=100000
print("Your gross income is",gross,"Euros")
if gross > 150000:
    bal=gross-150000
    tax=(0/100*in1)+(20/100*in2)+(40/100*in3)+(45/100*bal)
    nincome=gross-tax
    #nincome means net income
    print("Your net income is",nincome,"Euros")
    
elif 50000<gross<=150000:
    bal=gross-50000
    tax=(0/100*in1)+(20/100*in2)+(40/100*bal)
    nincome=gross-tax
    print("Your net income is",nincome,"Euros")
    
elif 12500<gross<=50000:
    bal=gross-12500
    tax=(0/100*in1)+(20/100*bal)
    nincome=gross-tax
    print("Your net income is",nincome,"Euros")
    
else:
    gross<=12500 
    tax=0
    nincome=gross-tax
    
    print("Your net income is",nincome,"Euros")



    
    
    
