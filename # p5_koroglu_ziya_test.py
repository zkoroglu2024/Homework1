# p5_koroglu_ziya.py
# Problem 5 - Interactive Caesar Cipher


# ---------- part a) ----------

def caesar_cipher(text, shift):
    """Encrypt text by shifting every letter forward by shift positions.
    Spaces, digits and punctuation are left alone, and the case of each
    letter is preserved."""

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    result = ""

    for ch in text:
        found = False

        # go through the alphabet and look for the character
        for i in range(26):

            if ch == lower[i]:
                result = result + lower[(i + shift) % 26]
                found = True
                break

            if ch == upper[i]:
                result = result + upper[(i + shift) % 26]
                found = True
                break

        # the character was not a letter, so copy it unchanged
        if not found:
            result = result + ch

    return result


# ---------- part b) ----------

def caesar_decipher(cyphertext, shift):
    """Decrypt a Caesar-encrypted string by shifting the letters back."""

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    result = ""

    for ch in cyphertext:
        found = False

        for i in range(26):

            if ch == lower[i]:
                result = result + lower[(i - shift) % 26]
                found = True
                break

            if ch == upper[i]:
                result = result + upper[(i - shift) % 26]
                found = True
                break

        if not found:
            result = result + ch

    return result


# ---------- part c) ----------

def letter_frequency(text):
    """Count how many times each letter of the alphabet appears in text.
    Upper and lower case count as the same letter, and anything that is not
    a letter is ignored."""

    lower = "abcdefghijklmnopqrstuvwxyz"

    # start every letter at zero
    counts = {}
    for i in range(26):
        counts[lower[i]] = 0

    for ch in text:
        ch = ch.lower()
        for i in range(26):
            if ch == lower[i]:
                counts[lower[i]] = counts[lower[i]] + 1
                break

    return counts


# ---------- part d) ----------

def show_frequency(text):
    """Print the letter frequency table for text, with a little bar for each
    letter so it is easy to read."""

    counts = letter_frequency(text)
    lower = "abcdefghijklmnopqrstuvwxyz"

    print()
    print("Letter frequencies:")

    total = 0
    for i in range(26):
        total = total + counts[lower[i]]

    if total == 0:
        print("  (there are no letters in this text)")
        return

    for i in range(26):
        letter = lower[i]
        if counts[letter] > 0:
            print("  {} : {:3}  {}".format(letter, counts[letter], "*" * counts[letter]))

    print("  total letters:", total)


def ask_for_shift():
    """Keep asking until the user types a whole number."""

    while True:
        answer = input("Enter the shift value (a whole number): ")
        if answer.lstrip("-").isdigit():
            return int(answer)
        print("That is not a whole number, please try again.")


def main():
    print("Welcome to the Caesar cipher program.")

    while True:
        print()
        print("=" * 40)
        print("1 - Encrypt a message")
        print("2 - Decrypt a message")
        print("3 - Show the letter frequencies of a message")
        print("4 - Encrypt, show frequencies, and decrypt back")
        print("5 - Quit")
        print("=" * 40)

        choice = input("What would you like to do? ")

        if choice == "5":
            print("Bye!")
            break

        elif choice == "1":
            text = input("Enter the message to encrypt: ")
            shift = ask_for_shift()
            print("Encrypted:", caesar_cipher(text, shift))

        elif choice == "2":
            text = input("Enter the message to decrypt: ")
            shift = ask_for_shift()
            print("Decrypted:", caesar_decipher(text, shift))

        elif choice == "3":
            text = input("Enter the message: ")
            show_frequency(text)

        elif choice == "4":
            text = input("Enter the message: ")
            shift = ask_for_shift()

            encrypted = caesar_cipher(text, shift)
            print()
            print("Original message :", text)
            print("Encrypted message:", encrypted)

            show_frequency(encrypted)

            print()
            print("Decrypted again  :", caesar_decipher(encrypted, shift))

        else:
            print("Sorry, that is not one of the choices. Please pick 1 to 5.")


# Only run the menu when this file is started directly, so that the test file
# can import the functions without the menu popping up.
if __name__ == "__main__":
    main()