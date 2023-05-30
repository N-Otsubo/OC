# 繰り返し処理をやってみよう
i = 1
# iが10になるまで繰り返す
while i <= 10:
    print(i)
    i += 1

i = 1
# 無限ループ
while True:
    print(i)
    i += 1
    # iは100か？
    if i == 100:
        # trueの処理
        print("100回繰り返しました.")
        # ループを抜ける
        break
