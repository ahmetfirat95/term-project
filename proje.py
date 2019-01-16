import sys
inputFile=open(sys.argv[1],"r")

####Creating BOARD#######################
boardlist=[]

for i in inputFile.readlines():
    i=i.split()
    boardlist.append(i)

counter=0
#######################################
def find_deleting_item(list,row,column,indexlist):
    try:
        if list[int(row)][int(column)]!=list[int(row-1)][int(column)] and list[int(row)][int(column)]!=list[int(row+1)][int(column)] and list[int(row)][int(column)]!=list[int(row)][int(column-1)] and list[int(row)][int(column)]!=list[int(row)][int(column+1)]:
            return 0
        else:
            if row==0 or column==0:
                if list[row][column]==list[-1][column] or  list[row][column]==list[row][-1]:
                    pass
                else:
                     counter=0
                     for x in list:
                        for y in range(0,len(x)):
                            try:
                                if x[y]==x[y+1]:
                                    if x[y]==list[int(row)][int(column)]:
                                            index=[]
                                            index.append(counter)
                                            index.append(y)
                                            indexlist.append(index)
                                            index=[]
                                            index.append(counter)
                                            index.append(y+1)
                                            indexlist.append(index)
                            except IndexError:
                                continue
                            try:
                                if list[counter][y]==list[counter+1][y]:
                                    if list[counter][y]==list[int(row)][int(column)]:
                                        index=[]
                                        index.append(counter)
                                        index.append(y)
                                        indexlist.append(index)
                                        index=[]
                                        index.append(counter+1)
                                        index.append(y)
                                        indexlist.append(index)
                            except IndexError:
                                continue
                        counter+=1
            else:
                     counter=0
                     for x in list:
                        for y in range(0,len(x)):
                            try:
                                if x[y]==x[y+1]:
                                    if x[y]==list[int(row)][int(column)]:
                                            index=[]
                                            index.append(counter)
                                            index.append(y)
                                            indexlist.append(index)
                                            index=[]
                                            index.append(counter)
                                            index.append(y+1)
                                            indexlist.append(index)
                            except IndexError:
                                continue
                            try:
                                if list[counter][y]==list[counter+1][y]:
                                    if list[counter][y]==list[int(row)][int(column)]:
                                        index=[]
                                        index.append(counter)
                                        index.append(y)
                                        indexlist.append(index)
                                        index=[]
                                        index.append(counter+1)
                                        index.append(y)
                                        indexlist.append(index)
                            except IndexError:
                                continue
                        counter+=1
    except IndexError:
        pass
##############################################################
def delete_same_index(list,ordered_index_list):
    for x in list:
        if x not in ordered_index_list:
            ordered_index_list.append(x)
    ordered_index_list.reverse()
###################################################################
def slide(liste, row, column):
    try:
        if liste[row+1][column] == ' ':
            liste[row+1][column] = liste[row][column]
            liste[row][column] = ' '
            if liste[row+2][column] == ' ':
                slide(liste,row+1,column)
    except IndexError:
        pass
def delete_element(mainboardlist,ordered_index_list):
    for i in ordered_index_list:
        mainboardlist[i[0]][i[1]]=" "
def delete(mainboardlist):
     for i in range(len(mainboardlist[0]),-1,-1):
        counter =0
        for j in range(len(mainboardlist),-1,-1):
            try:
                if mainboardlist[j][i] == ' ':
                    counter =1
                if mainboardlist[j][i] != ' ' and counter==1:
                    slide(mainboardlist, j, i)
            except IndexError:
                continue
##################################################################
def fib(n):
    x =[0,1]
    for i in range(n):
        x=[x[1],x[0]+x[1]]
    return x[0]
#################################################################
def check_column(boardlist):
    delete_column=[]
    for x in range(0,len(boardlist[0])):
        try:
            counter=0
            for y in boardlist:
                if y[x]==" ":
                    counter+=1
            if counter==len(boardlist):
                delete_column.append(x)
        except IndexError:
            continue
    for x in delete_column:
        try:
            for y in boardlist:
                y.pop(x)
        except IndexError:
            continue
############################################################
for y in range(0,len(boardlist)):
    for x in range(0,len(boardlist[0])+1):
        try:
            print(boardlist[y][x],end=" ")
        except IndexError:
            continue
    print("")
score=0
print("")
print("Your score is:{}\n".format(score))
##############################################################
game_finish=False
while game_finish==False:
    indexlist=[]
    ordered_index_list=[]
    check_list=[]
    row_and_column=input("Please enter a row and column number:")
    row_and_column=row_and_column.split()
    row=row_and_column[0]
    column=row_and_column[1]
    row=int(row)-1
    column=int(column)-1
    try:
        if boardlist[row][column]==" ":
            get_input=True
            while get_input==True:
                print("")
                print("Please enter a correct size!\n")
                row_and_column=input("Please enter a row and column number:")
                row_and_column=row_and_column.split()
                row=row_and_column[0]
                column=row_and_column[1]
                row=int(row)-1
                column=int(column)-1
                if boardlist[row][column]!=" ":
                    get_input=False

    except IndexError:
        continue
    element=int(boardlist[row][column])
    find_deleting_item(boardlist,row,column,indexlist)
    delete_same_index(indexlist,ordered_index_list)
    delete_element(boardlist,ordered_index_list)
    delete(boardlist)
    print("")
    check_column(boardlist)
    for y in range(0,len(boardlist)):
        for x in range(0,len(boardlist[0])):
            try:
                print(boardlist[y][x],end=" ")
            except IndexError:
                continue
        print("")
    score=score+element*fib(len((ordered_index_list)))
    print(" ")
    print("Your score is:{}\n".format(score))
    for x in range(0,len(boardlist)):
        for y in range(0,len(boardlist[0])):
            try:
                if boardlist[x][y]!=" ":
                    if boardlist[x][y]==boardlist[x][y+1] or boardlist[x][y]==boardlist[x][y+-1] or boardlist[x][y]==boardlist[x-1][y] or boardlist[x][y]==boardlist[x+1][y]:
                        check_list.append("a")
            except IndexError:
                continue
    if len(check_list)==0:
        game_finish=True
        print("Game Over")
