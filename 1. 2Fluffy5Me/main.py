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
            
            activity_number = input("What activity would you like to perform (type the number)? ").lower()
            
            if activity_number == 1:
                pass
                
            elif activity_number == 2:
                pass
                
            elif activity_number == 3:
                pass
                
            elif activity_number == 4:
                pass
                
            elif activity_number == 5:
                pass
                
            elif activity_number == 6:
                pass
                
            elif activity_number == 7:
                pass
                
            elif activity_number == 8:
                pass
                
            elif activity_number == 9:
                pass
                
            elif activity_number == 10:
                pass
                
            elif activity_number == 11:
                pass
                
            elif activity_number == 12:
                pass
                
            elif activity_number == 13:
                pass
                
            elif activity_number == 14:
                pass
                
            elif activity_number == 15:
                pass
                
            elif activity_number == 16:
                pass
                
            elif activity_number == 17:
                pass
                
            
            
            
            
        elif action == "help" or action == "guide" or action == "h" or action == "g":
            pass # for now
        
        
    phrases = ["You have killed your cat. It is dead. If it were alive now, I bet it would have choice words for you, young man. You should feel bad.", "...I'm not sure how to break it to you... but you've killed your cat.", "Your cat is now deader that the relationship you had with it."]
    
    print(r.choice(phrases))
    
    
if __name__ == "__main__":
    #intro()
    main()