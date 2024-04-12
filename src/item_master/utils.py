import string
import secrets

def random_string():
         count = 0
         str1 = ''
         str2 = ''
         str3 = ''
         while count < 2:
                  str1 += secrets.choice(string.ascii_uppercase)
                  count += 1
         str1 += " "

         numb = [1,2,3]
         numb_rand = secrets.choice(numb)
         count = 0
         while count < numb_rand:
                  str2 += secrets.choice(string.ascii_uppercase)
                  count += 1

         numb = [1,2]
         numb_rand = secrets.choice(numb)
         count = 0
         while count < numb_rand:
                  str3 += secrets.choice("0123456789")
                  count += 1
         str3 += " "

         #2nd portion of random string
         numb = [4,5,6,7]
         numb_rand = secrets.choice(numb)
         count = 0
         while count < numb_rand:
                  str1 += secrets.choice("0123456789")
                  str2 += secrets.choice("0123456789")
                  str3 += secrets.choice("0123456789")
                  count += 1
         return str1, str2, str3
