# -*- coding: utf-8 -*-
"""
Provides result classes that wrap native PyMongo result objects with additional
functionality. These classes include `InsertResult`, `DeleteResult`, `ReplaceResult`, and
`UpdateResult`, each of which corresponds to specific database operations and offers enhanced
access to operation details.

The module ensures compatibility with the `monkey.dao.results` result specifications and adapts
native pymongo result classes for extended use cases and ease of integration. It includes
optional support for bulk operations.
"""

from typing import Any, List, Union

from monkey.dao import results as result_spec
from pymongo import results as pymongo_results


class InsertResult(result_spec.InsertResult):
    """
    Represents the result of an insert operation in the database.

    This class encapsulates the details of the insertion operation, offering properties
    to access information such as the inserted IDs and acknowledgment status. It is designed
    to handle results from both single and bulk insert operations, abstracting specific
    details of the underlying database driver.

    :ivar acknowledged: Indicates whether the database acknowledged the operation.
    :type acknowledged: bool
    """

    def __init__(
        self,
        native_result: Union[
            pymongo_results.InsertManyResult, pymongo_results.InsertOneResult
        ],
    ):
        """
        Represents the outcome of a database insertion operation.

        This class acts as a wrapper around pymongo insertion result objects,
        such as InsertManyResult or InsertOneResult, providing additional
        abstraction and accessibility. It tracks the number of inserted
        documents, their respective IDs, and the acknowledgment status of the
        operation.

        :param native_result: PyMongo insertion result object
        """
        super().__init__(
            (
                len(native_result.inserted_ids)
                if isinstance(native_result, pymongo_results.InsertManyResult)
                else 1
            ),
            (
                native_result.inserted_ids
                if isinstance(native_result, pymongo_results.InsertManyResult)
                else [native_result.inserted_id]
            ),
        )
        self._native_result = native_result
        self.acknowledged = native_result.acknowledged

    @property
    def inserted_ids(self) -> List[Any]:
        """
        Provides access to the list of inserted ids for the current context (synonym of inserted_keys).

        This property retrieves the list of ids that have been processed and successfully inserted.

        :return: The list of inserted ids.
        """
        return self.inserted_keys


class DeleteResult(result_spec.DeleteResult):
    """
    Represents the result of a delete operation.

    This class encapsulates the result data of a delete operation performed in the
    database. It extends the base `result_spec.DeleteResult` and provides additional
    properties or attributes specific to the internal implementation.

    :ivar acknowledged: Indicates whether the database acknowledged the operation.
    :type acknowledged: bool
    """

    def __init__(self, native_result: pymongo_results.DeleteResult):
        """
        Represents the result of a delete operation in a MongoDB database.

        This class extends the base result of write operations, incorporating
        attributes specific to deletion results. It encapsulates details
        provided by the DeleteResult object returned by pymongo, allowing easy
        access to the count of documents deleted and acknowledgment status.

        :param native_result: The DeleteResult object returned by pymongo.
        """
        super().__init__(
            native_result.deleted_count, raw_result=native_result.raw_result
        )
        self._native_result = native_result
        self.acknowledged = native_result.acknowledged

    @property
    def deleted_ids(self) -> List[Any]:
        """
        Returns a list of deleted identifiers (synonym of deleted_keys).

        The property provides a read-only access to a collection of IDs
        that have been marked or flagged as deleted. The returned IDs can be
        used for audit or recovery operations if needed.

        :return: The list of deleted identifiers.
        """
        return self.deleted_keys


class ReplaceResult(result_spec.ReplaceResult):
    """
    Represents the result of a replace operation in the database.

    This class encapsulates the results of a replace operation, including the count
    of replaced documents, the raw database results, and the count of any upserted
    documents. It provides an interface to access native database results and
    identifiers of replaced documents.

    :ivar acknowledged: Indicates whether the database acknowledged the operation.
    :type acknowledged: bool
    :ivar upsert_count: The number of upserted documents.
    :type upsert_count: int
    """

    def __init__(
        self,
        replaced_count: int,
        native_result: Union[
            pymongo_results.UpdateResult, List[pymongo_results.UpdateResult]
        ],
        upsert_count: int,
    ):
        """
        Initializes an instance of the class.

        This constructor sets up the initial state of the class, which includes
        records of the number of replaced documents, the native results of the
        update operation, and the number of upserted documents. It ensures that
        the state of acknowledgment and upsert count are managed based on the
        provided results.

        :param replaced_count: The number of replaced documents.
        :param native_result: The native result of the replace operation.
        :param upsert_count: The number of upserted documents.
        """
        super().__init__(
            replaced_count,
            raw_result=(
                native_result
                if isinstance(native_result, pymongo_results.UpdateResult)
                else [result.raw_result for result in list(native_result)]
            ),
            did_upsert=upsert_count > 0,
        )
        self._native_result = native_result
        self.acknowledged = all(result.acknowledged for result in list(native_result))
        self.upsert_count = upsert_count

    @property
    def native_result(
        self,
    ) -> Union[pymongo_results.UpdateResult, List[pymongo_results.UpdateResult]]:
        """
        Gets the native database result of the update operation.

        The method returns the native result of an update operation executed through the database connection. This result may
        contain detailed information about the update operation, such as matched and modified document counts. The type of
        result may vary depending on whether a single update or multiple updates were performed.

        :return: The native result of the update operation.
        """
        return self._native_result

    @property
    def replaced_ids(self) -> List[Any]:
        """
        Indicates the list of replaced keys as a property. (synonym of replaced_keys).

        :return: The list of replaced ids.
        """
        return self.replaced_keys


class UpdateResult(result_spec.UpdateResult):
    """
    Represents the result of an update operation in a database context.

    This class provides access to the details of an update operation result,
    including whether the update was acknowledged, the number of documents
    modified, and other related information. It encapsulates a native result
    object and provides additional properties for derived data and easier
    access to some of its attributes.

    :ivar acknowledged: Indicates whether the update was acknowledged.
    :type acknowledged: bool
    """

    def __init__(
        self,
        native_result: pymongo_results.UpdateResult,
    ):
        """
        Initializes an object to wrap the result of a MongoDB update operation.

        :param native_result: The native result of the update operation.
        """
        super().__init__(
            native_result.modified_count, raw_result=native_result.raw_result
        )
        self._native_result = native_result
        self.acknowledged = native_result.acknowledged

    @property
    def native_result(self) -> pymongo_results.UpdateResult:
        """
        Provides access to the native MongoDB update result object.

        :return: The native MongoDB update result object.
        """
        return self._native_result

    @property
    def updated_ids(self) -> List[Any]:
        """
        Gets the updated IDs obtained from the updated ids. (synonym of update_ids).

        This property retrieves the updated IDs which are derived
        from the underlying updated keys. The updated keys are used
        internally to map or reference updated identifier values.

        :return: The updated IDs.
        """
        return self.updated_keys
