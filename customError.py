a=int(input("Enter no. between 5 and 9: "))
if(a<5 or a>9):
    raise ValueError('No. should be Between 5 and 9')