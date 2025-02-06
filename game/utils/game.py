# define card type
from enum import Enum
from typing import NamedTuple
import random
from pydantic import BaseModel
with open("game/utils/wordlist-eng.txt") as f:
        words = f.readlines()
    # select 25 random words
words = random.sample(words, 25)
    
class TeamColor(Enum):
    RED = "red"
    BLUE = "blue"

class CardColor(Enum):
    RED = "red"
    BLUE = "blue"
    BYSTANDER = "bystander"
    ASSASSIN = "assassin"

class CardType(BaseModel):
    # def __init__(self, word: str, color: CardColor | None, is_revealed: bool, was_recently_revealed: bool):
    #     self.word = word
    #     self.color = color
    #     self.is_revealed = is_revealed
    #     self.was_recently_revealed = was_recently_revealed

    word: str
    color: str | None
    is_revealed: bool
    was_recently_revealed: bool

class Role(Enum):
    SPYMASTER = "spymaster"
    OPERATIVE = "operative"

class ChatMessage(NamedTuple):
    sender: Role
    message: str
    team: TeamColor
    cards: list[CardType]

class Clue(NamedTuple):
    clueText: str
    number: int

class GameState():
    cards: list[CardType]
    chatHistory: list[ChatMessage]
    currentTeam: TeamColor
    currentRole: Role
    previousTeam: TeamColor | None = None
    previousRole: Role | None = None
    remainingRed: int
    remainingBlue: int
    currentClue: Clue = None
    currentGuesses: list[str] = None
    gameWinner: TeamColor = None

    def __init__(self):
        self.cards = [CardType(word=word.strip(), color=color, is_revealed=False, was_recently_revealed=False) 
                      for word, color in zip(words, [CardColor.RED]*9 + [CardColor.BLUE]*8 + [CardColor.BYSTANDER]*7 + [CardColor.ASSASSIN])]
        self.chatHistory = []
        self.currentTeam = TeamColor.RED
        self.currentRole = Role.SPYMASTER
        self.remainingRed = 9
        self.remainingBlue = 8
    
