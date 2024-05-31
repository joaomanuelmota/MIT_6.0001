# Define the main function to execute the program
def main():
    # Input the starting annual salary from the user
    annual_salary = float(input("Enter your starting annual salary: "))
    # Define total cost of the house
    total_cost = 1000000
    # Define semi-annual raise rate
    semi_annual_raise = 0.07
    # Calculate the down payment required for the house
    down_payment = total_cost * 0.25
    # Call the bisection function to find the optimal savings rate
    portion_saved, number_interactions = bisection(
        annual_salary, total_cost, semi_annual_raise, down_payment
    )
    # Print the best savings rate and the number of interactions it took
    print(f"Best Savings Rate: {portion_saved}")
    print(f"Number of Interactions: {number_interactions}")


# Define a function to calculate the savings
def calc_savings(annual_salary, portion_saved, total_cost, semi_annual_raise):
    # Calculate the monthly salary
    monthly_salary = annual_salary / 12
    # Initialize current savings to zero
    current_savings = 0
    # Define annual return rate
    r = 0.04

    # Loop over 36 months
    for month in range(36):
        # Update current savings with monthly salary and investment return
        current_savings = (
            current_savings
            + (current_savings * r / 12)
            + (monthly_salary * portion_saved)
        )

        # Apply semi-annual raise every 6 months
        if month % 6 == 0:
            annual_salary += annual_salary * semi_annual_raise
            monthly_salary = annual_salary / 12

    return current_savings


# Define a bisection function to find the optimal savings rate
def bisection(annual_salary, total_cost, semi_annual_raise, down_payment):
    # Initialize low and high bounds for bisection search
    low = 0
    high = 10000
    # Define a small value for precision
    epsilon = 100
    # Initialize the number of interactions
    number_interactions = 0

    while True:
        avg = (high + low) // 2  # Find midpoint for bisection search
        portion_saved = (
            avg / 10000
        )  # Convert the integer to a float between 0 and 1, representing the percent saved as a decimal
        current_savings = calc_savings(
            annual_salary, portion_saved, total_cost, semi_annual_raise
        )

        if abs(current_savings - down_payment) <= epsilon:
            break

        if current_savings > down_payment + epsilon:
            high = avg
        elif current_savings < down_payment - epsilon:
            low = avg

        number_interactions += 1

    return portion_saved, number_interactions


# Check if the script is being run directly
if __name__ == "__main__":
    # Call the main function to start the program
    main()
