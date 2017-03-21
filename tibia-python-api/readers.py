import re
from utils import encode_string, camelize


def read_online_players(html):
    response_character_online = []
    reference_content = html.findAll("tr", {"class": "LabelH"})
    online_players_table = reference_content[0].parent.find_all('tr')
    for playerRow in online_players_table:
        character_data_dict = {}
        count = 0
        cols = playerRow.find_all('td')
        for characterData in cols:
            text = encode_string(characterData.get_text())
            if count == 0:
                character_data_dict['name'] = text
            elif count == 1:
                character_data_dict['level'] = text
            elif count == 2:
                character_data_dict['vocation'] = text
            response_character_online.append(character_data_dict)
            count += 1
    return response_character_online


def read_character_information(html):
    reponse_character_data = {}
    pattern = re.compile(r'Character Information')
    character_data = html.find(text=pattern).parent.parent.parent.parent
    for data in character_data:
        text = encode_string(data.get_text())
        two_points_index = text.find(':')
        reponse_character_data[camelize(text[:two_points_index])] = text[two_points_index + 1:]
    return reponse_character_data


def read_character_death_information(html):
    response_character_data = []
    pattern = re.compile(r'Character Deaths')
    character_data = html.find(text=pattern).parent.parent.parent.parent
    for data in character_data:
        text = encode_string(data.get_text())
        cet_index = text.find('CET')
        if cet_index > 1:
            response_character_data.append({
                'date': text[:cet_index + 3],
                'killed_by_message': text[cet_index + 3:]
            })
    return response_character_data


def read_guild_information(html):
    guild_data = {}
    guild_information = html.find('div', {'id': 'GuildInformationContainer'})
    guild_data['guild_information'] = encode_string(guild_information.get_text())
    return guild_data
