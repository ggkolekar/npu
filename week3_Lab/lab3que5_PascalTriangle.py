def pascalTriangle(n):
     #arr = [[0 for x in range(n)]
      #        for y in range(n)]
    # iterate through every line and print integers in it
    #for line in range (0, n) :
        # every line has number of integers equal to line number
        #print("*\n", end="")
    row = []
    col = []
    num = 0
    for i in range (0, n):
        for k in range (0,i):
            if(i>1 and k>0):
                num = col[i][k-1] + col[i-1][k]
                col.append(num)
            else:
                  col.append(1)
            print(str(num),end="")
        for j in range (i,n):
            col.append(0)
        row.append(col)
        print("\n")

#print("*\n", end = "")


pascalTriangle(12)