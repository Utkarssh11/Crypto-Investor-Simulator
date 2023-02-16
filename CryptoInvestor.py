from time import sleep
import os
import random
from colorama import *

gamedays = {
  'ZXC_good': 'Mlon Eusk tweet: ZXC to the moon!',
  'PI_good': 'PI token received investments in the amount of $9999m',
  'MmM_godd': 'MMM token is bought by hamsters',
  'ZXC_bad': 'Rumor: ZXC token scam',
  'PI_bad': 'PI token smart-contract hacked',
  'MmM_bad': 'Hamsters sell their MMMs'
}


def game_loading():
  for i in range(90):
    print(f"Loading... | {i}%")
    sleep(0.02)
    os.system('clear')
  os.system('clear')
  print("lol this is fake loading")
  sleep(1)
  os.system('clear')
  print(
    "Hello. You've landed on another game posted on replit.\nI'm sure there are hundreds of similar games but thanks for choosing my game.\nI'm sure you won't like it.\n\n\nHave Fun!"
  )
  sleep(6.5)


def game_menu():
  balance = 10000
  day = 1
  ZXC, PI, MmM = 16, 256, 512
  usr_zxc, usr_pi, usr_mmm = 0, 0, 0
  for _ in range(999999999):
    os.system('clear')
    daily_news_key = random.choice(list(gamedays))
    print('Day:', day)
    if daily_news_key == 'ZXC_bad' or daily_news_key == 'PI_bad' or daily_news_key == 'MmM_bad':
      print(
        f'********** Daily News: {Fore.RED + gamedays[daily_news_key] + Style.RESET_ALL} **********'
      )
    else:
      print(
        f'********** Daily News: {Fore.GREEN + gamedays[daily_news_key] + Style.RESET_ALL} **********'
      )
    print(f'Your balance: {Fore.GREEN + str(balance)}$ ')
    print(Style.RESET_ALL)
    print(Fore.GREEN)
    print("*" * 30)
    print(f"* ZXC price: {ZXC}$ | You have: {usr_zxc} *")
    print(f"* PI price: {PI}$ | You have: {usr_pi} *")
    print(f"* MmM price: {MmM}$ | You have: {usr_mmm} *")
    print("*" * 30)
    print(Style.RESET_ALL)
    if (usr_zxc * ZXC) + (usr_mmm * MmM) + (usr_pi * PI) > 0:
      print(
        Fore.GREEN +
        f"* Your PNL: {(usr_zxc * ZXC) + (usr_mmm * MmM) + (usr_pi * PI)}$ *\n"
      )
      print(Style.RESET_ALL)
    else:
      print(
        Fore.RED +
        f"* Your PNL: {(usr_zxc * ZXC) + (usr_mmm * MmM) + (usr_pi * PI)}$ *\n"
      )
      print(Style.RESET_ALL)
    print(
      Fore.BLUE +
      "Press 1 to select ZXC token\nPress 2 to select PI token\nPress 3 to select MmM token\n\n"
      + Style.RESET_ALL)
    print("***** When you're done press ANY. Then a new day will begin *****")
    print()
    print()
    print()
    token_choice = str(input("Make a choice: "))
    if token_choice == '1':
      os.system('clear')
      print(f"{'*' * 15} You choosed ZXC token {'*' * 15}\n\n")
      print(f'You can buy: {balance // ZXC}')
      print(f"You can sell: {usr_zxc} tokens")
      print("\n\n")
      print("Press 1 if you want to BUY")
      print("Press 2 if you want to SELL")
      print("Press 3 if you want return to main menu")
      ininput = input("Let's do it: ")
      if ininput == '1':
        count = int(input("Enter the number of tokens you wish to purchase: "))
        if count * ZXC > balance:
          os.system('clear')
          print(Fore.RED + 'ERROR!')
          print(Style.RESET_ALL)
          sleep(1)
        else:
          usr_zxc += count
          balance -= ZXC * count
      elif ininput == '2':
        count = int(input("Enter the number of tokens you wish to sell: "))
        if count > usr_zxc:
          os.system('clear')
          print(Fore.RED + 'ERROR!')
          print(Style.RESET_ALL)
          sleep(1)
        else:
          usr_zxc -= count
          balance += ZXC * count
      elif ininput == '3':
        pass
    elif token_choice == '2':
      os.system('clear')
      print(f"{'*' * 15} You choosed PI token {'*' * 15}\n\n")
      print(f'You can buy: {balance // PI}')
      print(f"You can sell: {usr_pi} tokens")
      print("\n\n")
      print("Press 1 if you want to BUY")
      print("Press 2 if you want to SELL")
      print("Press 3 if you want return to main menu")
      ininput = input("Let's do it: ")
      if ininput == '1':
        count = int(input("Enter the number of tokens you wish to purchase: "))
        if count * PI > balance:
          os.system('clear')
          print(Fore.RED + 'ERROR!')
          print(Style.RESET_ALL)
          sleep(1)
        else:
          usr_pi += count
          balance -= PI * count
      elif ininput == '2':
        count = int(input("Enter the number of tokens you wish to sell: "))
        if count > usr_pi:
          os.system('clear')
          print(Fore.RED + 'ERROR!')
          print(Style.RESET_ALL)
          sleep(1)
        else:
          usr_pi -= count
          balance += PI * count
      elif ininput == '3':
        pass
    elif token_choice == '3':
      os.system('clear')
      print(f"{'*' * 15} You choosed MmM token {'*' * 15}\n\n")
      print(f'You can buy: {balance // MmM}')
      print(f"You can sell: {usr_mmm} tokens")
      print("\n\n")
      print("Press 1 if you want to BUY")
      print("Press 2 if you want to SELL")
      print("Press 3 if you want return to main menu")
      ininput = input("Let's do it: ")
      if ininput == '1':
        count = int(input("Enter the number of tokens you wish to purchase: "))
        if count * MmM > balance:
          os.system('clear')
          print(Fore.RED + 'ERROR!')
          print(Style.RESET_ALL)
          sleep(1)
        else:
          usr_mmm += count
          balance -= MmM * count
      elif ininput == '2':
        count = int(input("Enter the number of tokens you wish to sell: "))
        if count > usr_mmm:
          os.system('clear')
          print(Fore.RED + 'ERROR!')
          print(Style.RESET_ALL)
          sleep(1)
        else:
          usr_mmm -= count
          balance += MmM * count
      elif ininput == '3':
        pass
    elif token_choice != '1' and token_choice != '2' and token_choice != '3':
      day += 1
      if daily_news_key == 'ZXC_good':
        ZXC += random.randrange(10, 900)
      elif daily_news_key == 'PI_good':
        PI += random.randrange(5, 300)
      elif daily_news_key == 'MmM_godd':
        MmM += random.randrange(10, 100)
      elif daily_news_key == 'ZXC_bad':
        ZXC -= random.randrange(10, 90)
        if ZXC <= 0:
          ZXC = 1
      elif daily_news_key == 'PI_bad':
        PI -= random.randrange(5, 30)
        if PI <= 0:
          PI = 1
      elif daily_news_key == 'MmM_bad':
        MmM -= random.randrange(10, 101)
        if MmM <= 0:
          MmM = 1


if __name__ == "__main__":
  game_loading()
  game_menu()
