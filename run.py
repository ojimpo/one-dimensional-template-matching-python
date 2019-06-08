import csv

# CSVファイルを読み込んでdataという配列に格納する
with open('l_knee_angles_formatted.csv') as f:
    data = f.read().splitlines()

# data配列の一部を切り出してテンプレートとする
# sliceを用いて切り出す
template = data[30:60]

# 元データ配列, テンプレート配列の要素数を取得
dlength = len(data)
tlength = len(template)

#元データの一番後ろを取得
dlast = data[-1]

# スコア格納用の配列を作成
# 一番小さな値のインデックスがテンプレートと一致する位置
score = []

# テンプレートと同じ長さのデータを, 元データの最初から最後まで順番に取り出していく
calcdata = []
for calc in range(dlength):
    print(calc)
for i in template:
    print()
# 取り出したものとテンプレート間で, すべての値の絶対値の差を求める
# 全ての桁の差を足し合わせ、それをスコアとする
# スコアが一番小さかった部分が一致度が最も高い. そんインデックスを出力する

print(template)
print(data[-1])