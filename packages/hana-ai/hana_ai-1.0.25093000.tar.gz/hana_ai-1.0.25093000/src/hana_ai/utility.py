"""
Utility functions for counting tokens in a query.
"""
# check nltk has been installed, if not install it and reload the module
try:
    import nltk
except ImportError:
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "nltk"])
    import nltk

def count_tokens(query):
    """
    Counts the number of tokens in the given query.

    Parameters
    ----------
    query : str
        The input query.

    Returns
    -------
    int
        The number of tokens in the query.
    """
    return len(nltk.word_tokenize(query))

def remove_prefix_sharp(table_name):
    """
    Removes the '#' prefix from the given table name.

    Parameters
    ----------
    table_name : str
        The input table name.

    Returns
    -------
    str
        The table name without the '#' prefix.
    """
    if table_name.startswith("#"):
        return table_name[1:]
    return table_name
