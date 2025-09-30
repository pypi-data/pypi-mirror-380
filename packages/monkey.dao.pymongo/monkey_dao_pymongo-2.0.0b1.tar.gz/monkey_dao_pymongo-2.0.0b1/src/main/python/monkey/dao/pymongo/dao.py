# -*- coding: utf-8 -*-
"""
Provides implementation of the [Data Access Object (DAO)](https://en.wikipedia.org/wiki/Data_access_object) design model based on [MongoDB PyMongo](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/) as specified by [monkey.dao](https://dao.monkey-python.org) project.

This module contains the [`PyMongoDAO`](#monkey.dao.pymongo.dao.PyMongoDAO) class, designed to abstract database
operations such as querying, inserting, updating, and deleting documents
from a MongoDB collection. It also supports sequence number handling
on a per-document basis if enabled.

The module supports flexible collection configuration with options
such as codec options, read/write concerns, and read preferences.

It also introduces a sequence number management mechanism for the documents in the collection managed with an instance of [`PyMongoDAO`](#monkey.dao.pymongo.dao.PyMongoDAO).
The sequence numbers of each collection are stored in a special collection called 'sequences', by
default. It is possible to define another name for this collection, using the [`seq_collection_name`](#monkey.dao.pymongo.dao.PyMongoDAO) parameter at DAO instantiation.

"""

from logging import Logger, getLogger

from typing import Any, Union, Iterable, Optional, List, Dict

from bson.objectid import ObjectId
from bson.codec_options import CodecOptions
from pymongo.collection import Collection, ReturnDocument
from pymongo.database import Database
from pymongo.errors import PyMongoError
from pymongo.read_concern import ReadConcern
from pymongo.write_concern import WriteConcern
import pymongo.results

from monkey.dao.dao import DAO
from monkey.dao.errors import PersistenceError, ObjectNotFoundError
from monkey.dao.pymongo.results import (
    DeleteResult,
    InsertResult,
    UpdateResult,
    ReplaceResult,
)

_SEQ_COLLECTION_NAME: str = "sequences"
"""The name used for sequences collection, by default."""

_SEQ_VALUE_FIELD: str = "seq"
"""The name used for sequence value field in sequence collection, by default."""

_SEQ_NUM_FIELD: str = "_seq_num"
"""The name used for sequence number field, by default."""

_ID_FIELD: str = "_id"
"""The name used for the builtin id field."""


class PyMongoDAO(DAO):
    """
    Provides an implementation of a Data Access Object (DAO) for MongoDB using PyMongo.

    This class encapsulates operations for querying, inserting, updating, deleting,
    and counting documents within a specific MongoDB collection. It also provides
    support for sequence numbers on documents if enabled.

    The PyMongoDAO class is designed for ease of use and to abstract database
    persistence logic, allowing the rest of the application to interact with data
    without knowledge of MongoDB operations. Custom configurations such as sequence
    number handling and collection configuration are supported.
    """

    def __init__(
        self,
        database: Database,
        collection_name: str,
        seq_enabled: bool = False,
        seq_num_field: str = _SEQ_NUM_FIELD,
        seq_collection_name: str = _SEQ_COLLECTION_NAME,
        codec_options: Optional[CodecOptions] = None,
        read_preference=None,
        write_concern: Optional[WriteConcern] = None,
        read_concern: Optional[ReadConcern] = None,
        indexes: Optional[List[Dict[str, Any]]] = None,
    ):
        """
        Instantiates a new PyMongo DAO.

        :param database: A MongoDB database provided by pymongo.MongoClient.
        :param collection_name: The name of the collection in which documents persist.
        :param seq_enabled: If True, DAO will add a sequence number to all newly inserted documents.
        :param seq_num_field: The name of the document field is used for the sequence number.
        :param seq_collection_name: The name of the collection in which the last sequence number is stored.
        :param codec_options: An instance of :class: bson.codec_options.CodecOptions to configure the codec options for the collection. See :method: pymongo.database.Database.get_collection for more details.
        :param read_preference: The read preference to use. See :method: pymongo.database.Database.get_collection for more details.
        :param write_concern: The write concern to use. See :method: pymongo.database.Database.get_collection for more details.
        :param read_concern: The read concern to use. See :method: pymongo.database.Database.get_collection for more details.
        :param indexes: A list of indexes to use for this collection.
        """
        super().__init__()
        self.logger: Logger = getLogger(
            f"{self.__class__.__module__}.{self.__class__.__name__}.{collection_name}"
        )
        self.database: Database = database
        self.collection: Collection = database.get_collection(
            collection_name, codec_options, read_preference, write_concern, read_concern
        )
        self.seq_enabled: bool = seq_enabled
        if seq_enabled:
            self.seq_num_field: str = seq_num_field
            self.sequences: Collection = database.get_collection(seq_collection_name)
            self.sequence_name: str = collection_name

        if indexes:
            self._ensure_indexes(indexes)

    def _ensure_indexes(self, indexes: List[Dict[str, Any]]) -> None:
        """
        Ensures that the specified indexes exist on the collection. If an index does not already exist,
        it will be created. The method compares index definitions provided in the input with the
        existing indexes of the collection to determine if creation is necessary.

        :param indexes: A list of index definitions where each definition includes `key` for the index fields and
            `options` for additional index options.
        """
        for index_def in indexes:
            key = index_def["key"]
            options = index_def.get("options", {})
            index_name = options.get("name", "_".join([f"{k[0]}_{k[1]}" for k in key]))

            if index_name not in self.collection.index_information():
                self.logger.info(
                    f"Index {index_name} not found. Creating index {index_name}"
                )
                self.collection.create_index(key, **options)
            else:
                self.logger.info(f"Index {index_name} found. Index already exists")

    def find(
        self,
        query: Any = None,
        skip: int = 0,
        limit: int = 0,
        sort: Optional[Union[list[str], dict[str, int]]] = None,
        projection=None,
        **kwargs,
    ):
        """
        Finds documents matching the specified query.

        :param query: The filter used to query the data collection. If the query is None, all documents are returned.
        :param skip: The number of documents to omit (from the start of the result set) when returning the results.
        :param limit: The maximum number of documents to return.
        :param sort: A list of (field key, direction) pairs specifying the sort order for this list. For sort direction, use 1 for ascending and -1 for descending.
        :param projection: A list of field names that should be returned in the resultset or a dict specifying the
        fields to include or exclude.
        :param kwargs: Implementation specific arguments. See :method: pymongo.collection.Collection.find for more details.
        :return: The list of query matching documents. Itv returns an empty list if no document is found.
        """
        cursor = None
        try:
            cursor = self.collection.find(
                filter=query,
                projection=projection,
                skip=skip,
                limit=limit,
                sort=sort,
                **kwargs,
            )
            # TODO: Use list comprehension or lambda expression
            result = []
            for doc in cursor:
                result.append(doc)
            return result
        except PyMongoError as e:
            self.logger.error(f"Database error: {e}")
            raise PersistenceError("Unexpected error", e)
        finally:
            cursor.close()

    def find_one(self, query: Any = None, projection=None, **kwargs):
        """
        Finds a single document in the collection that matches the given query.

        If no matching document is found, the method may raise an ObjectNotFound error.

        :param query: The filter used to query the data collection. If the query is None, the first found document is returned.
        :param projection: A list of field names that should be returned in the resultset or a dict specifying the
        fields to include or exclude.
        :param kwargs: Implementation specific arguments. See :method: pymongo.collection.Collection.find_one for more details.
        :return: The document matching the query.
        :raises ObjectNotFoundError: If no document matches the given query.
        """
        try:
            doc = self.collection.find_one(query, projection=projection, **kwargs)
            if doc is not None:
                return doc
            else:
                raise ObjectNotFoundError(self.collection.name, query)
        except ObjectNotFoundError as e:
            self.logger.warning(
                f"No documents found in {self.collection.name} for query: {query}"
            )
            raise e
        except PyMongoError as e:
            self.logger.error(f"Database error: {e}")
            raise PersistenceError("Unexpected error", e)

    def find_one_by_id(
        self, oid: Union[ObjectId, str, bytes], projection=None, **kwargs
    ):
        """
        Finds a document by its identifier (i.e. by filtering on the '_id' field of the document).

        If no matching document is found, the method may raise an ObjectNotFound error.

        :param oid: The id of the document.
        :param projection: A list of field names that should be returned in the resultset or a dict specifying the
        fields to include or exclude.
        :param kwargs: Implementation specific arguments. See :method: pymongo.collection.Collection.find_one for more details.
        :return: The found document (if there is one).
        :raises ObjectNotFoundError: If no documents match the specified key.
        """
        query = {_ID_FIELD: ObjectId(oid)} if isinstance(oid, str) else {_ID_FIELD: oid}
        return self.find_one(query, projection, **kwargs)

    def find_one_by_key(
        self, key: Union[ObjectId, str, bytes], projection=None, **kwargs
    ):
        """
        Finds a document by its key (synonym of find_one_by_id).

        If no matching document is found, the method may raise an ObjectNotFound error.

        :param key: The key of the document.
        :param projection: A list of field names that should be returned in the resultset or a dict specifying the
        fields to include or exclude.
        :param kwargs: Implementation specific arguments. See :method: pymongo.collection.Collection.find_one for more details.
        :return: The found document (if there is one).
        :raises ObjectNotFoundError: If no documents match the specified key.
        """
        return self.find_one_by_id(key, projection, **kwargs)

    def find_one_by_seq_num(self, seq_num: int, projection=None, **kwargs):
        """
        Finds a document by its sequence number.

        If no matching document is found, the method may raise an ObjectNotFound error.

        :param seq_num: The sequence number of the document.
        :param projection: A list of field names that should be returned in the resultset or a dict specifying the
        fields to include or exclude.
        :param kwargs: Implementation specific arguments. See :method: pymongo.collection.Collection.find_one for more details.
        :return: The found document (if there is one).
        :raises ObjectNotFoundError: If no documents match the specified key.
        """
        if self.seq_enabled:
            return self.find_one({self.seq_num_field: seq_num}, projection, **kwargs)
        else:
            message = f"Sequence number is not enabled for {self.__class__} on '{self.collection.name}' collection"
            self.logger.error(message)
            raise NotImplementedError(message)

    def count(self, query: Any = None, **kwargs) -> int:
        """
        Counts the number of documents matching the query.

        :param query: The filter used to query the collection.
        :param kwargs: Implementation specific arguments. See :method: pymongo.collection.Collection.count_documents for more details.
        :return: The total number of documents.
        """
        if not query:
            query = {}
        try:
            return self.collection.count_documents(query, **kwargs)
        except PyMongoError as e:
            self.logger.error(f"Database error: {e}")
            raise PersistenceError("Unexpected error", e)

    def count_all(self, fast_count: bool = False, **kwargs) -> int:
        """
        Counts the number of all documents.

        :param fast_count: If True, uses the estimated document count provided by MongoDB.
        :param kwargs: Implementation specific arguments. See :method: pymongo.collection.Collection.estimated_document_count and :method: pymongo.collection.Collection.count_documents for more details.
        :return: The total number of documents.
        """
        if fast_count:
            return self.collection.estimated_document_count(**kwargs)
        else:
            return self.count({}, **kwargs)

    def delete(self, query: Any = None, **kwargs) -> DeleteResult:
        """
        Deletes the document identified by the given key.

        If no matching document is found, the method returns 0. Otherwise, it returns the number of deleted documents.

        :param query: The query filter used to query the documents to delete from the collection.
        :param kwargs: Implementation specific arguments. See :method: pymongo.collection.Collection.delete_many for more details.
        :return: An instance of DeleteResult.
        :raises PersistenceError: If the operation generates an error.
        """
        try:
            native_result: pymongo.results.DeleteResult = self.collection.delete_many(
                query, **kwargs
            )
            return DeleteResult(native_result)
        except PyMongoError as e:
            self.logger.error(f"Database error: {e}")
            raise PersistenceError("Unexpected error", e)

    def delete_one(
        self,
        query: Any = None,
        sort: Optional[Union[list[str], dict[str, int]]] = None,
        **kwargs,
    ) -> DeleteResult:
        """
        Deletes the first document matching the query.

        :param query: The query filter to select the document to be deleted from the data collection.
        :param kwargs: Implementation specific arguments. See :method: pymongo.collection.Collection.delete_one for more details.
        :param sort: A list of (key, direction) pairs specifying the sort order for this list. For sort direction, use 1 for ascending and -1 for descending.
        :return: An instance of DeleteResult.
        :raises PersistenceError: If the operation generates an error.
        """
        try:
            native_result: DeleteResult = self.collection.delete_one(query, **kwargs)
            return DeleteResult(native_result)
        except PyMongoError as e:
            self.logger.error(f"Database error: {e}")
            raise PersistenceError("Unexpected error", e)

    def delete_one_by_id(
        self, oid: Union[ObjectId, str, bytes], **kwargs
    ) -> DeleteResult:
        """
        Deletes the document matching the specified identifier.
        :param oid: The id of the document.
        :param kwargs: Implementation specific arguments. See :method: pymongo.collection.Collection.delete_one for more details.
        :return: An instance of DeleteResult.
        :raises PersistenceError: If the operation generates an error.
        """
        query = {_ID_FIELD: ObjectId(oid)} if isinstance(oid, str) else {_ID_FIELD: oid}
        return self.delete_one(query, **kwargs)

    def delete_one_by_key(
        self, key: Union[ObjectId, str, bytes], **kwargs
    ) -> DeleteResult:
        """
        Deletes the document identified by the given key (synonym of delete_one_by_id).

        :param key: The key of the document is to delete.
        :param kwargs: Implementation specific arguments. See :method: pymongo.collection.Collection.delete_one for more details.
        :return: An instance of DeleteResult.
        :raises PersistenceError: If the operation generates an error.
        """
        return self.delete_one_by_id(key, **kwargs)

    def insert(self, data: Iterable[dict], **kwargs) -> InsertResult:
        """
        Inserts many new documents into the data collection.

        :param data: The list of data to insert as new documents.
        :param kwargs: Implementation specific arguments. See :method: pymongo.collection.Collection.insert_many for more details.
        :return: An instance of InsertResult.
        :raises PersistenceError: If the operation generates an error.
        """
        docs = []
        count: int = sum(1 for _ in data)
        if self.seq_enabled:
            next_seq_num = self._reserve_seq_num(count)
            for d in data:
                doc = {self.seq_num_field: next_seq_num}
                doc.update(d)
                docs.append(doc)
                next_seq_num += 1
        else:
            docs = data
        try:
            native_result: pymongo.results.InsertManyResult = (
                self.collection.insert_many(docs)
            )
            return InsertResult(native_result)
        except PyMongoError as e:
            self.logger.error(f"Database error: {e}")
            raise PersistenceError("Unexpected error", e)

    def insert_one(self, data: dict, **kwargs) -> InsertResult:
        """
        Inserts a new document into the data collection.

        :param data: The data to insert.
        :param kwargs: Implementation specific arguments. See :method: pymongo.collection.Collection.insert_one for more details.
        :return: An instance of InsertResult.
        :raises PersistenceError: If the operation generates an error.
        """
        return self.insert([data], **kwargs)

    def update(
        self, query: Any, change_set: dict, upsert: bool = False, **kwargs
    ) -> UpdateResult:
        """
        Updates many documents in the database matching the provided query. The
        method will apply the given modifications defined in the data parameter.

        :param query: The query filter used to filter documents to update. Must define the matching criteria to find desired documents.
        :param change_set: The modifications to apply to the matched documents. Can include new values or transformations.
        :param upsert: Determines whether to insert a new document if no matching document exists.
            Defaults to False.
        :param kwargs: Implementation specific arguments. See [`pymongo.collection.Collection.update_many`](https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html#pymongo.collection.Collection.update_many) for more details.
        :return: Returns an instance of UpdateResult.
        :raises PersistenceError: If the operation generates an error.
        """
        try:
            native_result: pymongo.results.UpdateResult = self.collection.update_many(
                query, {"$set": change_set}, upsert=upsert, **kwargs
            )
            return UpdateResult(native_result)
        except PyMongoError as e:
            self.logger.error(f"Database error: {e}")
            raise PersistenceError("Unexpected error", e)

    def update_one(
        self,
        query: Any,
        change_set: dict,
        upsert: bool = False,
        sort: Optional[Union[list[str], dict[str, int]]] = None,
        **kwargs,
    ) -> UpdateResult:
        """
        Updates the first document found matching the query using provided data.

        :param query: The query filter used to filter documents to update. Must define the matching criteria to find desired documents.
        :param change_set: The data to update.
        :param upsert: If True, the document will be inserted if it does not exist.
        :param sort: A list of (field key, direction) pairs specifying the sort order for this list. For sort direction, use 1 for ascending and -1 for descending.
        :param kwargs: Implementation specific arguments. See :method: pymongo.collection.Collection.update_one for more details.
        :return: The updated document.
        :raises PersistenceError: If the operation generates an error.
        """
        try:
            # TODO: Check why introduction of `sort` parameter doesn't work (`TypeError`).
            # TODO: To be tested with a real database and not only with [mongomock](https://github.com/mongomock)
            # SEE: Changed in version 4.11 [pymongo.collection.Collection.update_one](https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html#pymongo.collection.Collection.update_one)
            # native_result: pymongo.results.UpdateResult = self.collection.update_one(query, {'$set': change_set},
            #                                                                         upsert=upsert, sort=sort, **kwargs)
            # WORKAROUND
            native_result: pymongo.results.UpdateResult = self.collection.update_one(
                query, {"$set": change_set}, upsert=upsert, **kwargs
            )
            return UpdateResult(native_result)
        except PyMongoError as e:
            self.logger.error(f"Database error: {e}")
            raise PersistenceError("Unexpected error", e)

    def update_one_by_id(
        self,
        oid: Union[ObjectId, str, bytes],
        change_set: dict,
        upsert: bool = False,
        **kwargs,
    ) -> UpdateResult:
        """
        Updates the document associated with the given key using provided data.

        :param oid: The id of the document to update.
        :param change_set: The data to update.
        :param upsert: If True, the document will be inserted if it does not exist.
        :param kwargs: Implementation specific arguments. See :method: pymongo.collection.Collection.update_one for more details.
        :return: The updated document.
        :raises PersistenceError: If the operation generates an error.
        """
        query = {_ID_FIELD: ObjectId(oid)} if isinstance(oid, str) else {_ID_FIELD: oid}
        return self.update_one(query, change_set, upsert, **kwargs)

    def update_one_by_key(
        self,
        key: Union[ObjectId, str, bytes],
        change_set: dict,
        upsert: bool = False,
        **kwargs,
    ) -> UpdateResult:
        """
        Updates the document associated with the given key using provided data (synonym of delete_one_by_id).

        :param key: The key of the document is to update.
        :param change_set: The data to update.
        :param upsert: If True, the document will be inserted if it does not exist.
        :param kwargs: Implementation specific arguments. See :method: pymongo.collection.Collection.update_one for more details.
        :return: An instance of UpdateResult.
        """
        return self.update_one_by_id(key, change_set, upsert, **kwargs)

    def replace(self, query: Any, data: dict, upsert: bool = False, **kwargs):
        """
        Replaces the documents matching the query with the provided data.

        Identifier and sequence number of the records have to be preserved during the replacement.

        :param query: The query filter used to locate the document that will be replaced. This
            determines the condition for document matching.
        :param data: The new data that will replace the matched document. This should be in an
            acceptable format for the database.
        :param upsert: If True, the document will be inserted if it does not exist.
            Defaults to False.
        :param kwargs: Implementation specific arguments. See :method: pymongo.collection.Collection.find and :method: pymongo.collection.Collection.replace_one for more details.
        :return: An instance of ReplaceResult.
        :raises PersistenceError: If the operation generates an error.
        """
        try:
            matching_doc_ids = self.lookup(query, **kwargs)
            replace_count = 0
            upsert_count = 0
            native_result = []
            for doc_id in matching_doc_ids:
                result: ReplaceResult = self.replace_one_by_id(
                    doc_id, data, upsert, **kwargs
                )
                upsert_count = upsert_count + 1 if result.did_upsert else upsert_count
                native_result.append(result.native_result)
                replace_count += result.replaced_count
            return ReplaceResult(replace_count, native_result, upsert_count > 0)
        except PyMongoError as e:
            self.logger.error(f"Database error: {e}")
            raise PersistenceError("Unexpected error", e)

    def replace_one(
        self, query: Any, data: dict, upsert: bool = False, **kwargs
    ) -> ReplaceResult:
        """
        Replaces the first document matching the query with the provided data.

        Identifier and sequence number of the records have to be preserved during the replacement.

        :param query: The query filter used to locate the document that will be replaced. This determines the condition for document matching.
        :param data: The new data that will replace the matched document. This should be in an acceptable format for the database.
        :param upsert: If True, the document will be inserted if it does not exist.
            Defaults to False.
        :param kwargs: Implementation specific arguments. See :method: pymongo.collection.Collection.find for more details.
        :return: An instance of ReplaceResult.
        :raises PersistenceError: If the operation generates an error.
        """
        document = {}
        document.update(data)
        try:
            query_filter = query
            if self.seq_enabled:
                seq_num = self.find_one(query, {self.seq_num_field: 1, "_id": 0})
                document[self.seq_num_field] = seq_num[self.seq_num_field]
                query_filter = {self.seq_num_field: seq_num[self.seq_num_field]}
            native_result: pymongo.results.UpdateResult = self.collection.replace_one(
                query_filter, document, upsert, **kwargs
            )
            return ReplaceResult(
                native_result.modified_count,
                native_result,
                int(native_result.did_upsert),
            )
        except PyMongoError as e:
            self.logger.error(f"Database error: {e}")
            raise PersistenceError("Unexpected error", e)

    def replace_one_by_id(
        self,
        oid: Union[ObjectId, str, bytes],
        data: Any,
        upsert: bool = False,
        **kwargs,
    ) -> ReplaceResult:
        """
        Replaces the record associated with the given key using provided data.

        The identifier has to be preserved during the replacement.

        :param oid: The id of the record to replace.
        :param data: The data to replace.
        :param upsert: If True, the record will be inserted if it does not exist.
        :param kwargs: Implementation specific arguments. See :method: pymongo.collection.Collection.replace_one for more details.
        :return: An instance of ReplaceResult.
        """
        query = {_ID_FIELD: ObjectId(oid)} if isinstance(oid, str) else {_ID_FIELD: oid}
        return self.replace_one(query, data, upsert, **kwargs)

    def replace_one_by_key(
        self,
        key: Union[ObjectId, str, bytes],
        data: Any,
        upsert: bool = False,
        **kwargs,
    ) -> ReplaceResult:
        """
        Replaces the record associated with the given key using provided data.

        The identifier has to be preserved during the replacement.

        :param key: The key of the record to replace.
        :param data: The data to replace.
        :param upsert: If True, the record will be inserted if it does not exist.
        :param kwargs: Implementation specific arguments. See :method: pymongo.collection.Collection.replace_one for more details.
        :return: An instance of ReplaceResult.
        """
        return self.replace_one_by_id(key, data, upsert, **kwargs)

    def lookup(
        self,
        query: Any = None,
        skip: int = 0,
        limit: int = 0,
        sort: Optional[Union[list[str], dict[str, int]]] = None,
        **kwargs,
    ) -> list[str]:
        """
        Retrieves ids of documents matching the specified query

        :param query: The filter used to query the data collection. If the query is None, all documents are returned.
        :param skip: The number of documents to omit (from the start of the result set) when returning the results.
        :param limit: The maximum number of documents to return.
        :param sort: A list of (field key, direction) pairs specifying the sort order for this list. For sort direction, use 1 for ascending and -1 for descending.
        :kwargs: Implementation specific arguments. See :method: pymongo.collection.Collection.find for more details.
        :return: List of matching document ids
        :raises PersistenceError: if an unexpected error occurs during the operation
        """
        docs = self.find(
            query, skip=skip, limit=limit, sort=sort, projection=[_ID_FIELD], **kwargs
        )
        result = [str(doc[_ID_FIELD]) for doc in docs]
        return result

    def lookup_one(
        self, query=None, sort: Union[None, list[str], dict[str, int]] = None, **kwargs
    ) -> Optional[str]:
        """
        Retrieves the id of the first document found matching the specified query
        :param query: The filter used to query the data collection. If the query is None, all documents are returned.
        :param sort: A list of (field key, direction) pairs specifying the sort order for this list. For sort direction, use 1 for ascending and -1 for descending.
        :kwargs: Implementation specific arguments. See :method: pymongo.collection.Collection.find_one for more details.
        :return: The id of the first document found matching the query
        :raises ObjectNotFoundError: if no document is found
        :raises PersistenceError: if an unexpected error occurs during the operation
        """
        try:
            doc = self.find_one(query, sort=sort, projection=[_ID_FIELD], **kwargs)
            if doc is not None:
                return str(doc[_ID_FIELD])
            else:
                raise ObjectNotFoundError(self.collection.name, query)
        except ObjectNotFoundError as e:
            self.logger.warning(
                f"No documents found in {self.collection.name} for query: {query}"
            )
            raise e
        except PyMongoError as e:
            self.logger.error(f"Database error: {e}")
            raise PersistenceError("Unexpected error", e)

    def _reserve_seq_num(self, count: int = 1) -> int:
        """
        Reserves the specified number of sequence numbers and returns the first sequence number reserved.

        :param count: The number of sequence numbers to reserve.
            Defaults to 1.
        :return: The first reserved sequence number (i.e., the next sequence number to use).
        """
        result = self.sequences.find_one_and_update(
            {_ID_FIELD: self.sequence_name},
            {"$inc": {_SEQ_VALUE_FIELD: count}},
            projection={_SEQ_VALUE_FIELD: True, _ID_FIELD: False},
            upsert=True,
            return_document=ReturnDocument.AFTER,
        )
        return result[_SEQ_VALUE_FIELD] - count + 1

    def _get_last_reserved_seq_num(self) -> int:
        """
        Retrieves the last reserved sequence number from a database.

        This method queries the *sequences* collection in the database to fetch the last
        reserved sequence number for the given sequence name. If no record is found,
        it defaults to returning 0.

        :return: The last reserved sequence number.
        """
        result = self.sequences.find_one(
            {_ID_FIELD: self.sequence_name}, projection={_SEQ_VALUE_FIELD: True}
        )
        return result[_SEQ_VALUE_FIELD] if result is not None else 0
