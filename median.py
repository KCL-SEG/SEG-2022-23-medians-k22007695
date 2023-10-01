import statistics
#Median Calculator

#Orders list
def orderNumbers(numbers):
    return (sorted(numbers))

#Finds median of list
def findMedian(numbers):
    return (statistics.median(map(float,numbers)))

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

numbers = orderNumbers(numbers)
print("Hello")
print(findMedian(numbers))

