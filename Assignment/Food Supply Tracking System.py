 # Food Supply Tracking System (SDG 2 - No Hunger)

# Function to input food details safely
def input_food():
    name = input("Enter food item: ")

    while True:
        try:
            quantity = int(input("Enter quantity available: "))
            break
        except ValueError:
            print("Invalid input! Enter a whole number.")

    return name, quantity


# Function to check food status
def check_status(quantity):
    if quantity >= 100:
        return "Sufficient"
    elif quantity >= 50:
        return "Moderate"
    else:
        return "Low (Needs urgent supply)"


# Function to display result
def display_result(name, quantity, status):
    print("\n--- FOOD STATUS ---")
    print("Food Item:", name)
    print("Quantity:", quantity)
    print("Status:", status)


# Main program
total_items = 0

while True:
    name, quantity = input_food()

    status = check_status(quantity)

    display_result(name, quantity, status)

    total_items += 1

    choice = input("\nAdd another food item? (yes/no): ").lower()
    if choice != "yes":
        break


# Final output
print("\n======================")
print("Total Food Items Recorded:", total_items)
print("======================")