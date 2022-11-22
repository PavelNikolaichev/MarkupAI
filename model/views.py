from django.shortcuts import render
from django.views import View

from natasha import (
    Segmenter,
    MorphVocab,

    NewsEmbedding,
    NewsMorphTagger,
    NewsSyntaxParser,
    NewsNERTagger,

    NamesExtractor,
    AddrExtractor,
    Doc
)


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
        doc = Doc(text)

        doc.segment(self.segmenter)

        doc.tag_ner(self.ner_tagger)

        # for span in doc.spans:
        #     if span.type == 'LOC':
        #         print(f'Type: {span.type}, Text: {span.text}')

        return self.addr_extractor.find(doc.text)


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        text = request.POST.get('text')
        model = AIModel()
        result = model.perform(text)
        return render(request, 'index.html', {'result': result})
