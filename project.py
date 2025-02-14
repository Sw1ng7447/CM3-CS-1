import requests

def get_exchange_rate(from_currency, to_currency):
    # Normally, we'd fetch real exchange rates, but for now, let's use fixed rates.
    rates = {
        ('USD', 'EUR'): 0.91,
        ('EUR', 'USD'): 1.1,
        ('USD', 'KZT'): 450,
        ('KZT', 'USD'): 0.0022,
        ('EUR', 'KZT'): 490,
        ('KZT', 'EUR'): 0.0020,
    }
    return rates.get((from_currency, to_currency), None)

def convert_currency(amount, from_currency, to_currency):
    rate = get_exchange_rate(from_currency, to_currency)
    if rate:
        return round(amount * rate, 2)
    return None

def main():
    print("Welcome to the Currency Converter!")
    amount = float(input("Enter amount: "))
    from_currency = input("Enter currency you have (USD, EUR, KZT): ").upper()
    to_currency = input("Enter currency you want (USD, EUR, KZT): ").upper()
    
    result = convert_currency(amount, from_currency, to_currency)
    if result is not None:
        print(f"{amount} {from_currency} is {result} {to_currency}.")
    else:
        print("Invalid currency pair.")

if __name__ == "__main__":
    main()
