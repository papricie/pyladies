#Napiš program, který postupně z jednotlivých 'X' vypíše:

#X
#X X
#X X X
#X X X X
#„Z jednotlivých 'X'“ opět znamená, že každý print vypíše maximálně jedno 'X'.


for i in range(1, 5): 
    for j in range(i):  
        print("X", end=" ") 
    print() 