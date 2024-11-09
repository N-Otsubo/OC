class Map:
    _floor = 1
    map_data = []
    map_config = [
        {"file": "map1.txt", "x": 49, "y": 9}
    ]

    def __init__(self):
        self.load_map()

    @property
    def Floor(self):
        return self._floor

    @property
    def init_x(self):
        return self.map_config[self._floor - 1]["x"]

    @property
    def init_y(self):
        return self.map_config[self._floor - 1]["y"]

    def load_map(self):
        with open(f"./map_data/{self.map_config[self._floor - 1]['file']}", 'r') as file:
            for line in file:
                line = line.rstrip("\n")

                if len(line) < 60:
                    line = line.ljust(60, " ")
                elif len(line) > 60:
                    line = line[:60]

                self.map_data.append(list(line))

    def print_map(self, stdscr, player, monster):
        p_x, p_y = player.position()
        m_x, m_y = monster.position()
        for _y in range(len(self.map_data)):
            for _x in range(len(self.map_data[p_y])):
                if _x == p_x and _y == p_y:
                    stdscr.addstr(_y+2, _x, "@")
                elif _x == m_x and _y == m_y:
                    stdscr.addstr(_y+2, _x, "D")
                else:
                    stdscr.addstr(_y+2, _x, self.map_data[_y][_x])

        stdscr.refresh()

    def is_wall(self, x, y):
        return self.map_data[y][x] in ['-', '|', ' ']

    def is_move_valid(self, x, y):
        if 0 <= x < len(self.map_data[0]) and 0 <= y < len(self.map_data):
            return not self.is_wall(x, y)  # 壁でない場合に移動可能
        return False

    def is_monster(self, player, monster):
        p_x, p_y = player.position()
        m_x, m_y = monster.position()
        # 周囲8マスの相対座標
        directions = [(-1, -2), (-1, 0), (-1, 2), (0, -2), (0, 2), (1, -2), (1, 0), (1, 2)]

        for dy, dx in directions:
            _x, _y = p_x + dx, p_y + dy
            if _x == m_x and _y == m_y:
                return True
        return False

    def is_player(self, player, monster):
        p_x, p_y = player.position()
        m_x, m_y = monster.position()
        # 周囲8マスの相対座標
        directions = [(-1, -2), (-1, 0), (-1, 2), (0, -2), (0, 2), (1, -2), (1, 0), (1, 2)]

        for dy, dx in directions:
            _x, _y = m_x + dx, m_y + dy
            if _x == p_x and _y == p_y:
                return True
        return False

    def is_item(self, x, y):
        return self.map_data[y][x] == '?'

    def is_floor(self, x, y):
        return self.map_data[y][x] == '<'

    def next_floor(self, stdscr, key, x, y):
        if self.is_floor(x, y):
            stdscr.addstr(18, 1, "階段を登りますか？ (Y/n)")
            if key == ord("Y") or key == ord("y"):
                self._floor += 1
