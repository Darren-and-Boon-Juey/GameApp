class BlackjackGame:
  def __init__(self):
    self.available = set()
    self.discard_pile = set()
    self.alphas = ["H", "D", "C", "S"]
    self.royals = set(["J", "Q", "K"])
    for typ in self.alphas:
      for i in range(1, 11):
        curr_card = typ + str(i)
        self.available.add(curr_card)
      
      for royal in list(self.royals):
        curr_card = typ + royal
        self.available.add(curr_card)
  
  
  def discard(self, cards):

    print(f"in discard now. cards: {cards}")
    """
    Bug that caused an error when doing blackjack discard S10C4C9

    if len(cards[0]) % 2 == 1:
      return "Your input is invalid! Please check that there are no typos!"
    """
    try:
      card_list = self.get_cards_sequence(cards)
    except:
      return "Your input is invalid! Please check that there are no typos!"
    
    
    for card in card_list:
      if card in self.discard_pile:
        return "One of the cards you typed in is already in the discarded pile!"
    
    for card in card_list:
      self.available.remove(card)
      self.discard_pile.add(card)

    return f"""
    The game's state has been updated! The follow cards have been added to the discarded pile:
    {card_list}.

    The discarded cards are:
    {self.discard_pile}

    The remaining cards are:
    {self.available}
    """
    
    
    
    for card in card_list:
      if card in self.discard_pile:
        return "One of the cards you typed in is already in the discarded pile!"
    
    for card in card_list:
      self.available.remove(card)
      self.discard_pile.add(card)

    return "Table updated!"
  
  def undo(self, card):
    #will do this if i have time
    pass
  
  def get_probability_info(self, house_card_lst_sequence, your_cards_lst_sequence):
    # Pr(win) = Pr(you > house) 
    # = Pr(your_hand < 21 && house_hand < 21 && your_hand > house_hand) + Pr(your_hand < 21 && house_hand > 21)
    remaining = set(self.available)

    print(f"your_cards_lst_sequence: {your_cards_lst_sequence}")
    print(f"house_card_lst_sequence: {house_card_lst_sequence}")

    your_cards_lst = self.get_cards_sequence(your_cards_lst_sequence)
    house_card_lst = self.get_cards_sequence(house_card_lst_sequence)

    for card in your_cards_lst:
      remaining.remove(card)
    
    for card in house_card_lst:
      remaining.remove(card)
    
    house_value = self.calculate_value(house_card_lst_sequence)
    your_value = self.calculate_value(your_cards_lst_sequence)
    
    # draw condition. OPTIONAL. because it is actually quite hard.
    # Case1: hand == house and hand <= 21 and house <= 21
    # Case2: hand > 21 and house > 21

    # win condition
    # Case1: hand <= 21 and hand > house and house <= 21

    case1_numerator = 0
    case2_numerator = 0

    for card in list(remaining):
      value = 0
      
      if card[1] in self.royals or card[1:] == "10":
          value += 10
      elif int(card[1:]) == 1:
        if house_value <= 10:
          value += 11
      else:
        value += int(card[1:])
      

      if ((value + house_value) < your_value) and (your_value <= 21) and (house_value <= 21):
        case1_numerator += 1
      elif (value + house_value > 21) and (your_value <= 21):
        case2_numerator += 1
    
    
    denominator = len(remaining)
    case1_prob = case1_numerator / denominator
    

    # Case2: house > 21 and hand <= 21
    case2_prob = (case2_numerator / denominator)

    win_probability = (case1_prob + case2_prob) * 100
    
    message = f"""
    Your hand's value: {your_value}
    The house's value: {house_value}
    Win probability: {round(win_probability, 2)}%
    """
    
    return message





  
  def get_stats(self, house_cards_lst, your_cards_lst):

    if len(your_cards_lst) == 2:
      if self.check_blackjack(your_cards_lst):
        return "Blackjack! Congrats! Lets hope the dealer does not get blackjack too."
    
    try:
      your_value = self.calculate_value(your_cards_lst)
    except:
      return "Please ensure the format of your card is correct!"
    
    if your_value > 21:
      return "Sorry, you busted. Lets hope the dealer busts too."
    else:

      if your_value > 21:
        return "Both of you busted!"
      
      try:
        # print(f"your_value input is: {your_cards_lst}")
        # print(f"house_cards input is: {house_cards_lst}")
        return self.get_probability_info(house_cards_lst, your_cards_lst)
      except:
        return "Please ensure your input valids are valid for both house and your cards"
    pass
  
  def get_cards_sequence(self, cards_lst):
    cards = cards_lst[0]
    card_list = []
    curr_card = ""
    for i in range(len(cards)):
      
      curr_word = cards[i]
      if curr_word in self.alphas and i!=0:
        card_list.append(curr_card)
        curr_card = curr_word
      else:
        curr_card += curr_word
    
    card_list.append(curr_card)
    return card_list
    


  def calculate_value(self, lst):
    total = 0
    aces_seen = 0
    cards_lst = self.get_cards_sequence(lst)
    
    for card in cards_lst:
        # print(f"current card being examined in calculate_value: {card}")
        if card[1] in self.royals:
          total += 10
        elif int(card[1:]) == 1:
          aces_seen += 1
        else:
          total += int(card[1:])
    
    value = 0

    if total == 0:
      value = 11 + (aces_seen - 1)
    elif aces_seen == 1 and total <= 10:
      value = total + 11
    elif aces_seen == 2 and total == 0:
      value = 21
    else:
      value = total + aces_seen
    
    # print(f"Return value is {value}")
    return value

  
  def check_blackjack(self, cards_lst):
    tens = set(["J", "Q", "K", "10"])
    aces = set(["H1", "D1", "C1", "S1"])
    card1 = cards_lst[0]
    card2 = cards_lst[1]
    if (card1[1:] in tens) and (card2[1:] in aces):
      return True
    
    if (card2[1:] in tens) and (card1[1:] in aces):
      return True
    
    return False

    
