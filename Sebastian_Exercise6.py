import re


def validate_phone_number(phone):
    '''
    Description:
    Validates a phone number using a regular expression.

    Parameters:
    phone (str) – The phone number entered by the user.

    Variables:
    pattern (str) – The regular expression pattern used to validate the phone number.

    Logical Steps:
    1. Create a regular expression pattern for a phone number.
    2. Use re.match() to compare the user input with the pattern.
    3. Return True if the phone number matches the pattern.
    4. Return False if the phone number does not match.

    Return:
    bool – True if valid, False if invalid.
    '''

    # Pattern for phone number: 123-456-7890
    pattern = r'^\d{3}-\d{3}-\d{4}$'

    # Check if phone number matches pattern
    if re.match(pattern, phone):
        return True
    else:
        return False


def validate_ssn(ssn):
    '''
    Description:
    Validates a social security number using a regular expression.

    Parameters:
    ssn (str) – The SSN entered by the user.

    Variables:
    pattern (str) – The regular expression pattern used to validate the SSN.

    Logical Steps:
    1. Create a regular expression pattern for SSN.
    2. Use re.match() to compare the user input with the pattern.
    3. Return True if the SSN matches the pattern.
    4. Return False if the SSN does not match.

    Return:
    bool – True if valid, False if invalid.
    '''

    # Pattern for SSN: 123-45-6789
    pattern = r'^\d{3}-\d{2}-\d{4}$'

    # Check if SSN matches pattern
    if re.match(pattern, ssn):
        return True
    else:
        return False


def validate_zip(zip_code):
    '''
    Description:
    Validates a ZIP code using a regular expression.

    Parameters:
    zip_code (str) – The ZIP code entered by the user.

    Variables:
    pattern (str) – The regular expression pattern used to validate the ZIP code.

    Logical Steps:
    1. Create a regular expression pattern for ZIP codes.
    2. Use re.match() to compare the user input with the pattern.
    3. Return True if the ZIP code matches the pattern.
    4. Return False if the ZIP code does not match.

    Return:
    bool – True if valid, False if invalid.
    '''

    # Pattern for ZIP code: 5 digits
    pattern = r'^\d{5}$'

    # Check if ZIP matches pattern
    if re.match(pattern, zip_code):
        return True
    else:
        return False


def main():
    '''
    Description:
    Gets user input and checks if the phone number, SSN, and ZIP code are valid.

    Parameters:
    None

    Variables:
    phone (str) – The phone number entered by the user.
    ssn (str) – The social security number entered by the user.
    zip_code (str) – The ZIP code entered by the user.

    Logical Steps:
    1. Prompt the user to enter a phone number.
    2. Prompt the user to enter a social security number.
    3. Prompt the user to enter a ZIP code.
    4. Call the validation functions for each input.
    5. Display whether each input is valid or invalid.

    Return:
    None
    '''

    # Ask user for input
    phone = input("Enter a phone number (format: 123-456-7890): ")
    ssn = input("Enter a Social Security Number (format: 123-45-6789): ")
    zip_code = input("Enter a ZIP code (5 digits): ")

    # Validate phone number
    if validate_phone_number(phone):
        print("Phone number is valid.")
    else:
        print("Phone number is invalid.")

    # Validate SSN
    if validate_ssn(ssn):
        print("Social Security Number is valid.")
    else:
        print("Social Security Number is invalid.")

    # Validate ZIP code
    if validate_zip(zip_code):
        print("ZIP code is valid.")
    else:
        print("ZIP code is invalid.")


if __name__ == "__main__":
    main()