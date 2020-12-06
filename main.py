import asyncio
import random

import discord

from EscapeRoom import EscapeRoom
from utils import Utils

#Token that connects with the bot, goto discord developer and create credentials
TOKEN = 'SECRET CODE'

client = discord.Client()

alive = True
channels = []
team_channels = {
    'Zeeroverslied': {
        'channel_id': 774404823155474483,
        'role_id': 774611033137610772},
    'De Blauwvoet': {
        'channel_id': 774607191105077258,
        'role_id': 774611220274741282},
    'Het zwartbruine bier': {
        'channel_id': 774607276559958026,
        'role_id': 774611272327102464},
    'Het loze vissertje': {
        'channel_id': 783423234959343667,
        'role_id': 783421970683265065},
    'Die Rietjie': {
        'channel_id': 783424010309599336,
        'role_id': 783422443120754710},
    'My Bonnie': {
        'channel_id': 783424285774577674,
        'role_id': 783422798612922378},
    'Loch Lomon': {
        'channel_id': 783424477093822494,
        'role_id': 783422918452707378},
    'Clementine': {
        'channel_id': 783424702013636779,
        'role_id': 783422952552923147},
    'Alouette': {
        'channel_id': 783427974786580553,
        'role_id': 783426346528538684},
    'Juchheidi': {
        'channel_id': 783428086746185828,
        'role_id': 783426393740148748},
    'Krambambouli': {
        'channel_id': 783428189108043786,
        'role_id': 783426450996985867},
    'Pintjedrinken': {
        'channel_id': 783428322368815155,
        'role_id': 783426786604220417},
    'Ein Prosit': {
        'channel_id': 783428445543596062,
        'role_id': 783426836511326269},
    'Annemarieken': {
        'channel_id': 784152092973596723,
        'role_id': 784151819400118352},
    'Al boven door het vensterken': {
        'channel_id': 783428582448824344,
        'role_id': 783426870288973875},
    'Het Kikkerlied': {
        'channel_id': 783428689307762728,
        'role_id': 783426949904728104},
    'Sarie Marais': {
        'channel_id': 783428806937018398,
        'role_id': 783427001247465492},
    'The wild rover': {
        'channel_id': 783429057752203294,
        'role_id': 783427054767046666},
    'Uilenspiegel': {
        'channel_id': 783429162060349440,
        'role_id': 783427088367353937},
    'When Johnny comes marching home': {
        'channel_id': 783429261847035984,
        'role_id': 783427130800472114},
    'Der Pappenheimer': {
        'channel_id': 783429351584694282,
        'role_id': 783427212401049680},
    'De slag om het Gravensteen': {
        'channel_id': 784174195407585333,
        'role_id': 784173690195542077},
    'Nummerlieke': {
        'channel_id': 784173911499735060,
        'role_id': 784173784487165982},
}
different_rooms = {
    'kp': {
        'channel_id': 781912997173919811},
    'wc': {
        'channel_id': 781914127927869501},
    'hagar': {
        'channel_id': 781914322203836437},
    'biokot': {
        'channel_id': 781913952778977292},
    'vatenkot': {
        'channel_id': 781915161413943297},
    'bot_channel': {
        'channel_id': 781923356328984599}}

msg = ''
utils = None
escaperoom = None
playing = False
bully_lines = ['Euhm, team {{TEAM}} heeft al een opdracht afgerond',
               'Zijn jullie soms in slaap gevallen? Team {{TEAM}} heeft weer een deur geopend', 'Willen jullie soms dat team {{TEAM}} wint?']

memes = ['meme0.png', 'meme1.jpg', 'meme2.jpg', 'meme3.png', 'meme4.jpg', 'meme0.png', 'meme6.jpg', 'meme7.jpg', 'meme8.jpg', 'meme9.jpg', 'meme10.jpg', 'meme11.jpg', 'meme12.jpg']
user_names = []

@client.event
async def on_message(message):
    global msg, alive, team_channels, utils, escaperoom, playing, memes, user_names
    print(message)

    # This part is the 'emergency' part, sometimes the bot starts freaking out so by typing '!KILL' the bot stops sending messages.
    if message.content == '!Phoenix' and message.author.id == 650664861147332609:
        await message.channel.send('Rebooting...');
        alive = True
    if not alive:
        return None
    if message.content == '!KILL' and message.author.id == 650664861147332609:
        alive = False
        await message.channel.send('Ingenium bot was killed... ')
        return

    # Make sure the bot doesn't replies to other bots
    if message.author == client.user or message.author.bot:
        return
    # Admin functies
    if message.channel.id == 705172201472524300:  # is id van 'send-to-all' channel
        msg = message.content.lower().replace(" ", '')
        if not message.author in user_names:
            for team, role in team_channels.items():
                team_name = team.lower().replace(" ", '')
                #print(team_name)
                if team_name in msg:
                    # TODO: zorgen dat iedereen max1 rol krijgt
                    role = message.author.guild.get_role(role['role_id'])
                    await message.author.add_roles(role)
                    role = message.author.guild.get_role(781913353944563732)
                    await message.author.add_roles(role)
                    user_names.append(message.author)

        msg = await message.channel.history(limit=1).flatten()
        await message.channel.delete_messages(msg)


    # Algemene functies die altijd werken
    if not playing or message.channel.id == 774633121122484244:
        if message.content == '!help' or message.content == '!Help':
            await message.channel.send(utils.help_menu(message.channel.id, message))
            return

    # Admin functies
    if message.channel.id == 774633121122484244: # is id van 'send-to-all' channel
        print(message)
        if message.content == '!send' or message.content == '!Send':
            for team, data in team_channels.items():
                channel = client.get_channel(data['channel_id'])
                if '{{TEAM_NAME}}' in msg:
                    split = msg.split('{{TEAM_NAME}}')
                    await channel.send(split[0] + team + split[1])
                else:
                    await channel.send(msg)
        if message.content == '!scores' or message.content == '!scores':
            await message.channel.send(escaperoom.get_scores())
        elif message.content == '!roles' or message.content == '!Roles':
            channel = client.get_channel(705172201472524300)
            await channel.send(file=discord.File('logo.png'))
            await channel.send('Normaal gezien hebben jullie via mail een geheime code gekregen, stuur deze code hieronder en dan weet ik meteen waar ik je naartoe kan brengen! Indien er een probleem is stuur dan even een berichtje in de helpdesk.  Alvast veel succes!!!\n\n(ps: Je kan maar 1 keer sturen dus zorg dat je het juiste liedje ingeeft)')
            # m = channel.last_message
            # emoji = '1️⃣'
            # await m.add_reaction(emoji)
            # emoji = '2️⃣'
            # await m.add_reaction(emoji)
            # emoji = '3️⃣'
            # await m.add_reaction(emoji)
        elif message.content == '!Welkom' or message.content == '!welkom':
            for team, data in team_channels.items():
                channel = client.get_channel(data['channel_id'])
                await channel.send('Hey team ' + team + ', \nWelkom bij de Ingenium Escape Room, ik heb zojuist het '
                                                   'signaal gekregen dat ik de gasten mag welkom heten en het spel mag uitleggen! '
                                                   ':partying_face:\n\nBij deze, Welkom allemaal! De escaperoom deze avond zal '
                                                   'volledig gehost worden door mij. De geweldige mensen van Ingenium staan uiteraard '
                                                   'klaar om in te grijpen maar dat is hopelijk niet nodig. Straks begin ik met de '
                                                   'eerte opdracht uit te leggen. Indien jullie een antwoord denken te weten dan mag '
                                                   'je dat hier onder typen en zal ik feedback geven. Je kan ook tips vragen maar '
                                                   'hier hangt uiteraard een straftijd aan vast. Een tip vragen kan je doen door `!tip [KAMER NAAM]` '
                                                   'te typen. Het is belangrijk om te weten dat alle bots mee doen!\n\nOhja, als er iets onduidelijk is van zodra het spel gestart is kan je altijd `!help` typen, '
                                                   'ik vat dan even mijn functies. Owja, nog iets belangrijk! Iedereen kan maar 1 bericht per 10 seconden sturen dus gokken heeft geen zin! :stuck_out_tongue: \n\nVeel succes!\n\n(Het startsignaal word zometeen '
                                                   'gegeven)')


        elif message.content == '!Start' or message.content == '!start':
            for team, data in team_channels.items():
                channel = client.get_channel(data['channel_id'])
                await channel.send('\nWelkom beste speurders, \nBij Ingenium '
                                   'willen we deze avond graag een cantus geven maar helaas zijn alle deuren van de '
                                   'KP en de Hagar nog op slot... \nEnkel dankzij jullie kunnen we (hopelijk) zo snel '
                                   'mogelijk beginnen aan de cantus. Zoals jullie kunnen zien zijn er enkele kanalen '
                                   'zichtbaar geworden, hier verschijnen jullie opdrachten. Waneer je een antwoord '
                                   'hebt gevonden dan stuur je dat hier! Iedere kamer heeft 1 opdracht, van zodra je '
                                   'deze kamer geopend hebt kan je die ruimte vergeten '
                                   '\n\nVeel succes!')
            channel = client.get_channel(different_rooms['wc']['channel_id'])
            await channel.send('\nEr hangt een cijferslot aan de deur naar de wc’s. De kans is groot dat een zatte '
                               'WINAKker dat daar voor de lol heeft gehangen, net zoals er nog steeds een '
                               'Ingeniumsticker '
                               'ergens in de wc’s van de Hagar plakt. Om het slot te openen hebben jullie een code '
                               'nodig van vier cijfers. Wat een geluk dat deze zatte plezante ook nog het volgende op '
                               'de deur heeft geschreven: a+bc-d². Waarschijnlijk dacht deze persoon dat hij of zij '
                               'de code de volgende ochtend niet meer zou weten. \n\nMeer info heb ik helaas ook '
                               'niet, ik heb wel de handleiding van het slot online gevonden: '
                               'https://drive.google.com/file/d/1aJo8IB7e88vt2iflM2DNtFOqjGma1xxr/view?usp=sharing ')
            channel = client.get_channel(different_rooms['biokot']['channel_id'])
            await channel.send('\n5C46+98    :10u Bloed geven'
                               '\n5CPP+Q8    :16u Engineers of Tomorrow vergadering'
                               '\n59CV+8R    :12u30 Pizza’s bestellen'
                               '\n4FV8+R4    :8u30 Kaaskroketten ophalen'
                               '\n59FW+XF    :13u snacks, prijzen voor bingo'
                               '\n4CJV+MP    :8u Micro ophalen'
                               '\n5CQG+33    :15u Pintje om ons stamcafé te steunen'
                               '\n5C84+XF    :11u Bak-voorbereiding'
                               '\n5CMC+J5    :14u Middageten'
                               '\n4FXM+P3    :9u Ingenium-emmers ophalen')
            channel = client.get_channel(different_rooms['bot_channel']['channel_id'])
            await channel.send('bot emma '+str(different_rooms['kp']['channel_id'])+' kp')
            channel = client.get_channel(different_rooms['hagar']['channel_id'])
            await channel.send('\nKennen jullie Emma al? Ze is ons nieuwste praesidium lid en zal ons helpen '
                               'vanavond. Net zoals de meesten komt ook Emma met fiets naar de KP. Soms doet ze al '
                               'eens een wedstrijdje “om ter snelste thuis” met de bot die even ver moet als '
                               'zij. Op de kaart staan de woonplaatsen van onze bots aangeduid! \n\n ps: je kan de '
                               'bots in privé sturen, als je de juiste vragen stelt zullen ze antwoorden!')
            await channel.send(file=discord.File('map.png'))
            channel = client.get_channel(different_rooms['vatenkot']['channel_id'])
            await channel.send('\nDe cantus kan bijna starten, alleen moet iedereen nog even gaan zitten! Geef de '
                               'volgorde als volgt door: persoon-persoon-persoon want anders snap ik er niets van')
            escaperoom.start()
            playing = True
        elif message.content == '!Stop' or message.content == '!stop':
            for team, data in team_channels.items():
                channel = client.get_channel(data['channel_id'])
                await channel.send('\nHet spel is even stilgelegd wegens technische problemen...')
            playing = False
        elif message.content == '!Clear' or message.content == '!clear':
            for team, data in team_channels.items():
                channel = client.get_channel(data['channel_id'])
                messages = await channel.history(limit=1000).flatten()
                await channel.delete_messages(messages)
            for team, data in different_rooms.items():
                channel = client.get_channel(data['channel_id'])
                messages = await channel.history().flatten()
                await channel.delete_messages(messages)
        else:
            msg = message.content
            await message.channel.send(msg)
            await message.channel.send('\nAls je dit bericht wil verzenden typ dan `!send`')
    if playing:
        # (Is the answer correct?, In what phase of the game are they now?, did they answer correctly?)
        if message.content == '!meme' or message.content == '!Meme':
            meme = escaperoom.meme(message)
            await message.channel.send(file=discord.File(memes[meme]))
            await asyncio.sleep(4)
            msg = await message.channel.history(limit=2).flatten()
            await message.channel.delete_messages(msg)
            return
        correct, new_status, team_win, response, door_opened = escaperoom.process(message)
        print(correct, new_status, team_win, response, door_opened)
        await message.channel.send(response)
        if correct:
            if 'hagar' == door_opened:
                role = message.author.guild.get_role(781966223105720331)
                print(message.author.voice.channel.members)
                for member in message.author.voice.channel.members:
                    print(member)
                    await member.add_roles(role)
                channel = client.get_channel(different_rooms['bot_channel']['channel_id'])
                await channel.send('bot ' + str(message.channel.id) + ' conv_hagar')
            if 'biokot' == door_opened:
                channel = client.get_channel(different_rooms['bot_channel']['channel_id'])
                await channel.send('bot ' + str(message.channel.id) + ' conv_biokot')
            if 'wc' in new_status and 'kp' in new_status and 'vatenkot' not in new_status:
                role = message.author.guild.get_role(781989687023763457)
                if message.author.voice:
                    for member in message.author.voice.channel.members:
                        await member.add_roles(role)
                channel = client.get_channel(different_rooms['bot_channel']['channel_id'])
                await channel.send('bot ' + str(message.channel.id) + ' conv_all')
            if 'kp' == door_opened and 'wc' not in new_status:
                channel = client.get_channel(different_rooms['bot_channel']['channel_id'])
                await channel.send('bot ' + str(message.channel.id) + ' conv_wc')
            if 'wc' == door_opened and 'kp' not in new_status:
                channel = client.get_channel(different_rooms['bot_channel']['channel_id'])
                await channel.send('bot ' + str(message.channel.id) + ' conv_wc')
            if 'vatenkot' == door_opened:
                role = message.author.guild.get_role(784144194330689556)
                if message.author.voice:
                    for member in message.author.voice.channel.members:
                        await member.add_roles(role)
            parts = bully_lines[random.randint(0, len(bully_lines) - 1)].split('{{TEAM}}')
            tekst = parts[0] + team_win + parts[1]
            for team, data in team_channels.items():
                if not team_win == team:
                    channel = client.get_channel(data['channel_id'])
                    await channel.send(tekst)


@client.event
async def on_reaction_add(reaction, user):
    # Asign roles
    if user == client.user:
        return
    print(str(reaction.emoji))
    role = user.guild.get_role(781913353944563732)
    await user.add_roles(role)
    if reaction.emoji == '1️⃣':
        print('team1 ', user.guild)
        role = user.guild.get_role(774611033137610772)
        print(role)
        await user.add_roles(role)
    if reaction.emoji == '2️⃣':
        role = user.guild.get_role(774611220274741282)
        await user.add_roles(role)
    if reaction.emoji == '3️⃣':
        role = user.guild.get_role(774611272327102464)
        await user.add_roles(role)


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        'Hey ' + member.name + ',\nIk ben de Ingenium bot en zal jouw doorheen het spel leiden. '
                               'Voorlopig moet je alleen zorgen dat je weet in welk team je zit. '
                               'De Team nummer heb je normaal gezien gekregen bij het '
                               'inschrijven. Indien dit niet het geval is kan je best even naar '
                               'de helpdesk sturen.')
    channel = client.get_channel(774633121122484244)
    await channel.send('test')


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


def start_up():
    global utils, escaperoom
    escaperoom = EscapeRoom()
    utils = Utils()


if __name__ == '__main__':
    start_up()
    client.run(TOKEN)
