from statistics import mean, median, mode
numbers = list(map(int, input("Enter space-separated numbers : ").split()))
print("Mean:", mean(numbers))
print("Median:", median(numbers))
print("Mode:", mode(numbers))
