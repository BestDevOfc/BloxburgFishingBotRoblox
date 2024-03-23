from fishingbot import*


def main():
    while True:
        print(f"{C.RED}[+] - {C.GREEN}[ Enter Path to Templatted Image ]: ")
        timg_path = input(f"")

        if os.path.isfile(timg_path) != True:
            print(f"{C.GREEN}[!] - {C.RED}[ One of the file images does not exist ! ]")
            input(f"[ Okay. ]")
        break

    Bot = FishingBot(timg_path)    
    Bot.startBot()
    
main()