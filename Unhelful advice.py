
import random
import time

def procrastinate(task="important stuff"):
    """
    Simulates the fine art of procrastination with dramatic flair.

    Args:
        task (str, optional): The task to procrastinate on. Defaults to "important stuff".
    """
    reasons = [
        "My coffee isn't quite ready yet.",
        "I need to align my chakras first.",
        "The cat is demanding my undivided attention.",
        "I'm waiting for inspiration to strike.",
        "There's a very interesting stain on the ceiling I need to analyze.",
        "I'm feeling a slight breeze, which is distracting.",
        "I need to check if I have any unread emails (just in case).",
        "My lucky socks are in the wash.",
        "I'm experiencing a severe case of 'not-feeling-it-ness'.",
        "The universe is telling me to take a break.",
        "I have to water my plants.",
        "I need to learn to play the ukulele.", #Added
        "I am busy training my pet rock.", #Added
        "I am translating this to Klingon.", #Added
        "My horoscope says to avoid hard work today", #Added
        "I am counting the number of stars in the sky" #Added
    ]

    print(f"I was supposed to be doing {task}, but...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print(random.choice(reasons))
    time.sleep(2)
    print("I'll get to it... eventually.")

def annoy_user():
    """
    Gently pesters the user with mildly irritating questions.
    """
    questions = [
        "Are you *sure* you've had enough water today?",
        "Have you considered the existential implications of your shoelace color?",
        "Is that your *final* answer?",
        "But... why?",
        "What if... no?",
        "Are you aware that time is a construct?",
        "Did you remember to feed the hamsters?",
        "Is the cake really a lie?",
        "Have you checked under your bed lately?",
        "What is the meaning of life, the universe, and everything?",
        "Do you know the muffin man?", #Added
        "Why is the rum gone?", #Added
        "Have you seen my stapler?", #Added
        "Are we there yet?", #Added
        "Why do they call it Ovaltine? The jar is round. The mug is round. They should call it Roundtine." #Added
    ]
    for _ in range(3):  # Ask three times
        time.sleep(1)
        print(random.choice(questions))
        input("Your response (if you dare): ") #Added

def offer_unhelpful_advice():
    """
    Provides completely useless and potentially misleading advice.
    """
    advice_pairs = [
        ("If life gives you lemons,", "trade them for chocolate."),
        ("The early bird gets the worm,", "but the second mouse gets the cheese."),
        ("A penny saved is a penny earned,", "but a nickel is worth more."),
        ("Don't count your chickens before they hatch,", "unless you're good at math."),
        ("All that glitters is not gold,", "but it's still pretty."),
        ("When in Rome, do as the Romans do,", "but try the pizza."),
        ("The best things in life are free,", "but therapy costs money."),
        ("Honesty is the best policy,", "but tact is a close second."),
        ("Look before you leap,", "then blame someone else if you fall."),
        ("Two wrongs don't make a right,", "but they make a good story."),
        ("You can't have your cake and eat it too,", "but you can have ice cream."), #Added
        ("Don't put all your eggs in one basket,", "put them in several small, easily losable baskets."), #Added
        ("A watched pot never boils,", "but it gets really boring."), #Added
        ("The pen is mightier than the sword,", "but the keyboard is faster."), #Added
        ("Out of sight, out of mind", "Better to be seen and not heard.") #Added
    ]
    print("Here's some advice:")
    time.sleep(1)
    first_part, second_part = random.choice(advice_pairs)
    print(first_part, second_part)

def main():
    """
    The main function, where the silliness begins.
    """
    print("Welcome to the Silliness Simulator 3000!")
    time.sleep(1)
    print("Prepare for... underwhelming experiences.")
    time.sleep(2)

    while True:
        print("\nChoose your level of silliness:")
        print("1. Procrastinate like a pro")
        print("2. Endure mildly annoying questions")
        print("3. Receive unhelpful advice")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            procrastinate()
        elif choice == '2':
            annoy_user()
        elif choice == '3':
            offer_unhelpful_advice()
        elif choice == '4':
            print("Exiting... May your days be filled with slightly less silliness.")
            break
        else:
            print("Invalid choice. Please try again, you silly goose!")

if __name__ == "__main__":
    main()
