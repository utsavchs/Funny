
# prompt: ask what color the user likes. if entered pink, yellow or any other color from red, blue, orange, print, you are a female. if entered red, blue or orange say you are a male. Any other color entered, say you are alien.

color = input("What is your favorite color? ")

if color.lower() == "pink" or color.lower() == "yellow":
  print("You are a female.")
elif color.lower() in ["red", "blue", "orange"]:
    print("You are a male.")
else:
  print("You are an alien.")
