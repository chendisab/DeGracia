import csv

def load_currency_data(file_path):
    currencies = {}
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if len(row) == 3:
                    code, name, rate = row
                    currencies[code] = float(rate)
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return currencies

def exchange_amount(amount, currency, rates):
    if currency in rates:
        return amount * rates[currency]
    else:
        print("Error: Currency not found.")
        return None

def main():
    file_path = r'LABACT_4B\currency.csv'
    exchange_rates = load_currency_data(file_path)
    
    if not exchange_rates:
        print("No exchange rates loaded. Exiting.")
        return
    
    try:
        amount = float(input("How much dollars do you have? "))
        target_currency = input("Which currency do you want to convert to? ").upper()
        converted_value = exchange_amount(amount, target_currency, exchange_rates)
        
        if converted_value is not None:
            print(f"\nAmount in USD: {amount} USD")
            print(f"Converted to {target_currency}: {converted_value}")
    except ValueError:
        print("Error: Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()


# Set operations

Set_A = {'a', 'b', 'c', 'd', 'f', 'g'}
Set_B = {'b', 'c', 'h', 'l', 'm', 'o'}
Set_C = {'c', 'd', 'f', 'h', 'j', 'i', 'k'}

common_in_A_and_B = Set_A & Set_B
print(f"Common elements in A and B: {common_in_A_and_B}")
print(f"Count of common elements in A and B: {len(common_in_A_and_B)}")

unique_in_B = Set_B - (Set_A | Set_C)
print(f"Unique elements in B (not in A and C): {unique_in_B}")
print(f"Count of unique elements in B (not in A and C): {len(unique_in_B)}")

print(f"i. Union of A, B, and C: {Set_A | Set_B | Set_C}")
print(f"ii. Intersection of A, B, and C: {Set_A & Set_B & Set_C}")
print(f"iii. Intersection of B and C: {Set_B & Set_C}")
print(f"iv. Intersection of A and C: {Set_A & Set_C}")
print(f"v. Elements in C but not in A or B: {Set_C - (Set_A | Set_B)}")
print(f"vi. Elements in B but not in A or C: {Set_B - (Set_A | Set_C)}")
