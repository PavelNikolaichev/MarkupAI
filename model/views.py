from django.shortcuts import render
from natasha import (
    Segmenter,
    MorphVocab,

    NewsEmbedding,
    NewsMorphTagger,
    NewsSyntaxParser,
    NewsNERTagger,

    PER,
    NamesExtractor,
    AddrExtractor,
    Doc
)


# Create your views here.

# TODO: make this class in the separate file. Also it would be cool to make an Interface or an Abstract class
class AIModel:
    def __init__(self):
        self.segmenter = Segmenter()
        self.morph_vocab = MorphVocab()

        self.emb = NewsEmbedding()
        self.addr_extractor = AddrExtractor(self.morph_vocab)
        self.morph_tagger = NewsMorphTagger(self.emb)
        self.syntax_parser = NewsSyntaxParser(self.emb)
        self.ner_tagger = NewsNERTagger(self.emb)

        self.names_extractor = NamesExtractor(self.morph_vocab)

    def perform(self, text) -> list:
        # TODO: clean up this mess.
        doc = Doc(text)

        doc.segment(self.segmenter)

        doc.tag_ner(self.ner_tagger)
        # for span in doc.spans:
        #     if span.type == 'LOC':
        #         print(f'Type: {span.type}, Text: {span.text}')

        prepared_data = []

        lines = [
            'Россия, Вологодская обл. г. Череповец, пр.Победы 93 б',
            '692909, РФ, Приморский край, г. Находка, ул. Добролюбова, 18',
            'ул. Народного Ополчения д. 9к.3',
            'В г.Москве загорелся дом на улице Ленина, 35.'
        ]

        for line in lines:
            prepared_data.append([self.addr_extractor.find(line).fact, line])
            display(self.addr_extractor.find(line).fact)
            print(line)
