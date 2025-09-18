def reverse_int(n,number=0):
    if n==0:
        return number
    else:
        digit=n%10
        return reverse_int(n//10,number*10+digit)
def is_plindrome(n):
    return reverse_int(n)==n
