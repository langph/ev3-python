# -*- coding: utf-8 -*-
import ev3, time
brick = ev3.connect_to_brick(address='10.0.1.1', port=9200)

#
# ev3_touch = ev3.EV3TouchSensor(brick, 1)
# nxt_touch = ev3.NXTTouchSensor(brick, 4)

# while True:
#     start = time.time()
#     ev3_touch.get_raw_data()
#     end = time.time() - start
#     print "took: ", end
# brick.close()

battery = brick.get_battery()
print battery.get_level()
print battery.get_message()
print battery.milli_voltage
time.sleep(20)

# print ev3_touch
# print ev3_touch.get_name()