def count_words():
    sentence = input("Text: ")
    words = sentence.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    max_length = max(len(word) for word in counts.keys())
    for word, count in sorted(counts.items()):
        print(f"{word:<{max_length}} : {count}")
count_words()