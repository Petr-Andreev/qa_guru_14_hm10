import dataclasses


@dataclasses.dataclass
class User:
    repo: str
    text_for_search: str
    text_for_should: str


admin = User(repo='Petr-Andreev/qa_guru_14_hm10',
             text_for_search='Test title',
             text_for_should='Test title')
