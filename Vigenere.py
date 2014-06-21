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

TEST_MESSAGE = "THISISATESTMESSAGE"
TEST_KEY = "KEY"


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
    return message == TEST_MESSAGE


def hack_cypher(secret, alphabet, keylen=4):
    """
    Tries to decrypt the secret message by brute force. This keep trying key combinations with different key length until keylen is reached.
    :param secret: the cyphered message
    :param alphabet: string containing all the valid characters
    :param keylen: the maximum key length
    """
    if keylen > 8:
        print("The key's length is to long")
        return
    for klen in range(1, keylen + 1):
        for key in [''.join(c) for c in permutations(list(MAY), klen)]:
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


def main():
    alphabet = MAY

    #message = raw_input('Write the message to cypher: ')
    #key = raw_input('Input the key: ')

    #secret_message = cypher(message, key, MAY)
    #mes = cypher(secret_message, key, MAY, True)

    secret_message = cypher(TEST_MESSAGE, TEST_KEY, alphabet)
    print(secret_message)
    #hack_cypher(secret_message, alphabet, 3)

    #IC = calculate_IC(secret_message, alphabet)
    #print(IC)

main()