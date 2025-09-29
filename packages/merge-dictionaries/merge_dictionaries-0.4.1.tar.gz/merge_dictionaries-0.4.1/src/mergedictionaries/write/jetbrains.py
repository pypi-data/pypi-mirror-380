#   -------------------------------------------------------------
#   Merge dictionaries :: Publishers :: JetBrains IDEs
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#   Project:        Nasqueron
#   Description:    Find application-level dictionaries
#                   from JetBrains IDEs
#   License:        BSD-2-Clause
#   -------------------------------------------------------------


from mergedictionaries.sources import jetbrains as jetbrains_source
from mergedictionaries.output import jetbrains as jetbrains_output
from mergedictionaries.utils.collections import remove_words


def write(words):
    contents = jetbrains_output.dump(words)

    for file_path in jetbrains_source.find_application_level_dictionaries():
        with open(file_path, "w") as fd:
            fd.write(contents)
            fd.write("\n")


def delete_words(file_path, words_to_delete):
    current_words = jetbrains_source.extract_words(file_path)

    if not any(word in current_words for word in words_to_delete):
        # Nothing to do, the dictionary is already up to date.
        return

    words = remove_words(current_words, words_to_delete)

    contents = jetbrains_output.dump(words)
    with open(file_path, "w") as fd:
        fd.write(contents)
        fd.write("\n")
