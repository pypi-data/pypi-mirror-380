from __future__ import annotations
import ostk.core.type
import typing
__all__ = ['RealInterval']
class RealInterval:
    class Type:
        """
        Members:
        
          Undefined
        
          Closed
        
          Open
        
          HalfOpenLeft
        
          HalfOpenRight
        """
        Closed: typing.ClassVar[RealInterval.Type]  # value = <Type.Closed: 1>
        HalfOpenLeft: typing.ClassVar[RealInterval.Type]  # value = <Type.HalfOpenLeft: 3>
        HalfOpenRight: typing.ClassVar[RealInterval.Type]  # value = <Type.HalfOpenRight: 4>
        Open: typing.ClassVar[RealInterval.Type]  # value = <Type.Open: 2>
        Undefined: typing.ClassVar[RealInterval.Type]  # value = <Type.Undefined: 0>
        __members__: typing.ClassVar[dict[str, RealInterval.Type]]  # value = {'Undefined': <Type.Undefined: 0>, 'Closed': <Type.Closed: 1>, 'Open': <Type.Open: 2>, 'HalfOpenLeft': <Type.HalfOpenLeft: 3>, 'HalfOpenRight': <Type.HalfOpenRight: 4>}
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
    def clip(intervals: list[RealInterval], clipping_interval: RealInterval) -> list[RealInterval]:
        """
                        Clip a list of intervals with a clipping interval.
        
                        Args:
                            intervals (list): List of intervals to clip.
                            clipping_interval (RealInterval): The interval to clip with.
        
                        Returns:
                            list: List of clipped intervals.
        
                        Example:
                            >>> intervals = [RealInterval.closed(0.0, 2.0), RealInterval.closed(3.0, 5.0)]
                            >>> clipping = RealInterval.closed(1.0, 4.0)
                            >>> clipped = RealInterval.clip(intervals, clipping)
        """
    @staticmethod
    def closed(lower_bound: ostk.core.type.Real, upper_bound: ostk.core.type.Real) -> RealInterval:
        """
                        Create a closed interval [a, b].
        
                        Args:
                            lower_bound (float): The lower bound (inclusive).
                            upper_bound (float): The upper bound (inclusive).
        
                        Returns:
                            RealInterval: A closed interval.
        
                        Example:
                            >>> interval = RealInterval.closed(0.0, 1.0)  # [0, 1]
                            >>> interval.contains(0.0)  # True
                            >>> interval.contains(1.0)  # True
        """
    @staticmethod
    def get_gaps(intervals: list[RealInterval], bound: RealInterval = ...) -> list[RealInterval]:
        """
                        Find gaps between intervals in a list.
        
                        Args:
                            intervals (list): List of intervals to find gaps between.
                            bound (RealInterval, optional): Bounding interval to consider gaps within. Defaults to undefined.
        
                        Returns:
                            list: List of intervals representing gaps.
        
                        Example:
                            >>> intervals = [RealInterval.closed(0.0, 1.0), RealInterval.closed(2.0, 3.0)]
                            >>> gaps = RealInterval.get_gaps(intervals)  # Gap from 1.0 to 2.0
        """
    @staticmethod
    def half_open_left(lower_bound: ostk.core.type.Real, upper_bound: ostk.core.type.Real) -> RealInterval:
        """
                        Create a half-open interval (a, b].
        
                        Args:
                            lower_bound (float): The lower bound (exclusive).
                            upper_bound (float): The upper bound (inclusive).
        
                        Returns:
                            RealInterval: A half-open left interval.
        
                        Example:
                            >>> interval = RealInterval.half_open_left(0.0, 1.0)  # (0, 1]
                            >>> interval.contains(0.0)  # False
                            >>> interval.contains(1.0)  # True
        """
    @staticmethod
    def half_open_right(lower_bound: ostk.core.type.Real, upper_bound: ostk.core.type.Real) -> RealInterval:
        """
                        Create a half-open interval [a, b).
        
                        Args:
                            lower_bound (float): The lower bound (inclusive).
                            upper_bound (float): The upper bound (exclusive).
        
                        Returns:
                            RealInterval: A half-open right interval.
        
                        Example:
                            >>> interval = RealInterval.half_open_right(0.0, 1.0)  # [0, 1)
                            >>> interval.contains(0.0)  # True
                            >>> interval.contains(1.0)  # False
        """
    @staticmethod
    def logical_and(intervals_1: list[RealInterval], intervals_2: list[RealInterval]) -> list[RealInterval]:
        """
                        Perform logical AND operation on two lists of intervals.
        
                        Args:
                            intervals_1 (list): First list of intervals.
                            intervals_2 (list): Second list of intervals.
        
                        Returns:
                            list: List of intervals representing the intersection of both lists.
        
                        Example:
                            >>> intervals1 = [RealInterval.closed(0.0, 2.0)]
                            >>> intervals2 = [RealInterval.closed(1.0, 3.0)]
                            >>> result = RealInterval.logical_and(intervals1, intervals2)  # [1.0, 2.0]
        """
    @staticmethod
    def logical_or(intervals_1: list[RealInterval], intervals_2: list[RealInterval]) -> list[RealInterval]:
        """
                        Perform logical OR operation on two lists of intervals.
        
                        Args:
                            intervals_1 (list): First list of intervals.
                            intervals_2 (list): Second list of intervals.
        
                        Returns:
                            list: List of intervals representing the union of both lists.
        
                        Example:
                            >>> intervals1 = [RealInterval.closed(0.0, 1.0)]
                            >>> intervals2 = [RealInterval.closed(2.0, 3.0)]
                            >>> result = RealInterval.logical_or(intervals1, intervals2)
        """
    @staticmethod
    def merge(intervals: list[RealInterval]) -> list[RealInterval]:
        """
                        Merge overlapping intervals in a list.
        
                        Args:
                            intervals (list): List of intervals to merge.
        
                        Returns:
                            list: List of merged intervals with no overlaps.
        
                        Example:
                            >>> intervals = [RealInterval.closed(0.0, 2.0), RealInterval.closed(1.0, 3.0)]
                            >>> merged = RealInterval.merge(intervals)  # [RealInterval.closed(0.0, 3.0)]
        """
    @staticmethod
    def open(lower_bound: ostk.core.type.Real, upper_bound: ostk.core.type.Real) -> RealInterval:
        """
                        Create an open interval (a, b).
        
                        Args:
                            lower_bound (float): The lower bound (exclusive).
                            upper_bound (float): The upper bound (exclusive).
        
                        Returns:
                            RealInterval: An open interval.
        
                        Example:
                            >>> interval = RealInterval.open(0.0, 1.0)  # (0, 1)
                            >>> interval.contains(0.0)  # False
                            >>> interval.contains(1.0)  # False
                            >>> interval.contains(0.5)  # True
        """
    @staticmethod
    def sort(intervals: list[RealInterval], by_lower_bound: bool = True, ascending: bool = True) -> list[RealInterval]:
        """
                        Sort a list of intervals.
        
                        Args:
                            intervals (list): List of intervals to sort.
                            by_lower_bound (bool, optional): Sort by lower bound if True, upper bound if False. Defaults to True.
                            ascending (bool, optional): Sort in ascending order if True, descending if False. Defaults to True.
        
                        Returns:
                            list: Sorted list of intervals.
        
                        Example:
                            >>> intervals = [RealInterval.closed(2.0, 3.0), RealInterval.closed(0.0, 1.0)]
                            >>> sorted_intervals = RealInterval.sort(intervals)
        """
    @staticmethod
    def undefined() -> RealInterval:
        """
                        Create an undefined interval.
        
                        Returns:
                            RealInterval: An undefined interval.
        
                        Example:
                            >>> undefined_interval = RealInterval.undefined()
                            >>> undefined_interval.is_defined()  # False
        """
    def __eq__(self, arg0: RealInterval) -> bool:
        ...
    def __init__(self, lower_bound: ostk.core.type.Real, upper_bound: ostk.core.type.Real, type: typing.Any) -> None:
        """
                        Create an interval with specified bounds and type.
        
                        Args:
                            lower_bound (float): The lower bound of the interval.
                            upper_bound (float): The upper bound of the interval.
                            type (RealInterval.Type): The type of interval (Closed, Open, HalfOpenLeft, HalfOpenRight).
        
                        Example:
                            >>> interval = RealInterval(0.0, 1.0, RealInterval.Type.Closed)  # [0, 1]
                            >>> interval = RealInterval(0.0, 1.0, RealInterval.Type.Open)    # (0, 1)
        """
    def __ne__(self, arg0: RealInterval) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __str__(self) -> str:
        ...
    @typing.overload
    def contains(self, real: ostk.core.type.Real) -> bool:
        """
                        Check if the interval contains a real number.
        
                        Args:
                            real (float): The real number to check.
        
                        Returns:
                            bool: True if the interval contains the number, False otherwise.
        
                        Example:
                            >>> interval = RealInterval.closed(0.0, 1.0)
                            >>> interval.contains(0.5)  # True
                            >>> interval.contains(1.5)  # False
        """
    @typing.overload
    def contains(self, interval: RealInterval) -> bool:
        """
                        Check if this interval contains another interval.
        
                        Args:
                            interval (RealInterval): The interval to check containment for.
        
                        Returns:
                            bool: True if this interval contains the other interval, False otherwise.
        
                        Example:
                            >>> interval1 = RealInterval.closed(0.0, 2.0)
                            >>> interval2 = RealInterval.closed(0.5, 1.5)
                            >>> interval1.contains(interval2)  # True
        """
    def get_intersection_with(self, interval: RealInterval) -> RealInterval:
        """
                        Get the intersection of this interval with another interval.
        
                        Args:
                            interval (RealInterval): The interval to intersect with.
        
                        Returns:
                            RealInterval: The intersection interval, or undefined if no intersection.
        
                        Example:
                            >>> interval1 = RealInterval.closed(0.0, 2.0)
                            >>> interval2 = RealInterval.closed(1.0, 3.0)
                            >>> intersection = interval1.get_intersection_with(interval2)
                            >>> # intersection represents [1.0, 2.0]
        """
    def get_lower_bound(self) -> ostk.core.type.Real:
        """
                        Get the lower bound of the interval.
        
                        Returns:
                            float: The lower bound value.
        
                        Example:
                            >>> interval = RealInterval.closed(0.0, 1.0)
                            >>> interval.get_lower_bound()  # 0.0
        """
    def get_union_with(self, interval: RealInterval) -> RealInterval:
        """
                        Get the union of this interval with another interval.
        
                        Args:
                            interval (RealInterval): The interval to union with.
        
                        Returns:
                            RealInterval: The union interval.
        
                        Example:
                            >>> interval1 = RealInterval.closed(0.0, 1.0)
                            >>> interval2 = RealInterval.closed(0.5, 2.0)
                            >>> union = interval1.get_union_with(interval2)
                            >>> # union represents [0.0, 2.0]
        """
    def get_upper_bound(self) -> ostk.core.type.Real:
        """
                        Get the upper bound of the interval.
        
                        Returns:
                            float: The upper bound value.
        
                        Example:
                            >>> interval = RealInterval.closed(0.0, 1.0)
                            >>> interval.get_upper_bound()  # 1.0
        """
    def intersects(self, interval: RealInterval) -> bool:
        """
                        Check if this interval intersects with another interval.
        
                        Args:
                            interval (RealInterval): The interval to check intersection with.
        
                        Returns:
                            bool: True if intervals intersect, False otherwise.
        
                        Example:
                            >>> interval1 = RealInterval.closed(0.0, 2.0)
                            >>> interval2 = RealInterval.closed(1.0, 3.0)
                            >>> interval1.intersects(interval2)  # True
        """
    def is_defined(self) -> bool:
        """
                        Check if the interval is defined.
        
                        Returns:
                            bool: True if the interval is defined, False otherwise.
        
                        Example:
                            >>> interval = RealInterval.closed(0.0, 1.0)
                            >>> interval.is_defined()  # True
        """
    def is_degenerate(self) -> bool:
        """
                        Check if the interval is degenerate (single point).
        
                        Returns:
                            bool: True if the interval represents a single point, False otherwise.
        
                        Example:
                            >>> interval = RealInterval.closed(1.0, 1.0)
                            >>> interval.is_degenerate()  # True
        """
    def to_string(self) -> ostk.core.type.String:
        """
                        Convert the interval to a string representation.
        
                        Returns:
                            str: String representation of the interval.
        
                        Example:
                            >>> interval = RealInterval.closed(0.0, 1.0)
                            >>> interval.to_string()  # "[0, 1]"
        """
