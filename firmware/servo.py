import machine
import time

class Servo:
    def __init__(self, pin, freq=50, min_us=500, max_us=2500, res=16):
        """
        Class for controlling servos via PWM.

        :param pin: Number of the GPIO pin connected to the servo.
        :param freq: PWM frequency in Hz (default 50 Hz for servos).
        :param min_us: Minimum pulse time in microseconds (default 500 µs).
        :param max_us: Maximum pulse time in microseconds (default 2500 µs).
        :param res: PWM resolution in bits (default 8 bits = 255 max).
        """
        self.pin_number = pin
        self.freq = freq
        self.min_duty = int((min_us / 20000) * (2 ** res - 1))
        self.max_duty = int((max_us / 20000) * (2 ** res - 1))
        self.range_bits = res

        # PWM initialization
        self.pwm = machine.PWM(machine.Pin(pin), freq=freq)
        self.current_duty = (self.min_duty + self.max_duty) // 2  # Środek zakresu

    def set_angle(self, angle):
        """
        Sets angle of servo
        :param angle: Angle in degrees (0-180)
        """
        if not 0 <= angle <= 360:
            raise ValueError("Angle has to be between 0-180 degrees. ")

        duty = int(self.min_duty + (self.max_duty - self.min_duty) * (angle/180))
        self.pwm.duty_u16(duty)

    def deinit(self):
        """
        Deinitialization of servo by turning off the PWM
        """
        self.pwm.deinit()