

class Calculator:
    @staticmethod
    def add(a,b):
        return a+b
    
    @staticmethod
    def subtract(a,b):
        return a-b
    
    @staticmethod
    def multiply(a,b):
        return a*b
    
    @staticmethod
    def divide(a,b):
        if b==0:
            return "Error: Cannot divide by zero"
        return a/b
    
# No need to create object – directly call using class name

print(Calculator.add(5,2))
print(Calculator.subtract(5,2))
print(Calculator.multiply(5,2))
print(Calculator.divide(5,2))