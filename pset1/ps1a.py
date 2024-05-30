def main():
    annual_salary = float(input("Enter your annual salary: "))
    portion_saved = float(
        input("Enter the percentage of your salary to save, as a decimal: ")
    )
    total_cost = float(input("Enter the cost of your dream house: "))
    months = house(annual_salary, portion_saved, total_cost)
    print(f"Number of Months: {months}")


def house(annual_salary, portion_saved, total_cost):
    monthly_salary = annual_salary / 12
    current_savings = 0
    portion_down_payment = total_cost * 0.25
    r = 0.04
    months = 0

    while current_savings < portion_down_payment:
        current_savings = (
            current_savings
            + (current_savings * r / 12)
            + (portion_saved * monthly_salary)
        )
        months += 1
    return months


if __name__ == "__main__":
    main()
