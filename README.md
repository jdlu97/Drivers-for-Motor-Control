# Drivers for Motor Control
 Source code and documentation of driver classes encapsulating the functionality of an encoder and a motor. A Pittman/Ametek 24V PM DC brush motor with a quadrature incremental encoder was used as well as an L6306 motor driver shield. The Nucleo STM32L476RG board was the microcontroller used in the project.
 
 ## Encoder Reading
 
 A common way to measure the movement of a motor is with an optical encoder. Because most encoders can send out signals at high frequency (sometimes up to 1MHz or so), we cannot read one with regular code; we need something faster such as interrupts or dedicated hardware.
 
 The STM32 processors have such hardware: timers which can read pulses from encoders and count distance and direction of motion. In this way, we are able to use the encoder to measure the motor's rotation as well as its speed.
 
 The encoder driver is a class that encapsulates the operation of the timer to read encoders. The class a constructor `__init__()` method which does the setup, given appropriate parameters such as pins and a timer. It also has `read()` and `zero()` methods which returns the current position and resets the position to zero, respectively.
  
 ## Motor Control
 
 The L6206 motor driver “shield”, a circuit board that can be attached atop the Nucleo, can be used to control two DC motors. It controls the torque produced by the motor and also its direction.
 
 An H-bridge motor driver has logic inputs to control which transistors in the bridge are turned on at any given time and to ensure that the two transistors in each half-bridge are never turned on at the same time, as this would short power to ground and let lots of smoke out.
 
 Just like with the encoder, a motor driver class was written. Its constructor `__init__()` sets up the pins to control the motor, and a method called `set_duty_cycle()` sets the duty cycle and direction of the motor power voltage.
 
 ## Testing
 
 The encoder class was tested by both turning the motor by hand and running the motor under power and printing the encoder position on the REPL. The code returned reasonable results when the motor was moved manually and by power. The encoder pulse rate was check with an oscilloscope and the count changed at the right number of counts per second.
 
 The motor driver class was tested by sending it a range of duty cycles, both positive and negative, and checking that the motor moved both ways. “Edge cases” such as the maximum and minimum possible duty cycles for proper operation was accounted for.