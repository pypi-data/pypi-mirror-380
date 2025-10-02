# Copyright 2018 Red Hat
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
from __future__ import absolute_import

import functools
import inspect
import typing
import unittest

import fixtures
import testtools

SKIP_CLASSES = unittest.SkipTest, testtools.TestCase.skipException

SkipException = unittest.SkipTest

SkipTarget = typing.Union[typing.Callable,
                          typing.Type[testtools.TestCase],
                          typing.Type[fixtures.Fixture]]
SkipDecorator = typing.Callable[[SkipTarget], SkipTarget]


SkipOnErrorType = typing.Union[typing.Type[Exception],
                               typing.Tuple[typing.Type[Exception], ...]]


def skip_test(reason: str,
              cause: Exception = None,
              bugzilla: int = None) -> typing.NoReturn:
    """Interrupt test case execution marking it as skipped for given reason"""
    if bugzilla is not None:
        reason += f'\nhttps://bugzilla.redhat.com/show_bug.cgi?id={bugzilla}\n'
    if cause is not None:
        reason += f"\n{cause}\n"
    raise unittest.SkipTest(reason) from cause


def skip(reason: str,
         bugzilla: int = None) -> SkipDecorator:
    """Mark test case for being skipped for a given reason"""
    return _skip_decorator(reason=reason, bugzilla=bugzilla)


def skip_if(reason: str,
            predicate: typing.Callable,
            *args,
            bugzilla: int = None,
            **kwargs) -> \
        SkipDecorator:
    """Mark test case for being skipped for a given reason if it matches"""
    predicate = _get_skip_predicate(predicate, *args, **kwargs)
    return _skip_decorator(reason=reason,
                           unless=False,
                           bugzilla=bugzilla,
                           predicate=predicate)


def skip_unless(reason: str,
                predicate: typing.Callable,
                *args,
                bugzilla: int = None,
                **kwargs) -> \
        SkipDecorator:
    """Mark test case for being skipped for a given reason unless it matches"""
    predicate = _get_skip_predicate(predicate, *args, **kwargs)
    return _skip_decorator(reason=reason,
                           unless=True,
                           bugzilla=bugzilla,
                           predicate=predicate)


def skip_on_error(reason: str,
                  predicate: typing.Callable,
                  *args,
                  error_type: SkipOnErrorType = None,
                  bugzilla: int = None,
                  **kwargs) -> \
        SkipDecorator:
    predicate = _get_skip_predicate(predicate, *args, **kwargs)
    return _skip_decorator(reason=reason,
                           error_type=error_type,
                           bugzilla=bugzilla,
                           predicate=predicate)


def _skip_decorator(reason: str,
                    unless: bool = None,
                    error_type: SkipOnErrorType = None,
                    bugzilla: int = None,
                    predicate: typing.Callable = None) \
        -> SkipDecorator:
    """Mark test case for being skipped for a given reason unless it matches"""

    if error_type is None:
        error_type = tuple()

    def decorator(obj: SkipTarget) -> SkipTarget:
        method = _get_skip_method(obj)

        @functools.wraps(method)
        def wrapper(*args, **kwargs):
            _reason = reason
            cause: typing.Optional[Exception] = None
            if predicate is not None:
                return_value: typing.Any = None
                try:
                    return_value = predicate()
                except error_type as ex:
                    cause = ex
                else:
                    if unless in [None, bool(return_value)]:
                        return method(*args, **kwargs)
                if '{return_value' in reason:
                    _reason = reason.format(return_value=return_value)
                if '{cause' in reason:
                    _reason = reason.format(cause=cause)
            skip_test(reason=_reason, cause=cause, bugzilla=bugzilla)

        if obj is method:
            return wrapper
        else:
            setattr(obj, method.__name__, wrapper)
            return obj

    return decorator


def _get_skip_method(obj: SkipTarget) -> typing.Callable:
    if inspect.isclass(obj):
        assert isinstance(obj, type)
        cls = typing.cast(typing.Type, obj)
        setup_method = getattr(cls, 'setUp', None)
        if callable(setup_method):
            return setup_method
        else:
            # Dummy setUp method implementation for abstract classes
            def setUp(self) -> None:
                super(cls, self).setUp()
            return setUp
    elif callable(obj):
        return obj
    else:
        raise TypeError(f"Object {obj} is not a class or a function")


def _get_skip_predicate(func: typing.Callable, *args, **kwargs) \
        -> typing.Callable:
    if args or kwargs:
        return functools.partial(func, *args, **kwargs)
    else:
        return func
