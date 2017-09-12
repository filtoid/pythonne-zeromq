import zmq
import time
import sys

from game import Game



def process_request(msg, game):
    # global port
    # global game

    VERSION = "0.0.1"

    ret = ""
    if msg == "details":
        ret = "This server is running version {} on port {}".format(VERSION, game.port)
    elif msg == "examine":
        ret = "{}\n{}\n{}\n{}".format(game.cur_room.name, game.cur_room.desc, game.get_exits(), game.get_objects())
    else:
        ret = game.process_request(msg)
    return ret
            
if __name__ == "__main__":
    #Create new game instance
    game = Game("5556")

    #Set up the ZeroMQ 
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:{}".format(game.port))

    while True:
        #Message Pump - receive process and reply
        message = socket.recv()
        message = str(message.decode('utf-8'))
        print("Message received: {}".format(message))
        
        ret = process_request(message, game)
        time.sleep(0.5)
        socket.send(ret.encode('utf-8'))
