temparray = []
file = open("possible board.txt", 'w')
for one in range(1,7):
    for two in range(1,7):
        for three in range(1,7):
            for four in range(1,7):
                for five in range(1,7):
                    for six in range(1,7):
                        temparray.append(one)
                        temparray.append(two)
                        temparray.append(three)
                        temparray.append(four)
                        temparray.append(five)
                        temparray.append(six)
                        redo=False
                        for check in range(1,7):
                            temparray[check-1] = int(temparray[check-1])
                            if temparray.count(check)>1 and redo==False:
                                redo = True
                        if redo==False:
                            for i in range(6):
                                file.write(str(temparray[i]))
                            file.write("\n")
                        temparray = []
