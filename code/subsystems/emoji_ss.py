import wpilib
import commands2
import rev
from constants import ELEC


class EmojiSubsystem(commands2.Subsystem):
    """
    This imaginary robot has an "emoji subsystem" that displays different
    emojis.  A motor is used to rotate the display left (showing the previous
    emoji) or right (showing the next emoji).

    This is intended as a very simple idea that resembles several real
    subsystems that use a single motor in forward or reverse.

    When writing code for a command-based robot, first create the subsystems
    (before writing the commands).  Subsystem methods should be provided to
    read any sensors, and to activate/deactivate any actuators.  Use the
    constants.py file to specify values such as motor CAN bus IDs or which
    RoboRIO port a sensor cable is plugged into.
    """
    def __init__(self) -> None:
        """Creates a new EmojiSubsystem"""
        super().__init__()
        self.motor = rev.CANSparkMax(
            ELEC.emoji_motor_CAN_ID, rev.CANSparkMax.MotorType.kBrushless)

    def rotate_left(self):
        """
        An example method that activates a subsystem actuator -- in this case,
        turning the motor left.
        """
        self.motor.set(-0.3)

    def rotate_right(self):
        """
        An example method that activates a subsystem actuator -- in this case,
        turning the motor right.
        """
        self.motor.set(0.3)

    def stop(self):
        """
        An example method that deactivates a subsystem actuator -- in this case,
        turning the motor off.
        """
        self.motor.set(0)
