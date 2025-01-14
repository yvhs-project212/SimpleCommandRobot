#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import wpilib
import wpimath.controller

import commands2
import commands2.button

from constants import OP, SW
import subsystems.motor_ss
from commands.motor_commands import MotorForward, MotorBackward, StopMotor, UpdateEncoder


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
        self.motor_ss = subsystems.motor_ss.MotorSubsystem()

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
        self.stick.leftBumper().onTrue(MotorForward(self.motor_ss))
        self.stick.rightBumper().onTrue(MotorBackward(self.motor_ss))
        self.stick.x().onTrue(StopMotor(self.motor_ss))
        self.stick.y().onTrue(UpdateEncoder(self.motor_ss))

    def getAutonomousCommand(self):
        return None
