import time

import output


class Morse:
    MORSE = {
        'A': '·—',
        'B': '—···',
        'C': '—·—·',
        'D': '—··',
        'E': '·',
        'F': '··—·',
        'G': '——·',
        'H': '····',
        'I': '··',
        'J': '·———',
        'K': '—·—',
        'L': '·—··',
        'M': '——',
        'N': '—·',
        'O': '———',
        'P': '·——·',
        'Q': '——·—',
        'R': '·—·',
        'S': '···',
        'T': '—',
        'U': '··—',
        'V': '···—',
        'W': '·——',
        'X': '—··—',
        'Y': '—·——',
        'Z': '——··',
        '0': '—————',
        '1': '·————',
        '2': '··———',
        '3': '···——',
        '4': '····—',
        '5': '·····',
        '6': '—····',
        '7': '——···',
        '8': '———··',
        '9': '————·',
        '.': '·—·—·—',
        ',': '——··——',
        '?': '··——··',
        '!': '—·—·——',
        '-': '—····—',
        '/': '—··—·',
        ':': '———···',
        "'": '·————·',
        '—': '—····—',
        ')': '—·——·—',
        ';': '—·—·—',
        '(': '—·——·',
        '=': '—···—',
        '@': '·——·—·',
        '&': '·–···',
    }
    EXPAND_TOKEN = {'·': '1', '—': '111'}

    def __init__(self, outp: output.Output, freq: int):
        self.outp = outp
        self.freq = freq

    def get_morse(self, symbol):
        m = self.MORSE[symbol]
        return '0'.join(self.EXPAND_TOKEN[mm] for mm in m)

    def show(self, curr_t):
        value = '000'.join(self.get_morse(s) for s in curr_t) + '0000000'
        print(value)
        for v in value:
            if v == '1':
                self.outp.on()
            elif v == '0':
                self.outp.off()
            else:
                print(f'Incorrect value {v} found')
            self.outp.callback()
            time.sleep(1 / self.freq)
