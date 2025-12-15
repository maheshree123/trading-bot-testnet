from binance.client import Client

# Enter your Testnet API keys here
api_key = input("Enter API Key: ")
api_secret = input("Enter API Secret: ")

client = Client(api_key, api_secret, testnet=True)

def show_menu():
    print("\n=== Binance Bot Menu ===")
    print("1 → Market Buy")
    print("2 → Market Sell")
    print("3 → Limit Buy")
    print("4 → Limit Sell")
    print("5 → Check Balance")
    print("6 → Check Open Orders")
    print("7 → Cancel Order")
    print("8 → Exit")

def market_order(symbol, side, quantity):
    order = client.futures_create_order(
        symbol=symbol,
        side=side,
        type='MARKET',
        quantity=quantity
    )
    print(order)

def limit_order(symbol, side, quantity, price):
    order = client.futures_create_order(
        symbol=symbol,
        side=side,
        type='LIMIT',
        timeInForce='GTC',
        quantity=quantity,
        price=price
    )
    print(order)

def check_balance():
    balance = client.futures_account_balance()
    print(balance)

def check_open_orders(symbol):
    orders = client.futures_get_open_orders(symbol=symbol)
    print(orders)

def cancel_order(symbol, orderId):
    result = client.futures_cancel_order(symbol=symbol, orderId=orderId)
    print(result)

# Main loop
while True:
    show_menu()
    choice = input("Choose option: ")
    
    if choice == '1':
        symbol = input("Symbol (e.g., BTCUSDT): ")
        qty = float(input("Quantity: "))
        market_order(symbol, 'BUY', qty)
    elif choice == '2':
        symbol = input("Symbol (e.g., BTCUSDT): ")
        qty = float(input("Quantity: "))
        market_order(symbol, 'SELL', qty)
    elif choice == '3':
        symbol = input("Symbol (e.g., BTCUSDT): ")
        qty = float(input("Quantity: "))
        price = float(input("Price: "))
        limit_order(symbol, 'BUY', qty, price)
    elif choice == '4':
        symbol = input("Symbol (e.g., BTCUSDT): ")
        qty = float(input("Quantity: "))
        price = float(input("Price: "))
        limit_order(symbol, 'SELL', qty, price)
    elif choice == '5':
        check_balance()
    elif choice == '6':
        symbol = input("Symbol (e.g., BTCUSDT): ")
        check_open_orders(symbol)
    elif choice == '7':
        symbol = input("Symbol (e.g., BTCUSDT): ")
        order_id = int(input("Order ID: "))
        cancel_order(symbol, order_id)
    elif choice == '8':
        print("Exiting...")
        break
    else:
        print("Invalid option. Try again.")
