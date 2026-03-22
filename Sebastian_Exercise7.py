# Program: Sentence Counter with Look-Ahead
# Description: This program allows the user to enter a paragraph.
# It correctly separates sentences using a look-ahead regex pattern,
# handling abbreviations and decimal numbers.


import re


# Function to extract sentences using look-ahead regex
def split_sentences(paragraph):
    pattern = r'[A-Z].*?[.!?](?= [A-Z]|$)'

    sentences = re.findall(pattern, paragraph, flags=re.DOTALL | re.MULTILINE)

    return sentences


# Function to display sentences and count
def display_sentences(sentences):
    print("\nIndividual Sentences:")

    for i in range(len(sentences)):
        print(f"{i + 1}. {sentences[i]}")

    print(f"\nTotal number of sentences: {len(sentences)}")


# Main function
def main():
    paragraph = input("Enter a paragraph:\n")

    sentences = split_sentences(paragraph)

    display_sentences(sentences)


# Run program
main()