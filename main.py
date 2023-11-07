def mainmenu():
    with open('ui/title.txt','r') as title:
        display = title.read()
        print(display)
        user = int(input("| > Menu: "))
        match user:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case _:
                mainmenu()
        
    
mainmenu()