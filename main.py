import random

import discord

from EscapeRoom import EscapeRoom
from utils import Utils

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
msg = ''
utils = None
escaperoom = None
playing = False
bully_lines = ['Euhm, {{TEAM}} heeft al een opdracht afgerond', 'Zijn jullie soms in slaap gevallen? {{TEAM}} heeft weer een deur geopend']


@client.event
async def on_message(message):
    global msg, alive, team_channels, utils, escaperoom, playing
    print(message)
    if message.content == '!Phoenix' and message.author.id == 650664861147332609:
        await message.channel.send('Rebooting...');
        alive = True
    if not alive:
        return None
    if message.content == '!KILL' and message.author.id == 650664861147332609:
        alive = False
        await message.channel.send('Ingenium bot was killed... ')
        return
    if message.author == client.user or message.author.bot:
        return

    # Algemene functies die altijd werken
    if not playing or message.channel.id == 774633121122484244:
        if message.content == '!help' or message.content == '!Help':
            await message.channel.send(utils.help_menu(message.channel.id, message))
            return

    # Admin functies
    if message.channel.id == 774633121122484244:
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
                                   'mogelijk beginnen aan de cantus. Jullie eerste opdracht is vrij simpel, ... , '
                                   '\n\nVeel succes!')
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
        else:
            msg = message.content
            await message.channel.send(msg)
            await message.channel.send('\nAls je dit bericht wil verzenden typ dan `!send`')
    if playing:
        correct, new_status, team_win, response = escaperoom.process(message)
        if correct:
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
