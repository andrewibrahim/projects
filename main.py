#!/usr/bin/env python3

import random

def main():
    while True:
      print("Wlecome to the number game!")
      guess = input('Enter your guess (H, L or X): ')
      if guess == "X":
        break
      print('Your guess was: ' + guess)
      rnd = random_number()
      print("Your number is", rnd)
  
      if (rnd <= 50 and guess == "L") or (rnd >= 51 and guess == "H"):
        print("You win!")
      else:
        print("You lose! Try again!")

def random_number():
  x = random.randint(0,100)
  return (x)


if __name__ == "__main__":
  main()