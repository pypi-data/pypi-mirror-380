from typing import ClassVar, Collection

from invenio_records_permissions import RecordPermissionPolicy
from invenio_records_permissions.generators import Generator
from invenio_requests.services.generators import Commenter as Commenter
from invenio_requests.services.generators import Creator as Creator
from invenio_requests.services.generators import Receiver as Receiver
from invenio_requests.services.generators import Reviewers as Reviewers
from invenio_requests.services.generators import Status as Status
from invenio_requests.services.generators import Topic as Topic

class PermissionPolicy(RecordPermissionPolicy):
    can_create: ClassVar[Collection[Generator]]
    can_search: ClassVar[Collection[Generator]]
    can_search_user_requests = can_search
    can_read: ClassVar[Collection[Generator]]
    can_update: ClassVar[Collection[Generator]]
    can_manage_access_options: ClassVar[Collection[Generator]]
    can_action_delete: ClassVar[Collection[Generator]]
    can_action_submit: ClassVar[Collection[Generator]]
    can_action_cancel: ClassVar[Collection[Generator]]
    can_action_expire: ClassVar[Collection[Generator]]
    can_action_accept: ClassVar[Collection[Generator]]
    can_action_decline: ClassVar[Collection[Generator]]
    can_update_comment: ClassVar[Collection[Generator]]
    can_delete_comment: ClassVar[Collection[Generator]]
    can_create_comment: ClassVar[Collection[Generator]]
    can_unused: ClassVar[Collection[Generator]]
