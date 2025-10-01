from __future__ import annotations
import numpy
import ostk.core.type
import typing
from . import d2
from . import d3
__all__ = ['Angle', 'd2', 'd3']
class Angle:
    class Unit:
        """
        Members:
        
          Undefined
        
          Radian
        
          Degree
        
          Arcminute
        
          Arcsecond
        
          Revolution
        """
        Arcminute: typing.ClassVar[Angle.Unit]  # value = <Unit.Arcminute: 3>
        Arcsecond: typing.ClassVar[Angle.Unit]  # value = <Unit.Arcsecond: 4>
        Degree: typing.ClassVar[Angle.Unit]  # value = <Unit.Degree: 2>
        Radian: typing.ClassVar[Angle.Unit]  # value = <Unit.Radian: 1>
        Revolution: typing.ClassVar[Angle.Unit]  # value = <Unit.Revolution: 5>
        Undefined: typing.ClassVar[Angle.Unit]  # value = <Unit.Undefined: 0>
        __members__: typing.ClassVar[dict[str, Angle.Unit]]  # value = {'Undefined': <Unit.Undefined: 0>, 'Radian': <Unit.Radian: 1>, 'Degree': <Unit.Degree: 2>, 'Arcminute': <Unit.Arcminute: 3>, 'Arcsecond': <Unit.Arcsecond: 4>, 'Revolution': <Unit.Revolution: 5>}
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def arcminutes(value: ostk.core.type.Real) -> Angle:
        """
                        Create an angle from a value in arcminutes.
        
                        Args:
                            value (float): The angle value in arcminutes.
        
                        Returns:
                            Angle: An angle with the specified value in arcminutes.
        
                        Example:
                            >>> angle = Angle.arcminutes(60.0)
                            >>> angle.in_degrees()  # 1.0
        """
    @staticmethod
    def arcseconds(value: ostk.core.type.Real) -> Angle:
        """
                        Create an angle from a value in arcseconds.
        
                        Args:
                            value (float): The angle value in arcseconds.
        
                        Returns:
                            Angle: An angle with the specified value in arcseconds.
        
                        Example:
                            >>> angle = Angle.arcseconds(3600.0)
                            >>> angle.in_degrees()  # 1.0
        """
    @staticmethod
    @typing.overload
    def between(first_vector: numpy.ndarray[numpy.float64[2, 1]], second_vector: numpy.ndarray[numpy.float64[2, 1]]) -> Angle:
        """
                        Calculate the angle between two 2D vectors.
        
                        Args:
                            first_vector (np.array): The first vector.
                            second_vector (np.array): The second vector.
        
                        Returns:
                            Angle: The angle between the vectors.
        
                        Example:
                            >>> v1 = np.array([1.0, 0.0])
                            >>> v2 = np.array([0.0, 1.0])
                            >>> angle = Angle.between(v1, v2)
                            >>> angle.in_degrees()  # 90.0
        """
    @staticmethod
    @typing.overload
    def between(first_vector: numpy.ndarray[numpy.float64[3, 1]], second_vector: numpy.ndarray[numpy.float64[3, 1]]) -> Angle:
        """
                        Calculate the angle between two 3D vectors.
        
                        Args:
                            first_vector (np.array): The first vector.
                            second_vector (np.array): The second vector.
        
                        Returns:
                            Angle: The angle between the vectors.
        
                        Example:
                            >>> v1 = np.array([1.0, 0.0, 0.0])
                            >>> v2 = np.array([0.0, 1.0, 0.0])
                            >>> angle = Angle.between(v1, v2)
                            >>> angle.in_degrees()  # 90.0
        """
    @staticmethod
    def degrees(value: ostk.core.type.Real) -> Angle:
        """
                        Create an angle from a value in degrees.
        
                        Args:
                            value (float): The angle value in degrees.
        
                        Returns:
                            Angle: An angle with the specified value in degrees.
        
                        Example:
                            >>> angle = Angle.degrees(180.0)
                            >>> angle.in_radians()  # ~3.14159
        """
    @staticmethod
    def half_pi() -> Angle:
        """
                        Create an angle of π/2 radians (90 degrees).
        
                        Returns:
                            Angle: An angle of π/2 radians.
        
                        Example:
                            >>> half_pi = Angle.half_pi()
                            >>> half_pi.in_degrees()  # 90.0
        """
    @staticmethod
    def pi() -> Angle:
        """
                        Create an angle of π radians (180 degrees).
        
                        Returns:
                            Angle: An angle of π radians.
        
                        Example:
                            >>> pi = Angle.pi()
                            >>> pi.in_degrees()  # 180.0
        """
    @staticmethod
    def radians(value: ostk.core.type.Real) -> Angle:
        """
                        Create an angle from a value in radians.
        
                        Args:
                            value (float): The angle value in radians.
        
                        Returns:
                            Angle: An angle with the specified value in radians.
        
                        Example:
                            >>> angle = Angle.radians(3.14159)
                            >>> angle.in_degrees()  # ~180.0
        """
    @staticmethod
    def revolutions(value: ostk.core.type.Real) -> Angle:
        """
                        Create an angle from a value in revolutions.
        
                        Args:
                            value (float): The angle value in revolutions.
        
                        Returns:
                            Angle: An angle with the specified value in revolutions.
        
                        Example:
                            >>> angle = Angle.revolutions(1.0)
                            >>> angle.in_degrees()  # 360.0
        """
    @staticmethod
    def string_from_unit(unit: typing.Any) -> ostk.core.type.String:
        """
                        Get the string representation of an angle unit.
        
                        Args:
                            unit (Angle.Unit): The angle unit.
        
                        Returns:
                            str: String representation of the unit.
        
                        Example:
                            >>> Angle.string_from_unit(Angle.Unit.Degree)  # "Degree"
        """
    @staticmethod
    def symbol_from_unit(unit: typing.Any) -> ostk.core.type.String:
        """
                        Get the symbol representation of an angle unit.
        
                        Args:
                            unit (Angle.Unit): The angle unit.
        
                        Returns:
                            str: Symbol representation of the unit.
        
                        Example:
                            >>> Angle.symbol_from_unit(Angle.Unit.Degree)  # "deg"
                            >>> Angle.symbol_from_unit(Angle.Unit.Radian)  # "rad"
        """
    @staticmethod
    def two_pi() -> Angle:
        """
                        Create an angle of 2π radians (360 degrees).
        
                        Returns:
                            Angle: An angle of 2π radians.
        
                        Example:
                            >>> two_pi = Angle.two_pi()
                            >>> two_pi.in_degrees()  # 360.0
        """
    @staticmethod
    def undefined() -> Angle:
        """
                        Create an undefined angle.
        
                        Returns:
                            Angle: An undefined angle.
        
                        Example:
                            >>> undefined_angle = Angle.undefined()
                            >>> undefined_angle.is_defined()  # False
        """
    @staticmethod
    def zero() -> Angle:
        """
                        Create a zero angle.
        
                        Returns:
                            Angle: A zero angle (0 radians).
        
                        Example:
                            >>> zero_angle = Angle.zero()
                            >>> zero_angle.is_zero()  # True
        """
    def __add__(self, arg0: Angle) -> Angle:
        ...
    def __eq__(self, arg0: Angle) -> bool:
        ...
    def __iadd__(self, arg0: Angle) -> Angle:
        ...
    def __imul__(self, arg0: ostk.core.type.Real) -> Angle:
        ...
    def __init__(self, value: ostk.core.type.Real, unit: typing.Any) -> None:
        """
                        Create an angle with specified value and unit.
        
                        Args:
                            value (float): The numerical value of the angle.
                            unit (Angle.Unit): The unit of the angle (Radian, Degree, etc.).
        
                        Example:
                            >>> angle = Angle(3.14159, Angle.Unit.Radian)
                            >>> angle = Angle(180.0, Angle.Unit.Degree)
        """
    def __isub__(self, arg0: Angle) -> Angle:
        ...
    def __itruediv__(self, arg0: ostk.core.type.Real) -> Angle:
        ...
    def __mul__(self, arg0: ostk.core.type.Real) -> Angle:
        ...
    def __ne__(self, arg0: Angle) -> bool:
        ...
    def __neg__(self) -> Angle:
        ...
    def __pos__(self) -> Angle:
        ...
    def __repr__(self) -> str:
        ...
    def __str__(self) -> str:
        ...
    def __sub__(self, arg0: Angle) -> Angle:
        ...
    def __truediv__(self, arg0: ostk.core.type.Real) -> Angle:
        ...
    def get_unit(self) -> ...:
        """
                        Get the unit of the angle.
        
                        Returns:
                            Angle.Unit: The unit of the angle.
        
                        Example:
                            >>> angle = Angle.degrees(90.0)
                            >>> angle.get_unit()  # Angle.Unit.Degree
        """
    @typing.overload
    def in_arcminutes(self) -> ostk.core.type.Real:
        """
                        Get the angle value in arcminutes.
        
                        Returns:
                            float: The angle value in arcminutes.
        
                        Example:
                            >>> angle = Angle.degrees(1.0)
                            >>> angle.in_arcminutes()  # 60.0
        """
    @typing.overload
    def in_arcminutes(self, lower_bound: ostk.core.type.Real, upper_bound: ostk.core.type.Real) -> ostk.core.type.Real:
        """
                        Get the angle value in arcminutes within specified bounds.
        
                        Args:
                            lower_bound (float): The lower bound in arcminutes.
                            upper_bound (float): The upper bound in arcminutes.
        
                        Returns:
                            float: The angle value in arcminutes, wrapped within bounds.
        """
    @typing.overload
    def in_arcseconds(self) -> ostk.core.type.Real:
        """
                        Get the angle value in arcseconds.
        
                        Returns:
                            float: The angle value in arcseconds.
        
                        Example:
                            >>> angle = Angle.degrees(1.0)
                            >>> angle.in_arcseconds()  # 3600.0
        """
    @typing.overload
    def in_arcseconds(self, lower_bound: ostk.core.type.Real, upper_bound: ostk.core.type.Real) -> ostk.core.type.Real:
        """
                        Get the angle value in arcseconds within specified bounds.
        
                        Args:
                            lower_bound (float): The lower bound in arcseconds.
                            upper_bound (float): The upper bound in arcseconds.
        
                        Returns:
                            float: The angle value in arcseconds, wrapped within bounds.
        """
    @typing.overload
    def in_degrees(self) -> ostk.core.type.Real:
        """
                        Get the angle value in degrees.
        
                        Returns:
                            float: The angle value in degrees.
        
                        Example:
                            >>> angle = Angle.radians(3.14159)
                            >>> angle.in_degrees()  # ~180.0
        """
    @typing.overload
    def in_degrees(self, lower_bound: ostk.core.type.Real, upper_bound: ostk.core.type.Real) -> ostk.core.type.Real:
        """
                        Get the angle value in degrees within specified bounds.
        
                        Args:
                            lower_bound (float): The lower bound in degrees.
                            upper_bound (float): The upper bound in degrees.
        
                        Returns:
                            float: The angle value in degrees, wrapped within bounds.
        
                        Example:
                            >>> angle = Angle.degrees(450.0)
                            >>> angle.in_degrees(-180.0, 180.0)  # 90.0
        """
    @typing.overload
    def in_radians(self) -> ostk.core.type.Real:
        """
                        Get the angle value in radians.
        
                        Returns:
                            float: The angle value in radians.
        
                        Example:
                            >>> angle = Angle.degrees(180.0)
                            >>> angle.in_radians()  # ~3.14159
        """
    @typing.overload
    def in_radians(self, lower_bound: ostk.core.type.Real, upper_bound: ostk.core.type.Real) -> ostk.core.type.Real:
        """
                        Get the angle value in radians within specified bounds.
        
                        Args:
                            lower_bound (float): The lower bound in radians.
                            upper_bound (float): The upper bound in radians.
        
                        Returns:
                            float: The angle value in radians, wrapped within bounds.
        
                        Example:
                            >>> angle = Angle.radians(7.0)
                            >>> angle.in_radians(-3.14159, 3.14159)  # Wrapped to [-π, π]
        """
    def in_revolutions(self) -> ostk.core.type.Real:
        """
                        Get the angle value in revolutions.
        
                        Returns:
                            float: The angle value in revolutions.
        
                        Example:
                            >>> angle = Angle.degrees(360.0)
                            >>> angle.in_revolutions()  # 1.0
        """
    def in_unit(self, unit: typing.Any) -> ostk.core.type.Real:
        """
                        Get the angle value in a specific unit.
        
                        Args:
                            unit (Angle.Unit): The unit to convert to.
        
                        Returns:
                            float: The angle value in the specified unit.
        
                        Example:
                            >>> angle = Angle.degrees(180.0)
                            >>> angle.in_unit(Angle.Unit.Radian)  # ~3.14159
        """
    def is_defined(self) -> bool:
        """
                        Check if the angle is defined.
        
                        Returns:
                            bool: True if the angle is defined, False otherwise.
        
                        Example:
                            >>> angle = Angle.radians(1.0)
                            >>> angle.is_defined()  # True
        """
    def is_near(self, angle: Angle, tolerance: Angle) -> bool:
        """
                        Check if this angle is near another angle within a tolerance.
        
                        Args:
                            angle (Angle): The angle to compare with.
                            tolerance (Angle): The tolerance for comparison.
        
                        Returns:
                            bool: True if angles are within tolerance, False otherwise.
        
                        Example:
                            >>> angle1 = Angle.degrees(30.0)
                            >>> angle2 = Angle.degrees(30.1)
                            >>> tolerance = Angle.degrees(0.2)
                            >>> angle1.is_near(angle2, tolerance)  # True
        """
    def is_negative(self) -> bool:
        """
                        Check if the angle is negative.
        
                        Returns:
                            bool: True if the angle is negative, False otherwise.
        
                        Example:
                            >>> angle = Angle.degrees(-30.0)
                            >>> angle.is_negative()  # True
        """
    def is_zero(self) -> bool:
        """
                        Check if the angle is zero.
        
                        Returns:
                            bool: True if the angle is zero, False otherwise.
        
                        Example:
                            >>> angle = Angle.zero()
                            >>> angle.is_zero()  # True
        """
    def to_string(self, precision: ostk.core.type.Integer = ...) -> ostk.core.type.String:
        """
                        Convert the angle to a string representation.
        
                        Args:
                            precision (int, optional): The precision for floating point numbers. Defaults to Integer.undefined().
        
                        Returns:
                            str: String representation of the angle.
        
                        Example:
                            >>> angle = Angle.degrees(90.0)
                            >>> angle.to_string()  # "90.0 [deg]"
        """
