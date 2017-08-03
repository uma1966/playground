# -*- coding: utf-8 -*-
"""cal.py module.

Project: garage.smartanalytics.sva
Created: 06/2017 - u.maurer@enbw.com

(c) Copyright EnBW AG 2017.
"""

import numpy as np
import datetime as dt

HOLIDAYS_GERMANY_BADEN_WUERTTEMBERG = [
# 2017
'2017-01-01',  # Neujahr
'2017-01-06',  # Heilige Drei Könige
'2017-04-14',  # Karfreitag
'2017-04-17',  # Ostermontag
'2017-05-01',  # Tag der Arbeit
'2017-05-25',  # Christi Himmelfahrt
'2017-06-05',  # Pfingstmontag
'2017-06-15',  # Fronleichnam
'2017-10-03',  # Tag der Deutschen Einheit
'2017-10-31',  # Reformationstag
'2017-11-01',  # Allerheiligen
'2017-12-25',  # 1. Weihnachtsfeiertag
'2017-12-26',  # 2. Weihnachtsfeiertag

# 2018
'2018-01-01',  # Neujahr
'2018-01-06',  # Heilige Drei Könige
'2018-03-30',  # Karfreitag
'2018-04-02',  # Ostermontag
'2018-05-01',  # Tag der Arbeit
'2018-05-10',  # Christi Himmelfahrt
'2018-05-21',  # Pfingstmontag
'2018-05-31',  # Fronleichnam
'2018-10-03',  # Tag der Deutschen Einheit
'2018-11-01',  # Allerheiligen
'2018-12-25',  # 1. Weihnachtsfeiertag
'2018-12-26',  # 2. Weihnachtsfeiertag

# 2019
'2019-01-01',  # Neujahr
'2019-01-06',  # Heilige Drei Könige
'2019-04-19',  # Karfreitag
'2019-04-22',  # Ostermontag
'2019-05-01',  # Tag der Arbeit
'2019-05-30',  # Christi Himmelfahrt
'2019-06-10',  # Pfingstmontag
'2019-06-20',  # Fronleichnam
'2019-10-03',  # Tag der Deutschen Einheit
'2019-11-01',  # Allerheiligen
'2019-12-25',  # 1. Weihnachtsfeiertag
'2019-12-26',  # 2. Weihnachtsfeiertag

# 2020
'2020-01-01',  # Neujahr
'2020-01-06',  # Heilige Drei Könige
'2020-04-10',  # Karfreitag
'2020-04-13',  # Ostermontag
'2020-05-01',  # Tag der Arbeit
'2020-05-21',  # Christi Himmelfahrt
'2020-06-01',  # Pfingstmontag
'2020-06-11',  # Fronleichnam
'2020-10-03',  # Tag der Deutschen Einheit
'2020-11-01',  # Allerheiligen
'2020-12-25',  # 1. Weihnachtsfeiertag
'2020-12-26',  # 2. Weihnachtsfeiertag
]
CALENDAR_WEEKMASK_GERMANY = 'Mon Tue Wed Thu Fri'

bdd = np.busdaycalendar(weekmask=CALENDAR_WEEKMASK_GERMANY, holidays=HOLIDAYS_GERMANY_BADEN_WUERTTEMBERG)
check = ['2017-01-01', '2017-05-01', '2017-08-31', '2017-12-25', '2017-12-26', '2017-12-31', '2019-02-04', '2018-08-31']

for day in check:
    d= np.datetime64(day)
    result = np.is_busday(d, busdaycal=bdd)
    print(day, result)

p = {
    'busday': {'on': dt.time(19, 0, 0), 'off': dt.time(8, 0, 0)},
    'holiday': {}
    }

check = [dt.datetime.now(), dt.datetime(2017,1,1,8,0,0), dt.datetime(2017,6,24,22,0,0),
         dt.datetime(2017,6,27,19,0,0), dt.datetime(2017,6,27,18,59,59), dt.datetime(2017,6,27,7,59,59),
         dt.datetime(2017, 6, 27, 8, 0, 0)]

for t in check:
    try:
        if np.is_busday(np.datetime64(t, 'D')):
            if t.time() >= p['busday']['on'] or t.time() < p['busday']['off']:
                print(t, 'ON')
            else:
                print(t, 'OFF')
        else:
            if t.time() >= p['holiday']['on'] or t.time() <= p['holiday']['off']:
                print(t, 'ON')
            else:
                print(t, 'OFF')
    except KeyError:
        print(t, 'ON')
