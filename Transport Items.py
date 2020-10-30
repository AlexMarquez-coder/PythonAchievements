import os
import time

factory = ["product"]
distribution = []
shop = []


run = True
while run == True:
    os.system("cls")
    print("Factory:", factory)
    print("distribution", distribution)
    print("Shop", shop)
    time.sleep(1)

    distribution.extend(factory)
    factory.remove("product")
    os.system("cls")
    print("Factory:", factory)
    print("distribution", distribution)
    print("Shop", shop)
    time.sleep(1)

    shop.extend(distribution)
    distribution.remove("product")
    os.system("cls")
    print("Factory:", factory)
    print("distribution", distribution)
    print("Shop", shop)
    time.sleep(1)

    antwoord = input("Nog een keer [J/N]")
    if antwoord.lower() == "j":
        factory.append("product")
        shop.clear()
        run = True
        os.system("cls")
    else:
        run = False



thislist = ["A", "B", "C"]
for x in thislist:
    print(x)

print(thislist[1])




