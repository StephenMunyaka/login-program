name = input("Type the network: ")
print(name)
while True:
    mpesa = input("Type the word 'mpesa' below:  ")
    if mpesa.isalpha():
        mpesa = str(mpesa)
        break
    else:
        print("Type the word 'mpesa' below :")

if mpesa == "mpesa":
    print("Type 'send money' :")
    while True:
        send_money = input("Type Here:")
        if send_money.isalpha():
            send_money = str(send_money)
            break
        else:
            print("Type the 'send money'")
    withdraw_cash = input("Type withdraw_cash")
else:
    print("type mpesa")