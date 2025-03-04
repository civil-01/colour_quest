from tkinter import *
from functools import partial # to prevent unwanted winows


class StartGame:
    """
    Initial Game interface (Asks users how many round they would like to play)
    """

    def __init__(self):
        """
        Gets number of round from user
        """

        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()


        # create play button
        self.play_button = Button(self.start_frame, font=("Arial", "16", "bold"),
                                  fg="#FFFFFF", bg="#0057D8", text="Play", width=10,
                                  command=self.check_rounds)
        self.play_button.grid(row=0, column=1)



    def check_rounds(self):
        """
        Checks users have entered 1 or more rounds
        """

        play(5)
        # hide root window(ie: hide round choice window).
        root.withdraw()


  

        

class play:
    """
    Interface for plaing the Colour Quest Game
    """            

    def __init__(self, how_many):
        self.play_box = Toplevel()

        self.game_frame = Frame(self.play_box)
        self.game_frame.grid(padx=10, pady=10)

        # body font for most labels
        body_font = ("Arial", "12")
 
        # list for label details (text | font | background | row)
        play_labels_list = [
            ["Round # of #", ("Arial", "16", "bold"), None, 0],
            ["Score to beat: #", body_font, "#FFF2CC", 1],
            ["Choose a colour below. God luck 🍀", body_font, ""]
        ]



    def close_play(self):
        # reshow root (ie: choose rounds) and end current
        # game / allow new game to start
        root.deiconify()
        self.play_box.destroy()






# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Colour Quest")
    StartGame()
    root.mainloop()

