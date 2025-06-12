# Question 4
def get_float_input(messege, error_message = "Invalid input"):
    while True:
        try:
            property_value = float(input(messege))
        except ValueError:
            print(error_message)
            continue
        else:
            break
    return property_value

def get_assessment_value(property_value):
    return property_value * 0.6

def get_property_tax(assessment_value):
    return assessment_value * 0.72 / 100


def main():
    while True:
        property_value = get_float_input("Enter the property value: ")
        assessment_value = get_assessment_value(property_value)
        property_tax = get_property_tax(assessment_value)

        print(f"\nProperty tax: {property_tax:.2f}")

        repeat = input("Do you wish to repeat? (y/n): ").strip().lower()
        if repeat == 'y':
            continue
        else:
            break

if __name__ == "__main__":
    main()