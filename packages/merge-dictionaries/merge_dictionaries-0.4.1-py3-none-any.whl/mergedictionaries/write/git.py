#   -------------------------------------------------------------
#   Merge dictionaries :: Publishers :: Git repository
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#   Project:        Nasqueron
#   Description:    Find application-level dictionaries
#                   from Git repository
#   License:        BSD-2-Clause
#   -------------------------------------------------------------


import os
from tempfile import NamedTemporaryFile
from typing import List

from mergedictionaries.sources import GitRepository
from mergedictionaries.utils.collections import remove_words


def build_temporary_dictionary(words):
    fd = NamedTemporaryFile(delete=False)
    for word in words:
        fd.write(f"{word}\n".encode("utf-8"))
    fd.close()

    return fd.name


def write(words, target_repos, cached_repos):
    if not target_repos:
        return

    tmp_dictionary_path = build_temporary_dictionary(words)

    for repo in target_repos:
        GitRepository(repo, cached_repos).publish(tmp_dictionary_path)

    os.unlink(tmp_dictionary_path)


def delete_words(repo: GitRepository, words_to_delete: List):
    current_words = repo.extract_words()

    if not any(word in current_words for word in words_to_delete):
        # Nothing to do, the dictionary is already up to date.
        return

    words = remove_words(current_words, words_to_delete)

    tmp_dictionary_path = build_temporary_dictionary(words)
    repo.publish(tmp_dictionary_path)

    os.unlink(tmp_dictionary_path)
