#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import logging
log = logging.Logger('P212-robot')

import wpilib
import commands2

from subsystems.music_ss import TalonFXMusicSubsystem
import constants


class NextSong(commands2.Command):
    """Command to load the next CHRP file"""
    def __init__(self, music_ss: TalonFXMusicSubsystem) -> None:
        """Constructor: sets instance variables, requires the subsystem."""
        super().__init__()
        self.music_ss = music_ss
        self.addRequirements(self.music_ss)

    def initialize(self):
        """Calls increment_song_id() to perform the entire command."""
        self.music_ss.increment_song_id()

    def isFinished(self):
        """Command is finished after initialize() runs!"""
        return True


class PreviousSong(commands2.Command):
    """Command to load the previous CHRP file"""
    def __init__(self, music_ss: TalonFXMusicSubsystem) -> None:
        """Constructor: sets instance variables, requires the subsystem."""
        super().__init__()
        self.music_ss = music_ss
        self.addRequirements(self.music_ss)

    def initialize(self):
        """Calls decrement_song_id() to perform the entire command."""
        self.music_ss.decrement_song_id()

    def isFinished(self):
        """Command is finished after initialize() runs!"""
        return True

class PlayMusic(commands2.Command):
    """Command to start playing the currently loaded song."""
    def __init__(self, music_ss: TalonFXMusicSubsystem) -> None:
        """Constructor: sets instance variables, requires the subsystem."""
        super().__init__()
        self.music_ss = music_ss
        self.addRequirements(self.music_ss)

    def initialize(self):
        """Calls play_song() to perform the entire command."""
        self.music_ss.play_song()

    def isFinished(self):
        """Command is finished after initialize() runs!"""
        return True


class PauseMusic(commands2.Command):
    """Command to pause the currently playing song."""
    def __init__(self, music_ss: TalonFXMusicSubsystem) -> None:
        """Constructor: sets instance variables, requires the subsystem."""
        super().__init__()
        self.music_ss = music_ss
        self.addRequirements(self.music_ss)

    def initialize(self):
        """Calls pause_song() to perform the entire command."""
        self.music_ss.pause_song()

    def isFinished(self):
        """Command is finished after initialize() runs!"""
        return True


class StopMusic(commands2.Command):
    """Command to stop playing the current song."""
    def __init__(self, music_ss: TalonFXMusicSubsystem) -> None:
        """Constructor: sets instance variables, requires the subsystem."""
        super().__init__()
        self.music_ss = music_ss
        self.addRequirements(self.music_ss)

    def initialize(self):
        """Calls stop_song() to perform the entire command."""
        self.music_ss.stop_song()

    def isFinished(self):
        """Command is finished after initialize() runs!"""
        return True

