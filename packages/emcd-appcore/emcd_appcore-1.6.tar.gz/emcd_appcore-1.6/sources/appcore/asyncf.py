# vim: set filetype=python fileencoding=utf-8:
# -*- coding: utf-8 -*-

#============================================================================#
#                                                                            #
#  Licensed under the Apache License, Version 2.0 (the "License");           #
#  you may not use this file except in compliance with the License.          #
#  You may obtain a copy of the License at                                   #
#                                                                            #
#      http://www.apache.org/licenses/LICENSE-2.0                            #
#                                                                            #
#  Unless required by applicable law or agreed to in writing, software       #
#  distributed under the License is distributed on an "AS IS" BASIS,         #
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  #
#  See the License for the specific language governing permissions and       #
#  limitations under the License.                                            #
#                                                                            #
#============================================================================#


''' Helper functions for async execution. '''


from . import __
from . import exceptions as _exceptions
from . import generics as _generics


@__.typx.overload
async def gather_async(  # pragma: no cover
    *operands: __.typx.Any,
    return_exceptions: __.typx.Literal[ True ],
    error_message: str = 'Failure of async operations.',
    ignore_nonawaitables: bool = False,
) -> tuple[ _generics.GenericResult, ... ]: ...


@__.typx.overload
async def gather_async(  # noqa: F811  # pragma: no cover
    *operands: __.typx.Any,
    return_exceptions: __.typx.Literal[ False ] = False,
    error_message: str = 'Failure of async operations.',
    ignore_nonawaitables: bool = False,
) -> tuple[ __.typx.Any, ... ]: ...


async def gather_async(  # noqa: F811
    *operands: __.typx.Any,
    return_exceptions: __.typx.Annotated[
        bool,
        __.ddoc.Doc( ''' Raw or wrapped results. Wrapped, if true. ''' )
    ] = False,
    error_message: str = 'Failure of async operations.',
    ignore_nonawaitables: __.typx.Annotated[
        bool,
        __.ddoc.Doc(
            ''' Ignore or error on non-awaitables. Ignore, if true. ''' )
    ] = False,
) -> tuple[ __.typx.Any, ... ]:
    ''' Gathers results from invocables concurrently and asynchronously. '''
    from exceptiongroup import ExceptionGroup  # TODO: Python 3.11: builtin
    if ignore_nonawaitables:
        results = await _gather_async_permissive( operands )
    else:
        results = await _gather_async_strict( operands )
    if return_exceptions: return tuple( results )
    errors = tuple( result.error for result in results if result.is_error( ) )
    if errors: raise ExceptionGroup( error_message, errors )
    return tuple( result.extract( ) for result in results )


async def intercept_error_async(
    awaitable: __.cabc.Awaitable[ __.typx.Any ]
) -> _generics.Result[ object, Exception ]:
    ''' Converts unwinding exceptions to error results.

        Exceptions, which are not instances of :py:exc:`Exception` or one of
        its subclasses, are allowed to propagate. In particular,
        :py:exc:`KeyboardInterrupt` and :py:exc:`SystemExit` must be allowed
        to propagate to be consistent with :py:class:`asyncio.TaskGroup`
        behavior.

        Helpful when working with :py:func:`asyncio.gather`, for example,
        because exceptions can be distinguished from computed values
        and collected together into an exception group.

        In general, it is a bad idea to swallow exceptions. In this case,
        the intent is to add them into an exception group for continued
        propagation.
    '''
    try: return _generics.Value( await awaitable )
    except Exception as exc:
        return _generics.Error( exc )


async def _gather_async_permissive(
    operands: __.cabc.Sequence[ __.typx.Any ]
) -> __.cabc.Sequence[ __.typx.Any ]:
    from asyncio import gather  # TODO? Python 3.11: TaskGroup
    awaitables: dict[ int, __.cabc.Awaitable[ __.typx.Any ] ] = { }
    results: list[ _generics.GenericResult ] = [ ]
    for i, operand in enumerate( operands ):
        if isinstance( operand, __.cabc.Awaitable ):
            awaitables[ i ] = (
                intercept_error_async( __.typx.cast(
                    __.cabc.Awaitable[ __.typx.Any ], operand ) ) )
            results.append( _generics.Value( None ) )
        else: results.append( _generics.Value( operand ) )
    results_ = await gather( *awaitables.values( ) )
    for i, result in zip( awaitables.keys( ), results_ ):
        results[ i ] = result
    return results


async def _gather_async_strict(
    operands: __.cabc.Sequence[ __.typx.Any ]
) -> __.cabc.Sequence[ __.typx.Any ]:
    from asyncio import gather  # TODO? Python 3.11: TaskGroup
    from inspect import isawaitable, iscoroutine
    awaitables: list[ __.cabc.Awaitable[ __.typx.Any ] ] = [ ]
    for operand in operands: # Sanity check.
        if isawaitable( operand ): continue
        for operand_ in operands: # Cleanup.
            if iscoroutine( operand_ ): operand_.close( )
        raise _exceptions.AsyncAssertionFailure( operand )
    for operand in operands:
        awaitables.append( intercept_error_async( __.typx.cast( # noqa: PERF401
            __.cabc.Awaitable[ __.typx.Any ], operand ) ) )
    return await gather( *awaitables )


if __.typx.TYPE_CHECKING: # pragma: no cover
    async def _type_check_canary( ) -> None:
        ''' Canary function to verify overload type checking works correctly.

            This function is never executed but helps ensure that Pyright
            correctly understands our gather_async overloads.
        '''
        async def dummy_operation( ) -> str: return "test"

        operations = ( dummy_operation( ), dummy_operation( ) )
        results = await gather_async( *operations, return_exceptions = True )
        for result in results:
            match result:
                case _generics.Value( value ): _ = value
                case _generics.Error( error ): _ = error
                case _: pass
        for result in results:
            if _generics.is_error( result ): _ = result.error
            else: _ = result.extract( )
        values = await gather_async( *operations, return_exceptions = False )
        for value in values: _ = str( value )
