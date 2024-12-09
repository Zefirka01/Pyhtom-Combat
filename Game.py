import time

earcli = 0
balance = 100
pcgshop = 100
pgeshop = 200
pcrshop = 10
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
        print("Connect to server...")
        time.sleep(1)
        print("======EARN STATUS======")
        time.sleep(0.2)
        print("click earn = " , earcli)
        time.sleep(0.4)
        print("youre balance = " , balance , "points")
        time.sleep(0.2)
        print("Cards purchased - " , cards)
    if command1 == 'shop':
        print("Connect to server...")
        time.sleep(1.5)
        print("======SHOP======")
        time.sleep(0.2)
        print("pyhton click game - " , pcgshop)
        time.sleep(0.5)
        print("pyhton game engene - " , pgeshop)
        time.sleep(0.3)
        print("Pyhton combat realise - " , pcrshop)
    if command1 == 'buy_pcg':
        print("Connecting to server...")
        cards = cards + 1
        balance = balance - pcgshop
        earcli = earcli + 10
        pcgshop = pcgshop + 10
        time.sleep(0.3)
        print("Card purchased successfully")
        print("Click earn - " , earcli)
        print("Cards purchased - " , cards)
    if command1 == 'buy_pge':
        print("Connecting to server...")
        time.sleep(0.2)
        balance = balance - pgeshop
        earcli = earcli + 20
        pgeshop = pgeshop + 1
        time.sleep(0.3)
        print("Card purchased successfully")
        print("Click earn - " , earcli)
        print("Cards purchased - " , cards)
    if command1 == 'buy_pcr':
        print("Connecting to server...")
        time.sleep(0.2)
        cards = cards + 1
        balance = balance - pcrshop
        earcli = earcli + 1
        pcrshop = pcrshop + 1
        time.sleep(0.3)
        print("Card purchased successfully")
        print("Click earn - " , earcli)
        print("Cards purchased - " , cards)
        
        
