#   -------------------------------------------------------------
#   Merge dictionaries :: Utilities :: Collections
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#   Project:        Nasqueron
#   Description:    Helper functions for lists
#   License:        BSD-2-Clause
#   -------------------------------------------------------------


from typing import List


def remove_words(current_words: List, words_to_delete: List) -> List:
    """
    Removes specified words from a list of words.

    Parameters:
    current_words: list
        The list of words from which specified words are to be removed.
    words_to_delete: list
        The list containing words that need to be removed.

    Returns:
    list
        A new list containing words from the current_words list that are not
        present in the words_to_delete list.
    """
    words = list(set(current_words) - set(words_to_delete))
    words.sort()

    return words
