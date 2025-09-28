class AstralAI:
    def __init__(self, model="basic"):
        self.model = model

    def predict(self, text: str) -> str:
        return f"[{self.model}] Response to: {text}"
