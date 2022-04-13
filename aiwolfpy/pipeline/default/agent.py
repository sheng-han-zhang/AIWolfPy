import aiwolfpy

# content factory
cf = aiwolfpy.ContentFactory()


class Agent(object):

    def __init__(self):
        # my name
        self.base_info = dict()
        self.game_setting = dict()

    def getName(self):
        return self.my_name

    # new game (no return)
    def initialize(self, base_info, diff_data, game_setting):
        self.base_info = base_info
        self.game_setting = game_setting

    # new information (no return)
    def update(self, base_info, diff_data, request):
        self.base_info = base_info

    # Start of the day (no return)
    def dayStart(self):
        return None

    # conversation actions: require a properly formatted
    # protocol string as the return.
    def talk(self):
        return cf.over()

    def whisper(self):
        return cf.over()

    # targetted actions: Require the id of the target
    # agent as the return
    def vote(self):
        return self.base_info['agentIdx']

    def attack(self):
        return self.base_info['agentIdx']

    def divine(self):
        return self.base_info['agentIdx']

    def guard(self):
        return self.base_info['agentIdx']

    # Finish (no return)
    def finish(self):
        return None
