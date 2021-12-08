"""
Jake MacDonald
Assignment 10.1: Your Own Class
tv.py
""" 

class TV(): 
    # These are the four class methods.
    # Power will be used for power_on and power_off
    # Mute, Loud, and Quiet will be used for set_volume and change_channel
    power = False
    mute = False
    loud = False 
    quiet = False
    # Constructor method that takes in the TV's screen size and service as arguements.
    def __init__(self, screen, service):
        self.__screen = screen 
        self.__service = service
    # Turns the TV on. 
    def power_on(self): 
        self.power = True 
        print("The TV is now on!")
    # Turns the TV off.
    def power_off(self):
        self.power = False 
        print("The TV is now off.")
    # Ajusts the "volume" of the TV.
    def set_volume(self, level):
        if level == "mute":
            self.mute = True
            self.loud = False 
            self.quiet = False
        elif level == "loud":
            self.loud = True
            self.mute = False
            self.quiet = False
            print("!(c>")
        elif level == "quiet":
            self.quiet = True
            self.mute = False
            self.loud = False
            print("c>")
        elif level == "normal":
            self.mute = False
            self.loud = False
            self.quiet = False
            print("(c>")

    # Displays different messages meant to represent TV channels.
    # The presentation of the text is dependent on the specific TV's screen size and service provider.
    def change_channel(self, channel):
        if self.power == False:
            print("TV isn't turned on...")
        else:
            print("Changing channel...")
        
        if self.mute == True:
            print("X>\n...")
        elif channel == "CNN" and self.__screen == "16:9" and self.__service == "xfinity":
            feed = "Good evening, I'm Anderson Cooper. Our top story is..."
            if self.loud == True:
                print(feed.upper())
            elif self.quiet == True:
                print(feed.lower())
            else:
                print(feed)
        elif channel == "CNN" and self.__screen == "16:9" and self.__service == "AT&T":
            feed = "Go_d ev__in_, I__ An__r_on _ooper. O_r _op st__y _s..."
            if self.loud == True:
                print(feed.upper())
            elif self.quiet == True:
                print(feed.lower())
            else:
                print(feed)
        elif channel == "CNN" and self.__screen == "4:3" and self.__service == "xfinity":
            feed = "Good evening, \nI'm Anderson Cooper. \nOur top story is..."
            if self.loud == True:
                print(feed.upper())
            elif self.quiet == True:
                print(feed.lower())
            else:
                print(feed)
        elif channel == "CNN" and self.__screen == "4:3" and self.__service == "AT&T":
            feed = "Go_d ev__in_, \nI__ An__r_on _ooper. \nO_r _op st__y _s..."
            if self.loud == True:
                print(feed.upper())
            elif self.quiet == True:
                print(feed.lower())
            else:
                print(feed)
        

        elif channel == "ESPN" and self.__screen == "16:9" and self.__service == "xfinity":
            feed = "Johnson passes to Mayfeild, 5 yards left- Touchdown!"
            if self.loud == True:
                print(feed.upper())
            elif self.quiet == True:
                print(feed.lower())
            else:
                print(feed)
        elif channel == "ESPN" and self.__screen == "16:9" and self.__service == "AT&T":
            feed = "Jo_nso_ _a_ses t_ Mayfeil_, _ ya_ds le_t- To__hdow_!"
            if self.loud == True:
                print(feed.upper())
            elif self.quiet == True:
                print(feed.lower())
            else:
                print(feed)
        elif channel == "ESPN" and self.__screen == "4:3" and self.__service == "xfinity":
            feed = "Johnson passes to\n Mayfeild, 5 yards\n left- Touchdown!"
            if self.loud == True:
                print(feed.upper())
            elif self.quiet == True:
                print(feed.lower())
            else:
                print(feed)
        elif channel == "ESPN" and self.__screen == "4:3" and self.__service == "AT&T":
            feed = "Jo_nso_ _a_ses t_\n Mayfeil_, _ ya_ds\n le_t- To__hdow_!"
            if self.loud == True:
                print(feed.upper())
            elif self.quiet == True:
                print(feed.lower())
            else:
                print(feed)


        elif channel == "HBO" and self.__screen == "16:9" and self.__service == "xfinity":
            feed = "One does not simply quote a show they haven't seen yet."
            if self.loud == True:
                print(feed.upper())
            elif self.quiet == True:
                print(feed.lower())
            else:
                print(feed)
        elif channel == "HBO" and self.__screen == "16:9" and self.__service == "AT&T":
            feed = "O__ _oes n_t _imp_y qu__e a _ho_ __ey haven'_ _een ye_."
            if self.loud == True:
                print(feed.upper())
            elif self.quiet == True:
                print(feed.lower())
            else:
                print(feed)
        elif channel == "HBO" and self.__screen == "4:3" and self.__service == "xfinity":
            feed = "One does not simply\n quote a show they\n haven't seen yet."
            if self.loud == True:
                print(feed.upper())
            elif self.quiet == True:
                print(feed.lower())
            else:
                print(feed)
        elif channel == "HBO" and self.__screen == "4:3" and self.__service == "AT&T":
            feed = "O__ _oes n_t _imp_y\n qu__e a _ho_ __ey\n haven'_ _een ye_."
            if self.loud == True:
                print(feed.upper())
            elif self.quiet == True:
                print(feed.lower())
            else:
                print(feed)    




# Main Function
def main():
    Sony = TV("16:9", "xfinity")
    Sony.power_on()
    Sony.set_volume("loud")
    Sony.change_channel("ESPN")
    Sony.set_volume("quiet")
    Sony.change_channel("HBO")
    Sony.set_volume("mute")
    Sony.change_channel("CNN")
    Sony.set_volume("normal")
    Sony.change_channel("CNN")
    Sony.power_off()

    LG = TV("4:3", "AT&T")
    LG.power_on()
    LG.set_volume("loud")
    LG.change_channel("ESPN")
    LG.set_volume("quiet")
    LG.change_channel("HBO")
    LG.set_volume("mute")
    LG.change_channel("CNN")
    LG.set_volume("normal")
    LG.change_channel("CNN")
    LG.power_off()


# Calls the main code
if __name__ == "__main__":
    main()