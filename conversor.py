coin_1 = 4014
coin_2 = 831
coin_3 = 20
coin_4 = 102



amount = ""
coin = ""

get_out = False
while get_out == False:
    print("--- Conversor of dollar to coins of other countries ---")
    coin = int(input("""Choose a currency of the list:
    1. COP
    2. CLP
    3. MXN
    4. ARS
    5. Exit
    """))
    amount = int(input("Insert the amount of dollars: "))

    if coin == 1: 
        cop = amount * coin_1
        print(f"You have: ${cop} pesos Colombianos")
    elif coin == 2:
        clp = amount * coin_2
        print(f"You have: ${clp} pesos Chilenos")
    elif coin == 3:
        mxn = amount * coin_3
        print(f"You have: ${mxn} pesos Mexicanos")
    elif coin == 4:
        ars = amount * coin_4
        print(f"You have: ${ars} pesos Argentinos")
    elif coin == 5:
        get_out = True
        print("Have a nice day")
    else:
        print("You must enter a valid number")
