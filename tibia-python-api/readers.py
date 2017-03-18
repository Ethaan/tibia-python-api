import re
from utils import encodeString, camelize

def readOnlinePlayers(html):
    responseCharactersOnline = []
    referenceContent = html.findAll("tr", { "class" : "LabelH" })
    onlinePlayersTable = referenceContent[0].parent.find_all('tr')
    for playerRow in onlinePlayersTable:
        characterDataDic = {}
        count = 0
        cols = playerRow.find_all('td')
        for characterData in cols:
            text = encodeString(characterData.get_text())
            if count == 0:
                print(count)
                characterDataDic['name'] = text
            elif count == 1:
                print(count)
                characterDataDic['level'] = text
            elif count == 2:
                print(count)
                characterDataDic['vocation'] = text
            responseCharactersOnline.append(characterDataDic)
            count += 1
    return responseCharactersOnline

def readCharacterInformation(html):
    responseCharacterData = {}
    pattern = re.compile(r'Character Information')
    characterData = html.find(text=pattern).parent.parent.parent.parent
    for data in characterData:
        text = encodeString(data.get_text())
        twoPointsIndex = text.find(':')
        responseCharacterData[camelize(text[:twoPointsIndex])] = text[twoPointsIndex + 1:]
    return responseCharacterData

def readCharacterDeathInformation(html):
    responseCharacterData = []
    pattern = re.compile(r'Character Deaths')
    characterDeathData = html.find(text=pattern).parent.parent.parent.parent
    for data in characterDeathData:
        text = encodeString(data.get_text())
        cetIndex = text.find('CET')
        if cetIndex > 1:
            responseCharacterData.append({
                'date': text[:cetIndex + 3],
                'killedByMessage': text[cetIndex + 3:]
            })
    return responseCharacterData

def readGuildInformation(html):
    guildData = {}
    guildInformation = html.find('div', { 'id': 'GuildInformationContainer' })
    guildData['guildInformation'] = encodeString(guildInformation.get_text())
    return guildData
