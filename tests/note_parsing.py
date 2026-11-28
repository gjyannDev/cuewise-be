"""`parse_note` and `load_corpus` with the real section splitter, for tests that want the notes as the app reads them.

The utils take the splitter as an argument (it is LangChain code, so it lives in `ai/`; tests/test_layers.py keeps
`utils/` below it); the app passes it from `ai/interviews_split.py`.
"""

from functools import partial

from app.modules.interviews.ai.interviews_split import split_sections
from app.modules.interviews.utils import interviews_knowledge_utils as _utils

parse_note = partial(_utils.parse_note, split=split_sections)
load_corpus = partial(_utils.load_corpus, split=split_sections)
