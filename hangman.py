import random
import re
import sys

class Hangman:
  wordList = ['orange', 'elephant', 'rabbit', 'leopard', 'apple', 'mango']
  # word = ''

  def __init__(self):
    self.guess = []
    self.misses = 0

  def board(self):
    pics = ['''
      ----+
      |
      |
      |
    =====''', '''
      ----+
      |   o
      |
      |
    ===== ''', ''''
      ----+
      |   o
      |   |
      |
    =====''', '''
      ----+
      |   o
      |  /|\\
      |
    =====     ''', '''
      ----+
      |   o
      |  /|\\
      |  / \\
    =====     ''']
    print(pics[self.misses])
    

  def display(self):
    self.board()
    print(self.word_display())


  def guess_letter(self):
    print('Enter your guess letter...')
    sel = re.compile(r'[A-Za-z]')
  
    while True:
      letter = input()
      match = sel.search(letter)
      if len(letter) != 1:
        print('Enter a single letter')
      elif match == None:
        print("Enter valid letter [AZ]")
      elif letter in self.guess: ### After guessing a letter remove the guessed letter from the word list, for ease in the recurring words
        print('You have already guessed it, pick another')
      else:
        return letter

  

  def win(self, word):
    for l in word:
      if l not in self.guess:
        return False
    return True 

  def lost(self):
    return (self.misses > 3)
    """
    if self.misses > 7:
      return True
    else:
      return False
    """

  def get_word(self):
    word = random.choice(self.wordList)
    return word

  def word_display(self):
    '''return self.word, with blanks for missing guesses'''
    return ' '.join(l if l in self.guess else '_' for l in self.word)
 
  
  
  def play(self):
    print("Getting word....")
    self.word = self.get_word()
    # print(self.word)
    # guessedList = ''

    while True:
      self.display()
      if self.lost():
        # print(self.misses)
        print('You lost the game...')
        return
      elif self.win(self.word):
        print('You won the Game...')
        return
      else:
        letter = self.guess_letter()
        if letter in self.word:
          self.guess.append(letter)
          # self.word.remove(letter)
        else:
          self.misses += 1
 
def play_again():
  print('Enter [Y/y] if you want to play again: ')
  a = input().lower()
  return a  

def main():
  print("### Hangman Game ###")
  while True:
    game = Hangman()
    game.play()
    a = play_again()
    if a == 'y':
      pass
    else:
      # sys.exit()
      break


if __name__ == '__main__':
  main()
