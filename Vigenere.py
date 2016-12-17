from __future__ import division
from itertools import permutations
import string

__author__ = 'Jorge Marey'

MAY = string.ascii_uppercase
MIN = string.ascii_lowercase
NUMBERS = string.digits
WHITESPACES = string.whitespace
PUNCTUATION = string.punctuation
ALL_PRINTABLE = string.printable

clear_message = ''

def cypher(message, key, alphabet, decrypt=False):
    """
    This function creates a secret message from the original and the key.
    :param message: string that contains the original message to cypher
    :param key: secret password used to create the secret message, as a string
    :param alphabet: string containing all the valid characters
    :param decrypt: True if the message is already cyphered
    :return: the cyphered message
    """
    key_len = len(key)
    alphabet_len = len(alphabet)
    opp = lambda x, y: x - y if decrypt else x + y
    secret = [alphabet[opp(alphabet.index(message[i]), alphabet.index(key[i % key_len])) % alphabet_len] for i in
              range(len(message))]
    return ''.join(secret)


def key_found(key, secret, alphabet):
    """
    Returns true if the provided key decrypts the secret message.
    :param key: the key to check
    :param secret: the cyphered message
    :param alphabet: string containing all the valid characters
    :return: True if the key is valid, False otherwise
    """
    message = cypher(secret, key, alphabet, True)
    return message == clear_message


def hack_cypher(secret, alphabet, key_len=4):
    """
    Tries to decrypt the secret message by brute force. This keep trying key combinations with different key length
    until key_len is reached.
    :param secret: the cyphered message
    :param alphabet: string containing all the valid characters
    :param key_len: the maximum key length
    """
    if key_len > 8:
        print("The key's maximum length is 8")
        return
    for n in range(1, key_len + 1):
        for key in [''.join(c) for c in permutations(list(MAY), n)]:
            if key_found(key, secret, alphabet):
                print("Key guessed!")
                return
    print("The key's length was not enough to decrypt the message")


def calculate_IC(message, alphabet):
    """
    Calculates de index of coincidence for a given message.
    :param message: the message for which to calculate de index of coincidence
    :param alphabet: string containing all the valid characters
    :return: the IC value for the message
    """
    addhoc_mult = lambda x: x * (x - 1)
    return sum(addhoc_mult(message.count(letter)) for letter in alphabet) / addhoc_mult(len(message))


def check_text(text, alphabet):
    """
    Check if all the characters of a text are contained the selected alphabet
    :param text: the text to check
    :param alphabet: all the possible characters
    :return: True if the text is valid, False otherwise
    """
    for letter in text:
        if letter not in alphabet:
            return False
    return True


def select_value(alphabet, show_text, fail_text="Please, insert only characters from the alphabet selected before"):
    """
    Return text entered by the user from the system input. This checks that the input text is correct.
    :param alphabet: All the possible characters of the text
    :param show_text: The text to show in the prompt
    :param fail_text: The text to show if there is a problem with the input.
    :return: the text inserted by the user
    """
    while True:
        message = raw_input(show_text)
        if not check_text(message, alphabet):
            print(fail_text)
            continue
        return message


def main():
    alphabet = ''

    print("Select the alphabet\n - u : uppercase letters\n - l : lowercase letters\n - n : numbers")
    print(" - p : punctuation\n - w : whitespaces\n         p.e : ul means uppercase and lowercase")
    s_alph = select_value('ulpnw', 'Components of the alphabet: ', "Please, insert only one or more of ulnpw")

    alphabet += MAY if 'u' in s_alph else ''
    alphabet += MIN if 'l' in s_alph else ''
    alphabet += NUMBERS if 'n' in s_alph else ''
    alphabet += PUNCTUATION if 'p' in s_alph else ''
    alphabet += WHITESPACES if 'w' in s_alph else ''

    message = select_value(alphabet, 'Write the message to cypher: ')
    global clear_message
    clear_message = message
    key = select_value(alphabet, 'Input the key: ')

    secret_message = cypher(message, key, alphabet)
    print('The encrypted message is: ' + secret_message)
    #decrypted_message = cypher(secret_message, key, alphabet, True)

    #hack_cypher(secret_message, alphabet, 3)
    #IC = calculate_IC(secret_message, alphabet)
    #print(IC)


main()
