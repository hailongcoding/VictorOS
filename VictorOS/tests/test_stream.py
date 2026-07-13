from JarvisOS.services.brain.openjarvis_adapter import OpenJarvisAdapter

adapter = OpenJarvisAdapter()

messages = [
    {
        "role": "user",
        "content": "Tell me a joke."
    }
]

print("Streaming...\n")

for token in adapter.stream_chat(messages):
    print(token, end="", flush=True)

print("\nDone.")

adapter.close()