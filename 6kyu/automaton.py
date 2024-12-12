# https://www.codewars.com/kata/5268acac0d3f019add000203
#
#

class Automaton(object):

    def __init__(self, commands):
        self.state = 'q1'
        self.read_commands(commands)

    def _change_state(self, command):
        match (self.state, command):
            case ('q1', '1') | ('q3', '1') | ('q3', '0'):
                self.state = 'q2'
            case ('q2', '0'):
                self.state = 'q3'

    def read_commands(self, commands):
        for i in commands:
            self._change_state(i)
        return self.state == 'q2'
        # Return True if we end in our accept state, False otherwise


commands = ["1", "0", "0", "1"]
my_automaton = Automaton(commands)
