import tkinter as tk
from tkinter import messagebox
from functools import partial
import random
import sys

#
screenHeight = 390
screenWidth = 390


class Application(tk.Frame):
    judgeFlg = 3
    judgeMsg = ""

    def __init__(self, master=None):
        super().__init__(master)

        self.mainframe = tk.Frame(self.master)
        self.mainframe.pack()

        self.frame1 = tk.Frame(self.master)
        self.frame1.grid(row=0, column=0, in_=self.mainframe, pady=50)

        self.cells = [[tk.StringVar() for i in range(3)] for j in range(3)]

        self.createButtonsWithGrid(cellSize=9, gridSize=3, fontSize=10)

    def createButtonsWithGrid(self, cellSize, gridSize: int, fontSize=0, cellSpace=0):
        for i in range(0, gridSize):
            for j in range(0, gridSize):
                button = tk.Button(
                    self.frame1,
                    relief="groove",
                    width=cellSize,
                    height=int(cellSize / 2),
                    textvariable=self.cells[i][j],
                    font=("system", fontSize),
                    command=partial(self.clicked, (i, j))
                )
                button.grid(column=i, row=j, padx=cellSpace, pady=cellSpace)

    def clicked(self, p):
        if (self.checkCell(p, "x") or self.checkCell(p, "o")):
            print("pass", (self.checkCell(p, "x"), self.checkCell(p, "o")))
            pass
        else:
            self.chengeCell(p, "o")
            app.update()

            if self.judgeGame(p, "o"):
                ans = messagebox.askyesno("勝利", "プレイヤーの勝利です。\nもう一度プレイしますか?")
                if ans:
                    self.resetGame()
                else:
                    sys.exit()
            else:
                enemyPos = self.setEnemy()
                app.update()

                if enemyPos[0] < 0:
                    ans = messagebox.askyesno("引き分け", "引き分けました。\nもう一度プレイしますか?")
                    if ans:
                        self.resetGame()
                    else:
                        sys.exit()

                if self.judgeGame(enemyPos, "x"):
                    ans = messagebox.askyesno("敗北", "あなたは敗北しました。\nもう一度プレイしますか?")
                    if ans:
                        self.resetGame()
                    else:
                        sys.exit()

    def chengeCell(self, p, msg):
        # print(p)
        self.cells[p[0]][p[1]].set(msg)

    def setEnemy(self):
        if self.checkWholeBoard():
            return (1, -1)

        i = random.randint(0, len(self.cells) - 1)
        j = random.randint(0, len(self.cells) - 1)

        while self.checkCell((i, j), "o") or self.checkCell((i, j), "x"):
            i = random.randint(0, len(self.cells) - 1)
            j = random.randint(0, len(self.cells) - 1)

        self.chengeCell((i, j), "x")
        return (i, j)

    def judgeGame(self, p: tuple, c):
        maxIndex = len(self.cells)-1

        if p[0] == maxIndex:
            if p[1] == maxIndex:
                # 右下
                if (self.checkCell((p[0], p[1]-2), c) and self.checkCell((p[0], p[1]-1), c)):
                    return True
                elif (self.checkCell((p[0]-2, p[1]), c) and self.checkCell((p[0]-1, p[1]), c)):
                    return True
                elif (self.checkCell((p[0]-2, p[1]-2), c) and self.checkCell((p[0]-1, p[1]-1), c)):
                    return True
            elif p[1] == 0:
                # 右上
                if (self.checkCell((p[0]-2, p[1]), c) and self.checkCell((p[0]-1, p[1]), c)):
                    return True
                elif (self.checkCell((p[0], p[1]+2), c) and self.checkCell((p[0], p[1]+1), c)):
                    return True
                elif (self.checkCell((p[0]-2, p[1]+2), c) and self.checkCell((p[0]-1, p[1]+1), c)):
                    return True
            else:
                # 右中
                if (self.checkCell((p[0], p[1]-1), c) and self.checkCell((p[0], p[1]+1), c)):
                    return True
                elif (self.checkCell((p[0]-1, p[1]), c) and self.checkCell((p[0]-2, p[1]), c)):
                    return True
                return False

        elif p[0] == 0:
            if p[1] == maxIndex:
                # 左下
                if (self.checkCell((p[0], p[1]-2), c) and self.checkCell((p[0], p[1]-1), c)):
                    return True
                elif (self.checkCell((p[0]+2, p[1]), c) and self.checkCell((p[0]+1, p[1]), c)):
                    return True
                elif (self.checkCell((p[0]+2, p[1]-2), c) and self.checkCell((p[0]+1, p[1]-1), c)):
                    return True
            elif p[1] == 0:
                # 左上
                if (self.checkCell((p[0]+2, p[1]), c) and self.checkCell((p[0]+1, p[1]), c)):
                    return True
                elif (self.checkCell((p[0], p[1]+2), c) and self.checkCell((p[0], p[1]+1), c)):
                    return True
                elif (self.checkCell((p[0]+2, p[1]+2), c) and self.checkCell((p[0]+1, p[1]+1), c)):
                    return True
            else:
                # 左中
                if (self.checkCell((p[0], p[1]-1), c) and self.checkCell((p[0], p[1]+1), c)):
                    return True
                elif (self.checkCell((p[0]+1, p[1]), c) and self.checkCell((p[0]+2, p[1]), c)):
                    return True
                return False

        else:
            if p[1] == 0:
                # 中上
                if (self.checkCell((p[0]-1, p[1]), c) and self.checkCell((p[0]+1, p[1]), c)):
                    return True
                elif (self.checkCell((p[0], p[1]+1), c) and self.checkCell((p[0], p[1]+2), c)):
                    return True
            elif p[1] == maxIndex:
                # 中下
                if (self.checkCell((p[0]-1, p[1]), c) and self.checkCell((p[0]+1, p[1]), c)):
                    return True
                elif (self.checkCell((p[0], p[1]-1), c) and self.checkCell((p[0], p[1]-2), c)):
                    return True
            else:
                # 中中
                if (self.checkCell((p[0]-1, p[1]), c) and self.checkCell((p[0]+1, p[1]), c)):
                    return True
                elif (self.checkCell((p[0], p[1]+1), c) and self.checkCell((p[0], p[1]+1), c)):
                    return True
                if (self.checkCell((p[0]-1, p[1]-1), c) and self.checkCell((p[0]+1, p[1]+1), c)):
                    return True
                elif (self.checkCell((p[0]+1, p[1]-1), c) and self.checkCell((p[0]-1, p[1]+1), c)):
                    return True
                return False

    def checkCell(self, p, c):
        return self.cells[p[0]][p[1]].get() == c

    def checkWholeBoard(self):
        for i in self.cells:
            for j in i:
                if j.get() == "":
                    return False
        return True

    def resetGame(self):
        for i in self.cells:
            for j in i:
                j.set("")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("○×ゲーム")
    root.geometry(str(screenWidth) + "x" + str(screenHeight))
    app = Application(master=root)
    app.mainloop()
