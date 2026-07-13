from JarvisOS.services.openjarvis.adapter import OpenJarvisAdapter
brain = OpenJarvisAdapter()

print(brain.ask("Say hello in one sentence."))

brain.close()