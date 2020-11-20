import datetime
import random
from time import time


class EscapeRoom:
    def __init__(self):
        self.admin_channel = 774633121122484244
        self.team_channels = {
            'Team 1': {
                'channel_id': 774404823155474483,
                'status': 0,
                'current_tips': [],
                'total_tips': 0,
                'duration': time()
            },
            'Team 2': {
                'channel_id': 774607191105077258,
                'status': 0,
                'current_tips': [],
                'total_tips': 0,
                'duration': time()
            },
            'Team 3': {
                'channel_id': 774607276559958026,
                'status': 0,
                'current_tips': [],
                'total_tips': 0,
                'duration': time()
            }}
        self.keys = ['1', '2', '3']
        self.failwords = ['Nope', 'Probeer nog maar eens', 'Fout', 'Niet juist', '...']
        self.replies = ['Proficiat, dat was inderdaad de eerste code! Nu moeten jullie ...',
                        'Razendsnel! Jullie zijn weer al door een deur...',
                        'Huh? Het lijk wel of ik mijn opdrachten te makkelijk heb gemaakt!']
        self.tips = [['De eerste tip, het is de ||eerste|| opdracht!', 'Het is 1'],
                     ['De tweede opdracht...', 'Komop, je had de eerste'],
                     ['Wat? Nogsteeds tips nodig?', 'Bruh...']]
        self.start_time = time()

    def start(self):
        self.start_time = time()

    def process(self, message):
        print(self.team_channels['Team 1'])
        for team, data in self.team_channels.items():
            if data['channel_id'] == message.channel.id:
                # Check if code is correct
                if message.content == '!help' or message.content == '!Help':
                    return False, 0, 0, self.help_menu(team, data)
                if message.content == '!tip' or message.content == '!Tip':
                    return False, 0, 0, self.tip(team, data)
                elif message.content == self.keys[data['status']]:
                    data['status'] = data['status'] + 1
                    if data['status'] == 3:
                        return self.set_points(team, data)
                    return True, data['status'] + 1, team, self.replies[data['status']]
                else:
                    return False, 0, 0, self.failwords[random.randint(0, len(self.failwords) - 1)]

    def set_points(self, team, data):
        reply = 'Proficiat ' + team + ', \n'
        reply += 'Dankzij jullie zal onze cantus kunnen doorgaan!\n'
        data['duration'] =  time() - self.start_time
        reply += 'In totaal deden jullie er ' + str(round(data['duration'])) + ' seconden over om alle opdrachten af te ronden!\n'
        if data['total_tips'] > 0:
            if data['total_tips'] == 1:
                reply += 'Helaas hebben jullie wel 1 tip gebruikt en zoals eerder gezegd zorgen tips voor een ' \
                         'straftijd... '
            else:
                reply += 'Helaas hebben jullie wel ' + str(
                    data['total_tips']) + ' tips gebruikt en zoals eerder gezegd zorgen ' \
                                          'tips voor een straftijd... '
            punishment = data['total_tips'] * 10
            reply += 'De totale straftijd die jullie krijgen is ' + str(
                punishment) + ' seconden, dit brengt jullie totaal op: '
            data['duration'] += float(punishment)
            reply += str(round(data['duration'])) +' seconden.'
            reply += '*door afrondingen kan het zijn dat de som hierboven niet lijkt te kloppen. De uiteindelijke score wordt berekent tot op de microseconde!'
        reply += '\n\nNu is het even wachten totdat de anderen klaar zijn, van zodra het zover is kan ik de winnaar ' \
                 'aankondigen! Alvast bedankt om mee te spelen en indien je nog graag wat blijft napraten dan kan dat ' \
                 'uiteraard! '
        return True, data['status'], team, reply
        pass

    def help_menu(self, team, data):
        reply = 'Hey ' + team + ', \nDit is wat ik zoal kan:'
        reply += '\n`!help`: brengt je hier'
        reply += '\n`!tip`: Ik bezorg je dan een tip, deze zullen wel meegerekend worden in de eindscore!'
        reply += '\n\nJullie tips:\n'
        if len(data['current_tips']) > 0:
            for tip in data['current_tips']:
                reply += tip + '\n'
        else:
            reply += 'Jullie hebben deze ronde nog geen tips gebruikt!'
        reply += '\nIn totaal hebben jullie ' + str(data['total_tips']) + ' tips gebruikt'
        return reply

    def tip(self, team, data):
        reply = 'Jullie willen dus een tip? dat kan!\n'
        reply += self.tips[int(data['status'])][len(data['current_tips'])]
        data['current_tips'].append(self.tips[int(data['status'])][len(data['current_tips'])])
        data['total_tips'] += 1
        return reply

    def get_scores(self):
        reply = 'Live score bord'
        scores = []
        for team, data in self.team_channels.items():
            scores.append([data['status'], team])
        scores.sort(reverse=True)
        reply += '\n-----'
        for status, team in scores:
            reply+= '\n'+team+': \tstatus: '+str(status)
        return reply
