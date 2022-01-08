'''
A database storing the cart for each chat.
session {
  chat_id: {
    mahjong: None,
    blackjack: None,
  }
}
'''
session = {}
 

TileIcons = {
  "DOTS": {
    1: "\U0001F019",
    2: "\U0001F01A",
    3: "\U0001F01B",
    4: "\U0001F01C",
    5: "\U0001F01D",
    6: "\U0001F01E",
    7: "\U0001F01F",
    8: "\U0001F020",
    9: "\U0001F021"
  },
  "BAMBOO": {
    1: "\U0001F010",
    2: "\U0001F011",
    3: "\U0001F012",
    4: "\U0001F013",
    5: "\U0001F014",
    6: "\U0001F015",
    7: "\U0001F016",
    8: "\U0001F017",
    9: "\U0001F018"
  },
  "CHARACTER": {
    1: "\U0001F007",
    2: "\U0001F008",
    3: "\U0001F009",
    4: "\U0001F00A",
    5: "\U0001F00B",
    6: "\U0001F00C",
    7: "\U0001F00D",
    8: "\U0001F00E",
    9: "\U0001F00F"
  },
  "WINDS": {
    "EAST": "\U0001F000",
    "SOUTH": "\U0001F001",
    "WEST": "\U0001F002",
    "NORTH": "\U0001F003"
  },
  "DRAGONS": {
    "ZHONG": "\U0001F004",
    "FA": "\U0001F005",
    "BAIBAN": "\U0001F006"
  },
  "FLOWERS": {
    1: "\U0001F022",
    2: "\U0001F023",
    3: "\U0001F024",
    4: "\U0001F025"
  },
  "SEASONS": {
    1: "\U0001F026",
    2: "\U0001F027",
    3: "\U0001F028",
    4: "\U0001F029"
  },
  "ANIMALS": {
    "CHICKEN": '\U0001F414',
    "CAT": '\U0001F408',
    "MOUSE": '\U0001F400',
    "WORM": '\U0001F41B'
  }
}


'''
A database storing the available items in the store.
'''
fruits = {
  'Apple': {
    'description': 'An apple',
    'price': 1.50,
    'img': 'https://images.unsplash.com/photo-1619546813926-a78fa6372cd2?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80'
  },
  'Pear': {
    'description': 'A pear',
    'price': 1.00,
    'img': 'https://images.unsplash.com/photo-1615484477778-ca3b77940c25?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=735&q=80'
  },
  'Orange': {
    'description': 'An orange',
    'price': 2.50,
    'img': 'https://images.unsplash.com/photo-1603664454146-50b9bb1e7afa?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80'
  },
}
