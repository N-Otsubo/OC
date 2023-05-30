import random

print("\t--------------------------")
print("\t|    Kazuate Game       |")
print("\t--------------------------")
print("1から50までの数字を入力して、隠された数字を当ててください。")


def guess_num(num):
    tries = 0 # 予想回数
    while True:
        guess = int(input("予想 : "))
        tries += 1

        if guess > num:
            print("もっと小さい")
        elif guess < num:
            print("もっと大きい")
        else:
            print("ご名答! 隠された数字は%sです。" % num)
            print("挑戦回数は%s回でした!\n" % tries)
            return


while True:
    # 目標値設定
    # １～１００までの数字をランダムに生成
    the_number = random.randrange(1, 50)

    # 予想ループ開始
    guess_num(the_number)

    # 終了判定
    play = input("もう一度挑戦しますか？（y/n）")
    if play == "N":
        # "N"を入力したらループ終了
        print("遊んでくれてありがとう！またね！！")
        break
