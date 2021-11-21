def esurvey_schlcafe():
    surveyarr = []
    sinarr = []
    boinarr  = []
    winarr = []
    pinarr = []

    sfin = input("Food survey. Type C to continue. ")
    if(sfin == 'C'):
        while(1==1):
            sin = int(input("Do you like Sandwitch? Type 1 for Yes and 0 for No "))
            sinarr.append(sin)
            boin = int(input("Do you like Burrito? Type 1 for Yes and 0 for No "))
            boinarr.append(boin)
            win = int(input("Do you like Bowl? Type 1 for Yes and 0 for No "))
            winarr.append(win)
            pin = int(input("Do you like Pasta? Type 1 for Yes and 0 for No "))
            pinarr.append(pin)

            uin = input("Would you like to continue? Type any character to continue and Q to quit.")
            if uin == 'Q':
                break

    surveyarr.append(sinarr)
    surveyarr.append(boinarr)
    surveyarr.append(winarr)
    surveyarr.append(pinarr)

    print("Survey result")
    # array to store sum of survey for all four options
    pl = [0,0,0,0]

    for i in range(len(surveyarr)):
        for j in range(len(surveyarr[i])):
                pl[i]+= surveyarr[i][j]


    print("number of people who like Sandwitch " + str(pl[0]))
    print("number of people who like Burrito " + str(pl[1]))
    print("number of people who like Bowl " + str(pl[2]))
    print("number of people who like Pasta " + str(pl[3]))

esurvey_schlcafe()


