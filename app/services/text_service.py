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
    def index_text(self, text):
        return TextResource(text)

    def parse_text(self, text: str, method: str):
        """Parse text into bag of words.

        Args:
        text (str): The raw text to be indexed in mem.
        method (str): Method to compute from raw text.
            Can be one of the following count, length, full_length

        """

        parsed = self.index_text(text)


        if method == "count":
            return parsed.compute_count_and_sort()
        elif method == "length":
            return parsed.compute_length_of_words()
        elif method == "full_length":
            return parsed.length


        raise NotImplementedError(f"method {method} not yet implemented")
