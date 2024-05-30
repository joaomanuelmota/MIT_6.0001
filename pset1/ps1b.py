def main():
    annual_salary = float(input("Enter your starting annual salary: "))
    portion_saved = float(
        input("Enter the percentage of your salary to save, as a decimal: ")
    )
    total_cost = float(input("Enter the cost of your dream house: "))
    semi_annual_raise = float(input("Enter the semiannual raise, as a decimal: "))
    months = house(annual_salary, portion_saved, total_cost, semi_annual_raise)
    print(f"Number of Months: {months}")


def house(annual_salary, portion_saved, total_cost, semi_annual_raise):
    monthly_salary = annual_salary / 12
    current_savings = 0
    portion_down_payment = total_cost * 0.25
    r = 0.04
    months = 0

    while current_savings < portion_down_payment:
        current_savings = (
            current_savings
            + (current_savings * r / 12)
            + (monthly_salary * portion_saved)
        )
        months += 1

        # Apply semi-annual raise every 6 months
        if months % 6 == 0:
            annual_salary += annual_salary * semi_annual_raise
            monthly_salary = annual_salary / 12

    return months


if __name__ == "__main__":
    main()
