from collections import Counter
def at(text):
    words = text.split()
    mcw = Counter(words).most_common(1)[0][0]
    lw = max(words, key=len)
    return mcw, lw
input_text = input("Введите текст: ")
common, l = at(input_text)
print(f"Самое частое слово: {common}")
print(f"Самое длинное слово: {l}")