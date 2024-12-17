def frequent_word():

    list = input("Enter the string: ")

    li = list.split()  #splits the entered string

    d = {}   #creating the empty dictionary to put the values in string

    for i in li:    #iterates the value in string and puts the string into i
        if i not in d.keys():    #the dictionary created will store the values 
            d[i]=0     #This dictionary puts the value inside 
        d[i]=d[i]+1
    print(d)  #This print statement should be below the for loop 

frequent_word()   #calls the function 