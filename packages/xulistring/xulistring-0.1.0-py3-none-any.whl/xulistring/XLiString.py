import re

class XLiString:
    def __init__(self, value=None) -> None:
        self.value = value

    @staticmethod
    def strip_punct(sentence: str) -> str:
        sentence = sentence.lower()
        return re.sub(r'[^\w\s]', ' ', sentence, flags=re.UNICODE).strip()
    
    @staticmethod
    def process_Sentence(sentence: str):
        sentence = XLiString.strip_punct(sentence)
        return sentence.split()

class MaHoa:
    @staticmethod
    def Diction(sentences):
        dictionary = set()
        for sentence in sentences:
            dictionary.update(XLiString.process_Sentence(sentence))
        return {w: i for i, w in enumerate(sorted(dictionary))}
