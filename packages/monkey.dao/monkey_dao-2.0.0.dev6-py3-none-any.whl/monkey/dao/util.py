# -*- coding: utf-8 -*-
"""
Provides constants for ascending and descending sort orders that can
be used in sorting implementations. Additionally, it defines the `OperationType`
enumeration which specifies CRUD-like operations for different contexts.
"""

from enum import Enum

ASC = ASCENDING = 1
"""Ascending sort order"""

DESC = DESCENDING = -1
"""Descending sort order"""


class OperationType(Enum):
    """
    Defines the OperationType enumeration that represents CRUD-like operations.

    This enumeration is used to specify the type of operation being performed,
    such as inserting, updating, deleting, or replacing. It can be used in
    contexts where a clear definition of the operation type is required.

    :ivar INSERT: Represents the "insert" operation.
    :type INSERT: str
    :ivar UPDATE: Represents the "update" operation.
    :type UPDATE: str
    :ivar DELETE: Represents the "delete" operation.
    :type DELETE: str
    :ivar REPLACE: Represents the "replace" operation.
    :type REPLACE: str
    """

    INSERT = "insert"
    UPDATE = "update"
    DELETE = "delete"
    REPLACE = "replace"
