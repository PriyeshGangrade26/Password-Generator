import string
import random

if __name__ == "__main__":
    try:
        s1 = string.ascii_lowercase
        # print(s1)
        s2 = string.ascii_uppercase
        # print(s2)
        s3 = string.digits
        # print(s3)
        s4 = string.punctuation
        # print(s4)
        plen = int(input("Enter password length:\n"))
        s = []
        s.extend(list(s1))
        s.extend(list(s2))
        s.extend(list(s3))
        s.extend(list(s4))
        # print(s)
        # random.shuffle(s)
        # print(s)
    
        # print("".join(s[0:plen]))
        print("Your password is: ")
        print("".join(random.sample(s, plen)))
    except Exception as e:
        print("***  Please enter a integer  ***")
