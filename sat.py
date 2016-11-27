import numpy as np

def randfunc():
    A = np.random.randint(0, 10, (10, 10))
    print "Input Image \n"
    print A
    print "Integral Image  \n"
    print A.cumsum(axis=0).cumsum(axis=1)
    print "If you want to change the size please open the program file in text editor and change the values on the list on line 4"

def spefunc():
    B = [[1, 2, 4, 6, 2],
              [34, 47, 52, 12, 54],
              [46, 12, 12, 4, 1],
              [9, 8, 2, 14, 76],
              [34, 12, 34, 16, 75]]
    Z = np.array(B)

    print "Input Image \n"
    print Z
    print "Integral Image  \n"
    print Z.cumsum(axis=0).cumsum(axis=1)
    print "\n"
    print "If you want to change the values please open the program file in text editor and change the values on the list on line 13"


a = int(raw_input('Enter 1 to take random or 2 to have specific: '))

if a == 1:
    randfunc()

elif a == 2:
    spefunc()

else:
    print "not a valid number please enter a valid number"
