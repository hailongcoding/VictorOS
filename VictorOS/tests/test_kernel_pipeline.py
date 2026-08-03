from VictorOS.core.kernel import Kernel

kernel = Kernel()

kernel.boot()

requests = kernel.execute(
    "Research Apple then code me a landing page."
)

print("=" * 40)

for request in requests:
    print(request.capability)
    print(request.payload)