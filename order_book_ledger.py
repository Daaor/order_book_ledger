order_book = {
    'symbol': 'ETH/USDT',
    'bids': [
        {'price': 2050.0, 'amount': 1.5},
        {'price': 2045.0, 'amount': 3.0},
        {'price': 2040.0, 'amount': 5.0}
    ],
    'asks': [
        {'price': 2055.0, 'amount': 2.0},
        {'price': 2060.0, 'amount': 4.5},
        {'price': 2065.0, 'amount': 10.0}
    ]
}

market_price = {
    'BTC': 73607.96,
    'ETH': 2053.36,
    'USDT': 1
}

portfolio = {
    'BTC': 0.5,
    'ETH': 3.0,
    'USDT': 5000.0
}

quit = False

while not quit: 
    activities = '''
        ------------- Crypto Ledger -------------
            What would you like to do today?
        
        1. add - Add or update a currency.
        2. fetch - Check Balance of a Currency
        3. value - View total portfolio valuation
        4. convert - Convert your token to its equivalent amount in USD
        5. book - View ETH/USDT order book and spread
        6. limit - place a limit order
        7. quit - Exit Program
        : 
'''
    query = input(activities).lower()

    if query == 'add': # Number 1
        key = input('Enter currency symbol: ')
        amount = float(input('Enter amount to add(format = 900.0): '))
        if key in portfolio:
            portfolio[key] += amount
        else:
            portfolio[key] = amount
    elif query == 'fetch': # Number 2
        key = input('Enter currency symbol: ')
        if key in portfolio:
            print(portfolio[key])
        else:
            choice = input('Not found. Would you like to add to ledger?(yes/no): ').lower()
            if choice == 'yes':
                portfolio[key] = 0.0
                print(portfolio[key])
    elif query == 'value': # Number 3
        total_amount = 0.0
        for token, amount in portfolio.items():
            market_amount = market_price.get(token, 0.0)
            converted_amount = market_amount * amount
            total_amount += converted_amount
        print(total_amount)
    elif query == 'convert': # Number 4
        key = input('Enter currency symbol: ')
        amount = market_price.get(key, 0.0) * portfolio.get(key, 0.0)
        print(f'The amount of holdings you have in {key} is {amount} USD')
    elif query == 'book': 
        high_bid = order_book['bids'][0]['price']
        low_ask = order_book['asks'][0]['price']
        spread = low_ask - high_bid
        mid_price = (high_bid + low_ask) / 2

        print(f'Highest Bid is {high_bid}')
        print(f'Lowest Ask is {low_ask}')
        print(f'Spread is {spread}')
        print(f'Mid Price is {mid_price}')
    elif query == 'limit':
        activity = input('Would you like to buy or sell?').lower()
        price = float(input('What price would you like this to execute at?: '))
        amount = float(input(f'How many units of would you like to {activity}?'))
        new_order = {
            'price': price,
            'amount': amount
        }

        if activity == 'buy':
            if price > order_book['bids'][0]['price']:
                order_book['bids'].insert(0, new_order)
            else:
                order_book['bids'].append(new_order)
        elif activity == 'sell':
            if price < order_book['bids'][0]['price']:
                order_book['bids'].insert[0, new_order]
            else:
                order_book['bids'].append(new_order)
        print('Order Placed!')
    elif query.lower() == 'quit':
        quit = True