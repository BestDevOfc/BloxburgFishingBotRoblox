# This file is simple styling
# initializations and stuff:

from globalimports import*


init(autoreset=True)

ENCODING: str = sys.getfilesystemencoding()

class Colors:
    RED = f"{Style.BRIGHT}{Fore.RED}"
    GREEN = f"{Style.BRIGHT}{Fore.GREEN}"
    CYAN = f"{Style.BRIGHT}{Fore.CYAN}"
    YELLOW = f"{Style.BRIGHT}{Fore.YELLOW}"
    MAGENTA = f"{Style.BRIGHT}{Fore.MAGENTA}"

C = Colors()


def timer(func):
    '''
        How long it took for a function/method to run:
    '''
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        time_passed = int(end-start)
        print(f"{C.GREEN}[ Execution of \'{func.__name__}\' took {time_passed} seconds ! ]")
        return result
    return wrapper