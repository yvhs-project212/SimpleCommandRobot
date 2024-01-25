#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import wpilib
import commands2
import commands2.cmd
import wpimath.controller

from subsystems.emoji_ss import EmojiSubsystem

import constants


class RotateEmojisLeft(commands2.Command):
    """
    This imaginary robot has an "emoji subsystem" that displays different
    emojis.  A motor is used to rotate the display left (showing the previous
    emoji) or right (showing the next emoji).  Running the motor for exactly
    2.0 seconds shifts the display by one emoji.
    """
    def __init__(self, emoji_ss: EmojiSubsystem) -> None:
        """
        Constructor for the command object.  Assigns some instance variables.
        """
        super().__init__()
        self.emoji_ss = emoji_ss
        self.timer = wpilib.Timer()

    def initialize(self):
        """
        Perform any setup to initialize the command.
        This method runs when the scheduler schedules the command.
        """
        self.timer.start()

    def execute(self):
        """
        Performs the main bulk of the command.
        This method runs 50 times a second while the command is active.
        """
        self.emoji_ss.rotate_left()

    def isFinished(self):
        """
        Returns a boolean indicating whether the command has completed.
        """
        # stop the motor after 2 seconds
        return self.timer.get() >= 2.0

    def end(self, interrupted: bool):
        """
        Perform any cleanup or final steps needed after the command finishes.
        If you need to do something different depending on whether the command
        completed normally or was interrupted (by another command), the
        :interrupted: parameter will be True if the command was interrupted.
        """
        self.emoji_ss.stop()


class RotateEmojisRight(commands2.Command):
    """
    This imaginary robot has an "emoji subsystem" that displays different
    emojis.  A motor is used to rotate the display left (showing the previous
    emoji) or right (showing the next emoji).  Running the motor for exactly
    2.0 seconds shifts the display by one emoji.
    """
    def __init__(self, emoji_ss: EmojiSubsystem) -> None:
        """
        Constructor for the command object.  Assigns some instance variables.
        """
        super().__init__()
        self.emoji_ss = emoji_ss
        self.timer = wpilib.Timer()

    def initialize(self):
        """
        Perform any setup to initialize the command.
        This method runs when the scheduler schedules the command.
        """
        self.timer.start()

    def execute(self):
        """
        Performs the main bulk of the command.
        This method runs 50 times a second while the command is active.
        """
        self.emoji_ss.rotate_right()

    def isFinished(self):
        """
        Returns a boolean indicating whether the command has completed.
        """
        # stop the motor after 2 seconds
        return self.timer.get() >= 2.0

    def end(self, interrupted: bool):
        """
        Perform any cleanup or final steps needed after the command finishes.
        If you need to do something different depending on whether the command
        completed normally or was interrupted (by another command), the
        :interrupted: parameter will be True if the command was interrupted.
        """
        self.emoji_ss.stop()
