# -*- coding: utf-8 -*-
import time
import ev3
import threading

print "starting"
time.sleep(1000)
# brick = ev3.connect_to_brick(address='10.0.1.1')
brick = ev3.connect_to_brick('00:16:53:3D:E4:77')

ultrasonic = ev3.EV3UltrasonicSensor(brick, 1)
distance = ultrasonic.get_selected_mode()
print "opened ultrasonic"

def time_that(iterations):
    time_taken = 0.0
    for _ in range(iterations + 1):
        start = time.time()
        sample = distance.fetch_sample()
        end = time.time()
        time_taken += end - start
        print (end - start, sample)

    print "time taken", time_taken
    print "avg time", time_taken / iterations

print "Starting timer"
time_that(100000)







# time.sleep(2)
# print "none in speed"
# motor.set_speed(0)
#
# time.sleep(2)
# print "setting up speed again"
# motor.set_speed(700)
# time.sleep(5)
# print "playing tune"
# # brick.beep()
# brick.buzz()

# def print_func(**kwargs):
#     print "Got a callback with args", kwargs
#
# sub = subscription.Subscription()
# brick.set_subscription(sub)
#
#
# # sub.subscribe_on_new_sensor(print_func)
# print "ev1"
# ev3_touch1 = ev3.EV3TouchSensor(brick, 1)  # should not raise an exception
# touch = ev3_touch1.get_touch_mode()
# print "first sensor connected"
# nxt_touch = ev3.NXTTouchSensor(brick, 4)
#
# sub.subscribe_on_samples_in_port(1, print_func)
# sub.subscribe_on_samples(print_func)
# # for _ in xrange(10000):
# #     if touch.is_pressed():
# #         print "YESSSSSSSS"
# #     time.sleep(0.1)
#
# print "second sensor connected"
# time.sleep(5)
# print "Complete"
#
# def INIT(engine):
#     print "??"

#
# # while True:
# #     start = time.time()
# #     ev3_touch.get_raw_data()
# #     end = time.time() - start
# #     print "took: ", end
# # brick.close()
#
# # battery = brick.get_battery()
# # print battery.get_level()
# # print battery.get_message()
# # print battery.milli_voltage
# # time.sleep(5)
#
# mode = ev3_touch1.get_touch_mode()
# print mode.is_pressed()
# ev3_touch1.set_cache_data([1])
# print mode.is_pressed() # should be true noe
# print ev3_touch1.get_name()
# class MyClass(object):
#     def __init__(self, i):
#         print i
#         print "never called in this case"
#
#     def __new__(cls, *args, **kwargs):
#         print "HAHAHA"
#         return super(MyClass, cls).__new__(cls)
#
#     def haha(self):
#         print "muhhahaha"
#
# obj = MyClass(1)
# print obj
# obj.haha()