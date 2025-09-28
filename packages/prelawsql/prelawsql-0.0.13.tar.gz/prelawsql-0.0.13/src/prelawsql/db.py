import logging
import sqlite3
from collections.abc import Iterable
from pathlib import Path
from typing import Any

import click
from sqlite_utils.db import Table, View


def extract_gravatars(v: Any, file: Path) -> list[str]:
    gravatars = []
    if not v:
        raise KeyError(f"No gravatar identifiers in {file=}")
    if isinstance(v, str):
        gravatars.append(v)
    elif isinstance(v, list):
        gravatars = v
    else:
        raise TypeError(f"Improper gravatars type in {file=}")
    if not gravatars:
        raise NotImplementedError(f"Missing author gravatars in {file=}")
    return gravatars


def check_table(tbl) -> Table:
    """Results in `sqlite_utils.db.Table` casting."""
    if isinstance(tbl, Table):
        return tbl
    raise TypeError("Must be a valid table.")


def check_view(v) -> View:
    """Results in `sqlite_utils.db.View` casting."""
    if isinstance(v, View):
        return v
    raise TypeError("Must be a valid view.")


def add_idx(tbl, cols: Iterable):
    """Add an index on a set of columns using a fixed naming convention.

    Args:
        tbl: A `sqlite_utils.db.Table`.
        cols: Iterable of column names.

    Notes:
        Index name is generated as:
        `idx_<table_name>_<col1>_<col2>_...`

    Examples:
        >>> from sqlite_utils import Database
        >>> db = Database(":memory:")
        >>> tbl = db["items"]
        >>> tbl.insert({"id": 1, "name": "Alice"})
        <Table items (id, name)>
        >>> add_idx(tbl, ["id", "name"])
        >>> tbl.indexes
        [Index(seq=0, name='idx_items_id_name', unique=0, origin='c', partial=0, columns=['id', 'name'])]
        >>> db.close()
    """
    if isinstance(tbl, Table):
        tbl.create_index(
            columns=cols,
            index_name=f"idx_{tbl.name.lower()}_{'_'.join(list(cols))}",
            if_not_exists=True,
        )


def get_database_path(conn: sqlite3.Connection) -> str:
    """Return the file path of the SQLite database for a given connection.

    Args:
        conn: SQLite connection.

    Returns:
        str: Path to the database file.

    Raises:
        FileNotFoundError: If the database path cannot be determined.

    Examples:
        >>> import sqlite3
        >>> conn = sqlite3.connect(":memory:")
        >>> get_database_path(conn)
        ''
        >>> conn.close()
    """
    cursor = conn.execute("PRAGMA database_list;")
    # The database path is in the third column of the first row returned
    row = cursor.fetchone()
    if row is not None:
        return row[2]  # The path to the database file
    raise FileNotFoundError


def run_sql_file(conn: Any, file: Path, prefix_expr: str | None = None):
    """Execute SQL statements from a file against a database connection.

    Args:
        conn: A `sqlite3.Connection`.
        file: Path to the SQL file.
        prefix_expr: Optional SQL expression to prepend (e.g., PRAGMA).

    Raises:
        Exception: If the connection is not a `sqlite3.Connection`.

    Examples:
        >>> import sqlite3, tempfile
        >>> conn = sqlite3.connect(":memory:")
        >>> sql_file = Path(tempfile.gettempdir()) / "demo.sql"
        >>> _ = sql_file.write_text("CREATE TABLE demo (id INTEGER);")
        >>> run_sql_file(conn, sql_file)
        >>> conn.execute("SELECT name FROM sqlite_master").fetchone()[0]
        'demo'
        >>> conn.close()
    """
    if not isinstance(conn, sqlite3.Connection):
        raise Exception("Could not get connection.")
    cur = conn.cursor()
    sql = file.read_text()
    if prefix_expr:
        sql = "\n".join((prefix_expr, sql))
    cur.execute(sql)
    conn.commit()


def run_sql_folder(db_name: str, folder: Path, pattern: str = "*.sql"):
    """Assumes that a folder contains `*.sql` files that can be executed against the
    database represented by `db_name`.
    """
    msg = "Run special sql files..."
    logging.info(msg)
    click.echo(msg)

    con = sqlite3.connect(db_name)
    cur = con.cursor()
    recipes = folder.glob(pattern)
    for recipe_file in recipes:
        sub_msg = f"script: {recipe_file=}"
        logging.info(sub_msg)
        click.echo(sub_msg)

        sql = recipe_file.read_text()
        cur.execute(sql)
        con.commit()
    con.close()
