def get_firefox_path(file="places.sqlite"):
    import sys  # Mitteilen ob Mac, Linux oder Win
    import os

    folder = ""

    # Mac
    if sys.platform == "darwin":  # Laufen wir auf Mac ? ~ -> Aktueller Benutzer
        folder = os.path.expanduser("~") + "/Library/Application Support/Firefox/Profiles/"

    # Linux
    elif sys.platform.startswith("linux"):
        # sys.platform == linux, sys.platform == linux2
        folder = os.path.expanduser("~") + "/.mozilla/firefox/"

    # Windowsm
    elif sys.platform == "win32" or sys.platform == "cygwin":
        folder = os.path.expanduser("~") + "/AppData/Roaming/Mozilla/Firefox/Profiles/"

    profile = None
    profiles = os.listdir(folder)
    for element in profiles:
        if element == "Crash Reports":
            continue

        if element[0] == ".":
            continue

        # folder + "/" + element
        if os.path.isdir(folder + "/" + element): # Wenn der Pfad ein existierender PFad ist
            if os.path.isfile(folder + "/" + element + "/places.sqlite"): # Wenn es auch noch das Element places.sqlite existiert
                profile = element

        if profile == None:
            raise Exception("firefox folder could not be found")

        return folder + "/" + element + "/" + file

