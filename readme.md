[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=11460086&assignment_repo_type=AssignmentRepo)
# HW. 4 Caesar Cipher

Nowadays there are alot of hackers that are trying to steal messages and useful information. Youre working for a company called AUPP, and they required you to create a basic Caesar Cipher encryption that will encrypt messages that were sent out by the company, for safety and security. And you were also ask to create a decrypt program.

- where it is using shift number to rotate different range of character in the alphabet
- And with the encrypted text, you will be able to decrypt it back using the same shift number.

<br>

## Development Requirement

Functional Test (50%)

1. create **caesar** function that take 3 parameters, **text as string, shift as int** and **operation as string (e or d)**
   1. **text** = string provided as encrypt or decrypt text.
   2. **shift** = number that is use to perform an alphabetically position shift in the list.
   3. **operation** = string letter "e" for encrypt and "d" for decrypt, the function will perform base on the instruct operation.
2. **shift** number is only support whole and positive number, otherwise return **"invalid shift number"**.
3. 26 is an invalid shift number, if provided, return **"invalid shift number"**.
4. if invalid operation letter provided, return **"invalid option"**.
5. if all parameter provided as expected, return **string** base on operation (encrypt or decrypt text)
   example:
   1. **caesar("hello", 20, "e")** should return **"byffi"**
   2. **caesar("byffi", 20, "d")** should return **"hello"**
      Note: you should be able to use shift number larger than 26 to encrypt or decrypt the text.

Application Test (50%)

1. application should not crashed when invalid input is provided.
2. user should be able to repeat the program after ended.
3. user friendly interface.

<br>

### Task: Your task is to write a python program that will encrypt and decrypt user's messages.

<br>

### Expected output:

![HW_4_CC](resource/HW_4_CC.png)

### HINT:

> - Make used of function

<br><br>

<h1 style="text-align: center;">*** Be Creative ***</h1>
