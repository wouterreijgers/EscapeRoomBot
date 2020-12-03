import datetime
import random
from time import time


class EscapeRoom:
    def __init__(self):
        self.admin_channel = 774633121122484244
        # Status -> O, niets open
        # 1, hagar open

        self.team_channels = {
            'Zeeroverslied': {
                'channel_id': 774404823155474483,
                'status': [],
                'current_tips': [],
                'tip_count': {'hagar': 0,
                              'biokot': 0,
                              'kp': 0,
                              'wc': 0,
                              'vatenkot': 0},
                'total_tips': 0,
                'duration': time(),
                'meme_count': 0,
                'final_score': 0,
            },
            'De Blauwvoet': {
                'channel_id': 774607191105077258,
                'status': [],
                'current_tips': [],
                'tip_count': {'hagar': 0,
                              'biokot': 0,
                              'kp': 0,
                              'wc': 0,
                              'vatenkot': 0},
                'total_tips': 0,
                'duration': time(),
                'meme_count': 0,
                'final_score': 0,

            },
            'Het zwartbruine bier': {
                'channel_id': 774607276559958026,
                'status': [],
                'current_tips': [],
                'tip_count': {'hagar': 0,
                              'biokot': 0,
                              'kp': 0,
                              'wc': 0,
                              'vatenkot': 0},
                'total_tips': 0,
                'duration': time(),
                'meme_count': 0,
                'final_score': 0,

            },
            'Het loze vissertje': {
                'channel_id': 783423234959343667,
                'status': [],
                'current_tips': [],
                'tip_count': {'hagar': 0,
                              'biokot': 0,
                              'kp': 0,
                              'wc': 0,
                              'vatenkot': 0},
                'total_tips': 0,
                'duration': time(),
                'meme_count': 0,
                'final_score': 0,

            },
            'Die Rietjie': {
                'channel_id': 783424010309599336,
                'status': [],
                'current_tips': [],
                'tip_count': {'hagar': 0,
                              'biokot': 0,
                              'kp': 0,
                              'wc': 0,
                              'vatenkot': 0},
                'total_tips': 0,
                'duration': time(),
                'meme_count': 0,
                'final_score': 0,

            },
            'My Bonnie': {
                'channel_id': 783424285774577674,
                'status': [],
                'current_tips': [],
                'tip_count': {'hagar': 0,
                              'biokot': 0,
                              'kp': 0,
                              'wc': 0,
                              'vatenkot': 0},
                'total_tips': 0,
                'duration': time(),
                'meme_count': 0,
                'final_score': 0,

            },
            'Loch Lomon': {
                'channel_id': 783424477093822494,
                'status': [],
                'current_tips': [],
                'tip_count': {'hagar': 0,
                              'biokot': 0,
                              'kp': 0,
                              'wc': 0,
                              'vatenkot': 0},
                'total_tips': 0,
                'duration': time(),
                'meme_count': 0,
                'final_score': 0,

            },
            'Clementine': {
                'channel_id': 783424702013636779,
                'status': [],
                'current_tips': [],
                'tip_count': {'hagar': 0,
                              'biokot': 0,
                              'kp': 0,
                              'wc': 0,
                              'vatenkot': 0},
                'total_tips': 0,
                'duration': time(),
                'meme_count': 0,
                'final_score': 0,

            },
            'Alouette': {
                'channel_id': 783427974786580553,
                'status': [],
                'current_tips': [],
                'tip_count': {'hagar': 0,
                              'biokot': 0,
                              'kp': 0,
                              'wc': 0,
                              'vatenkot': 0},
                'total_tips': 0,
                'duration': time(),
                'meme_count': 0,
                'final_score': 0,

            },
            'Juchheidi': {
                'channel_id': 783428086746185828,
                'status': [],
                'current_tips': [],
                'tip_count': {'hagar': 0,
                              'biokot': 0,
                              'kp': 0,
                              'wc': 0,
                              'vatenkot': 0},
                'total_tips': 0,
                'duration': time(),
                'meme_count': 0,
                'final_score': 0,

            },
            'Krambambouli': {
                'channel_id': 783428189108043786,
                'status': [],
                'current_tips': [],
                'tip_count': {'hagar': 0,
                              'biokot': 0,
                              'kp': 0,
                              'wc': 0,
                              'vatenkot': 0},
                'total_tips': 0,
                'duration': time(),
                'meme_count': 0,
                'final_score': 0,

            },
            'Pintjedrinken': {
                'channel_id': 783428322368815155,
                'status': [],
                'current_tips': [],
                'tip_count': {'hagar': 0,
                              'biokot': 0,
                              'kp': 0,
                              'wc': 0,
                              'vatenkot': 0},
                'total_tips': 0,
                'duration': time(),
                'meme_count': 0,
                'final_score': 0,

            },
            'Ein Prosit': {
                'channel_id': 783428445543596062,
                'status': [],
                'current_tips': [],
                'tip_count': {'hagar': 0,
                              'biokot': 0,
                              'kp': 0,
                              'wc': 0,
                              'vatenkot': 0},
                'total_tips': 0,
                'duration': time(),
                'meme_count': 0,
                'final_score': 0,

            },
            'Al boven door het vensterken': {
                'channel_id': 783428582448824344,
                'status': [],
                'current_tips': [],
                'tip_count': {'hagar': 0,
                              'biokot': 0,
                              'kp': 0,
                              'wc': 0,
                              'vatenkot': 0},
                'total_tips': 0,
                'duration': time(),
                'meme_count': 0,
                'final_score': 0,

            },
            'Het Kikkerlied': {
                'channel_id': 783428689307762728,
                'status': [],
                'current_tips': [],
                'tip_count': {'hagar': 0,
                              'biokot': 0,
                              'kp': 0,
                              'wc': 0,
                              'vatenkot': 0},
                'total_tips': 0,
                'duration': time(),
                'meme_count': 0,
                'final_score': 0,

            },
            'Sarie Marais': {
                'channel_id': 783428806937018398,
                'status': [],
                'current_tips': [],
                'tip_count': {'hagar': 0,
                              'biokot': 0,
                              'kp': 0,
                              'wc': 0,
                              'vatenkot': 0},
                'total_tips': 0,
                'duration': time(),
                'meme_count': 0,
                'final_score': 0,

            },
            'The wild rover': {
                'channel_id': 783429057752203294,
                'status': [],
                'current_tips': [],
                'tip_count': {'hagar': 0,
                              'biokot': 0,
                              'kp': 0,
                              'wc': 0,
                              'vatenkot': 0},
                'total_tips': 0,
                'duration': time(),
                'meme_count': 0,
                'final_score': 0,

            },
            'Uilenspiegel': {
                'channel_id': 783429162060349440,
                'status': [],
                'current_tips': [],
                'tip_count': {'hagar': 0,
                              'biokot': 0,
                              'kp': 0,
                              'wc': 0,
                              'vatenkot': 0},
                'total_tips': 0,
                'duration': time(),
                'meme_count': 0,
                'final_score': 0,

            },
            'When Johnny comes marching home': {
                'channel_id': 783429261847035984,
                'status': [],
                'current_tips': [],
                'tip_count': {'hagar': 0,
                              'biokot': 0,
                              'kp': 0,
                              'wc': 0,
                              'vatenkot': 0},
                'total_tips': 0,
                'duration': time(),
                'meme_count': 0,
                'final_score': 0,

            },
            'Der Pappenheimer': {
                'channel_id': 783429351584694282,
                'status': [],
                'current_tips': [],
                'tip_count': {'hagar': 0,
                              'biokot': 0,
                              'kp': 0,
                              'wc': 0,
                              'vatenkot': 0},
                'total_tips': 0,
                'duration': time(),
                'meme_count': 0,
                'final_score': 0,

            },
            'Annemarieken': {
                'channel_id': 784152092973596723,
                'status': [],
                'current_tips': [],
                'tip_count': {'hagar': 0,
                              'biokot': 0,
                              'kp': 0,
                              'wc': 0,
                              'vatenkot': 0},
                'total_tips': 0,
                'duration': time(),
                'meme_count': 0,
                'final_score': 0,

            },
            'De slag om het Gravensteen': {
                'channel_id': 784174195407585333,
                'status': [],
                'current_tips': [],
                'tip_count': {'hagar': 0,
                              'biokot': 0,
                              'kp': 0,
                              'wc': 0,
                              'vatenkot': 0},
                'total_tips': 0,
                'duration': time(),
                'meme_count': 0,
                'final_score': 0,

            },
            'Nummerlieke': {
                'channel_id': 784173911499735060,
                'status': [],
                'current_tips': [],
                'tip_count': {'hagar': 0,
                              'biokot': 0,
                              'kp': 0,
                              'wc': 0,
                              'vatenkot': 0},
                'total_tips': 0,
                'duration': time(),
                'meme_count': 0,
                'final_score': 0,

            },
        }
        self.keys = ['Yorben', 'Yorben Joosen', 'yorben', 'yorben joosen', 's', 'S', '2241',
                     'Yorben - Bas - Simon - Thomas - Siebe - Jaro - Wout', 'Yorben-Bas-Simon-Thomas-Siebe-Jaro-Wout',
                     'yorben - bas - simon - thomas - siebe - jaro - wout', 'yorben-bas-simon-thomas-siebe-jaro-wout']
        self.failwords = ['Nope',
                          'Probeer nog maar eens',
                          'Fout', 'Niet juist',
                          '...',
                          'Seriously?',
                          'omfg, zijn jullie zelfs aan het proberen?',
                          'Hoe komde daar zelfs op?',
                          'Heb je de opgaven wel gelezen?',
                          'Denken jullie eigenlijk na?',
                          'Aan dit tempo zijn jullie morgen nog bezig',
                          'Lies doet zelfs sneller een adje dan dat jullie dit raadsel oplossen',
                          'Zzzz, Maak je me nu wakker voor een fout antwoord?']
        self.replies = [
            'Proficiat, jullie hebben den Hagar opengekregen, maar we zijn hier nog niet klaar. Van hieruit zullen '
            'jullie de wc’s moeten vrijmaken en de deur naar de KP moet ook opengezet worden uiteraard. Misschien kan '
            'Emma Peeters jullie hier wel mee helpen.',
            'Amai, zalig jullie hebben het biokot geopend!',
            'Huh? Het lijk wel of ik mijn opdrachten te makkelijk heb gemaakt!',
            'De KP is nu ook geopend! Kei goed, van zodra het vatenkot ook open is dan kunnen we beginnen aan de '
            'cantus!']
        self.tips = \
            {'hagar': {
                0: 'hagar: Kijk eens op Strava',
                1: 'hagar: Vraag eens aan de bots “waar” ze wonen',
                2: 'hagar: Zoek aan de hand van de tips de persoon die even ver van de kop woont als Emma, '
                   'het antwoord is de naam van deze persoon!'},
                'biokot': {
                    0: 'biokot: Hebben jullie al eens geprobeerd op te zoeken waar deze codes voor staan?',
                    1: 'biokot: Een kaart met een route is altijd handig',
                    2: 'biokot: Kijk zeker naar de timing, de gevonden route vormt een letter.'},
                'kp': {
                    0: 'kp: Hebben jullie Emma haar facebook account al gezien',
                    1: 'kp: Zoek naar dingen die niet thuishoren op de fotos',
                    2: 'kp: Luister nog eens goed naar de voicemail'},
                'wc': {
                    0: 'wc: Hebben jullie de handleiding aandachtig genoeg gelezen?',
                    1: 'wc: Education, je zoekt hier naar c=... . Cloud, Kijk even goed wat er allemaal gebeurt! Geef '
                       'het wat tijd. Home, nul. Webshop, Probeer eens de hoodie te bestellen. Hier is nog een extra '
                       'tip, indien je vast zit in het doolhof kan je in de helpdesk `appelsien` sturen. Een '
                       'praesidium lid zal je dan verder helpen',
                    2: 'wc: De juiste cijfers zijn: 7 69 52 43. Zoek zelf maar uit welke A, B, C en D zijn'},
                'vatenkot': {
                    0: 'vatenkot: Simon of Thomas zit in het midden.',
                    1: 'vatenkot: Helemaal links zit Yorben en helemaal rechts zit Wout',
                    2: 'vatenkot: Yorben zit naast Bas en Jaro zit naast Wout'},
            }

        self.start_time = time()
        self.keys_kp = ['Cara', 'cara', 'CARA']

    def start(self):
        self.start_time = time()

    def process(self, message):
        for team, data in self.team_channels.items():
            print(team)
            if data['channel_id'] == message.channel.id:
                # Check if code is correct
                if message.content == '!help' or message.content == '!Help':
                    return False, 0, 0, self.help_menu(team, data), ''
                if '!tip' in message.content or '!Tip' in message.content:
                    return False, 0, 0, self.tip(team, data, message.content), ''
                elif message.content in self.keys or message.content in self.keys_kp:
                    # Juist geraden! Dit moet verwerkt worden.
                    print(self.keys[:4])
                    if message.content in self.keys[:4] and 'hagar' not in data['status']:
                        data['status'].append('hagar')
                        return True, data['status'], team, self.replies[0], 'hagar'
                    elif message.content in self.keys[5:6] and 'biokot' not in data['status']:
                        data['status'].append('biokot')
                        return True, data['status'], team, self.replies[1], 'biokot'
                    elif message.content in self.keys[6] and 'wc' not in data['status']:
                        data['status'].append('wc')
                        return True, data['status'], team, self.replies[2], 'wc'
                    elif message.content in self.keys_kp and 'kp' not in data['status']:
                        data['status'].append('kp')
                        return True, data['status'], team, self.replies[3], 'kp'
                    elif message.content in self.keys[2:] and 'vatenkot' not in data['status']:
                        if len(data['status']) != 4:
                            return False, 0, 0, 'Zorg er voor dat de wc en de kp open zijn!', ''
                        data['status'].append('vatenkot')
                        if len(data['status']) == 5:
                            return self.set_points(team, data)
                else:
                    return False, 0, 0, self.failwords[random.randint(0, len(self.failwords) - 1)], ''

    def set_points(self, team, data):
        reply = 'Proficiat team ' + team + ', \n'
        reply += 'Dankzij jullie zal onze cantus kunnen doorgaan!\n'
        data['duration'] = time() - self.start_time
        reply += 'In totaal deden jullie er ' + str(
            round(data['duration'] / 60)) + ' minuten over om alle opdrachten af te ronden!\n'
        if data['total_tips'] > 0:
            if data['total_tips'] == 1:
                reply += 'Helaas hebben jullie wel 1 tip gebruikt en zoals eerder gezegd zorgen tips voor een ' \
                         'straftijd... '
            else:
                reply += 'Helaas hebben jullie wel ' + str(
                    data['total_tips']) + ' tips gebruikt en zoals eerder gezegd zorgen ' \
                                          'tips voor een straftijd... '
            punishment = data['total_tips'] * 300
            reply += 'De totale straftijd die jullie krijgen is ' + str(
                punishment/60) + ' minuten, dit brengt jullie totaal op: '
            data['duration'] += float(punishment)
            reply += str(round(data['duration'] / 60)) + ' minuten.'
            reply += '\n*door afrondingen kan het zijn dat de som hierboven niet lijkt te kloppen. De uiteindelijke score wordt berekent tot op de microseconde!'
        reply += '\n\nNu is het even wachten totdat de anderen klaar zijn, van zodra het zover is kan ik de winnaar ' \
                 'aankondigen! Alvast bedankt om mee te spelen en indien je nog graag wat blijft napraten dan kan dat ' \
                 'uiteraard! '
        data['final_score'] = data['duration']
        return True, data['status'], team, reply, 'vatenkot'
        pass

    def help_menu(self, team, data):
        reply = 'Hey team ' + team + ', \nDit is wat ik zoal kan:'
        reply += '\n`!help`: brengt je hier'
        reply += '\n`!meme`: Geeft je een toffe meme zodat je even kan ontspannen, geen zorgen de bot ruimt alles mooi weer op!'
        reply += '\n`!tip [NAAM VAN EEN KAMER]`: Ik bezorg je dan een tip, deze zullen wel meegerekend worden in de eindscore!'
        reply += '\n`Als je een antwoord denkt te weten dan moet je het hier sturen, ik begrijp vast wel over welke deur je het hebt!'

        reply += '\n\nJullie tips:\n'
        if len(data['current_tips']) > 0:
            for tip in data['current_tips']:
                reply += tip + '\n'
        else:
            reply += 'Jullie hebben deze ronde nog geen tips gebruikt!'
        reply += '\nIn totaal hebben jullie ' + str(data['total_tips']) + ' tips gebruikt'
        return reply

    def tip(self, team, data, msg):
        comm = msg.split(' ')
        reply = 'Jullie willen dus een tip? dat kan!\n'
        reply += self.tips[comm[1]][data['tip_count'][comm[1]]]
        data['current_tips'].append(self.tips[comm[1]][data['tip_count'][comm[1]]])
        data['tip_count'][comm[1]] += 1
        data['total_tips'] += 1
        return reply

    def get_scores(self):
        reply = '```\nLive score bord'
        scores = []
        for team, data in self.team_channels.items():
            scores.append([data['status'], team, data['final_score']])
        # scores.sort(reverse=True)
        reply += '\n-----'
        for status, team, score in scores:
            temp = ''
            for i in range(32 - len(team)):
                temp += ' '
            reply += '\n' + team + ': ' + temp + 'status: ' + str(status) + '\tscore: ' + str(score) + '\n'
            for i in range(70):
                temp += '-'
        reply += '\n```'
        return reply

    def meme(self, message):
        for team, data in self.team_channels.items():
            if data['channel_id'] == message.channel.id:
                if data['meme_count'] == 12:
                    data['meme_count'] = 0
                data['meme_count'] += 1
                return data['meme_count']
