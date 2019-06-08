import numpy as np

data = [1, 1, 4, 5, 1, 4, 8, 1, 0, 1, 9, 1, 9]
template = [8, 1, 0]

diffScores = []

for i in range(0, len(data), len(template)):
    scan = data[i:i+len(template)]
    score = []
    for j in range(len(scan)):
        diff = abs(scan[j] - template[j])
        score.append(diff)
        print(diff)
    diffScores.append(sum(score))

print('min index is: ' + str(np.argmin(diffScores)))
bestScoreIndex = len(template) * np.argmin(diffScores)
print(bestScoreIndex)

print(diffScores)