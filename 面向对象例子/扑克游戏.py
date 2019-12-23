import random

class Card(object):

    def __init__(self, suite, face):
        self._suite = suite
        self._face = face

    @property
    def face(self):
        return self._face
    
    @property
    def suite(self):
        return self._suite

    def __str__(self):
        if self._face == 1:
            face_str = 'A'
        elif self._face == 11:
            face_str = 'J'
        elif self._face == 12:
            face_str = 'Q'
        elif self._face == 13:
            face_str = 'K'
        else:
            face_str = str(self._face)

        return '%s%s' % (self._suite, face_str)
    
    def __repr__(self):
        return self.__str__()

class Pocker(object):
    def __init__(self):
        self._cards = [Card(suite, face) 
                        for suite in '♠️♥️♣️♦️' 
                        for face in range(1, 14)]
        self._current = 0

    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        self._current = 0
        random.shuffle(self._cards)

    @property
    def next(self):
        card = self._cards[self._current]
        self._current += 1
        return card

    @property
    def has_next(self):
        return self._cards < len(self._cards)

    def __str__(self):
        for pocker in self._cards:
            print('%s%s' % ( pocker.suite, pocker.face))


class Player(object):

    def __init__(self, name):
        self._name = name
        self._cards_on_hand = []

    @property
    def name(self):
        return self._name

    @property
    def cards_on_hand(self):
        return self._cards_on_hand

    def get(self, card):
        self._cards_on_hand.append(card)

    # 整理手上的牌
    def arrange(self, card_key):
        self._cards_on_hand.sort(key=card_key)

def get_key(card):
    return (card.suite, card.face)

def main():
    p = Pocker()
    p.shuffle()

    players = [Player('斯大林'), Player('罗斯福'), Player('丘吉尔'), Player('蒋介石')]

    for _ in range(13):
        for player in players:
            print('接到的牌是', p.next)
            player.get(p.next)
        
        for player in players:
            print(player.name + ':', end=' ')
            player.arrange(get_key)
            print(player.cards_on_hand)

if __name__ == '__main__':
    main()