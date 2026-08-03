from VictorOS.services.ai.providers.ollama import OllamaProvider
from VictorOS.services.intent.builder import PromptPackage
from VictorOS.services.ai.pipeline.response_normalizer import ResponseNormalizer

class AIClient:

    def __init__(self):

        self.provider = OllamaProvider()

        self.normalizer = ResponseNormalizer()

    def chat(
        self,
        *,
        model: str,
        package: PromptPackage,
        stream: bool = False,
        think: bool = False,
    ) -> str:

        messages = [
            {
                "role": "system",
                "content": package.system,
            },
            {
                "role": "user",
                "content": package.user,
            },
        ]

        # print("=" * 50)
        # print("MODEL:", model)
        # print("SYSTEM:")
        # print(package.system)
        # print()
        # print("USER:")
        # print(package.user)
        # print("=" * 50)

        response = self.provider.chat(
            model=model,
            messages=messages,
            stream=stream,
            think=think,
        )

        return self.normalizer.normalize(response)