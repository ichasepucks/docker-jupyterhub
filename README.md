# docker-jupyterhub

## Repro Steps for DB timeouts
1. clone repo
2. docker-compose up --build
3. wait until you see
```
jupyterhub    | 22:35:38.186 - info: [ConfigProxy] 200 GET /api/routes
jupyterhub    | INFO:sqlalchemy.engine.base.Engine:COMMIT
jupyterhub    | 2017-10-13 22:35:38,187 INFO sqlalchemy.engine.base.Engine COMMIT
jupyterhub    | INFO:sqlalchemy.pool.QueuePool:Invalidate connection <mysql.connector.connection.MySQLConnection object at 0x7f55aea89b70> (reason: InterfaceError:2013: Lost connection to MySQL server during query)
jupyterhub    | 2017-10-13 22:35:38,218 INFO sqlalchemy.pool.QueuePool Invalidate connection <mysql.connector.connection.MySQLConnection object at 0x7f55aea89b70> (reason: InterfaceError:2013: Lost connection to MySQL server during query)
jupyterhub    | [E 2017-10-13 22:35:38.220 JupyterHub ioloop:638] Exception in callback functools.partial(<function wrap.<locals>.null_wrapper at 0x7f55ae57aea0>, <tornado.concurrent.Future object at 0x7f55ae549710>)
jupyterhub    |     Traceback (most recent call last):
jupyterhub    |       File "/opt/conda/lib/python3.5/site-packages/tornado/ioloop.py", line 605, in _run_callback
jupyterhub    |         ret = callback()
jupyterhub    |       File "/opt/conda/lib/python3.5/site-packages/tornado/stack_context.py", line 277, in null_wrapper
jupyterhub    |         return fn(*args, **kwargs)
jupyterhub    |       File "/opt/conda/lib/python3.5/site-packages/tornado/ioloop.py", line 626, in _discard_future_result
jupyterhub    |         future.result()
jupyterhub    |       File "/opt/conda/lib/python3.5/site-packages/jupyterhub/app.py", line 1513, in update_last_activity
jupyterhub    |         self.db.commit()
jupyterhub    |       File "/opt/conda/lib/python3.5/site-packages/sqlalchemy/orm/session.py", line 906, in commit
jupyterhub    |         self.transaction.commit()
jupyterhub    |       File "/opt/conda/lib/python3.5/site-packages/sqlalchemy/orm/session.py", line 465, in commit
jupyterhub    |         t[1].commit()
jupyterhub    |       File "/opt/conda/lib/python3.5/site-packages/sqlalchemy/engine/base.py", line 1632, in commit
jupyterhub    |         self._do_commit()
jupyterhub    |       File "/opt/conda/lib/python3.5/site-packages/sqlalchemy/engine/base.py", line 1663, in _do_commit
jupyterhub    |         self.connection._commit_impl()
jupyterhub    |       File "/opt/conda/lib/python3.5/site-packages/sqlalchemy/engine/base.py", line 723, in _commit_impl
jupyterhub    |         self._handle_dbapi_exception(e, None, None, None, None)
jupyterhub    |       File "/opt/conda/lib/python3.5/site-packages/sqlalchemy/engine/base.py", line 1402, in _handle_dbapi_exception
jupyterhub    |         exc_info
jupyterhub    |       File "/opt/conda/lib/python3.5/site-packages/sqlalchemy/util/compat.py", line 203, in raise_from_cause
jupyterhub    |         reraise(type(exception), exception, tb=exc_tb, cause=cause)
jupyterhub    |       File "/opt/conda/lib/python3.5/site-packages/sqlalchemy/util/compat.py", line 186, in reraise
jupyterhub    |         raise value.with_traceback(tb)
jupyterhub    |       File "/opt/conda/lib/python3.5/site-packages/sqlalchemy/engine/base.py", line 721, in _commit_impl
jupyterhub    |         self.engine.dialect.do_commit(self.connection)
jupyterhub    |       File "/opt/conda/lib/python3.5/site-packages/sqlalchemy/dialects/mysql/base.py", line 1586, in do_commit
jupyterhub    |         dbapi_connection.commit()
jupyterhub    |       File "/opt/conda/lib/python3.5/site-packages/mysql/connector/connection.py", line 850, in commit
jupyterhub    |         self._execute_query("COMMIT")
jupyterhub    |       File "/opt/conda/lib/python3.5/site-packages/mysql/connector/connection.py", line 869, in _execute_query
jupyterhub    |         self.cmd_query(query)
jupyterhub    |       File "/opt/conda/lib/python3.5/site-packages/mysql/connector/connection.py", line 488, in cmd_query
jupyterhub    |         result = self._handle_result(self._send_cmd(ServerCmd.QUERY, query))
jupyterhub    |       File "/opt/conda/lib/python3.5/site-packages/mysql/connector/connection.py", line 267, in _send_cmd
jupyterhub    |         return self._socket.recv()
jupyterhub    |       File "/opt/conda/lib/python3.5/site-packages/mysql/connector/network.py", line 228, in recv_plain
jupyterhub    |         raise errors.InterfaceError(errno=2013)
jupyterhub    |     sqlalchemy.exc.InterfaceError: (mysql.connector.errors.InterfaceError) 2013: Lost connection to MySQL server during query
```
