```
  __  __          _____   _____ _    _          _   _  _____ ______ _____  
 |  \/  |   /\   / ____| / ____| |  | |   /\   | \ | |/ ____|  ____|  __ \ 
 | \  / |  /  \ | |     | |    | |__| |  /  \  |  \| | |  __| |__  | |__) |
 | |\/| | / /\ \| |     | |    |  __  | / /\ \ | . ` | | |_ |  __| |  _  / 
 | |  | |/ ____ \ |____ | |____| |  | |/ ____ \| |\  | |__| | |____| | \ \ 
 |_|  |_/_/    \_\_____| \_____|_|  |_/_/    \_\_| \_|\_____|______|_|  \_\
```
MAC-CHANGER (PRO VERSION)
A robust Python utility designed for network anonymity and security testing. 
Unlike basic scripts, this version uses 'optparse' for terminal arguments 
and 'Regular Expressions' (Regex) to verify if the MAC address was 
successfully changed, ensuring a reliable result every time.

**Features**
* **Command-Line Arguments:** Professional CLI feel using `-i` (interface) and `-m` (mac) flags.
* **Regex Verification:** Scans system output to confirm the hardware address change.
* **Automated Interface Management:** Handles 'down' and 'up' states of the network card automatically.
* **Error Handling:** Provides visual feedback (BRAVO/TRY AGAIN) based on the operation's success.

**Prerequisites**
* Python 3.x
* Linux environment (Requires `ifconfig` tools).
* Root/Sudo privileges (To modify hardware settings).

**Installation**

Clone the repository:
   * git clone https://github.com/Tde99/MAC-Changer-Pro.git

Navigate to the directory:
   * cd MAC-Changer-Pro

Make the script executable:
   * chmod +x mac_changer.py

**Usage**
You must specify the network interface and the desired new MAC address. 

sudo python3 mac_changer.py -i eth0 -m 00:11:22:33:44:55

**How it Works:**
1. **Parsing:** The script captures your inputs via terminal flags.
2. **Execution:** It shuts down the interface, injects the new MAC, and brings the interface back up.
3. **Verification:** It runs `ifconfig` again, uses Regex to find the current MAC, and compares it with your input.


**Technical Highlights:**
* **Subprocess Module:** Used for secure system command execution.
* **Regular Expressions:** `r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w"` is used to precisely capture the hardware address from system strings.

**Important Notes:**
* **Temporary Change:** The MAC address change is temporary and will revert to the original hardware ID after a reboot.
* **Ethics:** Use this tool for privacy and authorized security testing only.
