import global_var


def cam_vertical_move(pos_relativa_y):
    if pos_relativa_y < -85:
        global_var.camera_y -= 768
    elif pos_relativa_y > 760:
        global_var.camera_y += 768


def cam_move(
    segment,
    pos,
    speed_x,
    right,
):
    middle = 360
    pos_relativa_x = pos[0] - global_var.camera_x
    pos_relativa_y = pos[1] - global_var.camera_y

    if segment == "Cutman_Stage_Segment_1":
        if right and pos_relativa_x > middle and pos[0] < 2736:
            global_var.camera_x += speed_x
        elif not right and pos_relativa_x < middle:
            if pos[0] > 340:
                global_var.camera_x -= speed_x
            if global_var.camera_x < 0:
                global_var.camera_x = 0
    elif segment == "Cutman_Stage_Segment_2":
        cam_vertical_move(pos_relativa_y)

    elif segment == "Cutman_Stage_Segment_3":
        if right and pos_relativa_x > middle and pos[0] < 4244:
            global_var.camera_x += speed_x
        elif not right and pos_relativa_x < middle and pos[0] > 2700:
            global_var.camera_x -= speed_x
    elif segment == "Cutman_Stage_Segment_4":
        cam_vertical_move(pos_relativa_y)

    elif segment == "Cutman_Stage_Segment_5":
        if right and pos_relativa_x > middle and pos[0] < 5740:
            global_var.camera_x += speed_x
        if not right and pos_relativa_x < middle and pos[0] > 4204:
            global_var.camera_x -= speed_x
    elif segment == "Cutman_Stage_Segment_6":
        cam_vertical_move(pos_relativa_y)
    elif segment == "Cutman_Stage_Segment_7":
        if (
            right
            and pos_relativa_x > middle
            and pos[0] <= 6550 + 1028 * global_var.first_door_open
        ):
            global_var.camera_x += speed_x
        if not right and pos_relativa_x < middle and pos[0] >= 5736:
            global_var.camera_x -= speed_x
    elif segment == "Cutman_Stage_Segment_8":
        if (
            right
            and pos_relativa_x > middle
            and pos[0] < 8038 + 768 + 48 + 756 * global_var.second_door_open
        ):
            global_var.camera_x += speed_x
        if not right and pos_relativa_x < middle and 9167 > pos[0] >= 7277:
            global_var.camera_x -= speed_x
