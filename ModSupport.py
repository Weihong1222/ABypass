import os



def LoadModInfo():
    if not os.path.exists("Mods"):
        os.makedirs("Mods")
        return
    else:
        ModsList = os.listdir("Mods")
    
    print("Found Mods folder.")
    print("Loading info...")
    InfoList = []

    for Mod in ModsList:
        if os.path.exists(f"Mods/{Mod}/ModInfo.json"):
            ModInfo = os.path.join("Mods",f"{Mod}","ModInfo.json")
            InfoList.append(ModInfo)
        else:
            print(f"Mode name {Mod} file strcture are not valid(ModInfoNotFound).")        

    


if __name__ == '__main__':
    LoadModInfo()