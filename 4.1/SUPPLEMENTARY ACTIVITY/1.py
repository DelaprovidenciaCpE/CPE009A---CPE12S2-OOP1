def word_filter(sentence, bad_words):
    words = sentence.split()

    for i in range(len(words)):
        if words[i].lower() in bad_words:
            words[i] = "*" * len(words[i])

    return " ".join(words)



text = "This is a bad example sentence"
bad = ["bad", "example"]

print(word_filter(text, bad))

