"""Text Resource Module.

This module contains the class for handling text.
"""

import numpy as np
import enchant
import re

class TextResource:
    """Class that handles text to get statistics."""

    def __init__(self, text: str):
        """Class constructor.
        
        Initializes the English dictionary to check for english words.
        """
        self.dictionary = enchant.Dict("en_US")
        self.text = text
        self.length = len(text)

    @property
    def text(self):
        """Getter for text."""
        return self._text

    @text.setter
    def text(self, text):
        """Index text into memory by parsing it to bag of words.

        Args:
        text (str): The raw text to be indexed in mem.

        """
        bag_of_words = re.split("[^a-z0-9']+", text.lower())
        bag_of_words = [
            word for word in bag_of_words if len(word) != 0
        ]

        filtered_words = [
            word for word in bag_of_words if self.dictionary.check(word) is True
        ]

        self._text = filtered_words


    def compute_count_and_sort(self):
        """Compute count of the the words from text and sort alphabetically."""

        unique, counts = np.unique(self.text, return_counts=True)

        return sorted(list(zip(unique, counts)), key=lambda row: row[0])

    def compute_length_of_words(self):
        """Compute count of the the words from text and sort alphabetically."""

        return len(self.text)
