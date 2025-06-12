# Question 01

def get_num_of_squarefeet():
    while True:
        try:
            squarefeet = float(input("Enter the area in square feet: "))
            if squarefeet <= 0:
                print("Area must be greater than zero.")
            else:
                return squarefeet
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
        

def get_cost_per_gallon():
    while True:
        try:
            cost_per_gallon = float(input("Enter the cost of paint per gallon: "))
            if cost_per_gallon <= 0:
                print("Cost must be greater than zero.")
            else:
                return cost_per_gallon
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def calculate_gallons_needed(squarefeet):
    coverage_per_gallon = 112  # square feet per gallon
    gallons_needed = squarefeet / coverage_per_gallon
    return gallons_needed

def calculate_total_cost(gallons_needed, cost_per_gallon):
    total_cost = gallons_needed * cost_per_gallon
    return total_cost

def main():
    while True:
        squarefeet = get_num_of_squarefeet()
        cost_per_gallon = get_cost_per_gallon()
        
        gallons_needed = calculate_gallons_needed(squarefeet)
        total_cost = calculate_total_cost(gallons_needed, cost_per_gallon)
        
        print(f"Gallons needed: {gallons_needed:.2f}")
        print(f"Total cost: ${total_cost:.2f} \n")
        
        again = input("Do you want to calculate again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thank you for using the paint calculator!")
            break


if __name__ == "__main__":
    main()

    