class Monster:
    _HP = 10
    _strength = 1
    x = 49
    y = 11

    @property
    def HP(self):
        return self.HP

    @property
    def Strength(self):
        return self._strength

    def position(self):
        return (self.x, self.y)

    def init_position(self, x, y):
        self.x, self.y = x, y

    # 行動
    def move(self, map):
        pass

    # 攻撃
    # プレイヤー検知
