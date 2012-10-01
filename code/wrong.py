def uppercase_words(words):
    """Take a list of words and upper case them
    """
    return [w.upper() for w in words]


print(uppercase_words("word1"))


def remove_expired_files():
    # use a global variable for the path
    for log_file in glob(LOG_DIR):
        pass
