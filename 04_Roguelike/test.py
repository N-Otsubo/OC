def is_monster(x, y):
    monster_x = 49
    monster_y = 11
    # 周囲8マスの相対座標
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1)]

    for dy, dx in directions:
        _x, _y = x + dx, y + dy
        if _x == monster_x and _y == monster_y:
            return (_x, _y)
    return False


x = 49
y = 10
if not is_monster(x, y):
    pass
else:
    print(f"{x},{y} 上 モンスターが現れた")

x = 48
y = 11
if not is_monster(x, y):
    pass
else:
    print(f"{x},{y} 左 モンスターが現れた")

x = 50
y = 11
if not is_monster(x, y):
    pass
else:
    print(f"{x},{y} 右 モンスターが現れた")

x = 49
y = 12
if not is_monster(x, y):
    pass
else:
    print(f"{x},{y} 下 モンスターが現れた")

x = 48
y = 10
if not is_monster(x, y):
    pass
else:
    print(f"{x},{y} 右上 モンスターが現れた")
