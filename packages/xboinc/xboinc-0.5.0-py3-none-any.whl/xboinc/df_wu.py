# copyright ###################################### #
# This file is part of the Xboinc Package.         #
# Copyright (c) CERN, 2025.                        #
# ################################################ #

import json
import sqlite3
from datetime import datetime, timedelta
from typing import Any, Dict, Optional, Union

import pandas as pd

from xaux import FsPath, timestamp

from .server.paths import infowudir
from .user import list_registered_users

wu_db = infowudir / "wu_status.db"
wu_db_dev = infowudir / "wu_status_dev.db"
user_db = infowudir / "users.db"


def _get_read_only_wu_db_connection(dev_server: bool = False) -> sqlite3.Connection:
    """Get a read-only database connection."""
    conn = sqlite3.connect(f"file:{wu_db_dev if dev_server else wu_db}?mode=ro", uri=True)
    return conn


def _get_read_only_user_db_connection() -> sqlite3.Connection:
    """Get a read-only user database connection."""
    conn = sqlite3.connect(f"file:{user_db}?mode=ro", uri=True)
    return conn


###################### Getters #################################################


def query_all_work_units(dev_server=False) -> pd.DataFrame:
    """List all work units in the database as a Pandas DataFrame."""
    with _get_read_only_wu_db_connection(dev_server) as conn:
        df = pd.read_sql_query("SELECT * FROM wu_status", conn)
        return df


def query_work_units_by_user(user: str, dev_server=False) -> pd.DataFrame:
    """List all work units for a specific user as a Pandas DataFrame."""
    with _get_read_only_wu_db_connection(dev_server) as conn:
        df = pd.read_sql_query(
            "SELECT * FROM wu_status WHERE user=?", conn, params=(user,)
        )
        return df


def query_work_units_by_status(status: str, dev_server=False) -> pd.DataFrame:
    """List all work units with a specific status as a Pandas DataFrame."""
    with _get_read_only_wu_db_connection(dev_server) as conn:
        df = pd.read_sql_query(
            "SELECT * FROM wu_status WHERE status=? AND dev_server=?",
            conn,
            params=(status, dev_server),
        )
        return df


def query_registered_work_units(
    status: Optional[str] = None, dev_server: bool = False
) -> pd.DataFrame:
    """
    List all work units for the registered users with an optional status filter.

    Parameters
    ----------
    status : Optional[str]
        The status to filter work units (e.g., 'running', 'completed').
    dev_server : bool
        Whether to query for the development server or production server.

    Returns
    -------
    pd.DataFrame
        DataFrame containing the work units for the user.
    """
    all_df = None
    for i, user in enumerate(list_registered_users()):
        if status:
            df = query_work_units_by_status(status, dev_server)
            df = df[df["user"] == user]
        else:
            df = query_work_units_by_user(user, dev_server)
        if i == 0:
            all_df = df
        else:
            all_df = pd.concat([all_df, df], ignore_index=True)
    return all_df


def query_subscribed_users() -> list[tuple[str, str]]:
    """
    Get a list of all users subscribed to the work unit database with their status.

    Returns
    -------
    list[tuple[str, str]]
        List of tuples containing (username, status) for users subscribed to the work unit database.
    """
    with _get_read_only_user_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT user, status FROM users")
        users = [(row[0], row[1]) for row in cursor.fetchall()]
    return users


def check_user_subscription(user: str) -> str:
    """
    Check if a user is subscribed to the work unit database.

    Parameters
    ----------
    user : str
        The username to check.

    Returns
    -------
    str
        The status of the user if subscribed, "not_subscribed" otherwise,
        "broken" if the user's directory is invalid.
    """
    users = query_subscribed_users()
    for u, status in users:
        if u == user:
            return status
    return "not_subscribed"
