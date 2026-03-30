# trouver top 3 mots les plus frequents

top_words = ["", "", ""]
top_counts = [0, 0, 0]

i = 0
while i < len(all_words):
    count = 0
    j = 0

    while j < len(all_words):
        if all_words[i] == all_words[j]:
            count = count + 1
        j = j + 1

    # verifier si dans top 3
    if count > top_counts[0]:
        top_counts[2] = top_counts[1]
        top_words[2] = top_words[1]

        top_counts[1] = top_counts[0]
        top_words[1] = top_words[0]

        top_counts[0] = count
        top_words[0] = all_words[i]

    elif count > top_counts[1] and all_words[i] != top_words[0]:
        top_counts[2] = top_counts[1]
        top_words[2] = top_words[1]

        top_counts[1] = count
        top_words[1] = all_words[i]

    elif count > top_counts[2] and all_words[i] != top_words[0] and all_words[i] != top_words[1]:
        top_counts[2] = count
        top_words[2] = all_words[i]

    i = i + 1

print("\nTop 3 most frequent words:")
print("1:", top_words[0], "-", top_counts[0], "times")
print("2:", top_words[1], "-", top_counts[1], "times")
print("3:", top_words[2], "-", top_counts[2], "times")