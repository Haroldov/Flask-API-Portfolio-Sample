"""Text Service Module.

This module contains the class for handling text.
"""
from functools import lru_cache

from resources.text_parser_resource import TextResource

import numpy as np
import enchant
import re

class TextService:
    """Class that handles text to parse it using resource."""

    def __init__(self):
        """Class constructor.
        """
        pass

    @lru_cache()
    def _index_text(self, text):
        return TextResource(text)

    def agg_words_count(self, text: str):
        """Get bag of words from text.

        Args:
        text (str): The raw text to be indexed in mem.

        Return:
        list of tuples with the word in index 0 and the freq in index 1.
        """

        parsed = self._index_text(text)

        return parsed.compute_count_and_sort()

    def agg_words_number(self, text: str):
        """Get number of words from text.

        Args:
        text (str): The raw text to be indexed in mem.

        Return:
        Number of words as integer
        """

        parsed = self._index_text(text)

        return parsed.compute_length_of_words()

    def text_length(self, text: str):
        """Get text length with and without spaces.

        Args:
        text (str): The raw text to be indexed in mem.

        Return:
        tuple, index 0 contains text full length and 1 length without spaces.
        """

        parsed = self._index_text(text)

        return (parsed.length, parsed.length_no_spaces)
