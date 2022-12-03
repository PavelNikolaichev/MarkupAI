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

    # TODO: Add spell check
    def perform(self, text) -> str:
        doc = Doc(text)
        doc.segment(self.segmenter)
        doc.tag_ner(self.ner_tagger)

        a = [span.text for span in doc.spans if span.type == 'LOC']
        a.extend([f'{part.type} {part.value}' for part in self.addr_extractor.find(doc.text).fact.parts])
        return ' '.join(a)

# class IndexView(View):
#     def get(self, request):
#         return render(request, 'index.html')
#
#     def post(self, request):
#         text = request.POST.get('text')
#         model = AIModel()
#         result = model.perform(text)
#         return render(request, 'index.html', {'result': result})
