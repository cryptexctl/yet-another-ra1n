import usb.core
import time
from .constants import APPLE_VID, DFU_PID

def find_device(pid=DFU_PID):
    dev = usb.core.find(idVendor=APPLE_VID, idProduct=pid)
    if not dev:
        return None
    return dev

def wait_for_device(pid=DFU_PID):
    print("[*] Waiting for device...")
    while True:
        dev = find_device(pid)
        if dev:
            print(f"[+] Device found: {dev}")
            return dev
        time.sleep(0.5)

def send_payload(dev, payload: bytes, block=0):
    print(f"[>] Sending payload ({len(payload)} bytes, block={block})...")
    try:
        dev.ctrl_transfer(
            bmRequestType=0x21,
            bRequest=1,
            wValue=block,
            wIndex=0,
            data_or_wLength=payload,
            timeout=2000
        )
        print("[+] Payload sent")
        return True
    except usb.core.USBError as e:
        print(f"[!] Error sending payload: {e}")
        return False

def clear_status(dev):
    try:
        dev.ctrl_transfer(0x21, 4, 0, 0, [], timeout=2000)
        print("[*] CLRSTATUS sent")
    except:
        pass

def trigger(dev):
    print("[>] Triggering...")
    try:
        resp = dev.ctrl_transfer(
            bmRequestType=0xA1,
            bRequest=3,
            wValue=0,
            wIndex=0,
            data_or_wLength=6,
            timeout=2000
        )
        print(f"[+] Response: {list(resp)}")
        return True
    except usb.core.USBError as e:
        print(f"[!] Error triggering: {e}")
        return False 