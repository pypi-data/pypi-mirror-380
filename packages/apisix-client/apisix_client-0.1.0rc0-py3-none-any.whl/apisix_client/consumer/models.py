from datetime import datetime

import attrs

from apisix_client.common.converter import str_or_none
from apisix_client.plugin import Plugins


@attrs.define()
class ConsumerResponse:
    create_time: datetime = attrs.field(converter=datetime.fromtimestamp)
    update_time: datetime = attrs.field(converter=datetime.fromtimestamp)
    username: str = attrs.field(converter=str)
    desc: str | None = attrs.field(converter=str_or_none, default=None)
    plugins: Plugins | None = attrs.field(default=None)


@attrs.define()
class Consumer:
    username: str = attrs.field(converter=str)
    group_id: str | None = attrs.field(converter=str_or_none, default=None)
    plugins: Plugins | None = attrs.field(default=None)
    desc: str | None = attrs.field(converter=str_or_none, default=None)
    labels: dict | None = attrs.field(default=None)
