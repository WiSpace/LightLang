import requests

class Bot:
    def __init__(self, token):
        self.token = token

    def send_message(self, channel_id, content):
        url = f"https://discord.com/api/v8/channels/{channel_id}/messages"
        header = {"authorization": self.token}
        data = {"content": content,
        'message_reference': {'channel_id': channel_id}}
        r = requests.post(url, json=data, headers=header)
        return r, r.text

class Base:
    def __init__(self, bot, id):
        self.bot = bot
        self.id = id

class Channel(Base):
    def rename(self, new_name):
        r = requests.patch(
            f'https://discord.com/api/v9/channels/{self.id}',
            json={'name': new_name},
            headers={'authorization': f'Bot {self.bot.token}'}
        )
        return r, r.text

    # def send_message(self, msg):
    #     r = requests.

class Guild(Base):
    def get_icon(self):
        return f"https://cdn.discordapp.com/icons/{self.id}/guild_icon.png"

class Role:
    def __init__(self, bot, guild, id):
        self.bot = bot
        self.guild = guild
        self.id = id
    
    def rename(self, new_name):
        r = requests.patch(
            f'https://discord.com/api/v9/guilds/{self.guild.id}/roles/{self.id}',
            json={'name': new_name},
            headers={'authorization': f'Bot {token}'}
        )

    def edit_premissions(self, new_permissions):
        r = requests.patch(
            f'https://discord.com/api/v9/guilds/{self.guild.id}/roles/{self.id}',
            json={'permissions': '0'},
            headers={'authorization': f'Bot {token}'}
        )

client =  Bot("MTAzMzc4Nzk2NzY2NTM1NjgxMQ.GhRdsU.DSHBuMrnurLugX71AsOGvEyNtWbcMe9jWtOamc")
print(Guild(client, 1011568154343919666).get_icon())
print(Channel(client, 1023588329314332682).rename("тесты"))
