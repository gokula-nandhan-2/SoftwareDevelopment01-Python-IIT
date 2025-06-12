# Question 02

def get_distance():
    while True:
        try:
            distance = float(input("Enter the distance in kilometers: "))
            if distance < 0:
                print("Distance cannot be negative. Please try again.")
            else:
                return distance
        except ValueError:
            print("Invalid input. Please enter a numeric value for distance.")

        
def convert_to_miles(kilometers):
    miles = kilometers * 0.6214
    return miles

def main():
    while True:
        kilometers = get_distance()
        miles = convert_to_miles(kilometers)
        print(f"{kilometers} kilometers is equal to {miles} miles.")

        again = input("Do you want to convert another distance? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Thank you for using the distance converter!")
            break

if __name__ == "__main__":
    main()