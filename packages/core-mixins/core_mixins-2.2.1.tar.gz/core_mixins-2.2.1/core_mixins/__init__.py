# -*- coding: utf-8 -*-

try:
    from enum import StrEnum as _StrEnum

except ImportError:
    from core_mixins.compatibility import StrEnum as _StrEnum  # type: ignore[assignment]


# Type alias that works with both standard library
# and the custom HTTPStatus...
StrEnum = _StrEnum
