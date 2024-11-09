# import os
import curses
# from termcolor import cprint
# import keyboard
from time import sleep
from player import Player
from monster import Monster
from map import Map


def draw_game(stdscr, filename):
    stdscr.clear()
    with open(f"./map_data/{filename}.txt", 'r') as file:
        for i, line in enumerate(file):
            line = line.rstrip("\n")
            stdscr.addstr(i, 1, line)

    stdscr.refresh()


def main(stdscr):
    stdscr.nodelay(False)

    map = Map()
    player = Player()
    player.init_position(map.init_x, map.init_y)

    monster = Monster()

    draw_game(stdscr, "start")
    press_enter(stdscr)

    while True:
        # 画面描画
        stdscr.clear()
        x, y = player.position()

        stdscr.addstr(1, 1, f"  {map.Floor}F                                  Lv.{player.level}  curses  {player.HP}/{player.MAX_HP}")
        map.print_map(stdscr, player, monster)

        key = stdscr.getch()
        # 判定
        map.next_floor(stdscr, key, x, y)

        if end_game(stdscr, map.Floor, key):
            break

        if map.is_monster(player, monster):
            stdscr.addstr(18, 1, "モンスターが現れた")

        # プレイヤー行動
        if key == ord('\n') or key == 10:
            player.attack(stdscr, monster)
        else:
            player.move(key, map)

        # 敵行動
        if map.is_player(player, monster):
            player.damage(stdscr, monster.Strength)
        else:
            monster.move(map)

        stdscr.refresh()
        sleep(0.1)


def press_enter(stdscr):
    while True:
        key = stdscr.getch()
        if key == ord('\n') or key == 10:
            break
        sleep(0.1)


def end_game(stdscr, floor, key):
    if floor == 2 or key == ord("q"):
        draw_game(stdscr, "complete")
        press_enter(stdscr)
        return True

    return False


if __name__ == '__main__':
    curses.wrapper(main)
