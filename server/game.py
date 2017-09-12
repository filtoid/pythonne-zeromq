from room import Room

class Game(object):
    def __init__(self, port):
        self.cur_room = Room()
        self.port = port

    def process_request(self, msg):

        verb = msg.split(" ")[0]
        if verb in self.cur_room.verbs:
            return self.cur_room.enact_verb(verb, msg.split(" ")[1:])

        return "Unknown command {}".format(msg)
    