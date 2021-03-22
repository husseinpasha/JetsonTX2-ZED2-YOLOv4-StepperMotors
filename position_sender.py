def id_list_maker():
    import time
    import os
    
    count = 0
    size0=0
    size1=1
    id_list = []

    file1 = open('/home/jetson/darknet/pos.txt', 'r+')

    num_lines = sum(1 for line in open('/home/jetson/darknet/pos.txt')) # each time that the numerb of lines are calulated the cursor goes to the end of the text file. So I open the file separately for line reading and line counting
    print('num_lines: ',num_lines)

    line_number = num_lines-1  # setting to the last line of the text file at the moment

    lines = file1.readlines() # reading the text 

    while count<300: # count indicates the number of lines that will be read from the txt file
            
        new_pos = list(lines[line_number].split()) 
        # print('New Positions', new_pos)
        X = float(new_pos[0])
        Y = float(new_pos[1])
        Z = float(new_pos[2])
        A = int(new_pos[3])

        if -10<X<10 and -10<Y<10 and -10<Z<10:    # to avoid 'inf' and 'nan' elements in id_list                
            id_list.append([X,Y,Z])

        count+=1
        line_number -= 1
        # print(count)



    chcecklist=[]
    for i in range (len(id_list)):
        for j in range(i+1, len(id_list)):
            # print('itereation i', i)
            # print('itereation j', j)
            if  (
            abs(id_list[i][0]-id_list[j][0]) < 0.30 and
            abs(id_list[i][1]-id_list[j][1]) < 0.30 and
            abs(id_list[i][2]-id_list[j][2]) < 0.30 
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