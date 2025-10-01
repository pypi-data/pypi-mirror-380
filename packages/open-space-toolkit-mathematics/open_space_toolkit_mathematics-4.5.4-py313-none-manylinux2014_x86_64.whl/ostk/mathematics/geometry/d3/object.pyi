from __future__ import annotations
import numpy
import ostk.core.type
import ostk.mathematics.geometry.d2.object
import ostk.mathematics.geometry.d3
import typing
__all__ = ['Composite', 'Cone', 'Cuboid', 'Ellipsoid', 'Line', 'LineString', 'Plane', 'Point', 'PointSet', 'Polygon', 'Pyramid', 'Ray', 'Segment', 'Sphere', 'set_point_3_array']
class Composite(ostk.mathematics.geometry.d3.Object):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def empty() -> Composite:
        """
                        Create an empty composite (containing no objects).
        
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
                        Create an undefined composite.
        
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
    def __init__(self, object: ostk.mathematics.geometry.d3.Object) -> None:
        """
                        Create a composite object from a single geometric object.
        
                        Args:
                            object (Object): The geometric object to wrap in the composite.
        
                        Example:
                            >>> point = Point(1.0, 2.0, 3.0)
                            >>> composite = Composite(point)
        """
    def __ne__(self, arg0: Composite) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __str__(self) -> str:
        ...
    def access_object_at(self, index: int) -> ostk.mathematics.geometry.d3.Object:
        """
                        Access the object at a specific index in the composite.
        
                        Args:
                            index (int): The index of the object to access.
        
                        Returns:
                            Object: Reference to the object at the specified index.
        
                        Raises:
                            IndexError: If the index is out of bounds.
        
                        Example:
                            >>> composite = Composite(Point(1.0, 2.0, 3.0))
                            >>> obj = composite.access_object_at(0)
        """
    def apply_transformation(self, transformation: typing.Any) -> None:
        """
                        Apply a transformation to all objects in the composite in place.
        
                        Args:
                            transformation (Transformation): The transformation to apply.
        
                        Example:
                            >>> composite = Composite(Point(1.0, 2.0, 3.0))
                            >>> transformation = Translation([1.0, 1.0, 1.0])
                            >>> composite.apply_transformation(transformation)
        """
    def as_composite(self) -> Composite:
        """
                        Convert the composite to a Composite object.
        
                        Returns:
                            Composite: The composite object contained in the composite.
        
                        Raises:
                            RuntimeError: If the composite does not contain a Composite.
        
                        Example:
                            >>> inner_composite = Composite(Point(1.0, 2.0, 3.0))
                            >>> outer_composite = Composite(inner_composite)
                            >>> extracted_composite = outer_composite.as_composite()
        """
    def as_cone(self) -> Cone:
        """
                        Convert the composite to a Cone object.
        
                        Returns:
                            Cone: The cone object contained in the composite.
        
                        Raises:
                            RuntimeError: If the composite does not contain a Cone.
        
                        Example:
                            >>> cone = Cone(Point(0.0, 0.0, 0.0), np.array([0.0, 0.0, 1.0]), Angle.degrees(30.0))
                            >>> composite = Composite(cone)
                            >>> extracted_cone = composite.as_cone()
        """
    def as_ellipsoid(self) -> Ellipsoid:
        """
                        Convert the composite to an Ellipsoid object.
        
                        Returns:
                            Ellipsoid: The ellipsoid object contained in the composite.
        
                        Raises:
                            RuntimeError: If the composite does not contain an Ellipsoid.
        
                        Example:
                            >>> ellipsoid = Ellipsoid(Point(0.0, 0.0, 0.0), 1.0, 0.8, 0.6)
                            >>> composite = Composite(ellipsoid)
                            >>> extracted_ellipsoid = composite.as_ellipsoid()
        """
    def as_line(self) -> Line:
        """
                        Convert the composite to a Line object.
        
                        Returns:
                            Line: The line object contained in the composite.
        
                        Raises:
                            RuntimeError: If the composite does not contain a Line.
        
                        Example:
                            >>> line = Line(Point(0.0, 0.0, 0.0), np.array([1.0, 0.0, 0.0]))
                            >>> composite = Composite(line)
                            >>> extracted_line = composite.as_line()
        """
    def as_line_string(self) -> LineString:
        """
                        Convert the composite to a LineString object.
        
                        Returns:
                            LineString: The line string object contained in the composite.
        
                        Raises:
                            RuntimeError: If the composite does not contain a LineString.
        
                        Example:
                            >>> points = [Point(0.0, 0.0, 0.0), Point(1.0, 1.0, 1.0), Point(2.0, 2.0, 2.0)]
                            >>> line_string = LineString(points)
                            >>> composite = Composite(line_string)
                            >>> extracted_line_string = composite.as_line_string()
        """
    def as_plane(self) -> Plane:
        """
                        Convert the composite to a Plane object.
        
                        Returns:
                            Plane: The plane object contained in the composite.
        
                        Raises:
                            RuntimeError: If the composite does not contain a Plane.
        
                        Example:
                            >>> plane = Plane(Point(0.0, 0.0, 0.0), np.array([0.0, 0.0, 1.0]))
                            >>> composite = Composite(plane)
                            >>> extracted_plane = composite.as_plane()
        """
    def as_point(self) -> Point:
        """
                        Convert the composite to a Point object.
        
                        Returns:
                            Point: The point object contained in the composite.
        
                        Raises:
                            RuntimeError: If the composite does not contain a Point.
        
                        Example:
                            >>> composite = Composite(Point(1.0, 2.0, 3.0))
                            >>> point = composite.as_point()
        """
    def as_point_set(self) -> PointSet:
        """
                        Convert the composite to a PointSet object.
        
                        Returns:
                            PointSet: The point set object contained in the composite.
        
                        Raises:
                            RuntimeError: If the composite does not contain a PointSet.
        
                        Example:
                            >>> point_set = PointSet([Point(1.0, 2.0, 3.0), Point(4.0, 5.0, 6.0)])
                            >>> composite = Composite(point_set)
                            >>> extracted_set = composite.as_point_set()
        """
    def as_polygon(self) -> Polygon:
        """
                        Convert the composite to a Polygon object.
        
                        Returns:
                            Polygon: The polygon object contained in the composite.
        
                        Raises:
                            RuntimeError: If the composite does not contain a Polygon.
        
                        Example:
                            >>> vertices = [Point(0.0, 0.0, 0.0), Point(1.0, 0.0, 0.0), Point(1.0, 1.0, 0.0)]
                            >>> polygon = Polygon(vertices)
                            >>> composite = Composite(polygon)
                            >>> extracted_polygon = composite.as_polygon()
        """
    def as_pyramid(self) -> Pyramid:
        """
                        Convert the composite to a Pyramid object.
        
                        Returns:
                            Pyramid: The pyramid object contained in the composite.
        
                        Raises:
                            RuntimeError: If the composite does not contain a Pyramid.
        
                        Example:
                            >>> apex = Point(0.0, 0.0, 1.0)
                            >>> base = Polygon([Point(0.0, 0.0, 0.0), Point(1.0, 0.0, 0.0), Point(1.0, 1.0, 0.0)])
                            >>> pyramid = Pyramid(base, apex)
                            >>> composite = Composite(pyramid)
                            >>> extracted_pyramid = composite.as_pyramid()
        """
    def as_ray(self) -> Ray:
        """
                        Convert the composite to a Ray object.
        
                        Returns:
                            Ray: The ray object contained in the composite.
        
                        Raises:
                            RuntimeError: If the composite does not contain a Ray.
        
                        Example:
                            >>> ray = Ray(Point(0.0, 0.0, 0.0), np.array([1.0, 0.0, 0.0]))
                            >>> composite = Composite(ray)
                            >>> extracted_ray = composite.as_ray()
        """
    def as_segment(self) -> Segment:
        """
                        Convert the composite to a Segment object.
        
                        Returns:
                            Segment: The segment object contained in the composite.
        
                        Raises:
                            RuntimeError: If the composite does not contain a Segment.
        
                        Example:
                            >>> segment = Segment(Point(0.0, 0.0, 0.0), Point(1.0, 1.0, 1.0))
                            >>> composite = Composite(segment)
                            >>> extracted_segment = composite.as_segment()
        """
    def as_sphere(self) -> Sphere:
        """
                        Convert the composite to a Sphere object.
        
                        Returns:
                            Sphere: The sphere object contained in the composite.
        
                        Raises:
                            RuntimeError: If the composite does not contain a Sphere.
        
                        Example:
                            >>> sphere = Sphere(Point(0.0, 0.0, 0.0), 1.0)
                            >>> composite = Composite(sphere)
                            >>> extracted_sphere = composite.as_sphere()
        """
    @typing.overload
    def contains(self, object: ostk.mathematics.geometry.d3.Object) -> bool:
        """
                        Check if the composite contains another geometric object.
        
                        Args:
                            object (Object): The object to check containment for.
        
                        Returns:
                            bool: True if the composite contains the object, False otherwise.
        
                        Example:
                            >>> composite = Composite(Sphere(Point(0.0, 0.0, 0.0), 2.0))
                            >>> point = Point(0.5, 0.0, 0.0)
                            >>> composite.contains(point)  # True
        """
    @typing.overload
    def contains(self, composite: Composite) -> bool:
        """
                        Check if the composite contains another composite.
        
                        Args:
                            composite (Composite): The composite to check containment for.
        
                        Returns:
                            bool: True if this composite contains the other composite, False otherwise.
        
                        Example:
                            >>> outer_composite = Composite(Sphere(Point(0.0, 0.0, 0.0), 2.0))
                            >>> inner_composite = Composite(Sphere(Point(0.0, 0.0, 0.0), 1.0))
                            >>> outer_composite.contains(inner_composite)  # True
        """
    def get_object_count(self) -> int:
        """
                        Get the number of objects contained in the composite.
        
                        Returns:
                            int: The number of objects in the composite.
        
                        Example:
                            >>> composite = Composite(Point(1.0, 2.0, 3.0))
                            >>> count = composite.get_object_count()  # 1
        """
    @typing.overload
    def intersection_with(self, object: ostk.mathematics.geometry.d3.Object) -> ...:
        """
                        Compute the intersection of the composite with another geometric object.
        
                        Args:
                            object (Object): The object to compute intersection with.
        
                        Returns:
                            Intersection: The intersection result.
        
                        Example:
                            >>> composite = Composite(Sphere(Point(0.0, 0.0, 0.0), 1.0))
                            >>> line = Line(Point(-2.0, 0.0, 0.0), np.array([1.0, 0.0, 0.0]))
                            >>> intersection = composite.intersection_with(line)
        """
    @typing.overload
    def intersection_with(self, composite: Composite) -> ...:
        """
                        Compute the intersection of the composite with another composite.
        
                        Args:
                            composite (Composite): The composite to compute intersection with.
        
                        Returns:
                            Intersection: The intersection result.
        
                        Example:
                            >>> composite1 = Composite(Sphere(Point(0.0, 0.0, 0.0), 1.0))
                            >>> composite2 = Composite(Sphere(Point(1.5, 0.0, 0.0), 1.0))
                            >>> intersection = composite1.intersection_with(composite2)
        """
    @typing.overload
    def intersects(self, object: ostk.mathematics.geometry.d3.Object) -> bool:
        """
                        Check if the composite intersects with another geometric object.
        
                        Args:
                            object (Object): The object to check intersection with.
        
                        Returns:
                            bool: True if the composite intersects the object, False otherwise.
        
                        Example:
                            >>> composite = Composite(Sphere(Point(0.0, 0.0, 0.0), 1.0))
                            >>> point = Point(0.5, 0.0, 0.0)
                            >>> composite.intersects(point)  # True
        """
    @typing.overload
    def intersects(self, composite: Composite) -> bool:
        """
                        Check if the composite intersects with another composite.
        
                        Args:
                            composite (Composite): The composite to check intersection with.
        
                        Returns:
                            bool: True if the composites intersect, False otherwise.
        
                        Example:
                            >>> composite1 = Composite(Sphere(Point(0.0, 0.0, 0.0), 1.0))
                            >>> composite2 = Composite(Sphere(Point(1.5, 0.0, 0.0), 1.0))
                            >>> composite1.intersects(composite2)  # True
        """
    def is_composite(self) -> bool:
        """
                        Check if the composite contains another Composite object.
        
                        Returns:
                            bool: True if the composite contains a Composite, False otherwise.
        
                        Example:
                            >>> inner_composite = Composite(Point(1.0, 2.0, 3.0))
                            >>> outer_composite = Composite(inner_composite)
                            >>> outer_composite.is_composite()  # True
        """
    def is_cone(self) -> bool:
        """
                        Check if the composite contains a Cone object.
        
                        Returns:
                            bool: True if the composite contains a Cone, False otherwise.
        
                        Example:
                            >>> cone = Cone(Point(0.0, 0.0, 0.0), np.array([0.0, 0.0, 1.0]), Angle.degrees(30.0))
                            >>> composite = Composite(cone)
                            >>> composite.is_cone()  # True
        """
    def is_defined(self) -> bool:
        """
                        Check if the composite is defined.
        
                        Returns:
                            bool: True if the composite is defined, False otherwise.
        
                        Example:
                            >>> composite = Composite(Point(1.0, 2.0, 3.0))
                            >>> composite.is_defined()  # True
        """
    def is_ellipsoid(self) -> bool:
        """
                        Check if the composite contains an Ellipsoid object.
        
                        Returns:
                            bool: True if the composite contains an Ellipsoid, False otherwise.
        
                        Example:
                            >>> ellipsoid = Ellipsoid(Point(0.0, 0.0, 0.0), 1.0, 0.8, 0.6)
                            >>> composite = Composite(ellipsoid)
                            >>> composite.is_ellipsoid()  # True
        """
    def is_empty(self) -> bool:
        """
                        Check if the composite is empty (contains no objects).
        
                        Returns:
                            bool: True if the composite is empty, False otherwise.
        
                        Example:
                            >>> empty_composite = Composite.empty()
                            >>> empty_composite.is_empty()  # True
        """
    def is_line(self) -> bool:
        """
                        Check if the composite contains a Line object.
        
                        Returns:
                            bool: True if the composite contains a Line, False otherwise.
        
                        Example:
                            >>> line = Line(Point(0.0, 0.0, 0.0), np.array([1.0, 0.0, 0.0]))
                            >>> composite = Composite(line)
                            >>> composite.is_line()  # True
        """
    def is_line_string(self) -> bool:
        """
                        Check if the composite contains a LineString object.
        
                        Returns:
                            bool: True if the composite contains a LineString, False otherwise.
        
                        Example:
                            >>> points = [Point(0.0, 0.0, 0.0), Point(1.0, 1.0, 1.0), Point(2.0, 2.0, 2.0)]
                            >>> line_string = LineString(points)
                            >>> composite = Composite(line_string)
                            >>> composite.is_line_string()  # True
        """
    def is_plane(self) -> bool:
        """
                        Check if the composite contains a Plane object.
        
                        Returns:
                            bool: True if the composite contains a Plane, False otherwise.
        
                        Example:
                            >>> plane = Plane(Point(0.0, 0.0, 0.0), np.array([0.0, 0.0, 1.0]))
                            >>> composite = Composite(plane)
                            >>> composite.is_plane()  # True
        """
    def is_point(self) -> bool:
        """
                        Check if the composite contains a Point object.
        
                        Returns:
                            bool: True if the composite contains a Point, False otherwise.
        
                        Example:
                            >>> composite = Composite(Point(1.0, 2.0, 3.0))
                            >>> composite.is_point()  # True
        """
    def is_point_set(self) -> bool:
        """
                        Check if the composite contains a PointSet object.
        
                        Returns:
                            bool: True if the composite contains a PointSet, False otherwise.
        
                        Example:
                            >>> point_set = PointSet([Point(1.0, 2.0, 3.0), Point(4.0, 5.0, 6.0)])
                            >>> composite = Composite(point_set)
                            >>> composite.is_point_set()  # True
        """
    def is_polygon(self) -> bool:
        """
                        Check if the composite contains a Polygon object.
        
                        Returns:
                            bool: True if the composite contains a Polygon, False otherwise.
        
                        Example:
                            >>> vertices = [Point(0.0, 0.0, 0.0), Point(1.0, 0.0, 0.0), Point(1.0, 1.0, 0.0)]
                            >>> polygon = Polygon(vertices)
                            >>> composite = Composite(polygon)
                            >>> composite.is_polygon()  # True
        """
    def is_pyramid(self) -> bool:
        """
                        Check if the composite contains a Pyramid object.
        
                        Returns:
                            bool: True if the composite contains a Pyramid, False otherwise.
        
                        Example:
                            >>> apex = Point(0.0, 0.0, 1.0)
                            >>> base = Polygon([Point(0.0, 0.0, 0.0), Point(1.0, 0.0, 0.0), Point(1.0, 1.0, 0.0)])
                            >>> pyramid = Pyramid(base, apex)
                            >>> composite = Composite(pyramid)
                            >>> composite.is_pyramid()  # True
        """
    def is_ray(self) -> bool:
        """
                        Check if the composite contains a Ray object.
        
                        Returns:
                            bool: True if the composite contains a Ray, False otherwise.
        
                        Example:
                            >>> ray = Ray(Point(0.0, 0.0, 0.0), np.array([1.0, 0.0, 0.0]))
                            >>> composite = Composite(ray)
                            >>> composite.is_ray()  # True
        """
    def is_segment(self) -> bool:
        """
                        Check if the composite contains a Segment object.
        
                        Returns:
                            bool: True if the composite contains a Segment, False otherwise.
        
                        Example:
                            >>> segment = Segment(Point(0.0, 0.0, 0.0), Point(1.0, 1.0, 1.0))
                            >>> composite = Composite(segment)
                            >>> composite.is_segment()  # True
        """
    def is_sphere(self) -> bool:
        """
                        Check if the composite contains a Sphere object.
        
                        Returns:
                            bool: True if the composite contains a Sphere, False otherwise.
        
                        Example:
                            >>> sphere = Sphere(Point(0.0, 0.0, 0.0), 1.0)
                            >>> composite = Composite(sphere)
                            >>> composite.is_sphere()  # True
        """
class Cone(ostk.mathematics.geometry.d3.Object):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def undefined() -> Cone:
        """
                        Create an undefined cone.
        
                        Returns:
                            Cone: An undefined cone object.
        
                        Example:
                            >>> undefined_cone = Cone.undefined()
                            >>> undefined_cone.is_defined()  # False
        """
    def __eq__(self, arg0: Cone) -> bool:
        ...
    def __init__(self, apex: Point, axis: numpy.ndarray[numpy.float64[3, 1]], angle: typing.Any) -> None:
        """
                        Create a 3D cone with specified apex, axis, and angle.
        
                        Args:
                            apex (Point): The apex (tip) point of the cone.
                            axis (np.array): The axis direction vector of the cone.
                            angle (Angle): The half-angle of the cone opening.
        
                        Example:
                            >>> apex = Point(0.0, 0.0, 0.0)
                            >>> axis = np.array([0.0, 0.0, 1.0])
                            >>> angle = Angle.degrees(30.0)
                            >>> cone = Cone(apex, axis, angle)
        """
    def __ne__(self, arg0: Cone) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __str__(self) -> str:
        ...
    def apply_transformation(self, transformation: typing.Any) -> None:
        """
                        Apply a transformation to the cone in place.
        
                        Args:
                            transformation (Transformation): The transformation to apply.
        
                        Example:
                            >>> cone = Cone(Point(0.0, 0.0, 0.0), np.array([0.0, 0.0, 1.0]), Angle.degrees(30.0))
                            >>> transformation = Translation([1.0, 2.0, 3.0])
                            >>> cone.apply_transformation(transformation)
        """
    @typing.overload
    def contains(self, point: Point) -> bool:
        """
                        Check if the cone contains a point.
        
                        Args:
                            point (Point): The point to check.
        
                        Returns:
                            bool: True if the cone contains the point, False otherwise.
        
                        Example:
                            >>> cone = Cone(Point(0.0, 0.0, 0.0), np.array([0.0, 0.0, 1.0]), Angle.degrees(30.0))
                            >>> cone.contains(Point(0.1, 0.1, 1.0))  # True for point inside cone
        """
    @typing.overload
    def contains(self, point_set: PointSet) -> bool:
        """
                        Check if the cone contains a point set.
        
                        Args:
                            point_set (PointSet): The point set to check.
        
                        Returns:
                            bool: True if the cone contains the point set, False otherwise.
        
                        Example:
                            >>> cone = Cone(Point(0.0, 0.0, 0.0), np.array([0.0, 0.0, 1.0]), Angle.degrees(30.0))
                            >>> cone.contains(PointSet([Point(0.1, 0.1, 1.0), Point(0.2, 0.2, 1.0)]))  # True for points inside cone
        """
    @typing.overload
    def contains(self, segment: Segment) -> bool:
        """
                        Check if the cone contains a segment.
        
                        Args:
                            segment (Segment): The segment to check.
                    
                        Returns:
                            bool: True if the cone contains the segment, False otherwise.
        
                        Example:
                            >>> cone = Cone(Point(0.0, 0.0, 0.0), np.array([0.0, 0.0, 1.0]), Angle.degrees(30.0))
                            >>> cone.contains(Segment(Point(0.1, 0.1, 1.0), Point(0.2, 0.2, 1.0)))  # True for segment inside cone
        """
    @typing.overload
    def contains(self, ray: Ray) -> bool:
        """
                        Check if the cone contains a ray.
        
                        Args:
                            ray (Ray): The ray to check.
        
                        Returns:
                            bool: True if the cone contains the ray, False otherwise.
        
                        Example:
                            >>> cone = Cone(Point(0.0, 0.0, 0.0), np.array([0.0, 0.0, 1.0]), Angle.degrees(30.0))
                            >>> cone.contains(Ray(Point(0.1, 0.1, 1.0), np.array([0.0, 0.0, 1.0])))  # True for ray inside cone
        """
    @typing.overload
    def contains(self, sphere: Sphere) -> bool:
        """
                        Check if the cone contains a sphere.
        
                        Args:
                            sphere (Sphere): The sphere to check.
        
                        Returns:
                            bool: True if the cone contains the sphere, False otherwise.
        
                        Example:
                            >>> cone = Cone(Point(0.0, 0.0, 0.0), np.array([0.0, 0.0, 1.0]), Angle.degrees(30.0))
                            >>> cone.contains(Sphere(Point(0.1, 0.1, 1.0), 0.1))  # True for sphere inside cone
        """
    @typing.overload
    def contains(self, ellipsoid: Ellipsoid) -> bool:
        """
                        Check if the cone contains an ellipsoid.
                        Args:
                            ellipsoid (Ellipsoid): The ellipsoid to check.
        
                        Returns:
                            bool: True if the cone contains the ellipsoid, False otherwise.
                        
                        Example:
                            >>> cone = Cone(Point(0.0, 0.0, 0.0), np.array([0.0, 0.0, 1.0]), Angle.degrees(30.0))
                            >>> cone.contains(Ellipsoid(Point(0.1, 0.1, 1.0), 0.1, 0.1, 0.1))  # True for ellipsoid inside cone
        """
    def distance_to(self, point: Point) -> ostk.core.type.Real:
        """
                        Calculate the distance from the cone to a point.
        
                        Args:
                            point (Point): The point to calculate distance to.
        
                        Returns:
                            float: The minimum distance from the cone surface to the point.
        
                        Example:
                            >>> cone = Cone(Point(0.0, 0.0, 0.0), np.array([0.0, 0.0, 1.0]), Angle.degrees(30.0))
                            >>> distance = cone.distance_to(Point(2.0, 0.0, 0.0))
        """
    def get_angle(self) -> ...:
        """
                        Get the half-angle of the cone opening.
        
                        Returns:
                            Angle: The half-angle of the cone.
        
                        Example:
                            >>> cone = Cone(Point(0.0, 0.0, 0.0), np.array([0.0, 0.0, 1.0]), Angle.degrees(30.0))
                            >>> angle = cone.get_angle()  # 30 degrees
        """
    def get_apex(self) -> Point:
        """
                        Get the apex (tip) point of the cone.
        
                        Returns:
                            Point: The apex point of the cone.
        
                        Example:
                            >>> cone = Cone(Point(1.0, 2.0, 3.0), np.array([0.0, 0.0, 1.0]), Angle.degrees(30.0))
                            >>> apex = cone.get_apex()  # Point(1.0, 2.0, 3.0)
        """
    def get_axis(self) -> numpy.ndarray[numpy.float64[3, 1]]:
        """
                        Get the axis direction vector of the cone.
        
                        Returns:
                            Vector3d: The axis direction vector.
        
                        Example:
                            >>> cone = Cone(Point(0.0, 0.0, 0.0), np.array([0.0, 0.0, 1.0]), Angle.degrees(30.0))
                            >>> axis = cone.get_axis()  # [0.0, 0.0, 1.0]
        """
    def get_rays_of_lateral_surface(self, ray_count: int = 0) -> list[Ray]:
        """
                        Get rays representing the lateral surface of the cone.
        
                        Args:
                            ray_count (int): Number of rays to generate around the surface.
        
                        Returns:
                            list: Array of Ray objects representing the lateral surface.
        
                        Example:
                            >>> cone = Cone(Point(0.0, 0.0, 0.0), np.array([0.0, 0.0, 1.0]), Angle.degrees(30.0))
                            >>> rays = cone.get_rays_of_lateral_surface(8)
        """
    @typing.overload
    def intersection_with(self, sphere: Sphere, only_in_sight: bool = False, discretization_level: int = 40) -> ...:
        """
                        Compute intersection of cone with sphere.
        
                        Args:
                            sphere (Sphere): The sphere to intersect with.
                            only_in_sight (bool): If true, only return intersection points that are in sight.
                            discretization_level (int): The discretization level for the intersection.
        
                        Returns:
                            Intersection: The intersection of the cone with the sphere.
        
                        Example:
                            >>> cone = Cone(Point(0.0, 0.0, 0.0), np.array([0.0, 0.0, 1.0]), Angle.degrees(30.0))
                            >>> sphere = Sphere(Point(2.0, 0.0, 0.0), 1.0)
                            >>> intersection = cone.intersection_with(sphere)
                            >>> intersection.get_point()  # Point(2.0, 0.0, 0.0)
        """
    @typing.overload
    def intersection_with(self, ellipsoid: Ellipsoid, only_in_sight: bool = False, discretization_level: int = 40) -> ...:
        """
                        Compute intersection of cone with ellipsoid.
        
                        Args:
                            ellipsoid (Ellipsoid): The ellipsoid to intersect with.
                            only_in_sight (bool): If true, only return intersection points that are in sight.
                            discretization_level (int): The discretization level for the intersection.
        
                        Returns:
                            Intersection: The intersection of the cone with the ellipsoid.
        
                        Example:
                            >>> cone = Cone(Point(0.0, 0.0, 0.0), np.array([0.0, 0.0, 1.0]), Angle.degrees(30.0))
                            >>> ellipsoid = Ellipsoid(Point(2.0, 0.0, 0.0), 1.0, 1.0, 1.0)
                            >>> intersection = cone.intersection_with(ellipsoid)
                            >>> intersection.get_point()  # Point(2.0, 0.0, 0.0)
        """
    @typing.overload
    def intersects(self, sphere: Sphere, discretization_level: int = 40) -> bool:
        """
                        Check if the cone intersects with a sphere.
        
                        Args:
                            sphere (Sphere): The sphere to check intersection with.
                            discretization_level (int): Level of discretization for intersection calculation.
        
                        Returns:
                            bool: True if the cone intersects the sphere, False otherwise.
        
                        Example:
                            >>> cone = Cone(Point(0.0, 0.0, 0.0), np.array([0.0, 0.0, 1.0]), Angle.degrees(30.0))
                            >>> sphere = Sphere(Point(1.0, 0.0, 1.0), 0.5)
                            >>> cone.intersects(sphere)
        """
    @typing.overload
    def intersects(self, ellipsoid: Ellipsoid, discretization_level: int = 40) -> bool:
        """
                        Check if the cone intersects with an ellipsoid.
        
                        Args:
                            ellipsoid (Ellipsoid): The ellipsoid to check intersection with.
                            discretization_level (int): Level of discretization for intersection calculation.
        
                        Returns:
                            bool: True if the cone intersects the ellipsoid, False otherwise.
        
                        Example:
                            >>> cone = Cone(Point(0.0, 0.0, 0.0), np.array([0.0, 0.0, 1.0]), Angle.degrees(30.0))
                            >>> ellipsoid = Ellipsoid(Point(1.0, 0.0, 1.0), 1.0, 0.8, 0.6)
                            >>> cone.intersects(ellipsoid)
        """
    def is_defined(self) -> bool:
        """
                        Check if the cone is defined.
        
                        Returns:
                            bool: True if the cone is defined, False otherwise.
        
                        Example:
                            >>> cone = Cone(Point(0.0, 0.0, 0.0), np.array([0.0, 0.0, 1.0]), Angle.degrees(30.0))
                            >>> cone.is_defined()  # True
        """
class Cuboid(ostk.mathematics.geometry.d3.Object):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def cube(center: Point, extent: ostk.core.type.Real) -> Cuboid:
        """
                        Create a cube (equal extents along all axes) centered at a point.
        
                        Args:
                            center (Point): The center point of the cube.
                            extent (float): The half-extent along all axes.
        
                        Returns:
                            Cuboid: A cuboid representing a cube.
        
                        Example:
                            >>> center = Point(0.0, 0.0, 0.0)
                            >>> cube = Cuboid.cube(center, 1.0)  # 2x2x2 cube
        """
    @staticmethod
    def undefined() -> Cuboid:
        """
                        Create an undefined cuboid.
        
                        Returns:
                            Cuboid: An undefined cuboid object.
        
                        Example:
                            >>> undefined_cuboid = Cuboid.undefined()
                            >>> undefined_cuboid.is_defined()  # False
        """
    def __eq__(self, arg0: Cuboid) -> bool:
        ...
    def __init__(self, center: Point, axes: list, extent: list) -> None:
        """
                        Create a 3D cuboid with specified center, axes, and extents.
        
                        Args:
                            center (Point): The center point of the cuboid.
                            axes (list): List of three Vector3d objects defining the cuboid's orientation.
                            extent (list): List of three float values defining the half-extents along each axis.
        
                        Example:
                            >>> center = Point(0.0, 0.0, 0.0)
                            >>> axes = [np.array([1.0, 0.0, 0.0]), np.array([0.0, 1.0, 0.0]), np.array([0.0, 0.0, 1.0])]
                            >>> extent = [1.0, 2.0, 3.0]
                            >>> cuboid = Cuboid(center, axes, extent)
        """
    def __ne__(self, arg0: Cuboid) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __str__(self) -> str:
        ...
    def apply_transformation(self, transformation: typing.Any) -> None:
        """
                        Apply a transformation to the cuboid in place.
        
                        Args:
                            transformation (Transformation): The transformation to apply.
        
                        Example:
                            >>> cuboid = Cuboid(center, axes, extent)
                            >>> transformation = Translation([1.0, 2.0, 3.0])
                            >>> cuboid.apply_transformation(transformation)
        """
    def get_center(self) -> Point:
        """
                        Get the center point of the cuboid.
        
                        Returns:
                            Point: The center point of the cuboid.
        
                        Example:
                            >>> cuboid = Cuboid(Point(1.0, 2.0, 3.0), axes, extent)
                            >>> center = cuboid.get_center()  # Point(1.0, 2.0, 3.0)
        """
    def get_first_axis(self) -> numpy.ndarray[numpy.float64[3, 1]]:
        """
                        Get the first axis vector of the cuboid.
        
                        Returns:
                            Vector3d: The first axis direction vector.
        
                        Example:
                            >>> cuboid = Cuboid(center, axes, extent)
                            >>> first_axis = cuboid.get_first_axis()
        """
    def get_first_extent(self) -> ostk.core.type.Real:
        """
                        Get the first half-extent of the cuboid.
        
                        Returns:
                            float: The half-extent along the first axis.
        
                        Example:
                            >>> cuboid = Cuboid(center, axes, [1.0, 2.0, 3.0])
                            >>> first_extent = cuboid.get_first_extent()  # 1.0
        """
    def get_second_axis(self) -> numpy.ndarray[numpy.float64[3, 1]]:
        """
                        Get the second axis vector of the cuboid.
        
                        Returns:
                            Vector3d: The second axis direction vector.
        
                        Example:
                            >>> cuboid = Cuboid(center, axes, extent)
                            >>> second_axis = cuboid.get_second_axis()
        """
    def get_second_extent(self) -> ostk.core.type.Real:
        """
                        Get the second half-extent of the cuboid.
        
                        Returns:
                            float: The half-extent along the second axis.
        
                        Example:
                            >>> cuboid = Cuboid(center, axes, [1.0, 2.0, 3.0])
                            >>> second_extent = cuboid.get_second_extent()  # 2.0
        """
    def get_third_axis(self) -> numpy.ndarray[numpy.float64[3, 1]]:
        """
                        Get the third axis vector of the cuboid.
        
                        Returns:
                            Vector3d: The third axis direction vector.
        
                        Example:
                            >>> cuboid = Cuboid(center, axes, extent)
                            >>> third_axis = cuboid.get_third_axis()
        """
    def get_third_extent(self) -> ostk.core.type.Real:
        """
                        Get the third half-extent of the cuboid.
        
                        Returns:
                            float: The half-extent along the third axis.
        
                        Example:
                            >>> cuboid = Cuboid(center, axes, [1.0, 2.0, 3.0])
                            >>> third_extent = cuboid.get_third_extent()  # 3.0
        """
    def get_vertices(self) -> list[Point]:
        """
                        Get all vertices of the cuboid.
        
                        Returns:
                            list: Array of Point objects representing the 8 vertices of the cuboid.
        
                        Example:
                            >>> cuboid = Cuboid(center, axes, extent)
                            >>> vertices = cuboid.get_vertices()  # 8 corner points
        """
    @typing.overload
    def intersects(self, point: Point) -> bool:
        """
                        Check if the cuboid intersects a point.
        
                        Args:
                            point (Point): The point to check.
        
                        Returns:
                            bool: True if the cuboid intersects the point, False otherwise.
        
                        Example:
                            >>> cuboid = Cuboid(Point(0.0, 0.0, 0.0), axes, extent)
                            >>> cuboid.intersects(Point(1.0, 2.0, 3.0))  # True
        """
    @typing.overload
    def intersects(self, point_set: PointSet) -> bool:
        """
                        Check if the cuboid intersects a point set.
        
                        Args:
                            point_set (PointSet): The point set to check.
        
                        Returns:
                            bool: True if the cuboid intersects the point set, False otherwise.
        
                        Example:
                            >>> cuboid = Cuboid(Point(0.0, 0.0, 0.0), axes, extent)
                            >>> cuboid.intersects(PointSet([Point(1.0, 2.0, 3.0), Point(4.0, 5.0, 6.0)]))  # True
        """
    @typing.overload
    def intersects(self, line: Line) -> bool:
        """
                        Check if the cuboid intersects a line.
        
                        Args:
                            line (Line): The line to check.
        
                        Returns:
                            bool: True if the cuboid intersects the line, False otherwise.
        
                        Example:
                            >>> cuboid = Cuboid(Point(0.0, 0.0, 0.0), axes, extent)
                            >>> cuboid.intersects(Line(Point(1.0, 2.0, 3.0), Point(4.0, 5.0, 6.0)))  # True
        """
    @typing.overload
    def intersects(self, cuboid: Cuboid) -> bool:
        """
                        Check if the cuboid intersects a cuboid.
        
                        Args:
                            cuboid (Cuboid): The cuboid to check.
        
                        Returns:
                            bool: True if the cuboid intersects the cuboid, False otherwise.
        """
    def is_defined(self) -> bool:
        """
                        Check if the cuboid is defined.
        
                        Returns:
                            bool: True if the cuboid is defined, False otherwise.
        
                        Example:
                            >>> cuboid = Cuboid(center, axes, extent)
                            >>> cuboid.is_defined()  # True
        """
    def is_near(self, arg0: Cuboid, arg1: ostk.core.type.Real) -> bool:
        """
                        Check if this cuboid is near another cuboid.
        
                        Args:
                            cuboid (Cuboid): The cuboid to compare with.
                            tolerance (float): The tolerance for comparison.
        
                        Returns:
                            bool: True if cuboids are within tolerance, False otherwise.
        
                        Example:
                            >>> cuboid1 = Cuboid(center1, axes1, extent1)
                            >>> cuboid2 = Cuboid(center2, axes2, extent2)
                            >>> cuboid1.is_near(cuboid2, 1e-6)
        """
class Ellipsoid(ostk.mathematics.geometry.d3.Object):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def undefined() -> Ellipsoid:
        """
                        Create an undefined ellipsoid.
        
                        Returns:
                            Ellipsoid: An undefined ellipsoid object.
        
                        Example:
                            >>> undefined_ellipsoid = Ellipsoid.undefined()
                            >>> undefined_ellipsoid.is_defined()  # False
        """
    def __eq__(self, arg0: Ellipsoid) -> bool:
        ...
    @typing.overload
    def __init__(self, center: Point, first_principal_semi_axis: ostk.core.type.Real, second_principal_semi_axis: ostk.core.type.Real, third_principal_semi_axis: ostk.core.type.Real) -> None:
        """
                        Create an ellipsoid with specified center and semi-axes.
        
                        Args:
                            center (Point): The center point of the ellipsoid.
                            first_principal_semi_axis (float): The first principal semi-axis length.
                            second_principal_semi_axis (float): The second principal semi-axis length.
                            third_principal_semi_axis (float): The third principal semi-axis length.
        
                        Example:
                            >>> center = Point(0.0, 0.0, 0.0)
                            >>> ellipsoid = Ellipsoid(center, 2.0, 1.5, 1.0)
        """
    @typing.overload
    def __init__(self, center: Point, first_principal_semi_axis: ostk.core.type.Real, second_principal_semi_axis: ostk.core.type.Real, third_principal_semi_axis: ostk.core.type.Real, orientation: typing.Any) -> None:
        """
                        Create an ellipsoid with specified center, semi-axes, and orientation.
        
                        Args:
                            center (Point): The center point of the ellipsoid.
                            first_principal_semi_axis (float): The first principal semi-axis length.
                            second_principal_semi_axis (float): The second principal semi-axis length.
                            third_principal_semi_axis (float): The third principal semi-axis length.
                            orientation (Quaternion): The orientation of the ellipsoid.
        
                        Example:
                            >>> center = Point(0.0, 0.0, 0.0)
                            >>> orientation = Quaternion.unit()
                            >>> ellipsoid = Ellipsoid(center, 2.0, 1.5, 1.0, orientation)
        """
    def __ne__(self, arg0: Ellipsoid) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __str__(self) -> str:
        ...
    def apply_transformation(self, transformation: typing.Any) -> None:
        """
                        Apply a transformation to the ellipsoid in place.
        
                        Args:
                            transformation (Transformation): The transformation to apply.
        
                        Example:
                            >>> ellipsoid = Ellipsoid(center, 2.0, 1.5, 1.0)
                            >>> transformation = Translation([1.0, 2.0, 3.0])
                            >>> ellipsoid.apply_transformation(transformation)
        """
    @typing.overload
    def contains(self, point: Point) -> bool:
        """
                        Check if the ellipsoid contains a point.
        
                        Args:
                            point (Point): The point to check.
        
                        Returns:
                            bool: True if the ellipsoid contains the point, False otherwise.
        
                        Example:
                            >>> ellipsoid = Ellipsoid(Point(0.0, 0.0, 0.0), 2.0, 1.5, 1.0)
                            >>> ellipsoid.contains(Point(0.5, 0.5, 0.5))  # True if inside
        """
    @typing.overload
    def contains(self, point_set: PointSet) -> bool:
        """
                        Check if the ellipsoid contains a point set.
        
                        Args:
                            point_set (PointSet): The point set to check.
        
                        Returns:
                            bool: True if the ellipsoid contains the point set, False otherwise.
        
                        Example:
                            >>> ellipsoid = Ellipsoid(Point(0.0, 0.0, 0.0), 2.0, 1.5, 1.0)
                            >>> ellipsoid.contains(PointSet([Point(0.5, 0.5, 0.5), Point(1.0, 1.0, 1.0)]))  # True if inside
        """
    @typing.overload
    def contains(self, segment: Segment) -> bool:
        """
                        Check if the ellipsoid contains a segment.
        
                        Args:
                            segment (Segment): The segment to check.
        
                        Returns:
                            bool: True if the ellipsoid contains the segment, False otherwise.
        
                        Example:
                            >>> ellipsoid = Ellipsoid(Point(0.0, 0.0, 0.0), 2.0, 1.5, 1.0)
                            >>> ellipsoid.contains(Segment(Point(0.5, 0.5, 0.5), Point(1.0, 1.0, 1.0)))  # True if inside
        """
    def get_center(self) -> Point:
        """
                        Get the center point of the ellipsoid.
        
                        Returns:
                            Point: The center point of the ellipsoid.
        
                        Example:
                            >>> ellipsoid = Ellipsoid(Point(1.0, 2.0, 3.0), 2.0, 1.5, 1.0)
                            >>> center = ellipsoid.get_center()  # Point(1.0, 2.0, 3.0)
        """
    def get_first_axis(self) -> numpy.ndarray[numpy.float64[3, 1]]:
        """
                        Get the first axis of the ellipsoid.
        
                        Returns:
                            np.array: The first axis of the ellipsoid.
        
                        Example:
                            >>> ellipsoid = Ellipsoid(center, 2.0, 1.5, 1.0)
                            >>> first_axis = ellipsoid.get_first_axis()  # np.array([1.0, 0.0, 0.0])
        """
    def get_first_principal_semi_axis(self) -> ostk.core.type.Real:
        """
                        Get the first principal semi-axis length.
        
                        Returns:
                            float: The length of the first principal semi-axis.
        
                        Example:
                            >>> ellipsoid = Ellipsoid(center, 2.0, 1.5, 1.0)
                            >>> first_axis = ellipsoid.get_first_principal_semi_axis()  # 2.0
        """
    def get_matrix(self) -> numpy.ndarray[numpy.float64[3, 3]]:
        """
                        Get the matrix of the ellipsoid.
        
                        Returns:
                            np.array: The matrix of the ellipsoid.
        
                        Example:
                            >>> ellipsoid = Ellipsoid(center, 2.0, 1.5, 1.0)
                            >>> matrix = ellipsoid.get_matrix()  # np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])
        """
    def get_orientation(self) -> ...:
        """
                        Get the orientation quaternion of the ellipsoid.
        
                        Returns:
                            Quaternion: The orientation quaternion of the ellipsoid.
        
                        Example:
                            >>> ellipsoid = Ellipsoid(center, 2.0, 1.5, 1.0, orientation)
                            >>> quat = ellipsoid.get_orientation()
        """
    def get_second_axis(self) -> numpy.ndarray[numpy.float64[3, 1]]:
        """
                        Get the second axis of the ellipsoid.
        
                        Returns:
                            np.array: The second axis of the ellipsoid.
        
                        Example:
                            >>> ellipsoid = Ellipsoid(center, 2.0, 1.5, 1.0)
                            >>> second_axis = ellipsoid.get_second_axis()  # np.array([0.0, 1.0, 0.0])
        """
    def get_second_principal_semi_axis(self) -> ostk.core.type.Real:
        """
                        Get the second principal semi-axis length.
        
                        Returns:
                            float: The length of the second principal semi-axis.
        
                        Example:
                            >>> ellipsoid = Ellipsoid(center, 2.0, 1.5, 1.0)
                            >>> second_axis = ellipsoid.get_second_principal_semi_axis()  # 1.5
        """
    def get_third_axis(self) -> numpy.ndarray[numpy.float64[3, 1]]:
        """
                        Get the third axis of the ellipsoid.
        
                        Returns:
                            np.array: The third axis of the ellipsoid.
        
                        Example:
                            >>> ellipsoid = Ellipsoid(center, 2.0, 1.5, 1.0)
                            >>> third_axis = ellipsoid.get_third_axis()  # np.array([0.0, 0.0, 1.0])
        """
    def get_third_principal_semi_axis(self) -> ostk.core.type.Real:
        """
                        Get the third principal semi-axis length.
        
                        Returns:
                            float: The length of the third principal semi-axis.
        
                        Example:
                            >>> ellipsoid = Ellipsoid(center, 2.0, 1.5, 1.0)
                            >>> third_axis = ellipsoid.get_third_principal_semi_axis()  # 1.0
        """
    @typing.overload
    def intersection(self, line: Line) -> ...:
        ...
    @typing.overload
    def intersection(self, ray: Ray, only_in_sight: bool) -> ...:
        ...
    @typing.overload
    def intersection(self, segment: Segment) -> ...:
        ...
    @typing.overload
    def intersection(self, pyramid: typing.Any, only_in_sight: bool) -> ...:
        ...
    @typing.overload
    def intersection(self, cone: typing.Any, only_in_sight: bool) -> ...:
        ...
    @typing.overload
    def intersection_with(self, line: Line) -> ...:
        """
                        Get the intersection of the ellipsoid with a line.
        
                        Args:
                            line (Line): The line to intersect with.
        
                        Returns:
                            Intersection: The intersection of the ellipsoid with the line.
        
                        Example:
                            >>> ellipsoid = Ellipsoid(center, 2.0, 1.5, 1.0)
                            >>> line = Line.points(Point(0.0, 0.0, 0.0), Point(1.0, 0.0, 0.0))
                            >>> intersection = ellipsoid.intersection_with(line)
                            >>> intersection.get_point()  # Point(0.0, 0.0, 0.0)
        """
    @typing.overload
    def intersection_with(self, ray: Ray, only_in_sight: bool = False) -> ...:
        """
                        Get the intersection of the ellipsoid with a ray.
        
                        Args:
                            ray (Ray): The ray to intersect with.
                            only_in_sight (bool, optional): If true, only return intersection points that are in sight. Defaults to False.
        
                        Returns:
                            Intersection: The intersection of the ellipsoid with the ray.
        
                        Example:
                            >>> ellipsoid = Ellipsoid(center, 2.0, 1.5, 1.0)
                            >>> ray = Ray(Point(0.0, 0.0, 0.0), Point(1.0, 0.0, 0.0))
                            >>> intersection = ellipsoid.intersection_with(ray)
                            >>> intersection.get_point()  # Point(0.0, 0.0, 0.0)
        """
    @typing.overload
    def intersection_with(self, segment: Segment) -> ...:
        """
                        Get the intersection of the ellipsoid with a segment.
        
                        Args:
                            segment (Segment): The segment to intersect with.
        
                        Returns:
                            Intersection: The intersection of the ellipsoid with the segment.
        
                        Example:
                            >>> ellipsoid = Ellipsoid(center, 2.0, 1.5, 1.0)
                            >>> segment = Segment(Point(0.0, 0.0, 0.0), Point(1.0, 0.0, 0.0))
                            >>> intersection = ellipsoid.intersection_with(segment)
                            >>> intersection.get_point()  # Point(0.0, 0.0, 0.0)
        """
    @typing.overload
    def intersection_with(self, pyramid: typing.Any, only_in_sight: bool = False) -> ...:
        """
                        Get the intersection of the ellipsoid with a pyramid.
        
                        Args:
                            pyramid (Pyramid): The pyramid to intersect with.
                            only_in_sight (bool, optional): If true, only return intersection points that are in sight. Defaults to False.
        
                        Returns:
                            Intersection: The intersection of the ellipsoid with the pyramid.
        
                        Example:
                            >>> origin = Point(0.0, 0.0, 0.0)
                            >>> ellipsoid = Ellipsoid(origin, 2.0, 1.5, 1.0)
                            >>> polygon2d = Polygon2d([Point2d(0.0, 0.0), Point2d(1.0, 0.0), Point2d(1.0, 1.0), Point2d(0.0, 1.0)])
                            >>> x_axis = np.array([1.0, 0.0, 0.0])
                            >>> y_axis = np.array([0.0, 1.0, 0.0])
                            >>> polygon = Polygon(polygon2d, origin, x_axis, y_axis)
                            >>> pyramid = Pyramid(polygon, Point(0.0, 0.0, 1.0))
                            >>> intersection = ellipsoid.intersection_with(pyramid)
                            >>> intersection.get_point()
        """
    @typing.overload
    def intersection_with(self, cone: typing.Any, only_in_sight: bool = False) -> ...:
        """
                        Get the intersection of the ellipsoid with a cone.
        
                        Args:
                            cone (Cone): The cone to intersect with.
                            only_in_sight (bool, optional): If true, only return intersection points that are in sight. Defaults to False.
        
                        Returns:
                            Intersection: The intersection of the ellipsoid with the cone.
        
                        Example:
                            >>> ellipsoid = Ellipsoid(center, 2.0, 1.5, 1.0)
                            >>> cone = Cone(Point(0.0, 0.0, 0.0), [1.0, 0.0, 0.0], Angle.degrees(30.0))
                            >>> intersection = ellipsoid.intersection_with(cone)
                            >>> intersection.get_point()
        """
    @typing.overload
    def intersects(self, point: Point) -> bool:
        """
                        Check if the ellipsoid intersects a point.
        
                        Args:
                            point (Point): The point to check.
        
                        Returns:
                            bool: True if the ellipsoid intersects the point, False otherwise.
        
                        Example:
                            >>> ellipsoid = Ellipsoid(Point(0.0, 0.0, 0.0), 2.0, 1.5, 1.0)
                            >>> ellipsoid.intersects(Point(0.5, 0.5, 0.5))  # True
        """
    @typing.overload
    def intersects(self, point_set: PointSet) -> bool:
        """
                        Check if the ellipsoid intersects a point set.
        
                        Args:
                            point_set (PointSet): The point set to check.
        
                        Returns:
                            bool: True if the ellipsoid intersects the point set, False otherwise.
        
                        Example:
                            >>> ellipsoid = Ellipsoid(Point(0.0, 0.0, 0.0), 2.0, 1.5, 1.0)
                            >>> ellipsoid.intersects(PointSet([Point(0.5, 0.5, 0.5), Point(1.0, 1.0, 1.0)]))  # True
        """
    @typing.overload
    def intersects(self, line: Line) -> bool:
        """
                        Check if the ellipsoid intersects a line.
        
                        Args:
                            line (Line): The line to check.
        
                        Returns:
                            bool: True if the ellipsoid intersects the line, False otherwise.
        
                        Example:
                            >>> ellipsoid = Ellipsoid(Point(0.0, 0.0, 0.0), 2.0, 1.5, 1.0)
                            >>> ellipsoid.intersects(Line.points(Point(0.5, 0.5, 0.5), Point(1.0, 1.0, 1.0)))  # True
        """
    @typing.overload
    def intersects(self, ray: Ray) -> bool:
        """
                        Check if the ellipsoid intersects a ray.
        
                        Args:
                            ray (Ray): The ray to check.
        
                        Returns:
                            bool: True if the ellipsoid intersects the ray, False otherwise.
        
                        Example:
                            >>> ellipsoid = Ellipsoid(Point(0.0, 0.0, 0.0), 2.0, 1.5, 1.0)
                            >>> ellipsoid.intersects(Ray(Point(0.5, 0.5, 0.5), [1.0, 0.0, 0.0]))  # True
        """
    @typing.overload
    def intersects(self, segment: Segment) -> bool:
        """
                        Check if the ellipsoid intersects a segment.
        
                        Args:
                            segment (Segment): The segment to check.
        
                        Returns:
                            bool: True if the ellipsoid intersects the segment, False otherwise.
        
                        Example:
                            >>> ellipsoid = Ellipsoid(Point(0.0, 0.0, 0.0), 2.0, 1.5, 1.0)
                            >>> ellipsoid.intersects(Segment(Point(0.5, 0.5, 0.5), Point(1.0, 1.0, 1.0)))  # True
        """
    @typing.overload
    def intersects(self, plane: Plane) -> bool:
        """
                        Check if the ellipsoid intersects a plane.
        
                        Args:
                            plane (Plane): The plane to check.
        
                        Returns:
                            bool: True if the ellipsoid intersects the plane, False otherwise.
        
                        Example:
                            >>> ellipsoid = Ellipsoid(Point(0.0, 0.0, 0.0), 2.0, 1.5, 1.0)
                            >>> ellipsoid.intersects(Plane(Point(0.5, 0.5, 0.5), Vector3d(1.0, 1.0, 1.0)))  # True
        """
    def is_defined(self) -> bool:
        """
                        Check if the ellipsoid is defined.
        
                        Returns:
                            bool: True if the ellipsoid is defined, False otherwise.
        
                        Example:
                            >>> ellipsoid = Ellipsoid(center, 2.0, 1.5, 1.0)
                            >>> ellipsoid.is_defined()  # True
        """
class Line(ostk.mathematics.geometry.d3.Object):
    """
    
                    An infinite line in 3D space.
    
                    A Line is defined by an origin point and a direction vector.
    
                    Example:
                        >>> line = Line.points(Point(0.0, 0.0), Point(1.0, 0.0))
                        >>> line.is_defined()  # True
                
    """
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
                            >>> line.is_defined()  # True
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
    def __init__(self, origin: Point, direction: numpy.ndarray[numpy.float64[3, 1]]) -> None:
        """
                        Construct a line from an origin point and direction vector.
        
                        Args:
                            origin (Point): A point on the line.
                            direction (numpy.ndarray): The direction vector of the line.
        
                        Example:
                            >>> line = Line.points(Point(0.0, 0.0), Point(1.0, 0.0))
                            >>> line.is_defined()  # True
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
                            bool: True if the line contains the point.
        
                        Example:
                            >>> line = Line.points(Point(0.0, 0.0), Point(1.0, 0.0))
                            >>> line.contains(Point(0.5, 0.5))  # True
        """
    @typing.overload
    def contains(self, point_set: PointSet) -> bool:
        """
                        Check if the line contains all points in a point set.
        
                        Args:
                            point_set (PointSet): The point set to check.
        
                        Returns:
                            bool: True if the line contains all points.
                        
                        Example:
                            >>> line = Line.points(Point(0.0, 0.0), Point(1.0, 0.0))
                            >>> points = PointSet([Point(0.5, 0.5), Point(0.25, 0.25)])
                            >>> line.contains(points)  # True
        """
    def distance_to(self, point: Point) -> ostk.core.type.Real:
        """
                        Calculate the distance from the line to a point.
        
                        Args:
                            point (Point): The point to measure distance to.
        
                        Returns:
                            float: The distance to the point.
        
                        Example:
                            >>> line = Line.points(Point(0.0, 0.0), Point(1.0, 0.0))
                            >>> distance = line.distance_to(Point(0.5, 1.0))  # 1.0
        """
    def get_direction(self) -> numpy.ndarray[numpy.float64[3, 1]]:
        """
                        Get the direction vector of the line.
        
                        Returns:
                            numpy.ndarray: The direction vector.
                        
                        Example:
                            >>> line = Line.points(Point(0.0, 0.0), Point(1.0, 0.0))
                            >>> direction = line.get_direction()  # [1.0, 0.0, 0.0]
        """
    def get_origin(self) -> Point:
        """
                        Get the origin point of the line.
        
                        Returns:
                            Point: The origin point.
        
                        Example:
                            >>> line = Line.points(Point(0.0, 0.0), Point(1.0, 0.0))
                            >>> origin = line.get_origin()  # Point(0.0, 0.0, 0.0)
        """
    def intersection_with(self, plane: typing.Any) -> ...:
        """
                        Compute the intersection of the line with a plane.
        
                        Args:
                            plane (Plane): The plane to intersect with.
        
                        Returns:
                            Intersection: The intersection result.
        
                        Example:
                            >>> line = Line.points(Point(0.0, 0.0), Point(1.0, 0.0))
                            >>> plane = Plane(Point(1.0, 0.0, 0.0), Vector3d(0.0, 0.0, 1.0))
                            >>> intersection = line.intersection_with(plane)
                            >>> intersection.get_point()  # Point(1.0, 0.0, 0.0)
        """
    @typing.overload
    def intersects(self, point: Point) -> bool:
        """
                        Check if the line intersects a point.
        
                        Args:
                            point (Point): The point to check intersection with.
        
                        Returns:
                            bool: True if the line intersects the point.
        
                        Example:
                            >>> line = Line.points(Point(0.0, 0.0), Point(1.0, 0.0))
                            >>> line.intersects(Point(0.5, 0.5))  # True
        """
    @typing.overload
    def intersects(self, plane: typing.Any) -> bool:
        """
                        Check if the line intersects a plane.
        
                        Args:
                            plane (Plane): The plane to check intersection with.
        
                        Returns:
                            bool: True if the line intersects the plane.
        
                        Example:
                            >>> line = Line.points(Point(0.0, 0.0), Point(1.0, 0.0))
                            >>> plane = Plane(Point(1.0, 0.0, 0.0), Vector3d(0.0, 0.0, 1.0))
                            >>> line.intersects(plane)  # True
        """
    @typing.overload
    def intersects(self, sphere: typing.Any) -> bool:
        """
                        Check if the line intersects a sphere.
        
                        Args:
                            sphere (Sphere): The sphere to check intersection with.
        
                        Returns:
                            bool: True if the line intersects the sphere.
        
                        Example:
                            >>> line = Line.points(Point(0.0, 0.0), Point(1.0, 0.0))
                            >>> sphere = Sphere(Point(1.0, 0.0, 0.0), 1.0)
                            >>> line.intersects(sphere)  # True
        """
    @typing.overload
    def intersects(self, ellipsoid: typing.Any) -> bool:
        """
                        Check if the line intersects an ellipsoid.
        
                        Args:
                            ellipsoid (Ellipsoid): The ellipsoid to check intersection with.
        
                        Returns:
                            bool: True if the line intersects the ellipsoid.
        
                        Example:
                            >>> line = Line.points(Point(0.0, 0.0), Point(1.0, 0.0))
                            >>> ellipsoid = Ellipsoid(Point(2.0, 0.0, 0.0), 1.0, 1.0, 1.0)
                            >>> line.intersects(ellipsoid)  # True
        """
    def is_defined(self) -> bool:
        """
                        Check if the line is defined.
        
                        Returns:
                            bool: True if the line is defined.
        
                        Example:
                            >>> line = Line.points(Point(0.0, 0.0), Point(1.0, 0.0))
                            >>> line.is_defined()  # True
        """
class LineString(ostk.mathematics.geometry.d3.Object):
    """
    
                    A sequence of connected line segments in 3D space.
    
                    A LineString is an ordered sequence of points forming a polyline.
    
                    Example:
                        >>> points = [Point(0.0, 0.0), Point(1.0, 1.0)]
                        >>> line_string = LineString(points)
                        >>> line_string.is_defined()  # True
                
    """
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def empty() -> LineString:
        """
                        Create an empty line string.
        
                        Returns:
                            LineString: An empty line string.
                    
                        Example:
                            >>> line_string = LineString.empty()
                            >>> line_string.is_empty()  # True
        """
    @staticmethod
    def segment(segment: Segment) -> LineString:
        """
                        Create a line string from a segment.
        
                        Args:
                            segment (Segment): The segment to convert.
        
                        Returns:
                            LineString: A line string representing the segment.
                        
                        Example:
                            >>> segment = Segment(Point(0.0, 0.0, 0.0), Point(1.0, 1.0, 1.0))
                            >>> line_string = LineString.segment(segment)
                            >>> line_string.is_defined()  # True
        """
    def __eq__(self, arg0: LineString) -> bool:
        ...
    def __getitem__(self, index: int) -> Point:
        ...
    def __init__(self, points: list[Point]) -> None:
        """
                        Construct a line string from an array of points.
                        
                        Args:
                        points (list[Point]): Array of 3D points defining the line string.
                        
                        Example:
                        >>> points = [Point(0.0, 0.0), Point(1.0, 1.0)]
                        >>> line_string = LineString(points)
                        >>> line_string.is_defined()  # True
        """
    def __iter__(self) -> typing.Iterator[Point]:
        ...
    def __len__(self) -> int:
        ...
    def __ne__(self, arg0: LineString) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __str__(self) -> str:
        ...
    def access_point_at(self, index: int) -> Point:
        """
                        Access a point at a given index.
        
                        Args:
                            index (int): The index of the point.
        
                        Returns:
                            Point: Reference to the point at the index.
        
                        Example:
                            >>> points = [Point(0.0, 0.0), Point(1.0, 1.0)]
                            >>> line_string = LineString(points)
                            >>> line_string.access_point_at(0)  # Point(0.0, 0.0)
        """
    def apply_transformation(self, transformation: typing.Any) -> None:
        """
                        Apply a transformation to all points in the line string.
                        
                        Args:
                            transformation (Transformation): The transformation to apply.
                        
                        Example:
                            >>> points = [Point(0.0, 0.0), Point(1.0, 1.0)]
                            >>> line_string = LineString(points)
                            >>> transformation = Transformation.translation([1.0, 0.0])
                            >>> line_string.apply_transformation(transformation)
        """
    def get_point_closest_to(self, point: Point) -> Point:
        """
                        Get the point in the line string closest to a given point.
        
                        Args:
                            point (Point): The reference point.
        
                        Returns:
                            Point: The closest point in the line string.
                        
                        Example:
                            >>> points = [Point(0.0, 0.0), Point(1.0, 1.0)]
                            >>> line_string = LineString(points)
                            >>> line_string.get_point_closest_to(Point(0.5, 0.5))  # Point(0.5, 0.5)
        """
    def get_point_count(self) -> int:
        """
                        Get the number of points in the line string.
        
                        Returns:
                            int: The number of points.
                        
                        Example:
                            >>> points = [Point(0.0, 0.0), Point(1.0, 1.0)]
                            >>> line_string = LineString(points)
                            >>> line_string.get_point_count()  # 2
        """
    def is_defined(self) -> bool:
        """
                        Check if the line string is defined.
        
                        Returns:
                            bool: True if the line string is defined.
        
                        Example:
                            >>> points = [Point(0.0, 0.0), Point(1.0, 1.0)]
                            >>> line_string = LineString(points)
                            >>> line_string.is_defined()  # True
        """
    def is_empty(self) -> bool:
        """
                        Check if the line string is empty.
        
                        Returns:
                            bool: True if the line string contains no points.
        
                        Example:
                            >>> line_string = LineString.empty()
                            >>> line_string.is_empty()  # True
        """
    def is_near(self, line_string: LineString, tolerance: ostk.core.type.Real) -> bool:
        """
                        Check if another line string is near this one within a tolerance.
                        
                        Args:
                        line_string (LineString): The line string to compare against.
                        tolerance (float): The maximum distance for points to be considered near.
                        
                        Returns:
                        bool: True if the line strings are near each other.
                        
                        Example:
                        >>> line_string = LineString(points)
                        >>> line_string.is_near(LineString(points), 0.1)  # True
        """
class Plane(ostk.mathematics.geometry.d3.Object):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def undefined() -> Plane:
        """
                        Create an undefined plane.
        
                        Returns:
                            Plane: An undefined plane.
        
                        Example:
                            >>> undefined_plane = Plane.undefined()
                            >>> undefined_plane.is_defined()  # False
        """
    def __eq__(self, arg0: Plane) -> bool:
        ...
    def __init__(self, point: Point, normal_vector: numpy.ndarray[numpy.float64[3, 1]]) -> None:
        """
                        Create a 3D plane from a point and normal vector.
        
                        Args:
                            point (Point): A point on the plane.
                            normal_vector (np.array): The normal vector to the plane.
        
                        Example:
                            >>> point = Point(0.0, 0.0, 0.0)
                            >>> normal = np.array([0.0, 0.0, 1.0])
                            >>> plane = Plane(point, normal)
        """
    def __ne__(self, arg0: Plane) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __str__(self) -> str:
        ...
    def apply_transformation(self, transformation: typing.Any) -> None:
        """
                        Apply a transformation to the plane.
        
                        Args:
                            transformation (Transformation): The transformation to apply.
        
                        Returns:
                            Plane: The transformed plane.
        
                        Example:
                            >>> plane = Plane(Point(0.0, 0.0, 0.0), np.array([0.0, 0.0, 1.0]))
                            >>> transformation = Transformation.identity()
                            >>> transformed = plane.apply_transformation(transformation)
        """
    @typing.overload
    def contains(self, point: Point) -> bool:
        """
                        Check if the plane contains a point.
        
                        Args:
                            point (Point): The point to check.
        
                        Returns:
                            bool: True if the plane contains the point, False otherwise.
        
                        Example:
                            >>> plane = Plane(Point(0.0, 0.0, 0.0), np.array([0.0, 0.0, 1.0]))
                            >>> plane.contains(Point(1.0, 1.0, 0.0))  # True (z=0 plane)
        """
    @typing.overload
    def contains(self, point_set: PointSet) -> bool:
        """
                        Check if the plane contains a point set.
        
                        Args:
                            point_set (PointSet): The point set to check.
        
                        Returns:
                            bool: True if the plane contains all points in the set, False otherwise.
        
                        Example:
                            >>> plane = Plane(Point(0.0, 0.0, 0.0), np.array([0.0, 0.0, 1.0]))
                            >>> points = PointSet([Point(1.0, 1.0, 0.0), Point(2.0, 2.0, 0.0)])
                            >>> plane.contains(points)  # True
        """
    @typing.overload
    def contains(self, line: Line) -> bool:
        """
                        Check if the plane contains a line.
        
                        Args:
                            line (Line): The line to check.
        
                        Returns:
                            bool: True if the plane contains the entire line, False otherwise.
        
                        Example:
                            >>> plane = Plane(Point(0.0, 0.0, 0.0), np.array([0.0, 0.0, 1.0]))
                            >>> line = Line(Point(0.0, 0.0, 0.0), np.array([1.0, 0.0, 0.0]))
                            >>> plane.contains(line)  # True (line lies in z=0 plane)
        """
    @typing.overload
    def contains(self, ray: Ray) -> bool:
        """
                        Check if the plane contains a ray.
        
                        Args:
                            ray (Ray): The ray to check.
        
                        Returns:
                            bool: True if the plane contains the entire ray, False otherwise.
        
                        Example:
                            >>> plane = Plane(Point(0.0, 0.0, 0.0), np.array([0.0, 0.0, 1.0]))
                            >>> ray = Ray(Point(0.0, 0.0, 0.0), np.array([1.0, 0.0, 0.0]))
                            >>> plane.contains(ray)  # True
        """
    @typing.overload
    def contains(self, segment: Segment) -> bool:
        """
                        Check if the plane contains a segment.
        
                        Args:
                            segment (Segment): The segment to check.
        
                        Returns:
                            bool: True if the plane contains the entire segment, False otherwise.
        
                        Example:
                            >>> plane = Plane(Point(0.0, 0.0, 0.0), np.array([0.0, 0.0, 1.0]))
                            >>> segment = Segment(Point(0.0, 0.0, 0.0), Point(1.0, 0.0, 0.0))
                            >>> plane.contains(segment)  # True
        """
    def get_normal_vector(self) -> numpy.ndarray[numpy.float64[3, 1]]:
        """
                        Get the normal vector of the plane.
        
                        Returns:
                            Vector3d: The normal vector to the plane.
        
                        Example:
                            >>> plane = Plane(Point(0.0, 0.0, 0.0), np.array([0.0, 0.0, 1.0]))
                            >>> normal = plane.get_normal_vector()  # [0.0, 0.0, 1.0]
        """
    def get_point(self) -> Point:
        """
                        Get a reference point on the plane.
        
                        Returns:
                            Point: A point on the plane.
        
                        Example:
                            >>> plane = Plane(Point(1.0, 2.0, 3.0), np.array([0.0, 0.0, 1.0]))
                            >>> point = plane.get_point()
        """
    @typing.overload
    def intersection_with(self, point: Point) -> ...:
        """
                        Compute the intersection of the plane with a point.
        
                        Args:
                            point (Point): The point to intersect with.
        
                        Returns:
                            Intersection: The intersection result.
        
                        Example:
                            >>> plane = Plane(Point(0.0, 0.0, 0.0), np.array([0.0, 0.0, 1.0]))
                            >>> intersection = plane.intersection_with(Point(1.0, 1.0, 0.0))
        """
    @typing.overload
    def intersection_with(self, point_set: PointSet) -> ...:
        """
                        Compute the intersection of the plane with a point set.
        
                        Args:
                            point_set (PointSet): The point set to intersect with.
        
                        Returns:
                            Intersection: The intersection result.
        
                        Example:
                            >>> plane = Plane(Point(0.0, 0.0, 0.0), np.array([0.0, 0.0, 1.0]))
                            >>> points = PointSet([Point(1.0, 1.0, 0.0), Point(2.0, 2.0, 1.0)])
                            >>> intersection = plane.intersection_with(points)
        """
    @typing.overload
    def intersection_with(self, line: Line) -> ...:
        """
                        Compute the intersection of the plane with a line.
        
                        Args:
                            line (Line): The line to intersect with.
        
                        Returns:
                            Intersection: The intersection result (point or line if coplanar).
        
                        Example:
                            >>> plane = Plane(Point(0.0, 0.0, 0.0), np.array([0.0, 0.0, 1.0]))
                            >>> line = Line(Point(0.0, 0.0, -1.0), np.array([0.0, 0.0, 1.0]))
                            >>> intersection = plane.intersection_with(line)
        """
    @typing.overload
    def intersection_with(self, ray: Ray) -> ...:
        """
                        Compute the intersection of the plane with a ray.
        
                        Args:
                            ray (Ray): The ray to intersect with.
        
                        Returns:
                            Intersection: The intersection result.
        
                        Example:
                            >>> plane = Plane(Point(0.0, 0.0, 0.0), np.array([0.0, 0.0, 1.0]))
                            >>> ray = Ray(Point(0.0, 0.0, -1.0), np.array([0.0, 0.0, 1.0]))
                            >>> intersection = plane.intersection_with(ray)
        """
    @typing.overload
    def intersection_with(self, segment: Segment) -> ...:
        """
                        Compute the intersection of the plane with a segment.
        
                        Args:
                            segment (Segment): The segment to intersect with.
        
                        Returns:
                            Intersection: The intersection result.
        
                        Example:
                            >>> plane = Plane(Point(0.0, 0.0, 0.0), np.array([0.0, 0.0, 1.0]))
                            >>> segment = Segment(Point(0.0, 0.0, -1.0), Point(0.0, 0.0, 1.0))
                            >>> intersection = plane.intersection_with(segment)
        """
    @typing.overload
    def intersects(self, point: Point) -> bool:
        """
                        Check if the plane intersects with a point.
        
                        Args:
                            point (Point): The point to check.
        
                        Returns:
                            bool: True if the plane intersects the point, False otherwise.
        
                        Example:
                            >>> plane = Plane(Point(0.0, 0.0, 0.0), np.array([0.0, 0.0, 1.0]))
                            >>> plane.intersects(Point(1.0, 1.0, 0.0))  # True
        """
    @typing.overload
    def intersects(self, point_set: PointSet) -> bool:
        """
                        Check if the plane intersects with a point set.
        
                        Args:
                            point_set (PointSet): The point set to check.
        
                        Returns:
                            bool: True if the plane intersects the point set, False otherwise.
        
                        Example:
                            >>> plane = Plane(Point(0.0, 0.0, 0.0), np.array([0.0, 0.0, 1.0]))
                            >>> points = PointSet([Point(1.0, 1.0, 0.0), Point(2.0, 2.0, 0.0)])
                            >>> plane.intersects(points)  # True
        """
    @typing.overload
    def intersects(self, line: Line) -> bool:
        """
                        Check if the plane intersects with a line.
        
                        Args:
                            line (Line): The line to check.
        
                        Returns:
                            bool: True if the plane intersects the line, False otherwise.
        
                        Example:
                            >>> plane = Plane(Point(0.0, 0.0, 0.0), np.array([0.0, 0.0, 1.0]))
                            >>> line = Line(Point(0.0, 0.0, -1.0), np.array([0.0, 0.0, 1.0]))
                            >>> plane.intersects(line)  # True
        """
    @typing.overload
    def intersects(self, ray: Ray) -> bool:
        """
                        Check if the plane intersects with a ray.
        
                        Args:
                            ray (Ray): The ray to check.
        
                        Returns:
                            bool: True if the plane intersects the ray, False otherwise.
        
                        Example:
                            >>> plane = Plane(Point(0.0, 0.0, 0.0), np.array([0.0, 0.0, 1.0]))
                            >>> ray = Ray(Point(0.0, 0.0, -1.0), np.array([0.0, 0.0, 1.0]))
                            >>> plane.intersects(ray)  # True
        """
    @typing.overload
    def intersects(self, segment: Segment) -> bool:
        """
                        Check if the plane intersects with a segment.
        
                        Args:
                            segment (Segment): The segment to check.
        
                        Returns:
                            bool: True if the plane intersects the segment, False otherwise.
        
                        Example:
                            >>> plane = Plane(Point(0.0, 0.0, 0.0), np.array([0.0, 0.0, 1.0]))
                            >>> segment = Segment(Point(0.0, 0.0, -1.0), Point(0.0, 0.0, 1.0))
                            >>> plane.intersects(segment)  # True
        """
    def is_defined(self) -> bool:
        """
                        Check if the plane is defined.
        
                        Returns:
                            bool: True if the plane is defined, False otherwise.
        
                        Example:
                            >>> plane = Plane(Point(0.0, 0.0, 0.0), np.array([0.0, 0.0, 1.0]))
                            >>> plane.is_defined()  # True
        """
class Point(ostk.mathematics.geometry.d3.Object):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def origin() -> Point:
        """
                        Create a point at the origin (0, 0, 0).
        
                        Returns:
                            Point: A point at coordinates (0, 0, 0).
        
                        Example:
                            >>> origin = Point.origin()
                            >>> origin.x()  # 0.0
                            >>> origin.y()  # 0.0
                            >>> origin.z()  # 0.0
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
    def vector(vector: numpy.ndarray[numpy.float64[3, 1]]) -> Point:
        """
                        Create a point from a 3D vector.
        
                        Args:
                            vector (np.array): The vector to convert to a point.
        
                        Returns:
                            Point: A point with coordinates from the vector.
        
                        Example:
                            >>> vector = np.array([1.0, 2.0, 3.0])
                            >>> point = Point.vector(vector)  # Point(1.0, 2.0, 3.0)
        """
    def __add__(self, arg0: numpy.ndarray[numpy.float64[3, 1]]) -> Point:
        ...
    def __eq__(self, arg0: Point) -> bool:
        ...
    def __init__(self, first_coordinate: ostk.core.type.Real, second_coordinate: ostk.core.type.Real, third_coordinate: ostk.core.type.Real) -> None:
        """
                        Create a 3D point with specified coordinates.
        
                        Args:
                            first_coordinate (float): The x-coordinate.
                            second_coordinate (float): The y-coordinate.
                            third_coordinate (float): The z-coordinate.
        
                        Example:
                            >>> point = Point(1.0, 2.0, 3.0)
                            >>> point.x()  # 1.0
                            >>> point.y()  # 2.0
                            >>> point.z()  # 3.0
        """
    def __ne__(self, arg0: Point) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __str__(self) -> str:
        ...
    @typing.overload
    def __sub__(self, arg0: numpy.ndarray[numpy.float64[3, 1]]) -> Point:
        ...
    @typing.overload
    def __sub__(self, arg0: Point) -> numpy.ndarray[numpy.float64[3, 1]]:
        ...
    def apply_transformation(self, transformation: typing.Any) -> None:
        """
                        Apply a transformation to the point.
        
                        Args:
                            transformation (Transformation): The transformation to apply.
        
                        Returns:
                            Point: The transformed point.
        
                        Example:
                            >>> point = Point(1.0, 2.0, 3.0)
                            >>> transformation = Transformation.identity()
                            >>> transformed = point.apply_transformation(transformation)
        """
    def as_vector(self) -> numpy.ndarray[numpy.float64[3, 1]]:
        """
                        Convert the point to a 3D vector.
        
                        Returns:
                            Vector3d: The point as a 3D vector.
        
                        Example:
                            >>> point = Point(1.0, 2.0, 3.0)
                            >>> vector = point.as_vector()  # np.array([1.0, 2.0, 3.0])
        """
    def distance_to(self, point: Point) -> ostk.core.type.Real:
        """
                        Calculate the distance to another point.
        
                        Args:
                            point (Point): The other point.
        
                        Returns:
                            float: The distance between the points.
        
                        Example:
                            >>> point1 = Point(0.0, 0.0, 0.0)
                            >>> point2 = Point(3.0, 4.0, 0.0)
                            >>> point1.distance_to(point2)  # 5.0
        """
    def is_defined(self) -> bool:
        """
                        Check if the point is defined.
        
                        Returns:
                            bool: True if the point is defined, False otherwise.
        
                        Example:
                            >>> point = Point(1.0, 2.0, 3.0)
                            >>> point.is_defined()  # True
        """
    def is_near(self, point: Point, tolerance: ostk.core.type.Real) -> bool:
        """
                        Check if this point is near another point within tolerance.
        
                        Args:
                            point (Point): The point to compare with.
                            tolerance (float): The tolerance for comparison.
        
                        Returns:
                            bool: True if points are within tolerance, False otherwise.
        
                        Example:
                            >>> point1 = Point(1.0, 2.0, 3.0)
                            >>> point2 = Point(1.1, 2.1, 3.1)
                            >>> point1.is_near(point2, 0.2)  # True
        """
    def to_string(self, precision: ostk.core.type.Integer = ...) -> ostk.core.type.String:
        """
                        Convert the point to a string representation.
        
                        Args:
                            precision (int, optional): Number of decimal places. Defaults to DEFAULT_PRECISION.
        
                        Returns:
                            str: String representation of the point.
        
                        Example:
                            >>> point = Point(1.123456, 2.345678, 3.567890)
                            >>> point.to_string(3)  # "[1.123, 2.346, 3.568]"
        """
    def x(self) -> ostk.core.type.Real:
        """
                        Get the x-coordinate of the point.
        
                        Returns:
                            float: The x-coordinate.
        
                        Example:
                            >>> point = Point(1.0, 2.0, 3.0)
                            >>> point.x()  # 1.0
        """
    def y(self) -> ostk.core.type.Real:
        """
                        Get the y-coordinate of the point.
        
                        Returns:
                            float: The y-coordinate.
        
                        Example:
                            >>> point = Point(1.0, 2.0, 3.0)
                            >>> point.y()  # 2.0
        """
    def z(self) -> ostk.core.type.Real:
        """
                        Get the z-coordinate of the point.
        
                        Returns:
                            float: The z-coordinate.
        
                        Example:
                            >>> point = Point(1.0, 2.0, 3.0)
                            >>> point.z()  # 3.0
        """
class PointSet(ostk.mathematics.geometry.d3.Object):
    """
    
                    A collection of 3D points.
    
                    A PointSet is an unordered collection of unique points in 3D space.
                
    """
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def empty() -> PointSet:
        """
                        Create an empty point set.
        
                        Returns:
                            PointSet: An empty point set.
        
                        Example:
                            >>> empty_set = PointSet.empty()
                            >>> empty_set.is_empty()  # True
                            >>> empty_set.get_size()  # 0
        """
    def __eq__(self, arg0: PointSet) -> bool:
        ...
    def __getitem__(self, arg0: int) -> Point:
        ...
    def __init__(self, points: list[Point]) -> None:
        """
                        Construct a point set from an array of points.
        
                        Args:
                            points (list[Point]): Array of 3D points.
        
                        Example:
                            >>> points = [Point(0.0, 0.0), Point(1.0, 1.0)]
                            >>> point_set = PointSet(points)
                            >>> point_set.is_defined()  # True
        """
    def __iter__(self) -> typing.Iterator[Point]:
        ...
    def __len__(self) -> int:
        ...
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
                            transformation (Transformation): The transformation to apply.
                        
                        Example:
                            >>> points = [Point(0.0, 0.0), Point(1.0, 1.0)]
                            >>> point_set = PointSet(points)
                            >>> transformation = Transformation.translation([1.0, 0.0])
                            >>> point_set.apply_transformation(transformation)
        """
    def distance_to(self, point: Point) -> ostk.core.type.Real:
        """
                        Calculate the minimum distance from the point set to a point.
        
                        Args:
                            point (Point): The point to measure distance to.
        
                        Returns:
                            float: The minimum distance to any point in the set.
        
                        Example:
                            >>> points = [Point(0.0, 0.0), Point(1.0, 1.0)]
                            >>> point_set = PointSet(points)
                            >>> point_set.distance_to(Point(0.5, 0.5))  # 0.5
        """
    def get_point_closest_to(self, point: Point) -> Point:
        """
                        Get the point in the set closest to a given point.
        
                        Args:
                            point (Point): The reference point.
        
                        Returns:
                            Point: The closest point in the set.
        
                        Example:
                            >>> points = [Point(0.0, 0.0), Point(1.0, 1.0)]
                            >>> point_set = PointSet(points)
                            >>> point_set.get_point_closest_to(Point(0.5, 0.5))  # Point(0.5, 0.5)
        """
    def get_size(self) -> int:
        """
                        Get the number of points in the set.
        
                        Returns:
                            int: The number of points.
        
                        Example:
                            >>> points = [Point(0.0, 0.0), Point(1.0, 1.0)]
                            >>> point_set = PointSet(points)
                            >>> point_set.get_size()  # 2
        """
    def is_defined(self) -> bool:
        """
                        Check if the point set is defined.
        
                        Returns:
                            bool: True if the point set is defined.
        
                        Example:
                            >>> points = [Point(0.0, 0.0), Point(1.0, 1.0)]
                            >>> point_set = PointSet(points)
                            >>> point_set.is_defined()  # True
        """
    def is_empty(self) -> bool:
        """
                        Check if the point set is empty.
        
                        Returns:
                            bool: True if the point set contains no points.
        """
    def is_near(self, point_set: PointSet, tolerance: ostk.core.type.Real) -> bool:
        """
                        Check if another point set is near this one within a tolerance.
        
                        Args:
                            point_set (PointSet): The point set to compare against.
                            tolerance (float): The maximum distance for points to be considered near.
        
                        Returns:
                            bool: True if the point sets are near each other.
        
                        Example:
                            >>> points = [Point(0.0, 0.0), Point(1.0, 1.0)]
                            >>> point_set = PointSet(points)
                            >>> point_set.is_near(PointSet(points), 0.1)  # True
        """
class Polygon(ostk.mathematics.geometry.d3.Object):
    """
    
                    A polygon in 3D space.
    
                    A Polygon is a planar figure defined by a 2D polygon and its position and orientation in 3D space.
                
    """
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
    def __init__(self, polygon: ostk.mathematics.geometry.d2.object.Polygon, origin: Point, x_axis: numpy.ndarray[numpy.float64[3, 1]], y_axis: numpy.ndarray[numpy.float64[3, 1]]) -> None:
        """
                        Construct a 3D polygon from a 2D polygon and coordinate frame.
        
                        Args:
                            polygon (Polygon2d): The 2D polygon.
                            origin (Point): The origin of the polygon in 3D space.
                            x_axis (numpy.ndarray): The x-axis direction of the polygon's local frame.
                            y_axis (numpy.ndarray): The y-axis direction of the polygon's local frame.
                        
                        Example:
                            >>> polygon2d = Polygon2d([Point2d(0.0, 0.0), Point2d(1.0, 0.0), Point2d(1.0, 1.0), Point2d(0.0, 1.0)])
                            >>> origin = Point(0.0, 0.0, 0.0)
                            >>> x_axis = np.array([1.0, 0.0, 0.0])
                            >>> y_axis = np.array([0.0, 1.0, 0.0])
                            >>> polygon = Polygon(polygon2d, origin, x_axis, y_axis)
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
                            >>> polygon = Polygon(polygon2d, origin, x_axis, y_axis)
                            >>> transformation = Transformation.identity()
                            >>> polygon.apply_transformation(transformation)
        """
    def get_edge_at(self, index: int) -> Segment:
        """
                        Get the edge at a given index.
        
                        Args:
                            index (int): The index of the edge.
        
                        Returns:
                            Segment: The edge segment.
                        
                        Example:
                            >>> polygon = Polygon(polygon2d, origin, x_axis, y_axis)
                            >>> polygon.get_edge_at(0)
        """
    def get_edge_count(self) -> int:
        """
                        Get the number of edges in the polygon.
        
                        Returns:
                            int: The number of edges.
                        
                        Example:
                            >>> polygon = Polygon(polygon2d, origin, x_axis, y_axis)
                            >>> polygon.get_edge_count()
        """
    def get_normal_vector(self) -> numpy.ndarray[numpy.float64[3, 1]]:
        """
                        Get the normal vector of the polygon's plane.
        
                        Returns:
                            numpy.ndarray: The normal vector.
                        
                        Example:
                            >>> polygon = Polygon(polygon2d, origin, x_axis, y_axis)
                            >>> polygon.get_normal_vector()
        """
    def get_origin(self) -> Point:
        """
                        Get the origin point of the polygon.
        
                        Returns:
                            Point: The origin point.
                        
                        Example:
                            >>> polygon = Polygon(polygon2d, origin, x_axis, y_axis)
                            >>> polygon.get_origin()
        """
    def get_polygon2d(self) -> ostk.mathematics.geometry.d2.object.Polygon:
        """
                        Get the 2D polygon representation.
        
                        Returns:
                            Polygon2d: The 2D polygon.
                        
                        Example:
                            >>> polygon = Polygon(polygon2d, origin, x_axis, y_axis)
                            >>> polygon.get_polygon2d()
        """
    def get_vertex_at(self, index: int) -> Point:
        """
                        Get the vertex at a given index.
        
                        Args:
                            index (int): The index of the vertex.
        
                        Returns:
                            Point: The vertex point.
                        
                        Example:
                            >>> polygon = Polygon(polygon2d, origin, x_axis, y_axis)
                            >>> polygon.get_vertex_at(0)
        """
    def get_vertex_count(self) -> int:
        """
                        Get the number of vertices in the polygon.
        
                        Returns:
                            int: The number of vertices.
                        
                        Example:
                            >>> polygon = Polygon(polygon2d, origin, x_axis, y_axis)
                            >>> polygon.get_vertex_count()
        """
    def get_vertices(self) -> list[Point]:
        """
                        Get all vertices of the polygon.
        
                        Returns:
                            list[Point]: Array of vertex points.
                        
                        Example:
                            >>> polygon = Polygon(polygon2d, origin, x_axis, y_axis)
                            >>> polygon.get_vertices()
        """
    def get_x_axis(self) -> numpy.ndarray[numpy.float64[3, 1]]:
        """
                        Get the x-axis direction of the polygon's local frame.
        
                        Returns:
                            numpy.ndarray: The x-axis vector.
                        
                        Example:
                            >>> polygon = Polygon(polygon2d, origin, x_axis, y_axis)
                            >>> polygon.get_x_axis()
        """
    def get_y_axis(self) -> numpy.ndarray[numpy.float64[3, 1]]:
        """
                        Get the y-axis direction of the polygon's local frame.
        
                        Returns:
                            numpy.ndarray: The y-axis vector.
                        
                        Example:
                            >>> polygon = Polygon(polygon2d, origin, x_axis, y_axis)
                            >>> polygon.get_y_axis()
        """
    def is_defined(self) -> bool:
        """
                        Check if the polygon is defined.
        
                        Returns:
                            bool: True if the polygon is defined.
                        
                        Example:
                            >>> polygon = Polygon(polygon2d, origin, x_axis, y_axis)
                            >>> polygon.is_defined()
        """
    def is_near(self, polygon: Polygon, tolerance: ostk.core.type.Real) -> bool:
        """
                        Check if another polygon is near this one within a tolerance.
        
                        Args:
                            polygon (Polygon): The polygon to compare against.
                            tolerance (float): The maximum distance for polygons to be considered near.
        
                        Returns:
                            bool: True if the polygons are near each other.
                        
                        Example:
                            >>> polygon = Polygon(polygon2d, origin, x_axis, y_axis)
                            >>> polygon.is_near(polygon, 0.0)
        """
class Pyramid(ostk.mathematics.geometry.d3.Object):
    """
    
                    A pyramid in 3D space.
    
                    A Pyramid is defined by a polygonal base and an apex point, with triangular lateral faces connecting the base edges to the apex.
                
    """
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def undefined() -> Pyramid:
        """
                        Create an undefined pyramid.
        
                        Returns:
                            Pyramid: An undefined pyramid.
                        
                        Example:
                            >>> undefined_pyramid = Pyramid.undefined()
                            >>> undefined_pyramid.is_defined()  # False
        """
    def __eq__(self, arg0: Pyramid) -> bool:
        ...
    def __init__(self, base: Polygon, apex: Point) -> None:
        """
                        Construct a pyramid from a base polygon and apex point.
        
                        Args:
                            base (Polygon): The polygonal base of the pyramid.
                            apex (Point): The apex point of the pyramid.
                        
                        Example:
                            >>> base = Polygon([Point2d(0.0, 0.0), Point2d(1.0, 0.0), Point2d(1.0, 1.0), Point2d(0.0, 1.0)])
                            >>> apex = Point(0.0, 0.0, 1.0)
                            >>> pyramid = Pyramid(base, apex)
        """
    def __ne__(self, arg0: Pyramid) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __str__(self) -> str:
        ...
    def apply_transformation(self, transformation: typing.Any) -> None:
        """
                        Apply a transformation to the pyramid.
        
                        Args:
                            transformation (Transformation): The transformation to apply.
                        
                        Example:
                            >>> base = Polygon([Point2d(0.0, 0.0), Point2d(1.0, 0.0), Point2d(1.0, 1.0), Point2d(0.0, 1.0)])
                            >>> apex = Point(0.0, 0.0, 1.0)
                            >>> pyramid = Pyramid(base, apex)
                            >>> transformation = Transformation.identity()
                            >>> pyramid.apply_transformation(transformation)
        """
    @typing.overload
    def contains(self, point: Point) -> bool:
        """
                        Check if the pyramid contains a point.
        
                        Args:
                            point (Point): The point to check.
        
                        Returns:
                            bool: True if the pyramid contains the point.
                        
                        Example:
                            >>> base = Polygon([Point2d(0.0, 0.0), Point2d(1.0, 0.0), Point2d(1.0, 1.0), Point2d(0.0, 1.0)])
                            >>> apex = Point(0.0, 0.0, 1.0)
                            >>> pyramid = Pyramid(base, apex)
                            >>> pyramid.contains(Point(0.5, 0.5, 0.5))
        """
    @typing.overload
    def contains(self, point_set: PointSet) -> bool:
        """
                        Check if the pyramid contains all points in a point set.
        
                        Args:
                            point_set (PointSet): The point set to check.
        
                        Returns:
                            bool: True if the pyramid contains all points.
                        
                        Example:
                            >>> base = Polygon([Point2d(0.0, 0.0), Point2d(1.0, 0.0), Point2d(1.0, 1.0), Point2d(0.0, 1.0)])
                            >>> apex = Point(0.0, 0.0, 1.0)
                            >>> pyramid = Pyramid(base, apex)
                            >>> pyramid.contains(PointSet([Point(0.5, 0.5, 0.5), Point(0.6, 0.6, 0.6)]))
        """
    @typing.overload
    def contains(self, segment: Segment) -> bool:
        """
                        Check if the pyramid contains a segment.
        
                        Args:
                            segment (Segment): The segment to check.
        
                        Returns:
                            bool: True if the pyramid contains the segment.
                        
                        Example:
                            >>> base = Polygon([Point2d(0.0, 0.0), Point2d(1.0, 0.0), Point2d(1.0, 1.0), Point2d(0.0, 1.0)])
                            >>> apex = Point(0.0, 0.0, 1.0)
                            >>> pyramid = Pyramid(base, apex)
                            >>> pyramid.contains(Segment(Point(0.5, 0.5, 0.5), Point(0.6, 0.6, 0.6)))
        """
    @typing.overload
    def contains(self, ellipsoid: Ellipsoid) -> bool:
        """
                        Check if the pyramid contains an ellipsoid.
        
                        Args:
                            ellipsoid (Ellipsoid): The ellipsoid to check.
        
                        Returns:
                            bool: True if the pyramid contains the ellipsoid.
                        
                        Example:
                            >>> base = Polygon([Point2d(0.0, 0.0), Point2d(1.0, 0.0), Point2d(1.0, 1.0), Point2d(0.0, 1.0)])
                            >>> apex = Point(0.0, 0.0, 1.0)
                            >>> pyramid = Pyramid(base, apex)
                            >>> pyramid.contains(Ellipsoid(Point(0.0, 0.0, 0.0), 1.0, 1.0, 1.0))
        """
    def get_apex(self) -> Point:
        """
                        Get the apex point of the pyramid.
        
                        Returns:
                            Point: The apex point.
                        
                        Example:
                            >>> base = Polygon([Point2d(0.0, 0.0), Point2d(1.0, 0.0), Point2d(1.0, 1.0), Point2d(0.0, 1.0)])
                            >>> apex = Point(0.0, 0.0, 1.0)
                            >>> pyramid = Pyramid(base, apex)
                            >>> pyramid.get_apex()
        """
    def get_base(self) -> Polygon:
        """
                        Get the base polygon of the pyramid.
        
                        Returns:
                            Polygon: The base polygon.
                        
                        Example:
                            >>> base = Polygon([Point2d(0.0, 0.0), Point2d(1.0, 0.0), Point2d(1.0, 1.0), Point2d(0.0, 1.0)])
                            >>> apex = Point(0.0, 0.0, 1.0)
                            >>> pyramid = Pyramid(base, apex)
                            >>> pyramid.get_base()
        """
    def get_lateral_face_at(self, index: int) -> Polygon:
        """
                        Get the lateral face at a given index.
        
                        Args:
                            index (int): The index of the lateral face.
        
                        Returns:
                            Polygon: The lateral face polygon.
                        
                        Example:
                            >>> base = Polygon([Point2d(0.0, 0.0), Point2d(1.0, 0.0), Point2d(1.0, 1.0), Point2d(0.0, 1.0)])
                            >>> apex = Point(0.0, 0.0, 1.0)
                            >>> pyramid = Pyramid(base, apex)
                            >>> pyramid.get_lateral_face_at(0)
        """
    def get_lateral_face_count(self) -> int:
        """
                        Get the number of lateral faces.
        
                        Returns:
                            int: The number of lateral faces.
                        
                        Example:
                            >>> base = Polygon([Point2d(0.0, 0.0), Point2d(1.0, 0.0), Point2d(1.0, 1.0), Point2d(0.0, 1.0)])
                            >>> apex = Point(0.0, 0.0, 1.0)
                            >>> pyramid = Pyramid(base, apex)
                            >>> pyramid.get_lateral_face_count()
        """
    def get_rays_of_lateral_face_at(self, lateral_face_index: int, ray_count: int = 2) -> list[Ray]:
        """
                        Get rays from the apex through a specific lateral face.
        
                        Args:
                            lateral_face_index (int): The index of the lateral face.
                            ray_count (int): The number of rays to generate (default: 2).
        
                        Returns:
                            list[Ray]: Array of rays.
                        
                        Example:
                            >>> base = Polygon([Point2d(0.0, 0.0), Point2d(1.0, 0.0), Point2d(1.0, 1.0), Point2d(0.0, 1.0)])
                            >>> apex = Point(0.0, 0.0, 1.0)
                            >>> pyramid = Pyramid(base, apex)
                            >>> pyramid.get_rays_of_lateral_face_at(0)
        """
    def get_rays_of_lateral_faces(self, ray_count: int = 0) -> list[Ray]:
        """
                        Get rays from the apex through all lateral faces.
        
                        Args:
                            ray_count (int, optional): The number of rays per face. Defaults to 0.
        
                        Returns:
                            list[Ray]: Array of rays.
                        
                        Example:
                            >>> base = Polygon([Point2d(0.0, 0.0), Point2d(1.0, 0.0), Point2d(1.0, 1.0), Point2d(0.0, 1.0)])
                            >>> apex = Point(0.0, 0.0, 1.0)
                            >>> pyramid = Pyramid(base, apex)
                            >>> pyramid.get_rays_of_lateral_faces(ray_count=1)
        """
    @typing.overload
    def intersection_with(self, sphere: Sphere, only_in_sight: bool = False, discretization_level: int = 40) -> ...:
        """
                        Compute the intersection of the pyramid with a sphere.
        
                        Args:
                            sphere (Sphere): The sphere to intersect with.
                            only_in_sight (bool): Only compute intersection in sight of the apex.
                            discretization_level (int): The level of discretization for the computation.
        
                        Returns:
                            Intersection: The intersection result.
                        
                        Example:
                            >>> base = Polygon([Point2d(0.0, 0.0), Point2d(1.0, 0.0), Point2d(1.0, 1.0), Point2d(0.0, 1.0)])
                            >>> apex = Point(0.0, 0.0, 1.0)
                            >>> pyramid = Pyramid(base, apex)
                            >>> pyramid.intersection_with(Sphere(Point(0.0, 0.0, 0.0), 1.0))
        """
    @typing.overload
    def intersection_with(self, ellipsoid: Ellipsoid, only_in_sight: bool = False, discretization_level: int = 40) -> ...:
        """
                        Compute the intersection of the pyramid with an ellipsoid.
        
                        Args:
                            ellipsoid (Ellipsoid): The ellipsoid to intersect with.
                            only_in_sight (bool): Only compute intersection in sight of the apex.
                            discretization_level (int): The level of discretization for the computation.
        
                        Returns:
                            Intersection: The intersection result.
                        
                        Example:
                            >>> base = Polygon([Point2d(0.0, 0.0), Point2d(1.0, 0.0), Point2d(1.0, 1.0), Point2d(0.0, 1.0)])
                            >>> apex = Point(0.0, 0.0, 1.0)
                            >>> pyramid = Pyramid(base, apex)
                            >>> pyramid.intersection_with(Ellipsoid(Point(0.0, 0.0, 0.0), 1.0, 1.0, 1.0))
        """
    def intersects(self, ellipsoid: Ellipsoid, discretization_level: int = 40) -> bool:
        """
                        Check if the pyramid intersects an ellipsoid.
        
                        Args:
                            ellipsoid (Ellipsoid): The ellipsoid to check intersection with.
                            discretization_level (int): The level of discretization for the check.
        
                        Returns:
                            bool: True if the pyramid intersects the ellipsoid.
        """
    def is_defined(self) -> bool:
        """
                        Check if the pyramid is defined.
        
                        Returns:
                            bool: True if the pyramid is defined.
                        
                        Example:
                            >>> base = Polygon([Point2d(0.0, 0.0), Point2d(1.0, 0.0), Point2d(1.0, 1.0), Point2d(0.0, 1.0)])
                            >>> apex = Point(0.0, 0.0, 1.0)
                            >>> pyramid = Pyramid(base, apex)
                            >>> pyramid.is_defined()
        """
class Ray(ostk.mathematics.geometry.d3.Object):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def undefined() -> Ray:
        """
                        Create an undefined ray.
        
                        Returns:
                            Ray: An undefined ray object.
        
                        Example:
                            >>> undefined_ray = Ray.undefined()
                            >>> undefined_ray.is_defined()  # False
        """
    def __eq__(self, arg0: Ray) -> bool:
        ...
    def __init__(self, origin: Point, direction: numpy.ndarray[numpy.float64[3, 1]]) -> None:
        """
                        Create a 3D ray with specified origin and direction.
        
                        Args:
                            origin (Point): The origin point of the ray.
                            direction (np.array): The direction vector of the ray.
        
                        Example:
                            >>> origin = Point(0.0, 0.0, 0.0)
                            >>> direction = np.array([1.0, 0.0, 0.0])
                            >>> ray = Ray(origin, direction)
        """
    def __ne__(self, arg0: Ray) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __str__(self) -> str:
        ...
    def apply_transformation(self, transformation: typing.Any) -> None:
        """
                        Apply a transformation to the ray.
        
                        Args:
                            transformation (Transformation): The transformation to apply.
        
                        Example:
                            >>> ray = Ray(Point(0.0, 0.0, 0.0), np.array([1.0, 0.0, 0.0]))
                            >>> transformation = Transformation.translation([1.0, 0.0])
                            >>> ray.apply_transformation(transformation)
        """
    @typing.overload
    def contains(self, point: Point) -> bool:
        """
                        Check if the ray contains a point.
        
                        Args:
                            point (Point): The point to check.
        
                        Returns:
                            bool: True if the ray contains the point, False otherwise.
        
                        Example:
                            >>> ray = Ray(Point(0.0, 0.0, 0.0), np.array([1.0, 0.0, 0.0]))
                            >>> ray.contains(Point(2.0, 0.0, 0.0))  # True (point on ray)
        """
    @typing.overload
    def contains(self, point_set: PointSet) -> bool:
        """
                        Check if the ray contains a point set.
        
                        Args:
                            point_set (PointSet): The point set to check.
        
                        Returns:
                            bool: True if the ray contains the point set, False otherwise.
        """
    def distance_to(self, point: Point) -> ostk.core.type.Real:
        """
                        Calculate the distance from the ray to a point.
        
                        Args:
                            point (Point): The point to calculate distance to.
        
                        Returns:
                            float: The minimum distance from the ray to the point.
        
                        Example:
                            >>> ray = Ray(Point(0.0, 0.0, 0.0), np.array([1.0, 0.0, 0.0]))
                            >>> distance = ray.distance_to(Point(1.0, 1.0, 0.0))  # 1.0
        """
    def get_direction(self) -> numpy.ndarray[numpy.float64[3, 1]]:
        """
                        Get the direction vector of the ray.
        
                        Returns:
                            Vector3d: The normalized direction vector of the ray.
        
                        Example:
                            >>> ray = Ray(Point(0.0, 0.0, 0.0), np.array([1.0, 0.0, 0.0]))
                            >>> direction = ray.get_direction()  # [1.0, 0.0, 0.0]
        """
    def get_origin(self) -> Point:
        """
                        Get the origin point of the ray.
        
                        Returns:
                            Point: The origin point of the ray.
        
                        Example:
                            >>> ray = Ray(Point(1.0, 2.0, 3.0), np.array([1.0, 0.0, 0.0]))
                            >>> origin = ray.get_origin()  # Point(1.0, 2.0, 3.0)
        """
    @typing.overload
    def intersection_with(self, plane: typing.Any) -> ...:
        """
                        Compute the intersection of the ray with a plane.
        
                        Args:
                            plane (Plane): The plane to intersect with.
        
                        Returns:
                            Intersection: The intersection of the ray with the plane.
                        
                        Example:
                            >>> ray = Ray(Point(0.0, 0.0, 0.0), np.array([0.0, 0.0, -1.0]))
                            >>> plane = Plane(Point(0.0, 0.0, 0.0), np.array([0.0, 0.0, 1.0]))
                            >>> intersection = ray.intersection_with(plane)
                            >>> intersection.get_point()  # Point(0.0, 0.0, 0.0)
        """
    @typing.overload
    def intersection_with(self, sphere: typing.Any, only_in_sight: bool = False) -> ...:
        """
                        Compute the intersection of the ray with a sphere.
        
                        Args:
                            sphere (Sphere): The sphere to intersect with.
                            only_in_sight (bool, optional): If true, only return intersection points that are in sight. Defaults to True.
        
                        Returns:
                            Intersection: The intersection of the ray with the sphere.
        
                        Example:
                            >>> ray = Ray(Point(0.0, 0.0, 0.0), np.array([1.0, 0.0, 0.0]))
                            >>> sphere = Sphere(Point(0.0, 0.0, 0.0), 1.0)
                            >>> intersection = ray.intersection_with(sphere)
                            >>> intersection.get_point()  # Point(0.0, 0.0, 0.0)
        """
    @typing.overload
    def intersection_with(self, ellipsoid: typing.Any, only_in_sight: bool = False) -> ...:
        """
                        Compute the intersection of the ray with an ellipsoid.
        
                        Args:
                            ellipsoid (Ellipsoid): The ellipsoid to intersect with.
                            only_in_sight (bool, optional): If true, only return intersection points that are in sight. Defaults to True.
        
                        Returns:
                            Intersection: The intersection of the ray with the ellipsoid.
        
                        Example:
                            >>> ray = Ray(Point(0.0, 0.0, 0.0), np.array([1.0, 0.0, 0.0]))
                            >>> ellipsoid = Ellipsoid(Point(0.0, 0.0, 0.0), 1.0, 1.0, 1.0)
                            >>> intersection = ray.intersection_with(ellipsoid)
                            >>> intersection.get_point()  # Point(0.0, 0.0, 0.0)
        """
    @typing.overload
    def intersects(self, point: Point) -> bool:
        ...
    @typing.overload
    def intersects(self, plane: typing.Any) -> bool:
        ...
    @typing.overload
    def intersects(self, sphere: typing.Any) -> bool:
        ...
    @typing.overload
    def intersects(self, ellipsoid: typing.Any) -> bool:
        ...
    def is_defined(self) -> bool:
        """
                        Check if the ray is defined.
        
                        Returns:
                            bool: True if the ray is defined, False otherwise.
        
                        Example:
                            >>> ray = Ray(Point(0.0, 0.0, 0.0), np.array([1.0, 0.0, 0.0]))
                            >>> ray.is_defined()  # True
        """
class Segment(ostk.mathematics.geometry.d3.Object):
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
    def __init__(self, first_point: Point, second_point: Point) -> None:
        """
                        Create a 3D segment between two points.
        
                        Args:
                            first_point (Point): The first endpoint of the segment.
                            second_point (Point): The second endpoint of the segment.
        
                        Example:
                            >>> point1 = Point(0.0, 0.0, 0.0)
                            >>> point2 = Point(1.0, 1.0, 1.0)
                            >>> segment = Segment(point1, point2)
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
                            transformation (Transformation): The transformation to apply.
        
                        Example:
                            >>> segment = Segment(Point(0.0, 0.0, 0.0), Point(1.0, 1.0, 1.0))
                            >>> transformation = Translation([1.0, 1.0, 1.0])
                            >>> segment.apply_transformation(transformation)
        """
    def contains(self, point: Point) -> bool:
        """
                        Check if the segment contains a point.
        
                        Args:
                            point (Point): The point to check.
        
                        Returns:
                            bool: True if the segment contains the point, False otherwise.
        
                        Example:
                            >>> segment = Segment(Point(0.0, 0.0, 0.0), Point(2.0, 0.0, 0.0))
                            >>> segment.contains(Point(1.0, 0.0, 0.0))  # True (midpoint)
        """
    @typing.overload
    def distance_to(self, point: Point) -> ostk.core.type.Real:
        """
                        Calculate the distance from the segment to a point.
        
                        Args:
                            point (Point): The point to calculate distance to.
        
                        Returns:
                            float: The distance from the segment to the point.
        
                        Example:
                            >>> segment = Segment(Point(0.0, 0.0, 0.0), Point(2.0, 0.0, 0.0))
                            >>> distance = segment.distance_to(Point(1.0, 0.0, 0.0))  # 1.0
        """
    @typing.overload
    def distance_to(self, point_set: PointSet) -> ostk.core.type.Real:
        """
                        Calculate the distance from the segment to a point set.
        
                        Args:
                            point_set (PointSet): The point set to calculate distance to.
        
                        Returns:
                            float: The distance from the segment to the point set.
        
                        Example:
                            >>> segment = Segment(Point(0.0, 0.0, 0.0), Point(2.0, 0.0, 0.0))
                            >>> points = PointSet([Point(1.0, 0.0, 0.0), Point(3.0, 0.0, 0.0)])
                            >>> distance = segment.distance_to(points)  # 1.0
        """
    def get_center(self) -> Point:
        """
                        Get the center point of the segment.
        
                        Returns:
                            Point: The midpoint of the segment.
        
                        Example:
                            >>> segment = Segment(Point(0.0, 0.0, 0.0), Point(2.0, 2.0, 2.0))
                            >>> center = segment.get_center()  # Point(1.0, 1.0, 1.0)
        """
    def get_direction(self) -> numpy.ndarray[numpy.float64[3, 1]]:
        """
                        Get the direction vector of the segment.
        
                        Returns:
                            Vector3d: The normalized direction vector from first to second point.
        
                        Example:
                            >>> segment = Segment(Point(0.0, 0.0, 0.0), Point(1.0, 0.0, 0.0))
                            >>> direction = segment.get_direction()  # [1.0, 0.0, 0.0]
        """
    def get_first_point(self) -> Point:
        """
                        Get the first endpoint of the segment.
        
                        Returns:
                            Point: The first endpoint of the segment.
        
                        Example:
                            >>> segment = Segment(Point(1.0, 2.0, 3.0), Point(4.0, 5.0, 6.0))
                            >>> first_point = segment.get_first_point()  # Point(1.0, 2.0, 3.0)
        """
    def get_length(self) -> ostk.core.type.Real:
        """
                        Get the length of the segment.
        
                        Returns:
                            float: The distance between the two endpoints.
        
                        Example:
                            >>> segment = Segment(Point(0.0, 0.0, 0.0), Point(3.0, 4.0, 0.0))
                            >>> length = segment.get_length()  # 5.0
        """
    def get_second_point(self) -> Point:
        """
                        Get the second endpoint of the segment.
        
                        Returns:
                            Point: The second endpoint of the segment.
        
                        Example:
                            >>> segment = Segment(Point(1.0, 2.0, 3.0), Point(4.0, 5.0, 6.0))
                            >>> second_point = segment.get_second_point()  # Point(4.0, 5.0, 6.0)
        """
    def intersection_with(self, plane: typing.Any) -> ...:
        """
                        Calculate the intersection of the segment with a plane.
        
                        Args:
                            plane (Plane): The plane to calculate intersection with.
        
                        Returns:
                            Intersection: The intersection of the segment with the plane.
        
                        Example:
                            >>> segment = Segment(Point(0.0, 0.0, 0.0), Point(2.0, 0.0, 0.0))
                            >>> plane = Plane(Point(1.0, 0.0, 0.0), Vector3d(0.0, 0.0, 1.0))
                            >>> intersection = segment.intersection_with(plane)
                            >>> intersection.get_point()  # Point(1.0, 0.0, 0.0)
        """
    @typing.overload
    def intersects(self, plane: typing.Any) -> bool:
        """
                        Check if the segment intersects a plane.
        
                        Args:
                            plane (Plane): The plane to check intersection with.
        
                        Returns:
                            bool: True if the segment intersects the plane.
        
                        Example:
                            >>> segment = Segment(Point(0.0, 0.0, 0.0), Point(2.0, 0.0, 0.0))
                            >>> segment.intersects(Plane(Point(1.0, 0.0, 0.0), Vector3d(0.0, 0.0, 1.0)))  # True
        """
    @typing.overload
    def intersects(self, sphere: typing.Any) -> bool:
        """
                        Check if the segment intersects a sphere.
        
                        Args:
                            sphere (Sphere): The sphere to check intersection with.
        
                        Returns:
                            bool: True if the segment intersects the sphere.
        
                        Example:
                            >>> segment = Segment(Point(0.0, 0.0, 0.0), Point(2.0, 0.0, 0.0))
                            >>> segment.intersects(Sphere(Point(1.0, 0.0, 0.0), 1.0))  # True
        """
    @typing.overload
    def intersects(self, ellipsoid: typing.Any) -> bool:
        """
                        Check if the segment intersects an ellipsoid.
        
                        Args:
                            ellipsoid (Ellipsoid): The ellipsoid to check intersection with.
        
                        Returns:
                            bool: True if the segment intersects the ellipsoid.
        
                        Example:
                            >>> segment = Segment(Point(0.0, 0.0, 0.0), Point(2.0, 0.0, 0.0))
                            >>> segment.intersects(Ellipsoid(Point(1.0, 0.0, 0.0), 1.0, 1.0, 1.0))  # True
        """
    def is_defined(self) -> bool:
        """
                        Check if the segment is defined.
        
                        Returns:
                            bool: True if the segment is defined, False otherwise.
        
                        Example:
                            >>> segment = Segment(Point(0.0, 0.0, 0.0), Point(1.0, 1.0, 1.0))
                            >>> segment.is_defined()  # True
        """
    def is_degenerate(self) -> bool:
        """
                        Check if the segment is degenerate (both endpoints are the same).
        
                        Returns:
                            bool: True if the segment is degenerate, False otherwise.
        
                        Example:
                            >>> point = Point(0.0, 0.0, 0.0)
                            >>> degenerate_segment = Segment(point, point)
                            >>> degenerate_segment.is_degenerate()  # True
        """
    def to_line(self) -> Line:
        """
                        Convert the segment to a line.
        
                        Returns:
                            Line: A line passing through the segment's endpoints.
        
                        Example:
                            >>> segment = Segment(Point(0.0, 0.0, 0.0), Point(1.0, 1.0, 1.0))
                            >>> line = segment.to_line()
        """
class Sphere(ostk.mathematics.geometry.d3.Object):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def undefined() -> Sphere:
        """
                        Create an undefined sphere.
        
                        Returns:
                            Sphere: An undefined sphere.
        
                        Example:
                            >>> undefined_sphere = Sphere.undefined()
                            >>> undefined_sphere.is_defined()  # False
        """
    @staticmethod
    def unit(center: Point) -> Sphere:
        """
                        Create a unit sphere (radius = 1) at a given center.
        
                        Args:
                            center (Point): The center point of the unit sphere.
        
                        Returns:
                            Sphere: A unit sphere centered at the given point.
        
                        Example:
                            >>> center = Point(1.0, 2.0, 3.0)
                            >>> unit_sphere = Sphere.unit(center)
                            >>> unit_sphere.get_radius()  # 1.0
        """
    def __eq__(self, arg0: Sphere) -> bool:
        ...
    def __init__(self, center: Point, radius: ostk.core.type.Real) -> None:
        """
                        Create a 3D sphere with center and radius.
        
                        Args:
                            center (Point): The center point of the sphere.
                            radius (float): The radius of the sphere.
        
                        Example:
                            >>> center = Point(0.0, 0.0, 0.0)
                            >>> sphere = Sphere(center, 1.0)
        """
    def __ne__(self, arg0: Sphere) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __str__(self) -> str:
        ...
    def apply_transformation(self, transformation: typing.Any) -> None:
        """
                        Apply a transformation to the sphere in place.
        
                        Args:
                            transformation (Transformation): The transformation to apply.
        
                        Example:
                            >>> sphere = Sphere(Point(0.0, 0.0, 0.0), 1.0)
                            >>> transformation = Translation([1.0, 0.0, 0.0])
                            >>> sphere.apply_transformation(transformation)
        """
    @typing.overload
    def contains(self, point: Point) -> bool:
        """
                        Check if the sphere contains a point.
        
                        Args:
                            point (Point): The point to check.
        
                        Returns:
                            bool: True if the sphere contains the point, False otherwise.
        
                        Example:
                            >>> sphere = Sphere(Point(0.0, 0.0, 0.0), 1.0)
                            >>> sphere.contains(Point(0.5, 0.5, 0.5))  # True
        """
    @typing.overload
    def contains(self, point_set: PointSet) -> bool:
        """
                        Check if the sphere contains a point set.
        
                        Args:
                            point_set (PointSet): The point set to check.
        
                        Returns:
                            bool: True if the sphere contains the point set, False otherwise.
        
                        Example:
                            >>> sphere = Sphere(Point(0.0, 0.0, 0.0), 1.0)
                            >>> sphere.contains(PointSet([Point(0.5, 0.5, 0.5), Point(1.0, 1.0, 1.0)]))  # True
        """
    def get_center(self) -> Point:
        """
                        Get the center point of the sphere.
        
                        Returns:
                            Point: The center point of the sphere.
        
                        Example:
                            >>> sphere = Sphere(Point(1.0, 2.0, 3.0), 1.0)
                            >>> center = sphere.get_center()  # Point(1.0, 2.0, 3.0)
        """
    def get_radius(self) -> ostk.core.type.Real:
        """
                        Get the radius of the sphere.
        
                        Returns:
                            float: The radius of the sphere.
        
                        Example:
                            >>> sphere = Sphere(Point(0.0, 0.0, 0.0), 2.5)
                            >>> radius = sphere.get_radius()  # 2.5
        """
    @typing.overload
    def intersection_with(self, line: Line) -> ...:
        """
                        Check if the sphere intersects a line.
        
                        Args:
                            line (Line): The line to check intersection with.
        
                        Returns:
                            bool: True if the sphere intersects the line.
        
                        Example:
                            >>> sphere = Sphere(Point(0.0, 0.0, 0.0), 1.0)
                            >>> sphere.intersection_with(Line(Point(1.0, 0.0, 0.0), Point(0.0, 1.0, 0.0)))  # True
        """
    @typing.overload
    def intersection_with(self, ray: Ray, only_in_sight: bool = False) -> ...:
        """
                        Check if the sphere intersects a ray.
        
                        Args:
                            ray (Ray): The ray to check intersection with.
                            only_in_sight (bool, optional): If true, only return intersection points that are in sight. Defaults to False.
        
                        Returns:
                            bool: True if the sphere intersects the ray.
        
                        Example:
                            >>> sphere = Sphere(Point(0.0, 0.0, 0.0), 1.0)
                            >>> sphere.intersection_with(Ray(Point(1.0, 0.0, 0.0), Point(0.0, 1.0, 0.0)))  # True
        """
    @typing.overload
    def intersects(self, point: Point) -> bool:
        """
                        Check if the sphere intersects a point.
        
                        Args:
                            point (Point): The point to check intersection with.
        
                        Returns:
                            bool: True if the sphere intersects the point.
        
                        Example:
                            >>> sphere = Sphere(Point(0.0, 0.0, 0.0), 1.0)
                            >>> sphere.intersects(Point(1.0, 0.0, 0.0))  # True
        """
    @typing.overload
    def intersects(self, point_set: PointSet) -> bool:
        """
                        Check if the sphere intersects a point set.
        
                        Args:
                            point_set (PointSet): The point set to check intersection with.
        
                        Returns:
                            bool: True if the sphere intersects the point set.
        
                        Example:
                            >>> sphere = Sphere(Point(0.0, 0.0, 0.0), 1.0)
                            >>> sphere.intersects(PointSet([Point(1.0, 0.0, 0.0), Point(0.0, 1.0, 0.0)]))  # True
        """
    @typing.overload
    def intersects(self, line: Line) -> bool:
        """
                        Check if the sphere intersects a line.
        
                        Args:
                            line (Line): The line to check intersection with.
        
                        Returns:
                            bool: True if the sphere intersects the line.
        
                        Example:
                            >>> sphere = Sphere(Point(0.0, 0.0, 0.0), 1.0)
                            >>> sphere.intersects(Line(Point(1.0, 0.0, 0.0), Point(0.0, 1.0, 0.0)))  # True
        """
    @typing.overload
    def intersects(self, ray: Ray) -> bool:
        """
                        Check if the sphere intersects a ray.
        
                        Args:
                            ray (Ray): The ray to check intersection with.
        
                        Returns:
                            bool: True if the sphere intersects the ray.
        
                        Example:
                            >>> sphere = Sphere(Point(0.0, 0.0, 0.0), 1.0)
                            >>> sphere.intersects(Ray(Point(1.0, 0.0, 0.0), Point(0.0, 1.0, 0.0)))  # True
        """
    @typing.overload
    def intersects(self, segment: Segment) -> bool:
        """
                        Check if the sphere intersects a segment.
        
                        Args:
                            segment (Segment): The segment to check intersection with.
        
                        Returns:
                            bool: True if the sphere intersects the segment.
        
                        Example:
                            >>> sphere = Sphere(Point(0.0, 0.0, 0.0), 1.0)
                            >>> sphere.intersects(Segment(Point(1.0, 0.0, 0.0), Point(0.0, 1.0, 0.0)))  # True
        """
    @typing.overload
    def intersects(self, plane: Plane) -> bool:
        """
                        Check if the sphere intersects a plane.
        
                        Args:
                            plane (Plane): The plane to check intersection with.
        
                        Returns:
                            bool: True if the sphere intersects the plane.
        
                        Example:
                            >>> sphere = Sphere(Point(0.0, 0.0, 0.0), 1.0)
                            >>> sphere.intersects(Plane(Point(1.0, 0.0, 0.0), Vector3d(0.0, 0.0, 1.0)))  # True
        """
    def is_defined(self) -> bool:
        """
                        Check if the sphere is defined.
        
                        Returns:
                            bool: True if the sphere is defined, False otherwise.
        
                        Example:
                            >>> sphere = Sphere(Point(0.0, 0.0, 0.0), 1.0)
                            >>> sphere.is_defined()  # True
        """
    def is_unitary(self) -> bool:
        """
                        Check if the sphere is a unit sphere (radius = 1).
        
                        Returns:
                            bool: True if the sphere has unit radius, False otherwise.
        
                        Example:
                            >>> sphere = Sphere(Point(0.0, 0.0, 0.0), 1.0)
                            >>> sphere.is_unitary()  # True
        """
def set_point_3_array(arg0: list[Point]) -> None:
    ...
