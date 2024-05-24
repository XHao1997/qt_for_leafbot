# 发布者
import zmq
import time
 
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://192.168.101.14:5555")

# while True:
for i in range(1000):
    news = "Breaking News! Time: {}".format(time.time())

    socket.send_string(news)
    time.sleep(1)