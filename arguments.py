# -*- coding: utf-8 -*-
"""arguments.py module.

Project: garage.smartanalytics.sva
Created: 05/2017 - u.maurer@enbw.com

(c) Copyright EnBW AG 2017.
"""

import socket
import argparse

if __name__ == '__main__':
    hostname = socket.gethostname()
    parser = argparse.ArgumentParser(description='Install SVA on this system.')
    parser.add_argument('configs', metavar='config', nargs='*',
                        help='Name of config section(s) in ini file to choose; default is hostname.', default=[hostname])
    parser.add_argument('--quick', help='Quick install without building everything from scratch.',
                        action='store_true')
    args = parser.parse_args()

    print('Installing for environment', args.configs, '...')
