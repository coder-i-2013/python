import colorama
from colorama import Fore, Style
from textblob import TextBlob

positive=0
negative=0
neutral=0

colorama.init()
print(Fore.CYAN)
name = input(f"{Fore.MAGENTA}Please enter your name:{Style.RESET_ALL}")
if not name:
    name = "Mystery"
conversation_history = []

print(f"\n{Fore.CYAN}Hello, agent", name, "!")
print(f"Type a sentence and I will analyze your sentences with TextBlob and show you the sentiment.")
print(f"Type{Fore.YELLOW}'exit'{Fore.CYAN}to quit and view the amoutn of texts you have gotten{Style.RESET_ALL}\n")

while True:
    user_input = input(f"{Fore.GREEN}>>{Style.RESET_ALL}").strip()
    if not user_input:
        print(f"{Fore.RED}Please enter some text or valid command{Style.RESET_ALL}")
        continue
    if user_input.lower() == "exit":
        print(f"\n{Fore.BLUE}Exiting Sentiment Spy. Farewell Agent {name}!{Style.RESET_ALL}")
        print(f"{Fore.RED}The amount of NEGATIVE texts you have gotten is",negative)
        print(f"{Fore.GREEN}\nThe amount of POSITIVE texts you have gotten is",positive)
        print(f"{Fore.YELLOW}\nThe amount of NEUTRAL texts you have gotten is",neutral)
        break
    polarity = TextBlob(user_input).sentiment.polarity
    if polarity > 0.25:
        positive=positive+1
        sentiment_type = "Positive"
        color = Fore.GREEN
        emoji = ""
    elif polarity < -0.25:
        negative=negative+1
        sentiment_type = "Negative"
        color = Fore.RED
        emoji = ""
    else:
        neutral=neutral+1
        sentiment_type = "Neutral"
        color = Fore.YELLOW
        emoji = ""

    conversation_history.append((user_input, polarity, sentiment_type))
    print(f"{color}{emoji}{sentiment_type} sentiment detected\nPolarity: {polarity:.2f}{Style.RESET_ALL}")
