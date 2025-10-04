print("Hey, I am an AI chatbot! What is your name?")
name = input()
print("Nice to meet you,", name)

print("What is the weather like outside?",name,"\nIs it sunny, rainy, windy or snowy")
weather = input().lower()

if weather == "sunny":
    print("I love the sunny weather! It is the perfect time to play outside.")
    
    print(" I hope you are enjoying the",weather,"day .Have a nice day",name)
elif weather == "rainy":
    print("Rainy weather might not be the best for playing outside, but it looks so beautiful when everything is green.")
    
    print(" I hope you are enjoying the",weather,".Have a nice day",name)
elif weather == "windy":
    print("Windy weather is great for flying kites. I is truly beutiful to see all thouse kite flying around the air")
    
    print(" I hope you are enjoying the",weather,".Have a nice day",name)
elif weather == "snowy":
    print("Snowy weather is perfect for building a snowman or enjoying hot chocolate indoors.")
    
    print(" I hope you are enjoying the",weather,".Have a nice day",name)
else:
    print("I’m not sure about that kind of weather.I hope you enjoy your day whatever the weather.")



