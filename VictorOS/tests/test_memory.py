from openjarvis import Jarvis

j = Jarvis()

print("Version:", j.version)

print()

print("Memory stats:")
print(j.memory.stats())

j.close()