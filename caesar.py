def caesar(text, shift, operation):
    '''
    caesar function that take 3 parameters, text as string, 
    shift as int and operation as string (e or d)
    ---------------------------------
    @param:
        text = string provided as encrypt or decrypt text.
        shift = number that is use to perform an alphabetically position shift in the list.
        operation = string letter "e" for encrypt and "d" for decrypt, the function will 
        perform base on the instruct operation.

    @return:
        if operation is "e" then the function will return the encrypt text.
        if operation is "d" then the function will return the decrypt text.
    '''

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    # your code is here!
    ...
    cipher_text = ""
 
    
    # if type(shift)== int:
             
    if type(shift) == float or type(shift) == str:
        return("invalid shift number") 
    elif shift == 26: 
        return("invalid shift number")
    elif shift < 0:
         return("invalid shift number")
    elif operation == "g":
        return("invalid option")
    elif operation =="e":
            for x in text:
                if x in alphabet:
                    x = x.lower()
                    shift_index = alphabet.index(x)
                        # if shift_index == -1:
                        #     cipher_text  += x
                    
                    new_index = (shift_index + shift) % 26
                    new_character = alphabet[new_index]
                    cipher_text += new_character
            return (cipher_text)
    elif operation == "d":
            for x in text:
           
                if x in alphabet:
                    x = x.lower()
                   
                    shift_index = alphabet.index(x)
                    new_index = (shift_index - shift) % 26
                    new_character = alphabet[new_index]
                    cipher_text += new_character
            return(cipher_text)
                   
             
                  
   
    
            
    
    