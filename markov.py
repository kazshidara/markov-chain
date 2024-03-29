"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    file = open(file_path)
    txt = file.read()
    
    return txt

def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    # returns an array of words ~.split() without any arguments splits at \n as well
    word_list = text_string.split()

    for i in range(len(word_list) - 2):
        key = (word_list[i], word_list[i + 1])

        word_to_add = word_list[i + 2]
       
        chains[key] = chains.get(key, []) + [word_to_add]
        
    return chains


def make_text(chains):
    """Return text from chains."""


    words = []
    key = choice(list(chains))
    
    while chains.get(key):
        word = choice(chains[key])
        link = [key[0], key[1], word]
        words += link
        key = (key[1], word)

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
