# -*- coding: utf-8 -*-
"""acknowledge.py module.

Project: garage.smartanalytics.sva
Created: 07/2017 - u.maurer@enbw.com

(c) Copyright EnBW AG 2017.
"""

import http.client

# conn = http.client.HTTPSConnection("10.67.0.26:38880")
conn = http.client.HTTPConnection("localhost:8000")

payload = '{ "event_id": "354b8bb1-5448-4d73-ad4f-be4a1c126494", "event_classified_as": "ALARM"}'

headers = {
    'authorization': "Basic bHlueDpMeW54NHN2YQ==",
    'content-type': "application/json",
    'cache-control': "no-cache",
    }

conn.request("PUT", "/events/acknowledge-event/", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))