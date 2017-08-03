from sva import alarm

event = alarm.Event(alarm.EventType.VIDEO_MOTION, 'testdevice')
alarm.send_event_to_remote(event)

