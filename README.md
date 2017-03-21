## Python Tibia API.

Easy to use [Tibia](http://www.tibia.com/news/?subtopic=latestnews) API.

### Get started

`pip install tibia-python-api`

### How to use it.

```
from tibia-python-api import Tibia

tibia = Tibia('Zanera');

tibia.get_online_players() // prints the whole list
```
### Methods.

`get_online_players(worldName)` - Method to get all the online players `worldName` is optional.

**Example response**
```
 {
   { name: 'Abelardini', level: '246', vocation: 'Royal Paladin' },
   ...more,
 }
```
`get_character_information(character_name)` - Method to get the whole character information

**Example response**
```
{ 'name:': 'Diegopump ',
  'sex:': 'male',
  'vocation:': 'Elder Druid',
  'level:': '257',
  'achievement_points:': '171',
  'world:': 'Morta',
  'residence:': 'Thais',
  'lastLogin:': 'Feb 12 2017, 06:35:37 CET',
  'account_status:': 'Free Account'
}
```

`get_character_death_information(character_name)` - Method to get the whole character death information by a giving name

**Example response**
```
[
  { date: 'Feb 12 2017, 04:47:16 CET', killed_by_message: 'Killed  at Level 258 by Fenlord.' },
  ...deaths
]
```

`get_guild_information(guild_url_O_Name //guild_url or guild_name)` - Method to get the guild information by a giving guild URL or guild name.

**Example response**
```
[
  guild_information: 'guild information'
]
```
