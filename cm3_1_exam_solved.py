# -*- coding: utf-8 -*-

"""
Solved version of cm3_1_exam.py
"""

import string

# EXERCISE 1: A Simple Calculator
def simple_calculator():
    print("Select operation\n")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("\nEnter choice (1/2/3/4): ")

    try:
        num1 = float(input("\nEnter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            result = num1 + num2
            operation = "Addition"
        elif choice == '2':
            result = num1 - num2
            operation = "Subtraction"
        elif choice == '3':
            result = num1 * num2
            operation = "Multiplication"
        elif choice == '4':
            if num2 == 0:
                raise ZeroDivisionError("Error: Division by zero is not allowed.")
            result = num1 / num2
            operation = "Division"
        else:
            print("Invalid input. Please select a valid option.")
            return

        print(f"\n{operation} result: {result}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")
    except ZeroDivisionError as e:
        print(e)

# EXERCISE 2: Parsing a Speech
def parse_speech(speech_text):
    # Convert text to lowercase
    speech_text = speech_text.lower()

    # Remove punctuation
    speech_text = speech_text.translate(str.maketrans("", "", string.punctuation))

    # Split into words
    words = speech_text.split()

    # Count word occurrences
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    # Sort word frequency in descending order
    sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

    return sorted_word_count

# Test speech text
speech_text = """
Five score years ago, a great American, in whose symbolic shadow we
stand signed the Emancipation Proclamation. This momentous decree
came as a great beacon light of hope to millions of Negro slaves who
had been seared in the flames of withering injustice. It came as a
joyous daybreak to end the long night of captivity.
"""

# Running the speech parsing function
word_frequencies = parse_speech(speech_text)

# Displaying word frequencies
import pandas as pd
df = pd.DataFrame(word_frequencies, columns=["Word", "Frequency"])
print(df)
