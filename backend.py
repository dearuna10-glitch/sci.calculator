
import math


n = int(input("How many numbers do you want to enter? "))
numbers = []

for i in range(n):
    num = int(input("Enter a number: "))
    numbers.append(num)

def calculator(numbers):
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("6. Power")
    print("7. Modulus")
    print("8. root")
    print("9. Square root")
    print("10. Factorial")
    print("11. sine")
    print("12. cosine")
    print("13. tangent")
    print("14. logarithm")
    print("15.Radian to degree")
    print("16.Degree to radian")
    print("17. Percentage")
    print("18. pi")
    print("19. antilog")
    print("20. exponential")
    print("21. inverse trigonometric functions")
    print("22. hyperbolic functions")
    print("23. inverse hyperbolic functions")
    print("24. Integral")
    print("25. Derivative")
    print("26. Combination")
    print("27. Permutation")
    print("28. Matrix operations")
    print("29. Complex number operations")
    print("30. Solve equations")

    choice = input("Enter choice (1/2/3/4/6/7/8/9/10/11/12/13/14/15/16/17/18/19/20/21/22/23/24/25/26/27/28/29/30): ")

    if choice == '1':
        return sum(numbers)
    elif choice == '2':
        return numbers[0] - sum(numbers[1:])
    elif choice == '3':
        return math.prod(numbers)
    elif choice == '4':
        if len(numbers) > 2:
            return "Error!  more than 2 bro try again."
        elif numbers[1] != 0:
            return numbers[0] / numbers[1]
        else:
            return "Error! Division by zero."
    elif choice == '6':
        if len(numbers) > 2:
            return "Error! more than 2 bro try again."
        return numbers[0] ** numbers[1]
    elif choice == '7':
        if len(numbers) > 2:
            return "Error! more than 2 bro try again."
        return numbers[0] % numbers[1]
    elif choice == '8':
        if len(numbers) > 2:
            return "Error! more than 2 bro try again."
        elif numbers[1] != 0:
            return numbers[0] ** (1/numbers[1])
        else:
            return "Error! Invalid root."
    elif choice == '9':
        if numbers[0] < 0:
            return "Error! Invalid input for square root."
        if len(numbers) > 1:
            return "Error! more than 1 number provided for square root."
        return numbers[0] ** 0.5
    elif choice == '10':
        if len(numbers) > 1:
            return "Error! more than 1 number provided for factorial."
        elif numbers[0] >= 0:
            return math.factorial(numbers[0])
        else:
            return "Error! Invalid input for factorial."
    elif choice == '11':
        return math.sin(numbers[0])
    elif choice == '12':
        return math.cos(numbers[0])
    elif choice == '13':
        return math.tan(numbers[0])
    elif choice == '14':
        if len(numbers) > 1:
            return "Error! more than 1 number provided for logarithm."
        if numbers[0] > 0:
            return math.log(numbers[0])
        else:
            return "Error! Invalid input for logarithm."
    elif choice == '15':
        if len(numbers) > 1:
            return "Error! more than 1 number provided for degrees."
        return math.degrees(numbers[0])
    elif choice == '16':
        if len(numbers) > 1:
            return "Error! more than 1 number provided for radians."
        return math.radians(numbers[0])
    elif choice == '17':
        if len(numbers) > 2:
            return "Error! more than 2 numbers provided for percentage."
        return (numbers[0] / 100) * numbers[1]
    elif choice == '18':
        if len(numbers) > 0:
            return "Error! No numbers should be provided for pi."
        return math.pi
    elif choice == '19':
        if len(numbers) > 1:
            return "Error! more than 1 number provided for power of 10."
        return 10 ** numbers[0]
    elif choice == '20':
        if len(numbers) > 1:
            return "Error! more than 1 number provided for exponential."
            return math.exp(numbers[0])
    elif choice == '21':
        if len(numbers) > 1:
            return "Error! more than 1 number provided for inverse trigonometric functions."
        return math.asin(numbers[0])
    elif choice == '22':
        if len(numbers) > 1:
            return "Error! more than 1 number provided for hyperbolic functions."
        return math.sinh(numbers[0])
    elif choice == '23':
        if len(numbers) > 1:
            return "Error! more than 1 number provided for inverse hyperbolic functions."
        return math.asinh(numbers[0])
    elif choice == '24':
        if len(numbers) > 1:
            return "Error! more than 1 number provided for integral."
        return math.integral(numbers[0])
    elif choice == '25':
        if len(numbers) > 1:
            return "Error! more than 1 number provided for derivative."
        return math.derivative(numbers[0])
    elif choice == '26':
        if len(numbers) > 2:
            return "Error! more than 2 numbers provided for combination."
        return math.combination(numbers[0], numbers[1])
    elif choice == '27':
        if len(numbers) > 2:
            return "Error! more than 2 numbers provided for permutation."
        return math.permutation(numbers[0], numbers[1])
    elif choice == '28':
        if len(numbers) > 2:
            return "Error! more than 2 numbers provided for matrix operations."
        return math.matrix_operations(numbers[0], numbers[1])
    elif choice == '29':
        if len(numbers) > 2:
            return "Error! more than 2 numbers provided for complex number operations."
        return math.complex_number_operations(numbers[0], numbers[1])
    elif choice == '30':
        if len(numbers) > 2:
            return "Error! more than 2 numbers provided for solving equations."
        return math.solve_equations(numbers[0], numbers[1])
    else:
        return "Invalid input"
number = calculator(numbers)

print("Result:", number)
    