# 发布者
import zmq
import time
 
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://127.0.0.1:5555")
 
# while True:
for i in range(10):
    news = "Breaking News! Time: {}".format(time.time())

    socket.send_string(news)
    time.sleep(1)