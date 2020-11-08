import random



class EscapeRoom:
    def __init__(self):
        self.admin_channel = 774633121122484244
        self.team_channels = {
            'Team 1': {
                'channel_id': 774404823155474483,
                'status': 0,
                'current_tips': [],
                'total_tips': []},
            'Team 2': {
                'channel_id': 774607191105077258,
                'status': 0,
                'current_tips': [],
                'total_tips': 0
            },
            'Team 3': {
                'channel_id': 774607276559958026,
                'status': 0,
                'current_tips': [],
                'total_tips': 0
            }}
        self.keys = ['1', '2', '3']
        self.failwords = ['Nope', 'Probeer nog maar eens', 'Fout', 'Niet juist', '...']
        self.replies = ['Proficiat, dat was inderdaad de eerste code! Nu moeten jullie ...', 'Razendsnel! Jullie zijn weer al door een deur...', 'Huh? Het lijk wel of ik mijn opdrachten te makkelijk heb gemaakt!']
        self.tips = [['De eerste tip, het is de ||eerste|| opdracht!', 'Het is 1'],
                     ['De tweede opdracht...', 'Komop, je had de eerste'],
                     ['Wat? Nogsteeds tips nodig?', 'Bruh...']]

    def process(self, message):
        print(self.team_channels['Team 1'])
        for team, data in self.team_channels.items():
            if data['channel_id'] == message.channel.id:
                # Check if code is correct
                if message.content == '!help' or message.content == '!Help':
                    return False, 0, 0, self.help_menu(team, data)
                elif message.content == self.keys[data['status']]:
                    data['status'] = data['status'] + 1
                    self.add_points(team)
                    return True, data['status'] + 1, team, self.replies[data['status']]
                else:
                    return False, 0, 0, self.failwords[random.randint(0, len(self.failwords) - 1)]

    def add_points(self, team):
        #TODO: Een functie die de score berekent
        pass

    def help_menu(self, team, data):
        reply = 'Hey ' + team+', \nDit is wat ik zoal kan:'
        reply+= '\n`!help`: brengt je hier'
        reply+= '\n`!tip`: Ik bezorg je dan een tip, deze zullen wel meegerekend worden in de eindscore!'
        reply+= '\n\nJullie tips:\n'
        if len(data['current_tips'])>0:
            for tip in data['current_tips']:
                reply += tip + '\n'
        else:
            reply+='Jullie hebben deze ronde nog geen tips gebruikt!'
        reply+='In totaal hebben jullie '+str(data['total_tips'])+' tips gebruikt'
        return reply
