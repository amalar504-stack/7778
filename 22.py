f = open("log.txt", "r")
text = f.read()
f.close()

words = text.split()

counts = {}

for w in words:
    if w in counts:
        counts[w] += 1
    else:
        counts[w] = 1

f = open("word_stats.txt", "w")

for i in range(10):
    max_word = ""
    max_count = 0

    for w in counts:
        if counts[w] > max_count:
            max_count = counts[w]
            max_word = w

    if max_word != "":
        f.write(max_word + " " + str(max_count) + "\n")
        counts[max_word] = 0 

f.close()