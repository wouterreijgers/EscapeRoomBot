
class Utils:
    def __init__(self):
        self.admin_channel = 774633121122484244

    def help_menu(self, channel_id, message):
        if channel_id == self.admin_channel:
            reply = 'Hey ' +message.author.name +',\n'
            reply += 'Je bevindt je momenteel in het \'send-to-all\' kanaal, dit wil zeggen dat al de berichten die hier gestuurd worden doorgestuurd kunnen worden naar alle teams. Dit kan bijvoorbeeld gebruikt worden om de start van het spel aan te kondigen. '
            reply += '\n\nHier heb ik even de functies samengevat:'
            reply += '\n- Je kan een bericht aanmaken door het simpelweg in dit kanaal te sturen.'
            reply += '\n- `!send`: Enkel wanneer dit commando getypt word zal ik het bericht versturen.'
            reply += '\n- `!welkom`: Een welkom bericht word gestuurd.'
            reply += '\n- `!start`: Het spel wordt gestart en de eerste opdracht word gestuurd.'
            reply += '\n- `!clear`: De team kanalen worden volledig leeg gemaakt.'
            reply += '\n- `!roles`: Er word een bericht in `Algemeen` gestuurd, de leden kunnen zo hun rollen toewijzen.'
            reply += '\n- `{{TEAM_NAME}}`: Dit kan je in je bericht plaatsen, wanneer het dan verstuurd word zal dit aangepast worden naar de team naam.'
            return reply