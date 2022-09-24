'''!    @file       motor_driver.py
        @brief      A driver for working with a DC motor.
        @details    Encapsulates functionality of DC motor in the form of a 
                    motor driver class. This class sets up pins to control the
                    motor and sets the duty cycle and direction of the motor. 

        @author     Juan Luna
        @author     Cade Liberty
        @author     Marcus Monroe

        @date       January 26, 2022
'''

import pyb
import utime

class MotorDriver:
    '''! @brief      A motor driver class for the L6206 motor driver.
         @details    Objects of this class can be used to instantiate motor
                     driver objects to control two DC motors.
    '''

    def __init__ (self, en_pin, in1_pin, in2_pin, timer):
        '''! @brief      Initializes objects of the MotorDriver class.
             @param  en_pin      Enable pin object.
             @param  in1_pin     Microcontroller control pin object "1".
             @param  in2_pin     Microcontroller control pin object "2".
             @param  timer       Motor timer object of specified frequency.
             @param  tim_ch1     Channel object "1" for motor timer.
             @param  tim_ch2     Channel object "2" for motor timer.
        '''
        # Enable pin object
        self.en_pin = en_pin
        # Set enable pin high
        self.en_pin.high()

        #  Define MCU control pins objects IN1 and IN2 that will directly 
        #  control output pins OUT1 and OUT2, connected to the motor.
        self.in1_pin = in1_pin
        self.in2_pin = in2_pin

        # Motor timer object for motor
        self.timer = timer
        
        # Motor timer channels configured in PWM mode (active high).
        self.tim_ch1 = self.timer.channel(1, mode = pyb.Timer.PWM, 
                                              pin = self.in1_pin)
        self.tim_ch2 = self.timer.channel(2, mode = pyb.Timer.PWM, 
                                              pin = self.in2_pin)

    def set_duty_cycle (self, duty):
        '''! @brief      Sets duty cycle as a pulse width percent for the motors.
             @details    Positive values represent rotation of the motor in one
                         direction (clockwise) and negative values in the
                         opposite direction (counterclockwise).

             @param  duty    Signed value of percent duty cycle of PWM signal.    
        '''

        print("Setting duty cycle to " + str(duty))
        
        # "Positive" duty cycle
        if (duty <= 100 and duty >= 0):
            self.tim_ch1.pulse_width_percent(abs(duty))
            self.tim_ch2.pulse_width_percent(0)

        # "Negative" duty cycle
        elif (duty > -100 and duty < 0):
            self.tim_ch1.pulse_width_percent(0)
            self.tim_ch2.pulse_width_percent(abs(duty))
        else:
            print("Enter valid percent duty cycle (0-100)...")

if __name__ == '__main__':
    # The following code tests the functionality of the motor driver.
    
    # Define enable pin objects
    ENA = pyb.Pin(pyb.Pin.cpu.A10, pyb.Pin.OUT_PP)
    ENB = pyb.Pin(pyb.Pin.cpu.C1, pyb.Pin.OUT_PP)

    # Define control pin objects associated with first motor.
    IN1A_pin = pyb.Pin.cpu.B4
    IN2A_pin = pyb.Pin.cpu.B5

    # Define control pin objects associated with second motor.
    IN1B_pin = pyb.Pin.cpu.A0
    IN2B_pin = pyb.Pin.cpu.A1

    # Define timer objects for motors with 20-kHz frequency.
    tim_MOT_A = pyb.Timer(3, freq = 20000)
    tim_MOT_B = pyb.Timer(5, freq = 20000)

    # Define motor driver objects for both motors
    motor_A = MotorDriver(ENA, IN1A_pin, IN2A_pin, tim_MOT_A)
    motor_B = MotorDriver(ENB, IN1B_pin, IN2B_pin, tim_MOT_B)
    
    # Test code
    while True:
        motor_A.set_duty_cycle(int(input('Enter duty cycle for Motor A: ')))
        motor_B.set_duty_cycle(int(input('Enter duty cycle for Motor B: ')))