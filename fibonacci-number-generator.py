
print("===== Fibonacci Number Generator =====")

while True:
    n = input("\nEnter the number of terms: ")

    if not n.isdigit() or int(n) == 0:
        print("Please enter a positive whole number!")
        continue

    n = int(n)
    a = 0
    b = 1
    total = 0

    print("\nFibonacci Series:")

    for i in range(n):
        print(a, end=" ")
        total += a
        a, b = b, a + b

    print("\n\nTotal Terms:", n)
    print("Sum of Series:", total)

    again = input("\nGenerate another series? (y/n): ").lower()

    if again != "y":
        print("Thank you for using Fibonacci Generator!")
        break
