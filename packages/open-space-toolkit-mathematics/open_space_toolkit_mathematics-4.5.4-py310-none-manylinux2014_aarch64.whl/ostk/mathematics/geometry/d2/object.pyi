from __future__ import annotations
import numpy
import ostk.core.type
import ostk.mathematics.geometry.d2
import typing
__all__ = ['Composite', 'Line', 'LineString', 'MultiPolygon', 'Point', 'PointSet', 'Polygon', 'Segment', 'set_point_2_array', 'set_point_array']
class Composite(ostk.mathematics.geometry.d2.Object):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def empty() -> Composite:
        """
                        Create an empty 2D composite (containing no objects).
        
                        Returns:
                            Composite: An empty composite object.
        
                        Example:
                            >>> empty_composite = Composite.empty()
                            >>> empty_composite.is_empty()  # True
                            >>> empty_composite.get_object_count()  # 0
        """
    @staticmethod
    def undefined() -> Composite:
        """
                        Create an undefined 2D composite.
        
                        Returns:
                            Composite: An undefined composite object.
        
                        Example:
                            >>> undefined_composite = Composite.undefined()
                            >>> undefined_composite.is_defined()  # False
        """
    def __add__(self, arg0: Composite) -> Composite:
        ...
    def __eq__(self, arg0: Composite) -> bool:
        ...
    def __iadd__(self, arg0: Composite) -> Composite:
        ...
    def __init__(self, object: ostk.mathematics.geometry.d2.Object) -> None:
        """
                        Create a 2D composite object from a single geometric object.
        
                        Args:
                            object (Object): The 2D geometric object to wrap in the composite.
        
                        Example:
                            >>> point = Point(1.0, 2.0)
                            >>> composite = Composite(point)
        """
    def __ne__(self, arg0: Composite) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __str__(self) -> str:
        ...
    def access_object_at(self, index: int) -> ostk.mathematics.geometry.d2.Object:
        """
                        Access the object at a specific index in the 2D composite.
        
                        Args:
                            index (int): The index of the object to access.
        
                        Returns:
                            Object: Reference to the object at the specified index.
        
                        Raises:
                            IndexError: If the index is out of bounds.
        
                        Example:
                            >>> composite = Composite(Point(1.0, 2.0))
                            >>> obj = composite.access_object_at(0)
        """
    @typing.overload
    def any_contains(self, object: ostk.mathematics.geometry.d2.Object) -> bool:
        """
                        Check if any object in the 2D composite contains another geometric object.
        
                        Args:
                            object (Object): The 2D object to check containment for.
        
                        Returns:
                            bool: True if any object in the composite contains the object, False otherwise.
        
                        Example:
                            >>> polygon1 = Polygon([Point(0.0, 0.0), Point(1.0, 0.0), Point(1.0, 1.0)])
                            >>> polygon2 = Polygon([Point(2.0, 2.0), Point(3.0, 2.0), Point(3.0, 3.0)])
                            >>> composite = Composite(polygon1) + Composite(polygon2)
                            >>> point = Point(0.5, 0.5)
                            >>> composite.any_contains(point)  # True
        """
    @typing.overload
    def any_contains(self, composite: Composite) -> bool:
        """
                        Check if any object in the 2D composite contains another composite.
        
                        Args:
                            composite (Composite): The composite to check containment for.
        
                        Returns:
                            bool: True if any object in this composite contains the other composite, False otherwise.
        
                        Example:
                            >>> outer_polygon = Polygon([Point(0.0, 0.0), Point(3.0, 0.0), Point(3.0, 3.0)])
                            >>> composite1 = Composite(outer_polygon)
                            >>> inner_composite = Composite(Point(1.5, 1.5))
                            >>> composite1.any_contains(inner_composite)  # True
        """
    def apply_transformation(self, transformation: typing.Any) -> None:
        """
                        Apply a transformation to all objects in the 2D composite in place.
        
                        Args:
                            transformation (Transformation): The 2D transformation to apply.
        
                        Example:
                            >>> composite = Composite(Point(1.0, 2.0))
                            >>> transformation = Translation([1.0, 1.0])
                            >>> composite.apply_transformation(transformation)
        """
    def as_composite(self) -> Composite:
        """
                        Convert the composite to a 2D Composite object.
        
                        Returns:
                            Composite: The composite object contained in the composite.
        
                        Raises:
                            RuntimeError: If the composite does not contain a Composite.
        
                        Example:
                            >>> inner_composite = Composite(Point(1.0, 2.0))
                            >>> outer_composite = Composite(inner_composite)
                            >>> extracted_composite = outer_composite.as_composite()
        """
    def as_line(self) -> Line:
        """
                        Convert the composite to a 2D Line object.
        
                        Returns:
                            Line: The line object contained in the composite.
        
                        Raises:
                            RuntimeError: If the composite does not contain a Line.
        
                        Example:
                            >>> line = Line(Point(0.0, 0.0), np.array([1.0, 1.0]))
                            >>> composite = Composite(line)
                            >>> extracted_line = composite.as_line()
        """
    def as_line_string(self) -> LineString:
        """
                        Convert the composite to a 2D LineString object.
        
                        Returns:
                            LineString: The line string object contained in the composite.
        
                        Raises:
                            RuntimeError: If the composite does not contain a LineString.
        
                        Example:
                            >>> points = [Point(0.0, 0.0), Point(1.0, 1.0), Point(2.0, 2.0)]
                            >>> line_string = LineString(points)
                            >>> composite = Composite(line_string)
                            >>> extracted_line_string = composite.as_line_string()
        """
    def as_point(self) -> Point:
        """
                        Convert the composite to a 2D Point object.
        
                        Returns:
                            Point: The point object contained in the composite.
        
                        Raises:
                            RuntimeError: If the composite does not contain a Point.
        
                        Example:
                            >>> composite = Composite(Point(1.0, 2.0))
                            >>> point = composite.as_point()
        """
    def as_point_set(self) -> PointSet:
        """
                        Convert the composite to a 2D PointSet object.
        
                        Returns:
                            PointSet: The point set object contained in the composite.
        
                        Raises:
                            RuntimeError: If the composite does not contain a PointSet.
        
                        Example:
                            >>> point_set = PointSet([Point(1.0, 2.0), Point(3.0, 4.0)])
                            >>> composite = Composite(point_set)
                            >>> extracted_set = composite.as_point_set()
        """
    def as_polygon(self) -> Polygon:
        """
                        Convert the composite to a 2D Polygon object.
        
                        Returns:
                            Polygon: The polygon object contained in the composite.
        
                        Raises:
                            RuntimeError: If the composite does not contain a Polygon.
        
                        Example:
                            >>> vertices = [Point(0.0, 0.0), Point(1.0, 0.0), Point(1.0, 1.0)]
                            >>> polygon = Polygon(vertices)
                            >>> composite = Composite(polygon)
                            >>> extracted_polygon = composite.as_polygon()
        """
    def as_segment(self) -> Segment:
        """
                        Convert the composite to a 2D Segment object.
        
                        Returns:
                            Segment: The segment object contained in the composite.
        
                        Raises:
                            RuntimeError: If the composite does not contain a Segment.
        
                        Example:
                            >>> segment = Segment(Point(0.0, 0.0), Point(1.0, 1.0))
                            >>> composite = Composite(segment)
                            >>> extracted_segment = composite.as_segment()
        """
    @typing.overload
    def contains(self, object: ostk.mathematics.geometry.d2.Object) -> bool:
        """
                        Check if the 2D composite contains another geometric object.
        
                        Args:
                            object (Object): The 2D object to check containment for.
        
                        Returns:
                            bool: True if the composite contains the object, False otherwise.
        
                        Example:
                            >>> composite = Composite(Polygon([Point(0.0, 0.0), Point(2.0, 0.0), Point(2.0, 2.0)]))
                            >>> point = Point(1.0, 1.0)
                            >>> composite.contains(point)  # True
        """
    @typing.overload
    def contains(self, composite: Composite) -> bool:
        """
                        Check if the 2D composite contains another composite.
        
                        Args:
                            composite (Composite): The composite to check containment for.
        
                        Returns:
                            bool: True if this composite contains the other composite, False otherwise.
        
                        Example:
                            >>> outer_composite = Composite(Polygon([Point(0.0, 0.0), Point(3.0, 0.0), Point(3.0, 3.0)]))
                            >>> inner_composite = Composite(Polygon([Point(1.0, 1.0), Point(2.0, 1.0), Point(2.0, 2.0)]))
                            >>> outer_composite.contains(inner_composite)  # True
        """
    def get_object_count(self) -> int:
        """
                        Get the number of objects contained in the 2D composite.
        
                        Returns:
                            int: The number of objects in the composite.
        
                        Example:
                            >>> composite = Composite(Point(1.0, 2.0))
                            >>> count = composite.get_object_count()  # 1
        """
    @typing.overload
    def intersects(self, object: ostk.mathematics.geometry.d2.Object) -> bool:
        """
                        Check if the 2D composite intersects with another geometric object.
        
                        Args:
                            object (Object): The 2D object to check intersection with.
        
                        Returns:
                            bool: True if the composite intersects the object, False otherwise.
        
                        Example:
                            >>> composite = Composite(Polygon([Point(0.0, 0.0), Point(1.0, 0.0), Point(1.0, 1.0)]))
                            >>> point = Point(0.5, 0.5)
                            >>> composite.intersects(point)  # True
        """
    @typing.overload
    def intersects(self, composite: Composite) -> bool:
        """
                        Check if the 2D composite intersects with another composite.
        
                        Args:
                            composite (Composite): The composite to check intersection with.
        
                        Returns:
                            bool: True if the composites intersect, False otherwise.
        
                        Example:
                            >>> composite1 = Composite(Polygon([Point(0.0, 0.0), Point(1.0, 0.0), Point(1.0, 1.0)]))
                            >>> composite2 = Composite(Polygon([Point(0.5, 0.5), Point(1.5, 0.5), Point(1.5, 1.5)]))
                            >>> composite1.intersects(composite2)  # True
        """
    def is_composite(self) -> bool:
        """
                        Check if the composite contains another 2D Composite object.
        
                        Returns:
                            bool: True if the composite contains a Composite, False otherwise.
        
                        Example:
                            >>> inner_composite = Composite(Point(1.0, 2.0))
                            >>> outer_composite = Composite(inner_composite)
                            >>> outer_composite.is_composite()  # True
        """
    def is_defined(self) -> bool:
        """
                        Check if the 2D composite is defined.
        
                        Returns:
                            bool: True if the composite is defined, False otherwise.
        
                        Example:
                            >>> composite = Composite(Point(1.0, 2.0))
                            >>> composite.is_defined()  # True
        """
    def is_empty(self) -> bool:
        """
                        Check if the 2D composite is empty (contains no objects).
        
                        Returns:
                            bool: True if the composite is empty, False otherwise.
        
                        Example:
                            >>> empty_composite = Composite.empty()
                            >>> empty_composite.is_empty()  # True
        """
    def is_line(self) -> bool:
        """
                        Check if the composite contains a 2D Line object.
        
                        Returns:
                            bool: True if the composite contains a Line, False otherwise.
        
                        Example:
                            >>> line = Line(Point(0.0, 0.0), np.array([1.0, 1.0]))
                            >>> composite = Composite(line)
                            >>> composite.is_line()  # True
        """
    def is_line_string(self) -> bool:
        """
                        Check if the composite contains a 2D LineString object.
        
                        Returns:
                            bool: True if the composite contains a LineString, False otherwise.
        
                        Example:
                            >>> points = [Point(0.0, 0.0), Point(1.0, 1.0), Point(2.0, 2.0)]
                            >>> line_string = LineString(points)
                            >>> composite = Composite(line_string)
                            >>> composite.is_line_string()  # True
        """
    def is_point(self) -> bool:
        """
                        Check if the composite contains a 2D Point object.
        
                        Returns:
                            bool: True if the composite contains a Point, False otherwise.
        
                        Example:
                            >>> composite = Composite(Point(1.0, 2.0))
                            >>> composite.is_point()  # True
        """
    def is_point_set(self) -> bool:
        """
                        Check if the composite contains a 2D PointSet object.
        
                        Returns:
                            bool: True if the composite contains a PointSet, False otherwise.
        
                        Example:
                            >>> point_set = PointSet([Point(1.0, 2.0), Point(3.0, 4.0)])
                            >>> composite = Composite(point_set)
                            >>> composite.is_point_set()  # True
        """
    def is_polygon(self) -> bool:
        """
                        Check if the composite contains a 2D Polygon object.
        
                        Returns:
                            bool: True if the composite contains a Polygon, False otherwise.
        
                        Example:
                            >>> vertices = [Point(0.0, 0.0), Point(1.0, 0.0), Point(1.0, 1.0)]
                            >>> polygon = Polygon(vertices)
                            >>> composite = Composite(polygon)
                            >>> composite.is_polygon()  # True
        """
    def is_segment(self) -> bool:
        """
                        Check if the composite contains a 2D Segment object.
        
                        Returns:
                            bool: True if the composite contains a Segment, False otherwise.
        
                        Example:
                            >>> segment = Segment(Point(0.0, 0.0), Point(1.0, 1.0))
                            >>> composite = Composite(segment)
                            >>> composite.is_segment()  # True
        """
class Line(ostk.mathematics.geometry.d2.Object):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def points(first_point: Point, second_point: Point) -> Line:
        """
                        Create a line passing through two points.
        
                        Args:
                            first_point (Point): The first point.
                            second_point (Point): The second point.
        
                        Returns:
                            Line: A line passing through both points.
        
                        Example:
                            >>> point1 = Point(0.0, 0.0)
                            >>> point2 = Point(1.0, 1.0)
                            >>> line = Line.points(point1, point2)
        """
    @staticmethod
    def undefined() -> Line:
        """
                        Create an undefined line.
        
                        Returns:
                            Line: An undefined line.
        
                        Example:
                            >>> undefined_line = Line.undefined()
                            >>> undefined_line.is_defined()  # False
        """
    def __eq__(self, arg0: Line) -> bool:
        ...
    def __init__(self, point: Point, direction: numpy.ndarray[numpy.float64[2, 1]]) -> None:
        """
                        Create a 2D line with a point and direction vector.
        
                        Args:
                            point (Point): A point on the line.
                            direction (np.array): The direction vector of the line.
        
                        Example:
                            >>> point = Point(0.0, 0.0)
                            >>> direction = np.array([1.0, 1.0])
                            >>> line = Line(point, direction)
        """
    def __ne__(self, arg0: Line) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __str__(self) -> str:
        ...
    def apply_transformation(self, transformation: typing.Any) -> None:
        """
                        Apply a transformation to the line in place.
        
                        Args:
                            transformation (Transformation): The transformation to apply.
        
                        Example:
                            >>> line = Line.points(Point(0.0, 0.0), Point(1.0, 0.0))
                            >>> transformation = Translation([1.0, 1.0])
                            >>> line.apply_transformation(transformation)
        """
    @typing.overload
    def contains(self, point: Point) -> bool:
        """
                        Check if the line contains a point.
        
                        Args:
                            point (Point): The point to check.
        
                        Returns:
                            bool: True if the line contains the point, False otherwise.
        
                        Example:
                            >>> line = Line.points(Point(0.0, 0.0), Point(1.0, 1.0))
                            >>> line.contains(Point(0.5, 0.5))  # True
        """
    @typing.overload
    def contains(self, point_set: PointSet) -> bool:
        """
                        Check if the line contains all points in a point set.
        
                        Args:
                            point_set (PointSet): The set of points to check.
        
                        Returns:
                            bool: True if the line contains all points in the set, False otherwise.
        
                        Example:
                            >>> line = Line.points(Point(0.0, 0.0), Point(1.0, 1.0))
                            >>> points = PointSet([Point(0.5, 0.5), Point(0.25, 0.25)])
                            >>> line.contains(points)
        """
    def distance_to(self, point: Point) -> ostk.core.type.Real:
        """
                        Calculate the distance from the line to a point.
        
                        Args:
                            point (Point): The point to calculate distance to.
        
                        Returns:
                            float: The distance from the line to the point.
        
                        Example:
                            >>> line = Line.points(Point(0.0, 0.0), Point(1.0, 0.0))
                            >>> distance = line.distance_to(Point(0.5, 1.0))  # 1.0
        """
    def get_direction(self) -> numpy.ndarray[numpy.float64[2, 1]]:
        """
                        Get the direction vector of the line.
        
                        Returns:
                            Vector2d: The direction vector of the line.
        
                        Example:
                            >>> line = Line.points(Point(0.0, 0.0), Point(1.0, 1.0))
                            >>> direction = line.get_direction()
        """
    def get_origin(self) -> Point:
        """
                        Get the origin point of the line.
        
                        Returns:
                            Point: The origin point of the line.
        
                        Example:
                            >>> line = Line.points(Point(1.0, 2.0), Point(3.0, 4.0))
                            >>> origin = line.get_origin()
        """
    def intersects(self, point: Point) -> bool:
        """
                        Check if the line intersects with a point.
        
                        Args:
                            point (Point): The point to check intersection with.
        
                        Returns:
                            bool: True if the line intersects with the point, False otherwise.
        
                        Example:
                            >>> line = Line.points(Point(0.0, 0.0), Point(1.0, 1.0))
                            >>> line.intersects(Point(0.5, 0.5))  # True
        """
    def is_defined(self) -> bool:
        """
                        Check if the line is defined.
        
                        Returns:
                            bool: True if the line is defined, False otherwise.
        
                        Example:
                            >>> line = Line.points(Point(0.0, 0.0), Point(1.0, 1.0))
                            >>> line.is_defined()  # True
        """
class LineString(ostk.mathematics.geometry.d2.Object):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def empty() -> LineString:
        """
                        Create an empty line string.
        
                        Returns:
                            LineString: An empty line string.
        
                        Example:
                            >>> empty_line = LineString.empty()
                            >>> empty_line.is_empty()  # True
        """
    def __eq__(self, arg0: LineString) -> bool:
        ...
    def __getitem__(self, index: int) -> Point:
        """
                        Access a point by index (Python indexing support).
        
                        Args:
                            index (int): The index of the point to access.
        
                        Returns:
                            Point: The point at the specified index.
        
                        Raises:
                            IndexError: If the index is out of range.
        
                        Example:
                            >>> points = [Point(0.0, 0.0), Point(1.0, 1.0)]
                            >>> line_string = LineString(points)
                            >>> first_point = line_string[0]  # Point(0.0, 0.0)
        """
    def __init__(self, points: list[Point]) -> None:
        """
                        Create a 2D line string from a sequence of points.
        
                        Args:
                            points (list): A list of Point objects defining the line string.
        
                        Example:
                            >>> points = [Point(0.0, 0.0), Point(1.0, 1.0), Point(2.0, 0.0)]
                            >>> line_string = LineString(points)
        """
    def __iter__(self) -> typing.Iterator[Point]:
        """
                        Make the line string iterable (Python for loop support).
        
                        Returns:
                            iterator: An iterator over the points in the line string.
        
                        Example:
                            >>> points = [Point(0.0, 0.0), Point(1.0, 1.0)]
                            >>> line_string = LineString(points)
                            >>> for point in line_string:
                            ...     print(point)
        """
    def __len__(self) -> int:
        """
                        Get the number of points in the line string (Python len() function).
        
                        Returns:
                            int: The number of points.
        
                        Example:
                            >>> points = [Point(0.0, 0.0), Point(1.0, 1.0)]
                            >>> line_string = LineString(points)
                            >>> len(line_string)  # 2
        """
    def __ne__(self, arg0: LineString) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __str__(self) -> str:
        ...
    def apply_transformation(self, transformation: typing.Any) -> None:
        """
                        Apply a transformation to the line string in place.
        
                        Args:
                            transformation (Transformation): The transformation to apply.
        
                        Example:
                            >>> line_string = LineString(points)
                            >>> transformation = Transformation.translation([1.0, 0.0])
                            >>> line_string.apply_transformation(transformation)
        """
    def get_point_closest_to(self, point: Point) -> Point:
        """
                        Get the point on the line string closest to a given point.
        
                        Args:
                            point (Point): The reference point.
        
                        Returns:
                            Point: The closest point on the line string.
        
                        Example:
                            >>> points = [Point(0.0, 0.0), Point(1.0, 1.0), Point(2.0, 0.0)]
                            >>> line_string = LineString(points)
                            >>> closest = line_string.get_point_closest_to(Point(0.5, 0.5))
        """
    def get_point_count(self) -> int:
        """
                        Get the number of points in the line string.
        
                        Returns:
                            int: The number of points.
        
                        Example:
                            >>> points = [Point(0.0, 0.0), Point(1.0, 1.0), Point(2.0, 0.0)]
                            >>> line_string = LineString(points)
                            >>> line_string.get_point_count()  # 3
        """
    def is_defined(self) -> bool:
        """
                        Check if the line string is defined.
        
                        Returns:
                            bool: True if the line string is defined, False otherwise.
        
                        Example:
                            >>> points = [Point(0.0, 0.0), Point(1.0, 1.0)]
                            >>> line_string = LineString(points)
                            >>> line_string.is_defined()  # True
        """
    def is_empty(self) -> bool:
        """
                        Check if the line string is empty (has no points).
        
                        Returns:
                            bool: True if the line string is empty, False otherwise.
        
                        Example:
                            >>> empty_line = LineString.empty()
                            >>> empty_line.is_empty()  # True
        """
    def is_near(self, line_string: LineString, tolerance: ostk.core.type.Real) -> bool:
        """
                        Check if the line string is near another line string.
        
                        Args:
                            line_string (LineString): The line string to check.
                            tolerance (float): The tolerance.
        
                        Returns:
                            bool: True if the line string is near another line string, False otherwise.
        
                        Example:
                            >>> line_string = LineString(points)
                            >>> line_string.is_near(LineString(points), 0.1)  # True
        """
    def to_string(self, format: ostk.mathematics.geometry.d2.Object.Format = ..., precision: ostk.core.type.Integer = ...) -> ostk.core.type.String:
        """
                        Convert the line string to a string representation.
        
                        Args:
                            format (Object.Format, optional): The output format. Defaults to Standard.
                            precision (int, optional): The precision for floating point numbers. Defaults to undefined.
        
                        Returns:
                            str: String representation of the line string.
        
                        Example:
                            >>> points = [Point(0.0, 0.0), Point(1.0, 1.0)]
                            >>> line_string = LineString(points)
                            >>> line_string.to_string()
        """
class MultiPolygon(ostk.mathematics.geometry.d2.Object):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def polygon(polygon: Polygon) -> MultiPolygon:
        """
                        Create a multi-polygon from a single polygon.
        
                        Args:
                            polygon (Polygon): The polygon to wrap in a multi-polygon.
        
                        Returns:
                            MultiPolygon: A multi-polygon containing the single polygon.
        
                        Example:
                            >>> polygon = Polygon([Point(0.0, 0.0), Point(1.0, 0.0), Point(1.0, 1.0)])
                            >>> multi_polygon = MultiPolygon.polygon(polygon)
                            >>> multi_polygon.get_polygon_count()  # 1
        """
    @staticmethod
    def undefined() -> MultiPolygon:
        """
                        Create an undefined multi-polygon.
        
                        Returns:
                            MultiPolygon: An undefined multi-polygon object.
        
                        Example:
                            >>> undefined_multi_polygon = MultiPolygon.undefined()
                            >>> undefined_multi_polygon.is_defined()  # False
        """
    def __eq__(self, arg0: MultiPolygon) -> bool:
        ...
    def __init__(self, polygons: list[Polygon]) -> None:
        """
                        Create a multi-polygon from an array of polygons.
        
                        Args:
                            polygons (list): List of Polygon objects to combine into a multi-polygon.
        
                        Example:
                            >>> polygon1 = Polygon([Point(0.0, 0.0), Point(1.0, 0.0), Point(1.0, 1.0)])
                            >>> polygon2 = Polygon([Point(2.0, 2.0), Point(3.0, 2.0), Point(3.0, 3.0)])
                            >>> multi_polygon = MultiPolygon([polygon1, polygon2])
        """
    def __ne__(self, arg0: MultiPolygon) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __str__(self) -> str:
        ...
    def apply_transformation(self, transformation: typing.Any) -> None:
        """
                        Apply a transformation to all polygons in the multi-polygon in place.
        
                        Args:
                            transformation (Transformation): The 2D transformation to apply.
        
                        Example:
                            >>> polygon = Polygon([Point(0.0, 0.0), Point(1.0, 0.0), Point(1.0, 1.0)])
                            >>> multi_polygon = MultiPolygon([polygon])
                            >>> transformation = Translation([1.0, 1.0])
                            >>> multi_polygon.apply_transformation(transformation)
        """
    @typing.overload
    def contains(self, point: Point) -> bool:
        """
                        Check if the multi-polygon contains a point.
        
                        Args:
                            point (Point): The point to check for containment.
        
                        Returns:
                            bool: True if any polygon in the multi-polygon contains the point, False otherwise.
        
                        Example:
                            >>> polygon = Polygon([Point(0.0, 0.0), Point(2.0, 0.0), Point(2.0, 2.0)])
                            >>> multi_polygon = MultiPolygon([polygon])
                            >>> multi_polygon.contains(Point(1.0, 1.0))  # True
                            >>> multi_polygon.contains(Point(3.0, 3.0))  # False
        """
    @typing.overload
    def contains(self, point_set: PointSet) -> bool:
        """
                        Check if the multi-polygon contains all points in a point set.
        
                        Args:
                            point_set (PointSet): The point set to check for containment.
        
                        Returns:
                            bool: True if the multi-polygon contains all points in the set, False otherwise.
        
                        Example:
                            >>> polygon = Polygon([Point(0.0, 0.0), Point(3.0, 0.0), Point(3.0, 3.0)])
                            >>> multi_polygon = MultiPolygon([polygon])
                            >>> points = PointSet([Point(1.0, 1.0), Point(2.0, 2.0)])
                            >>> multi_polygon.contains(points)  # True
        """
    def get_convex_hull(self) -> Polygon:
        """
                        Compute the convex hull of all polygons in the multi-polygon.
        
                        Returns:
                            Polygon: A polygon representing the convex hull of all vertices.
        
                        Example:
                            >>> polygon1 = Polygon([Point(0.0, 0.0), Point(1.0, 0.0), Point(1.0, 1.0)])
                            >>> polygon2 = Polygon([Point(2.0, 2.0), Point(3.0, 2.0), Point(3.0, 3.0)])
                            >>> multi_polygon = MultiPolygon([polygon1, polygon2])
                            >>> convex_hull = multi_polygon.get_convex_hull()
        """
    def get_polygon_count(self) -> int:
        """
                        Get the number of polygons in the multi-polygon.
        
                        Returns:
                            int: The number of polygons contained in the multi-polygon.
        
                        Example:
                            >>> polygon1 = Polygon([Point(0.0, 0.0), Point(1.0, 0.0), Point(1.0, 1.0)])
                            >>> polygon2 = Polygon([Point(2.0, 2.0), Point(3.0, 2.0), Point(3.0, 3.0)])
                            >>> multi_polygon = MultiPolygon([polygon1, polygon2])
                            >>> multi_polygon.get_polygon_count()  # 2
        """
    def get_polygons(self) -> list[Polygon]:
        """
                        Get all polygons contained in the multi-polygon.
        
                        Returns:
                            list: List of Polygon objects contained in the multi-polygon.
        
                        Example:
                            >>> polygon1 = Polygon([Point(0.0, 0.0), Point(1.0, 0.0), Point(1.0, 1.0)])
                            >>> polygon2 = Polygon([Point(2.0, 2.0), Point(3.0, 2.0), Point(3.0, 3.0)])
                            >>> multi_polygon = MultiPolygon([polygon1, polygon2])
                            >>> polygons = multi_polygon.get_polygons()
                            >>> len(polygons)  # 2
        """
    def is_defined(self) -> bool:
        """
                        Check if the multi-polygon is defined.
        
                        Returns:
                            bool: True if the multi-polygon is defined, False otherwise.
        
                        Example:
                            >>> polygon = Polygon([Point(0.0, 0.0), Point(1.0, 0.0), Point(1.0, 1.0)])
                            >>> multi_polygon = MultiPolygon([polygon])
                            >>> multi_polygon.is_defined()  # True
        """
    def to_string(self, format: ostk.mathematics.geometry.d2.Object.Format = ..., precision: ostk.core.type.Integer = ...) -> ostk.core.type.String:
        """
                        Convert the multi-polygon to a string representation.
        
                        Args:
                            format (Object.Format, optional): The output format. Defaults to Standard.
                            precision (int, optional): The precision for floating point numbers. Defaults to undefined.
        
                        Returns:
                            str: String representation of the multi-polygon.
        
                        Example:
                            >>> polygon = Polygon([Point(0.0, 0.0), Point(1.0, 0.0), Point(1.0, 1.0)])
                            >>> multi_polygon = MultiPolygon([polygon])
                            >>> multi_polygon.to_string()
        """
    def union_with(self, multipolygon: MultiPolygon) -> MultiPolygon:
        """
                        Compute the union of this multi-polygon with another multi-polygon.
        
                        Args:
                            multipolygon (MultiPolygon): The multi-polygon to union with.
        
                        Returns:
                            MultiPolygon: A new multi-polygon representing the union.
        
                        Example:
                            >>> polygon1 = Polygon([Point(0.0, 0.0), Point(1.0, 0.0), Point(1.0, 1.0)])
                            >>> polygon2 = Polygon([Point(0.5, 0.5), Point(1.5, 0.5), Point(1.5, 1.5)])
                            >>> multi1 = MultiPolygon([polygon1])
                            >>> multi2 = MultiPolygon([polygon2])
                            >>> union_result = multi1.union_with(multi2)
        """
class Point(ostk.mathematics.geometry.d2.Object):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def origin() -> Point:
        """
                        Create a point at the origin (0, 0).
        
                        Returns:
                            Point: A point at coordinates (0, 0).
        
                        Example:
                            >>> origin = Point.origin()
                            >>> origin.x()  # 0.0
                            >>> origin.y()  # 0.0
        """
    @staticmethod
    def undefined() -> Point:
        """
                        Create an undefined point.
        
                        Returns:
                            Point: An undefined point.
        
                        Example:
                            >>> undefined_point = Point.undefined()
                            >>> undefined_point.is_defined()  # False
        """
    @staticmethod
    def vector(vector: numpy.ndarray[numpy.float64[2, 1]]) -> Point:
        """
                        Create a point from a 2D vector.
        
                        Args:
                            vector (np.array): The vector to convert to a point.
        
                        Returns:
                            Point: A point with coordinates from the vector.
        
                        Example:
                            >>> vector = np.array([1.0, 2.0])
                            >>> point = Point.vector(vector)  # Point(1.0, 2.0)
        """
    def __add__(self, arg0: numpy.ndarray[numpy.float64[2, 1]]) -> Point:
        ...
    def __eq__(self, arg0: Point) -> bool:
        ...
    def __init__(self, x: ostk.core.type.Real, y: ostk.core.type.Real) -> None:
        """
                        Create a 2D point with specified coordinates.
        
                        Args:
                            x (float): The x-coordinate.
                            y (float): The y-coordinate.
        
                        Example:
                            >>> point = Point(1.0, 2.0)
                            >>> point.x()  # 1.0
                            >>> point.y()  # 2.0
        """
    def __ne__(self, arg0: Point) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __str__(self) -> str:
        ...
    @typing.overload
    def __sub__(self, arg0: Point) -> numpy.ndarray[numpy.float64[2, 1]]:
        ...
    @typing.overload
    def __sub__(self, arg0: numpy.ndarray[numpy.float64[2, 1]]) -> Point:
        ...
    def apply_transformation(self, transformation: typing.Any) -> None:
        """
                        Apply a transformation to the point in place.
        
                        Args:
                            transformation (Transformation): The transformation to apply.
        
                        Example:
                            >>> point = Point(1.0, 2.0)
                            >>> transformation = Translation([1.0, 1.0])
                            >>> point.apply_transformation(transformation)
        """
    def as_vector(self) -> numpy.ndarray[numpy.float64[2, 1]]:
        """
                        Convert the point to a 2D vector.
        
                        Returns:
                            Vector2d: The point as a 2D vector.
        
                        Example:
                            >>> point = Point(1.0, 2.0)
                            >>> vector = point.as_vector()  # np.array([1.0, 2.0])
        """
    def distance_to(self, point: Point) -> ostk.core.type.Real:
        """
                        Calculate the distance to another point.
        
                        Args:
                            point (Point): The other point.
        
                        Returns:
                            float: The distance between the points.
        
                        Example:
                            >>> point1 = Point(0.0, 0.0)
                            >>> point2 = Point(3.0, 4.0)
                            >>> point1.distance_to(point2)  # 5.0
        """
    def is_defined(self) -> bool:
        """
                        Check if the point is defined.
        
                        Returns:
                            bool: True if the point is defined, False otherwise.
        
                        Example:
                            >>> point = Point(1.0, 2.0)
                            >>> point.is_defined()  # True
        """
    def is_near(self, point: Point, tolerance: ostk.core.type.Real) -> bool:
        """
                        Check if this point is near another point within a tolerance.
        
                        Args:
                            point (Point): The point to compare with.
                            tolerance (float): The tolerance for comparison.
        
                        Returns:
                            bool: True if points are within tolerance, False otherwise.
        
                        Example:
                            >>> point1 = Point(1.0, 2.0)
                            >>> point2 = Point(1.1, 2.1)
                            >>> point1.is_near(point2, 0.2)  # True
        """
    def to_string(self, format: ostk.mathematics.geometry.d2.Object.Format = ..., precision: ostk.core.type.Integer = ...) -> ostk.core.type.String:
        """
                        Convert the point to a string representation.
        
                        Args:
                            format (Object.Format, optional): The output format. Defaults to Standard.
                            precision (int, optional): The precision for floating point numbers. Defaults to undefined.
        
                        Returns:
                            str: String representation of the point.
        
                        Example:
                            >>> point = Point(1.0, 2.0)
                            >>> point.to_string()  # "(1.0, 2.0)"
        """
    def x(self) -> ostk.core.type.Real:
        """
                        Get the x-coordinate of the point.
        
                        Returns:
                            float: The x-coordinate.
        
                        Example:
                            >>> point = Point(1.0, 2.0)
                            >>> point.x()  # 1.0
        """
    def y(self) -> ostk.core.type.Real:
        """
                        Get the y-coordinate of the point.
        
                        Returns:
                            float: The y-coordinate.
        
                        Example:
                            >>> point = Point(1.0, 2.0)
                            >>> point.y()  # 2.0
        """
class PointSet(ostk.mathematics.geometry.d2.Object):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def empty() -> PointSet:
        """
                        Create an empty point set.
        
                        Returns:
                            PointSet: An empty point set containing no points.
        
                        Example:
                            >>> empty_set = PointSet.empty()
                            >>> empty_set.is_empty()  # True
                            >>> empty_set.get_size()  # 0
        """
    def __eq__(self, arg0: PointSet) -> bool:
        ...
    def __getitem__(self, arg0: int) -> Point:
        """
                        Access a point by index (Python indexing support).
        
                        Args:
                            index (int): The index of the point to access.
        
                        Returns:
                            Point: The point at the specified index.
        
                        Raises:
                            IndexError: If the index is out of range.
        
                        Example:
                            >>> points = [Point(0.0, 0.0), Point(1.0, 1.0)]
                            >>> point_set = PointSet(points)
                            >>> first_point = point_set[0]  # Point(0.0, 0.0)
        """
    def __init__(self, points: list[Point]) -> None:
        """
                        Create a 2D point set from an array of points.
        
                        Args:
                            points (list[Point]): List of Point objects to include in the set.
        
                        Example:
                            >>> points = [Point(0.0, 0.0), Point(1.0, 1.0), Point(2.0, 2.0)]
                            >>> point_set = PointSet(points)
        """
    def __iter__(self) -> typing.Iterator[Point]:
        """
                        Make the point set iterable (Python for loop support).
        
                        Returns:
                            iterator: An iterator over the points in the set.
        
                        Example:
                            >>> points = [Point(0.0, 0.0), Point(1.0, 1.0)]
                            >>> point_set = PointSet(points)
                            >>> for point in point_set:
                            ...     print(point)
        """
    def __len__(self) -> int:
        """
                        Get the number of points in the set (Python len() function).
        
                        Returns:
                            int: The number of points in the set.
        
                        Example:
                            >>> points = [Point(0.0, 0.0), Point(1.0, 1.0)]
                            >>> point_set = PointSet(points)
                            >>> len(point_set)  # 2
        """
    def __ne__(self, arg0: PointSet) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __str__(self) -> str:
        ...
    def apply_transformation(self, transformation: typing.Any) -> None:
        """
                        Apply a transformation to all points in the set.
        
                        Args:
                            transformation (Transformation): The 2D transformation to apply.
        
                        Example:
                            >>> points = [Point(0.0, 0.0), Point(1.0, 1.0)]
                            >>> point_set = PointSet(points)
                            >>> transformation = Translation([1.0, 1.0])
                            >>> point_set.apply_transformation(transformation)
        """
    def distance_to(self, point: Point) -> ostk.core.type.Real:
        """
                        Calculate the distance from the point set to a point.
        
                        Args:
                            point (Point): The point to calculate distance to.
        
                        Returns:
                            float: The minimum distance from any point in the set to the given point.
        
                        Example:
                            >>> points = [Point(0.0, 0.0), Point(2.0, 0.0)]
                            >>> point_set = PointSet(points)
                            >>> distance = point_set.distance_to(Point(1.0, 0.0))  # 1.0
        """
    def get_point_closest_to(self, point: Point) -> Point:
        """
                        Get the point in the set that is closest to a given point.
        
                        Args:
                            point (Point): The reference point.
        
                        Returns:
                            Point: The closest point in the set to the given point.
        
                        Example:
                            >>> points = [Point(0.0, 0.0), Point(2.0, 0.0), Point(4.0, 0.0)]
                            >>> point_set = PointSet(points)
                            >>> closest = point_set.get_point_closest_to(Point(1.5, 0.0))  # Point(2.0, 0.0)
        """
    def get_size(self) -> int:
        """
                        Get the number of points in the set.
        
                        Returns:
                            int: The number of points in the set.
        
                        Example:
                            >>> points = [Point(0.0, 0.0), Point(1.0, 1.0), Point(2.0, 2.0)]
                            >>> point_set = PointSet(points)
                            >>> point_set.get_size()  # 3
        """
    def is_defined(self) -> bool:
        """
                        Check if the point set is defined.
        
                        Returns:
                            bool: True if the point set is defined, False otherwise.
        
                        Example:
                            >>> points = [Point(0.0, 0.0), Point(1.0, 1.0)]
                            >>> point_set = PointSet(points)
                            >>> point_set.is_defined()  # True
        """
    def is_empty(self) -> bool:
        """
                        Check if the point set is empty (contains no points).
        
                        Returns:
                            bool: True if the point set is empty, False otherwise.
        
                        Example:
                            >>> empty_set = PointSet.empty()
                            >>> empty_set.is_empty()  # True
                            >>> points = [Point(0.0, 0.0)]
                            >>> point_set = PointSet(points)
                            >>> point_set.is_empty()  # False
        """
    def is_near(self, point_set: PointSet, tolerance: ostk.core.type.Real) -> bool:
        """
                        Check if this point set is near another point set within tolerance.
        
                        Args:
                            point_set (PointSet): The point set to compare with.
                            tolerance (float): The tolerance for comparison.
        
                        Returns:
                            bool: True if point sets are within tolerance, False otherwise.
        
                        Example:
                            >>> points1 = [Point(0.0, 0.0), Point(1.0, 1.0)]
                            >>> points2 = [Point(0.1, 0.1), Point(1.1, 1.1)]
                            >>> set1 = PointSet(points1)
                            >>> set2 = PointSet(points2)
                            >>> set1.is_near(set2, 0.2)  # True
        """
    def to_string(self, format: ostk.mathematics.geometry.d2.Object.Format = ..., precision: ostk.core.type.Integer = ...) -> ostk.core.type.String:
        """
                        Convert the point set to a string representation.
        
                        Args:
                            format (Object.Format, optional): The output format. Defaults to Standard.
                            precision (int, optional): The precision for floating point numbers. Defaults to undefined.
        
                        Returns:
                            str: String representation of the point set.
        
                        Example:
                            >>> points = [Point(0.0, 0.0), Point(1.0, 1.0)]
                            >>> point_set = PointSet(points)
                            >>> point_set.to_string()
        """
class Polygon(ostk.mathematics.geometry.d2.Object):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def undefined() -> Polygon:
        """
                        Create an undefined polygon.
        
                        Returns:
                            Polygon: An undefined polygon.
        
                        Example:
                            >>> undefined_polygon = Polygon.undefined()
                            >>> undefined_polygon.is_defined()  # False
        """
    def __eq__(self, arg0: Polygon) -> bool:
        ...
    @typing.overload
    def __init__(self, outer_ring: list[Point], inner_rings: list[list[Point]]) -> None:
        """
                        Create a polygon with outer ring and inner rings (holes).
        
                        Args:
                            outer_ring (list[Point]): List of points defining the outer boundary.
                            inner_rings (list[list[Point]]): List of lists of points defining holes.
        
                        Example:
                            >>> outer = [Point(0.0, 0.0), Point(1.0, 0.0), Point(1.0, 1.0), Point(0.0, 1.0)]
                            >>> inner = [[Point(0.2, 0.2), Point(0.8, 0.2), Point(0.8, 0.8), Point(0.2, 0.8)]]
                            >>> polygon = Polygon(outer, inner)
        """
    @typing.overload
    def __init__(self, outer_ring: list[Point]) -> None:
        """
                        Create a simple polygon with just an outer ring.
        
                        Args:
                            outer_ring (list[Point]): List of points defining the polygon boundary.
        
                        Example:
                            >>> points = [Point(0.0, 0.0), Point(1.0, 0.0), Point(1.0, 1.0), Point(0.0, 1.0)]
                            >>> polygon = Polygon(points)
        """
    def __ne__(self, arg0: Polygon) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __str__(self) -> str:
        ...
    def apply_transformation(self, transformation: typing.Any) -> None:
        """
                        Apply a transformation to the polygon in place.
        
                        Args:
                            transformation (Transformation): The transformation to apply.
        
                        Example:
                            >>> polygon = Polygon([Point(0.0, 0.0), Point(1.0, 0.0), Point(1.0, 1.0), Point(0.0, 1.0)])
                            >>> transformation = Translation([1.0, 1.0])
                            >>> polygon.apply_transformation(transformation)
        """
    @typing.overload
    def contains(self, point: Point) -> bool:
        """
                        Check if the polygon contains a point.
        
                        Args:
                            point (Point): The point to check.
        
                        Returns:
                            bool: True if the polygon contains the point, False otherwise.
        
                        Example:
                            >>> polygon = Polygon([Point(0.0, 0.0), Point(1.0, 0.0), Point(1.0, 1.0), Point(0.0, 1.0)])
                            >>> polygon.contains(Point(0.5, 0.5))  # True
        """
    @typing.overload
    def contains(self, point_set: PointSet) -> bool:
        """
                        Check if the polygon contains a point set.
        
                        Args:
                            point_set (PointSet): The point set to check.
        
                        Returns:
                            bool: True if the polygon contains the point set, False otherwise.
        
                        Example:
                            >>> polygon = Polygon([Point(0.0, 0.0), Point(1.0, 0.0), Point(1.0, 1.0), Point(0.0, 1.0)])
                            >>> point_set = PointSet([Point(0.5, 0.5), Point(1.5, 0.5), Point(1.5, 1.5)])
                            >>> polygon.contains(point_set)  # True
        """
    def difference_with(self, polygon: Polygon) -> ...:
        """
                        Get the difference of the polygon with another polygon.
        
                        Args:
                            polygon (Polygon): The polygon to check difference with.
        
                        Returns:
                            Intersection: The difference of the polygon with another polygon.
        
                        Example:
                            >>> polygon1 = Polygon([Point(0.0, 0.0), Point(1.0, 0.0), Point(1.0, 1.0)])
                            >>> polygon2 = Polygon([Point(0.01, 0.01), Point(1.01, 0.01), Point(1.01, 1.01)])
                            >>> polygon1.difference_with(polygon2)  # Intersection
        """
    def get_convex_hull(self) -> Polygon:
        """
                        Get the convex hull of the polygon.
        
                        Returns:
                            Polygon: The convex hull of the polygon.
        
                        Example:
                            >>> polygon = Polygon([Point(0.0, 0.0), Point(1.0, 0.0), Point(1.0, 1.0), Point(0.0, 1.0)])
                            >>> polygon.get_convex_hull()
        """
    def get_edge_at(self, index: int) -> Segment:
        """
                        Get the edge at the given index.
        
                        Args:
                            index (int): The index of the edge.
        
                        Returns:
                            Polygon.Edge: The edge at the given index.
        
                        Example:
                            >>> polygon = Polygon([Point(0.0, 0.0), Point(1.0, 0.0), Point(1.0, 1.0), Point(0.0, 1.0)])
                            >>> polygon.get_edge_at(0)
        """
    def get_edge_count(self) -> int:
        """
                        Get the number of edges in the polygon.
        
                        Returns:
                            int: The number of edges.
        
                        Example:
                            >>> polygon = Polygon([Point(0.0, 0.0), Point(1.0, 0.0), Point(1.0, 1.0), Point(0.0, 1.0)])
                            >>> polygon.get_edge_count()  # 4
        """
    def get_edges(self) -> list[Segment]:
        """
                        Get all edges of the polygon.
        
                        Returns:
                            list: List of all edges in the polygon.
        
                        Example:
                            >>> polygon = Polygon([Point(0.0, 0.0), Point(1.0, 0.0), Point(1.0, 1.0), Point(0.0, 1.0)])
                            >>> polygon.get_edges()
        """
    def get_inner_ring_at(self, arg0: int) -> LineString:
        """
                        Get the inner ring at the given index.
        
                        Args:
                            index (int): The index of the inner ring.
        
                        Returns:
                            Polygon.Ring: The inner ring at the given index.
        
                        Example:
                            >>> polygon = Polygon([Point(0.0, 0.0), Point(1.0, 0.0), Point(1.0, 1.0), Point(0.0, 1.0)])
                            >>> polygon.get_inner_ring_at(0)
        """
    def get_inner_ring_count(self) -> int:
        """
                        Get the number of inner rings in the polygon.
        
                        Returns:
                            int: The number of inner rings.
        
                        Example:
                            >>> polygon = Polygon([Point(0.0, 0.0), Point(1.0, 0.0), Point(1.0, 1.0), Point(0.0, 1.0)])
                            >>> polygon.get_inner_ring_count()  # 0
        """
    def get_outer_ring(self) -> LineString:
        """
                        Get the outer ring of the polygon.
        
                        Returns:
                            Polygon.Ring: The outer ring of the polygon.
        
                        Example:
                            >>> polygon = Polygon([Point(0.0, 0.0), Point(1.0, 0.0), Point(1.0, 1.0), Point(0.0, 1.0)])
                            >>> polygon.get_outer_ring()
        """
    def get_vertex_at(self, index: int) -> Point:
        """
                        Get the vertex at the given index.
        
                        Args:
                            index (int): The index of the vertex.
        
                        Returns:
                            Polygon.Vertex: The vertex at the given index.
        
                        Example:
                            >>> polygon = Polygon([Point(0.0, 0.0), Point(1.0, 0.0), Point(1.0, 1.0), Point(0.0, 1.0)])
                            >>> polygon.get_vertex_at(0)
        """
    def get_vertex_count(self) -> int:
        """
                        Get the total number of vertices in the polygon.
        
                        Returns:
                            int: The number of vertices.
        
                        Example:
                            >>> polygon = Polygon([Point(0.0, 0.0), Point(1.0, 0.0), Point(1.0, 1.0), Point(0.0, 1.0)])
                            >>> polygon.get_vertex_count()  # 4
        """
    def get_vertices(self) -> list[Point]:
        """
                        Get all vertices of the polygon.
        
                        Returns:
                            list: List of all vertices in the polygon.
        
                        Example:
                            >>> polygon = Polygon([Point(0.0, 0.0), Point(1.0, 0.0), Point(1.0, 1.0)])
                            >>> vertices = polygon.get_vertices()
        """
    def intersection_with(self, polygon: Polygon) -> ...:
        """
                        Get the intersection of the polygon with another polygon.
        
                        Args:
                            polygon (Polygon): The polygon to check intersection with.
        
                        Returns:
                            Intersection: The intersection of the polygon with another polygon.
        
                        Example:
                            >>> polygon1 = Polygon([Point(0.0, 0.0), Point(1.0, 0.0), Point(1.0, 1.0)])
                            >>> polygon2 = Polygon([Point(0.01, 0.01), Point(1.01, 0.01), Point(1.01, 1.01)])
                            >>> polygon1.intersection_with(polygon2)  # Intersection
        """
    def intersects(self, polygon: Polygon) -> bool:
        """
                        Check if the polygon intersects another polygon.
        
                        Args:
                            polygon (Polygon): The polygon to check intersection with.
        
                        Returns:
                            bool: True if the polygons intersect, False otherwise.
        
                        Example:
                            >>> polygon1 = Polygon([Point(0.0, 0.0), Point(1.0, 0.0), Point(1.0, 1.0)])
                            >>> polygon2 = Polygon([Point(0.01, 0.01), Point(1.01, 0.01), Point(1.01, 1.01)])
                            >>> polygon1.intersects(polygon2)  # True
        """
    def is_defined(self) -> bool:
        """
                        Check if the polygon is defined.
        
                        Returns:
                            bool: True if the polygon is defined, False otherwise.
        
                        Example:
                            >>> polygon = Polygon([Point(0.0, 0.0), Point(1.0, 0.0), Point(1.0, 1.0)])
                            >>> polygon.is_defined()  # True
        """
    def is_near(self, polygon: Polygon, tolerance: ostk.core.type.Real) -> bool:
        """
                        Check if this polygon is near another polygon within tolerance.
        
                        Args:
                            polygon (Polygon): The polygon to compare with.
                            tolerance (float): The tolerance for comparison.
        
                        Returns:
                            bool: True if polygons are within tolerance, False otherwise.
        
                        Example:
                            >>> polygon1 = Polygon([Point(0.0, 0.0), Point(1.0, 0.0), Point(1.0, 1.0)])
                            >>> polygon2 = Polygon([Point(0.01, 0.01), Point(1.01, 0.01), Point(1.01, 1.01)])
                            >>> polygon1.is_near(polygon2, 0.1)  # True
        """
    def to_string(self, format: ostk.mathematics.geometry.d2.Object.Format = ..., precision: ostk.core.type.Integer = ...) -> ostk.core.type.String:
        """
                        Get the string representation of the polygon.
        
                        Args:
                            format (Object.Format, optional): The output format. Defaults to Standard.
                            precision (int, optional): The precision for floating point numbers. Defaults to undefined.
        
                        Returns:
                            str: String representation of the polygon.
        
                        Example:
                            >>> polygon = Polygon([Point(0.0, 0.0), Point(1.0, 0.0), Point(1.0, 1.0), Point(0.0, 1.0)])
                            >>> polygon.to_string()
        """
    def union_with(self, polygon: Polygon) -> ...:
        """
                        Get the union of the polygon with another polygon.
        
                        Args:
                            polygon (Polygon): The polygon to union with.
        
                        Returns:
                            Polygon: The union of the polygon with another polygon.
        
                        Example:
                            >>> polygon1 = Polygon([Point(0.0, 0.0), Point(1.0, 0.0), Point(1.0, 1.0), Point(0.0, 1.0)])
                            >>> polygon2 = Polygon([Point(0.01, 0.01), Point(1.01, 0.01), Point(1.01, 1.01), Point(0.01, 1.01)])
                            >>> polygon1.union_with(polygon2)
        """
class Segment(ostk.mathematics.geometry.d2.Object):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def undefined() -> Segment:
        """
                        Create an undefined segment.
        
                        Returns:
                            Segment: An undefined segment object.
        
                        Example:
                            >>> undefined_segment = Segment.undefined()
                            >>> undefined_segment.is_defined()  # False
        """
    def __eq__(self, arg0: Segment) -> bool:
        ...
    def __init__(self, start_point: Point, end_point: Point) -> None:
        """
                        Create a 2D segment defined by two endpoints.
        
                        Args:
                            start_point (Point): The starting point of the segment.
                            end_point (Point): The ending point of the segment.
        
                        Example:
                            >>> start = Point(0.0, 0.0)
                            >>> end = Point(1.0, 1.0)
                            >>> segment = Segment(start, end)
        """
    def __ne__(self, arg0: Segment) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __str__(self) -> str:
        ...
    def apply_transformation(self, transformation: typing.Any) -> None:
        """
                        Apply a transformation to the segment in place.
        
                        Args:
                            transformation (Transformation): The 2D transformation to apply.
        
                        Example:
                            >>> segment = Segment(Point(0.0, 0.0), Point(1.0, 1.0))
                            >>> transformation = Translation([1.0, 1.0])
                            >>> segment.apply_transformation(transformation)
        """
    @typing.overload
    def distance_to(self, point: Point) -> ostk.core.type.Real:
        """
                        Calculate the distance from the segment to a point.
        
                        Args:
                            point (Point): The point to calculate distance to.
        
                        Returns:
                            float: The minimum distance from the segment to the point.
        
                        Example:
                            >>> segment = Segment(Point(0.0, 0.0), Point(2.0, 0.0))
                            >>> distance = segment.distance_to(Point(1.0, 1.0))  # 1.0
        """
    @typing.overload
    def distance_to(self, point_set: PointSet) -> ostk.core.type.Real:
        """
                        Calculate the distance from the segment to a point set.
        
                        Args:
                            point_set (PointSet): The point set to calculate distance to.
        
                        Returns:
                            float: The minimum distance from the segment to any point in the set.
        
                        Example:
                            >>> segment = Segment(Point(0.0, 0.0), Point(2.0, 0.0))
                            >>> points = PointSet([Point(1.0, 1.0), Point(3.0, 1.0)])
                            >>> distance = segment.distance_to(points)  # 1.0
        """
    def get_center(self) -> Point:
        """
                        Get the center (midpoint) of the segment.
        
                        Returns:
                            Point: The center point of the segment.
        
                        Example:
                            >>> segment = Segment(Point(0.0, 0.0), Point(2.0, 2.0))
                            >>> center = segment.get_center()  # Point(1.0, 1.0)
        """
    def get_direction(self) -> numpy.ndarray[numpy.float64[2, 1]]:
        """
                        Get the direction vector of the segment (from start to end, normalized).
        
                        Returns:
                            Vector2d: The normalized direction vector of the segment.
        
                        Example:
                            >>> segment = Segment(Point(0.0, 0.0), Point(3.0, 4.0))
                            >>> direction = segment.get_direction()  # [0.6, 0.8]
        """
    def get_first_point(self) -> Point:
        """
                        Get the first (starting) point of the segment.
        
                        Returns:
                            Point: The starting point of the segment.
        
                        Example:
                            >>> segment = Segment(Point(0.0, 0.0), Point(1.0, 1.0))
                            >>> start = segment.get_first_point()  # Point(0.0, 0.0)
        """
    def get_length(self) -> ostk.core.type.Real:
        """
                        Get the length of the segment.
        
                        Returns:
                            float: The length of the segment.
        
                        Example:
                            >>> segment = Segment(Point(0.0, 0.0), Point(3.0, 4.0))
                            >>> length = segment.get_length()  # 5.0
        """
    def get_second_point(self) -> Point:
        """
                        Get the second (ending) point of the segment.
        
                        Returns:
                            Point: The ending point of the segment.
        
                        Example:
                            >>> segment = Segment(Point(0.0, 0.0), Point(1.0, 1.0))
                            >>> end = segment.get_second_point()  # Point(1.0, 1.0)
        """
    def is_defined(self) -> bool:
        """
                        Check if the segment is defined.
        
                        Returns:
                            bool: True if the segment is defined, False otherwise.
        
                        Example:
                            >>> segment = Segment(Point(0.0, 0.0), Point(1.0, 1.0))
                            >>> segment.is_defined()  # True
        """
    def is_degenerate(self) -> bool:
        """
                        Check if the segment is degenerate (start and end points are the same).
        
                        Returns:
                            bool: True if the segment is degenerate, False otherwise.
        
                        Example:
                            >>> segment = Segment(Point(1.0, 1.0), Point(1.0, 1.0))
                            >>> segment.is_degenerate()  # True
                            >>> segment2 = Segment(Point(0.0, 0.0), Point(1.0, 1.0))
                            >>> segment2.is_degenerate()  # False
        """
    def to_line(self) -> Line:
        """
                        Convert the segment to an infinite line.
        
                        Returns:
                            Line: A line that passes through both endpoints of the segment.
        
                        Example:
                            >>> segment = Segment(Point(0.0, 0.0), Point(1.0, 1.0))
                            >>> line = segment.to_line()
        """
    def to_string(self, format: ostk.mathematics.geometry.d2.Object.Format = ..., precision: ostk.core.type.Integer = ...) -> ostk.core.type.String:
        """
                        Convert the segment to a string representation.
        
                        Args:
                            format (Object.Format, optional): The output format. Defaults to Standard.
                            precision (int, optional): The precision for floating point numbers. Defaults to undefined.
        
                        Returns:
                            str: String representation of the segment.
        
                        Example:
                            >>> segment = Segment(Point(0.0, 0.0), Point(1.0, 1.0))
                            >>> segment.to_string()
        """
def set_point_2_array(arg0: list[list[Point]]) -> None:
    ...
def set_point_array(arg0: list[Point]) -> None:
    ...
