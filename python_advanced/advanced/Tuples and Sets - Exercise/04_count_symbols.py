text = [c for c in input()]

char_occ = {}

for char in text:
    if char not in char_occ:
        char_occ[char] = text.count(char)

char_occ = (sorted(char_occ.items()))

for char, occ in char_occ:
    print(f"{char}: {occ} time/s")



