import wpilib
import commands2
from constants import ELEC
import phoenix6

class MotorSubsystem(commands2.Subsystem):
    """
    This class represents an example subsystem for your robot.  Edit it to
    model your actual subsystems.
    """
    def __init__(self) -> None:
        """Creates a new MotorSubsystem"""
        super().__init__()
        # Create sensors here, and assign them to instance variables.
        # (Define what DIO port your sensor uses in constants.py)
        self.motor = phoenix6.hardware.TalonFX(ELEC.motor_CAN_ID)

    def activate(self, rate):
        """Turn motor on at the given rate (-1.0 to 1.0)"""
        self.motor.set(rate)

    def stop(self):
        """Turn motor off"""
        self.motor.set(0.0)

    def encoder_value(self):
        """
        Example method that activates a subsystem actuator
        """
        status_signal = self.motor.get_rotor_position()
        return status_signal.value

