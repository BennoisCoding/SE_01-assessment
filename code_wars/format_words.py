def cleanup_words(words):
    """Remove all the empty strings."""

    while "" in words:
        words.remove("")

    return(words)


def format_words(words):
    """Formats the words of a list into a single comma separated value."""

    words = cleanup_words(words)

    string = ""

    for i in range(len(words)):
        string += words.pop(0)

        if len(words) == 1:
            string += " and "
        else:
            string += ", "

    string = string.strip(", ")
    
    print(string)


words_0 = ["four", "two", ""]
words_1 = [""]
format_words(words_0)