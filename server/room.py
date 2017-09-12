class Room(object):

    def __init__(self):
        self.name = "Main Room"
        self.desc = "This room is sparkly"
        self.pickups = ['key']
        self.verbs = ['pickup']
        self.exits = []

    def is_verb_allowed(self, verb):
        if verb in self.verbs:
            return True 
        return False

    def enact_verb(self, verb, content):
        if verb == "pickup":
            if content == "key":
                return "Picked up the key"
            else:
                return "Cannot pickup the {}".format(content)
        else:
            return "Unable to process command {}".format(verb)

    def get_exits(self):
        if len(self.exits)==0:
            return "There are no exits"
        elif len(self.exits)==1:
            return "The only exit is to the {}".format(self.exits[0])
        else:
            ret = "There are exits to the "
            for e, k in self.exits:
                if k != len(self.exits)-1:
                    ret += e
                else:
                    ret += " and {}".format(e)
            return ret

            
