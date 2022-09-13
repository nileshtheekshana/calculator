print('welcome to calculator')
print('press 1 for + ')
print('press 2 for - ')
print('press 3 for x ')
print('press 4 for / ')


while True:
    inp = int(input('enter your choice :  '))

    if inp >4 or inp<0:
        print('enter valid number')
        continue
    elif inp ==1:
        fno=float(input('enter 1st number : '))
        sno = float(input('enter 2nd number : '))
        print (f"{fno}+{sno} = {fno+sno}")

    elif inp ==2:
        fno=float(input('enter 1st number : '))
        sno = float(input('enter 2nd number : '))
        print (f"{fno}-{sno} = {fno-sno}")

    elif inp ==3:
        fno=float(input('enter 1st number : '))
        sno = float(input('enter 2nd number : '))
        print (f"{fno}X{sno} = {fno*sno}")

    elif inp ==4:
        fno=float(input('enter 1st number : '))
        sno = float(input('enter 2nd number : '))
        print (f"{fno}/{sno} = {fno/sno}")
