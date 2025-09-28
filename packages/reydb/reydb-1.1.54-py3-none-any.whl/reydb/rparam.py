# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2022-12-05 14:10:02
@Author  : Rey
@Contact : reyxbo@163.com
@Explain : Database parameter methods.
"""


from typing import overload

from .rbase import DatabaseBase
from .rdb import Database


__all__ = (
    'DatabaseParameters',
    'DatabaseParametersStatus',
    'DatabaseParametersVariable',
    'DatabaseParametersPragma'
)


class DatabaseParameters(DatabaseBase):
    """
    Database parameters type.
    """


    def __init__(
        self,
        db: Database,
        global_: bool
    ) -> None:
        """
        Build instance attributes.

        Parameters
        ----------
        db: `Database` instance.
        global\\_ : Whether base global.
        """

        # Set parameter.
        self.db = db
        self.global_ = global_


    def __getitem__(self, key: str) -> str | None:
        """
        Get item of parameter dictionary.

        Parameters
        ----------
        key : Parameter key.

        Returns
        -------
        Parameter value.
        """

        # Get.
        value = self.get(key)

        return value


    def __setitem__(self, key: str, value: str | float) -> None:
        """
        Set item of parameter dictionary.

        Parameters
        ----------
        key : Parameter key.
        value : Parameter value.
        """

        # Set.
        params = {key: value}

        # Update.
        self.update(params)


class DatabaseParametersStatus(DatabaseParameters):
    """
    Database parameters status type.
    """


    @overload
    def get(self) -> dict[str, str]: ...

    @overload
    def get(self, key: str) -> str | None: ...

    def get(self, key: str | None = None) -> dict[str, str] | str | None:
        """
        Get parameter.

        Parameters
        ----------
        key : Parameter key.
            - `None`: Return dictionary of all parameters.
            - `str`: Return value of parameter.

        Returns
        -------
        Status of database.
        """

        # Generate SQL.

        ## Global.
        if self.global_:
            sql = 'SHOW GLOBAL STATUS'

        ## Not global.
        else:
            sql = 'SHOW STATUS'

        # Execute SQL.

        ## Dictionary.
        if key is None:
            result = self.db.execute(sql, key=key)
            status = result.to_dict(val_field=1)

        ## Value.
        else:
            sql += ' LIKE :key'
            result = self.db.execute(sql, key=key)
            row = result.first()
            if row is None:
                status = None
            else:
                status = row['Value']

        return status


    def update(self, params: dict[str, str | float]) -> None:
        """
        Update parameter.

        Parameters
        ----------
        params : Update parameter key value pairs.
        """

        # Throw exception.
        raise AssertionError('database status not update')


class DatabaseParametersVariable(DatabaseParameters):
    """
    Database parameters variable type.
    """


    @overload
    def get(self) -> dict[str, str]: ...

    @overload
    def get(self, key: str) -> str | None: ...

    def get(self, key: str | None = None) -> dict[str, str] | str | None:
        """
        Get parameter.

        Parameters
        ----------
        key : Parameter key.
            - `None`: Return dictionary of all parameters.
            - `str`: Return value of parameter.

        Returns
        -------
        Variables of database.
        """

        # Generate SQL.

        ## Global.
        if self.global_:
            sql = 'SHOW GLOBAL VARIABLES'

        ## Not global.
        else:
            sql = 'SHOW VARIABLES'

        # Execute SQL.

        ## Dictionary.
        if key is None:
            result = self.db.execute(sql, key=key)
            variables = result.to_dict(val_field=1)

        ## Value.
        else:
            sql += ' LIKE :key'
            result = self.db.execute(sql, key=key)
            row = result.first()
            if row is None:
                variables = None
            else:
                variables = row['Value']

        return variables


    def update(self, params: dict[str, str | float]) -> None:
        """
        Update parameter.

        Parameters
        ----------
        params : Update parameter key value pairs.
        """

        # Generate SQL.
        sql_set_list = [
            '%s = %s' % (
                key,
                (
                    value
                    if type(value) in (int, float)
                    else "'%s'" % value
                )
            )
            for key, value in params.items()
        ]
        sql_set = ',\n    '.join(sql_set_list)

        ## Global.
        if self.global_:
            sql = f'SET GLOBAL {sql_set}'

        ## Not global.
        else:
            sql = f'SET {sql_set}'

        # Execute SQL.
        self.db.execute(sql)


class DatabaseParametersPragma(DatabaseParameters):
    """
    Database parameters pragma type.
    """


    def __init__(
        self,
        db: Database
    ) -> None:
        """
        Build instance attributes.

        Parameters
        ----------
        db: `Database` instance.
        """

        # Set parameter.
        self.db = db


    def get(self, key: str) -> str | None:
        """
        Get parameter.

        Parameters
        ----------
        key : Parameter key.

        Returns
        -------
        Variables of database.
        """

        # Generate SQL.
        sql = f'PRAGMA %s' % key

        # Execute SQL.
        result = self.db.execute(sql)
        row = result.first()
        if row is None:
            variables = None
        else:
            variables = row[0]

        return variables


    def update(self, params: dict[str, str | float]) -> None:
        """
        Update parameter.

        Parameters
        ----------
        params : Update parameter key value pairs.
        """

        # Generate SQL.
        sql_set_list = [
            'PRAGMA %s = %s' % (
                key,
                (
                    value
                    if type(value) in (int, float)
                    else "'%s'" % value
                )
            )
            for key, value in params.items()
        ]
        sql = ';\n'.join(sql_set_list)

        # Execute SQL.
        self.db.execute(sql)
