# -*- coding: utf-8 -*-
"""sig.py module.

Project: garage.smartanalytics.sva
Created: 07/2017 - u.maurer@enbw.com

(c) Copyright EnBW AG 2017.
"""

import signal


def signal_handler(signo, stackframe):
    print('Signal {} received!'.format(signo))
    signal.signal(signo, signal.SIG_DFL)



if __name__ == '__main__':

    signal.signal(signal.SIGINT, signal_handler)
    print('Press <ctrl>+<c> to end.')
    signal.pause()
    print('This message should never be printed...')
