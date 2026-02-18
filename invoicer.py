#!/usr/bin/python3



cust_first_name = input("Customer First name: ")

cust_last_name = input("Customer Last name: ")

file_ext = ".txt"

inv_name = cust_last_name + file_ext

f = open(inv_name, "a")

cust_address = input(" Address: ")

cust_city = input(" City: ")

cust_state = input(" State: ")

cust_zip = input(" Zip: ")



print(cust_last_name)

print(cust_address)

items = {"plates" : 3, "cups" : 1, "glasses" : 2}

for x in items:

    print(x, items[x])

no_plates = input("Number of Plates: ")

no_cups = input("Number of Cups: ")

no_glasses = input("Number of Glasses: ")

total_plates = int(no_plates) * int(items["plates"])

total_cups = int(no_cups) * int(items["cups"])

total_glasses = int(no_glasses) * int(items["glasses"])

total_charge = int(total_plates) + int(total_cups) + int(total_glasses)

inv_name = cust_first_name + " " + cust_last_name + "\n"

print(inv_name)

f.write(inv_name)

inv_address = cust_address + "\n"

print(cust_address)

f.write(inv_address)

print(cust_city)

inv_city = cust_city + "\n"

f.write(inv_city)

print(cust_state)

inv_state = cust_state + "\n"

f.write(inv_state)

print(cust_zip)

inv_zip = cust_zip + "\n"

f.write(inv_zip)



## line item for plates

price_plates = items["plates"]

inv_plates = f"You Bought {no_plates} number of plates at ${price_plates:.2f} = ${total_plates:.2f} dollars. \n"

f.write(inv_plates)

myplates = "You Bought {} number of plates at {} = {} dollars."

print(myplates.format(no_plates, items["plates"], total_plates))



## line item for cups

price_cups = items["cups"]

inv_cups = f"You Bought {no_cups} number of cups at ${price_cups:.2f} = ${total_cups:.2f} dollars. \n"

f.write(inv_cups)

mycups = " {} number of cups at {} = {} dollars."

print(mycups.format(no_cups, items["cups"], total_cups))



## line item for glasses

price_glasses = items["plates"]

inv_glasses = f"You Bought {no_glasses} number of glasses at ${price_glasses:.2f} = ${total_glasses:.2f} dollars. \n"

f.write(inv_glasses)

myglasses = " {} number of glasses at {} = {} dollars."

print(myglasses.format(no_glasses, items["glasses"], total_glasses))



print('==============================================================')

inv_total = f" Total Amount Due = ${total_charge:.2f} dollars. \n"

f.write("============================================================== \n")

f.write(inv_total)



mytotal = " Total Amount Due = {} dollars."

print(mytotal.format(total_charge))

f.close()