from __future__ import annotations
import numpy
import ostk.core.type
import ostk.mathematics.curve_fitting
import typing
__all__ = ['BarycentricRational', 'CubicSpline', 'Linear']
class BarycentricRational(ostk.mathematics.curve_fitting.Interpolator):
    def __init__(self, x: numpy.ndarray[numpy.float64[m, 1]], y: numpy.ndarray[numpy.float64[m, 1]]) -> None:
        """
                        Create a barycentric rational interpolator with data points.
        
                        Args:
                            x (np.array): The x-coordinates of data points.
                            y (np.array): The y-coordinates of data points.
        
                        Example:
                            >>> x = np.array([0.0, 1.0, 2.0, 3.0])
                            >>> y = np.array([1.0, 2.0, 0.5, 3.0])
                            >>> interpolator = BarycentricRational(x, y)
        """
    @typing.overload
    def compute_derivative(self, x: float) -> float:
        """
                        Compute the derivative of the barycentric rational interpolation at a single point.
        
                        Args:
                            x (float): The x-coordinate to compute derivative at.
        
                        Returns:
                            float: The derivative value.
        
                        Example:
                            >>> interpolator = BarycentricRational([0.0, 1.0, 2.0], [1.0, 2.0, 0.5])
                            >>> derivative = interpolator.compute_derivative(0.5)
        """
    @typing.overload
    def compute_derivative(self, x: numpy.ndarray[numpy.float64[m, 1]]) -> numpy.ndarray[numpy.float64[m, 1]]:
        """
                        Compute the derivative of the barycentric rational interpolation at multiple points.
        
                        Args:
                            x (np.array): The x-coordinates to compute derivatives at.
        
                        Returns:
                            (np.array): The derivative values.
        
                        Example:
                            >>> interpolator = BarycentricRational([0.0, 1.0, 2.0], [1.0, 2.0, 0.5])
                            >>> derivatives = interpolator.compute_derivative([0.2, 0.8])
        """
    @typing.overload
    def evaluate(self, x: numpy.ndarray[numpy.float64[m, 1]]) -> numpy.ndarray[numpy.float64[m, 1]]:
        """
                        Evaluate the barycentric rational interpolation at multiple points.
        
                        Args:
                            x (np.array): The x-coordinates to evaluate at.
        
                        Returns:
                            (np.array): The interpolated y-values.
        
                        Example:
                            >>> interpolator = BarycentricRational([0.0, 1.0, 2.0], [1.0, 2.0, 0.5])
                            >>> result = interpolator.evaluate([0.5, 1.5])
        """
    @typing.overload
    def evaluate(self, x: float) -> float:
        """
                        Evaluate the barycentric rational interpolation at a single point.
        
                        Args:
                            x (float): The x-coordinate to evaluate at.
        
                        Returns:
                            float: The interpolated y-value.
        
                        Example:
                            >>> interpolator = BarycentricRational([0.0, 1.0, 2.0], [1.0, 2.0, 0.5])
                            >>> result = interpolator.evaluate(0.5)
        """
class CubicSpline(ostk.mathematics.curve_fitting.Interpolator):
    @typing.overload
    def __init__(self, x: numpy.ndarray[numpy.float64[m, 1]], y: numpy.ndarray[numpy.float64[m, 1]]) -> None:
        """
                        Create a cubic spline interpolator with data points.
        
                        Args:
                            x (np.array): The x-coordinates of data points.
                            y (np.array): The y-coordinates of data points.
        
                        Example:
                            >>> x = np.array([0.0, 1.0, 2.0, 3.0])
                            >>> y = np.array([0.0, 1.0, 4.0, 9.0])
                            >>> interpolator = CubicSpline(x, y)
        """
    @typing.overload
    def __init__(self, y: numpy.ndarray[numpy.float64[m, 1]], x_0: ostk.core.type.Real, h: ostk.core.type.Real) -> None:
        """
                        Create a cubic spline interpolator with uniform spacing.
        
                        Args:
                            y (np.array): The y-coordinates of data points.
                            x_0 (float): The starting x-coordinate.
                            h (float): The uniform spacing between x-coordinates.
        
                        Example:
                            >>> y = np.array([0.0, 1.0, 4.0, 9.0])
                            >>> interpolator = CubicSpline(y, 0.0, 1.0)  # x = [0, 1, 2, 3]
        """
    @typing.overload
    def compute_derivative(self, x: float) -> float:
        """
                        Compute the derivative of the cubic spline at a single point.
        
                        Args:
                            x (float): The x-coordinate to compute derivative at.
        
                        Returns:
                            float: The derivative value.
        
                        Example:
                            >>> interpolator = CubicSpline([0.0, 1.0, 2.0], [0.0, 1.0, 4.0])
                            >>> derivative = interpolator.compute_derivative(0.5)
        """
    @typing.overload
    def compute_derivative(self, x: numpy.ndarray[numpy.float64[m, 1]]) -> numpy.ndarray[numpy.float64[m, 1]]:
        """
                        Compute the derivative of the cubic spline at multiple points.
        
                        Args:
                            x (np.array): The x-coordinates to compute derivatives at.
        
                        Returns:
                            (np.array): The derivative values.
        
                        Example:
                            >>> interpolator = CubicSpline([0.0, 1.0, 2.0], [0.0, 1.0, 4.0])
                            >>> derivatives = interpolator.compute_derivative([0.2, 0.8])
        """
    @typing.overload
    def evaluate(self, x: numpy.ndarray[numpy.float64[m, 1]]) -> numpy.ndarray[numpy.float64[m, 1]]:
        """
                        Evaluate the cubic spline interpolation at multiple points.
        
                        Args:
                            x (np.array): The x-coordinates to evaluate at.
        
                        Returns:
                            (np.array): The interpolated y-values.
        
                        Example:
                            >>> interpolator = CubicSpline([0.0, 1.0, 2.0], [0.0, 1.0, 4.0])
                            >>> result = interpolator.evaluate([0.5, 1.5])
        """
    @typing.overload
    def evaluate(self, x: float) -> float:
        """
                        Evaluate the cubic spline interpolation at a single point.
        
                        Args:
                            x (float): The x-coordinate to evaluate at.
        
                        Returns:
                            float: The interpolated y-value.
        
                        Example:
                            >>> interpolator = CubicSpline([0.0, 1.0, 2.0], [0.0, 1.0, 4.0])
                            >>> result = interpolator.evaluate(0.5)
        """
class Linear(ostk.mathematics.curve_fitting.Interpolator):
    def __init__(self, x: numpy.ndarray[numpy.float64[m, 1]], y: numpy.ndarray[numpy.float64[m, 1]]) -> None:
        """
                        Create a linear interpolator with data points.
        
                        Args:
                            x (np.array): The x-coordinates of data points.
                            y (np.array): The y-coordinates of data points.
        
                        Example:
                            >>> x = np.array([0.0, 1.0, 2.0])
                            >>> y = np.array([0.0, 2.0, 4.0])
                            >>> interpolator = Linear(x, y)
        """
    @typing.overload
    def compute_derivative(self, x: float) -> float:
        """
                        Compute the derivative of the linear interpolation at a single point.
        
                        Args:
                            x (float): The x-coordinate to compute derivative at.
        
                        Returns:
                            float: The derivative value.
        
                        Example:
                            >>> interpolator = Linear([0.0, 1.0], [0.0, 2.0])
                            >>> derivative = interpolator.compute_derivative(0.5)  # 2.0
        """
    @typing.overload
    def compute_derivative(self, x: numpy.ndarray[numpy.float64[m, 1]]) -> numpy.ndarray[numpy.float64[m, 1]]:
        """
                        Compute the derivative of the linear interpolation at multiple points.
        
                        Args:
                            x (np.array): The x-coordinates to compute derivatives at.
        
                        Returns:
                            (np.array): The derivative values.
        
                        Example:
                            >>> interpolator = Linear([0.0, 1.0], [0.0, 2.0])
                            >>> derivatives = interpolator.compute_derivative([0.2, 0.8])
        """
    @typing.overload
    def evaluate(self, x: numpy.ndarray[numpy.float64[m, 1]]) -> numpy.ndarray[numpy.float64[m, 1]]:
        """
                        Evaluate the linear interpolation at multiple points.
        
                        Args:
                            x (np.array): The x-coordinates to evaluate at.
        
                        Returns:
                            (np.array): The interpolated y-values.
        
                        Example:
                            >>> interpolator = Linear([0.0, 1.0], [0.0, 2.0])
                            >>> result = interpolator.evaluate([0.5, 1.5])
        """
    @typing.overload
    def evaluate(self, x: float) -> float:
        """
                        Evaluate the linear interpolation at a single point.
        
                        Args:
                            x (float): The x-coordinate to evaluate at.
        
                        Returns:
                            float: The interpolated y-value.
        
                        Example:
                            >>> interpolator = Linear([0.0, 1.0], [0.0, 2.0])
                            >>> result = interpolator.evaluate(0.5)  # 1.0
        """
