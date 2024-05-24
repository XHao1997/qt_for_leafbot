from enum import Enum


class TASK(Enum):
    MOVE_SINGLE_JOINT = 1
    MOVE_ALL_JOINT = 2
    MOVE_ARM_EYE2HAND = 3
    MOVE_ARM_MOVE_RANDOM = 4
    MOVE_ARM_FOR_GRAP_LEAF = 5
    MOVE_JOINT1_NN = 6


class Msg:
    def __init__(self):
        self.task = None
        self.cmd = None
