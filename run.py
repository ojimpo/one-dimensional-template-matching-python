import csv
import numpy as np

# CSVファイルを読み込んでdataという配列に格納する
with open('l_knee_angles_formatted.csv') as f:
    data = f.read().splitlines()

# data配列の一部をliceを用いて切り出してテンプレートとする
template = data[30:60]

# 配列内の要素の型をint型に変換する
data = [float(i) for i in data]
template = [float(i) for i in template]

# スコア格納用の配列を作成
diffScores = []

for i in range(0, len(data), 1):
    scan = data[i:i+len(template)]
    score = []
    for j in range(len(scan)):
        diff = abs(scan[j] - template[j])
        score.append(diff)
    diffScores.append(sum(score))

print('min score is: ' + str(np.min(diffScores)) + ', min index is: ' + str(np.argmin(diffScores)))
print(diffScores)