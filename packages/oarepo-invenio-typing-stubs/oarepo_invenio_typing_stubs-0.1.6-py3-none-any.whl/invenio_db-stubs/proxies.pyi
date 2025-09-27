from invenio_db.shared import SQLAlchemy
from werkzeug.local import LocalProxy

current_db: LocalProxy[SQLAlchemy]
