import requests
import hashlib
import sys



def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code !=200:
        raise RuntimeError(f'error fetching: {res.status_code}, check the api and try again')
    return res

def get_password_leaks_count(hashes , hash_to_ckeck):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h,count in hashes:
        if h == hash_to_ckeck:
            return count
    return 0
    
def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5] , sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response , tail)

def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times in database... you should probably change your password!')
        else:
            print(f'{password} was not found in database, you\'re good to goo')

prompt_input_message = '''
***Welcome to password leakage checker***
*Developed by MohamadEzza @ github (https://github.com/mohamadezza)*

give me your password to check:
'''

prompt_input = input(prompt_input_message)

if __name__== '__main__':
    main(prompt_input.splitlines())
    k = input('press any key to close the program.')