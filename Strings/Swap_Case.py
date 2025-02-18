def swap_case(s):
    #Option 1.  Using predefined python function
    #s.swapcase() 
    
    #Option 2.  Using List Comprehension
    #Generate a letter array from doing case checking and conversion
    return  ''.join([letter.lower() if letter.isupper() else letter.upper()for letter in s])

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)