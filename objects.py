

import random
from word import Word
MARGINX = 6
FONTWIDTH = 9 # based on Consolas Bold 16 pt font size

class Object():
    def __init__(self):
        self.wordlist = self.init_words()
        self.game_words = []

    def init_words(self):
        words_list = None
        try:
            with open("words.txt", "r", newline='') as file:
                words_list = [line.strip() for line in file.readlines()]
        except:
            # Error handling, provide default:
            words_list = ['a','b','c','d','e','f','g','h','i','j','k',
                             'l','m','n','o','p','q','r','s','t','u','v',
                             'x','y','z']
            random.shuffle(words_list)
        self.wordlist_len = len(words_list)
        return words_list
    
    def add_word(self):
        # check that word doesn't duplicate first character in list
        word = random.choice(self.wordlist[:min(self.wordlist_len,1000*level)])
        firstchar = [word.text[0] for word in self.game_words]
        while (word[0] in firstchar):
            word = random.choice(self.wordlist)

        max_x = (self.width - MARGINX) - (FONTWIDTH * len(word))
        x = random.randint(MARGINX,max_x)

        self.game_words.append(Word(word, x))
        return self.game_words[-1]

    def on_execute(self):
        self.on_init()
        
