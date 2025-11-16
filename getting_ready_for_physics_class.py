"""
Getting Ready for Physics Class

You are a physics teacher preparing for the upcoming semester. You want to provide your students with some functions that will help them calculate 
some fundamental physical properties.
"""

# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


### Defining a function to convert tempeture from Fahrenheit to Celsius
def f_to_c(f_temp):
  return (f_temp - 32) * 5/9

f100_in_celsius = f_to_c(100)
# print(f100_in_celsius)

# Defining a function to convert tempeture from Celsius to Fahrenheit
def c_to_f(c_temp):
  return (c_temp * (9/5)) + 32 

c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

### Returns the force given mass and acceleration
def get_force(mass, acceleration):
  return mass * acceleration

### Testing the get_force() function.
train_force = get_force(train_mass, train_acceleration)
# print(train_force)

print(f"The GE train supplies {train_force} Newtons of force.")

### Defining a function called get_energy()
def get_energy(mass, c=3*10**8):
  return mass * c ** 2

### Testing the get_energy() function.
bomb_energy = get_energy(bomb_mass)

print(f"A 1kg bomb supplies {bomb_energy} Joules.")

### Defining a function called get_work()
def get_work(mass, acceleration, distance):
  return get_force(mass, acceleration) * distance

### Testing the get_work() function.
train_work = get_work(train_mass, train_acceleration, train_distance)

print(f"The GE train does {train_work} Joules of work over {train_distance}.")