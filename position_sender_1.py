# in this file the positions are being read from th first line of the text file
def id_list_maker():
    import time
    import os
    
    count = 0
    size0=0
    size1=1
    id_list = []

    file1 = open('/home/jetson/darknet/pos.txt', 'r+')

    while count<1000: # count indicates the number of lines that will be read from the txt file
        size1 = os.path.getsize('/home/jetson/darknet/pos.txt')

        if size1>size0: #to make sure that a new line is written to the txt file
            lines = file1.readline()
            line = lines.strip()
            new_pos = list(line.split()) 
            print('New Positions', new_pos)
            X = float(new_pos[0])
            Y = float(new_pos[1])
            Z = float(new_pos[2])
            A = int(new_pos[3])
            print("Done!", count)

            if -10<X<10 and -10<Y<10 and -10<Z<10:    # to avoid 'inf' and 'nan' elements in id_list                
                size0 = size1
                id_list.append([X,Y,Z])

            count+=1

        else:
            time.sleep(0.001)


    # file1.truncate(0) # clean the text file up


    # file1.close() 

    # print ("length of id_list: ", len(id_list))
    # print ('id_list: ', id_list)

    # making a list of must-remove elements
    chcecklist=[]
    for i in range (len(id_list)):
        for j in range(i+1, len(id_list)):
            # print('itereation i', i)
            # print('itereation j', j)
            if  (
            abs(id_list[i][0]-id_list[j][0]) < 0.10 and
            abs(id_list[i][1]-id_list[j][1]) < 0.10 and
            abs(id_list[i][2]-id_list[j][2]) < 0.10 
            ): 
                if i not in chcecklist:  # avoid dulicated appending
                    chcecklist.append(i)

    # print('old', id_list)
    # print("checklist: ", chcecklist)

    # removing the must-remove elements from id_list
    cnt = 0
    for ele in chcecklist:
        del id_list[ele-cnt]
        cnt+=1  # at each iteration that an element is removed the length
                # of the id_list decreases and the index of the unwanted 
                # elements decreases by one as well. So we need a counter

    print('new id_list length', len(id_list))
    print('new id list', id_list)
    return (id_list)
    # just for test
    
def best_id_finder(): # sort the ids based on area and return the id that has largest area
    for id in id_list_maker():
        print (id)



    # X_obj = id_list[0][0]
    # Y_obj = id_list[0][1]
    # Z_obj = id_list[0][2]

    # return [X_obj, Y_obj, Z_obj]

id_list_maker()
