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

    def activate(self):
        """Turn motor on at 20%"""
        self.motor.set(0.2)

    def stop(self):
        """Turn motor off"""
        self.motor.set(0.0)

    def encoder_value(self):
        """
        Example method that activates a subsystem actuator
        """
        return self.motor.get_rotor_position()

