from CalcPI import CalcPI
import time

# test it yourself!
# Calcuating the first million digits of PI (& the time needed)!
start = time.time()
firstMillion = CalcPI.correctUpTo(1_000_000)
end = time.time()

print(firstMillion)
print("Took {} seconds!".format(end-start))
print("Checking..", CalcPI.check(firstMillion))