class Vehicle:
  def __init__(self, type):
    self.type = type

  def drive(self, speed):
    self.mode = "driving"
    self.speed = speed

class Car(Vehicle):
  def __init__(self, enginetype):
    super().__init__("Car")
    self.wheels = 4
    self.doors = 4
    self.enginetype = enginetype

  def drive(self, speed):
    super().drive(speed)
    print("driving my", self.enginetype, "car at", self.speed)


class Motorcycle(Vehicle):
  def __init__(self, enginetype, hassidecar):
    super().__init__("Motorcycle")
    if (hassidecar):
      self.wheels = 3
    else:
      self.wheels = 2

    self.doors = 0
    self.enginetype = enginetype

  def drive(self, speed):
    super().drive(speed)
    print("driving my", self.enginetype, "motorcycle at", self.speed)

car1 = Car("gas")
car2 = Car("electric")
mc1 = Motorcycle("gas", True)
mc2 = Motorcycle("gas", False)

print(mc1.wheels)
print(car1.enginetype)
print(mc2.wheels)

car1.drive(50)
car2.drive(60)
mc1.drive(70)
mc2.drive(65)