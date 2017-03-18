## Python Tibia API.

Easy to use [Tibia](http://www.tibia.com/news/?subtopic=latestnews) API.

### Get started

`pip install tibia-python-api`

### How to use it.

```
from tibia-python-api import Tibia

tibia = Tibia('Zanera');

tibia.getOnlinePlayers() // prints the whole list
```
### Methods.

`getOnlinePlayers(worldName)` - Method to get all the online players `worldName` is optional.

**Example response**
```
 {
   { name: 'Abelardini', level: '246', vocation: 'Royal Paladin' },
   ...more,
 }
```
`getCharacterInformation(characterName)` - Method to get the whole character information

**Example response**
```
{ 'name:': 'Diegopump ',
  'sex:': 'male',
  'vocation:': 'Elder Druid',
  'level:': '257',
  'achievementPoints:': '171',
  'world:': 'Morta',
  'residence:': 'Thais',
  'lastLogin:': 'Feb 12 2017, 06:35:37 CET',
  'accountStatus:': 'Free Account'
}
```

`getCharacterDeathInformation(characterName)` - Method to get the whole character death information by a giving name

**Example response**
```
[
  { date: 'Feb 12 2017, 04:47:16 CET', killedByMessage: 'Killed  at Level 258 by Fenlord.' },
  ...deaths
]
```

`getGuildInformation(guildUrlOrName //guildUrl or GuildName)` - Method to get the guild information by a giving guild URL or guild name.

**Example response**
```
[
  guildInformation: 'guild information'
]
```
