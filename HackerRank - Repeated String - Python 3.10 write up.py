##    https://www.hackerrank.com/challenges/repeated-string/problem

##    There is a string, s, of lowercase English letters that is repeated
##    infinitely many times. Given an integer, n, find and print the number of
##    letter a's in the first n letters of the infinite string.

##### ##### ##### #####

#   O(n)
#   n is the length of s
#   Idea:
#       If a finite string is repeated an infinite number of times,
#       then the number of times the entire finite string appears in
#       the first n letters of the infinite repetition is the floor
#       of n divided by the length of s.  If n is not evenly divisible
#       by the length of s, a single substring of size n mod length of s,
#       will appear.

#       For example:

#           s = 'abc'
#           n = 10

#           The length of s is 3, so the number of times the entire string
#           appears in the first n letters is the floor of 10 divided by 3.
#           10 mod 3 is 1 so a substring of length 1 appears at the end.

#           'abc abc abc a'

#   Algo:
#       1. Initiate variable to keep track of the number of a's in the given
#           string s => O(1)
#       2. Count the number of a's in the given string s => O(len(s))
#       3. Initiate variable to keep track of the number of a's in first n
#           characters of the infinite string s.  Set this variable equal
#           to a_count * (n // length of s) => O(1)
#       4. Count the number in the a's that appear in the remaining single
#           substring and add this to total a count => O(n mod(len(s))

def repeatedString(s, n):
    
    a_count = 0
    
    for char in s:
        
        if char == 'a':
            a_count += 1
            
    total_a_count = a_count * (n // len(s))
    
    for char in s[:n % len(s)]:
        
        if char == 'a':
            total_a_count += 1
            
    return total_a_count
