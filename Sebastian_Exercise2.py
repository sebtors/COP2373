def calculate_spam_score(message, spam_keywords):
    """
    Description:
    This function scans the user's email message and calculates a spam score
    based on the number of spam keywords found.

    Parameters:
    message (str) – The email message entered by the user.
    spam_keywords (list of str) – A list containing spam-related words and phrases.

    Variables:
    score (int) – Stores the total spam score.
    found_keywords (list of str) – Stores the spam words found in the message.
    count (int) – Stores the number of times a keyword appears.

    Logical Steps:
    1. Convert the message to lowercase to ensure case-insensitive comparison.
    2. Loop through each keyword in the spam keyword list.
    3. Count how many times each keyword appears in the message.
    4. Add the count to the spam score.
    5. Store detected keywords in a list.
    6. Return the spam score and list of found keywords.

    Return:
    Returns score (int) and found_keywords (list of str).
    """

    # Initialize spam score to zero
    score = 0

    # Create list to store found spam keywords
    found_keywords = []

    # Convert message to lowercase for case-insensitive matching
    message = message.lower()

    # Loop through each spam keyword
    for keyword in spam_keywords:

        # Count how many times the keyword appears in the message
        count = message.count(keyword.lower())

        # If keyword appears at least once
        if count > 0:

            # Add occurrences to spam score
            score += count

            # Store the keyword in found list
            found_keywords.append(keyword)

    # Return the final spam score and found keywords
    return score, found_keywords



def rate_spam_likelihood(score):
    """
    Description:
    This function determines the likelihood that an email message is spam
    based on the spam score.

    Parameters:
    score (int) – The total spam score calculated from the message.

    Variables:
    likelihood (str) – Stores the spam likelihood rating.

    Logical Steps:
    1. Evaluate the spam score using conditional statements.
    2. Assign a likelihood rating based on the score range.
    3. Return the likelihood rating.

    Return:
    Returns likelihood (str).
    """

    # Determine spam likelihood based on score ranges
    if score == 0:
        likelihood = "Very Low (Not likely spam)"
    elif score <= 3:
        likelihood = "Low"
    elif score <= 6:
        likelihood = "Moderate"
    elif score <= 10:
        likelihood = "High"
    else:
        likelihood = "Very High (Most likely spam)"

    # Return the likelihood rating
    return likelihood



def run_spam_filter():
    """
    Description:
    This function runs the spam detection program. It collects user input,
    calls the spam score calculation function, determines the spam likelihood,
    and displays the results.

    Parameters:
    None

    Variables:
    spam_keywords (list of str) – List of 30 spam-related words and phrases.
    email_message (str) – Stores the user’s email input.
    score (int) – Spam score returned from calculate_spam_score().
    found_keywords (list of str) – Detected spam keywords.
    likelihood (str) – Spam likelihood rating.

    Logical Steps:
    1. Create a list of 30 spam keywords.
    2. Prompt the user to enter an email message.
    3. Call calculate_spam_score().
    4. Call rate_spam_likelihood().
    5. Display the spam score.
    6. Display the likelihood rating.
    7. Display detected spam keywords.

    Return:
    None
    """

    # Create list of 30 spam keywords
    spam_keywords = [
        "Free", "Winner", "Congratulations", "Click here", "Act now",
        "Limited time", "Urgent", "Claim now", "Risk free", "Guaranteed",
        "Make money", "Work from home", "No credit check", "Exclusive deal",
        "Buy now", "Special promotion", "Lowest price", "Earn cash",
        "Fast cash", "Double your income", "Get rich", "Investment opportunity",
        "Call now", "Apply now", "Hot singles", "Lose weight fast",
        "Free trial", "Winner selected", "Credit card required",
        "This is not a scam"
    ]

    # Prompt user to enter an email message
    print("Please enter the email message you would like to analyze:")
    email_message = input()

    # Calculate spam score and found keywords
    score, found_keywords = calculate_spam_score(email_message, spam_keywords)

    # Determine spam likelihood rating
    likelihood = rate_spam_likelihood(score)

    # Display results to user
    print("\nSpam Score:", score)
    print("Spam Likelihood:", likelihood)

    # Display detected spam keywords if any were found
    if found_keywords:
        print("\nSpam Keywords Detected:")
        for keyword in found_keywords:
            print("-", keyword)
    else:
        print("\nNo spam keywords were detected.")



if __name__ == "__main__":

    # Call the main spam filter function
    run_spam_filter()
