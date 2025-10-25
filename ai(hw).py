import colorama
from colorama import Fore, Style
colorama.init

print(f"{Fore.CYAN}Hey, I am an AI chatbot! What is your name?")
name = input()
print(f"{Fore.YELLOW}Nice to meet you,", name)
print(f"{Fore.CYAN} What is the weather like outside today")
print(f"{Fore.YELLOW} Is it sunny, rainy, windy or snowy.")
weather = input().lower()
if weather == "sunny":
    print(f"{Fore.YELLOW}I love the sunny weather! It is the perfect time to play outside.")
elif weather == "rainy":
    print(f"{Fore.BLUE}Rainy weather might not be the best for playing outside, but it looks so beautiful when everything is green.")  
elif weather == "windy":
    print(f"{Fore.LIGHTBLUE_EX}Windy weather is great for flying kites. It is truly beutiful to see all thouse kite flying around the air") 
elif weather == "snowy":
    print(f"{Fore.WHITE}Snowy weather is perfect for building a snowman or enjoying hot chocolate indoors.")
else:
    print("I’m not sure about that kind of weather.I hope you enjoy your day whatever the weather.")

print(Style.RESET_ALL)
print(" I hope you are enjoying the",weather,"day.Have a nice day",name)



