input_amount = int(input())

if(input_amount == 0):
    print('No change')
else:
    def getCoins(input):
        num_dollars = input // 100
        dollar_remainder = input % 100
        if num_dollars == 1:
            print(f'{num_dollars} Dollar')
            getCoins(input - 1 * 100)
        elif num_dollars > 1:
            print(f'{num_dollars} Dollars')
            getCoins(input - num_dollars * 100)
        elif dollar_remainder >= 25:
            quarter = dollar_remainder // 25
            if quarter == 1:
                print(f'{quarter} Quarter')
                getCoins(input - 1 * 25)
            elif quarter > 1:
                print(f'{quarter} Quarters')
                getCoins(input - quarter * 25)
        elif dollar_remainder >= 10:
            dime = dollar_remainder // 10
            if dime == 1:
                print(f'{dime} Dime')
                getCoins(input - 1 * 10)
            elif dime > 1:
                print(f'{dime} Dimes')
                getCoins(input - dime * 10)
        elif dollar_remainder >= 5:
            nickel = dollar_remainder // 5
            if nickel == 1:
                print(f'{nickel} Nickel')
                getCoins(input - 1 * 5)
            elif nickel > 1:
                print(f'{nickel} Nickels')
                getCoins(input - nickel * 5)
        elif dollar_remainder >= 1:
                penny = dollar_remainder // 1
                if penny == 1:
                    print(f'{penny} Penny')
                    getCoins(input - 1 * 1)
                else:
                    print(f'{penny} Pennies')
                    getCoins(input-penny * 1)

    getCoins(input_amount)