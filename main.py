import asyncio
import random

import discord

from EscapeRoom import EscapeRoom
from utils import Utils

#Token that connects with the bot
TOKEN = 'Nzc0NjA4NTIwMzM5MTI4MzIw.X6aQZg.7Lir-zWzwbhO1edzUmoXF-_4Kuo    '

client = discord.Client()

alive = True
channels = []
team_channels = {
    'Team 1': {
        'channel_id': 774404823155474483},
    'Team 2': {
        'channel_id': 774607191105077258},
    'Team 3': {
        'channel_id': 774607276559958026}}
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
bully_lines = ['Euhm, {{TEAM}} heeft al een opdracht afgerond',
               'Zijn jullie soms in slaap gevallen? {{TEAM}} heeft weer een deur geopend']


@client.event
async def on_message(message):
    global msg, alive, team_channels, utils, escaperoom, playing
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
            await channel.send('Duid hier onder jouw team aan, dan zal ik er voor zorgen dat je in de juiste chats '
                               'terechtkomt! Weet je niet bij welk team je hoort? Stuur dan even een bericht naar de '
                               'helpdesk.')
            m = channel.last_message
            emoji = '1️⃣'
            await m.add_reaction(emoji)
            emoji = '2️⃣'
            await m.add_reaction(emoji)
            emoji = '3️⃣'
            await m.add_reaction(emoji)
            print(m)
        elif message.content == '!Welkom' or message.content == '!welkom':
            for team, data in team_channels.items():
                channel = client.get_channel(data['channel_id'])
                await channel.send('Hey ' + team + ', \nWelkom bij de Ingenium Escape Room, ik heb zojuist het '
                                                   'signaal gekregen dat ik de gasten mag welkom heten en het spel mag uitleggen! '
                                                   ':partying_face:\n\nBij deze, Welkom allemaal! De escaperoom deze avond zal '
                                                   'volledig gehost worden door mij. De geweldige mensen van Ingenium staan uiteraard '
                                                   'klaar om in te grijpen maar dat is hopelijk niet nodig. Straks begin ik met de '
                                                   'eerte opdracht uit te leggen. Indien jullie een antwoord denken te weten dan mag '
                                                   'je dat hier onder typen en zal ik feedback geven. Je kan ook tips vragen maar '
                                                   'hier hangt uiteraard een straftijd aan vast. Een tip vragen kan je doen door !tip '
                                                   'te typen.\n\nOhja, als er iets onduidelijk is kan je altijd `!help` typen, '
                                                   'ik vat dan even mijn functies.\n\nVeel succes!\n\n(Het startsignaal word zometeen '
                                                   'gegeven)')


        elif message.content == '!Start' or message.content == '!start':
            for team, data in team_channels.items():
                channel = client.get_channel(data['channel_id'])
                await channel.send('\nWelkom beste speurders, \nBij Ingenium '
                                   'willen we deze avond graag een cantus geven maar helaas zijn alle deuren van de '
                                   'KP en de Hagar nog op slot... \nEnkel dankzij jullie kunnen we (hopelijk) zo snel '
                                   'mogelijk beginnen aan de cantus. Zoals jullie kunnen zien zijn er enkele kanalen '
                                   'zichtbaar geworden, hier verschijnen jullie opdrachten. Waneer je een antwoord '
                                   'hebt gevonden dan stuur je dat hier! '
                                   '\n\nVeel succes!')
            channel = client.get_channel(different_rooms['wc']['channel_id'])
            await channel.send('\nEr hangt een cijferslot aan de deur naar de wc’s. De kans is groot dat een zatte '
                               'WINAKKER dat daar voor de lol heeft gehangen. Zoals er nog steeds een Ingeniumsticker '
                               'ergens in de wc’s van de Hagar plakt. Om het slot te openen hebben jullie een code '
                               'nodig van vier cijfers. Wat een geluk dat deze zatte plezante ook nog het volgende op '
                               'de deur heeft geschreven: a+bc-d². Waarschijnlijk dacht deze persoon dat hij of zij '
                               'de code de volgende ochtend niet meer zou weten. \n\nMeer info heb ik helaas ook '
                               'niet, ik heb wel de handleiding van het slot online gevonden: '
                               'https://drive.google.com/file/d/1I_MyLb_7Npn2UHel90NYjr2bdJBfyKK-/view?usp=sharing ')
            channel = client.get_channel(different_rooms['biokot']['channel_id'])
            await channel.send('\n5CPP+Q8    :16u Engineers of Tomorrow vergadering'
                               '\n59CV+8R    :12u30 Pizza’s bestellen'
                               '\n4FV8+R4    :8u30 Kaaskroketten ophalen'
                               '\n5C46+98    :10u Bloed geven'
                               '\n59FW+XF    :13u snacks, prijzen voor bingo'
                               '\n4CJV+MP    :8u Micro ophalen'
                               '\n5CQG+33    :15u Pintje om ons stamcafé te steunen'
                               '\n5C84+XF    :11u Bak-voorbereiding'
                               '\n5CMC+J5    :14u Middageten'
                               '\n4FXM+P3    :9u Ingenium-emmers ophalen')
            channel = client.get_channel(different_rooms['hagar']['channel_id'])
            await channel.send('\nKennen jullie Emma al? Ze is ons nieuwste praesidium lid en zal ons helpen '
                               'vanavond. Net zoals de meesten komt ook Emma met fiets naar de KP. Soms doet ze al '
                               'eens een wedstrijdje “om ter snelste thuis” met andere mensen die even ver moeten als '
                               'zij.')
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
                messages = await channel.history().flatten()
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
            await message.channel.send(file=discord.File('meme0.jpg'))
            await asyncio.sleep(2)
            msg = await message.channel.history(limit=2).flatten()
            await message.channel.delete_messages(msg)
            return
        correct, new_status, team_win, response, door_opened = escaperoom.process(message)
        if correct:
            if 'hagar' == door_opened:
                role = message.author.guild.get_role(781966223105720331)
                if message.author.voice:
                    for member in message.author.voice.channel.members:
                        await member.add_roles(role)()
                channel = client.get_channel(different_rooms['bot_channel']['channel_id'])
                await channel.send('bot ' + str(message.channel.id) + ' conv_hagar')
            if 'biokot' == door_opened:
                channel = client.get_channel(different_rooms['bot_channel']['channel_id'])
                await channel.send('bot ' + str(message.channel.id) + ' conv_biokot')
            if 'wc' == door_opened:
                role = message.author.guild.get_role(781989687023763457)
                if message.author.voice:
                    for member in message.author.voice.channel.members:
                        await member.add_roles(role)
                channel = client.get_channel(different_rooms['bot_channel']['channel_id'])
                await channel.send('bot ' + str(message.channel.id) + ' conv_wc')

            parts = bully_lines[random.randint(0, len(bully_lines) - 1)].split('{{TEAM}}')
            tekst = parts[0] + team_win + parts[1]
            for team, data in team_channels.items():
                if not team_win == team:
                    channel = client.get_channel(data['channel_id'])
                    await channel.send(tekst)
        await message.channel.send(response)


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
