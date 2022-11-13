#**********************************************************************************
# content		= cube.py
#               = Python Advanced Assignment
#
# date			= 10/11/2022
#
# author        = Enrico Vaccari <e.vaccari99@gmail.com>
#**********************************************************************************

"""
CUBE CLASS

1. CREATE an abstract class "Cube" with the functions:
   translate(x, y, z), rotate(x, y, z), scale(x, y, z) and color(R, G, B)
   All functions store and print out the data in the cube (translate, rotate, scale and color).

2. ADD an __init__(name) and create 3 cube objects.

3. ADD the function print_status() which prints all the variables nicely formatted.

4. ADD the function update_transform(ttype, value).
   "ttype" can be "translate", "rotate" and "scale" while "value" is a list of 3 floats.
   This function should trigger either the translate, rotate or scale function.

   BONUS: Can you do it without using ifs?

5. CREATE a parent class "Object" which has a name, translate, rotate and scale.
   Use Object as the parent for your Cube class.
   Update the Cube class to not repeat the content of Object.

"""

#**********************************************************************************
# SOLUTION (1)
#**********************************************************************************

'''
class Object:
    translate_val = [0, 0, 0]
    rotate_val    = [0, 0, 0]
    scale_val     = [1, 1, 1]

    def __init__(self, name):
        self.name = name

class Cube(Object):
    color_val     = [255, 255, 255]
   
    def print_status(self):
        print(f'Name: {self.name}')
        print(f'Translation values: {self.translate_val}')
        print(f'Rotate values:      {self.rotate_val}')
        print(f'Scale values:       {self.scale_val}')
        print(f'Color values:       {self.color_val}\n')

    def translate(self, x, y, z):
        self.translate_val = [x, y, z]
        print(self.translate_val)

    def rotate(self, x, y, z):
        self.rotate_val = [x, y, z]
        print(self.rotate_val)

    def scale(self, x, y, z):
        self.scale_val = [x, y, z]
        print(self.scale_val)

    def color(self, R, G, B):
        self.color_val = [R, G, B]
        print(self.color_val)

    def update_transform(self, ttype, value):
        if ttype == 'translate':
            self.translate(value[0], value[1], value[2])
        elif ttype == 'rotate':
            self.rotate(value[0], value[1], value[2])
        elif ttype == 'scale':
            self.scale(value[0], value[1], value[2])
    
    # without ifs (eval)

    # def update_transform(self, ttype, value):
    #     eval(f'self.{ttype}({value[0]}, {value[1]}, {value[2]})')

'''

#**********************************************************************************
# SOLUTION (2) - super() to print out info for both <parent> and <child> classes
#**********************************************************************************


class Object:
    translate_val = [0, 0, 0]
    rotate_val    = [0, 0, 0]
    scale_val     = [1, 1, 1]
   
    def __init__(self, name):
        self.name = name
        self.print_status()
   
    def print_status(self):
        print(f'\nName: {self.name}')
        print(f'Translation values: {self.translate_val}')
        print(f'Rotate values:      {self.rotate_val}')
        print(f'Scale values:       {self.scale_val}')

class Cube(Object):
    color_val     = [255, 255, 255]

    def print_status(self):
        super().print_status()
        print(f'Color values:       {self.color_val}\n')

    def translate(self, x, y, z):
        self.translate_val = [x, y, z]
        print(self.translate_val)

    def rotate(self, x, y, z):
        self.rotate_val = [x, y, z]
        print(self.rotate_val)

    def scale(self, x, y, z):
        self.scale_val = [x, y, z]
        print(self.scale_val)

    def color(self, R, G, B):
        self.color_val = [R, G, B]
        print(self.color_val)

    def update_transform(self, ttype, value):
        if ttype == 'translate':
            self.translate(value[0], value[1], value[2])
        elif ttype == 'rotate':
            self.rotate(value[0], value[1], value[2])
        elif ttype == 'scale':
            self.scale(value[0], value[1], value[2])
    
    # without ifs (eval)

    # def update_transform(self, ttype, value):
    #     eval(f'self.{ttype}({value[0]}, {value[1]}, {value[2]})')


#**********************************************************************************
# EXECUTION (SOLUTION 1)
#**********************************************************************************

'''
# example
object = Object('Any')
cube1 = Cube('cube1')
cube2 = Cube('cube2')
cube3 = Cube('cube3')

cube1.print_status()
cube2.print_status()
cube3.print_status()

cube1.translate(2,3,4)
cube1.print_status()
cube1.update_transform('scale', [1, 90, 80])
cube1.print_status()
'''

#**********************************************************************************
# EXECUTION (SOLUTION 2)
#**********************************************************************************


# example

# objects creation
object = Object('Any')
cube1 = Cube('cube1')
cube2 = Cube('cube2')
cube3 = Cube('cube3')

# print status
object.print_status()
cube1.print_status()
cube2.print_status()
cube3.print_status()

# changing transformation values
cube1.translate(2,3,4)
cube1.print_status()
cube1.update_transform('scale', [1, 90, 80])
cube1.print_status()
