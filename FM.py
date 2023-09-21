position = input("Position: ")
position2 = input("Position: ")
position3 = input("Position: ")


if position == "sk de":
    counter = counter1 = counter2 = 0
    for i in range(35):
        x = int(input("stat: "))
        counter = counter + x
        if i in range(0, 3) or i in range(4, 9) or i in range(10, 13) or i in range(16, 19) or i in (14, 23, 25, 27, 28):
            counter1 = counter1 + x
        if i in (1, 6, 7, 10, 14, 17, 23, 28):
            counter2 = counter2 + x
    sum = counter / 35
    sum1 = counter1 / 19
    sum2 = counter2 / 8
    skde = (sum + sum1 + sum2)
    secret = (int(input("stat: ")) * 3) / 10
    total = (skde + secret) / 4
    print("sk de: ", round(total, 2))


elif position == "sk su":
    counter = counter1 = counter2 = 0
    for i in range(35):
        x = int(input("stat: "))
        counter = counter + x
        if i in range(0, 3) or i in range(4, 9) or i in range(10, 13) or i in range(16, 19) or i in (14, 23, 25, 27, 28):
            counter1 = counter1 + x
        if i in (1, 6, 7, 10, 14, 17, 23, 28):
            counter2 = counter2 + x
    sum = counter / 35
    sum1 = counter1 / 19
    sum2 = counter2 / 10
    sksu = (sum + sum1 + sum2)
    secret = (int(input("stat: ")) * 3) / 10
    total = (sksu + secret) / 4
    print("sk su: ", round(total, 2))


elif position == "gk":
    counter = counter1 = counter2 = 0
    for i in range(35):
        x = int(input("stat: "))
        counter = counter + x
        if i in range(0, 3) or i in range(5, 8) or i in (10, 12, 14, 17, 18, 23, 29):
            counter1 = counter1 + x
        if i in (0, 1, 2, 5, 6, 10, 17, 23, 29):
            counter2 = counter2 + x
    sum = counter / 35
    sum1 = counter1 / 13
    sum2 = counter2 / 9
    gk = (sum + sum1 + sum2)
    secret = (int(input("stat: ")) * 3) / 10
    total = (gk + secret) / 4
    print("gk: ", round(total, 2))


else:
    stat = []
    for i in range(36):
            x = int(input("stat: "))
            stat.append(x)


if position == "wb su" or position2 == "wb su" or position3 == "wb su":
    counter = counter1 = counter2 = 0
    for i in range(36):
        if i in range(1, 5) or i in range(6, 11) or i in range(12, 37):
            counter = counter + stat[i]
        if i in range(23, 26) or i in range(27, 30) or i in (1, 2, 4, 9, 10, 12, 13, 15, 18, 19, 33, 34):
            counter1 = counter1 + stat[i]
        if i in (1, 2, 9, 12, 23, 25, 27, 28, 34):
            counter2 = counter2 + stat[i]
    sum = counter / 33
    sum1 = counter1 / 18
    sum2 = counter2 / 9
    wbsu = (sum + sum1 + sum2)
    secret = (int(input("stat: ")) * 3) / 10
    total = (wbsu + secret) / 4
    print("wb su: ", round(total, 2))


if position == "wb at" or position2 == "wb at" or position3 == "wb at":
    counter = counter1 = counter2 = 0
    for i in range(36):
        if i in range(1, 5) or i in range(6, 11) or i in range(12, 37):
            counter = counter + stat[i]
        if i in range(23, 26) or i in range(27, 30) or i in (1, 2, 4, 9, 10, 12, 13, 15, 18, 19, 21, 33, 34):
            counter1 = counter1 + stat[i]
        if i in (1, 2, 12, 13, 23, 25, 27, 28, 33, 34):
            counter2 = counter2 + stat[i]
    sum = counter / 33
    sum1 = counter1 / 19
    sum2 = counter2 / 10
    wbat = (sum + sum1 + sum2)
    secret = (int(input("stat: ")) * 3) / 10
    total = (wbat + secret) / 4
    print("wb at: ", round(total, 2))

if position == "fb su" or position2 == "fb su" or position3 == "fb su":
    counter = counter1 = counter2 = 0
    for i in range(36):
        if i in range(1, 5) or i in range(6, 11) or i in range(12, 37):
            counter = counter + stat[i]
        if i in range(17, 20) or i in (1, 2, 9, 10, 12, 13, 15, 24, 25, 27, 33, 34):
            counter1 = counter1 + stat[i]
        if i in (9, 12, 15, 18, 24, 25, 27):
            counter2 = counter2 + stat[i]
    sum = counter / 33
    sum1 = counter1 / 15
    sum2 = counter2 / 7
    fbsu = (sum + sum1 + sum2)
    secret = (int(input("stat: ")) * 3) / 10
    total = (fbsu + secret) / 4
    print("fb su: ", round(total, 2))


if position == "fb at" or position2 == "fb at" or position3 == "fb at":
    counter = counter1 = counter2 = 0
    for i in range(36):
        if i in range(1, 5) or i in range(6, 11) or i in range(12, 37):
            counter = counter + stat[i]
        if i in range(17, 20) or i in (1, 2, 4, 9, 10, 12, 13, 15, 23, 24, 25, 27, 28, 29, 33, 34):
            counter1 = counter1 + stat[i]
        if i in (1, 12, 15, 24, 25, 27, 33, 34):
            counter2 = counter2 + stat[i]
    sum = counter / 33
    sum1 = counter1 / 19
    sum2 = counter2 / 8
    fbat = (sum + sum1 + sum2)
    secret = (int(input("stat: ")) * 3) / 10
    total = (fbat + secret) / 4
    print("fb at: ", round(total, 2))


if position == "bpd de" or position2 == "bpd de" or position3 == "bpd de":
    counter = counter1 = counter2 = 0
    for i in range(36):
        if i in range(12, 37) or i in (4, 6, 9, 10):
            counter = counter + stat[i]
        if i in range(12, 20) or i in (4, 6, 9, 10, 24, 26, 31, 33, 35):
            counter1 = counter1 + stat[i]
        if i in (6, 9, 10, 12, 17, 24, 31, 35):
            counter2 = counter2 + stat[i]
    sum = counter / 28
    sum1 = counter1 / 17
    sum2 = counter2 / 8
    bpdde = (sum + sum1 + sum2)
    secret = (int(input("stat: ")) * 3) / 10
    total = (bpdde + secret) / 4
    print("bpd de: ", round(total, 2))


if position == "cd de" or position2 == "cd de" or position3 == "cd de":
    counter = counter1 = counter2 = 0
    for i in range(36):
        if i in range(12, 37) or i in (4, 6, 9, 10):
            counter = counter + stat[i]
        if i in range(14, 20) or i in (6, 9, 12, 24, 31, 33, 35):
            counter1 = counter1 + stat[i]
        if i in (6, 9, 12, 24, 31, 35):
            counter2 = counter2 + stat[i]
    sum = counter / 28
    sum1 = counter1 / 13
    sum2 = counter2 / 6
    cdde = (sum + sum1 + sum2)
    secret = (int(input("stat: ")) * 3) / 10
    total = (cdde + secret) / 4
    print("cd de: ", round(total, 2))


if position == "dm su" or position2 == "dm su" or position3 == "dm su":
    counter = counter1 = counter2 = 0
    for i in range(36):
        if i in range(12, 37) or i in (2, 4, 6, 9, 10):
            counter = counter + stat[i]
        if i in range(17, 20) or i in (4, 9, 10, 12, 14, 15, 24, 25, 27, 34, 35):
            counter1 = counter1 + stat[i]
        if i in (12, 15, 18, 24, 25):
            counter2 = counter2 + stat[i]
    sum = counter / 29
    sum1 = counter1 / 14
    sum2 = counter2 / 5
    dmsu = (sum + sum1 + sum2)
    secret = (int(input("stat: ")) * 3) / 10
    total = (dmsu + secret) / 4
    print("dm su: ", round(total, 2))


if position == "bwm de" or position2 == "bwm de" or position3 == "bwm de":
    counter = counter1 = counter2 = 0
    for i in range(36):
        if i in range(12, 37) or i in (2, 4, 6, 9, 10):
            counter = counter + stat[i]
        if i in range(17, 20) or i in (4, 9, 10, 12, 14, 15, 24, 25, 27, 34, 35):
            counter1 = counter1 + stat[i]
        if i in (12, 15, 18, 24, 25):
            counter2 = counter2 + stat[i]
    sum = counter / 29
    sum1 = counter1 / 14
    sum2 = counter2 / 5
    bwmde = (sum + sum1 + sum2)
    secret = (int(input("stat: ")) * 3) / 10
    total = (bwmde + secret) / 4
    print("bwm de: ", round(total, 2))


if position == "dlp su" or position2 == "dlp su" or position3 == "dlp su":
    counter = counter1 = counter2 = 0
    for i in range(36):
        if i in range(12, 37) or i in (2, 4, 6, 9, 10):
            counter = counter + stat[i]
        if i in range(23, 27) or i in (4, 10, 13, 15, 17, 19, 30):
            counter1 = counter1 + stat[i]
        if i in (4, 10, 13, 17, 19, 25, 26):
            counter2 = counter2 + stat[i]
    sum = counter / 29
    sum1 = counter1 / 11
    sum2 = counter2 / 7
    dlpsu = (sum + sum1 + sum2)
    secret = (int(input("stat: ")) * 3) / 10
    total = (dlpsu + secret) / 4
    print("dlp su: ", round(total, 2))


if position == "dlp de" or position2 == "dlp de" or position3 == "dlp de":
    counter = counter1 = counter2 = 0
    for i in range(36):
        if i in range(12, 37) or i in (2, 4, 6, 9, 10):
            counter = counter + stat[i]
        if i in range(24, 27) or i in (4, 10, 12, 13, 15, 17, 19, 30):
            counter1 = counter1 + stat[i]
        if i in (4, 10, 13, 17, 19, 25, 26):
            counter2 = counter2 + stat[i]
    sum = counter / 29
    sum1 = counter1 / 11
    sum2 = counter2 / 7
    dlpde = (sum + sum1 + sum2)
    secret = (int(input("stat: ")) * 3) / 10
    total = (dlpde + secret) / 4
    print("dlp de: ", round(total, 2))


if position == "bbm su" or position2 == "bbm su" or position3 == "bbm su":
    counter = counter1 = counter2 = 0
    for i in range(36):
        if i in range(12, 37) or i in (2, 3, 4, 6, 7, 9, 10):
            counter = counter + stat[i]
        if i in range(2, 5) or i in range(12, 16) or i in range(23, 26) or i in range(33, 36) or i in (7, 10, 17, 19, 27, 28, 30):
            counter1 = counter1 + stat[i]
        if i in (10, 12, 23, 25, 27, 34):
            counter2 = counter2 + stat[i]
    sum = counter / 31
    sum1 = counter1 / 20
    sum2 = counter2 / 6
    bbmsu = (sum + sum1 + sum2)
    secret = (int(input("stat: ")) * 3) / 10
    total = (bbmsu + secret) / 4
    print("bbm su: ", round(total, 2))


if position == "cm su" or position2 == "cm su" or position3 == "cm su":
    counter = counter1 = counter2 = 0
    for i in range(36):
        if i in range(12, 37) or i in (2, 3, 4, 6, 7, 9, 10):
            counter = counter + stat[i]
        if i in range(17, 20) or i in range(25, 28) or i in (4, 10, 12, 13, 15, 23, 34):
            counter1 = counter1 + stat[i]
        if i in (4, 10, 12, 19, 25):
            counter2 = counter2 + stat[i]
    sum = counter / 31
    sum1 = counter1 / 13
    sum2 = counter2 / 5
    cmsu = (sum + sum1 + sum2)
    secret = (int(input("stat: ")) * 3) / 10
    total = (cmsu + secret) / 4
    print("cm su: ", round(total, 2))


if position == "car" or position2 == "car" or position3 == "car":
    counter = counter1 = counter2 = 0
    for i in range(36):
        if i in range(12, 37) or i in (2, 3, 4, 6, 7, 9, 10):
            counter = counter + stat[i]
        if i in range(17, 20) or i in range(23, 28) or i in (4, 10, 12, 13, 15, 34):
            counter1 = counter1 + stat[i]
        if i in (4, 10, 12, 19, 24, 25, 34):
            counter2 = counter2 + stat[i]
    sum = counter / 31
    sum1 = counter1 / 14
    sum2 = counter2 / 7
    car = (sum + sum1 + sum2)
    secret = (int(input("stat: ")) * 3) / 10
    total = (car + secret) / 4
    print("car: ", round(total, 2))


if position == "mez at" or position2 == "mez at" or position3 == "mez at":
    counter = counter1 = counter2 = 0
    for i in range(36):
        if i in range(12, 37) or i in (2, 3, 4, 6, 7, 9, 10):
            counter = counter + stat[i]
        if i in range(2, 5) or i in range(26, 29) or i in (7, 10, 13, 15, 17, 19, 21, 23, 30, 34):
            counter1 = counter1 + stat[i]
        if i in (2, 10, 13, 19, 23, 26, 27, 28):
            counter2 = counter2 + stat[i]
    sum = counter / 31
    sum1 = counter1 / 16
    sum2 = counter2 / 8
    mezat = (sum + sum1 + sum2)
    secret = (int(input("stat: ")) * 3) / 10
    total = (mezat + secret) / 4
    print("mez at: ", round(total, 2))


if position == "mez su" or position2 == "mez su" or position3 == "mez su":
    counter = counter1 = counter2 = 0
    for i in range(36):
        if i in range(12, 37) or i in (2, 3, 4, 6, 7, 9, 10):
            counter = counter + stat[i]
        if i in range(26, 29) or i in (2, 4, 7, 10, 13, 15, 17, 19, 23, 30, 34):
            counter1 = counter1 + stat[i]
        if i in (10, 13, 19, 23, 27, 28):
            counter2 = counter2 + stat[i]
    sum = counter / 31
    sum1 = counter1 / 15
    sum2 = counter2 / 6
    mezsu = (sum + sum1 + sum2)
    secret = (int(input("stat: ")) * 3) / 10
    total = (mezsu + secret) / 4
    print("mez su: ", round(total, 2))


if position == "am at" or position2 == "am at" or position3 == "am at":
    counter = counter1 = counter2 = 0
    for i in range(36):
        if i in range(12, 37) or i in (2, 3, 4, 7, 10):
            counter = counter + stat[i]
        if i in range(2, 5) or i in (7, 10, 13, 15, 17, 19, 21, 23, 26, 29):
            counter1 = counter1 + stat[i]
        if i in (2, 4, 7, 10, 13, 15, 19, 21, 23):
            counter2 = counter2 + stat[i]
    sum = counter / 29
    sum1 = counter1 / 13
    sum2 = counter2 / 9
    amat = (sum + sum1 + sum2)
    secret = (int(input("stat: ")) * 3) / 10
    total = (amat + secret) / 4
    print("am at: ", round(total, 2))


if position == "iw at" or position2 == "iw at" or position3 == "iw at":
    counter = counter1 = counter2 = 0
    for i in range(36):
        if i in range(1, 5) or i in range(13, 37) or i in (7, 10):
            counter = counter + stat[i]
        if i in (1, 2, 4, 7, 10, 13, 15, 17, 19, 21, 23, 26, 28, 29, 33):
            counter1 = counter1 + stat[i]
        if i in (2, 10, 13, 23, 28, 29):
            counter2 = counter2 + stat[i]
    sum = counter / 29
    sum1 = counter1 / 15
    sum2 = counter2 / 6
    iwat = (sum + sum1 + sum2)
    secret = (int(input("stat: ")) * 3) / 10
    total = (iwat + secret) / 4
    print("iw at: ", round(total, 2))


if position == "if su" or position2 == "if su" or position3 == "if su":
    counter = counter1 = counter2 = 0
    for i in range(36):
        if i in range(1, 5) or i in range(13, 37) or i in (7, 10):
            counter = counter + stat[i]
        if i in range(2, 5) or i in range(28, 31) or i in (7, 10, 13, 15, 17, 21, 23, 26, 33):
            counter1 = counter1 + stat[i]
        if i in range(28, 31) or i in (2, 4, 10, 13, 23):
            counter2 = counter2 + stat[i]
    sum = counter / 29
    sum1 = counter1 / 15
    sum2 = counter2 / 8
    ifsu = (sum + sum1 + sum2)
    secret = (int(input("stat: ")) * 3) / 10
    total = (ifsu + secret) / 4
    print("if su: ", round(total, 2))


if position == "if at" or position2 == "if at" or position3 == "if at":
    counter = counter1 = counter2 = 0
    for i in range(36):
        if i in range(1, 5) or i in range(13, 37) or i in (7, 10):
            counter = counter + stat[i]
        if i in range(2, 5) or i in range(28, 31) or i in (7, 10, 13, 15, 17, 21, 23, 33):
            counter1 = counter1 + stat[i]
        if i in range(2, 5) or i in range(28, 31) or i in (13, 23):
            counter2 = counter2 + stat[i]
    sum = counter / 29
    sum1 = counter1 / 14
    sum2 = counter2 / 8
    ifat = (sum + sum1 + sum2)
    secret = (int(input("stat: ")) * 3) / 10
    total = (ifat + secret) / 4
    print("if at: ", round(total, 2))


if position == "af at" or position2 == "af at" or position3 == "af at":
    counter = counter1 = counter2 = 0
    for i in range(36):
        if i in range(2, 5) or i in range(13, 37) or i in (6, 7, 10):
            counter = counter + stat[i]
        if i in range(2, 5) or i in range(27, 31) or i in (10, 13, 15, 17, 19, 23, 33, 34):
            counter1 = counter1 + stat[i]
        if i in range(2, 5) or i in (13, 17, 23, 28):
            counter2 = counter2 + stat[i]
    sum = counter / 29
    sum1 = counter1 / 15
    sum2 = counter2 / 7
    afat = (sum + sum1 + sum2)
    secret = (int(input("stat: ")) * 3) / 10
    total = (afat + secret) / 4
    print("af at: ", round(total, 2))


if position == "pf at" or position2 == "pf at" or position3 == "pf at":
    counter = counter1 = counter2 = 0
    for i in range(36):
        if i in range(2, 5) or i in range(13, 37) or i in (6, 7, 10):
            counter = counter + stat[i]
        if i in range(14, 20) or i in range(27, 31) or i in range(33, 36) or i in (3, 4, 23, 25):
            counter1 = counter1 + stat[i]
        if i in range(14, 17) or i in (23, 25, 26, 27, 28, 33, 34):
            counter2 = counter2 + stat[i]
    sum = counter / 29
    sum1 = counter1 / 17
    sum2 = counter2 / 9
    pfat = (sum + sum1 + sum2)
    secret = (int(input("stat: ")) * 3) / 10
    total = (pfat + secret) / 4
    print("pf at: ", round(total, 2))

if position == "cf at" or position2 == "cf at" or position3 == "cf at":
    counter = counter1 = counter2 = 0
    for i in range(36):
        if i in range(2, 5) or i in range(13, 37) or i in (6, 7, 10):
            counter = counter + stat[i]
        if i in range(2, 5) or i in range(25, 32) or i in range(33, 36) or i in (6, 7, 10, 13, 15, 17, 19, 23):
            counter1 = counter1 + stat[i]
        if i in range(2, 5) or i in (6, 13, 15, 17, 23, 28, 29, 35):
            counter2 = counter2 + stat[i]
    sum = counter / 29
    sum1 = counter1 / 21
    sum2 = counter2 / 11
    cfat = (sum + sum1 + sum2)
    secret = (int(input("stat: ")) * 3) / 10
    total = (cfat + secret) / 4
    print("cf at: ", round(total, 2))


if position == "dlf su" or position2 == "dlf su" or position3 == "dlf su":
    counter = counter1 = counter2 = 0
    for i in range(36):
        if i in range(2, 5) or i in range(13, 37) or i in (6, 7, 10):
            counter = counter + stat[i]
        if i in (3, 4, 10, 13, 15, 17, 19, 21, 23, 24, 25, 29, 34):
            counter1 = counter1 + stat[i]
        if i in (4, 10, 13, 17, 19, 23, 24):
            counter2 = counter2 + stat[i]
    sum = counter / 29
    sum1 = counter1 / 13
    sum2 = counter2 / 7
    dlfsu = (sum + sum1 + sum2)
    secret = (int(input("stat: ")) * 3) / 10
    total = (dlfsu + secret) / 4
    print("dlf su: ", round(total, 2))

