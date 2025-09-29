# Merge dictionaries

## Root problem

You uses everal IDEs and each maintain its own spelling dictionary.

You want to merge them so words from PyCharm are available in PhpStorm too.

## Usage

### Merge all dictionaries

To discover dictionaries in your computer, extract words and merge them:

```shell
$ merge-dictionaries --merge
```

This is a potentially destructive operation:
your dictionary files will be overwritten.

### Extract dictionaries words

To print all the words:

```shell
$ merge-dictionaries --extract
```

This is a safe operation.

### Build an Hunspell-compatible dictionary

To create a personal dictionary file for your Hunspell dictionary:

```shell
$ merge-dictionaries --extract > $HOME/.hunspell_default
```

This is a safe read-only operation for your IDE files. This can
overwrite your default Hunspell dictionary if it already exists.

### Build a dictionary in a IDE specific format

You can specify `--format=<format>` as argument to the extract task:

```shell
$ merge-dictionaries --extract --format=JetBrains
```

It will output a dictionary file you can use in any IDE compatible with that format.

This is a safe read-only operation.

### Sync with a Git repository

Create a `$HOME/.config/merge-dictionaries.conf` with the following content:

```yaml
git:
  - git@github.com:luser/dictionary.git
```

See below if you wish to host the Git repository locally.

### Delete words from a dictionary

Now your dictionaries are synced, it can be tricky to delete words from them,
as the next sync will overwrite them and restore words you removed if still in
the Git repository or one local fi
le.

If you added a word in a dictionary, you can delete it:

```shell
$ merge-dictionaries --delete-words <word> [word ...]
```

This is a potentially destructive operation:
your dictionary files will be overwritten.

## IDE support

Currently, the following IDEs are supported

* All JetBrains IDEs: application-level dictionary
* Hunspell: read personal dictionaries
* Git repository

## Extend the code
### How to add an IDE?

To add an IDE, you need to provide the following methods:

* sources
  * a list of paths candidates for the IDE dictionary
  * a method extracting words from the dictionary
* output
  * a method to dump the extracted words in the IDE format
* write
  * a method to save the files, normally you can call the ones created
  * a method to rewrite a file with a list of words, so delete works too

### How can I contribute?

You can commit your changes to the upstream by following instructions at https://agora.nasqueron.org/How_to_contribute_code

The canonical repository is https://devcentral.nasqueron.org/source/merge-dictionaries.git

## FAQ

### Host locally the Git repository

If you want to host the repository on your local machine, use a bare repository:

```shell
$ git init --bare ~/.cache/dictionary
Initialized empty Git repository in /usr/home/luser/.cache/dictionary/
```

You can push to a bare repository, but non-bare ones are protected against pushes,
to avoid a desync between your index and the working files. 

Alternatively, you can prepare a script to do this sequence of operation:
```shell
$ merge-dictionaries --merge
$ cd  ~/.cache/dictionary
$ git reset
```

## License

BSD-2-Clause, see [LICENSE](LICENSE) file.
