# https://www.codewars.com/kata/54acc128329e634e9a000362
#
#

class Automaton(object):

    def __init__(self):
        self.state = 'CLOSED'

    def _change_state(self, event):
        match (self.state, event):
            case ('CLOSED', 'APP_PASSIVE_OPEN'):
                self.state = 'LISTEN'
            case ('CLOSED', 'APP_ACTIVE_OPEN') | ('LISTEN', 'APP_SEND'):
                self.state = 'SYN_SENT'
            case ('LISTEN', 'RCV_SYN') | ('SYN_SENT', 'RCV_SYN'):
                self.state = 'SYN_RCVD'
            case ('SYN_RCVD', 'APP_CLOSE') | ('ESTABLISHED', 'APP_CLOSE'):
                self.state = 'FIN_WAIT_1'
            case ('SYN_RCVD', 'RCV_ACK') | ('SYN_SENT', 'RCV_SYN_ACK'):
                self.state = 'ESTABLISHED'
            case ('SYN_SENT', 'APP_CLOSE') | ('LAST_ACK', 'RCV_ACK') | \
                    ('TIME_WAIT', 'APP_TIMEOUT') | ('LISTEN', 'APP_CLOSE'):
                self.state = 'CLOSED'
            case ('ESTABLISHED', 'RCV_FIN'):
                self.state = 'CLOSE_WAIT'
            case ('FIN_WAIT_1', 'RCV_FIN'):
                self.state = 'CLOSING'
            case ('FIN_WAIT_1', 'RCV_FIN_ACK') | ('CLOSING', 'RCV_ACK') | \
                    ('FIN_WAIT_2', 'RCV_FIN'):
                self.state = 'TIME_WAIT'
            case ('FIN_WAIT_1', 'RCV_ACK'):
                self.state = 'FIN_WAIT_2'
            case ('CLOSE_WAIT', 'APP_CLOSE'):
                self.state = 'LAST_ACK'
            case _:
                self.state = 'ERROR'

    def read_events(self, events):
        for i in events:
            self._change_state(i)
        return self.state


def traverse_TCP_states(events):
    my = Automaton()
    print(events)
    return my.read_events(events)


# e = ["APP_PASSIVE_OPEN", "APP_SEND", "RCV_SYN_ACK"]
# e = ["APP_ACTIVE_OPEN", "RCV_SYN_ACK", "APP_CLOSE", "RCV_FIN_ACK", "RCV_ACK"]
e = ['APP_ACTIVE_OPEN', 'RCV_SYN_ACK', 'RCV_FIN', 'APP_CLOSE']
my = Automaton()
print(my.read_events(e))
