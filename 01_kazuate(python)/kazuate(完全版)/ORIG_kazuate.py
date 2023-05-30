import random
from colorama import init
from termcolor import colored

# Ctrl+cで処理を終了する
import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# 文字列の色を変える
init()
title = colored('Kazuate Game','cyan')
rule = colored('1～50','red')

print("\t--------------------------")
print("\t|    " + title + "       |")
print("\t--------------------------")
print("\n " + rule + "までの数字を入力して、隠された数字を当ててください.")

def guess_num(num):
    """
    目標値を当てるまでループを続ける

    Args:
        num : int
            目標値
    Examples:
        number = random.randrange(1,100)
        guess_num(number) 
    """
    tries = 0 # 予想回数
    while True:
        guess = input("\n予想 : ")
        tries += 1
        if guess.isdigit() :
            guess = int(guess)
            if guess > num:
                print ("もっと小さい")
            elif guess < num:
                print ("もっと大きい")
            else:
                print ("\nご名答! 隠された数字は%sです." % colored(num, 'red'))
                print ("挑戦回数は%s回でした!\n" % colored(tries,'red'))
                return
        else:
            print ("数字を入力してください.\n")

while True:
    # 目標値設定
    # １～１００までの数字をランダムに生成
    the_number = random.randrange(1,50)

    #予想ループ開始
    guess_num(the_number) 

    # 終了判定
    play = input("もう一度挑戦しますか？（y/n）").lower()

    if  play == "n":
        # "n"または"N"を入力したらループ終了
        print("遊んでくれてありがとう！またね！！")
        break
    else:
        print("\n--------------------------")
        print("" + rule + "までの数字を入力して、隠された数字を当ててください.")
