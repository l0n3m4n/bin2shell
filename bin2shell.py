import argparse

class Color:
    BRIGHT_RED = '\033[31;1m'
    BRIGHT_GREEN = '\033[32;1m'
    BRIGHT_YELLOW = '\033[33;1m'
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

def main():
    banner = f"""{Color.BRIGHT_GREEN}
  ,--.   ,--.         ,---.        ,--.            ,--.,--. 
  |  |-. `--',--,--, '.-.  \ ,---. |  ,---.  ,---. |  ||  | 
  | .-. ',--.|      \ .-' .'(  .-' |  .-.  || .-. :|  ||  | 
  | `-' ||  ||  ||  |/   '-..-'  `)|  | |  |\   --.|  ||  | 
   `---' `--'`--''--''-----'`----' `--' `--' `----'`--'`--' 
      {Color.RESET}{Color.PINK}Author: @l0n3m4n / Shellcode Generator / v1.2
{Color.RESET}"""

    parser = argparse.ArgumentParser(description="Shellcode Generator (C,C#,CPP,ASM)",
                                    epilog='Example usage: python3 bin2shell.py -bin shellcode.bin -c shellcode_c.txt')
    print(banner)
    parser.add_argument('-bin', metavar="shellcode.bin", required=True, help='Input shellcode binary file')
    parser.add_argument('-c', help='Output file for C formatted shellcode')
    parser.add_argument('-cpp', help='Output file for C++ formatted shellcode')
    parser.add_argument('-cs', help='Output file for C# formatted shellcode')
    parser.add_argument('-asm', help='Output file for Assembly (NASM) formatted shellcode')

    args = parser.parse_args()

    input_file = args.shellcode

    if args.c_output:
        # Format shellcode for C
        c_code = format_shellcode_c(input_file)
        print(f"\n{Color.BRIGHT_GREEN}Formatted C Shellcode:\n")
        print(c_code)

        with open(args.c_output, 'w') as f:
            f.write(c_code)
        print(f"\nSaved C formatted shellcode to {args.c_output}")

    if args.cpp_output:
        # Format shellcode for C++
        cpp_code = format_shellcode_cpp(input_file)
        print("\nFormatted C++ Shellcode:\n")
        print(cpp_code)

        with open(args.cpp_output, 'w') as f:
            f.write(cpp_code)
        print(f"\nSaved C++ formatted shellcode to {args.cpp_output}")

    if args.cs_output:
        # Format shellcode for C#
        csharp_code = format_shellcode_csharp(input_file)
        print("\nFormatted C# Shellcode:\n")
        print(csharp_code)

        with open(args.cs_output, 'w') as f:
            f.write(csharp_code)
        print(f"\nSaved C# formatted shellcode to {args.cs_output}")

    if args.asm_output:
        # Format shellcode for ASM
        asm_code = format_shellcode_asm(input_file)
        print("\nFormatted ASM Shellcode:\n")
        print(asm_code)

        with open(args.asm_output, 'w') as f:
            f.write(asm_code)
        print(f"\nSaved ASM formatted shellcode to {args.asm_output}{Color.RESET}")

if __name__ == "__main__":
    main()
