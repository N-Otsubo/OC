from time import sleep


class Player:
    _x, _y = 0, 0
    _level = 0
    _MAX_HP = 0
    _HP = 0
    _strength = 0
    _exe = 0
    _level_table = {
        1: 10,
        2: 30,
        3: 70,
        4: 130,
        5: 210,
        6: 320,
        7: 460,
        8: 630,
        9: 850,
        10: 0
    }

    def __init__(self):
        self._x = 0
        self._y = 0
        self._level = 1
        self._MAX_HP = 10
        self._HP = self._MAX_HP
        self._strength = 1

    @property
    def level(self):
        return self._level

    @property
    def MAX_HP(self):
        return self._MAX_HP

    @property
    def HP(self):
        return self._HP

    @property
    def exe(self):
        return self._exe

    def attack(self, stdscr, monster):
        stdscr.addstr(18, 1, f"プレイヤーの攻撃 モンスターに{self._strength}のダメージ！！")
        monster.HP -= self._strength
        sleep(0.5)

    def damage(self, stdscr, strength):
        stdscr.addstr(18, 1, f"モンスターの攻撃 プレイヤーに{strength}のダメージ！！")
        self._HP -= strength

    def gain_exe(self, exe):
        self._exe += exe

        if self._level_table[self._level] < self._exe:
            exe_buf = self._exe
            while 0 < exe_buf:
                exe_buf -= self._level_table[self._level]
                self.level_UP()

    def level_UP(self):
        self._level += 1
        self._MAX_HP += 4 # todo:確率で増加量が変動
        self._strength += 2 # todo:Lv1~9までは+2,Lv10で+3

    def position(self):
        return (self._x, self._y)

    def init_position(self, x, y):
        self._x = x
        self._y = y

    def move(self, key, map):
        x, y = self._x, self._y

        if key == ord('w'):  # 上に移動
            y -= 1
        elif key == ord('s'):  # 下に移動
            y += 1
        elif key == ord('a'):  # 左に移動
            x -= 2
        elif key == ord('d'):  # 右に移動
            x += 2

        if not map.is_wall(x, y):
            self._x = x
            self._y = y
