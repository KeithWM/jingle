import os
from subprocess import (run, PIPE)

from output import Output


class GpioPin:
    """
This is a horribly inefficient stand-in to use until I get a decent gpio access library working on
my orange pi one.
    """
    def __init__(self, num):
        self.num = num
        self.exported_name = '/sys/class/gpio/gpio%d' % num

    def export(self, s_direction=None, only_if_nec=True):
        if not (only_if_nec and os.path.exists(self.exported_name)):
            run('echo %d > /sys/class/gpio/export' % self.num, shell=True, stdout=PIPE)
        if s_direction:
            self.set_direction(s_direction)

    def set_direction(self, s_direction):
        run('echo %s > %s/direction' % (s_direction, self.exported_name), shell=True, stdout=PIPE)

    def get(self):
        cp = run("cat %s/value" % self.exported_name, shell=True, stdout=PIPE)
        return cp.stdout == b'1\n'

    def set(self, val):
        print('echo %d > %s/value' % (int(val), self.exported_name))
        run('echo %d > %s/value' % (int(val), self.exported_name), shell=True, stdout=PIPE)


class OptocouplerOutput(Output):
    def __init__(self, chunk, rate):
        super().__init__(chunk, rate)
        self.pinC4 = GpioPin(68)
        self.pinC7 = GpioPin(71)
        for pin in (self.pinC4, self.pinC7):
            pin.export('out')
        self.is_on = False

    def on(self):
        if not self.is_on:
            self.is_on = True
            self.pinC4.set(1)

    def off(self):
        if self.is_on:
            self.is_on = False
            self.pinC4.set(0)

    def callback(self):
        pass


if __name__ == "__main__":
    pass
