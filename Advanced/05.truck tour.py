text = input()

histogram = {}

for letter in text:
    if letter not in histogram:
        histogram[letter] = 0
    histogram[letter] += 1
    # histogram[letter] = histogram.get(letter, 0) + 1

for letter in sorted(histogram):
    print(f"{letter}: {histogram[letter]} time/s")