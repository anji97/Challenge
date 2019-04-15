size=input("Enter a number,that you want to be the board size : ")
size=int(size)
line1=" --- "
line2=" | | "
for j in range(1,size+1):
    print(line1*size)
    print(line2*size)

        