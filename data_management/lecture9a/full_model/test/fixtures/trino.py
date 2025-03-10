from ...discover import remote_host
from trino.dbapi import connect
import contextlib

@contextlib.contextmanager
def remote_trino(stage):
    conn = connect(
        host=remote_host(stage, "Trino"),
        port=80,
        user="almalinux",
        catalog="hive"
    )
    cur = conn.cursor()
    yield cur