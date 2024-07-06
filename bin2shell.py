#!/bin/python3 

import argparse
import struct

class Color:
    BRIGHT_RED = '\033[31;1m'
    BRIGHT_GREEN = '\033[32;1m'
    BRIGHT_YELLOW = '\033[33;1m'
    BLUE = '\033[34m'
    CYAN = '\033[36m'
    GREEN = '\033[32m'
    PINK = '\033[95m'
    RESET = '\033[0m'

def format_shellcode_c(input_file):
    ctr = 1
    maxlen = 15
    formatted_shellcode = "\""

    with open(input_file, "rb") as f:
        byte = f.read(1)
        while byte:
            formatted_shellcode += "\\x" + byte.hex()
            if ctr == maxlen:
                formatted_shellcode += "\" \n\""
                ctr = 0
            ctr += 1
            byte = f.read(1)
    formatted_shellcode += "\""
    
    return formatted_shellcode

def format_shellcode_cpp(input_file):
    formatted_shellcode = "const char shellcode[] = {"

    with open(input_file, "rb") as f:
        byte = f.read(1)
        while byte:
            formatted_shellcode += "0x" + byte.hex() + ","
            byte = f.read(1)
    
    formatted_shellcode = formatted_shellcode.rstrip(',') + "};"
    
    return formatted_shellcode

def format_shellcode_csharp(input_file):
    formatted_shellcode = "byte[] shellcode = new byte[] {"

    with open(input_file, "rb") as f:
        byte = f.read(1)
        while byte:
            formatted_shellcode += "0x" + byte.hex() + ","
            byte = f.read(1)
    
    formatted_shellcode = formatted_shellcode.rstrip(',') + "};"
    
    return formatted_shellcode

def format_shellcode_asm(input_file):
    formatted_shellcode = "section .text\n"
    formatted_shellcode += "global _start\n\n"
    formatted_shellcode += "_start:\n"
    formatted_shellcode += "\tjmp shellcode\n\n"
    formatted_shellcode += "shellcode:\n"
    
    with open(input_file, "rb") as f:
        byte = f.read(1)
        while byte:
            formatted_shellcode += f"\tdb 0x{byte.hex()}\n"
            byte = f.read(1)
    
    return formatted_shellcode

def format_shellcode_bof(input_file): 
    with open(input_file, 'rb') as f:
        payload = f.read()
    
    # Define the random magic header and prepare the payload
    magic_hdr = 0xe9e63f1c 
    payload += struct.pack("<L", magic_hdr)
    payload += struct.pack("<L", len(payload))  
    
    return payload  
    

def main():
    banner = f"""{Color.BRIGHT_GREEN}
  ,--.   ,--.         ,---.        ,--.            ,--.,--. 
  |  |-. `--',--,--, '.-.  \ ,---. |  ,---.  ,---. |  ||  | 
  | .-. ',--.|      \ .-' .'(  .-' |  .-.  || .-. :|  ||  | 
  | `-' ||  ||  ||  |/   '-..-'  `)|  | |  |\   --.|  ||  | 
   `---' `--'`--''--''-----'`----' `--' `--' `----'`--'`--' 
       {Color.RESET}{Color.PINK}Author: @l0n3m4n / Shellcode Generator / v1.2 {Color.RESET}"""

    parser = argparse.ArgumentParser(description="Binary payload to shellcode generator (C,C#,CPP,ASM)",
                                    epilog='Example usage: python3 bin2shell.py -bin payload.bin -c shellcode_c.txt')
    print(banner)
    parser.add_argument('-bin', required=True, help='Input shellcode binary file')
    parser.add_argument('-c', help='Convert binary into C raw shellcode')
    parser.add_argument('-cpp', help='Convert binary into C++ raw shellcode')
    parser.add_argument('-cs', help='Convert binary into C# raw shellcode')
    parser.add_argument('-asm', help='Convert binary into (NASM) raw shellcode')
    parser.add_argument('-bof', help='Convert cobalt strike BOF into raw shellcode')

    args = parser.parse_args()

    input_file = args.bin

    if args.c:
        # Format shellcode for C
        c_code = format_shellcode_c(input_file)
        print(f"\n{Color.CYAN}Formatted{Color.RESET}{Color.GREEN} C Shellcode:{Color.RESET}\n")
        print(Color.CYAN + c_code + Color.RESET)

        with open(args.c, 'w') as f:
            f.write(c_code)
        print(f"\n{Color.CYAN}Saved{Color.RESET}{Color.GREEN} C formatted shellcode to {args.c}{Color.RESET}")

    if args.cpp:
        # Format shellcode for C++
        cpp_code = format_shellcode_cpp(input_file)
        print(f"\n{Color.CYAN}Formatted{Color.RESET}{Color.GREEN} C++ Shellcode:{Color.RESET}\n")
        print(Color.CYAN + cpp_code + Color.RESET)

        with open(args.cpp, 'w') as f:
            f.write(cpp_code)
        print(f"\n{Color.CYAN}Saved{Color.RESET} {Color.GREEN}C++ formatted shellcode to {args.cpp}{Color.RESET}")

    if args.cs:
        # Format shellcode for C#
        csharp_code = format_shellcode_csharp(input_file)
        print(f"\n{Color.CYAN}Formatted{Color.RESET} {Color.GREEN}C# Shellcode:{Color.RESET}\n")
        print(Color.CYAN + csharp_code + Color.RESET)

        with open(args.cs, 'w') as f:
            f.write(csharp_code)
        print(f"\n{Color.CYAN}Saved{Color.RESET} {Color.GREEN}C# formatted shellcode to {args.cs}{Color.RESET}")

    if args.asm:
        # Format shellcode for ASM
        asm_code = format_shellcode_asm(input_file)
        print(f"\n{Color.CYAN}Formatted{Color.RESET} {Color.GREEN}ASM Shellcode:\n{Color.RESET}")
        print(Color.CYAN + asm_code + Color.RESET)

        with open(args.asm, 'w') as f:
            f.write(asm_code)
        print(f"\n{Color.CYAN}Saved{Color.RESET} {Color.GREEN}ASM formatted shellcode to {args.asm}{Color.RESET}")
    
    if args.bof:
        # Format shellcode for BOF Loader (e.g., Cobaltstrike)
        bof_code = format_shellcode_bof(input_file) 
        print(f"\n{Color.CYAN}Formatted{Color.RESET} {Color.GREEN}BOF Loader Shellcode:\n{Color.RESET}")
        print(Color.CYAN + bof_code.hex() + Color.RESET) 
        
        with open(args.bof, 'wb') as f: 
            f.write(bof_code)
        print(f"\n{Color.CYAN}Saved{Color.RESET} {Color.GREEN}BOF Loader formatted shellcode to {args.bof}{Color.RESET}")

if __name__ == "__main__":
    main()
