import statistics
#Median Calculator

def orderNumbers(numbers):
    return (sorted(numbers))

def findMedian(numbers):
    return (statistics.median(map(float,numbers)))

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        print(numbers)
        numbers = orderNumbers(numbers)
        print(numbers)
        print(findMedian(numbers))
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

