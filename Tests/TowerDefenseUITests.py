import unittest
from altunityrunner import *


class TowerDefenseUITest(unittest.TestCase):
    altdriver = None

    @classmethod
    def setUpClass(cls):
        cls.altdriver = AltUnityDriver() # start connection with AltUnity Server

    @classmethod
    def tearDownClass(cls):
        cls.altdriver.stop() # stop connection

    def test_open_pause_menu(self):
        self.altdriver.load_scene('MainMenu')

        self.altdriver.find_object(By.NAME, "Level Select").click()

        self.altdriver.find_object(By.NAME, "LevelSelectionButton(Clone)").click()

        self.altdriver.find_object(By.PATH, "//Game UI/PauseMenu/Button").click()

        pause_menu = self.altdriver.find_object(By.PATH, "//Game UI/PauseMenu/PauseMenu")

        canvas_enabled = pause_menu.get_component_property("UnityEngine.Canvas", "enabled")

        self.assertTrue(canvas_enabled, "pause menu not opened")

    def test_add_1000_energy(self):
        self.altdriver.load_scene('MainMenu')

        self.altdriver.find_object(By.NAME, "Level Select").click()

        self.altdriver.find_object(By.NAME, "LevelSelectionButton(Clone)").click()

        self.altdriver.find_object(By.NAME, "Debug Add Currency").click()

        energy = self.altdriver.find_object(By.PATH, "//Game UI/PlayerBaseLife/Panel/CurrencyContainer/CurrencyAmount").get_text()

        self.assertEqual("1010", energy, "energy not added")

    def test_open_build_info(self):
        self.altdriver.load_scene('MainMenu')

        self.altdriver.find_object(By.NAME, "Level Select").click()

        self.altdriver.find_object(By.NAME, "LevelSelectionButton(Clone)").click()

        self.altdriver.wait_for_object(By.PATH, "//Game UI/Build Menu/Sidebar/TowerBuildButton(Clone)/Button").click()

        build_info = self.altdriver.find_object(By.PATH, "//Game UI/Build Menu/BuildInfoMask/BuildInfo")

        canvas_enabled = build_info.get_component_property("UnityEngine.Canvas", "enabled")

        self.assertTrue(canvas_enabled, "build info not opened")

    def test_wave_started(self):
        self.altdriver.load_scene('MainMenu')

        self.altdriver.find_object(By.NAME, "Level Select").click()

        self.altdriver.find_object(By.NAME, "LevelSelectionButton(Clone)").click()

        self.altdriver.wait_for_object(By.NAME, "StartWaveButton").click()

        wave_info = self.altdriver.find_object(By.PATH, "//Game UI/WaveContainer")

        canvas_enabled = wave_info.get_component_property("UnityEngine.Canvas", "enabled")

        self.assertTrue(canvas_enabled, "wave info not opened")

        
