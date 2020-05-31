import time
import threading

def hello():
    print("hello, world")

t = threading.Timer(3.0, hello)
t.start()  # after 30 seconds, "hello, world" will be printed



# def countdown():
#     global timer
#
#     timer = 300
#
#     for i in range(300):
#         timer -= 1
#         time.sleep(1)
#         if cancel:
#             if timer - (timer // 60) * 60 < 10:
#                 print(f"Time left: {timer // 60}:0{timer - (timer // 60) * 60}")
#             else:
#                 print(f"Time left: {timer // 60}:{timer - (timer // 60) * 60}")
#             break
#
#
# def start_timer():
#     global timer
#     global cancel
#     cancel = False
#     countdown_thread = threading.Thread(target=countdown)
#     countdown_thread.start()
#     while timer > 0:
#         if input() == "y":
#             cancel = True
#
#
# start_timer()
