__all__ = ['Query']

from typing import Any, Dict, Optional

from botocore.exceptions import ClientError

import nuql
from nuql import types, api, resources


class Query(api.Boto3Adapter):
    def prepare_client_args(
            self,
            key_condition: Dict[str, Any] | None = None,
            condition: str | Dict[str, Any] | None = None,
            index_name: str = 'primary',
            limit: int | None = None,
            scan_index_forward: bool = True,
            exclusive_start_key: Dict[str, Any] | None = None,
            consistent_read: bool = False,
    ) -> Dict[str, Any]:
        """
        Prepares args for performing a query against the table (client API).

        :param key_condition: Key condition expression as a dict.
        :param condition: Filter condition expression as a dict.
        :param index_name: Index to perform query against.
        :param limit: Number of items to retrieve.
        :param scan_index_forward: Direction of scan.
        :param exclusive_start_key: Exclusive start key.
        :param consistent_read: Perform query as a consistent read.
        :return: Query result.
        """
        # Key condition is parsed from a dict and validated
        key_condition = api.KeyCondition(self.table, key_condition, index_name)

        # Filter condition is parsed from a string and validated
        resources.validate_condition_dict(condition)
        filter_condition = api.Condition(
            table=self.table,
            condition=condition,
            condition_type='FilterExpression'
        )

        return {
            **key_condition.client_args,
            **filter_condition.client_args,
            'ScanIndexForward': scan_index_forward,
            'ConsistentRead': consistent_read,
        }

    def prepare_args(
            self,
            key_condition: Dict[str, Any] | None = None,
            condition: str | Dict[str, Any] | None = None,
            index_name: str = 'primary',
            limit: int | None = None,
            scan_index_forward: bool = True,
            exclusive_start_key: Dict[str, Any] | None = None,
            consistent_read: bool = False,
    ) -> Dict[str, Any]:
        """
        Prepares args for performing a query against the table (resource API).

        :param key_condition: Key condition expression as a dict.
        :param condition: Filter condition expression as a dict.
        :param index_name: Index to perform query against.
        :param limit: Number of items to retrieve.
        :param scan_index_forward: Direction of scan.
        :param exclusive_start_key: Exclusive start key.
        :param consistent_read: Perform query as a consistent read.
        :return: Query result.
        """
        # Key condition is parsed from a dict and validated
        key_condition = api.KeyCondition(self.table, key_condition, index_name)

        # Filter condition is parsed from a string and validated
        resources.validate_condition_dict(condition)
        filter_condition = api.Condition(
            table=self.table,
            condition=condition,
            condition_type='FilterExpression'
        )

        return {
            **key_condition.resource_args,
            **filter_condition.resource_args,
            'ScanIndexForward': scan_index_forward,
            'ConsistentRead': consistent_read,
        }

    def invoke_sync(
            self,
            key_condition: Dict[str, Any] | None = None,
            condition: str | Dict[str, Any] | None = None,
            index_name: str = 'primary',
            limit: int | None = None,
            scan_index_forward: bool = True,
            exclusive_start_key: Dict[str, Any] | None = None,
            consistent_read: bool = False,
    ) -> Dict[str, Any]:
        """
        Synchronously invokes a query against the table.

        :param key_condition: Key condition expression as a dict.
        :param condition: Filter condition expression as a dict.
        :param index_name: Index to perform query against.
        :param limit: Number of items to retrieve.
        :param scan_index_forward: Direction of scan.
        :param exclusive_start_key: Exclusive start key.
        :param consistent_read: Perform query as a consistent read.
        :return: Query result.
        """
        args = self.prepare_args(
            key_condition=key_condition,
            condition=condition,
            index_name=index_name,
            limit=limit,
            scan_index_forward=scan_index_forward,
            exclusive_start_key=exclusive_start_key,
            consistent_read=consistent_read,
        )

        data = []
        last_evaluated_key = exclusive_start_key
        fulfilled = False

        while not fulfilled:
            # Subtract processed records from limit
            if isinstance(limit, int):
                args['Limit'] = limit - len(data)

            # Break when limit is reached
            if 'Limit' in args and args['Limit'] == 0:
                break

            # Pagination is achieved by using LEK as exclusive start key
            if last_evaluated_key:
                args['ExclusiveStartKey'] = last_evaluated_key

            try:
                response = self.connection.table.query(**args)
            except ClientError as exc:
                raise nuql.Boto3Error(exc, args)

            data.extend(response.get('Items', []))
            last_evaluated_key = response.get('LastEvaluatedKey')

            if not last_evaluated_key:
                fulfilled = True

        # Deserialise the data
        data = [self.table.serialiser.deserialise(item) for item in data]

        output = {'items': [], 'last_evaluated_key': last_evaluated_key}

        # Follow functionality on local/global indexes - batch gets all retrieved items
        index = self.table.indexes.get_index(index_name) if index_name != 'primary' else self.table.indexes.primary

        if 'follow' in index and index['follow'] is True:
            batch_get = api.BatchGet(self.client, self.table)
            output.update(batch_get.invoke_sync(data))
        else:
            output['items'] = data

        return output
