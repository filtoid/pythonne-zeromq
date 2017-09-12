import zmq
import time

if __name__ == "__main__":
    port = "5556"
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:{}".format(port))

    socket.send_string("details")
    #  Get the reply.
    message = socket.recv().decode('utf-8')
    print(message)

   