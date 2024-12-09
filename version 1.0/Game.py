

earcli = 0
balance = 100
pcgshop = 100
pgeshop = 200
pcrshop = 10
Lbfshop = 40
pcushop = 20
cards = 0

print("Pyhton combat")
print("shop = mining cards shop open")
print("click = to add clicks")
print("earn = youre earn status")
while True:
    command1 = input("Py_Combat > ")
    if command1 == 'click':
        print("Youre got +" , + earcli , "click")
        balance = balance + earcli
    if command1 == 'earn':
        print("======EARN STATUS======")
        print("click earn = " , earcli)
        print("youre balance = " , balance , "points")
        print("Cards purchased - " , cards)
    if command1 == 'shop':
        print("======SHOP======")
        print("pyhton click game - " , pcgshop)
        print("pyhton game engene - " , pgeshop)
        print("Pyhton combat realise - " , pcrshop)
        print("Litle bug fix - " , Lbfshop)
        print("Pyhton Combat update - " , pcushop)
    if command1 == 'buy_pcg':
        cards = cards + 1
        balance = balance - pcgshop
        earcli = earcli + 10
        pcgshop = pcgshop + 10
        print("Card purchased successfully")
        print("Click earn - " , earcli)
        print("Cards purchased - " , cards)
    if command1 == 'buy_pge':
        balance = balance - pgeshop
        earcli = earcli + 20
        pgeshop = pgeshop + 1
        print("Card purchased successfully")
        print("Click earn - " , earcli)
        print("Cards purchased - " , cards)
    if command1 == 'buy_pcr':
        cards = cards + 1
        balance = balance - pcrshop
        earcli = earcli + 1
        pcrshop = pcrshop + 1
        print("Card purchased successfully")
        print("Click earn - " , earcli)
        print("Cards purchased - " , cards)
    if command1 == "buy_lbf"
        cards = cards + 1
        balance = balance - Lbfshop
        earcli = earcli + 50
        Lbfshop = Lbfshop + 5
        print("Card purchased successfully")
        print("Click earn - " , earcli)
        print("Cards purchased - " , cards)
    if command1 == 'buy_pcu'
        cards = cards + 1
        balance = balance - pcushop
        earcli = earcli + 50
        pcushop = pcushop + 2
        print("Card purchased successfully")
        print("Click earn - " , earcli)
        print("Cards purchased - " , cards)


        
        
