import time
import os

def rotate(input,d):
 
    # Slice string in two parts for left and right
    Lfirst = input[0 : d]
    Lsecond = input[d :]
    Rfirst = input[0 : len(input)-d]
    Rsecond = input[len(input)-d : ]
 
    # now concatenate two parts together
    print ("Left Rotation : ", (Lsecond + Lfirst) )
    print ("Right Rotation : ", (Rsecond + Rfirst))

    return Lsecond + Lfirst

# Main
frase = "Hello World!"
for i in range(0,len(frase)):
    frase = rotate(frase,1)
    time.sleep(0.2)
    os.system("cls")