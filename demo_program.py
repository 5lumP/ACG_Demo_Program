import hashlib
#Example on the limitations of sha1
password = input('Enter the password to hash\n>>>')
print('\nSHA1: \n')
for i in range(3):
    setpass = bytes(password, 'utf-8') #converting our password into bytes
    hash_object = hashlib.sha1(setpass) #This hashes our converted password with sha1
    guess_pass = hash_object.hexdigest() #By using hexdigest() we are able to convert hash_object into hexadecimal 
    print(guess_pass) #You will see that as we iterate through the loop it returns the same hash value
