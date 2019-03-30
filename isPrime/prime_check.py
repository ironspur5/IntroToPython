# Patrick Guha psg486


# dont use num, num is a python defined keyword; use something like numb instead
def isPrime(numb):

    # prime numbers are greater than 1
    if numb > 1:
        # check for factors
        for i in range(2, numb):  # for loops in python
            if (numb % i) == 0:  # modulo (remainder) num with index up to it
                print(numb, "is not a prime number")
                break
        else:
            print(numb, "is a prime number")

    # if input number is less than or equal to 1, it is not prime
    else:
        print(numb, "is not a prime number")


# There is no main in python!

# cast character keyboard input to int
input = int(input("Enter a number: "))

isPrime(input)










