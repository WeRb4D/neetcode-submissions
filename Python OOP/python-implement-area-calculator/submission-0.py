import math

class AreaCalc:
    # TODO: Implement calculate method
    def calculate(self, *args):
        if len(args) == 2:
            result = args[0] * args[1]
            return result
        else:
            result = (3.14159 * (args[0]**2))
            result = round(result, 2)
            return result    

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
