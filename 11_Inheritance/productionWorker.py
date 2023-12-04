from employee import Employee


class ProductionWorker(Employee):

  def __init__(self, name, number, shift, pay):
    self.set_shift(shift)
    self.__pay = pay
    Employee.__init__(self, name, number)

  def set_shift(self, shift):
    if shift == '1':
      self.__shift = "Day"
    elif shift == '2':
      self.__shift = "Night"
    else:
      self.__shift = "Enter 1 for Day or 2 for Night"

  def set_pay(self, pay):
    self.__pay = pay

  def get_shift(self):
    return self.__shift

  def get_pay(self):
    return self.__pay
