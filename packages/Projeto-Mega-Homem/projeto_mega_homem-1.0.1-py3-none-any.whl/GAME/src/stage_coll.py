import global_var
import copy
import list_coll
from list_coll import collisions, doors


class Stage_collisions:
    def __init__(self):
        self.floor_collisions = copy.deepcopy(list_coll.og_floor_col)
        self.stairs_collisions = copy.deepcopy(list_coll.og_stair_col)
        self.death_collisions = []
        self.selected_seg = "Cutman_Stage_Segment_1"
        self.og_f_coll = collisions[self.selected_seg][0]
        self.og_s_coll = collisions[self.selected_seg][1]
        self.og_death_coll = collisions[self.selected_seg][2]

    def update_coll_list(self):
        self.og_f_coll = collisions[self.selected_seg][0]
        self.og_s_coll = collisions[self.selected_seg][1]
        self.og_death_coll = collisions[self.selected_seg][2]
        self.floor_collisions = copy.deepcopy((self.og_f_coll))
        self.stairs_collisions = copy.deepcopy((self.og_s_coll))
        self.death_collisions = copy.deepcopy(self.og_death_coll)

    def update_coll(self):
        self.update_coll_list()
        cx = global_var.camera_x
        cy = global_var.camera_y
        for i in range(len(self.floor_collisions)):
            self.floor_collisions[i][0] = self.og_f_coll[i][0] - cx
            self.floor_collisions[i][1] = self.og_f_coll[i][1] - cy

    def update_stair_coll(self):
        cx = global_var.camera_x
        cy = global_var.camera_y
        for i in range(len(self.stairs_collisions)):
            self.stairs_collisions[i][0] = self.og_s_coll[i][0] - cx
            self.stairs_collisions[i][1] = self.og_s_coll[i][1] - cy

    def update_death_coll(self):
        cx = global_var.camera_x
        cy = global_var.camera_y
        for i in range(len(self.death_collisions)):
            self.death_collisions[i][0] = self.og_death_coll[i][0] - cx
            self.death_collisions[i][1] = self.og_death_coll[i][1] - cy

    def list_doors(self, segment):
        if segment >= "Cutman_Stage_Segment_7":
            return doors
        else:
            return []
