"""Module for Screen Class"""
# coding: utf-8

import os


class Screen:
    """ Class used for display informations on screen"""

    def __init__(self):
        self.text = []

    def on_screen(self):
        """Print on screen self.text"""
        print("".join(self.text))

    def add_infos(self, infos):
        """Add text on self.text"""
        self.text.extend(infos)

    def info_users(self, info):
        """Add info for bad user keystroke"""
        self.text = [data for data in info]

    def warning(self, text):
        print(text)

    def clear(self):
        """Clear the screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
