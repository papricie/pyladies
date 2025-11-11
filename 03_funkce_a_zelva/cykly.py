# Jak opakovat – a neopakovat se
#for i in range(100):
    #print('Nikdy nebudu odsazovat o tři mezery!')
# Tento cyklus vypíše 100krát stejný text, protože range(100) vytvoří čísla od 0 do 99 (celkem 100 čísel)






#for pozdrav in 'Ahoj', 'Hello', 'Hola', 'Hei', 'SYN':
    #print(pozdrav + '!')
# Tento cyklus projde všech pět pozdravů a každý vypíše s vykřičníkem






#for i in range(5):   # Doporučuju použít jen 5 místo 100
    #print(i)






#from turtle import forward, penup, pendown, exitonclick

#for i in range(10):
    #forward(10)
    #penup()
    #forward(5)
    #pendown()

#exitonclick()






#První čárka je dlouhá 1 jednotku, druhá 2 jednotky, třetí 3, atd. podle hodnoty i(index) v cyklu.
#Dokonce můžeš na začátek dát prázdnou čárku (0 jednotek) a mít tak délky 0, 1, 2, 3, 4, …

from turtle import forward, penup, pendown, left, exitonclick

for i in range(20):
    forward(i)
    penup()
    forward(5)
    pendown()

exitonclick()





