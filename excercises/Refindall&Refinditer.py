# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
S = input()
matches = re.findall(r'[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]([AEIOUaeiou]{2,})(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])', S)
print("\n".join(matches) if matches != [] else -1)
