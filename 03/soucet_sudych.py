total = 0
# vypocitej soucet sudych cisel od 1 do 10
for number in range (1,11): #puvodne zadana 10, ale musi byt 11)
    if number % 2 == 0:
        total += number #misto = pouzito +=
print ("soucet sudych cisel:", total)
print ("ocekavame:", 30)
