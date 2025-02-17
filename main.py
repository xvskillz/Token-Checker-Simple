import requests
from colorama import init, Fore

init(autoreset=True)

def check(token):  
    headers = {"Authorization": token}  
    response = requests.get("https://discord.com/api/v9/users/@me", headers=headers)

    if response.status_code == 200: 
        print(Fore.GREEN + '[VALID] ' + token)  
    else:
        print(Fore.RED + '[INVALID] ' + token)  

def main():
    try:
        with open('tokens.txt', 'r') as file:
            tokens = [line.strip() for line in file if line.strip()]

        if not tokens:
            print(Fore.YELLOW + 'No tokens found in tokens.txt')  
            return
        
        print(Fore.GREEN + f'Checking {len(tokens)} tokens...' + Fore.RESET)  

        for token in tokens:
            check(token)  

    except FileNotFoundError:  
        print(Fore.RED + 'tokens.txt not found')

if __name__ == '__main__':
    main()