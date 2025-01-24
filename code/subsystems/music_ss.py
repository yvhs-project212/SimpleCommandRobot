import logging
log = logging.getLogger('P212-robot')

from phoenix6.hardware import TalonFX
from phoenix6.orchestra import Orchestra

import commands2
from constants import ELEC


class TalonFXMusicSubsystem(commands2.Subsystem):
    """
    This class represents a set of TalonFX motor controllers that will be
    used to play music.
    """
    def __init__(self, chrp_filenames) -> None:
        """Creates a new TalonFXMusicSubsystem"""
        super().__init__()
        self.chrps = chrp_filenames
        if not chrp_filenames:
            raise ValueError(f"chrp_filenames had no content {chrp_filenames}")
        self.motors = []

        # ELEC may have many keys.  We're looking for the ones with names like
        # "motor_2_CAN_ID".
        for key in dir(ELEC):
            if key.startswith("motor") and key.endswith("CAN_ID"):
                can_id = getattr(ELEC, key)
                this_motor = TalonFX(can_id)
                self.motors.append(this_motor)
                log.info(f"Added motor with CAN ID {can_id}")
        if len(self.motors) == 0:
            raise ValueError("No motor_*_CAN_ID keys found in ELEC constants")

        self.orchestra = Orchestra()
        for motor in self.motors:
            self.orchestra.add_instrument(motor)
        self.set_song_id(0)

    def set_song_id(self, song_id):
        self.song_id = song_id
        if song_id >= len(self.chrps):
            raise ValueError(f"Can't play song ID {song_id} (song #{song_id+1}) -- only {len(self.chrps)} songs available")

        songfile = self.chrps[song_id]
        status = self.orchestra.load_music(songfile)
        log.info(f"Loaded {songfile}, status = {status}")

    def increment_song_id(self):
        new_song_id = (self.song_id + 1) % len(self.chrps)
        self.set_song_id(new_song_id)

    def decrement_song_id(self):
        new_song_id = (self.song_id - 1) % len(self.chrps)
        self.set_song_id(new_song_id)

    def play_song(self, song_id=0):
        """
        Play the current song.
        """
        log.info(f"Playing...")
        return self.orchestra.play()

    def pause_song(self):
        """
        Pause the currently playing song, if any
        """
        log.info(f"Pausing...")
        if self.orchestra.is_playing():
            return self.orchestra.pause()

    def stop_song(self):
        """
        Stop the currently playing song, if any
        """
        log.info(f"Stopping music...")
        if self.orchestra.is_playing():
            return self.orchestra.stop()
