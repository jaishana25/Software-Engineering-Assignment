import string
from collections import Counter

def count_words(text):
    """
    Counts the number of words in a given text.

    Parameters:
    text (str): The text to analyze.

    Returns:
    int: The number of words in the text.
    """
    # Remove punctuation and convert to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.lower()

    # Split into words and count them
    words = text.split()
    word_count = len(words)

    return word_count


def count_sentences(text):
    """
    Counts the number of sentences in a given text.

    Parameters:
    text (str): The text to analyze.

    Returns:
    int: The number of sentences in the text.
    """
    # Count the number of sentence-ending punctuation marks
    sentence_count = text.count('.') + text.count('!') + text.count('?')

    return sentence_count


def average_sentence_length(text):
    """
    Calculates the average length of sentences in a given text.

    Parameters:
    text (str): The text to analyze.

    Returns:
    float: The average length of sentences in the text.
    """
    # Count the number of words and sentences
    word_count = count_words(text)
    sentence_count = count_sentences(text)

    # Calculate the average sentence length
    if sentence_count > 0:
        average_sentence_length = word_count / sentence_count
    else:
        average_sentence_length = 0

    return average_sentence_length


def most_common_words(text, n=3):
    """
    Finds the most common words in a given text.
    Parameters:
    text (str): The text to analyze.
    n (int): The number of most common words to return. Defaults to 3.
    Returns:
    list: A list of tuples containing the most common words and their counts.
    """
    # Remove punctuation and convert to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.lower()

    # Split into words and count them
    words = text.split()
    word_counts = Counter(words)

    # Get the most common words and their counts
    most_common = word_counts.most_common(n)

    return most_common


# Import the text analytics program
# import text_analytics_program

# Define some sample text to analyze
#sample_text = "This is some sample text. It contains several small sentences, each with different words and punctuation."
sample_text = "All of us are living in a beautiful asian country called India. Indeed we are happ."
print (sample_text)

# Test the word count function
#word_count = text_analytics_program.count_words(sample_text)
word_count = count_words(sample_text)
expected_word_count = 16 # Counted manually
assert word_count == expected_word_count, f"Error: word count should be {expected_word_count}, but got {word_count}"
print(word_count)

# Test the sentence count function
#sentence_count = text_analytics_program.count_sentences(sample_text)
sentence_count = count_sentences(sample_text)
expected_sentence_count = 2 # Counted manually
assert sentence_count == expected_sentence_count, f"Error: sentence count should be {expected_sentence_count}, but got {sentence_count}"
print(sentence_count)

# Test the average sentence length function
#average_sentence_length = text_analytics_program.average_sentence_length(sample_text)
average_sentence_length = average_sentence_length(sample_text)
expected_average_sentence_length = 8 # Counted manually
assert average_sentence_length == expected_average_sentence_length, f"Error: average sentence length should be {expected_average_sentence_length}, but got {average_sentence_length}"

# Test the most common words function
#most_common_words = text_analytics_program.most_common_words(sample_text)
most_common_words = most_common_words(sample_text)
expected_most_common_words = [("are", 2), ("all", 1), ("of", 1)] # Counted manually
assert most_common_words == expected_most_common_words, f"Error: most common words should be {expected_most_common_words}, but got {most_common_words}"
print(most_common_words)


print("All tests passed!")
