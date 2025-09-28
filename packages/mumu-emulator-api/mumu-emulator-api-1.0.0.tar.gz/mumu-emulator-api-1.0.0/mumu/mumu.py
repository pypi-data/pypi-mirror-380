#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/7/28 下午9:36
# @Author : wlkjyy
# @File : mumu.py
# @Software: PyCharm
import os.path
from typing import Union

from mumu.api.adb.Adb import Adb
from mumu.api.core.Core import Core
from mumu.api.core.app import App
from mumu.api.core.performance import Performance
from mumu.api.core.power import Power
from mumu.api.core.shortcut import Shortcut
from mumu.api.core.simulation import Simulation
from mumu.api.core.window import Window
from mumu.api.develop.androidevent import AndroidEvent
from mumu.api.driver.Driver import Driver
import mumu.config as config
from mumu.api.network.Network import Network
from mumu.api.permission.Permission import Permission
from mumu.api.screen.gui import Gui
from mumu.api.screen.screen import Screen
from mumu.api.setting.setting import Setting
from mumu.utils import utils


class Mumu:
    __mumu_manager = r"D:\Program Files\Netease\MuMu Player 12\shell\MuMuManager.exe"

    __vm_index = None

    def __init__(self, mumu_manager_path=None):
        if mumu_manager_path is not None:
            # 后续创建的实例未设置时使用之前设置的路径
            if config.MUMU_PATH is None:
                self.__mumu_manager = mumu_manager_path
            else:
                self.__mumu_manager = config.MUMU_PATH

        if not os.path.exists(self.__mumu_manager):
            raise RuntimeError(f"MuMuManager.exe not found in {self.__mumu_manager}")

        base_path = os.path.dirname(self.__mumu_manager)

        config.MUMU_PATH = self.__mumu_manager
        config.ADB_PATH = os.path.join(base_path, "adb.exe")

    def select(self, vm_index: Union[int, list, tuple] = None, *args):
        """
            选择要操作的模拟器索引
        :param vm_index: 模拟器索引
        :param args: 更多的模拟器索引
        :return:

        Example:
            Mumu().select(1)
            Mumu().select(1, 2, 3)
            Mumu().select([1, 2, 3])
            Mumu().select((1, 2, 3))
        """

        if vm_index is None:
            self.__vm_index = 'all'
            return self

        if len(args) > 0:
            if isinstance(vm_index, int):
                vm_index = [vm_index]
            else:
                vm_index = list(vm_index)

            vm_index.extend(args)

        if isinstance(vm_index, int):
            self.__vm_index = str(vm_index)
        else:
            vm_index = list(set(vm_index))
            self.__vm_index = ",".join([str(i) for i in vm_index])

        return self

    def generate_utils(self) -> utils:
        return utils().set_vm_index(self.__vm_index).set_mumu_root_object(self)

    def all(self):
        """
            选择所有模拟器
        :return:
        """
        self.__vm_index = 'all'
        return self

    @property
    def core(self) -> Core:
        """
            模拟器类
        :return:
        """
        return Core(self.generate_utils())

    @property
    def driver(self) -> Driver:
        """
            驱动类

            已完成
        :return:
        """

        return Driver(self.generate_utils())

    @property
    def permission(self) -> Permission:
        """
            权限类

            已完成
        :return:
        """
        return Permission(self.generate_utils())

    @property
    def power(self):
        """
            电源类

            已完成
        :return:
        """
        return Power(self.generate_utils())

    @property
    def window(self) -> Window:
        """
            窗口类

            已完成
        :return:
        """

        return Window(self.generate_utils())

    @property
    def app(self) -> App:
        """
            app类

            已完成
        :return:
        """

        return App(self.generate_utils())

    @property
    def androidEvent(self) -> AndroidEvent:
        """
            安卓事件类

            已完成
        :return:
        """
        return AndroidEvent(self.generate_utils())

    @property
    def shortcut(self) -> Shortcut:
        """
            快捷方式类

            已完成
        :return:
        """
        return Shortcut(self.generate_utils())

    @property
    def simulation(self) -> Simulation:
        """
            机型类（这玩意很鸡肋，没什么用）

            已完成
        :return:
        """
        return Simulation(self.generate_utils())

    @property
    def setting(self) -> Setting:
        """
            配置类
        :return:
        """

        return Setting(self.generate_utils())

    @property
    def screen(self) -> Screen:
        """
            屏幕类
        :return:
        """
        return Screen(self.generate_utils())

    @property
    def performance(self) -> Performance:
        """
            性能类
        :return:
        """
        return Performance(self.generate_utils())

    @property
    def network(self):
        """
            网路操作类
        :return:
        """

        return Network(self.generate_utils())

    @property
    def adb(self) -> Adb:
        """
            ADB类
        :return:
        """
        return Adb(self.generate_utils())

    @property
    def auto(self) -> Gui:
        """
            GUI自动化类
        :return:
        """

        try:
            import cv2
        except ImportError:
            raise ImportError("if you want to use autoGui class, you should install opencv-python")

        return Gui(self.generate_utils())
