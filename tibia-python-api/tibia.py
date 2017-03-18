from utils import isUrl
from scrappers import getPageConent
from readers import readOnlinePlayers, readCharacterInformation, readCharacterDeathInformation, readGuildInformation

class Tibia:
    baseWorldsUrl = 'https://secure.tibia.com/community/?subtopic=worlds&world='
    characterBaseUrl = 'https://secure.tibia.com/community/?subtopic=characters&name='
    baseUrlGuild = 'https://secure.tibia.com/community/?subtopic=guilds&page=view&GuildName='

    def __init__(self, worldName):
        self.worldName = worldName

    def getOnlinePlayers(self):
        url = self.baseWorldsUrl + self.worldName
        return getPageConent(url, readOnlinePlayers)

    def getCharacterInformation(self, characterName):
        url = self.characterBaseUrl + characterName
        return getPageConent(url, readCharacterInformation)

    def getCharacterDeathInformation(self, characterName):
        url = self.characterBaseUrl + characterName
        return getPageConent(url, readCharacterDeathInformation)

    def getGuildInformation(self, guildUrlOName):
        urlOrName = guildUrlOName
        isByUrl = isUrl(urlOrName)
        if isByUrl == False:
            url = self.baseUrlGuild + urlOrName.replace(' ', '+')
        print(url)
        return getPageConent(url, readGuildInformation)
