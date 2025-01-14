#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import wpilib
import commands2
import constants

from subsystems.motor_ss import MotorSubsystem

class MotorForward(commands2.Command):
    def __init__(self, motor_ss: MotorSubsystem):
        self.motor_ss = motor_ss

    def initialize(self):
        self.motor_ss.activate(constants.SW.motor_speed)

    def isFinished(self):
        return True


class MotorBackward(commands2.Command):
    def __init__(self, motor_ss: MotorSubsystem):
        self.motor_ss = motor_ss

    def initialize(self):
        self.motor_ss.activate(-1.0 * constants.SW.motor_speed)

    def isFinished(self):
        return True


class StopMotor(commands2.Command):
    def __init__(self, motor_ss: MotorSubsystem):
        self.motor_ss = motor_ss

    def initialize(self):
        self.motor_ss.stop()

    def isFinished(self):
        return True

class UpdateEncoder(commands2.Command):
    def __init__(self, motor_ss: MotorSubsystem):
        self.motor_ss = motor_ss

    def initialize(self):
        wpilib.SmartDashboard.putNumber("Encoder", self.motor_ss.encoder_value())

    def isFinished(self):
        return True
