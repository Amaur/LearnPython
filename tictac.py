tictac = [ [None,None,None],[None,None,None],[None,None,None]]

def chekwin(tic):
    win = False
    #chech line
    if((tic[0][0]==tic[0][1]==tic[0][2]=="x") or (tic[0][0]==tic[0][1]==tic[0][2]=="o") ):
        win = True

    elif((tic[1][0]==tic[1][1]==tic[1][2]=="x") or (tic[1][0]==tic[1][1]==tic[1][2]=="o")):
        win = True

    elif( (tic[2][0]==tic[2][1]==tic[2][2]=="x") or (tic[2][0]==tic[2][1]==tic[2][2]=="o") ):
        win = True


    #check colun
    elif((tic[0][0]==tic[1][0]==tic[2][0]=="x") or (tic[0][0]==tic[1][0]==tic[2][0]=="o") ):
        win = True

    elif((tic[0][1]==tic[1][1]==tic[2][1]=="x") or (tic[0][1]==tic[1][1]==tic[2][1]=="o") ):
        win = True

    elif((tic[0][2]==tic[1][2]==tic[2][2]=="x") or (tic[0][2]==tic[1][2]==tic[2][2]=="o") ):
        win = True


    #check diago
    elif((tic[0][0]==tic[1][1]==tic[2][2]=="x") or (tic[0][0]==tic[1][1]==tic[2][2]=="o") ):
        win = True
    return win

def addVal(tic):

    while True:

        i = int(input("Enter line:"))
        j = int(input("Enter colun:"))
        if(tic[i][j]==None):
            val = input("enter x or o :")
            tic[i][j]=val
            break
        else:
            print("invalid position")
            print("try another")
    return (tic)

while True:

    tict=addVal(tictac)
    print("\n",tict[0],"\n",tict[1],"\n",tict[2])
    tr = chekwin(tict)
    print(tr)
    if(tr):
        print("you wine")
        break