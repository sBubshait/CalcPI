from mpmath import * # enable us to do arbitary precision arithmetic
import math

class CalcPI(): # Using Gauss–Legendre algorithm
    
    correctMillionDigits = open('millionDigitsOfPI.txt').read() # instead of reading each time.

    @staticmethod
    def correctUpTo(digits: int = 100):
        """Gives PI correct up to the number of digits provided (otherwise, 100). NB: this means that all the number of digits wanted will be correct. However, the result given might be in higher digits than that exact number provided.

    Parameters:
    digits (int): the number of digits (after 3.) of PI wanted. If not provided, then 100.
    
    Returns:
    str: returns a string containing only numbers representing PI correct up to the number of digits provided."""
        mp.dps = digits + 2 # the precision is digits + 2 to avoid rounding errors.
        a = mpf(1)
        b = fdiv(1, mp.sqrt(2))
        t = mpf(0.25)
        p = mpf(1)
        a0 = mpf(1)
        pi = mpf(1)

        for i in range(0, math.ceil(math.log2(digits if digits > 1 else 2))): # log2 is taken to get the number of iterations needed as Gauss-Legendre has a quadratic convergence
            a = fdiv(fadd(a, b), 2)
            b = sqrt(fmul(a0,b))
            t = fsub(t, fmul(p, power(fsub(a0,a),2)))
            p = fmul(p,2)
            pi = fdiv(power(fadd(a,b),2), fmul(t,4))
            a0 = a

        return str(pi)
    
    @staticmethod
    def check(piEstimate: str):
        """Checks a string of PI estimate provided correct up what number of digits.

    Parameters:
    piEstimate (str): a string represnting the PI estimate watned. This should include the integer part, i.e. (3.) as well as the decimal places.
    
    Returns:
    str: returns a string indicating the result of the check. It could either be 'Correct Up to X digits!' which indicates that it is correct only up to X digits or 'Matched all X digits!' which indicates that all the string provided is correct. NB: this checks the digits again, so if the number was for example (4.14) then it will be correct to -2 places which means that the integer part is incorrect. Similarly, (3.1) will be only correct to one digit."""
        length = len(piEstimate) if len(piEstimate) < 1000002 else 1000002
        for i in range(length):
            if piEstimate[i] != CalcPI.correctMillionDigits[i]: # To maximise efficiency, this checks the piEstiamte provided against previous data of the first million digits of PI calculated. This is ideal and fast for such application as it will probably not be used to discover new digits of PI.
                return 'Correct up to {} digits!'.format(i - 2)
        return 'Matched all {} digits!'.format(length - 2)