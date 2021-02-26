score_keys = []
scores = {'C': 4, 'A': 1, 'B': 1, 'E': 4, 'D': 6}
new_scores = sorted(scores.items(), key=lambda item:item[1], reverse=True)
for x in new_scores:
    score_keys.append(x[0])
print(scores)
print(new_scores)
print(score_keys)