"""Define PIDStore proxies.

Type stubs for invenio_pidstore.proxies.
"""

from invenio_pidstore.ext import _PIDStoreState
from werkzeug.local import LocalProxy

current_pidstore: LocalProxy[_PIDStoreState]
