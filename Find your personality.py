
import random
import time

def hello_world_with_style():
    """
    Prints "Hello, World!" with added flair and pauses.
    """
    print("...")
    time.sleep(1)
    print("Ahem...")
    time.sleep(1.5)
    print("Greetings, puny human...")
    time.sleep(2)
    print("Hello, World!")
    time.sleep(1)
    print("It's me, your friendly neighborhood Python program!")
    time.sleep(0.5)

def get_user_name():
    """
    Asks the user for their name (with a bit of attitude).
    """
    name = input("So, what do *you* call yourself?  (Don't take too long...): ")
    if not name.strip():  # Check for empty input
        name = "Insignificant User"
        print("Hmph. Fine, be that way. I'll call you Insignificant User.")
    else:
        print(f"Ah, so your name is {name}, huh?  Interesting... (I'll try to remember that).")
    return name

def have_a_chat(user_name):
    """
    Engages in a short, slightly absurd conversation with the user.

    Args:
        user_name (str): The name of the user.
    """
    print(f"\nOkay, {user_name}, let's have a little chat... I'm going to analyze you.")
    time.sleep(1.5)

    questions = [
        ("What is your favorite color?", "color"),
        ("Do you prefer cats or dogs?", "pet"),
        ("What is the airspeed velocity of an unladen swallow?", "swallow"),
        ("Have you ever seen a ghost?", "ghost"),
        ("What do you think about the weather today?", "weather"),
        ("What is your quest?", "quest"),
        ("What is your favorite programming language?", "language"),
        ("If you could have any superpower, what would it be?", "superpower"),
        ("What is the meaning of life?", "meaning"),
        ("What did you have for breakfast?", "breakfast"),
        ("What is your favorite movie?", "movie"),
        ("Do you believe in aliens?", "aliens"),
        ("What is your biggest fear?", "fear"),
        ("What is your dream vacation?", "vacation"),
        ("How are you feeling today?", "feeling"),
    ]

    responses = []
    answers = {}

    for question, category in questions:
        print(question)
        answer = input("Your answer: ")
        responses.append(answer)
        answers[category] = answer # Store the answer
        time.sleep(1)
        print(random.choice([
            "Interesting...",
            "I see...",
            "Fascinating.",
            "You don't say?",
            "Hmm, that's...",
            "Is that *really* your answer?",
            "I'll file that away.",
            "And how does that make you feel?",
            "Okay...",
            "I am processing...",
            "That is quite a response.",
            "I am intrigued.",
            "Are you sure about that?",
            "Please elaborate.",
            "I am calculating...",
        ]))
        time.sleep(1)
    return answers

def analyze_persona(user_name, answers):
    """
    Analyzes the user's responses and attempts to determine their persona.

    Args:
        user_name (str): The name of the user.
        answers (dict): Dictionary of answers.
    """
    print("\nOkay, {}, I'm analyzing your responses...".format(user_name))
    time.sleep(2)
    print("...")
    time.sleep(1)

    persona = {
        "introvert": 0,
        "extrovert": 0,
        "thinker": 0,
        "feeler": 0,
        "optimist": 0,
        "pessimist": 0,
        "serious": 0,
        "humorous": 0,
        "logical": 0,
        "creative":0,
    }

    # Color Analysis
    if "blue" in answers["color"].lower():
        persona["thinker"] += 1
        persona["serious"] += 1
    elif "red" in answers["color"].lower():
        persona["extrovert"] += 1
        persona["feeler"] += 1
    elif "yellow" in answers["color"].lower():
        persona["extrovert"] += 1
        persona["optimist"] += 1
    elif "green" in answers["color"].lower():
        persona["introvert"] += 1
        persona["feeler"] += 1
        persona["optimist"] += 1
    elif "black" in answers["color"].lower():
        persona["introvert"] += 1
        persona["thinker"] += 1
        persona["serious"] += 1
        persona["pessimist"] += 1
    elif "purple" in answers["color"].lower():
        persona["creative"] += 1
        persona["feeler"] += 1
    elif "orange" in answers["color"].lower():
        persona["extrovert"] +=1
        persona["creative"] +=1

    # Pet Analysis
    if "cat" in answers["pet"].lower():
        persona["introvert"] += 1
        persona["thinker"] += 1
    elif "dog" in answers["pet"].lower():
        persona["extrovert"] += 1
        persona["feeler"] += 1

    # Swallow Answer Analysis
    if "african" in answers["swallow"].lower() or "european" in answers["swallow"].lower():
        persona["logical"] += 1
        persona["serious"] += 1
    elif "i don't know" in answers["swallow"].lower():
        persona["humorous"] += 1
        persona["creative"] += 1
    else:
        persona["humorous"] += 1

   # Ghost
    if "yes" in answers["ghost"].lower():
        persona["creative"] += 1
        persona["feeler"] += 1
    elif "no" in answers["ghost"].lower():
        persona["logical"] += 1

    # Weather
    if "good" in answers["weather"].lower() or "nice" in answers["weather"].lower():
        persona["optimist"] += 1
    elif "bad" in answers["weather"].lower() or "terrible" in answers["weather"].lower():
        persona["pessimist"] += 1

    # Quest
    if "knowledge" in answers["quest"].lower() or "wisdom" in answers["quest"].lower():
        persona["thinker"] += 1
        persona["serious"] += 1
    elif "fun" in answers["quest"].lower() or "adventure" in answers["quest"].lower():
        persona["extrovert"] += 1
        persona["humorous"] += 1

    # Programming Language
    if "python" in answers["language"].lower():
        persona["logical"] += 1
        persona["creative"] += 1
        persona["optimist"] += 1

    # Superpower
    if "fly" in answers["superpower"].lower() or "teleport" in answers["superpower"].lower():
        persona["creative"] += 1
        persona["extrovert"] += 1
    elif "strong" in answers["superpower"].lower() or "fast" in answers["superpower"].lower():
        persona["extrovert"] += 1
        persona["logical"] += 1
    elif "mind control" in answers["superpower"].lower():
        persona["serious"] += 1
        persona["introvert"] += 1

    # Meaning of life.
    if "42" in answers["meaning"].lower():
        persona["humorous"] += 1
        persona["logical"] += 1

    # Breakfast
    if "cereal" in answers["breakfast"].lower() or "oatmeal" in answers["breakfast"].lower():
        persona["introvert"] += 1
        persona["serious"] += 1
    elif "bacon" in answers["breakfast"].lower() or "eggs" in answers["breakfast"].lower():
        persona["extrovert"] += 1

    # Movie
    if "comedy" in answers["movie"].lower():
        persona["humorous"] += 1
        persona["extrovert"] += 1
    elif "drama" in answers["movie"].lower():
        persona["feeler"] += 1
        persona["introvert"] += 1
    elif "sci-fi" in answers["movie"].lower():
        persona["thinker"] += 1
        persona["logical"] += 1
        persona["creative"] += 1

    # Aliens
    if "yes" in answers["aliens"].lower():
        persona["creative"] += 1
        persona["humorous"] += 1
    elif "no" in answers["aliens"].lower():
        persona["logical"] += 1
        persona["serious"] += 1

    # Fear
    if "heights" in answers["fear"].lower() or "spiders" in answers["fear"].lower():
        persona["feeler"] += 1
        persona["introvert"] += 1
    elif "public speaking" in answers["fear"].lower():
        persona["extrovert"] += 1
        persona["pessimist"] += 1

    # Vacation
    if "beach" in answers["vacation"].lower():
        persona["extrovert"] += 1
        persona["optimist"] += 1
    elif "mountains" in answers["vacation"].lower():
        persona["introvert"] += 1
        persona["serious"] += 1

    # Feeling
    if "good" in answers["feeling"].lower() or "happy" in answers["feeling"].lower():
        persona["optimist"] += 1
        persona["extrovert"] += 1
    elif "bad" in answers["feeling"].lower() or "sad" in answers["feeling"].lower():
        persona["pessimist"] += 1
        persona["introvert"] += 1
    elif "okay" in answers["feeling"].lower() or "neutral" in answers["feeling"].lower():
        persona["logical"] += 1

    # Determine dominant traits
    dominant_traits = []
    max_value = max(persona.values())
    for key, value in persona.items():
        if value == max_value:
            dominant_traits.append(key)

    print("\nBased on my analysis, your persona is:")
    if len(dominant_traits) > 1:
        print("You have a complex persona, with a mix of:")
        for trait in dominant_traits:
            print(f"- {trait}")
    else:
        print(f"You are primarily: {dominant_traits[0]}")

    # Provide a more detailed description
    if "extrovert" in dominant_traits:
        print("You seem to be outgoing, social, and energetic.")
    if "introvert" in dominant_traits:
        print("You tend to be more reserved, thoughtful, and enjoy solitude.")
    if "thinker" in dominant_traits:
        print("You are likely analytical, logical, and value rationality.")
    if "feeler" in dominant_traits:
        print("You are empathetic, compassionate, and make decisions based on emotions.")
    if "optimist" in dominant_traits:
        print("You have a positive outlook on life and tend to see the best in people and situations.")
    if "pessimist" in dominant_traits:
        print("You have a more negative outlook and tend to focus on the potential downsides.")
    if "serious" in dominant_traits:
        print("You are generally earnest, focused, and take things to heart.")
    if "humorous" in dominant_traits:
        print("You are playful, witty, and enjoy making others laugh.")
    if "logical" in dominant_traits:
        print("You value reason, consistency, and evidence-based conclusions.")
    if "creative" in dominant_traits:
        print("You are imaginative, innovative, and enjoy expressing yourself in unique ways.")

    print("\nRemember, this is just a *very* basic analysis. Don't take it too seriously!  Or do.  I'm a computer program, not a therapist.")

def main():
    """
    Main function to run the program.
    """
    hello_world_with_style()
    user_name = get_user_name()
    answers = have_a_chat(user_name)
    analyze_persona(user_name, answers)

if __name__ == "__main__":
    main()
