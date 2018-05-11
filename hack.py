import os, time, random
from sys import platform as _platform

# ==================== CONFIG ====================

CMD_CHARACTER = "=>"
TICK = "✓"
CROSS = "✖"

LOGO = " _   _   ___  _____  _   __  _______   __ _____ \n| | | | / _ \/  __ \| | / / |  ___\ \ / /|  ___|\n| |_| |/ /_\ \ /  \/| |/ /  | |__  \ V / | |__  \n|  _  ||  _  | |    |    \  |  __| /   \ |  __| \n| | | || | | | \__/\| |\  \_| |___/ /^\ \| |___ \n\_| |_/\_| |_/\____/\_| \_(_)____/\/   \/\____"

# ==================== GLOABL ====================

DELETED, UNAVAILABLE = [], []

# ==================== HELPER FUNCTIONS ====================

def pr(string):
    print("[hack.exe] " + CMD_CHARACTER + " {}".format(string))

def nested_pr(string, name):
    print("\t[" + name + "] " + CMD_CHARACTER + " " + string)

def cmd(string):
    return input("[hack.exe] {} {} ".format(string, CMD_CHARACTER))

def nested_cmd(string, name):
    return input("\t[{}] {} {} ".format(name, string, CMD_CHARACTER))

def space():
    print("")

def process(t = 0.2):
    time.sleep(t)

def clear():
    if _platform == "linux" or _platform == "linux2":
       os.system("clear")

    elif _platform == "darwin":
       os.system("clear")

    elif _platform == "win32" or _platform == "win64":
       space()
       print("=========================================")
       space()

def loader(string, t = 0.05, interval = [0, 100]):
    for i in range(interval[0], interval[1] + 1):
        pr(string.format(i))
        time.sleep(t)

def logo(procedral = True, t = 0.5, spacing = True):
    global LOGO

    if not procedral:
        if spacing: space()
        print(LOGO)
        if spacing: space()

    else:
        layered_logo = LOGO.split("\n")

        if spacing: space()

        for layer in layered_logo:
            print(layer)
            time.sleep(t)

        if spacing: space()

def is_string(string):
    return True if (string[0] == "\"" or string[0] == "'") and (string[-1] == "\"" or string[-1] == "'") else False

def hacking_method():
    hacking_methods = ["Quantum Key Decryption", "Malware Blockchain Schemes", "A Man-on-the-Side attack", "LI Process Brute-Forcing", "SerialKiller Key Exchange Interception", "HeartBleed Code Intercept", "IBM Watson 'What, Son' Attack"]
    return random.choice(hacking_methods)

def random_name(gender = None):
    if gender == "boy":
        with open("data/boy_names.txt", "r") as f:
            return random.choice(f.readlines())[0:-1]

    elif gender == "girl":
        with open("data/girl_names.txt", "r") as f:
            return random.choice(f.readlines())[0:-1]

    else:
        names = []

        with open("data/girl_names.txt", "r") as f:
            names += f.readlines()

        with open("data/boy_names.txt", "r") as f:
            names += f.readlines()

        return random.choice(names)[0:-1]

def random_password():
    passwords = ["123", "letmein", "abc123", "ihatethisstupidjob", "iwanttodie", "cats", "dogs", "abcdefg", "12345", "hello", "beep", "accessgranted", "loveyoumum"]
    return random.choice(passwords)

# ==================== FUNCTIONS ====================

def login():

    clear()

    usernames = ["admin", "root", "", "hack", "hacker", "hacked", "123", "e';DROP TABLE VERIFIED_USERNAMES--", "a"]
    passwords = ["", "123", "password", "pa$$word", "p@$$word", "p@$$w0rd", "hello", "12345", "abc", "abc123", "admin", "root", "", "hack", "hacker", "hacked", "123", "e';DROP TABLE VERIFIED_USERNAMES--", "a"]

    count = 0

    while True:
        if count == 0:
            pr("Welcome to hack.exe, the complete hacking suite.")
            pr("To prove your hacking abilities, you must hack into this very file.")
            pr("This program has been secured using Python 6 malware encryption, using a form of blockchain to validate private keys. Good luck.")

            space()

        attempted_username = input("[hack.exe] USERNAME: ")
        attempted_password = input("[hack.exe] PASSWORD: ")

        space()
        process()

        if attempted_username in usernames:
            pr("Username: " + TICK)

            process(0.4)

            if attempted_password in passwords:
                pr("Password: " + TICK)

                process(0.3)
                break

            else:
                pr("Password: " + CROSS)

                process(0.3)

        else:
            pr("Username: " + CROSS)
            process(0.4)
            pr("Password: " + CROSS)

        space()

        pr("Ha! Try again.")

        space()

        process(1)

        clear()

        count += 1

    process(1)

    space()

    pr("Oh shiznip! I didn't think you were that good! Here... here's the program: <PRESS ENTER TO LOAD>")
    input()

def program_loading():
    loader("LOADING PROGRAM: {}% Complete...", interval = [0, 99])
    pr("100% Completion.")

    process(1.2)

def hack_command(curr_cmd, head, tail, params):
    # "hack" command - Allows you to hack into any system, anywhere.
    space()

    if params == "":
        pr("ERROR - What to hack has not been specified.")
        pr("        Command Format: hack '[what to hack]'")

    elif not is_string(params):
        pr("ERROR - What to hack is not a string. Please place what to hack in quotes.")
        pr("        Command Format: hack '[what to hack]'")

    else:
        process(1)

        hack_name = params[1:-1]
        pr("Ok, attempting to hack '{}'...".format(hack_name))
        process(1.2)

        pr("Searching for hacking methods...")
        process(3)

        space()

        hack_method = hacking_method()

        pr("Hacking method found: {}".format(hack_method))
        process(0.5)

        space()

        pr("Attempting to execute (1/3)...")
        process(2)

        pr("FAILED!")
        space()

        pr("Attempting to execute (2/3)...")
        process(1.8)

        pr("FAILED!")
        space()

        pr("Attempting to execute (3/3)...")
        process(4)

        pr("Success: Complete root access enabled.")
        process(1)

        pr("Finding open terminal...")
        process(2.5)

        space()

        pr("OPEN TERMINAL FOUND:")
        process(1)

        print("===== STARTING SSH TUNNEL =====")
        process(3.5)

        clear()

        count = 0

        while True:
            space()

            if count == 0: nested_pr("Welcome to the '" + hack_name + "' terminal.", hack_name); space()

            nested_pr("What action would you like to perform?", hack_name)
            space()

            print("\t\t[1] Delete system.")
            print("\t\t[2] Turn off system.")
            print("\t\t[3] Print passwords.")

            space()

            action = int(nested_cmd("Perform", hack_name))

            process()

            if action == 1:
                nested_pr("Ok, strange request admin, but if you say so, ok.".format(hack_name), hack_name)
                process(1.3)

                nested_pr("Deleting the '" + hack_name + "' syst-", hack_name)
                process(4)

                space()

                pr("=== CONNECTION SEVERED ===")

                space()
                process()

                pr("Hack complete.")

                DELETED.append(hack_name)

                break

            elif action == 2:
                nested_pr("Switching off the system.", hack_name)
                process(2.5)

                space()

                pr("=== CONNECTION STOPPED ===")

                space()
                process()

                pr("Hack complete.")

                UNAVAILABLE.append(hack_name)

                break

            elif action == 3:
                while True:
                    magic_word = nested_cmd("What's the magic word?", hack_name)

                    if magic_word == "please":
                        break

                    else:
                        nested_pr("I'm sorry, be more polite please.")
                        process(1)

                        clear()

                space()

                nested_pr("Well since you asked so politely, sure...", hack_name)

                process()
                
                nested_pr("You are acting a bit strange today...", hack_name)

                process(3)

                for _ in range(100):
                    print("\tUsername: '{}', Password: {}".format(random_name(), random_password()))
                    process()

                space()

                nested_cmd("Press <ENTER> to end connection", hack_name)

                process(3)

                space()

                pr("=== CONNECTION ENDED ===")

                space()
                process()

                pr("Hack complete.")



def help_command(curr_cmd, head, tail, params):
    if len(tail) > 0:
        # User has specified what they want help with/
        pass

    else:
        pr("You need help? You're really that bad of a hacker?")
        pr("Commands:")
        pr("help [what to help with]: Shows help, or if specified what help is needed, shows help for a specific command.")
        pr("hack [what to hack]: Can hack into any system, anywhere. [what to hack] must be a string.")

def home():
    clear()
    logo()

    while True:
        curr_cmd = cmd("enter command").split(" ")
        head = curr_cmd[0]
        tail = curr_cmd[1:]

        params = " ".join(tail)

        if head == "help":
            help_command(curr_cmd, head, tail, params)

        elif head == "hack":
            if params[1:-1] in DELETED and is_string(params):
                pr("I'm sorry, that service has been deleted.")

            if params[1:-1] in UNAVAILABLE and is_string(params):
                pr("I'm sorry, that service is unavailable.")

            hack_command(curr_cmd, head, tail, params)


        space()




# ==================== MAIN ====================

def main():
    # login()
    # program_loading()
    home()

if __name__ == "__main__":
    main()
