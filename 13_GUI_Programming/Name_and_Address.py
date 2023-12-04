# The source code for the examples in the book have been provided.
# You can find it: Modules --> Resources --> Chapter Example Code.

# Try these examples out and use them as a starting point to modify
# them to do the two labs.

# 1. Name and Address
# Write a GUI program that displays your name and address when a
# button is clicked. The program’s window should appear as the sketch
# below when it runs. When the user clicks the Show Info button, the
# program should display your name and address, as shown in the sketch
# on the right of the figure.  (12 points)

# Upload an image that displays the data when the Show Info button is
# clicked. (3 points)

import tkinter


class MyGUI:

  def __init__(self):
    self.main_window = tkinter.Tk()
    self.main_window.title("")

    self.info_label = tkinter.Label(self.main_window,
                                    text='',
                                    font=('Arial', 12))

    self.info_label.pack(padx=10, pady=10)

    self.show_info_button = tkinter.Button(self.main_window,
                                           text='Show Info',
                                           command=self.show_info)

    self.show_info_button.pack(side='left', padx=10, pady=10)

    self.quit_button = tkinter.Button(self.main_window,
                                      text='Quit',
                                      command=self.main_window.quit)

    self.quit_button.pack(side='right', padx=10, pady=10)

    tkinter.mainloop()

  def show_info(self):
    self.info_label.config(
        text='Hayk Pash\nHollywood\nLos Angeles, California')


if __name__ == '__main__':
  gui = MyGUI()
