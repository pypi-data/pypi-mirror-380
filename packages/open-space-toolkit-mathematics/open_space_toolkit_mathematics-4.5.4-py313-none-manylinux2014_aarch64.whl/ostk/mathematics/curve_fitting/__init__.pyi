from __future__ import annotations
import numpy
import typing
from . import interpolator
__all__ = ['Interpolator', 'interpolator']
class Interpolator:
    class Type:
        """
        Members:
        
          BarycentricRational
        
          CubicSpline
        
          Linear
        """
        BarycentricRational: typing.ClassVar[Interpolator.Type]  # value = <Type.BarycentricRational: 0>
        CubicSpline: typing.ClassVar[Interpolator.Type]  # value = <Type.CubicSpline: 1>
        Linear: typing.ClassVar[Interpolator.Type]  # value = <Type.Linear: 2>
        __members__: typing.ClassVar[dict[str, Interpolator.Type]]  # value = {'BarycentricRational': <Type.BarycentricRational: 0>, 'CubicSpline': <Type.CubicSpline: 1>, 'Linear': <Type.Linear: 2>}
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
    @staticmethod
    def generate_interpolator(interpolation_type: Interpolator.Type, x: numpy.ndarray[numpy.float64[m, 1]], y: numpy.ndarray[numpy.float64[m, 1]]) -> Interpolator:
        """
                        Generate an interpolator of specified type with data points.
        
                        Args:
                            interpolation_type (Interpolator.Type): The type of interpolation.
                            x (np.array): The x-coordinates of data points.
                            y (np.array): The y-coordinates of data points.
        
                        Returns:
                            Interpolator: The created interpolator.
        
                        Example:
                            >>> x = np.array([0.0, 1.0, 2.0])
                            >>> y = np.array([0.0, 2.0, 4.0])
                            >>> interpolator = Interpolator.generate_interpolator(
                            ...     Interpolator.Type.CubicSpline, x, y
                            ... )
        """
    def __init__(self, interpolation_type: Interpolator.Type) -> None:
        """
                        Create an interpolator of specified type.
        
                        Args:
                            interpolation_type (Interpolator.Type): The type of interpolation method.
        
                        Example:
                            >>> interpolator = Interpolator(Interpolator.Type.Linear)
        """
    @typing.overload
    def compute_derivative(self, x: float) -> float:
        """
                        Compute the derivative of the interpolation at a single point.
        
                        Args:
                            x (float): The x-coordinate to compute derivative at.
        
                        Returns:
                            float: The derivative value.
        
                        Example:
                            >>> interpolator = Interpolator.generate_interpolator(
                            ...     Interpolator.Type.Linear, [0.0, 1.0], [0.0, 2.0]
                            ... )
                            >>> derivative = interpolator.compute_derivative(0.5)  # 2.0
        """
    @typing.overload
    def compute_derivative(self, x: numpy.ndarray[numpy.float64[m, 1]]) -> numpy.ndarray[numpy.float64[m, 1]]:
        """
                        Compute the derivative of the interpolation at multiple points.
        
                        Args:
                            x (np.array): The x-coordinates to compute derivatives at.
        
                        Returns:
                            (np.array): The derivative values.
        
                        Example:
                            >>> interpolator = Interpolator.generate_interpolator(
                            ...     Interpolator.Type.Linear, [0.0, 1.0], [0.0, 2.0]
                            ... )
                            >>> derivatives = interpolator.compute_derivative([0.2, 0.8])
        """
    @typing.overload
    def evaluate(self, x: numpy.ndarray[numpy.float64[m, 1]]) -> numpy.ndarray[numpy.float64[m, 1]]:
        """
                        Evaluate the interpolation at multiple points.
        
                        Args:
                            x (np.array): The x-coordinates to evaluate at.
        
                        Returns:
                            (np.array): The interpolated y-values.
        
                        Example:
                            >>> interpolator = Interpolator.generate_interpolator(
                            ...     Interpolator.Type.Linear, [0.0, 1.0], [0.0, 2.0]
                            ... )
                            >>> result = interpolator.evaluate([0.5, 1.5])
        """
    @typing.overload
    def evaluate(self, x: float) -> float:
        """
                        Evaluate the interpolation at a single point.
        
                        Args:
                            x (float): The x-coordinate to evaluate at.
        
                        Returns:
                            float: The interpolated y-value.
        
                        Example:
                            >>> interpolator = Interpolator.generate_interpolator(
                            ...     Interpolator.Type.Linear, [0.0, 1.0], [0.0, 2.0]
                            ... )
                            >>> result = interpolator.evaluate(0.5)  # 1.0
        """
    def get_interpolation_type(self) -> Interpolator.Type:
        """
                        Get the interpolation type of this interpolator.
        
                        Returns:
                            Interpolator.Type: The interpolation type.
        
                        Example:
                            >>> interpolator = Interpolator(Interpolator.Type.CubicSpline)
                            >>> type = interpolator.get_interpolation_type()
        """
