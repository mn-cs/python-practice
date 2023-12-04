# (b) Joe’s Automotive
# Joe’s Automotive performs the following routine maintenance services:

# Oil change—$30.00
# Lube job—$20.00
# Radiator flush—$40.00
# Transmission flush—$100.00
# Inspection—$35.00
# Muffler replacement—$200.00
# Tire rotation—$20.00

# Write a GUI program with check buttons that allow the user to select
# any or all of these services.

# When the user clicks a button, the total charges should be displayed.

# Upload an image with all the services selected and the total charges
# calculated and displayed. (3 points)

import tkinter


class MyGUI:

  def __init__(self):
    self.main_window = tkinter.Tk()
    self.main_window.title("")

    self.services = {
        "Oil Change": 30.00,
        "Lube Job": 20.00,
        "Radiator Flush": 40.00,
        "Transmission Flush": 100.00,
        "Inspection": 35.00,
        "Muffler Replacement": 200.00,
        "Tire Rotation": 20.00
    }

    self.check_vars = {
        service: tkinter.BooleanVar()
        for service in self.services
    }

    for service in self.services:
      tkinter.Checkbutton(self.main_window,
                          text=f"{service}—${self.services[service]:.2f}",
                          variable=self.check_vars[service]).pack(anchor='w')

    self.total_label = tkinter.Label(self.main_window,
                                     pady=20,
                                     text="Total Charges: $0.00")

    self.total_label.pack()

    self.calc_button = tkinter.Button(self.main_window,
                                      text="Calculate Total",
                                      command=self.calculate_total)

    self.calc_button.pack(pady=10)

    tkinter.mainloop()

  def calculate_total(self):
    total = sum(self.services[service]
                for service, var in self.check_vars.items() if var.get())
    self.total_label.config(text=f"Total Charges: ${total:.2f}")


if __name__ == '__main__':
  gui = MyGUI()
