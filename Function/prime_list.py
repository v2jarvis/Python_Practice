#Write a function that takes a list of numbers as input and returns a new list containing
#only the prime numbers from the original list.
def prime_val(l1):
    def prime(num):
        if num < 2:
            return False
        for i in range(2, int(num//2)+1):
            if num%i==0:
                return False
        return True

    l2=[]
    for num in l1:
        if prime(num):
            l2.append(num)
    return l2

num=[1,2,3,4,5,6,7,8,9,10]
print(prime_val(num))
