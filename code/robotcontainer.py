#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import logging
log = logging.Logger('P212-robot')

import wpilib
import commands2
import commands2.button

from constants import OP
from subsystems.music_ss import TalonFXMusicSubsystem
from commands.music_commands import (
    NextSong, PreviousSong, PlayMusic, PauseMusic, StopMusic)


class RobotContainer:
    """
    This class is where the bulk of the robot should be declared.  Since
    Command-based is a "declarative" paradigm, very little robot logic should
    actually be handled in the :class:`.Robot` periodic methods (other than
    the scheduler calls). Instead, the structure of the robot (including
    subsystems, commands, and button mappings) should be declared here.
    """

    def __init__(self):
        """
        The container for the robot. Contains subsystems, user controls,
        and commands.
        """
        # The robot's subsystems
        import os, os.path
        chrp_files_found = []
        for dirpath, dirnames, filenames in os.walk(os.path.dirname(__file__)):
            for filename in filenames:
                if not (filename.endswith(".chrp") or filename.endswith(".CHRP")):
                    continue
                chrp_files_found.append(f"{dirpath}/{filename}")
        log.info(f"CHRP files found: {chrp_files_found}")
        if not chrp_files_found:
            raise ValueError(f"No CHRP files found under {os.path.dirname(__file__)}")
        self.music_ss = TalonFXMusicSubsystem(chrp_files_found)

        # The driver's controller
        self.stick = commands2.button.CommandXboxController(OP.joystick_port)

        # Configure the button bindings
        self.configureButtonBindings()


    def configureButtonBindings(self):
        """
        Use this method to define your button->command mappings. Buttons can
        be created via the button factories on
        commands2.button.CommandGenericHID or one of its subclasses
        (commands2.button.CommandJoystick or
        command2.button.CommandXboxController).
        """
        # Load next song when the left bumper is pressed
        self.stick.leftBumper().onTrue(NextSong(self.music_ss))

        # Load previous song when the right bumper is pressed
        self.stick.rightBumper().onTrue(PreviousSong(self.music_ss))

        # Play the music when the A button is pressed
        self.stick.a().onTrue(PlayMusic(self.music_ss))

        # Pause the music when the Y button is pressed
        self.stick.y().onTrue(PauseMusic(self.music_ss))

        # Stop the music when the X button is pressed
        self.stick.x().onTrue(StopMusic(self.music_ss))

    def getAutonomousCommand(self):
        return None
