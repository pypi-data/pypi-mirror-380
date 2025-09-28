# -*- coding: utf-8 -*-
"""
Encapsulates results of various database operations including delete, update, insert, and replace.

The module defines specialized classes for operation results, providing detailed insights
into the execution of common database actions. Each class represents a specific type of
database action and provides structured access to the results, including the count of records affected
and any associated raw data.
"""
from abc import ABC
from typing import Any, List, Optional

from monkey.dao.errors import UnsupportedFeatureError
from monkey.dao.util import OperationType


class OperationResult(ABC):
    """
    Represents the result of an operation.

    This class contains details of the operation result, including the type of operation, the number of records
    involved, and the raw result.

    :ivar op_type: The type of the operation.
    :type op_type: OperationType
    :ivar rec_count: The number of records affected by the operation.
    :type rec_count: int
    :ivar affected_keys: The list of record keys affected by the operation.
    :type affected_keys: List[Any]
    :ivar raw_result: The raw result of the operation. It depends on the data source and the operation type.
    :type raw_result: Optional[Any]
    """

    def __init__(
        self,
        op_type: OperationType,
        rec_count: int = 0,
        affected_keys: Optional[List[Any]] = None,
        raw_result: Optional[Any] = None,
    ):
        """
        Initializes the instance. Used for creating an object encapsulating the result details of a specific operation.

        :param op_type: The specific operation type being performed.
        :param rec_count: The count of records affected by the operation.
        :param affected_keys: The list of record keys affected by the operation.
            Use an empty list if no record was affected.
            Use None if not supported by the implementation.
            Default: None.
        :param raw_result: The raw result data or object returned from the operation.
        """
        self.op_type = op_type
        self.rec_count = rec_count
        self.affected_keys = affected_keys
        self.raw_result = raw_result


class InsertResult(OperationResult):
    """
    Represents the result of an insert operation.
    """

    def __init__(
        self,
        rec_count: int,
        affected_keys: Optional[List[Any]],
        raw_result: Optional[Any] = None,
    ):
        """
        Initializes an instance of the class with details regarding an insert operation.
        :param rec_count: The number of records affected by the operation.
        :param affected_keys: The list of keys associated with the inserted records.
            Use an empty list if no new record was inserted.
            Use None if not supported by the implementation.
            Default: None.
        :param raw_result: Raw data or result object associated with the operation.
        """
        super().__init__(OperationType.INSERT, rec_count, affected_keys, raw_result)

    @property
    def inserted_count(self) -> int:
        """
        Provides access to the number of records inserted into the database or a relevant storage.

        :return: The count of records inserted so far.
        """
        return self.rec_count

    @property
    def inserted_keys(self) -> List[Any]:
        """
        Provides access to the list of keys that have been affected.

        :return: The list of affected keys.
        :raises UnsupportedFeatureError: If the feature is not supported.
        """
        if self.affected_keys is not None:
            return self.affected_keys
        raise UnsupportedFeatureError(
            "{self.__class__.__name__} does not handle inserted keys.}"
        )


class DeleteResult(OperationResult):
    """
    Represents the outcome of a delete operation.
    """

    def __init__(
        self,
        rec_count: int,
        affected_keys: Optional[List[Any]] = None,
        raw_result: Optional[Any] = None,
    ):
        """
        Initializes an instance of the class with details regarding a delete operation.

        :param rec_count: The number of records affected by the operation.
        :param affected_keys: The list of keys associated with the deleted records.
            Use an empty list if no new record was deleted.
            Use None if not supported by the implementation.
            Default: None.
        :param raw_result: The raw data resulting from the operation execution for further processing or storage.
            Defaults to None.
        """
        super().__init__(OperationType.DELETE, rec_count, affected_keys, raw_result)

    @property
    def deleted_count(self) -> int:
        """
        This property provides access to the count of records that have been marked or
        processed as deleted. It is expected to return the current count of such records,
        which is represented internally by a tracked attribute.

        :return: The number of records that have been marked as deleted.
        """
        return self.rec_count

    @property
    def deleted_keys(self) -> List[Any]:
        """
        Retrieves the list of deleted keys if available.

        :return: The list of affected (deleted) keys.
        :raises UnsupportedFeatureError: If the object does not support handling deleted keys.
        """
        if self.affected_keys is not None:
            return self.affected_keys
        raise UnsupportedFeatureError(
            "{self.__class__.__name__} does not handle deleted keys."
        )


class UpdateResult(OperationResult):
    """
    Represents the result of an update operation.

    :ivar did_upsert: Indicates whether the operation resulted in an upsert (insert if not found).
    :type did_upsert: bool
    """

    def __init__(
        self,
        rec_count: int,
        affected_keys: Optional[List[Any]] = None,
        raw_result: Optional[Any] = None,
        did_upsert: bool = False,
    ):
        """
        Initializes an instance of the class with details regarding an update operation.

        :param rec_count: The number of records affected by the update operation.
        :param affected_keys: The list of keys associated with the affected records.
            Use an empty list if no new record was updated.
            Use None if not supported by the implementation.
            Default: None.
        :param raw_result: The raw result returned from the database operation.
        :param did_upsert: Indicates if the operation resulted in an upsert to the database. Defaults to False.
        """
        super().__init__(OperationType.UPDATE, rec_count, affected_keys, raw_result)
        self.did_upsert = did_upsert

    @property
    def updated_count(self) -> int:
        """
        Provides the number of records that have been updated.

        This count does not distinguish between records that have been updated and those that have been inserted in the event of an upsert.

        :return: The count of updated records.
        """
        return self.rec_count

    @property
    def updated_keys(self) -> List[Any]:
        """
        Retrieves the list of deleted keys if available.

        This list contains both the keys of modified records and those of inserted records, in the event of an upsert.

        :return: The list of affected (updated or inserted) keys.
        :raises UnsupportedFeatureError: If the object does not support handling updated keys.
        """
        if self.affected_keys is not None:
            return self.affected_keys
        raise UnsupportedFeatureError(
            "{self.__class__.__name__} does not handle updated keys."
        )


class ReplaceResult(OperationResult):
    """
    Represents the result of a replace operation.

    This class extends OperationResult and is specifically designed to handle
    the results of a document replace operation. It includes functionality to
    track whether records were upserted as part of the replacement action.

    :ivar did_upsert: Indicates if an upsert operation occurred during the replacement process.
    :type did_upsert: bool
    """

    def __init__(
        self,
        rec_count: int,
        affected_keys: Optional[List[Any]] = None,
        raw_result: Optional[Any] = None,
        did_upsert: bool = False,
    ):
        """
        Initializes an instance of the class with details regarding a replace operation.

        :param rec_count: The number of records affected by the replace operation.
        :param affected_keys: The list of keys associated with the affected records.
            Use an empty list if no new record was updated.
            Use None if not supported by the implementation.
            Default: None.
        :param raw_result: Raw result object containing the replace operation's detailed outcome.
        :param did_upsert: Indicates whether the replace operation resulted in an
            upsert (insert if no record exists). Default is False.
        """
        super().__init__(OperationType.REPLACE, rec_count, affected_keys, raw_result)
        self.did_upsert = did_upsert

    @property
    def replaced_count(self) -> int:
        """
        Provides access to the count of records that have been replaced.

        This count does not distinguish between records that have been modified and those that have been inserted in the event of an upsert.

        :return: The count of records replaced.
        """
        return self.rec_count

    @property
    def replaced_keys(self) -> List[Any]:
        """
        Retrieves the list of replaced record keys if available.

        This list contains both the keys of modified records and those of inserted records, in the event of an upsert.

        :return: The list of affected (updated or inserted) keys.
        :raises UnsupportedFeatureError: If the object does not support handling updated keys.
        """
        if self.affected_keys is not None:
            return self.affected_keys
        raise UnsupportedFeatureError(
            "{self.__class__.__name__} does not handle replaced keys."
        )
