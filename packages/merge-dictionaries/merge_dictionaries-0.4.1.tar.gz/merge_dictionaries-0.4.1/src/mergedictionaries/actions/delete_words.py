#!/usr/bin/env python3

#   -------------------------------------------------------------
#   Delete words from all dictionaries
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#   Project:        Nasqueron
#   Description:    Delete words from all dictionaries from
#                   all currently found sources.
#   License:        BSD-2-Clause
#   -------------------------------------------------------------


from mergedictionaries import sources, write
from mergedictionaries.sources import GitRepository


class DeleteAction:
    def __init__(self, context):
        self.git_config = context["config"].get("git", [])

        if "git" not in context:
            context["git"] = []
        self.git_cached_repos = context["git"]

    def run(self, words):
        for source in self.get_sources():
            for arg in source["query"]():
                source["delete"](words, arg)

    def get_sources(self):
        return [
            {
                "query": sources.jetbrains.find_application_level_dictionaries,
                "delete": lambda words, file: write.jetbrains.delete_words(file, words),
            },
            {
                "query": self.query_git_repositories,
                "delete": lambda words, repo: write.git.delete_words(repo, words),
            },
        ]

    def query_git_repositories(self):
        return [
            GitRepository(git_repo_url, self.git_cached_repos)
            for git_repo_url in self.git_config
        ]
