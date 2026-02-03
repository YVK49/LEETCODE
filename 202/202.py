class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n!=1:
            if n in seen:
                return False
            seen.add(n)
            list_of_numbers = list(str(n))
            sum_of_squares = 0
            for digits in list_of_numbers:
                sum_of_squares+=int(digits)**2
            n=sum_of_squares
        return True     