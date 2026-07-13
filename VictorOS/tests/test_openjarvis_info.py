#import openjarvis
#
#print("OpenJarvis exports:")
#print(dir(openjarvis))
from openjarvis import Jarvis

j = Jarvis()

print("=== Direct ===")
print(j.ask("Hello"))

print("\n=== Full ===")
print(j.ask_full("What is 2+2?"))

j.close()