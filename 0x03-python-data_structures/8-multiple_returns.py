(sentence):
    if not sentence:
        return (0, None)

    return (len(sentence), sentence[0])
