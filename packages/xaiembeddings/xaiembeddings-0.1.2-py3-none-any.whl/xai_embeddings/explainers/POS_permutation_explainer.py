import pickle
from .explainer import Explainer
from .explanation import Explanation
from ..models.model import Model
from ..distances import cosine_distance, euclidean_distance
import spacy
import random
import copy


class POS_explainer(Explainer):
    """
    Permutation feature importance considering parts of speech.
    Changes a token n times to another with the same part of speech
    and calculates the distance to the analyzed embedding.
    This allows assessing the influence of a given token on the embedding.
    Uses a dictionary of parts of speech, which is loaded from a file.
    """

    def __init__(self, model: Model, **kwargs):
        self.model = model
        self.distance = kwargs.get("distance", cosine_distance)
        path = kwargs.get("pos_dict", None)
        spaCyModel = kwargs.get("spacy", "en_core_web_trf")
        self.pos_tagger = spacy.load(spaCyModel)

        # Dictionary with POS tags as keys and lists of words as values
        self.pos_dict: dict = self.load_pos_dict(path)

        # Number of permutations for each token
        self.n = kwargs.get("n", 100)

    def explainEmbeddings(self, sentence, word_range=None, **kwargs) -> Explanation:
        tokens = self.model.tokenizer.tokenize(sentence)

        embeddings = self.model.get_embeddings(sentence)

        # POS tag list
        pos_tags = self.tag_tokens(tokens)

        if word_range is None:
            word_range = (0, len(tokens))

        # Reconstruct the sentence from the tokens in the specified range
        analyzed_tokens = tokens[word_range[0] : word_range[1]]
        anazlyzed_sentence = self.model.reconstruct_sentence(analyzed_tokens)

        # Create an explanation object
        explanation = Explanation(
            f"POS-PFI{self.n}", anazlyzed_sentence, analyzed_tokens
        )

        # Iterate over the specified range of tokens
        for word in range(word_range[0], word_range[1]):
            token = tokens[word]

            # Get word scores
            word_scores = self.get_word_score(
                token, word, pos_tags, tokens, embeddings, sentence
            )

            # Add scores to the explanation
            for sub_pos, score in enumerate(tokens):
                explanation.add_one_word(
                    token, word, score, sub_pos, word_scores[score]
                )

        return explanation

    # Load POS dictionary from a file
    def load_pos_dict(self, pos_dict_path):
        with open(pos_dict_path, "rb") as f:
            self.pos_dict = pickle.load(f)
        if not isinstance(self.pos_dict, dict):
            raise ValueError("Loaded POS dictionary is not a dictionary")
        return self.pos_dict

    # Tag tokens with their POS tags
    def tag_tokens(self, tokens):
        pos_tags = []
        for token in tokens:
            if token.startswith("##"):
                if not pos_tags[-1] == ("SUBWORD"):
                    pos_tags[-1] = "SUBWORD"
                pos_tags.append("SUBWORD")
            else:
                try:
                    doc = self.pos_tagger(token)
                    pos_tags.append(doc[0].pos_)
                except:
                    pos_tags.append("X")

        return pos_tags

    # Make a sentence with a change at a specific position
    def make_sentence(self, change, position, tokens):
        copy_tokens = copy.deepcopy(tokens)
        copy_tokens[position] = change
        return self.model.reconstruct_sentence(copy_tokens)

    # Calculate the score for a word based on its POS tag
    def get_word_score(self, word, position, pos_tags, tokens, embeddings, sentence):
        pos_tag = pos_tags[position]

        if pos_tag == "SUBWORD":
            return self.subword_score(position, tokens, embeddings, sentence)

        scores = {}
        for token in tokens:
            scores[token] = 0.0

        for n in range(self.n):
            replacement = random.choice(self.pos_dict[pos_tag])
            permuted_sentence = self.make_sentence(replacement, position, tokens)
            permuted_embeddings = self.model.get_embeddings(permuted_sentence)

            for i, tok in enumerate(tokens):
                distance = self.distance(embeddings[i], permuted_embeddings[i])
                scores[tok] += distance

        for key in scores:
            scores[key] /= self.n

        return scores

    def explainOne(self, sentence, position, **kwargs) -> Explanation:
        return self.explainEmbeddings(
            sentence, word_range=(position, position + 1), **kwargs
        )

    def subword_score(self, position, tokens, embeddings, sentence: str):

        # Find the start of the subword
        subword_start = position
        while subword_start > 0 and tokens[subword_start].startswith("##"):
            subword_start -= 1

        # Get the complete word and its POS tag
        word_pos = 0
        sentence_split = sentence.split()
        for i in range(subword_start):
            if not tokens[i].startswith("##") or tokens[i] in ".,!?;":
                word_pos += 1

        complete_word = sentence_split[word_pos]
        pos_tag = self.pos_tagger(complete_word)[0].pos_
        iter = 0
        subword_end = len(tokens) - 1
        for i in range(subword_start + 1, len(tokens)):
            if tokens[i].startswith("##"):
                subword_end = i
                for j in range(2, len(tokens[i])):
                    iter += 1
                    if iter >= len(complete_word):
                        break
            else:
                break

        scores = {}
        for token in tokens:
            scores[token] = 0.0

        for n in range(self.n):
            sentence_split[word_pos] = random.choice(self.pos_dict[pos_tag])
            permuted_sentence = " ".join(sentence_split)
            permuted_embeddings = self.model.get_embeddings(permuted_sentence)

            for i, tok in enumerate(tokens[:subword_start]):
                distance = self.distance(embeddings[i], permuted_embeddings[i])
                scores[tok] += distance

            for i, tok in enumerate(tokens[-subword_end + 1 :]):
                distance = self.distance(embeddings[i], permuted_embeddings[i])
                scores[tok] += distance

        for key in scores:
            scores[key] /= self.n

        return scores
