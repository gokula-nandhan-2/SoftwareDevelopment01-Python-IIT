# Question 3

def get_cost(expense_name):
    while True:
        try:
            cost = float(input(f"Enter the cost of the {expense_name}: "))
            if cost < 0:
                print("Cost cannot be negative. Please try again.")
            else:
                return cost
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def culculate_monthly_expenses(expenses):
    total_cost = sum(expenses)
    return total_cost


def main():
    expenses = []
    expense_names = ["Loan payment", "Insurance", "Gas", "Oil", "Tires", "Maintanence"]

    for expense_name in expense_names:
        cost = get_cost(expense_name)
        expenses.append(cost)

    total_expenses = culculate_monthly_expenses(expenses)
    annual_expenses = total_expenses * 12

    print(f"\nMonthly expenses: {total_expenses:.2f}")
    print(f"Annual expenses: {annual_expenses:.2f}")

if __name__ == "__main__":
    main()

    
    
    