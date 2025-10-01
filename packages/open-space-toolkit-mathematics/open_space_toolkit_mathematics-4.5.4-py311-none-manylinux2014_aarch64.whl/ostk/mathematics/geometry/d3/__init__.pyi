from __future__ import annotations
import numpy
import ostk.core.type
import typing
from . import object
from . import transformation
__all__ = ['Intersection', 'Object', 'Transformation', 'object', 'transformation']
class Intersection:
    """
    
                Represents the intersection of 3D geometric objects.
    
                An Intersection can contain various geometric types resulting from intersecting two objects.
            
    """
    class Type:
        """
        Members:
        
          Undefined
        
          Empty
        
          Point
        
          PointSet
        
          Line
        
          Ray
        
          Segment
        
          Plane
        
          Sphere
        
          Ellipsoid
        
          Complex
        """
        Complex: typing.ClassVar[Intersection.Type]  # value = <Type.Complex: 14>
        Ellipsoid: typing.ClassVar[Intersection.Type]  # value = <Type.Ellipsoid: 12>
        Empty: typing.ClassVar[Intersection.Type]  # value = <Type.Empty: 1>
        Line: typing.ClassVar[Intersection.Type]  # value = <Type.Line: 4>
        Plane: typing.ClassVar[Intersection.Type]  # value = <Type.Plane: 9>
        Point: typing.ClassVar[Intersection.Type]  # value = <Type.Point: 2>
        PointSet: typing.ClassVar[Intersection.Type]  # value = <Type.PointSet: 3>
        Ray: typing.ClassVar[Intersection.Type]  # value = <Type.Ray: 5>
        Segment: typing.ClassVar[Intersection.Type]  # value = <Type.Segment: 6>
        Sphere: typing.ClassVar[Intersection.Type]  # value = <Type.Sphere: 11>
        Undefined: typing.ClassVar[Intersection.Type]  # value = <Type.Undefined: 0>
        __members__: typing.ClassVar[dict[str, Intersection.Type]]  # value = {'Undefined': <Type.Undefined: 0>, 'Empty': <Type.Empty: 1>, 'Point': <Type.Point: 2>, 'PointSet': <Type.PointSet: 3>, 'Line': <Type.Line: 4>, 'Ray': <Type.Ray: 5>, 'Segment': <Type.Segment: 6>, 'Plane': <Type.Plane: 9>, 'Sphere': <Type.Sphere: 11>, 'Ellipsoid': <Type.Ellipsoid: 12>, 'Complex': <Type.Complex: 14>}
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
                            Intersection: An empty intersection.
                        
                        Example:
                            >>> intersection = Intersection.empty()
                            >>> intersection.is_empty()  # True
        """
    @staticmethod
    def line(line: object.Line) -> Intersection:
        """
                        Create an intersection from a line.
        
                        Args:
                            line (Line): The line.
        
                        Returns:
                            Intersection: An intersection containing the line.
                        
                        Example:
                            >>> intersection = Intersection.line(Line(Point(1.0, 2.0, 3.0), Point(3.0, 4.0, 5.0)))
                            >>> intersection.is_defined()  # True
        """
    @staticmethod
    def point(point: object.Point) -> Intersection:
        """
                        Create an intersection from a point.
        
                        Args:
                            point (Point): The point.
        
                        Returns:
                            Intersection: An intersection containing the point.
                        
                        Example:
                            >>> intersection = Intersection.point(Point(1.0, 2.0, 3.0))
                            >>> intersection.is_defined()  # True
        """
    @staticmethod
    def point_set(point_set: object.PointSet) -> Intersection:
        """
                        Create an intersection from a point set.
        
                        Args:
                            point_set (PointSet): The point set.
        
                        Returns:
                            Intersection: An intersection containing the point set.
                        
                        Example:
                            >>> intersection = Intersection.point_set(PointSet([Point(1.0, 2.0, 3.0), Point(3.0, 4.0, 5.0)]))
                            >>> intersection.is_defined()  # True
        """
    @staticmethod
    def ray(ray: object.Ray) -> Intersection:
        """
                        Create an intersection from a ray.
        
                        Args:
                            ray (Ray): The ray.
        
                        Returns:
                            Intersection: An intersection containing the ray.
                        
                        Example:
                            >>> intersection = Intersection.ray(Ray(Point(1.0, 2.0, 3.0), Vector(3.0, 4.0, 5.0)))
                            >>> intersection.is_defined()  # True
        """
    @staticmethod
    def segment(segment: object.Segment) -> Intersection:
        """
                        Create an intersection from a segment.
        
                        Args:
                            segment (Segment): The segment.
        
                        Returns:
                            Intersection: An intersection containing the segment.
                        
                        Example:
                            >>> intersection = Intersection.segment(Segment(Point(1.0, 2.0, 3.0), Point(3.0, 4.0, 5.0)))
                            >>> intersection.is_defined()  # True
        """
    @staticmethod
    def string_from_type(type: typing.Any) -> ostk.core.type.String:
        """
                        Convert an intersection type to a string.
        
                        Args:
                            type (Intersection.Type): The intersection type.
        
                        Returns:
                            str: The string representation of the type.
                        
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
                            >>> intersection = Intersection.undefined()
                            >>> intersection.is_defined()  # False
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
                        Access the composite object in the intersection.
        
                        Returns:
                            Composite: Reference to the composite object.
                        
                        Example:
                            >>> composite = intersection.access_composite()
        """
    def as_composite(self) -> object.Composite:
        """
                        Convert the intersection to a composite.
        
                        Returns:
                            Composite: The intersection as a composite object.
                        
                        Example:
                            >>> composite = intersection.as_composite()
        """
    def as_ellipsoid(self) -> object.Ellipsoid:
        """
                        Convert the intersection to an ellipsoid.
        
                        Returns:
                            Ellipsoid: The intersection as an ellipsoid.
                        
                        Example:
                            >>> ellipsoid = intersection.as_ellipsoid()
        """
    def as_line(self) -> object.Line:
        """
                        Convert the intersection to a line.
        
                        Returns:
                            Line: The intersection as a line.
                        
                        Example:
                            >>> intersection = Intersection.line(Line.points(Point(1.0, 2.0, 3.0), Point(3.0, 4.0, 5.0)))
                            >>> line = intersection.as_line()
        """
    def as_line_string(self) -> object.LineString:
        """
                        Convert the intersection to a line string.
        
                        Returns:
                            LineString: The intersection as a line string.
                        
                        Example:
                            >>> intersection = Intersection.point_set(PointSet([Point(1.0, 2.0, 3.0), Point(3.0, 4.0, 5.0)]))
                            >>> line_string = intersection.as_line_string()
        """
    def as_plane(self) -> object.Plane:
        """
                        Convert the intersection to a plane.
        
                        Returns:
                            Plane: The intersection as a plane.
                        
                        Example:
                            >>> plane = intersection.as_plane()
        """
    def as_point(self) -> object.Point:
        """
                        Convert the intersection to a point.
        
                        Returns:
                            Point: The intersection as a point.
                        
                        Example:
                            >>> intersection = Intersection.point(Point(1.0, 2.0, 3.0))
                            >>> point = intersection.as_point()
        """
    def as_point_set(self) -> object.PointSet:
        """
                        Convert the intersection to a point set.
        
                        Returns:
                            PointSet: The intersection as a point set.
                        
                        Example:
                            >>> intersection = Intersection.point_set(PointSet([Point(1.0, 2.0, 3.0), Point(3.0, 4.0, 5.0)]))
                            >>> point_set = intersection.as_point_set()
        """
    def as_polygon(self) -> object.Polygon:
        """
                        Convert the intersection to a polygon.
        
                        Returns:
                            Polygon: The intersection as a polygon.
                        
                        Example:
                            >>> polygon = intersection.as_polygon()
        """
    def as_pyramid(self) -> object.Pyramid:
        """
                        Convert the intersection to a pyramid.
        
                        Returns:
                            Pyramid: The intersection as a pyramid.
                        
                        Example:
                            >>> pyramid = intersection.as_pyramid()
        """
    def as_ray(self) -> object.Ray:
        """
                        Convert the intersection to a ray.
        
                        Returns:
                            Ray: The intersection as a ray.
                        
                        Example:
                            >>> intersection = Intersection.ray(Ray(Point(1.0, 2.0, 3.0), np.array([3.0, 4.0, 5.0])))
                            >>> ray = intersection.as_ray()
        """
    def as_segment(self) -> object.Segment:
        """
                        Convert the intersection to a segment.
        
                        Returns:
                            Segment: The intersection as a segment.
                        
                        Example:
                            >>> intersection = Intersection.segment(Segment(Point(1.0, 2.0, 3.0), Point(3.0, 4.0, 5.0)))
                            >>> segment = intersection.as_segment()
        """
    def as_sphere(self) -> object.Sphere:
        """
                        Convert the intersection to a sphere.
        
                        Returns:
                            Sphere: The intersection as a sphere.
                        
                        Example:
                            >>> sphere = intersection.as_sphere()
        """
    def get_type(self) -> ...:
        """
                        Get the type of the intersection.
        
                        Returns:
                            Intersection.Type: The type of the intersection.
                        
                        Example:
                            >>> intersection = Intersection.point(Point(1.0, 2.0, 3.0))
                            >>> intersection.get_type()  # Intersection.Type.Point
        """
    def is_complex(self) -> bool:
        """
                        Check if the intersection is complex (contains multiple objects).
        
                        Returns:
                            bool: True if the intersection contains multiple objects.
                        
                        Example:
                            >>> intersection = Intersection.point(Point(1.0, 2.0, 3.0)) + Intersection.point(Point(3.0, 4.0, 5.0))
                            >>> intersection.is_complex()  # True
        """
    def is_composite(self) -> bool:
        """
                        Check if the intersection is a composite.
        
                        Returns:
                            bool: True if the intersection contains a composite object.
                        
                        Example:
                            >>> intersection = Intersection.point_set(PointSet([Point(1.0, 2.0), Point(3.0, 4.0)]))
                            >>> intersection.is_composite()  # False
        """
    def is_defined(self) -> bool:
        """
                        Check if the intersection is defined.
        
                        Returns:
                            bool: True if the intersection is defined.
                        
                        Example:
                            >>> intersection = Intersection.point(Point(1.0, 2.0, 3.0))
                            >>> intersection.is_defined()  # True
        """
    def is_ellipsoid(self) -> bool:
        """
                        Check if the intersection is an ellipsoid.
        
                        Returns:
                            bool: True if the intersection contains an ellipsoid.
                        
                        Example:
                            >>> intersection = Intersection.point_set(PointSet([Point(1.0, 2.0, 3.0), Point(3.0, 4.0, 5.0)]))
                            >>> intersection.is_ellipsoid()  # False
        """
    def is_empty(self) -> bool:
        """
                        Check if the intersection is empty.
        
                        Returns:
                            bool: True if the intersection contains no objects.
                        
                        Example:
                            >>> intersection = Intersection.empty()
                            >>> intersection.is_empty()  # True
        """
    def is_line(self) -> bool:
        """
                        Check if the intersection is a line.
        
                        Returns:
                            bool: True if the intersection contains a line.
                        
                        Example:
                            >>> intersection = Intersection.line(Line.points(Point(1.0, 2.0, 3.0), Point(3.0, 4.0, 5.0)))
                            >>> intersection.is_line()  # True
        """
    def is_line_string(self) -> bool:
        """
                        Check if the intersection is a line string.
        
                        Returns:
                            bool: True if the intersection contains a line string.
                        
                        Example:
                            >>> intersection = Intersection.point_set(PointSet([Point(1.0, 2.0, 3.0), Point(3.0, 4.0, 5.0)]))
                            >>> intersection.is_line_string()  # False
        """
    def is_plane(self) -> bool:
        """
                        Check if the intersection is a plane.
        
                        Returns:
                            bool: True if the intersection contains a plane.
                        
                        Example:
                            >>> intersection = Intersection.point_set(PointSet([Point(1.0, 2.0, 3.0), Point(3.0, 4.0, 5.0)]))
                            >>> intersection.is_plane()  # False
        """
    def is_point(self) -> bool:
        """
                        Check if the intersection is a point.
        
                        Returns:
                            bool: True if the intersection contains a single point.
                        
                        Example:
                            >>> intersection = Intersection.point(Point(1.0, 2.0, 3.0))
                            >>> intersection.is_point()  # True
        """
    def is_point_set(self) -> bool:
        """
                        Check if the intersection is a point set.
        
                        Returns:
                            bool: True if the intersection contains a point set.
                        
                        Example:
                            >>> intersection = Intersection.point_set(PointSet([Point(1.0, 2.0, 3.0), Point(3.0, 4.0, 5.0)]))
                            >>> intersection.is_point_set()  # True
        """
    def is_polygon(self) -> bool:
        """
                        Check if the intersection is a polygon.
        
                        Returns:
                            bool: True if the intersection contains a polygon.
                        
                        Example:
                            >>> intersection = Intersection.point_set(PointSet([Point(1.0, 2.0, 3.0), Point(3.0, 4.0, 5.0)]))
                            >>> intersection.is_polygon()  # False
        """
    def is_pyramid(self) -> bool:
        """
                        Check if the intersection is a pyramid.
        
                        Returns:
                            bool: True if the intersection contains a pyramid.
                        
                        Example:
                            >>> intersection = Intersection.point_set(PointSet([Point(1.0, 2.0), Point(3.0, 4.0)]))
                            >>> intersection.is_pyramid()  # False
        """
    def is_ray(self) -> bool:
        """
                        Check if the intersection is a ray.
        
                        Returns:
                            bool: True if the intersection contains a ray.
                        
                        Example:
                            >>> intersection = Intersection.ray(Ray(Point(1.0, 2.0, 3.0), np.array([3.0, 4.0, 5.0])))
                            >>> intersection.is_ray()  # True
        """
    def is_segment(self) -> bool:
        """
                        Check if the intersection is a segment.
        
                        Returns:
                            bool: True if the intersection contains a segment.
                        
                        Example:
                            >>> intersection = Intersection.segment(Segment(Point(1.0, 2.0, 3.0), Point(3.0, 4.0, 5.0)))
                            >>> intersection.is_segment()  # True
        """
    def is_sphere(self) -> bool:
        """
                        Check if the intersection is a sphere.
        
                        Returns:
                            bool: True if the intersection contains a sphere.
                        
                        Example:
                            >>> intersection = Intersection.point_set(PointSet([Point(1.0, 2.0, 3.0), Point(3.0, 4.0, 5.0)]))
                            >>> intersection.is_sphere()  # False
        """
class Object:
    """
    
                    Base class for 3D geometric objects.
    
                    Object is the abstract base class for all 3D geometric primitives and shapes.
                
    """
    __hash__: typing.ClassVar[None] = None
    def __eq__(self, arg0: Object) -> bool:
        ...
    def __ne__(self, arg0: Object) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __str__(self) -> str:
        ...
    def apply_transformation(self, transformation: typing.Any) -> None:
        """
                        Apply a transformation to the object in place
        
                        Args:
                            transformation (Transformation): The transformation to apply.
        """
    def as_cone(self) -> ...:
        """
                        Convert the object to a cone.
        
                        Returns:
                            Cone: The cone.
        """
    def as_ellipsoid(self) -> ...:
        """
                        Convert the object to an ellipsoid.
        
                        Returns:
                            Ellipsoid: The ellipsoid.
        """
    def as_line(self) -> ...:
        """
                        Convert the object to a line.
        
                        Returns:
                            Line: The line.
        """
    def as_line_string(self) -> ...:
        """
                        Convert the object to a line string.
        
                        Returns:
                            LineString: The line string.
        """
    def as_plane(self) -> ...:
        """
                        Convert the object to a plane.
        
                        Returns:
                            Plane: The plane.
        """
    def as_point(self) -> ...:
        """
                        Convert the object to a point.
        
                        Returns:
                            Point: The point.
        """
    def as_point_set(self) -> ...:
        """
                        Convert the object to a point set.
        
                        Returns:
                            PointSet: The point set.
        """
    def as_polygon(self) -> ...:
        """
                        Convert the object to a polygon.
        
                        Returns:
                            Polygon: The polygon.
        """
    def as_pyramid(self) -> ...:
        """
                        Convert the object to a pyramid.
        
                        Returns:
                            Pyramid: The pyramid.
        """
    def as_ray(self) -> ...:
        """
                        Convert the object to a ray.
        
                        Returns:
                            Ray: The ray.
        """
    def as_segment(self) -> ...:
        """
                        Convert the object to a segment.
        
                        Returns:
                            Segment: The segment.
        """
    def as_sphere(self) -> ...:
        """
                        Convert the object to a sphere.
        
                        Returns:
                            Sphere: The sphere.
        """
    def contains(self, arg0: Object) -> bool:
        """
                        Check if this object contains another object.
        
                        Args:
                            object (Object): The object to check containment of.
        
                        Returns:
                            bool: True if this object contains the other object.
        
                        Example:
                            >>> object = Cone(Point(1.0, 2.0, 3.0), [0.0, 0.0, 1.0], Angle.degrees(30.0))
                            >>> other_object = Point(1.0, 2.0, 3.1)
                            >>> object.contains(other_object)  # True
        """
    def intersects(self, arg0: Object) -> bool:
        """
                        Check if this object intersects another object.
        
                        Args:
                            object (Object): The object to check intersection with.
        
                        Returns:
                            bool: True if the objects intersect.
        
                        Example:
                            >>> object = Cone(Point(1.0, 2.0, 3.0), [0.0, 0.0, 1.0], Angle.degrees(30.0))
                            >>> other_object = Point(1.0, 2.0, 3.1)
                            >>> object.intersects(other_object)  # True
        """
    def is_cone(self) -> bool:
        """
                        Check if the object is a cone.
        
                        Returns:
                            bool: True if the object is a cone.
        """
    def is_defined(self) -> bool:
        """
                        Check if the object is defined.
        
                        Returns:
                            bool: True if the object is defined.
        
                        Example:
                            >>> object = Point(1.0, 2.0, 3.0)
                            >>> object.is_defined()  # True
        """
    def is_ellipsoid(self) -> bool:
        """
                        Check if the object is an ellipsoid.
        
                        Returns:
                            bool: True if the object is an ellipsoid.
        """
    def is_line(self) -> bool:
        """
                        Check if the object is a line.
        
                        Returns:
                            bool: True if the object is a line.
        """
    def is_line_string(self) -> bool:
        """
                        Check if the object is a line string.
        
                        Returns:
                            bool: True if the object is a line string.
        """
    def is_plane(self) -> bool:
        """
                        Check if the object is a plane.
        
                        Returns:
                            bool: True if the object is a plane.
        """
    def is_point(self) -> bool:
        """
                        Check if the object is a point.
        
                        Returns:
                            bool: True if the object is a point.
        """
    def is_point_set(self) -> bool:
        """
                        Check if the object is a point set.
        
                        Returns:
                            bool: True if the object is a point set.
        """
    def is_polygon(self) -> bool:
        """
                        Check if the object is a polygon.
        
                        Returns:
                            bool: True if the object is a polygon.
        """
    def is_pyramid(self) -> bool:
        """
                        Check if the object is a pyramid.
        
                        Returns:
                            bool: True if the object is a pyramid.
        """
    def is_ray(self) -> bool:
        """
                        Check if the object is a ray.
        
                        Returns:
                            bool: True if the object is a ray.
        """
    def is_segment(self) -> bool:
        """
                        Check if the object is a segment.
        
                        Returns:
                            bool: True if the object is a segment.
        """
    def is_sphere(self) -> bool:
        """
                        Check if the object is a sphere.
        
                        Returns:
                            bool: True if the object is a sphere.
        """
class Transformation:
    """
    
                Represents a 3D geometric transformation.
    
                A Transformation can represent translation, rotation, scaling, reflection, shear, or general affine transformations.
            
    """
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
                        Create an identity transformation.
        
                        Returns:
                            Transformation: An identity transformation.
        
                        Example:
                            >>> transformation = Transformation.identity()
                            >>> transformation.is_defined()  # True
        """
    @staticmethod
    @typing.overload
    def rotation(rotation_vector: typing.Any) -> Transformation:
        """
                        Create a rotation transformation from a rotation vector.
        
                        Args:
                            rotation_vector (RotationVector): The rotation vector.
        
                        Returns:
                            Transformation: A rotation transformation.
        
                        Example:
                            >>> rotation_vector = RotationVector(1.0, 2.0, 3.0)
                            >>> transformation = Transformation.rotation(rotation_vector)
                            >>> transformation.is_defined()  # True
        """
    @staticmethod
    @typing.overload
    def rotation(rotation_matrix: typing.Any) -> Transformation:
        """
                        Create a rotation transformation from a rotation matrix.
        
                        Args:
                            rotation_matrix (RotationMatrix): The rotation matrix.
        
                        Returns:
                            Transformation: A rotation transformation.
        
                        Example:
                            >>> rotation_matrix = RotationMatrix(1.0, 2.0, 3.0)
                            >>> transformation = Transformation.rotation(rotation_matrix)
                            >>> transformation.is_defined()  # True
        """
    @staticmethod
    def rotation_around(point: object.Point, rotation_vector: typing.Any) -> Transformation:
        """
                        Create a rotation transformation around a point.
        
                        Args:
                            point (Point): The point to rotate around.
                            rotation_vector (RotationVector): The rotation vector.
        
                        Returns:
                            Transformation: A rotation transformation around the point.
        
                        Example:
                            >>> point = Point(1.0, 2.0, 3.0)
                            >>> rotation_vector = RotationVector(1.0, 2.0, 3.0)
                            >>> transformation = Transformation.rotation_around(point, rotation_vector)
                            >>> transformation.is_defined()  # True
        """
    @staticmethod
    def string_from_type(type: typing.Any) -> ostk.core.type.String:
        """
                        Convert a transformation type to a string.
        
                        Args:
                            type (Transformation.Type): The transformation type.
        
                        Returns:
                            str: The string representation of the type.
        
                        Example:
                            >>> transformation = Transformation.identity()
                            >>> transformation.string_from_type()  # "Identity"
        """
    @staticmethod
    def translation(translation_vector: numpy.ndarray[numpy.float64[3, 1]]) -> Transformation:
        """
                        Create a translation transformation.
        
                        Args:
                            translation_vector (numpy.ndarray): The translation vector.
        
                        Returns:
                            Transformation: A translation transformation.
        
                        Example:
                            >>> translation_vector = Vector3d(1.0, 2.0, 3.0)
                            >>> transformation = Transformation.translation(translation_vector)
                            >>> transformation.is_defined()  # True
        """
    @staticmethod
    def type_of_matrix(matrix: numpy.ndarray[numpy.float64[4, 4]]) -> ...:
        """
                        Determine the type of a transformation matrix.
        
                        Args:
                            matrix (numpy.ndarray): The 4x4 transformation matrix.
        
                        Returns:
                            Transformation.Type: The type of the transformation.
        
                        Example:
                            >>> transformation = Transformation.identity()
                            >>> transformation.type_of_matrix()  # Transformation.Type.Identity
        """
    @staticmethod
    def undefined() -> Transformation:
        """
                        Create an undefined transformation.
        
                        Returns:
                            Transformation: An undefined transformation.
        
                        Example:
                            >>> transformation = Transformation.undefined()
                            >>> transformation.is_defined()  # False
        """
    def __eq__(self, arg0: Transformation) -> bool:
        ...
    def __init__(self, matrix: numpy.ndarray[numpy.float64[4, 4]]) -> None:
        """
                    Construct a transformation from a 4x4 matrix.
        
                    Args:
                        matrix (numpy.ndarray): A 4x4 transformation matrix.
        
                    Example:
                        >>> import numpy as np
                        >>> matrix = np.eye(3)  # 3x3 identity matrix
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
                            >>> transformation = Transformation.identity()
                            >>> point = Point(1.0, 2.0, 3.0)
                            >>> transformed_point = transformation.apply_to(point)  # Point(1.0, 2.0, 3.0)
        """
    @typing.overload
    def apply_to(self, vector: numpy.ndarray[numpy.float64[3, 1]]) -> numpy.ndarray[numpy.float64[3, 1]]:
        """
                        Apply the transformation to a vector.
        
                        Args:
                            vector (numpy.ndarray): The vector to transform.
        
                        Returns:
                            numpy.ndarray: The transformed vector.
        
                        Example:
                            >>> transformation = Transformation.identity()
                            >>> vector = Vector3d(1.0, 2.0, 3.0)
                            >>> transformed_vector = transformation.apply_to(vector)  # Vector3d(1.0, 2.0, 3.0)
        """
    def get_inverse(self) -> Transformation:
        """
                        Get the inverse transformation.
        
                        Returns:
                            Transformation: The inverse transformation.
        
                        Example:
                            >>> transformation = Transformation.identity()
                            >>> inverse = transformation.get_inverse()  # Identity transformation
        """
    def get_matrix(self) -> numpy.ndarray[numpy.float64[4, 4]]:
        """
                        Get the transformation matrix.
        
                        Returns:
                            numpy.ndarray: The 4x4 transformation matrix.
        
                        Example:
                            >>> transformation = Transformation.identity()
                            >>> matrix = transformation.get_matrix()  # 4x4 identity matrix
        """
    def get_type(self) -> ...:
        """
                        Get the type of the transformation.
        
                        Returns:
                            Transformation.Type: The transformation type.
        
                        Example:
                            >>> transformation = Transformation.identity()
                            >>> transformation.get_type()  # Transformation.Type.Identity
        """
    def is_defined(self) -> bool:
        """
                        Check if the transformation is defined.
        
                        Returns:
                            bool: True if the transformation is defined.
        
                        Example:
                            >>> transformation = Transformation.identity()
                            >>> transformation.is_defined()  # True
        """
