import csv
import random
from tkinter import *
from functools import partial



class StartGame:
    """
    Initial Game interface (Asks users how many round they would like to play)
    """

    def __init__(self,):
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

        # Retrive rounds to be converted
        rounds_wanted = 5
        self.to_play(rounds_wanted)

    def to_play(self, num_rounds):
        """
        Invokes Game GUI and take accross numebr of rounds to be played
        """
        Play(num_rounds)
        # Hide root window (ie: hide rounds choice window) 
        root.withdraw()

class Play:
    """
    Interface for playing the colour quest game
    """
    def __init__(self, how_many):
        self.play_box = Toplevel()

        self.game_frame = Frame(self.play_box)
        self.game_frame.grid(padx=10, pady=10)

        self.heading_label = Label(self.game_frame, text="Colour Quest", font=("Airal", "16", 'bold'),
                                   padx=5, pady=5)
        self.heading_label.grid(row=0)

        self.hints_button =Button(self.game_frame, font=("arial", "14", "bold"),
                                  text="Hints", width=15, fg="#FFFFFF",
                                  bg="#FF8000", padx=10, pady=10, command=self.to_hints)
        self.hints_button.grid(row=1)

    def to_hints(self):
        """
        Displays hints for playing game
        :return:
        """
        DisplayHints(self)

class DisplayHints:

    def __init__(self, partner):
        # setup dialogue box amd background colour
        background = "#ffe6cc"
        self.hints_box = Toplevel()

        # disable hints button
        partner.hints_button.config(state=DISABLED)

        # if users press cross at the top, closes hints
        #  and releases hints box
        self.hints_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_hints, partner))

        self.hints_frame = Frame(self.hints_box, width=300,
                                height=200)
        self.hints_frame.grid()

        self.hints_heading_label = Label(self.hints_frame,
                                        text="Hints",
                                        font=("Arial", "14", "bold"))
        self.hints_heading_label.grid(row=0)

        self.hints_text_label = Label(self.hints_frame,
                                     text="hints text goes here", wraplength=350,
                                     justify="left")
        self.hints_text_label.grid(row=1, padx=10)

        self.dismiss_button = Button(self.hints_frame,
                                     font=("Arial", "12", "bold"),
                                     text="Dismiss", bg="#CC6600",
                                     fg="#FFFFFF",
                                     command=partial(self.close_hints, partner))
        self.dismiss_button.grid(row=2, padx=10, pady=10)

        # list and loop to set the background colour on
        # everything except buttons
        recolour_list = [self.hints_frame, self.hints_heading_label,
                         self.hints_text_label]

        for item in recolour_list:
            item.config(bg=background)

    def close_hints(self, partner):
        """
        Closes hints dialogue box (and enable hints button)
        """
        # put hints button back to normal
        partner.hints_button.config(state=NORMAL)
        self.hints_box.destroy()



    


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Colour Quest")
    StartGame()
    root.mainloop()


  