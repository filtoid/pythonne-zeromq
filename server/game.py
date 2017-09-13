from room import Room
from roomloading import load_start, load_south, load_west

class Game(object):
    def __init__(self, port):
        self.rooms = []
        self.rooms.append(load_start())
        self.rooms.append(load_south())
        self.rooms.append(load_west())
        self.user_objs = []
        self.cur_room = self.rooms[0]
        self.port = port

    def process_direction(self, dir):
        if dir == "N" or dir.lower()=="north":
            return "North"
        if dir == "E" or dir.lower()=="east":
            return "East"
        if dir == "W" or dir.lower()=="west":
            return "West"
        if dir == "S" or dir.lower()=="south":
            return "South"
        return None

    def process_request(self, msg):
        dir_list = ["North", "East", "South", "West", "N", "E", "S", "W", "south", "north", "east", "west"]

        if msg in self.cur_room.auto_responses:
            return self.cur_room.auto_responses[msg]

        verb = msg.split(" ")[0]
        if verb in self.cur_room.verbs:
            if verb == "pickup" or verb == "get":
                ret = self.cur_room.enact_verb(verb, msg.split(" ")[1:], self.user_objs)
                if len(ret.split(" ")) > 1:
                    return ret
                else:
                    self.user_objs.append(ret)
                    return "Picked up the {}".format(ret)
            else:
                ret = self.cur_room.enact_verb(verb, msg.split(" ")[1:], self.user_objs)
                if ret == None:
                    return "Unable to pickup the object"
                return ret

        elif verb == 'move':
            if len(msg.split(" "))<2:
                return "Can't move when no direction given"

            if msg.split(" ")[1] in dir_list:
                #Process the move
                dir = self.process_direction(msg.split(" ")[1])
                if dir == None:
                    return "Not a known direction ({})".format(msg.split(" ")[1])
                
                num = self.cur_room.process_move(dir)
                if num == None:\
                    return "Cannot move in that direction"
                self.cur_room = self.rooms[num]
                return "{}\n{}\n{}\n{}".format(self.cur_room.name, self.cur_room.desc, self.get_exits(), self.get_objects())

            else:
                return "Not a known direction ({})".format(msg.split(" ")[1])
        return "Unknown command {}".format(msg)

    def get_exits(self):
        return self.cur_room.get_exits()

    def get_objects(self):
        return self.cur_room.get_objects()