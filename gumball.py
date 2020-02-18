def main():
    while(1):
        balance = 0

        userInput = input("0.05: Insert Nickel\n0.10: InsertDime\n0.25: Insert Quarter\nRed: Recieve Red Gumball\nYellow: Revieve Yellow Gumball\nReturn: Return Change\n")

        if(userInput == '0.05' or userInput == '0.10' or userInput == '0.25'):
            coin = float(userInput)
            balance = balance + coin

        if(userInput == 'Red'):
            if(balance >= 0.05):
                balance = balance - 0.05
                print("Red gumball has been dispensed")
            else:
                print("Insufficient Balance")

        if(userInput == 'Yellow'):
            if(balance >= 0.10):
                balance = balance - 0.10
                print("Yellow gumball has been dispensed")
            else:
                print("Insufficient Balance")

        if(userInput == 'Return'):
            print("Returned " + str(balance))
            break
        print("Current balance is : " + str(balance))

if __name__ == '__main__':
    main()
