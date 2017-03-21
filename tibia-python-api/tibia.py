import utils
from scrappers import get_page_content
from readers import read_online_players, read_character_information, read_character_death_information, \
    read_guild_information


class Tibia:
    base_worlds_url = 'https://secure.tibia.com/community/?subtopic=worlds&world='
    character_base_url = 'https://secure.tibia.com/community/?subtopic=characters&name='
    base_url_guild = 'https://secure.tibia.com/community/?subtopic=guilds&page=view&GuildName='

    def __init__(self, world_name):
        self.world_name = world_name

    def get_online_players(self):
        url = self.base_worlds_url + self.world_name
        return get_page_content(url, read_online_players)

    def get_character_information(self, character_name):
        url = self.character_base_url + character_name
        return get_page_content(url, read_character_information)

    def get_character_death_information(self, character_name):
        url = self.character_base_url + character_name
        return get_page_content(url, read_character_death_information)

    def get_guild_information(self, guild_url_o_name):
        url = ''
        url_or_name = guild_url_o_name
        is_by_url = utils.is_url(url_or_name)
        if not is_by_url:
            url = self.base_url_guild + url_or_name.replace(' ', '+')
        return get_page_content(url, read_guild_information)
