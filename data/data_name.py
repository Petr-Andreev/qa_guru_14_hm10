import dataclasses


@dataclasses.dataclass
class Data:
    repo: str
    text_for_search: str
    text_for_should: str


issue = Data(repo='Petr-Andreev/qa_guru_14_hm10',
             text_for_search='Test title',
             text_for_should='Test title')
