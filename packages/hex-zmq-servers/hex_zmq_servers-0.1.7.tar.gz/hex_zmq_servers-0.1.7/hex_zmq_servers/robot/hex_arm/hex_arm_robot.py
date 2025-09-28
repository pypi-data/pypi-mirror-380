#!/usr/bin/env python3
# -*- coding:utf-8 -*-
################################################################
# Copyright 2025 Dong Zhaorui. All rights reserved.
# Author: Dong Zhaorui 847235539@qq.com
# Date  : 2025-09-14
################################################################

import numpy as np
import time

from ..robot_base import HexRobotBase
from ...zmq_base import (
    MAX_SEQ_NUM,
    hex_zmq_ts_now,
    hex_zmq_ts_delta_ms,
    HexRate,
    HexSafeValue,
)
from hex_device import HexDeviceApi
from hex_device.motor_base import CommandType

ROBOT_CONFIG = {
    "device_ip": "172.18.8.161",
    "device_port": 8439,
    "control_hz": 250,
    "arm_type": 16,
    "mit_kp": [200.0, 200.0, 200.0, 75.0, 15.0, 15.0],
    "mit_kd": [12.5, 12.5, 12.5, 6.0, 0.31, 0.31],
    "sens_ts": True,
}


class HexHexArmRobot(HexRobotBase):

    def __init__(
        self,
        robot_config: dict = ROBOT_CONFIG,
    ):
        HexRobotBase.__init__(self)

        try:
            device_ip = robot_config["device_ip"]
            device_port = robot_config["device_port"]
            control_hz = robot_config["control_hz"]
            arm_type = robot_config["arm_type"]
            self.__sens_ts = robot_config["sens_ts"]
        except KeyError as ke:
            missing_key = ke.args[0]
            raise ValueError(
                f"robot_config is not valid, missing key: {missing_key}")

        self.__kp = np.array(
            robot_config.get(
                "mit_kp",
                [200.0, 200.0, 200.0, 75.0, 15.0, 15.0],
            ),
            dtype=np.float32,
        )
        self.__kd = np.array(
            robot_config.get(
                "mit_kd",
                [12.5, 12.5, 12.5, 6.0, 0.31, 0.31],
            ),
            dtype=np.float32,
        )

        # variables
        # hex_arm variables
        self.__hex_api = None
        self.__arm_archer = None

        # open device
        self.__hex_api = HexDeviceApi(
            ws_url=f"ws://{device_ip}:{device_port}",
            control_hz=control_hz,
        )
        while self.__hex_api.find_device_by_robot_type(arm_type) is None:
            print("\033[33mArm not found\033[0m")
            time.sleep(1)
        self.__arm_archer = self.__hex_api.find_device_by_robot_type(arm_type)
        self._dofs = len(self.__arm_archer)
        limits = np.array(self.__arm_archer.get_joint_limits())
        self._limits = np.ascontiguousarray(limits).reshape(self._dofs, 3, 2)

        # start work loop
        self._working.set()

    def work_loop(self, hex_values: list[HexSafeValue]):
        states_value = hex_values[0]
        cmds_value = hex_values[1]

        last_states_ts = hex_zmq_ts_now()
        states_count = 0
        last_cmds_seq = -1
        rate = HexRate(1000)
        while self._working.is_set():
            # states
            ts, states = self.__get_states()
            if states is not None:
                if hex_zmq_ts_delta_ms(ts, last_states_ts) > 1.0:
                    last_states_ts = ts
                    states_value.set((ts, states_count, states))
                    states_count = (states_count + 1) % MAX_SEQ_NUM

            # cmds
            cmds_pack = cmds_value.get(timeout_s=-1.0)
            if cmds_pack is not None:
                ts, seq, cmds = cmds_pack
                if seq > last_cmds_seq:
                    last_cmds_seq = seq
                    if hex_zmq_ts_delta_ms(hex_zmq_ts_now(), ts) < 200.0:
                        self.__set_cmds(cmds)

            # sleep
            rate.sleep()

    def __get_states(self) -> tuple[np.ndarray | None, dict | None]:
        if self.__arm_archer is None:
            return None, None

        # (n_dofs, 3) # pos vel eff
        states_dict = self.__arm_archer.get_simple_motor_status()
        pos = np.asarray(states_dict['pos'])
        vel = np.asarray(states_dict['vel'])
        eff = np.asarray(states_dict['eff'])
        ts = states_dict['ts']
        return ts if self.__sens_ts else hex_zmq_ts_now(), np.array(
            [pos, vel, eff]).T

    def __set_cmds(self, cmds: np.ndarray) -> bool:
        if self.__arm_archer is None:
            return False

        cmd_pos, cmd_tor = None, None
        if len(cmds.shape) == 1:
            cmd_pos = cmds
            cmd_tor = np.zeros(self._dofs)
        else:
            cmd_pos = cmds[:, 0]
            cmd_tor = cmds[:, 1]
        tar_pos = self._apply_pos_limits(
            cmd_pos,
            self._limits[:, 0, 0],
            self._limits[:, 0, 1],
        )

        mit_cmd = self.__arm_archer.construct_mit_command(
            tar_pos,
            np.zeros(self._dofs),
            cmd_tor,
            self.__kp,
            self.__kd,
        )
        self.__arm_archer.motor_command(CommandType.MIT, mit_cmd)

        return True

    def close(self):
        self.__hex_api.close()
