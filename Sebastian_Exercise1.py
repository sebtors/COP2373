"""
Program: Cinema Ticket Pre-Sales
Description: This program allows users to pre-purchase a limited number of cinema tickets.
Each buyer can purchase up to 4 tickets, and only 20 tickets total can be sold.
The program continues until all tickets are sold and then displays the total number of buyers.
"""


def sell_tickets():
    """
    Description:
        Manages the ticket-selling process by prompting users for how many tickets
        they want to buy and tracking remaining tickets.

    Parameters:
        None

    Variables:
        total_tickets (int) - total number of tickets available
        remaining_tickets (int) - tickets left to sell
        buyers (int) - accumulator that counts total buyers
        tickets_requested (int) - number of tickets requested by the user

    Logical Steps:
        1. Initialize total tickets and buyers.
        2. Loop while tickets remain.
        3. Prompt the user for ticket quantity.
        4. Validate ticket request using if statements.
        5. Subtract tickets from remaining total.
        6. Increment buyers count.
        7. Display remaining tickets after each purchase.

    Return:
        buyers (int) - total number of buyers
    """

    # Initialize total ticket count
    total_tickets = 10

    # Set remaining tickets equal to total tickets
    remaining_tickets = total_tickets

    # Accumulator for counting buyers
    total_buyers_count = 0

    # Loop until all tickets are sold
    while remaining_tickets > 0:

        # Prompt user for number of tickets
        tickets_requested = int(input("How many tickets would you like to buy today (1–4)? "))

        # Validate ticket request
        if tickets_requested < 1 or tickets_requested > 4:
            print("Invalid amount. You may only purchase between 1 and 4 tickets.")

        elif tickets_requested > remaining_tickets:
            print("Not enough tickets remaining.")

        else:
            # Subtract requested tickets from remaining tickets
            remaining_tickets -= tickets_requested

            # Increment buyer count
            total_buyers_count += 1

            # Display remaining tickets
            print(f"Tickets remaining: {remaining_tickets}")

    # Return total buyers after tickets are sold
    return total_buyers_count


def display_results(total_buyers):
    """
    Description:
        Displays the total number of buyers after all tickets have been sold.

    Parameters:
        total_buyers (int) - total number of buyers

    Variables:
        None

    Logical Steps:
        1. Display a message indicating tickets are sold out.
        2. Display the total number of buyers.

    Return:
        None
    """

    # Display final results
    print("\nAll tickets have been sold.")
    print(f"Total number of buyers: {total_buyers}")


if __name__ == "__main__":

    # Call function to sell tickets and get total buyers
    total_buyers = sell_tickets()

    # Call function to display final results
    display_results(total_buyers)
