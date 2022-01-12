from backend.storage.database import TileIcons

class MahjongGame:
    def __init__(self):
        # Setting up game tiles and "board"
        self.playersWind = ''
        self.MahjongTiles = {}
        self.NumMahjongTiles = 148

        MahjongTileCategories = ["DOTS", "BAMBOO", "CHARACTER", "WINDS", "DRAGONS", "FLOWERS", "SEASONS", "ANIMALS"]
        for Category in MahjongTileCategories:
            self.MahjongTiles[Category] = {}

        for i in range(1, 10):
            self.MahjongTiles["DOTS"][i] = 4
            self.MahjongTiles["BAMBOO"][i] = 4
            self.MahjongTiles["CHARACTER"][i] = 4

        for i in ["NORTH", "SOUTH", "EAST", "WEST"]:
            self.MahjongTiles["WINDS"][i] = 4

        self.MahjongTiles["DRAGONS"]["ZHONG"] = 4
        self.MahjongTiles["DRAGONS"]["FA"] = 4
        self.MahjongTiles["DRAGONS"]["BAIBAN"] = 4

        for i in range(1, 5):
            self.MahjongTiles["FLOWERS"][i] = 1
            self.MahjongTiles["SEASONS"][i] = 1

        self.MahjongTiles["ANIMALS"]["CHICKEN"] = 1
        self.MahjongTiles["ANIMALS"]["MOUSE"] = 1
        self.MahjongTiles["ANIMALS"]["CAT"] = 1
        self.MahjongTiles["ANIMALS"]["WORM"] = 1

        
        # Setting up individual players' hands
        # To find bonus tiles, just iterate and take those len == 1
        self.NORTHPlayer = set()
        self.SOUTHPlayer = set()
        self.EASTPlayer = set()
        self.WESTPlayer = set()

    def inputHandler(self, inputArr):
      if len(inputArr) == 0:
        return "An error has occured, kindly check your inputs"
      
      if len(inputArr) != 1 and self.playersWind == '':
        return "Kindly set your wind first"

      if len(inputArr) == 1 and inputArr[0] in ['N', 'S', 'E', 'W', 'n', 'e', 's', 'w'] and self.playersWind == '':
          # Wind can only be set one time per game
        inputArr[0] = inputArr[0].upper()
        if inputArr[0] == 'E':
          self.playersWind = 'EAST'
        elif inputArr[0] == 'W':
          self.playersWind = 'WEST'
        elif inputArr[0] == 'N':
          self.playersWind = 'NORTH'
        elif inputArr[0] == 'S':
          self.playersWind = 'SOUTH'
        return "Your wind direction has been set"
      else:
        if self.playersWind != '':
          try:
            err = self.executeAction(inputArr[0].upper(), inputArr[1].upper(), inputArr[2:])
            if not err:
              return self.printAllInformation2()
            else:
              return err
          except:
            return "An error has occured, kindly check your inputs"
        else:
          return "Kindly set your wind first"
        
    def executeAction(self, player, action, tiles):
      if player == 'N':
        cur_player = self.NORTHPlayer
      elif player == 'S':
        cur_player = self.SOUTHPlayer
      elif player == 'E':
        cur_player = self.EASTPlayer
      elif player == 'W':
        cur_player = self.WESTPlayer
      tiles = tiles[0]

      if action == 'DISCARD':
        # Only 1 tile
        temp = self.convertRepresentation(tiles)
        if self.isBonus(temp[0], temp[1]):
          return "You cannot discard bonus tiles or multiple tiles at once. Kindly use the mahjong help command for more information"
        if self.MahjongTiles[temp[0]][temp[1]] == 0:
          return "There should not be any tiles left to discard"
        else:
          self.MahjongTiles[temp[0]][temp[1]] -= 1

      elif action == 'EAT':
        if not self.validEat(tiles):
          return "You can only eat 3 consecutive tiles, from the same suite"
        new_tiles = []
        for i in range(0, 6, 2):
          temp = self.convertRepresentation(tiles[i:i+2])
          if self.MahjongTiles[temp[0]][temp[1]] == 0:
            return "An eat is impossible at this time"
        for i in range(0, 6, 2):
          temp = self.convertRepresentation(tiles[i:i+2])
          self.MahjongTiles[temp[0]][temp[1]] -= 1
          new_tiles.append(temp)
        cur_player.add(tuple(new_tiles))

      elif action == 'PONG':
        temp = self.convertRepresentation(tiles)
        if self.MahjongTiles[temp[0]][temp[1]] >= 3:
          self.MahjongTiles[temp[0]][temp[1]] -= 3
          cur_player.add((temp, temp, temp))
        else:
          return "A pong is impossible at this point in time"
        
      elif action == 'GANG':
        temp = self.convertRepresentation(tiles)
        if (temp, temp, temp) in cur_player and self.MahjongTiles[temp[0]][temp[1]] == 1:
          cur_player.remove((temp, temp, temp))
          cur_player.add((temp, temp, temp, temp))
          self.MahjongTiles[temp[0]][temp[1]] = 0
        elif self.MahjongTiles[temp[0]][temp[1]] == 4:
          cur_player.add((temp, temp, temp, temp))
          self.MahjongTiles[temp[0]][temp[1]] = 0
        else:
          return "A gang is impossible at this point in time"

      elif action == 'BONUS':
        temp = self.convertRepresentation(tiles)
        if not self.isBonus(temp[0], temp[1]):
          return "This is not a bonus tile"
        if self.MahjongTiles[temp[0]][temp[1]] == 0:
          return "This bonus tile has already been claimed before"
        else:
          self.MahjongTiles[temp[0]][temp[1]] = 0
          cur_player.add(temp)

    def validEat(self, tiles):
      if len(tiles) != 6:
        return False
      elif int(tiles[1]) + 1 != int(tiles[3]) or int(tiles[3]) != int(tiles[5]) - 1:
        return False
      elif tiles[0] != tiles[2] and tiles[0] != tiles[4]:
        return False
      return True

    def isBonus(self, inputString0, inputString1):
      inputString1 = str(inputString1)
      bonuses = {'CHICKEN', 'CAT', 'MOUSE', 'WORM', 'FLOWERS1', 'FLOWERS2', 'FLOWERS3', 'FLOWERS4', 'SEASONS1', 'SEASONS2', 'SEASONS3', 'SEASONS4'}
      if inputString1.upper() in bonuses:
        return True
      temp = inputString0 + inputString1
      if temp in bonuses:
        return True
      return False

    def convertRepresentation(self, inputString):
      if inputString.upper() == 'CHICKEN':
        return ('ANIMALS', 'CHICKEN')
      elif inputString.upper() == 'CAT':
        return ('ANIMALS', 'CAT')
      elif inputString.upper() == 'MOUSE':
        return ('ANIMALS', 'MOUSE')
      elif inputString.upper() == 'WORM':
        return ('ANIMALS', 'WORM')
      
      elif inputString.upper() == 'ZHONG':
        return ('DRAGONS', 'ZHONG')
      elif inputString.upper() == 'FA':
        return ('DRAGONS', 'FA')
      elif inputString.upper() == 'BAIBAN':
        return ('DRAGONS', 'BAIBAN')

      elif inputString.upper() == 'N':
        return ('WINDS', 'NORTH')
      elif inputString.upper() == 'E':
        return ('WINDS', 'EAST')
      elif inputString.upper() == 'S':
        return ('WINDS', 'SOUTH')
      elif inputString.upper() == 'W':
        return ('WINDS', 'WEST')

      elif len(inputString) == 2 and inputString.upper()[0] == 'C' and 0 <= int(inputString[1]) <= 9:
        return ('CHARACTER', int(inputString[1]))
      elif len(inputString) == 2 and inputString.upper()[0] == 'D' and 0 <= int(inputString[1]) <= 9:
        return ('DOTS', int(inputString[1]))
      elif len(inputString) == 2 and inputString.upper()[0] == 'B' and 0 <= int(inputString[1]) <= 9:
        return ('BAMBOO', int(inputString[1]))

      elif inputString.upper()[0] == 'F' and 1 <= int(inputString[1]) <= 4:
        return ('FLOWERS', int(inputString[1]))
      elif inputString.upper()[0] == 'S' and 1 <= int(inputString[1]) <= 4:
        return ('SEASONS', int(inputString[1]))

      else:
        print("THERE WAS SOME ISSUE WITH THE INPUT")

    """
    def printAllInformation(self):
        print("-------------------------------------")
        print("Current unrevealed tiles:")
        print("-------------------------------------")
        
        print('\U0001F007', '\U0001F008', '\U0001F009', '\U0001F00A', '\U0001F00B', '\U0001F00C', '\U0001F00D', '\U0001F00E', '\U0001F00F', '\n', sep=' ', end=' ')
        for i in range(1, 10):
            print(self.MahjongTiles["CHARACTER"][i], end=' ')
        print()

        print('\U0001F010', '\U0001F011', '\U0001F012', '\U0001F013', '\U0001F014', '\U0001F015', '\U0001F016', '\U0001F017', '\U0001F018', '\n', sep=' ', end=' ')
        for i in range(1, 10):
            print(self.MahjongTiles["BAMBOO"][i], end=' ')
        print()

        print('\U0001F019', '\U0001F01A', '\U0001F01B', '\U0001F01C', '\U0001F01D', '\U0001F01E', '\U0001F01F', '\U0001F020', '\U0001F021', '\n', sep=' ', end=' ')
        for i in range(1, 10):
            print(self.MahjongTiles["DOTS"][i], end=' ')
        print()

        print('\U0001F000', '\U0001F001', '\U0001F002', '\U0001F003', '\n', sep=' ', end=' ')
        for i in ["EAST", "SOUTH", "WEST", "NORTH"]:
            print(self.MahjongTiles["WINDS"][i], end=' ')
        print()

        print('\U0001F004', '\U0001F005', '\U0001F006', '\n', sep=' ', end=' ')
        for i in ["ZHONG", "FA", "BAIBAN"]:
            print(self.MahjongTiles["DRAGONS"][i], end=' ')
        print()

        print('\U0001F022', '\U0001F023', '\U0001F024', '\U0001F025', '\U0001F026', '\U0001F027', '\U0001F028', '\U0001F029', '\n', sep=' ', end=' ')
        for i in range(1, 5):
            print(self.MahjongTiles["FLOWERS"][i], end=' ')
        for i in range(1, 5):
            print(self.MahjongTiles["SEASONS"][i], end=' ')
        print()

        print('\U0001F414', '\U0001F41B', '\U0001F408', '\U0001F400', '\n', sep=' ', end=' ')
        for i in ["CHICKEN", "WORM", "CAT", "MOUSE"]:
            print(self.MahjongTiles["ANIMALS"][i], end='  ')
        print()

        print("-------------------------------------")

        self.printPlayerInformation('EAST', self.EASTPlayer)
        self.printPlayerInformation('SOUTH', self.SOUTHPlayer)
        self.printPlayerInformation('WEST', self.WESTPlayer)
        self.printPlayerInformation('NORTH', self.NORTHPlayer)

    def printPlayerInformation(self, wind, player):
        if self.playersWind == wind:
          print(wind, "Player (You)")
        else:
          print(wind, "Player")
        print("-------------------------------------")

        for tiles in player:
          suite = ""
          if len(tiles) >= 3:
            tiles = list(tiles)
            for tile in tiles:
              suite += TileIcons[tile[0]][tile[1]]
            print(suite, end=' ')
        print()

        for tiles in player:
          if len(tiles) == 2:
            print(TileIcons[tiles[0]][tiles[1]], end='')
        print()
        print("-------------------------------------")
    """
    
    def printAllInformation2(self):
      res = []
      res.append("-------------------------------------")
      res.append("Current unrevealed tiles:")
      res.append("-------------------------------------")

      res.append('\U0001F007 \U0001F008 \U0001F009 \U0001F00A \U0001F00B \U0001F00C \U0001F00D \U0001F00E \U0001F00F')
      temp = ''
      for i in range(1, 10):
        temp += str(self.MahjongTiles["CHARACTER"][i]) + ' '
      res.append(temp)

      res.append('\U0001F010 \U0001F011 \U0001F012 \U0001F013 \U0001F014 \U0001F015 \U0001F016 \U0001F017 \U0001F018')
      temp = ''
      for i in range(1, 10):
        temp += str(self.MahjongTiles["BAMBOO"][i]) + ' '
      res.append(temp)

      res.append('\U0001F019 \U0001F01A \U0001F01B \U0001F01C \U0001F01D \U0001F01E \U0001F01F \U0001F020 \U0001F021')
      temp = ''
      for i in range(1, 10):
          temp += str(self.MahjongTiles["DOTS"][i]) + ' '
      res.append(temp)

      res.append('\U0001F000 \U0001F001 \U0001F002 \U0001F003')
      temp = ''
      for i in ["EAST", "SOUTH", "WEST", "NORTH"]:
          temp += str(self.MahjongTiles["WINDS"][i]) + ' '
      res.append(temp)

      res.append('\U0001F004 \U0001F005 \U0001F006')
      temp = ''
      for i in ["ZHONG", "FA", "BAIBAN"]:
          temp += str(self.MahjongTiles["DRAGONS"][i]) + ' '
      res.append(temp)

      res.append('\U0001F022 \U0001F023 \U0001F024 \U0001F025 \U0001F026 \U0001F027 \U0001F028 \U0001F029')
      temp = ''
      for i in range(1, 5):
          temp += str(self.MahjongTiles["FLOWERS"][i]) + ' '
      for i in range(1, 5):
          temp += str(self.MahjongTiles["SEASONS"][i]) + ' '
      res.append(temp)

      res.append('\U0001F414 \U0001F41B \U0001F408 \U0001F400')
      temp = ''
      for i in ["CHICKEN", "WORM", "CAT", "MOUSE"]:
          temp += str(self.MahjongTiles["ANIMALS"][i]) + ' '
      res.append(temp)

      res.append("-------------------------------------")

      res.append(self.printPlayerInformation2('EAST', self.EASTPlayer))
      res.append(self.printPlayerInformation2('SOUTH', self.SOUTHPlayer))
      res.append(self.printPlayerInformation2('WEST', self.WESTPlayer))
      res.append(self.printPlayerInformation2('NORTH', self.NORTHPlayer))
      
      return '\n'.join(res)

    def printPlayerInformation2(self, wind, player):
      res = []
      if self.playersWind == wind:
        res.append(wind + " Player (You)")
      else:
        res.append(wind + " Player")
        res.append("-------------------------------------")

      temp = ""
      for tiles in player:
        if len(tiles) >= 3:
          tiles = list(tiles)
          for tile in tiles:
            temp += TileIcons[tile[0]][tile[1]]
          temp += ' '
      res.append(temp)

      temp = ""
      for tiles in player:
        if len(tiles) == 2:
          temp += TileIcons[tiles[0]][tiles[1]] + ' '
      res.append(temp)
      res.append("-------------------------------------")

      return '\n'.join(res)
    