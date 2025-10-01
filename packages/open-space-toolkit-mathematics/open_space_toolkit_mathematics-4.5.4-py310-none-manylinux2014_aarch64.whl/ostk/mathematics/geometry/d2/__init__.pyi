from __future__ import annotations
import numpy
import ostk.core.type
import typing
from . import object
__all__ = ['Intersection', 'Object', 'Transformation', 'object']
class Intersection:
    class Type:
        """
        Members:
        
          Undefined
        
          Empty
        
          Point
        
          PointSet
        
          Line
        
          LineString
        
          Segment
        
          Polygon
        
          Complex
        """
        Complex: typing.ClassVar[Intersection.Type]  # value = <Type.Complex: 8>
        Empty: typing.ClassVar[Intersection.Type]  # value = <Type.Empty: 1>
        Line: typing.ClassVar[Intersection.Type]  # value = <Type.Line: 4>
        LineString: typing.ClassVar[Intersection.Type]  # value = <Type.LineString: 6>
        Point: typing.ClassVar[Intersection.Type]  # value = <Type.Point: 2>
        PointSet: typing.ClassVar[Intersection.Type]  # value = <Type.PointSet: 3>
        Polygon: typing.ClassVar[Intersection.Type]  # value = <Type.Polygon: 7>
        Segment: typing.ClassVar[Intersection.Type]  # value = <Type.Segment: 5>
        Undefined: typing.ClassVar[Intersection.Type]  # value = <Type.Undefined: 0>
        __members__: typing.ClassVar[dict[str, Intersection.Type]]  # value = {'Undefined': <Type.Undefined: 0>, 'Empty': <Type.Empty: 1>, 'Point': <Type.Point: 2>, 'PointSet': <Type.PointSet: 3>, 'Line': <Type.Line: 4>, 'LineString': <Type.LineString: 6>, 'Segment': <Type.Segment: 5>, 'Polygon': <Type.Polygon: 7>, 'Complex': <Type.Complex: 8>}
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
    def empty() -> Intersection:
        """
                        Create an empty intersection.
        
                        Returns:
                            Intersection: An empty intersection containing no geometry.
        
                        Example:
                            >>> empty_intersection = Intersection.empty()
                            >>> empty_intersection.is_empty()  # True
        """
    @staticmethod
    def line(line: object.Line) -> Intersection:
        """
                        Create an intersection containing a line.
        
                        Args:
                            line (Line): The line to include in the intersection.
        
                        Returns:
                            Intersection: An intersection containing the line.
        
                        Example:
                            >>> line = Line(Point(0.0, 0.0), np.array([1.0, 1.0]))
                            >>> intersection = Intersection.line(line)
        """
    @staticmethod
    def point(point: object.Point) -> Intersection:
        """
                        Create an intersection containing a single point.
        
                        Args:
                            point (Point): The point to include in the intersection.
        
                        Returns:
                            Intersection: An intersection containing the point.
        
                        Example:
                            >>> point = Point(1.0, 2.0)
                            >>> intersection = Intersection.point(point)
        """
    @staticmethod
    def point_set(point_set: object.PointSet) -> Intersection:
        """
                        Create an intersection containing a point set.
        
                        Args:
                            point_set (PointSet): The point set to include in the intersection.
        
                        Returns:
                            Intersection: An intersection containing the point set.
        
                        Example:
                            >>> points = PointSet([Point(1.0, 2.0), Point(3.0, 4.0)])
                            >>> intersection = Intersection.point_set(points)
        """
    @staticmethod
    def segment(segment: object.Segment) -> Intersection:
        """
                        Create an intersection containing a segment.
        
                        Args:
                            segment (Segment): The segment to include in the intersection.
        
                        Returns:
                            Intersection: An intersection containing the segment.
        
                        Example:
                            >>> segment = Segment(Point(0.0, 0.0), Point(1.0, 1.0))
                            >>> intersection = Intersection.segment(segment)
        """
    @staticmethod
    def string_from_type(type: typing.Any) -> ostk.core.type.String:
        """
                        Get the string representation of an intersection type.
        
                        Args:
                            type (Intersection.Type): The intersection type.
        
                        Returns:
                            str: String representation of the type.
        
                        Example:
                            >>> Intersection.string_from_type(Intersection.Type.Point)  # "Point"
        """
    @staticmethod
    def undefined() -> Intersection:
        """
                        Create an undefined intersection.
        
                        Returns:
                            Intersection: An undefined intersection.
        
                        Example:
                            >>> undefined_intersection = Intersection.undefined()
                            >>> undefined_intersection.is_defined()  # False
        """
    def __add__(self, arg0: Intersection) -> Intersection:
        ...
    def __eq__(self, arg0: Intersection) -> bool:
        ...
    def __iadd__(self, arg0: Intersection) -> Intersection:
        ...
    def __ne__(self, arg0: Intersection) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __str__(self) -> str:
        ...
    def access_composite(self) -> object.Composite:
        """
                        Access the composite representation of the intersection.
        
                        Returns:
                            Composite: Reference to the composite containing all intersection objects.
        
                        Example:
                            >>> intersection = Intersection.point(Point(1.0, 2.0))
                            >>> composite = intersection.access_composite()
        """
    def as_composite(self) -> object.Composite:
        """
                        Convert the intersection to a Composite.
        
                        Returns:
                            Composite: The composite contained in the intersection.
        
                        Raises:
                            RuntimeError: If the intersection does not contain a Composite.
        
                        Example:
                            >>> composite = Composite(Point(1.0, 2.0))
                            >>> # intersection = Intersection.composite(composite)
                            >>> # extracted_composite = intersection.as_composite()
        """
    def as_line(self) -> object.Line:
        """
                        Convert the intersection to a Line.
        
                        Returns:
                            Line: The line contained in the intersection.
        
                        Raises:
                            RuntimeError: If the intersection does not contain a Line.
        
                        Example:
                            >>> line = Line(Point(0.0, 0.0), np.array([1.0, 1.0]))
                            >>> intersection = Intersection.line(line)
                            >>> extracted_line = intersection.as_line()
        """
    def as_line_string(self) -> object.LineString:
        """
                        Convert the intersection to a LineString.
        
                        Returns:
                            LineString: The line string contained in the intersection.
        
                        Raises:
                            RuntimeError: If the intersection does not contain a LineString.
        
                        Example:
                            >>> points = [Point(0.0, 0.0), Point(1.0, 1.0), Point(2.0, 2.0)]
                            >>> line_string = LineString(points)
                            >>> # intersection = Intersection.line_string(line_string)
                            >>> # extracted_line_string = intersection.as_line_string()
        """
    def as_point(self) -> object.Point:
        """
                        Convert the intersection to a Point.
        
                        Returns:
                            Point: The point contained in the intersection.
        
                        Raises:
                            RuntimeError: If the intersection does not contain a Point.
        
                        Example:
                            >>> intersection = Intersection.point(Point(1.0, 2.0))
                            >>> point = intersection.as_point()
        """
    def as_point_set(self) -> object.PointSet:
        """
                        Convert the intersection to a PointSet.
        
                        Returns:
                            PointSet: The point set contained in the intersection.
        
                        Raises:
                            RuntimeError: If the intersection does not contain a PointSet.
        
                        Example:
                            >>> points = PointSet([Point(1.0, 2.0), Point(3.0, 4.0)])
                            >>> intersection = Intersection.point_set(points)
                            >>> point_set = intersection.as_point_set()
        """
    def as_polygon(self) -> object.Polygon:
        """
                        Convert the intersection to a Polygon.
        
                        Returns:
                            Polygon: The polygon contained in the intersection.
        
                        Raises:
                            RuntimeError: If the intersection does not contain a Polygon.
        
                        Example:
                            >>> vertices = [Point(0.0, 0.0), Point(1.0, 0.0), Point(1.0, 1.0)]
                            >>> polygon = Polygon(vertices)
                            >>> # intersection = Intersection.polygon(polygon)
                            >>> # extracted_polygon = intersection.as_polygon()
        """
    def as_segment(self) -> object.Segment:
        """
                        Convert the intersection to a Segment.
        
                        Returns:
                            Segment: The segment contained in the intersection.
        
                        Raises:
                            RuntimeError: If the intersection does not contain a Segment.
        
                        Example:
                            >>> segment = Segment(Point(0.0, 0.0), Point(1.0, 1.0))
                            >>> intersection = Intersection.segment(segment)
                            >>> extracted_segment = intersection.as_segment()
        """
    def get_type(self) -> ...:
        """
                        Get the type of the intersection.
        
                        Returns:
                            Intersection.Type: The type of geometry contained in the intersection.
        
                        Example:
                            >>> intersection = Intersection.point(Point(1.0, 2.0))
                            >>> intersection.get_type()  # Intersection.Type.Point
        """
    def is_complex(self) -> bool:
        """
                        Check if the intersection is complex (contains multiple different types).
        
                        Returns:
                            bool: True if the intersection is complex, False otherwise.
        
                        Example:
                            >>> # Complex intersections contain multiple geometric types
                            >>> intersection.is_complex()
        """
    def is_composite(self) -> bool:
        """
                        Check if the intersection contains a Composite.
        
                        Returns:
                            bool: True if the intersection contains a Composite, False otherwise.
        
                        Example:
                            >>> composite = Composite(Point(1.0, 2.0))
                            >>> # intersection = Intersection.composite(composite)
                            >>> # intersection.is_composite()  # True
        """
    def is_defined(self) -> bool:
        """
                        Check if the intersection is defined.
        
                        Returns:
                            bool: True if the intersection is defined, False otherwise.
        
                        Example:
                            >>> intersection = Intersection.point(Point(1.0, 2.0))
                            >>> intersection.is_defined()  # True
        """
    def is_empty(self) -> bool:
        """
                        Check if the intersection is empty (no geometric objects).
        
                        Returns:
                            bool: True if the intersection is empty, False otherwise.
        
                        Example:
                            >>> empty_intersection = Intersection.empty()
                            >>> empty_intersection.is_empty()  # True
        """
    def is_line(self) -> bool:
        """
                        Check if the intersection contains a Line.
        
                        Returns:
                            bool: True if the intersection contains a Line, False otherwise.
        
                        Example:
                            >>> line = Line(Point(0.0, 0.0), np.array([1.0, 1.0]))
                            >>> intersection = Intersection.line(line)
                            >>> intersection.is_line()  # True
        """
    def is_line_string(self) -> bool:
        """
                        Check if the intersection contains a LineString.
        
                        Returns:
                            bool: True if the intersection contains a LineString, False otherwise.
        
                        Example:
                            >>> points = [Point(0.0, 0.0), Point(1.0, 1.0), Point(2.0, 2.0)]
                            >>> line_string = LineString(points)
                            >>> # intersection = Intersection.line_string(line_string)
                            >>> # intersection.is_line_string()  # True
        """
    def is_point(self) -> bool:
        """
                        Check if the intersection contains a Point.
        
                        Returns:
                            bool: True if the intersection contains a Point, False otherwise.
        
                        Example:
                            >>> intersection = Intersection.point(Point(1.0, 2.0))
                            >>> intersection.is_point()  # True
        """
    def is_point_set(self) -> bool:
        """
                        Check if the intersection contains a PointSet.
        
                        Returns:
                            bool: True if the intersection contains a PointSet, False otherwise.
        
                        Example:
                            >>> points = PointSet([Point(1.0, 2.0), Point(3.0, 4.0)])
                            >>> intersection = Intersection.point_set(points)
                            >>> intersection.is_point_set()  # True
        """
    def is_polygon(self) -> bool:
        """
                        Check if the intersection contains a Polygon.
        
                        Returns:
                            bool: True if the intersection contains a Polygon, False otherwise.
        
                        Example:
                            >>> vertices = [Point(0.0, 0.0), Point(1.0, 0.0), Point(1.0, 1.0)]
                            >>> polygon = Polygon(vertices)
                            >>> # intersection = Intersection.polygon(polygon)
                            >>> # intersection.is_polygon()  # True
        """
    def is_segment(self) -> bool:
        """
                        Check if the intersection contains a Segment.
        
                        Returns:
                            bool: True if the intersection contains a Segment, False otherwise.
        
                        Example:
                            >>> segment = Segment(Point(0.0, 0.0), Point(1.0, 1.0))
                            >>> intersection = Intersection.segment(segment)
                            >>> intersection.is_segment()  # True
        """
class Object:
    class Format:
        """
        Members:
        
          Undefined
        
          Standard
        
          WKT
        """
        Standard: typing.ClassVar[Object.Format]  # value = <Format.Standard: 1>
        Undefined: typing.ClassVar[Object.Format]  # value = <Format.Undefined: 0>
        WKT: typing.ClassVar[Object.Format]  # value = <Format.WKT: 2>
        __members__: typing.ClassVar[dict[str, Object.Format]]  # value = {'Undefined': <Format.Undefined: 0>, 'Standard': <Format.Standard: 1>, 'WKT': <Format.WKT: 2>}
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
    def __eq__(self, arg0: Object) -> bool:
        """
                        Check if two 2D objects are equal.
        
                        Args:
                            other (Object): The object to compare with.
        
                        Returns:
                            bool: True if objects are equal, False otherwise.
        
                        Example:
                            >>> point1 = Point(1.0, 2.0)
                            >>> point2 = Point(1.0, 2.0)
                            >>> point1 == point2  # True
        """
    def __ne__(self, arg0: Object) -> bool:
        """
                        Check if two 2D objects are not equal.
        
                        Args:
                            other (Object): The object to compare with.
        
                        Returns:
                            bool: True if objects are not equal, False otherwise.
        
                        Example:
                            >>> point1 = Point(1.0, 2.0)
                            >>> point2 = Point(3.0, 4.0)
                            >>> point1 != point2  # True
        """
    def __repr__(self) -> str:
        ...
    def __str__(self) -> str:
        ...
    def apply_transformation(self, transformation: typing.Any) -> None:
        """
                        Apply a transformation to the 2D object in place.
        
                        Args:
                            transformation (Transformation): The 2D transformation to apply.
        
                        Example:
                            >>> point = Point(1.0, 2.0)
                            >>> transformation = Translation([1.0, 1.0])
                            >>> point.apply_transformation(transformation)
        """
    def contains(self, object: Object) -> bool:
        """
                        Check if this 2D object contains another object.
        
                        Args:
                            object (Object): The object to check containment for.
        
                        Returns:
                            bool: True if this object contains the other, False otherwise.
        
                        Example:
                            >>> polygon = Polygon([Point(0.0, 0.0), Point(2.0, 0.0), Point(2.0, 2.0)])
                            >>> point = Point(1.0, 1.0)
                            >>> polygon.contains(point)  # True
        """
    def intersects(self, object: Object) -> bool:
        """
                        Check if this 2D object intersects with another object.
        
                        Args:
                            object (Object): The object to check intersection with.
        
                        Returns:
                            bool: True if objects intersect, False otherwise.
        
                        Example:
                            >>> line1 = Line(Point(0.0, 0.0), np.array([1.0, 0.0]))
                            >>> line2 = Line(Point(0.0, -1.0), np.array([0.0, 1.0]))
                            >>> line1.intersects(line2)  # True
        """
    def is_defined(self) -> bool:
        """
                        Check if the 2D object is defined.
        
                        Returns:
                            bool: True if the object is defined, False otherwise.
        
                        Example:
                            >>> point = Point(1.0, 2.0)
                            >>> point.is_defined()  # True
        """
class Transformation:
    class Type:
        """
        Members:
        
          Undefined
        
          Identity
        
          Translation
        
          Rotation
        
          Scaling
        
          Reflection
        
          Shear
        
          Affine
        """
        Affine: typing.ClassVar[Transformation.Type]  # value = <Type.Affine: 7>
        Identity: typing.ClassVar[Transformation.Type]  # value = <Type.Identity: 1>
        Reflection: typing.ClassVar[Transformation.Type]  # value = <Type.Reflection: 5>
        Rotation: typing.ClassVar[Transformation.Type]  # value = <Type.Rotation: 3>
        Scaling: typing.ClassVar[Transformation.Type]  # value = <Type.Scaling: 4>
        Shear: typing.ClassVar[Transformation.Type]  # value = <Type.Shear: 6>
        Translation: typing.ClassVar[Transformation.Type]  # value = <Type.Translation: 2>
        Undefined: typing.ClassVar[Transformation.Type]  # value = <Type.Undefined: 0>
        __members__: typing.ClassVar[dict[str, Transformation.Type]]  # value = {'Undefined': <Type.Undefined: 0>, 'Identity': <Type.Identity: 1>, 'Translation': <Type.Translation: 2>, 'Rotation': <Type.Rotation: 3>, 'Scaling': <Type.Scaling: 4>, 'Reflection': <Type.Reflection: 5>, 'Shear': <Type.Shear: 6>, 'Affine': <Type.Affine: 7>}
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
    def identity() -> Transformation:
        """
                        Create an identity transformation (no change).
        
                        Returns:
                            Transformation: The identity transformation.
        
                        Example:
                            >>> identity = Transformation.identity()
                            >>> point = Point(1.0, 2.0)
                            >>> identity.apply_to(point)  # Point(1.0, 2.0) - unchanged
        """
    @staticmethod
    def rotation(rotation_angle: typing.Any) -> Transformation:
        """
                        Create a rotation transformation around the origin.
        
                        Args:
                            rotation_angle (Angle): The rotation angle.
        
                        Returns:
                            Transformation: The rotation transformation.
        
                        Example:
                            >>> rotation = Transformation.rotation(Angle.degrees(90.0))
                            >>> point = Point(1.0, 0.0)
                            >>> rotation.apply_to(point)  # Point(0.0, 1.0)
        """
    @staticmethod
    def rotation_around(point: object.Point, rotation_angle: typing.Any) -> Transformation:
        """
                        Create a rotation transformation around a specific point.
        
                        Args:
                            point (Point): The center point of rotation.
                            rotation_angle (Angle): The rotation angle.
        
                        Returns:
                            Transformation: The rotation transformation around the specified point.
        
                        Example:
                            >>> center = Point(1.0, 1.0)
                            >>> rotation = Transformation.rotation_around(center, Angle.degrees(90.0))
                            >>> point = Point(2.0, 1.0)
                            >>> rotation.apply_to(point)  # Point(1.0, 2.0)
        """
    @staticmethod
    def string_from_type(type: typing.Any) -> ostk.core.type.String:
        """
                        Get the string representation of a transformation type.
        
                        Args:
                            type (Transformation.Type): The transformation type.
        
                        Returns:
                            str: String representation of the type.
        
                        Example:
                            >>> Transformation.string_from_type(Transformation.Type.Translation)  # "Translation"
        """
    @staticmethod
    def translation(translation_vector: numpy.ndarray[numpy.float64[2, 1]]) -> Transformation:
        """
                        Create a translation transformation.
        
                        Args:
                            translation_vector (Vector2d): The translation vector.
        
                        Returns:
                            Transformation: The translation transformation.
        
                        Example:
                            >>> translation = Transformation.translation([1.0, 2.0])
                            >>> point = Point(0.0, 0.0)
                            >>> translation.apply_to(point)  # Point(1.0, 2.0)
        """
    @staticmethod
    def type_of_matrix(matrix: numpy.ndarray[numpy.float64[3, 3]]) -> ...:
        """
                        Determine the transformation type from a matrix.
        
                        Args:
                            matrix (Matrix3d): The transformation matrix to analyze.
        
                        Returns:
                            Transformation.Type: The detected transformation type.
        
                        Example:
                            >>> import numpy as np
                            >>> matrix = np.eye(3)
                            >>> Transformation.type_of_matrix(matrix)  # Transformation.Type.Identity
        """
    @staticmethod
    def undefined() -> Transformation:
        """
                        Create an undefined transformation.
        
                        Returns:
                            Transformation: An undefined transformation.
        
                        Example:
                            >>> undefined_transform = Transformation.undefined()
                            >>> undefined_transform.is_defined()  # False
        """
    def __eq__(self, arg0: Transformation) -> bool:
        ...
    def __init__(self, matrix: numpy.ndarray[numpy.float64[3, 3]]) -> None:
        """
                        Create a 2D transformation from a 3x3 transformation matrix.
        
                        Args:
                            matrix (Matrix3d): The 3x3 transformation matrix in homogeneous coordinates.
        
                        Example:
                            >>> import numpy as np
                            >>> matrix = np.eye(3)  # Identity matrix
                            >>> transformation = Transformation(matrix)
        """
    def __ne__(self, arg0: Transformation) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __str__(self) -> str:
        ...
    @typing.overload
    def apply_to(self, point: object.Point) -> object.Point:
        """
                        Apply the transformation to a point.
        
                        Args:
                            point (Point): The point to transform.
        
                        Returns:
                            Point: The transformed point.
        
                        Example:
                            >>> point = Point(1.0, 2.0)
                            >>> translation = Transformation.translation([1.0, 1.0])
                            >>> transformed = translation.apply_to(point)  # Point(2.0, 3.0)
        """
    @typing.overload
    def apply_to(self, vector: numpy.ndarray[numpy.float64[2, 1]]) -> numpy.ndarray[numpy.float64[2, 1]]:
        """
                        Apply the transformation to a vector.
        
                        Args:
                            vector (Vector2d): The vector to transform.
        
                        Returns:
                            Vector2d: The transformed vector.
        
                        Example:
                            >>> vector = np.array([1.0, 0.0])
                            >>> rotation = Transformation.rotation(Angle.degrees(90.0))
                            >>> transformed = rotation.apply_to(vector)  # [0.0, 1.0]
        """
    def get_inverse(self) -> Transformation:
        """
                        Get the inverse transformation.
        
                        Returns:
                            Transformation: The inverse transformation.
        
                        Example:
                            >>> translation = Transformation.translation([1.0, 2.0])
                            >>> inverse = translation.get_inverse()  # Translation by [-1.0, -2.0]
        """
    def get_matrix(self) -> numpy.ndarray[numpy.float64[3, 3]]:
        """
                        Get the transformation matrix.
        
                        Returns:
                            Matrix3d: The 3x3 transformation matrix in homogeneous coordinates.
        
                        Example:
                            >>> transformation = Transformation.identity()
                            >>> matrix = transformation.get_matrix()  # 3x3 identity matrix
        """
    def get_type(self) -> ...:
        """
                        Get the type of the transformation.
        
                        Returns:
                            Transformation.Type: The transformation type (Identity, Translation, Rotation, etc.).
        
                        Example:
                            >>> transformation = Transformation.identity()
                            >>> transformation.get_type()  # Transformation.Type.Identity
        """
    def is_defined(self) -> bool:
        """
                        Check if the transformation is defined.
        
                        Returns:
                            bool: True if the transformation is defined, False otherwise.
        
                        Example:
                            >>> transformation = Transformation.identity()
                            >>> transformation.is_defined()  # True
        """
