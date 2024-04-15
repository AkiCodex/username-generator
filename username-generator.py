import argparse


def generate_root_list_lowercase(wordlist):
    """
    Generate a list of lowercase names from a wordlist file.

    Args:
        wordlist (str): Path to the wordlist file.

    Returns:
        list: List of lowercase names.
    """
    names = []
    with open(wordlist) as f:
        for line in f:
            names.append(line.strip().lower())
    return names


def lowercase_transformations(names):
    """
    Generate various lowercase transformations of names.

    Args:
        names (list): List of names.
    """
    for line in names:
        first_word, second_word = line.split()
        print(first_word)  # Print first word
        print(second_word)  # Print second word
        # Print initials separated by dot
        print(f"{first_word[0]}.{second_word}")
        # Print initials separated by hyphen
        print(f"{first_word[0]}-{second_word}")
        # Print initials separated by underscore
        print(f"{first_word[0]}_{second_word}")
        # Print initials separated by plus
        print(f"{first_word[0]}+{second_word}")
        # Print first initial concatenated with the second word
        print(f"{first_word[0]}{second_word}")
        # Print concatenation of both words
        print(f"{first_word}{second_word}")
        # Print concatenation of both words with reversed order
        print(f"{second_word}{first_word}")
        # Print first word followed by dot and second word
        print(f"{first_word}.{second_word}")
        # Print second word followed by dot and first word
        print(f"{second_word}.{first_word}")


def uppercase_transformations(names):
    """
    Generate various uppercase transformations of names.

    Args:
        names (list): List of names.
    """
    for line in names:
        first_word, second_word = line.split()
        # Print first word with capitalized first letter
        print(first_word.capitalize())
        # Print second word with capitalized first letter
        print(second_word.capitalize())
        # Print initials separated by dot with first letter of first word capitalized
        print(f"{first_word[0].upper()}.{second_word.capitalize()}")
        # Print initials separated by hyphen with first letter of first word capitalized
        print(f"{first_word[0].upper()}-{second_word.capitalize()}")
        # Print initials separated by underscore with first letter of first word capitalized
        print(f"{first_word[0].upper()}_{second_word.capitalize()}")
        # Print first initial concatenated with the second word with first letter of first word capitalized
        print(f"{first_word[0].upper()}{second_word.capitalize()}")
        # Print concatenation of both words with first letter of each word capitalized
        print(f"{first_word.capitalize()}{second_word.capitalize()}")
        # Print concatenation of both words with reversed order and first letter of each word capitalized
        print(f"{second_word.capitalize()}{first_word.capitalize()}")
        # Print first word in uppercase
        print(first_word.upper())
        # Print second word in uppercase
        print(second_word.upper())
        # Print concatenation of both words in uppercase
        print(f"{first_word.upper()}{second_word.upper()}")


parser = argparse.ArgumentParser(description='Python script to generate user lists for bruteforcing!')
parser.add_argument('-w', '--wordlist', type=str, metavar='wordlist', required=True, help="Specify path to the wordlist")
parser.add_argument('-u', '--uppercase', action='store_true', help='Also produce uppercase permutations. Disabled by default')

args = parser.parse_args()

names = generate_root_list_lowercase(args.wordlist)
lowercase_transformations(names)

if args.uppercase:
    uppercase_transformations(names)
