from .explainer import Explainer
from ..models.model import Model
from .explanation import Explanation
import torch
import numpy as np
import warnings


class BertAttentionExplainer(Explainer):
    """
    BERT specific attention explainer.
    Uses attention weights from BERT to explain token influence.
    Supports different aggregation methods (sum, mean, max).
    """

    def __init__(self, model: Model, **kwargs):
        self.model = model
        self.aggregation_method = kwargs.get(
            "aggregation_method", "sum"
        )  # Options: sum, mean, max
        self.silent = kwargs.get("silent", False)
        self.sep_cls = kwargs.get("sep_cls", False)

    def explainEmbeddings(self, sentence, word_idx=None, **kwargs) -> Explanation:
        if self.silent:
            warnings.filterwarnings("ignore")
        tokens = self.model.tokenize(sentence)

        # Get attention weights from the modelrt
        attention_weights = self._get_attention_weights(sentence)

        # Create explanation object
        explanation = Explanation("attention", sentence, tokens)

        # Process attention weights and add to explanation
        if word_idx is not None:
            # Explain only the specified token
            if not self.silent:
                print(f'Explaining token: "{tokens[word_idx]}"')
            self._process_token_attention(
                tokens, attention_weights, explanation, word_idx
            )
        else:
            # Explain all tokens
            for idx in range(len(tokens)):
                if not self.silent:
                    print(f'Token "{tokens[idx]}": {idx+1}/{len(tokens)}')
                self._process_token_attention(
                    tokens, attention_weights, explanation, idx
                )

        return explanation

    def explainOne(self, sentence, position=None, **kwargs) -> Explanation:
        return self.explainEmbeddings(sentence, position, **kwargs)

    def _get_attention_weights(self, sentence):
        # Tokenize input
        inputs = self.model.tokenizer(sentence, return_tensors="pt")
        input_ids = inputs["input_ids"].to(self.model.device)
        attention_mask = inputs["attention_mask"].to(self.model.device)

        self.model.model.to(self.model.device)
        with torch.no_grad():
            outputs = self.model.model(
                input_ids=input_ids,
                attention_mask=attention_mask
                )
        attention_weights = outputs.attentions

        return attention_weights

    def _process_token_attention(
        self, tokens, attention_weights, explanation, token_idx
    ):
        # Convert attention_weights to numpy arrays for easier manipulation
        attn_arrays = [attn_layer.cpu().numpy()[0] for attn_layer in attention_weights]

        # Aggregate attention weights across all layers and heads
        aggregated_attention = self._aggregate_attention_weights(attn_arrays)

        # Adjust index for CLS token (BERT adds [CLS] at beginning)
        if self.sep_cls:
            bert_token_idx = token_idx  # No adjustment needed
        else:
            bert_token_idx = token_idx + 1

        # Get attention scores for this token (how much it attends to other tokens)
        if self.sep_cls:
            token_attention = aggregated_attention[
                bert_token_idx
            ]  # No exclusion of [CLS] and [SEP]
        else:
            token_attention = aggregated_attention[
                bert_token_idx, 1:-1
            ]  # Exclude [CLS] and [SEP]

        # Add scores to explanation object
        for i, score in enumerate(token_attention):
            explanation.add_one_word(
                tokens[token_idx],  # Main token
                token_idx,  # Main position
                tokens[i],  # Sub token
                i,  # Sub position
                float(score),  # Attention score
            )

    def _aggregate_attention_weights(self, attention_arrays):
        # Stack all layers
        all_layers = np.stack(attention_arrays)

        # Aggregate across layers and heads
        if self.aggregation_method == "sum":
            # Sum across all layers and heads
            return np.sum(all_layers, axis=(0, 1))
        elif self.aggregation_method == "mean":
            # Average across all layers and heads
            return np.mean(all_layers, axis=(0, 1))
        elif self.aggregation_method == "max":
            # Take maximum attention score across all layers and heads
            return np.max(all_layers, axis=(0, 1))
        else:
            raise ValueError(f"Unknown aggregation method: {self.aggregation_method}")
