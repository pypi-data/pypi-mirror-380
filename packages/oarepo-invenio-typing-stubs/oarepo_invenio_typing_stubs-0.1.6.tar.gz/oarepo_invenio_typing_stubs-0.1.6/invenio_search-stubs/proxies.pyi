from typing import Any

from invenio_search.ext import _SearchState
from werkzeug.local import LocalProxy

def _get_current_search() -> _SearchState: ...
def _get_current_search_client() -> Any: ...

current_search: LocalProxy[_SearchState]
current_search_client: LocalProxy[Any]
