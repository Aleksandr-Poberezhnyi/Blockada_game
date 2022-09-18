x=y=0

for r in level:
    for c in r:
        if c == 'r':
            r1 = Settings(x, y, 40, 40,0, nothing)
            blocks_r.append(r1)
            items.add(r1)

        if c == 'l':
            r1 = Settings(x, y, 40, 40,0, nothing)
            blocks_l.append(r1)
            items.add(r1)

        if c == '/':
            r2 = Settings(x, y - 40, 40, 180, 0, stair)
            stairs.append(r2)
            items.add(r2)

        if c == '':
            r1 = Settings(x, y, 40, 40,0, coin)
            coins.append(r3)
            items.add(r3)

        if c == '*':
            r4 = Settings(x,y, 40,40 , 0, portal)
            items.add(r4)

        if c == '-':
            r5 = Settings(x, y, 40, 40 ,0 , platform)
            platforms.append(r5)
            items.add(r5)

        if c == '>':
            r6 = Settings(x, y - 40, 80, 80, 0, chest_close)
            items.add(r6)

        x +=40
    y+=40
    x = 0