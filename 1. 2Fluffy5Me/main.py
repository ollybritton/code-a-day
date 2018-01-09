#coding=utf-8
import time, os, sys, random
from datetime import datetime

class Random:
    def __init__(self):
        pass
    
    def integer(self, a, b):
        return random.randint(a, b)
        
    def choice(self, xs):
        return random.choice(xs)
        
    def name(self):
        names = ["Bubbles", "Bundles", "Bunny", "Buttercup", "Button", "Chipmunk", "Cinnamon", "Cuddles", "Daisy", "Dimples", "Hiccup", "Huggie", "Jellybean", "Jiggles ", "Jujube ", "Kitkat", "Lollipop ", "Marshmallow ", "Munchkin", "Nibbles", "Nugget", "Panda", "Peaches ", "Pickles", "Pixie ", "Pocket", "Schmoopy ", "Skittles ", "Snickers ", "Snowball", "Snuggles ", "Squiggle ", "Taffy", "Teacup", "Tipsy", "Twinkles", "Velvet", "Waffles", "Wiggles", "Winky", "Bambi", "Barbie", "Blossom", "Bluebell", "Calypso", "Cookie", "Cuddles", "Cupcake", "Daisy", "Electra", "Giggles", "Ginger", "Goldilocks", "Gumdrop", "Honeybee", "Jasmine", "Juliette", "Juniper", "Ladybug", "Lakshmi", "Misty", "Nutmeg", "Olympia", "Princess", "Ruby", "Tiara", "Tinkerbell", "Trixie", "Twinkle", "Venus", "Amigo", "Banjo", "Cosmo", "Crocket", "Donatello", "Electro", "Elvis", "Euripides", "Figaro", "Fonzie", "Galileo", "Geronimo", "Hendrix", "Hercules", "Hobbes", "Houdini", "Lancelot", "Mars", "Moses", "Ozzy", "Pharaoh", "Picasso", "Prince", "Rembrandt", "Romeo", "Rumi", "Simba", "Tarzan", "Wizard", "Zorro"]
        
        return self.choice(names)
        
    def mood(self):
        return 5 + self.integer(-2, 2)
        
    def health(self):
        return 9 + self.integer(-1, 1)
        
    def personality(self):
        activities = ["Pet", "Groom", "Clean", "Walk", "Go to the Park", "Dress Up", "Brush", "Listen to Music", "Take a Catnap", "Bird Watch", "Travel", "Zen Out", "Go Camping", "High-Five", "Watch TV", "Go to Work", "Chill Out"]
        
        likes = []
        hates = []        
        
        for i in range(6):
            a = self.choice(activities)
            likes.append(a)
            
            del activities[activities.index(a)]
            
            
        for i in range(6):
            a = self.choice(activities)
            hates.append(a)
            
            del activities[activities.index(a)]
            
        passive = activities
        
        return {
            "likes": likes,
            "hates": hates,
            "passive": passive
        }
        
def clear():
    os.system("clear")
    
def sleep(amount):
    time.sleep(amount)

class Creature:
    def __init__(self, name, mood, health, personality):
        self.name = name
        self.mood = mood
        self.health = health
        
        self.personality = personality
        self.likes = personality["likes"]
        self.hates = personality["hates"]
        self.passive = personality["passive"]
        
        
    def evaluate(self, activity):
        if activity in self.likes:
            self.mood += Random.integer(1, 2)
            
        elif activity in self.hates:
            self.mood -= Random.integer(1, 2)
            
    def hp(self):
        return "♥"*self.health
        
    def mood_counter(self):
        return "✓"*self.mood + "✖"*(10 - self.mood)
            

class Util:
    def hp(self, amount):
        return "♥"*amount
    
    def health(self, amount):
        if amount < 0:
            phrases = ["You have killed your cat. It is dead. If it were alive now, I bet it would have choice words for you, young man. You should feel bad.", "...I'm not sure how to break it to you... but you've killed your cat.", "Your cat is now deader that the relationship you had with it."]
            
            print(Random.choice(phrases) + " (Press enter to accept fate and end game)", end = "")
            input()
            
            sys.exit()
        
            
        elif amount == 1:
            phrases = ["Your cat is on the brink of death.", "Your cat is very close to dying.", "Your cat sits on the edge of life and death. One final push could could knock it either way."]
            
        elif amount == 2:
            pass
            
        elif amount == 3:
            pass
            
        elif amount == 4:
            pass
            
        elif amount == 5:
            pass
            
        elif amount == 6:
            pass
            
        elif amount == 7:
            pass
            
        elif amount == 8:
            pass
            
        elif amount == 9:
            pass
            
        elif amount == 10:
            pass
            
        elif amount > 10:
            pass    
       

def intro():
    while True:
        clear()
        print("██████╗ ███████╗██╗     ██╗   ██╗███████╗███████╗██╗   ██╗███████╗███╗   ███╗███████╗\n╚════██╗██╔════╝██║     ██║   ██║██╔════╝██╔════╝╚██╗ ██╔╝██╔════╝████╗ ████║██╔════╝\n █████╔╝█████╗  ██║     ██║   ██║█████╗  █████╗   ╚████╔╝ ███████╗██╔████╔██║█████╗  \n██╔═══╝ ██╔══╝  ██║     ██║   ██║██╔══╝  ██╔══╝    ╚██╔╝  ╚════██║██║╚██╔╝██║██╔══╝  \n███████╗██║     ███████╗╚██████╔╝██║     ██║        ██║   ███████║██║ ╚═╝ ██║███████╗\n╚══════╝╚═╝     ╚══════╝ ╚═════╝ ╚═╝     ╚═╝        ╚═╝   ╚══════╝╚═╝     ╚═╝╚══════╝")
        print("Hello and Welcom to 2Fluffy5Me, a cat simulator for lonely people! (Press <ENTER> to continue) ", end = "")
        input()
        
        print("(Full Disclaimer: I don't have a cat, and have no idea what it's like)")
        print("--------\n")
        
        print("Anyway, shall we start? [Y]es, [n]o, [m]eow: ", end = "")
        start_bool = input().lower()
        
        if start_bool == "yes" or start_bool == "y" or start_bool == "":
            print("Puuuurrrrrfect! Let's get going! (Press <ENTER> to continue) ", end = "")
            input()
            break
            
        elif start_bool == "meow" or start_bool == "m":
            print("Claw-some! I see you're getting into the persona! Let's get ready to rumble! (Press <ENTER> to continue) ", end = "")
            input()
            break
            
        elif start_bool == "no" or start_bool == "n":
            print("Uhhhh wut? You start again and give me the CORRECT answer. (Press <ENTER> to continue) ", end = "")
            input()
    
    
def main():
    clear()
    
    r = Random()
    cat =  Creature(r.name(), r.mood(), r.health(), r.personality())
    
    inital_like = r.choice(cat.likes)
    inital_hate = r.choice(cat.hates)
    initial_passive = r.choice(cat.passive)
    
    known_likes = [inital_like]
    known_hates = [inital_hate]
    known_passive = [initial_passive]
    
    times = []
    
    print("Ok! Your cat has been generated! (Press <ENTER> to continue) ", end = "")
    input()
    
    print("Meet {}, your lovely cat!".format(cat.name) + " (Press <ENTER> to continue) ", end = "")
    input()
    
    print("Here's a breakdown:")
    print("Health: {}".format(cat.hp()))
    print("Mood: {}".format(cat.mood_counter()))
    
    print("")
    
    print("Likes: {}".format( ", ".join( list( map( lambda x: "to " + x, known_likes ) ) ) ))
    print("Hates: {}".format( ", ".join( list( map( lambda x: "to " + x, known_hates ) ) ) ))
    print("Doesn't Mind: {}".format( ", ".join( list( map( lambda x: "to " + x, known_passive ) ) ) ))
    print("(Press enter to continue) ", end = "")
    input()
    
    print("")
    
    print("Ok! Have fun you two! (Press enter to continue) ", end = "")
    input()
    
    while cat.health > 0:
        clear()
        
        try:
            # Has the program been left for more than a minute?
            if (times[-2] - times[-1]).total_seconds() > 60:
                cat.health -= 1
                
        except:
            pass
            
        if cat.mood == 2:
            # Cats with mood 2 or lower self harm every turn.
            cat.health -= 1
            
        elif cat.mood == 1:
            cat.health -= 2
            
        elif cat.mood <= 0:
            print("Cat: Meow meow meow!")
            print("Cat (Translated): I'm tired of your sh*t! I'm f**king leaving! Bye b*tch!")
            print("(Press enter to accept your rejection) ", end = "")
            input()
            
            sys.exit()
            
        
        print("Your cat:")
        print("Health: {}".format(cat.hp()))
        print("Mood: {}".format(cat.mood_counter()))
        
        print("")
        
        print("Discovered personality:")
        print("Likes: {}".format( ", ".join( list( map( lambda x: "to " + x, known_likes ) ) ) ))
        print("Hates: {}".format( ", ".join( list( map( lambda x: "to " + x, known_hates ) ) ) ))
        print("Doesn't Mind: {}".format( ", ".join( list( map( lambda x: "to " + x, known_passive ) ) ) ))
        
        print("")
        print("----------")
        print("")
        print("Actions:")
        print("[F]eed: Feed your cat, both to keep it's mood up and not kill it.")
        print("[P]erform Activity: Perform an activity with your cat.")
        print("[H]elp/Guide: Read the help or guide on the game.")
        
        print("")
        
        action = input("What would you like to do? ").lower()
        print("")
        
        if action == "feed" or action == "f":
            phrases = ["Yum! That sure was delicous!", "Mhmmmm...", "That was puuuurrrrrfect!", "That was meownificient!"]
            print("Cat: Meow meow... meow.")
            print("Cat (Translated): {}".format(r.choice(phrases)))
            times.append(datetime.utcnow())
            
            print("\n(Press enter to continue)", end = "")
            input()
            
        elif action == "perform" or action == "activity" or action == "p" or action == "a":
            activities = ["Pet", "Groom", "Clean", "Walk", "Go to the Park", "Dress Up", "Brush", "Listen to Music", "Take a Catnap", "Bird Watch", "Travel", "Zen Out", "Go Camping", "High-Five", "Watch TV", "Go to Work", "Chill Out"]
            
            print("Ok, these are the activities you can go on!")
            print("[1] Pet: Pet the cat.")
            print("[2] Groom: Pet the cat.")
            print("[3] Clean: Pet the cat.")
            print("[4] Walk: Pet the cat.")
            print("[5] Go to the Park: Pet the cat.")
            print("[6] Dress Up: Pet the cat.")
            print("[7] Brush: Pet the cat.")
            print("[8] Listen to Music: Pet the cat.")
            print("[9] Take a Catnap: Pet the cat.")
            print("[10] Bird Watch: Pet the cat.")
            print("[11] Travel: Pet the cat.")
            print("[12] Zen: Pet the cat.")
            print("[13] Go Camping: Pet the cat.")
            print("[14] High-Five: Pet the cat.")
            print("[15] Watch TV: Pet the cat.")
            print("[16] Go to Work: Pet the cat.")
            print("[17] Chill Out: Pet the cat.")
            
            print("")
            print("You know that these are the things your cat likes:")
            print("Likes: {}".format( ", ".join( list( map( lambda x: "to " + x, known_likes ) ) ) ))
            print("Hates: {}".format( ", ".join( list( map( lambda x: "to " + x, known_hates ) ) ) ))
            print("Doesn't Mind: {}".format( ", ".join( list( map( lambda x: "to " + x, known_passive ) ) ) ))
            
            print("However, if you experiment, you get a FIRST TIME MOOD BONUS! YEEEEAAAAA!")
            
            print("")
            
            activity_number = int(input("What activity would you like to perform (type the number)? ").lower())
            
            if activity_number == 1:
                # Pet
                curr = activities[activity_number - 1]
                
                print("You have chosen: Petting")
                print("(Press enter to continue) ", end = "")
                input()
                print("")
                
                luck = r.integer(0, 10)
                modifier = 0
                
                if (not curr in known_hates) and (not curr in known_hates) and (not curr in known_hates):
                    # FIRST TIME BONUS WOO
                    modifier += 1
                
                if curr in cat.hates and (not curr in known_hates):
                    # Is hated, but doesn't know it.
                    known_hates.append(curr)
                    
                    phrases = ["Straight away, you realise {} hates this.", "All of a sudden, you realise this was a rubbish idea.", "As soon as you start, you notice a sudden shift in {} liking toward you. In a bad way. A vey bad way.", "Huh. {} hates this.", "You get a sudden scowl from {}."]
                    
                    print(r.choice(phrases).format(cat.name))
                    
                    modifier -= r.integer(1, 2)
                    
                elif curr in cat.hates and curr in known_hates:
                    # Is hated, and totally knows it.
                    phrases = ["You already knew {} hated this. You horrible human being.", "You horrible, horrible human being.", "Forcing you cat to do something it doesn't like? You horrible person."]
                    
                    print(r.choice(phrases).format(cat.name))
                    
                    modifier -= 2
                    
                elif curr in cat.likes and (not curr in known_likes):
                    # Is liked, but doesn't know it.
                    known_likes.append(curr)
                    
                    phrases = ["This seems to bring {} joy like no other activity you've seen before.", "This is like heaven for {}. They really like you now."]
                    
                    print(r.choice(phrases).format(cat.name))
                    
                    modifier += r.integer(1, 3)
                    
                elif curr in cat.likes and curr in known_likes:
                    # Is liked, and knows it.
                    phrases = ["Like always. this is so much fun for {}.", "Once again, {} loves this.", "This brings the same feeling of joy both to you and {}."]
                    
                    print(r.choice(phrases).format(cat.name))
                    
                    modifier += r.integer(1, 2)
                    
                elif curr in cat.passive and (not curr in known_passive):
                    # Is passive, but doesn't know it.
                    phrases = ["This seems very... normal for {}.", "{} doesn't mind this.", "{} shows no emotion whatsoever."]
                    
                    print(r.choice(phrases).format(cat.name))
                    
                elif curr in cat.passive and curr in known_passive:
                    # Is passive, and knows it.
                    phrases = ["Being mundane today are we?", "Like normal, this is normal.", "Once again, {} doesn't mind this.", "Like always, {} shows no emotion.", "As always, this is very normal for {}."]
                    
                    print(r.choice(phrases).format(cat.name))
                    
                print("(Press enter to continue) ", end = "")
                input()
                print("")
                
                
                luck = luck + modifier
                
                if luck <= 0:
                    print("In a freak petting accident, you manage to crush {}'s spine. It is not a nice look, and with a short breath and one final 'meow' before falling unconscious, you feel a sense of a not anger, but disapointment flood through you.")
                    print("(Press enter to continue) ", end = "")
                    input()
                    
                    print("")
                    
                    print("After an emergency trip to the vet, your cat hates your guts. Badly. It destests you.")
                    print("(Press enter to continue) ", end = "")
                    input()
                    
                    cat.health -= 3
                    cat.mood -= 4
                    
                    continue
                    
                    
                elif luck == 1:
                    print("Instead of petting, you manage to slip and firmly press down on the cat's body, causing its legs to collapase, forcing it the ground. You get the sense it will be alright, but it hurt more emotionally.")
                    print("(Press enter to continue) ", end = "")
                    input()
                    
                    print("")
                    
                    print("After a while, it begins to recover. It isn't that hurt, but it probably hates you now.")
                    print("(Press enter to continue) ", end = "")
                    input()
                    
                    cat.health -= 2
                    cat.mood -= 3
                    
                    continue
                
                    
                    
                elif luck in [2, 3, 4]:
                    print("You pet a little too hard, and accidentally firmly slap it. {} quickly jumps away.".format(cat.name))
                    print("(Press enter to continue) ", end = "")
                    input()
                    
                    print("")
                    
                    print("After some time has passed, you get the idea that things weren't what they once were.")
                    print("(Press enter to continue) ", end = "")
                    input()
                    
                    cat.health -= 1
                    cat.mood -= 2
                    
                    continue
                    
                    
                elif luck == 5:
                    print("The petting is OK, but a little hard at times. It doesn't mind it.")
                    print("(Press enter to continue) ", end = "")
                    input()
                    
                    cat.health -= 0
                    cat.mood -= 0
                    
                    continue
                    
                    
                elif luck in [6, 7]:
                    print("The petting was pretty good, and you both enjoyed the experince.")
                    print("(Press enter to continue) ", end = "")
                    input()
                    
                    
                    cat.health += 0
                    cat.mood += 1 
                    
                    continue
                    
                    
                    
                elif luck == 8:
                    print("That was some awesome petting. You especially rembered the part where you petted it very well. As well as being happier, the cat seems pyhsically and mentally healed.")
                    print("(Press enter to continue) ", end = "")
                    input()
                    
                    
                    cat.health += 1
                    cat.mood += 2
                    
                    continue
                    
                    
                elif luck == 9:
                    print("That was some PRO level petting. You shared an intimate moment together, and feel as if your previous relationship has now flowered into something wonderous and beautiful.")
                    print("(Press enter to continue) ", end = "")
                    input()
                    
                    
                    cat.health += 2
                    cat.mood += 3
                    
                    continue
                    
                    
                elif luck >= 10:
                    print("Before you even start petting, you know this is gonna be reaally, reaaallllyyy good petting. You feel energised, rivatalised, almost as if God himself has shone down a holy blessing of love into your fingertips.")
                    print("(Press enter to continue) ", end = "")
                    input()
                    
                    print("")
                    
                    print("You notice a distinct shift in the way {} looks and moves, almost as if the petting it recieved flowed through it like happiness and life flows through you upon seeing a loved one. It's truly amazing.".format(cat.name))
                    print("(Press enter to continue) ", end = "")
                    input()
                    
                    cat.health += 4
                    cat.mood += 5
                    
                    continue
                    
                            
                
            elif activity_number == 2:
                # Groom
                print("You have chosen: Grooming")

                
            elif activity_number == 3:
                # Clean
                print("You have chosen: Cleaning")

                
            elif activity_number == 4:
                # Walk
                print("You have chosen: Walking")

                
            elif activity_number == 5:
                # Go to Park
                print("You have chosen: Going to the Park")

                
            elif activity_number == 6:
                # Dress Up
                print("You have chosen: Dressing Up")

                
            elif activity_number == 7:
                # Brush
                print("You have chosen: Brushing")

                
            elif activity_number == 8:
                # Listen to Music
                print("You have chosen: Listening to Music")

                
            elif activity_number == 9:
                # Take a Catnap
                print("You have chosen: Taking a Catnap")

                
            elif activity_number == 10:
                # Bird Watch
                print("You have chosen: Bird Watch")

                
            elif activity_number == 11:
                # Travel
                print("You have chosen: Travelling")

                
            elif activity_number == 12:
                # Zen
                print("You have chosen: Zenning")

                
            elif activity_number == 13:
                # Go Camping
                print("You have chosen: Camping")

                
            elif activity_number == 14:
                # High-Five
                print("You have chosen: High-Fiving")

                
            elif activity_number == 15:
                # Watch TV
                print("You have chosen: Watching TV")

                
            elif activity_number == 16:
                # Go to Work
                print("You have chosen: Going to Work")

                
            elif activity_number == 17:
                # Chill Out
                print("You have chosen: Chilling Out")

                
            
            
            
            
        elif action == "help" or action == "guide" or action == "h" or action == "g":
            pass # for now
        
        
    phrases = ["You have killed your cat. It is dead. If it were alive now, I bet it would have choice words for you, young man. You should feel bad.", "...I'm not sure how to break it to you... but you've killed your cat.", "Your cat is now deader that the relationship you had with it."]
    
    print(r.choice(phrases))
    
    
if __name__ == "__main__":
    #intro()
    main()