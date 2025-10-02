import torch
import numpy as np
from transformers import AutoTokenizer, AutoModelForSequenceClassification

class ZeroShotClassifier:
    def __init__(self, model_name="PratikChourasia2/classification_model", label_dict=None, device=None):
        # Default labels
        if label_dict is None:
            label_dict = {
                "healthcare": 0,
                "travel": 1
            }
        self.label_dict = label_dict
        self.label_map = {v: k for k, v in label_dict.items()}

        # Load model + tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)

        # Device setup
        if device:
            self.device = device
        else:
            self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)
        self.model.eval()

    def predict(self, text: str) -> str:
        """Predict category for a given input text."""
        encoded_input = self.tokenizer.encode_plus(
            text,
            add_special_tokens=True,
            return_attention_mask=True,
            padding="max_length",
            max_length=64,
            return_tensors="pt"
        )

        input_ids = encoded_input["input_ids"].to(self.device)
        attention_mask = encoded_input["attention_mask"].to(self.device)

        with torch.no_grad():
            outputs = self.model(input_ids, attention_mask=attention_mask)
            logits = outputs.logits

        logits = logits.detach().cpu().numpy()
        predicted_index = np.argmax(logits)
        return self.label_map[predicted_index]

