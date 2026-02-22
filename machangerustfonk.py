import subprocess
import re
import optparse

def start(): #input degerleri
    parse = optparse.OptionParser()
    parse.add_option("-i", "--interface", dest="interface", help="interface changer")
    parse.add_option("-m", "--machanger", dest="mac_address", help="mac change")

    return parse.parse_args()

def mac(inter,macha): #mac degistirme
    subprocess.call(["ifconfig", inter, "down"])
    subprocess.call(["ifconfig", inter, "hw", "ether", macha])
    subprocess.call(["ifconfig", inter, "up"])

def cont(interface):#istedğimiz kısmı çıkartan sonrasında yazı
    ifconfig = subprocess.check_output(["ifconfig", interface]).decode()
    ymac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig)

    if ymac:
        return ymac.group(0)
    else:
        return None

print("MAC Changer Started")
(userInput,argumants) = start()
mac(userInput.interface,userInput.mac_address)
emac = cont(userInput.interface)
print(emac)
if emac == userInput.mac_address:
    print("BRAVO :]")
else:
    print("TRY AGAIN :/")