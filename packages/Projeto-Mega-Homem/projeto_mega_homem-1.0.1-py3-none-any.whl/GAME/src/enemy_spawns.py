from enemy import Blaster, Octopus, Big_eye


offset = 3
bw = 3 * 16
bh = 3 * 16


bl1_1 = Blaster(bw * 51 + offset, 5 * bh, False)
bl1_2 = Blaster(bw * 59 + offset, 8 * bh, False)

seg_1_en = [bl1_1, bl1_2]

bl2_1 = Blaster(bw * 61 + offset, -7 * bh, False)
bl2_2 = Blaster(bw * 57 + offset, -13 * bh, False)
bl2_3 = Blaster(bw * 55 + offset, -11 * bh, False)
bl2_4 = Blaster(bw * 55 + offset, -25 * bh, False)
bl2_5 = Blaster(bw * 52 - offset, -21 * bh, True)
bl2_6 = Blaster(bw * 59 + offset, -29 * bh, False)
bl2_7 = Blaster(bw * 55 - offset, -35 * bh, True)
bl2_8 = Blaster(bw * 59 + offset, -43 * bh, False)
bl2_9 = Blaster(bw * 57 + offset, -46 * bh, False)

seg_2_en = [
    bl1_1,
    bl1_2,
    bl2_1,
    bl2_2,
    bl2_3,
    bl2_4,
    bl2_5,
    bl2_6,
    bl2_7,
    bl2_8,
    bl2_9,
]

ob1_0 = Octopus(84 * bw, -54 * bh, True, True)
ob1_1 = Octopus(86 * bw, -59 * bh, True, True)
ob1_2 = Octopus(91 * bw, -56 * bh, False, False)
seg_3_en = [
    ob1_0,
    ob1_1,
    ob1_2,
]

ob2_0 = Octopus(85 * bw, -72 * bh, True, False)
ob2_1 = Octopus(87 * bw, -74 * bh, False, False)
ob2_2 = Octopus(93 * bw, -72 * bh, False, False)
ob2_3 = Octopus(84 * bw, -76 * bh, False, False)
ob2_4 = Octopus(88 * bw, -85 * bh, True, False)
ob2_5 = Octopus(87 * bw, -86 * bh, False, False)
ob2_6 = Octopus(91 * bw, -90 * bh, False, False)
ob2_7 = Octopus(93 * bw, -92 * bh, False, False)
ob2_8 = Octopus(83 * bw, -105 * bh, True, False)
ob2_9 = Octopus(83 * bw, -102 * bh, False, False)
ob2_10 = Octopus(82 * bw, -108 * bh, False, True)
ob2_11 = Octopus(88 * bw, -104 * bh, False, True)

seg_4_en = [
    ob1_0,
    ob1_1,
    ob1_2,
    ob2_0,
    ob2_1,
    ob2_2,
    ob2_3,
    ob2_4,
    ob2_5,
    ob2_6,
    ob2_7,
    ob2_8,
    ob2_9,
    ob2_10,
    ob2_11,
]


big_eye = Big_eye(134 * bw, -69 * bh)

seg_7_mid_boss = [big_eye]
spawn_bl = {"Cutman_Stage_Segment_1": seg_1_en, "Cutman_Stage_Segment_2": seg_2_en}

spawn_oc = {"Cutman_Stage_Segment_3": seg_3_en, "Cutman_Stage_Segment_4": seg_4_en}

spawn_ey = {"Cutman_Stage_Segment_7": seg_7_mid_boss}


def spawn_blasters(segment, enemies):
    for enemy in spawn_bl[segment]:
        if enemy.can_respawn:
            enemies.append(enemy)


def spawn_octopus(segment, enemies):
    for enemy in spawn_oc[segment]:
        if enemy.can_respawn:
            enemies.append(enemy)


def spawn_big_eye(segment, enemies):
    for enemy in spawn_ey[segment]:
        if enemy.can_respawn:
            enemies.append(enemy)
