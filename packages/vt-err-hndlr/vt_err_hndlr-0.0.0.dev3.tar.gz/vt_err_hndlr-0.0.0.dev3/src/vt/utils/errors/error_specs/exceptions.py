#!/usr/bin/env python3
# coding=utf-8

"""
Exceptions and exception hierarchies native to `Vaastav Technologies (OPC) Private Limited` python code.
"""

from abc import abstractmethod
from subprocess import CalledProcessError
from typing import Protocol, override, overload
from vt.utils.commons.commons.core_py import fallback_on_none_strict
from vt.utils.errors.error_specs import (
    ERR_GENERIC_ERR,
    ERR_CMD_NOT_FOUND,
    ErrorMsgFormer,
)

errmsg = ErrorMsgFormer


class HasExitCode(Protocol):
    """
    Interface denoting that it stores an ``exit_code`` which can be used by applications during time of exit to denote
    an exit, error or ok condition using this error code.
    """

    @property
    @abstractmethod
    def exit_code(self) -> int:
        """
        :return: an exit code which can be used by applications during time of exit to denote
            an exit, error or ok condition using this error code.
        """
        ...


class VTException(Exception):
    """
    Exception class native to `Vaastav Technologies (OPC) Private Limited` python code.

    Encapsulates any known exception raised by known code and hence can be handled in internal projects, like CLI(s).
    """

    def __init__(self, *args, **kwargs):
        """
        Examples:

          * standalone exception raising:

            * plain class:

            >>> raise VTException
            Traceback (most recent call last):
            error_specs.exceptions.VTException

            * instance without message:

            >>> raise VTException()
            Traceback (most recent call last):
            error_specs.exceptions.VTException

            * instance with message:

            >>> raise VTException('Expected.')
            Traceback (most recent call last):
            error_specs.exceptions.VTException: Expected.

          * chain known exceptions from known code:

            * plain class:

            >>> raise VTException from ValueError
            Traceback (most recent call last):
            error_specs.exceptions.VTException: ValueError

            >>> raise VTException from ValueError()
            Traceback (most recent call last):
            error_specs.exceptions.VTException: ValueError

            >>> raise VTException from ValueError('cause message.')
            Traceback (most recent call last):
            error_specs.exceptions.VTException: ValueError: cause message.

            * plain cause class:

            >>> raise VTException() from ValueError
            Traceback (most recent call last):
            error_specs.exceptions.VTException: ValueError

            >>> raise VTException('main message') from ValueError
            Traceback (most recent call last):
            error_specs.exceptions.VTException: ValueError: main message

            * blank instance with cause class instance:

            >>> raise VTException() from ValueError()
            Traceback (most recent call last):
            error_specs.exceptions.VTException: ValueError

            * with message in cause:

            >>> raise VTException() from ValueError('cause message.')
            Traceback (most recent call last):
            error_specs.exceptions.VTException: ValueError: cause message.

            * with message in instance:

            >>> raise VTException('main message.') from ValueError
            Traceback (most recent call last):
            error_specs.exceptions.VTException: ValueError: main message.

            >>> raise VTException('main message.') from ValueError()
            Traceback (most recent call last):
            error_specs.exceptions.VTException: ValueError: main message.

          * chain known exceptions with their own message. The main instance message gets preference.

            >>> raise VTException('main message.') from ValueError('cause message.')
            Traceback (most recent call last):
            error_specs.exceptions.VTException: ValueError: main message.

          * chained exceptions are retained in ``cause`` property for further inspection and stack-trace.

            >>> try:
            ...     raise VTException('main message.') from ValueError('cause message.')
            ... except VTException as v:
            ...     v.cause
            ValueError('cause message.')

        :param args: arguments for ``Exception``.
        :param kwargs: extra keyword-args for more info storage.
        """
        super().__init__(*args)
        self.kwargs = kwargs

    @property
    def cause(self) -> BaseException | None:
        """
        :return: the ``__cause__`` of this exception, obtained when exception is raised using a ``from`` clause.
        """
        return self.__cause__

    def __str__(self) -> str:
        if not self.args and self.cause:
            if not self.cause.args:
                return f"{self.cause.__class__.__name__}"
            else:
                return f"{self.cause.__class__.__name__}: {self.cause.__str__()}"
        if self.args and not self.cause:
            return super().__str__()
        if self.args and self.cause:
            return f"{self.cause.__class__.__name__}: {super().__str__()}"
        return ""

    def to_dict(self) -> dict[str, str | None]:
        """
        :return: a structured dict version of the exception for structured logging.
        """
        return {
            "type": self.__class__.__name__,
            "message": str(self),
            "cause_type": type(self.cause).__name__ if self.cause else None,
            "cause_message": str(self.cause) if self.cause else None,
        }


class VTExitingException(VTException, HasExitCode):
    """
    A ``VTException`` that contains error code for exiting an application, if needed.
    """

    def __init__(self, *args, exit_code: int = ERR_GENERIC_ERR, **kwargs):
        """
        Examples:

          * standalone exceptions raising:

            >>> raise VTExitingException()
            Traceback (most recent call last):
            error_specs.exceptions.VTExitingException

          * standalone exceptions raising with error code:

            >>> raise VTExitingException(exit_code=30)
            Traceback (most recent call last):
            error_specs.exceptions.VTExitingException

          * standalone exceptions raising with message:

            >>> raise VTExitingException('Expected.')
            Traceback (most recent call last):
            error_specs.exceptions.VTExitingException: Expected.

          * standalone exceptions raising with message and error code:

            >>> raise VTExitingException('Expected.', exit_code=20)
            Traceback (most recent call last):
            error_specs.exceptions.VTExitingException: Expected.

          * chain known exceptions from known code:

            >>> raise VTExitingException('A relevant exception') from ValueError
            Traceback (most recent call last):
            error_specs.exceptions.VTExitingException: ValueError: A relevant exception

          * chain known exceptions from known code with error code:

            >>> raise VTExitingException('A relevant exception', exit_code=9) from ValueError
            Traceback (most recent call last):
            error_specs.exceptions.VTExitingException: ValueError: A relevant exception

          * chain known exceptions from known code:

            >>> raise VTExitingException('A relevant exception') from ValueError()
            Traceback (most recent call last):
            error_specs.exceptions.VTExitingException: ValueError: A relevant exception

          * chain known exceptions from known code with error code:

            >>> raise VTExitingException('A relevant exception', exit_code=40) from ValueError()
            Traceback (most recent call last):
            error_specs.exceptions.VTExitingException: ValueError: A relevant exception

          * chain known exceptions with their own message.

            >>> raise VTExitingException('A relevant exception') from ValueError('Unexpected value.')
            Traceback (most recent call last):
            error_specs.exceptions.VTExitingException: ValueError: A relevant exception

          * chain known exceptions with their own message with error code.

            >>> raise VTExitingException('A relevant exception', exit_code=90) from ValueError('Unexpected value.')
            Traceback (most recent call last):
            error_specs.exceptions.VTExitingException: ValueError: A relevant exception

          * chained exceptions are retained in ``cause`` property for further inspection and stact-trace.

            >>> try:
            ...     raise VTExitingException('Some exception message') from ValueError('Unexpected value.')
            ... except VTExitingException as v:
            ...     v.cause
            ValueError('Unexpected value.')

          * chained exceptions are retained in ``cause`` property for further inspection and stact-trace.

            >>> try:
            ...     raise VTExitingException('Some exception message', exit_code=10) from ValueError('Unexpected value.')
            ... except VTExitingException as v:
            ...     v.cause
            ValueError('Unexpected value.')

        :param args: arguments for ``Exception``.
        :param exit_code: exit code if application needs to exit.
        :param kwargs: extra keyword-args for more info storage.
        """
        super().__init__(*args, exit_code=exit_code, **kwargs)
        self._exit_code = exit_code

    @override
    @property
    def exit_code(self) -> int:
        return self._exit_code


class VTCmdException(VTExitingException):
    """
    A ``VTExitingException`` that is raised for a command error and contains error code and other details of the
    command error in question.
    """

    def __init__(
        self,
        *args,
        called_process_error: CalledProcessError,
        exit_code: int | None = None,
        **kwargs,
    ):
        """
        Examples:

          * Minimal usage with only `called_process_error`:

            >>> from subprocess import CalledProcessError
            >>> raise VTCmdException(called_process_error=CalledProcessError(10, 'uname')) # always use `from` clause.
            Traceback (most recent call last):
            error_specs.exceptions.VTCmdException: CalledProcessError: Command 'uname' returned non-zero exit status 10.

          * With custom message:

            >>> raise VTCmdException('Command failed', called_process_error=CalledProcessError(1, ['echo'])) # always use `from` clause.
            Traceback (most recent call last):
            error_specs.exceptions.VTCmdException: CalledProcessError: Command failed

          * With overridden exit code:

            >>> raise VTCmdException('Overridden exit code', called_process_error=CalledProcessError(1, 'ls'), exit_code=42) # always use `from` clause.
            Traceback (most recent call last):
            error_specs.exceptions.VTCmdException: CalledProcessError: Overridden exit code

          * With stderr attached in the original error:

            >>> err = CalledProcessError(2, 'cat', stderr='No such file or directory')
            >>> raise VTCmdException('Cat failed', called_process_error=err) # always use `from` clause.
            Traceback (most recent call last):
            error_specs.exceptions.VTCmdException: CalledProcessError: Cat failed

          * Without a custom message (defaults to CalledProcessError's __str__):

            >>> err = CalledProcessError(127, 'git --version')
            >>> raise VTCmdException(called_process_error=err) # always use `from` clause.
            Traceback (most recent call last):
            error_specs.exceptions.VTCmdException: CalledProcessError: Command 'git --version' returned non-zero exit status 127.

          * Chaining with `from` clause (preserves original stacktrace):

            >>> try:
            ...     raise CalledProcessError(128, ['git', 'fetch'], stderr='fatal: repository not found')
            ... except CalledProcessError as _e:
            ...     raise VTCmdException('Git fetch failed', called_process_error=_e) from _e
            Traceback (most recent call last):
            error_specs.exceptions.VTCmdException: CalledProcessError: Git fetch failed

          * `cause` reflects the `from` error when available:

            >>> try:
            ...     raise CalledProcessError(3, ['whoami'])
            ... except CalledProcessError as _e:
            ...     try:
            ...         raise VTCmdException('Whoami failed', called_process_error=_e) from _e
            ...     except VTCmdException as ve:
            ...         isinstance(ve.cause, CalledProcessError)
            True

          * `cause` falls back to `called_process_error` if not chained:

            >>> _e = CalledProcessError(1, 'ls')
            >>> ve = VTCmdException('Not chained', called_process_error=_e) # always use the `from` clause.
            >>> ve.cause is ve.called_process_error
            True

          * Access `exit_code` property (inherited from `VTExitingException`):

            >>> _e = CalledProcessError(99, ['fake-cmd'])
            >>> ve = VTCmdException('Custom fail', called_process_error=_e) # always use the `from` clause.
            >>> ve.exit_code
            99

          * Explicit override of exit code:

            >>> ve = VTCmdException('Manual exit code', called_process_error=_e, exit_code=11) # always use the `from` clause.
            >>> ve.exit_code
            11

          * Structured representation using `to_dict()`:

            >>> d = VTCmdException('Structured', called_process_error=_e).to_dict()
            >>> d["type"], d["message"]
            ('VTCmdException', 'CalledProcessError: Structured')

          * Raise with extra keyword arguments (retained in `.kwargs`):

            >>> ve = VTCmdException('With meta', called_process_error=_e, meta='x')
            >>> ve.kwargs['meta']
            'x'

        :param args: arguments for ``Exception``.
        :param called_process_error: the ``CalledProcessError`` that is to be encapsulated within this exception.
        :param exit_code: exit code supplied by the caller else exit code of the called process which err'd if
            ``None`` supplied or exit code not provided by the user.
        :param kwargs: extra keyword-args for more info storage.
        """
        super().__init__(
            *args,
            exit_code=fallback_on_none_strict(
                exit_code, called_process_error.returncode
            ),
            **kwargs,
        )
        self.called_process_error = called_process_error

    @override
    @property
    def cause(self) -> CalledProcessError:
        """
        Examples:

          * Fallback to called_process_error if no cause is set:

            >>> cpe = CalledProcessError(1, ['git', 'status'], output='err', stderr='fail')
            >>> ex = VTCmdException('git failed', called_process_error=cpe)
            >>> ex.cause is cpe
            True

          * Correct usage: ``raise ... from CalledProcessError``:

            >>> try:
            ...     cpe = CalledProcessError(1, ['git', 'status'])
            ...     raise VTCmdException('git failed', called_process_error=cpe) from cpe
            ... except VTCmdException as e:
            ...     isinstance(e.cause, CalledProcessError)
            True

          * Incorrect cause: set manually (simulating bad ``from``):

            >>> try:
            ...     e = VTCmdException('wrong cause', called_process_error=cpe)
            ...     e.__cause__ = ValueError('not a subprocess error')  # simulate wrong cause
            ...     _ = e.cause
            ... except TypeError as t:
            ...     'Expected cause to be CalledProcessError' in str(t)
            True

          * Fallback works even when cause is falsy (e.g., returncode 0):

            >>> cpe2 = CalledProcessError(0, ['git', 'status'], output='')
            >>> ex2 = VTCmdException('noop error', called_process_error=cpe2)
            >>> ex2.cause is cpe2
            True

          * Raise with both message and cause:

            >>> try:
            ...     cpe = CalledProcessError(1, ['git', 'fetch'])
            ...     raise VTCmdException('Fetch failed', called_process_error=cpe) from cpe
            ... except VTCmdException as ve:
            ...     str(ve)
            'CalledProcessError: Fetch failed'

        :return: the ``__cause__`` of this exception, obtained when exception is raised using a ``from`` clause.
            Else, ctor ``self.called_process_error`` if no ``from`` clause was used (not recommended).
        :raise TypeError: if the exception's ``__cause__``, which is set by the ``from`` clause, is anything different
            from ``CalledProcessError``.
        """
        if self.__cause__ is not None:
            if not isinstance(self.__cause__, CalledProcessError):
                raise TypeError(
                    f"Expected cause to be CalledProcessError, got {type(self.__cause__)}."
                )
            return self.__cause__
        return self.called_process_error


class VTCmdNotFoundError(VTExitingException):
    """
    A ``VTExitingException`` that is raised when a supposedly runnable command is not found.
    """

    @overload
    def __init__(
        self,
        *args,
        command: str | list[str],
        exit_code: int = ERR_CMD_NOT_FOUND,
        **kwargs,
    ): ...

    @overload
    def __init__(
        self,
        *args,
        file_not_found_error: FileNotFoundError,
        exit_code: int = ERR_CMD_NOT_FOUND,
        **kwargs,
    ): ...

    def __init__(
        self,
        *args,
        command: str | list[str] | None = None,
        file_not_found_error: FileNotFoundError | None = None,
        exit_code: int = ERR_CMD_NOT_FOUND,
        **kwargs,
    ):
        """
        Examples:

          * Atleast one of ``command`` or ``file_not_found_error`` must be provided:

            >>> raise VTCmdNotFoundError() # always use `from` clause.
            Traceback (most recent call last):
            ValueError: Either command or file_not_found_error is required

          * ``file_not_found_error`` must be a ``FileNotFoundError`` instance:

            >>> raise VTCmdNotFoundError(file_not_found_error=Exception()) # type: ignore[arg-type] # always use `from` clause.
            Traceback (most recent call last):
            TypeError: file_not_found_error must be of type/subtype FileNotFoundError

          * Minimal usage with only `command`:

            * When `command` is ``str``:

              >>> from subprocess import CalledProcessError
              >>> raise VTCmdNotFoundError(command="non-existent-command") # always use `from` clause.
              Traceback (most recent call last):
              error_specs.exceptions.VTCmdNotFoundError: Command `non-existent-command` not found

            * When ``command -i`` is ``list[str]`` (likely split by ``shlex.spli()``):

              >>> from subprocess import CalledProcessError
              >>> raise VTCmdNotFoundError(command=["non-existent-command", "-i"]) # always use `from` clause.
              Traceback (most recent call last):
              error_specs.exceptions.VTCmdNotFoundError: Command ['non-existent-command', '-i'] not found

          * Exception message details

            * ``command`` message taken when only command is supplied:

              >>> raise VTCmdNotFoundError(command="ne-cmd") # always use `from` clause.
              Traceback (most recent call last):
              error_specs.exceptions.VTCmdNotFoundError: Command `ne-cmd` not found

            * ``file_not_found_error`` message taken when only file_not_found_error is supplied:

              >>> raise VTCmdNotFoundError(file_not_found_error=FileNotFoundError("ne-cmd")) # always use `from` clause.
              Traceback (most recent call last):
              error_specs.exceptions.VTCmdNotFoundError: FileNotFoundError: ne-cmd

            * command default message taken when both command and file_not_found_error are supplied:

              >>> raise VTCmdNotFoundError(command="ne-cmd", file_not_found_error=FileNotFoundError("ne-cmd")) # always use `from` clause.
              Traceback (most recent call last):
              error_specs.exceptions.VTCmdNotFoundError: FileNotFoundError: Command `ne-cmd` not found

          * With custom message:

            >>> raise VTCmdNotFoundError('Command failed', command="ne-cmd") # always use `from` clause.
            Traceback (most recent call last):
            error_specs.exceptions.VTCmdNotFoundError: ('Command failed', 'Command `ne-cmd` not found')

          * With overridden exit code:

            * Without ``file_not_found_error``:

              >>> raise VTCmdNotFoundError(command="ne-cmd", exit_code=42) # always use `from` clause.
              Traceback (most recent call last):
              error_specs.exceptions.VTCmdNotFoundError: Command `ne-cmd` not found

            * With ``file_not_found_error``:

              >>> raise VTCmdNotFoundError(command="ne-cmd", file_not_found_error=FileNotFoundError("ne-cmd"), exit_code=42) # always use `from` clause.
              Traceback (most recent call last):
              error_specs.exceptions.VTCmdNotFoundError: FileNotFoundError: Command `ne-cmd` not found

            * With ``file_not_found_error``:

              >>> fe = FileNotFoundError()
              >>> raise VTCmdNotFoundError(command="ne-cmd", file_not_found_error=fe, exit_code=42) # always use `from` clause.
              Traceback (most recent call last):
              error_specs.exceptions.VTCmdNotFoundError: FileNotFoundError: Command `ne-cmd` not found

          * Chaining with `from` clause (preserves original stacktrace):

            >>> try:
            ...     raise FileNotFoundError("ne-cmd")
            ... except FileNotFoundError as _f:
            ...     raise VTCmdNotFoundError(file_not_found_error=_f) from _f
            Traceback (most recent call last):
            error_specs.exceptions.VTCmdNotFoundError: FileNotFoundError: ne-cmd

            >>> try:
            ...     raise FileNotFoundError(ERR_CMD_NOT_FOUND, "ne-cmd")
            ... except FileNotFoundError as _f:
            ...     raise VTCmdNotFoundError(file_not_found_error=_f, exit_code=ERR_CMD_NOT_FOUND) from _f
            Traceback (most recent call last):
            error_specs.exceptions.VTCmdNotFoundError: FileNotFoundError: [Errno 127] ne-cmd

            >>> try:
            ...     raise FileNotFoundError("ne-cmd")
            ... except FileNotFoundError as _f:
            ...     raise VTCmdNotFoundError(command="ne-cmd", file_not_found_error=_f) from _f
            Traceback (most recent call last):
            error_specs.exceptions.VTCmdNotFoundError: FileNotFoundError: Command `ne-cmd` not found

          * `cause` reflects the `from` error when available:

            >>> try:
            ...     raise FileNotFoundError("ne-cmd")
            ... except FileNotFoundError as _f:
            ...     try:
            ...         raise VTCmdNotFoundError(file_not_found_error=_f) from _f
            ...     except VTCmdNotFoundError as ve:
            ...         isinstance(ve.cause, FileNotFoundError)
            True

          * `cause` falls back to `called_process_error` if not chained:

            >>> _f = FileNotFoundError(ERR_CMD_NOT_FOUND, "ne-cmd")
            >>> ve = VTCmdNotFoundError(file_not_found_error=_f) # always use the `from` clause.
            >>> ve.cause is ve.file_not_found_error
            True

          * Access `exit_code` property (inherited from `VTExitingException`):

            >>> _f = FileNotFoundError('fake-cmd')
            >>> ve = VTCmdNotFoundError('Custom fail', file_not_found_error=_f, exit_code=ERR_CMD_NOT_FOUND) # always use the `from` clause.
            >>> ve.exit_code
            127

          * Explicit override of exit code:

            >>> ve = VTCmdNotFoundError('Manual exit code', file_not_found_error=_f, exit_code=11) # always use the `from` clause.
            >>> ve.exit_code
            11

          * Structured representation using `to_dict()`:

            >>> d = VTCmdNotFoundError('Structured', file_not_found_error=_f).to_dict()
            >>> d["type"], d["message"]
            ('VTCmdNotFoundError', 'FileNotFoundError: Structured')

          * Raise with extra keyword arguments (retained in `.kwargs`):

            >>> ve = VTCmdNotFoundError('With meta', file_not_found_error=_f, meta='x')
            >>> ve.kwargs['meta']
            'x'

        :param args: arguments for ``Exception``.
        :param command: ``str`` command for the non-existant command which was attempted to run. ``list[str]`` for
            non-existent commands that are ``shlex.split``'ed.
        :param file_not_found_error: the ``FileNotFoundError`` that is to be encapsulated within this exception.
        :param exit_code: exit code can be supplied by the caller.
        :param kwargs: extra keyword-args for more info storage.
        """
        if not command and not file_not_found_error:
            raise ValueError(
                errmsg.at_least_one_required("command", "file_not_found_error")
            )
        if command:
            args = (
                *args,
                f"Command {f'`{command}`' if isinstance(command, str) else command} not found",
            )
        if file_not_found_error and not isinstance(
            file_not_found_error, FileNotFoundError
        ):
            raise TypeError(
                "file_not_found_error must be of type/subtype FileNotFoundError"
            )
        super().__init__(*args, exit_code=exit_code, **kwargs)
        self.command = command
        self.file_not_found_error = file_not_found_error

    @override
    @property
    def cause(self) -> FileNotFoundError | None:
        """
        Examples:

          * Fallback to called_process_error if no cause is set:

            >>> _f = FileNotFoundError(1, ['git', 'status'])
            >>> ex = VTCmdNotFoundError('git failed', file_not_found_error=_f)
            >>> ex.cause is _f
            True

          * Correct usage: ``raise ... from CalledProcessError``:

            >>> try:
            ...     fpe = FileNotFoundError(['git', 'status'])
            ...     raise VTCmdNotFoundError('git failed', file_not_found_error=fpe) from fpe
            ... except VTCmdNotFoundError as ve:
            ...     isinstance(ve.cause, FileNotFoundError)
            True

          * Incorrect cause: set manually (simulating bad ``from``):

            >>> try:
            ...     _e = VTCmdNotFoundError('wrong cause', file_not_found_error=_f)
            ...     _e.__cause__ = ValueError('not a subprocess error')  # simulate wrong cause
            ...     _ = _e.cause
            ... except TypeError as t:
            ...     'Expected cause to be FileNotFoundError' in str(t)
            True

          * Fallback works even when cause is falsy (e.g., returncode 0):

            >>> fpe2 = FileNotFoundError(['git', 'status'])
            >>> ex2 = VTCmdNotFoundError('noop error', file_not_found_error=fpe2)
            >>> ex2.cause is fpe2
            True

          * Raise with both message and cause:

            >>> try:
            ...     fpe = FileNotFoundError(1, ['git', 'fetch'])
            ...     raise VTCmdNotFoundError('Fetch failed', file_not_found_error=fpe) from fpe
            ... except VTCmdNotFoundError as ve:
            ...     str(ve)
            'FileNotFoundError: Fetch failed'

        :return: the ``__cause__`` of this exception, obtained when exception is raised using a ``from`` clause.
            Else, ctor ``self.called_process_error`` if no ``from`` clause was used (not recommended).
        :raise TypeError: if the exception's ``__cause__``, which is set by the ``from`` clause, is anything different
            from ``CalledProcessError``.
        """
        if self.__cause__ is not None:
            if not isinstance(self.__cause__, FileNotFoundError):
                raise TypeError(
                    f"Expected cause to be FileNotFoundError, got {type(self.__cause__)}."
                )
            return self.__cause__
        return self.file_not_found_error
