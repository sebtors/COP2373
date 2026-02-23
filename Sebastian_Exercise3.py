from functools import reduce


def get_monthly_expenses():
    '''
    Description:
        This function collects monthly expenses from the user.
        The user enters the expense type and the expense amount.
        The function stores each expense as a tuple inside a list.

    Parameters:
        None

    Variables:
        expenses (list) – stores tuples containing expense name (str) and amount (float)
        expense_type (str) – the name of the expense entered by the user
        amount (float) – the numeric value of the expense

    Logical Steps:
        1. Create an empty list to store expenses.
        2. Prompt the user to enter an expense type.
        3. If the user enters "done", stop the loop.
        4. Prompt the user to enter the expense amount.
        5. Convert the amount to float.
        6. Store the expense as a tuple in the list.
        7. Repeat until the user types "done".
        8. Return the list of expenses.

    Return:
        expenses (list of tuples)
    '''

    # Create an empty list to store expenses
    expenses = []

    # Display instructions to the user
    print("Please enter your monthly expenses.")
    print("Type 'done' when you are finished.\n")

    # Continue asking for expenses until the user types 'done'
    while True:

        # Ask the user for the expense type
        expense_type = input("Enter the expense type: ")

        # Stop the loop if the user types 'done'
        if expense_type.lower() == "done":
            break

        try:
            # Ask the user for the expense amount
            amount = float(input("Enter the amount for this expense: $"))

            # Store the expense as a tuple
            expenses.append((expense_type, amount))

        except ValueError:
            # Display an error message if the amount is not numeric
            print("Invalid input. Please enter a numeric value.\n")

    return expenses



def calculate_total(expenses):
    '''
    Description:
        This function calculates the total of all expense amounts
        using the reduce method.

    Parameters:
        expenses (list) – list of tuples containing expense name (str) and amount (float)

    Variables:
        total (float) – the sum of all expense amounts

    Logical Steps:
        1. Use reduce() to add all expense amounts together.
        2. Start the accumulation at 0.
        3. Return the total amount.

    Return:
        total (float)
    '''

    # Use reduce to calculate the total expense amount
    total = reduce(lambda x, y: x + y[1], expenses, 0)

    return total



def calculate_highest(expenses):
    '''
    Description:
        This function determines the highest expense
        using the reduce method.

    Parameters:
        expenses (list) – list of tuples containing expense name (str) and amount (float)

    Variables:
        highest (tuple) – the tuple containing the highest expense

    Logical Steps:
        1. Use reduce() to compare expense amounts.
        2. Keep the tuple with the larger amount.
        3. Return the highest expense tuple.

    Return:
        highest (tuple)
    '''

    # Use reduce to find the expense with the highest amount
    highest = reduce(lambda a, b: a if a[1] > b[1] else b, expenses)

    return highest



def calculate_lowest(expenses):
    '''
    Description:
        This function determines the lowest expense
        using the reduce method.

    Parameters:
        expenses (list) – list of tuples containing expense name (str) and amount (float)

    Variables:
        lowest (tuple) – the tuple containing the lowest expense

    Logical Steps:
        1. Use reduce() to compare expense amounts.
        2. Keep the tuple with the smaller amount.
        3. Return the lowest expense tuple.

    Return:
        lowest (tuple)
    '''

    # Use reduce to find the expense with the lowest amount
    lowest = reduce(lambda a, b: a if a[1] < b[1] else b, expenses)

    return lowest



def display_summary(expenses):
    '''
    Description:
        This function displays the total, highest, and lowest expenses.

    Parameters:
        expenses (list) – list of tuples containing expense name (str) and amount (float)

    Variables:
        total (float) – total expense amount
        highest (tuple) – highest expense
        lowest (tuple) – lowest expense

    Logical Steps:
        1. Check if the list is empty.
        2. Call calculation functions.
        3. Display formatted results.

    Return:
        None
    '''

    # Check if no expenses were entered
    if len(expenses) == 0:
        print("No expenses were entered.")
        return

    # Calculate total, highest, and lowest expenses
    total = calculate_total(expenses)
    highest = calculate_highest(expenses)
    lowest = calculate_lowest(expenses)

    # Display the formatted summary
    print("\nMonthly Expense Summary")
    print("------------------------")
    print(f"Total Expenses: ${total:.2f}")
    print(f"Highest Expense: {highest[0]} - ${highest[1]:.2f}")
    print(f"Lowest Expense: {lowest[0]} - ${lowest[1]:.2f}")



def main():
    '''
    Description:
        This is the main control function of the program.
        It calls the functions to gather expenses and display results.

    Parameters:
        None

    Variables:
        expenses (list) – list of expense tuples

    Logical Steps:
        1. Call get_monthly_expenses().
        2. Call display_summary().

    Return:
        None
    '''

    # Get the user's expenses
    expenses = get_monthly_expenses()

    # Display the results
    display_summary(expenses)



if __name__ == "__main__":

    # Call the main function to start the program
    main()