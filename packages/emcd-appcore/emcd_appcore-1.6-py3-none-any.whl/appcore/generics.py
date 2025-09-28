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


''' Generic types. '''
# TODO: Independent package.


from . import __


T = __.typx.TypeVar( 'T' ) # generic
U = __.typx.TypeVar( 'U' ) # generic
E = __.typx.TypeVar( 'E', bound = Exception ) # error


class Result( __.immut.Protocol, __.typx.Generic[ T, E ] ):
    ''' Either a value or an error. '''

    def is_error( self ) -> bool:
        ''' Returns ``True`` if error result. Else ``False``. '''
        return isinstance( self, Error )

    def is_value( self ) -> bool:
        ''' Returns ``True`` if value result. Else ``False``. '''
        return isinstance( self, Value )

    @__.abc.abstractmethod
    def extract( self ) -> T:
        ''' Extracts value from result. Else, raises error from result.

            Similar to Result.unwrap in Rust.
        '''
        raise NotImplementedError  # pragma: no cover

    @__.abc.abstractmethod
    def transform(
        self, function: __.typx.Callable[ [ T ], U ]
    ) -> __.typx.Self | "Result[ U, E ]":
        ''' Transforms value in value result. Ignores error result.

            Similar to Result.map in Rust.
        '''
        raise NotImplementedError  # pragma: no cover


class Value( Result[ T, E ] ):
    ''' Result of successful computation. '''

    __match_args__ = ( 'value', )
    __slots__ = ( 'value', )

    value: T

    def __init__( self, value: T ): self.value = value

    def extract( self ) -> T: return self.value

    def transform(
        self, function: __.typx.Callable[ [ T ], U ]
    ) -> "Result[ U, E ]": return Value( function( self.value ) )


class Error( Result[ T, E ] ):
    ''' Result of failed computation. '''

    __match_args__ = ( 'error', )
    __slots__ = ( 'error', )

    error: E

    def __init__( self, error: E ): self.error = error

    def extract( self ) -> __.typx.Never: raise self.error

    def transform(
        self, function: __.typx.Callable[ [ T ], U ]
    ) -> __.typx.Self: return self


GenericResult: __.typx.TypeAlias = Result[ __.typx.Any, Exception ]


def is_error( result: Result[ T, E ] ) -> __.typx.TypeIs[ Error[ T, E ] ]:
    ''' Type guard: Returns ``True`` if result is an error. '''
    return isinstance( result, Error )


def is_value( result: Result[ T, E ] ) -> __.typx.TypeIs[ Value[ T, E ] ]:
    ''' Type guard: Returns ``True`` if result is a value. '''
    return isinstance( result, Value )
