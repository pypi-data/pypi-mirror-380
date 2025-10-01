"""
The Youtube Autonomous Testing Module.
"""
from typing import Union
from dotenv import load_dotenv

import functools
import os
import pytest


TEST_FILES_PATH = 'test_files'
"""
The relative path to the test files
folder. This is the one we should use
in all our projects.
"""

def assert_exception_is_raised(
    function: callable,
    exception_type: Union[Exception, str, None] = None,
    message: Union[str, None] = None
):
    """
    Call this method providing some code defined
    as a function to validate that it is raising
    an exception when called (send the function,
    not the call).

    The 'exception_type' can be an Exception, a
    TypeError, a ValueError, a string including
    the name of the exception type to expect, or
    None if the type is not important and must 
    not be checked.

    The 'message' can be the string we expect to
    be received as the exception message, or None
    if we don't care about the message. We will
    look for the provided 'message' text inside
    the exception message, it can be a part of 
    the message and not the exact one.

    Here is an example:
    ```
    assert_exception_is_raised(
        function = lambda: ParameterValidator.validate_tuple('tuple', 3),
        exception_type = None,
        message = 'The provided "tuple" parameter is not a tuple.'
    )
    ```
    """
    with pytest.raises(
        expected_exception = Exception,
        match = message
    ) as exception:
        function()

    # Any exception is subclass of 'Exception'
    # so we avoid checking it
    if isinstance(exception_type, str):
        if exception_type != 'Exception':
            assert exception.type.__name__ == exception_type
    elif exception_type is not None:
        if exception_type != Exception:
            assert exception.type == exception_type

def float_approx_to_compare(float):
    """
    Compare float values with 
    approximation due to the decimal
    differences we can have.

    Then, you can compare floats by
    using:

    - `assert fa == float_approx_to_compare(fb)`
    """
    return pytest.approx(float, rel = 1e-5, abs = 1e-8)


def skip_pytest(
    env_var: str = 'SKIP_TESTS'
):
    """
    *Decorator*

    Decorator to skip the pytest if the env
    variable 'env_var' is set and has a valid
    value ('1', 'true', 'yes', ''). This is
    useful when we have some tests we want to
    execute only in local, so we can set the
    variable in remote environments to avoid
    them of being executed.
    """
    def decorator(
        function
    ):
        @functools.wraps(function)
        def wrapper(
            *args,
            **kwargs
        ):
            path = os.getcwd().replace('\\', '/')
            load_dotenv(f'{path}/.env')
            env_var_value = os.getenv(env_var, '').lower()

            if env_var_value in ('1', 'true', 'yes', ''):
                pytest.skip(f'Skipping test "{function.__name__}": file-related tests are disabled by configuration ("{env_var_value}" environment variable).')

            return function(*args, **kwargs)
        
        return wrapper
    
    return decorator

class TestFilesHandler:
    """
    Class to easily handle the files we
    create when testing the projects.
    
    This class must be instantiated before
    the tests are executed, and the 
    '.delete_new_files()' method must be
    called when all the tests have finished.
    """

    __test__ = False
    """
    Attribute to be ignored by pytest.
    """

    @property
    def files(
        self
    ) -> list[str]:
        """
        The files that are currently in the
        'test_files' folder.
        """
        return set(os.listdir(self._test_files_path))

    def __init__(
        self,
        test_files_path: str = TEST_FILES_PATH
    ):
        self._test_files_path: str = test_files_path
        """
        The relative path to the test files
        folder.
        """
        self._initial_files: list[str] = self.files
        """
        The files that were available when the
        class was instantiated (before executing
        the tests).
        """

    def delete_new_files(
        self
    ) -> list[str]:
        """
        Delete all the new files found and return
        a list containing the names of the files
        that have been deleted.
        """
        files_removed = []

        for f in self.files - self._initial_files:
            path = os.path.join(self._test_files_path, f)
            if os.path.isfile(path):
                os.remove(path)
                files_removed.append(path)

        return files_removed