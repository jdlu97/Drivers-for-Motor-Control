# Drivers for Motor Control
 Source code for driver classes encapsulating the functionality of an encoder and a motor. A Pittman/Ametek 24V PM DC brush motor with a quadrature incremental encoder was used as well as an L6206 motor driver shield. The Nucleo STM32L476RG board was the microcontroller used in the project.
 
 ## Encoder Reading
 
 A common way to measure the movement of a motor is with an optical encoder. Because most encoders can send out signals at high frequency (sometimes up to 1MHz or so), we cannot read one with regular code; we need something faster such as interrupts or dedicated hardware.
 
 The STM32 processors have such hardware: timers that can read pulses from encoders and count distance and direction of motion. In this way, we are able to use the encoder to measure the motor's rotation as well as its speed.
 
 The encoder driver is a class that encapsulates the operation of the timer to read encoders. The class a constructor `__init__()` method which does the setup, given appropriate parameters such as pins and a timer. It also has the `read()` and `zero()` methods which returns the current position and resets the position to zero, respectively.
  
 ## Motor Control
 
 The L6206 motor driver shield, a circuit board that can be attached atop the Nucleo, can be used to control two DC motors. It controls the torque produced by the motor and also its direction.
 
 An H-bridge motor driver has logic inputs to control which transistors in the bridge are turned on at any given time and to ensure that the two transistors in each half-bridge are never turned on at the same time, as this would short power to ground and let lots of smoke out. An excerpt from the L6206 motor driver IC’s datasheet is shown below:

  <p align="center">
    <img src="https://github.com/jdlu97/Drivers-for-Motor-Control/blob/main/img/h_bridge_logic.png?raw=true" alt="H-Bridge-Logic"/>
 </p>

 One of the chip’s two H-bridges consists of the four N-channel FET’s in the right half of the diagram, with the motor connected to pins OUT1A and OUT2A. The microcontroller controls pins ENA, IN1A, and IN2A. A common way of using these pins is to set ENA high to enable the motor, set IN1A low, and send a PWM signal to IN2A to power the motor in one direction; reverse the signals to IN1A and IN2A to power the motor in the other direction.
 
 Just like with the encoder, a motor driver class was written. Its constructor `__init__()` sets up the pins to control the motor, and a method called `set_duty_cycle()` sets the duty cycle and direction of the motor power voltage.
 
 ## Testing
 
 The encoder class was tested by both turning the motor by hand and running the motor under power and printing the encoder position on the REPL. The code returned reasonable results when the motor was moved manually and by power. The encoder pulse rate was check with an oscilloscope and the count changed at the right number of counts per second.
 
 The motor driver class was tested by sending it a range of duty cycles, both positive and negative, and checking that the motor moved both ways. “Edge cases” such as the maximum and minimum possible duty cycles for proper operation was accounted for.