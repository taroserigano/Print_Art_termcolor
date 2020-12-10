from pyfiglet import figlet_format 
from termcolor import colored 

def print_art():
  loop = True

  while loop:
    valid_colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "blue")

    msg = input("What would you like to print? \n")
    color = input("What color? \n")

    if color not in valid_colors:
      color = "blue"

    ascii_art = figlet_format(msg)
    colored_ascii = colored(ascii_art, color=color)
    print(colored_ascii)

    question = input("Do some more art? Press Y for YES, N for NO\n")
    if question.lower() == "y":
      loop = True
    else:
      print("Thank you for playing!")
      loop = False   



print_art()
