with open('books/frankenstien.txt', 'r') as f:
    book = f.read()

print(book)

counter = book.split()

chars = {}

text = book.lower()

for c in text:
    if c in chars:
        chars[c] += 1
    else:
        chars[c] = 1


sortedChars = list(chars.items())
sortedChars.sort(key=lambda item: item[1], reverse=True)

print(f"--- Begin report of {f} ---")
print(f"{len(counter)} words found in the document\n")

for char, count in sortedChars:
    print(f"The '{char}' character was found {count} times")

print("--- End report ---")
