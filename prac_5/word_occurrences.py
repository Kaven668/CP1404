text_to_count = {}
text = input("Text:")
words = text.split()
for i in words:
    count = text_to_count.get(i, 0)
    text_to_count[i] = count + 1

words = list(text_to_count.keys())
words.sort()

max_length = max(len(i) for i in words)

for i in words:
    print("{:{}}:{}".format(i, max_length, text_to_count[i]))
