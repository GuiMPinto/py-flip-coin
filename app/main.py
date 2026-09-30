import random


result = random.choice(['heads', 'tails'])

counts = [0] * 11
for _ in range(10000):
    heads = 0
    for _ in range(10):
        if random.choice(['heads', 'tails']) == 'heads':
            heads += 1
    counts[heads] += 1

percentages = {}
for heads, count in counts.items():
    percentages[heads] = round((count / 10000) * 100, 2)




