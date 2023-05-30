# ランダムな値を出力して見よう
# ランダムな値を作ってくれるモジュールを使う宣言する
import random

# ランダムな値の作成
rand = random.random()
print(rand)

# 決められた範囲でランダムな値を作成
# 今回は1～100の範囲で作成
rand = random.randrange(1, 100)
print(rand)
