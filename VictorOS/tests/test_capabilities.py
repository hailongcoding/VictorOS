from openjarvis import Jarvis

j = Jarvis()

print("=== MODELS ===")
print(j.list_models())

print()

print("=== ASK ===")
print(j.ask("Hello"))

j.close()