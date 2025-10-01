from __future__ import annotations
import numpy
import ostk.core.type
import typing
__all__ = ['EulerAngle', 'Quaternion', 'RotationMatrix', 'RotationVector', 'set_quaternion_array']
class EulerAngle:
    class AxisSequence:
        """
        Members:
        
          Undefined
        
          XYZ
        
          ZXY
        
          ZYX
        """
        Undefined: typing.ClassVar[EulerAngle.AxisSequence]  # value = <AxisSequence.Undefined: 0>
        XYZ: typing.ClassVar[EulerAngle.AxisSequence]  # value = <AxisSequence.XYZ: 1>
        ZXY: typing.ClassVar[EulerAngle.AxisSequence]  # value = <AxisSequence.ZXY: 2>
        ZYX: typing.ClassVar[EulerAngle.AxisSequence]  # value = <AxisSequence.ZYX: 3>
        __members__: typing.ClassVar[dict[str, EulerAngle.AxisSequence]]  # value = {'Undefined': <AxisSequence.Undefined: 0>, 'XYZ': <AxisSequence.XYZ: 1>, 'ZXY': <AxisSequence.ZXY: 2>, 'ZYX': <AxisSequence.ZYX: 3>}
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
    def quaternion(quaternion: Quaternion, axis_sequence: typing.Any) -> EulerAngle:
        """
                        Create Euler angles from a quaternion with specified axis sequence.
        
                        Args:
                            quaternion (Quaternion): The quaternion to convert.
                            axis_sequence (EulerAngle.AxisSequence): The desired axis sequence.
        
                        Returns:
                            EulerAngle: The equivalent Euler angles.
        
                        Example:
                            >>> quat = Quaternion.unit()
                            >>> euler = EulerAngle.quaternion(quat, EulerAngle.AxisSequence.XYZ)
        """
    @staticmethod
    def rotation_matrix(rotation_matrix: RotationMatrix, axis_sequence: typing.Any) -> EulerAngle:
        ...
    @staticmethod
    def rotation_vector(rotation_vector: RotationVector, axis_sequence: typing.Any) -> EulerAngle:
        ...
    @staticmethod
    def undefined() -> EulerAngle:
        """
                        Create an undefined Euler angle.
        
                        Returns:
                            EulerAngle: An undefined Euler angle object.
        
                        Example:
                            >>> undefined_euler = EulerAngle.undefined()
                            >>> undefined_euler.is_defined()  # False
        """
    @staticmethod
    def unit() -> EulerAngle:
        """
                        Create a unit Euler angle (no rotation).
        
                        Returns:
                            EulerAngle: A unit Euler angle representing no rotation.
        
                        Example:
                            >>> unit_euler = EulerAngle.unit()
                            >>> unit_euler.is_unitary()  # True
        """
    @staticmethod
    def xyz(phi: typing.Any, theta: typing.Any, psi: typing.Any) -> EulerAngle:
        """
                        Create Euler angles with XYZ axis sequence.
        
                        Args:
                            phi (Angle): The first rotation angle around X-axis.
                            theta (Angle): The second rotation angle around Y-axis.
                            psi (Angle): The third rotation angle around Z-axis.
        
                        Returns:
                            EulerAngle: An Euler angle with XYZ sequence.
        
                        Example:
                            >>> euler = EulerAngle.xyz(Angle.degrees(30.0), Angle.degrees(45.0), Angle.degrees(60.0))
        """
    @staticmethod
    def zxy(phi: typing.Any, theta: typing.Any, psi: typing.Any) -> EulerAngle:
        """
                        Create Euler angles with ZXY axis sequence.
        
                        Args:
                            phi (Angle): The first rotation angle around Z-axis.
                            theta (Angle): The second rotation angle around X-axis.
                            psi (Angle): The third rotation angle around Y-axis.
        
                        Returns:
                            EulerAngle: An Euler angle with ZXY sequence.
        
                        Example:
                            >>> euler = EulerAngle.zxy(Angle.degrees(30.0), Angle.degrees(45.0), Angle.degrees(60.0))
        """
    @staticmethod
    def zyx(phi: typing.Any, theta: typing.Any, psi: typing.Any) -> EulerAngle:
        """
                        Create Euler angles with ZYX axis sequence.
        
                        Args:
                            phi (Angle): The first rotation angle around Z-axis.
                            theta (Angle): The second rotation angle around Y-axis.
                            psi (Angle): The third rotation angle around X-axis.
        
                        Returns:
                            EulerAngle: An Euler angle with ZYX sequence.
        
                        Example:
                            >>> euler = EulerAngle.zyx(Angle.degrees(30.0), Angle.degrees(45.0), Angle.degrees(60.0))
        """
    def __eq__(self, arg0: EulerAngle) -> bool:
        ...
    @typing.overload
    def __init__(self, phi: typing.Any, theta: typing.Any, psi: typing.Any, axis_sequence: typing.Any) -> None:
        """
                        Create Euler angles from three angle components and axis sequence.
        
                        Args:
                            phi (Angle): The first rotation angle.
                            theta (Angle): The second rotation angle.
                            psi (Angle): The third rotation angle.
                            axis_sequence (EulerAngle.AxisSequence): The axis sequence (XYZ, ZXY, ZYX).
        
                        Example:
                            >>> phi = Angle.degrees(30.0)
                            >>> theta = Angle.degrees(45.0)
                            >>> psi = Angle.degrees(60.0)
                            >>> euler = EulerAngle(phi, theta, psi, EulerAngle.AxisSequence.XYZ)
        """
    @typing.overload
    def __init__(self, vector: numpy.ndarray[numpy.float64[3, 1]], angle_unit: typing.Any, axis_sequence: typing.Any) -> None:
        """
                        Create Euler angles from a 3D vector with specified angle unit and axis sequence.
        
                        Args:
                            vector (np.array): Vector containing the three angle values.
                            angle_unit (Angle.Unit): The unit of the angles in the vector.
                            axis_sequence (EulerAngle.AxisSequence): The axis sequence.
        
                        Example:
                            >>> vector = np.array([30.0, 45.0, 60.0])
                            >>> euler = EulerAngle(vector, Angle.Unit.Degree, EulerAngle.AxisSequence.XYZ)
        """
    def __ne__(self, arg0: EulerAngle) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __str__(self) -> str:
        ...
    def is_defined(self) -> bool:
        """
                        Check if the Euler angle is defined.
        
                        Returns:
                            bool: True if the Euler angle is defined, False otherwise.
        
                        Example:
                            >>> euler = EulerAngle(phi, theta, psi, EulerAngle.AxisSequence.XYZ)
                            >>> euler.is_defined()  # True
        """
    def is_near(self, euler_angle: EulerAngle, angular_tolerance: typing.Any) -> bool:
        """
                        Check if this Euler angle is near another Euler angle within tolerance.
        
                        Args:
                            euler_angle (EulerAngle): The Euler angle to compare with.
                            angular_tolerance (Angle): The angular tolerance for comparison.
        
                        Returns:
                            bool: True if angles are within tolerance, False otherwise.
        
                        Example:
                            >>> euler1 = EulerAngle(phi1, theta1, psi1, sequence)
                            >>> euler2 = EulerAngle(phi2, theta2, psi2, sequence)
                            >>> euler1.is_near(euler2, Angle.degrees(1.0))
        """
    def is_unitary(self) -> bool:
        """
                        Check if the Euler angle represents a unit rotation.
        
                        Returns:
                            bool: True if the Euler angle is unitary, False otherwise.
        
                        Example:
                            >>> euler = EulerAngle.unit()
                            >>> euler.is_unitary()  # True
        """
    @typing.overload
    def to_string(self) -> ostk.core.type.String:
        ...
    @typing.overload
    def to_string(self, angle_unit: typing.Any) -> ostk.core.type.String:
        ...
    def to_vector(self, angle_unit: typing.Any) -> numpy.ndarray[numpy.float64[3, 1]]:
        """
                        Convert the Euler angle to a 3D vector with specified unit.
        
                        Args:
                            angle_unit (Angle.Unit): The unit for the output vector angles.
        
                        Returns:
                            Vector3d: A vector containing [phi, theta, psi] in the specified unit.
        
                        Example:
                            >>> euler = EulerAngle(phi, theta, psi, EulerAngle.AxisSequence.XYZ)
                            >>> vector = euler.to_vector(Angle.Unit.Degree)
        """
    @property
    def axis_sequence(self) -> ...:
        ...
    @property
    def phi(self) -> ...:
        ...
    @property
    def psi(self) -> ...:
        ...
    @property
    def theta(self) -> ...:
        ...
class Quaternion:
    class Format:
        """
        Members:
        
          XYZS
        
          SXYZ
        """
        SXYZ: typing.ClassVar[Quaternion.Format]  # value = <Format.SXYZ: 1>
        XYZS: typing.ClassVar[Quaternion.Format]  # value = <Format.XYZS: 0>
        __members__: typing.ClassVar[dict[str, Quaternion.Format]]  # value = {'XYZS': <Format.XYZS: 0>, 'SXYZ': <Format.SXYZ: 1>}
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
    def euler_angle(euler_angle: typing.Any) -> Quaternion:
        """
                        Create a quaternion from Euler angles.
        
                        Args:
                            euler_angle (EulerAngle): The Euler angles.
        
                        Returns:
                            Quaternion: The quaternion representing the rotation.
        
                        Example:
                            >>> ea = EulerAngle.zyx(Angle.radians(0.1), Angle.radians(0.2), Angle.radians(0.3))
                            >>> q = Quaternion.euler_angle(ea)
        """
    @staticmethod
    def lerp(first_quaternion: Quaternion, second_quaternion: Quaternion, ratio: ostk.core.type.Real) -> Quaternion:
        """
                        Linear interpolation between two quaternions.
        
                        Args:
                            first_quaternion (Quaternion): The first quaternion.
                            second_quaternion (Quaternion): The second quaternion.
                            ratio (float): The interpolation ratio (0.0 to 1.0).
        
                        Returns:
                            Quaternion: The interpolated quaternion.
        
                        Example:
                            >>> q1 = Quaternion.unit()
                            >>> q2 = Quaternion(0.1, 0.2, 0.3, 0.9, Quaternion.Format.XYZS)
                            >>> q_interp = Quaternion.lerp(q1, q2, 0.5)
        """
    @staticmethod
    def nlerp(first_quaternion: Quaternion, second_quaternion: Quaternion, ratio: ostk.core.type.Real) -> Quaternion:
        """
                        Normalized linear interpolation between two quaternions.
        
                        Args:
                            first_quaternion (Quaternion): The first quaternion.
                            second_quaternion (Quaternion): The second quaternion.
                            ratio (float): The interpolation ratio (0.0 to 1.0).
        
                        Returns:
                            Quaternion: The normalized interpolated quaternion.
        
                        Example:
                            >>> q1 = Quaternion.unit()
                            >>> q2 = Quaternion(0.1, 0.2, 0.3, 0.9, Quaternion.Format.XYZS)
                            >>> q_interp = Quaternion.nlerp(q1, q2, 0.5)
        """
    @staticmethod
    def parse(string: ostk.core.type.String, format: typing.Any) -> Quaternion:
        """
                        Parse a quaternion from a string.
        
                        Args:
                            string (str): The string representation of the quaternion.
                            format (Quaternion.Format): The format of the quaternion.
        
                        Returns:
                            Quaternion: The parsed quaternion.
        
                        Example:
                            >>> q = Quaternion.parse("[0.0, 0.0, 0.0, 1.0]", Quaternion.Format.XYZS)
        """
    @staticmethod
    def rotation_matrix(rotation_matrix: typing.Any) -> Quaternion:
        """
                        Create a quaternion from a rotation matrix.
        
                        Args:
                            rotation_matrix (RotationMatrix): The rotation matrix.
        
                        Returns:
                            Quaternion: The quaternion representing the rotation.
        
                        Example:
                            >>> rm = RotationMatrix.identity()
                            >>> q = Quaternion.rotation_matrix(rm)
        """
    @staticmethod
    def rotation_vector(rotation_vector: typing.Any) -> Quaternion:
        """
                        Create a quaternion from a rotation vector.
        
                        Args:
                            rotation_vector (RotationVector): The rotation vector.
        
                        Returns:
                            Quaternion: The quaternion representing the rotation.
        
                        Example:
                            >>> rv = RotationVector([0.1, 0.2, 0.3], Angle.radians(1.0))
                            >>> q = Quaternion.rotation_vector(rv)
        """
    @staticmethod
    def shortest_rotation(first_vector: numpy.ndarray[numpy.float64[3, 1]], second_vector: numpy.ndarray[numpy.float64[3, 1]]) -> Quaternion:
        """
                        Create a quaternion representing the shortest rotation between two vectors.
        
                        Args:
                            first_vector (np.array): The first vector.
                            second_vector (np.array): The second vector.
        
                        Returns:
                            Quaternion: The quaternion representing the shortest rotation.
        
                        Example:
                            >>> v1 = np.array([1.0, 0.0, 0.0])
                            >>> v2 = np.array([0.0, 1.0, 0.0])
                            >>> q = Quaternion.shortest_rotation(v1, v2)
        """
    @staticmethod
    def slerp(first_quaternion: Quaternion, second_quaternion: Quaternion, ratio: ostk.core.type.Real) -> Quaternion:
        """
                        Spherical linear interpolation between two quaternions.
        
                        Args:
                            first_quaternion (Quaternion): The first quaternion.
                            second_quaternion (Quaternion): The second quaternion.
                            ratio (float): The interpolation ratio (0.0 to 1.0).
        
                        Returns:
                            Quaternion: The spherically interpolated quaternion.
        
                        Example:
                            >>> q1 = Quaternion.unit()
                            >>> q2 = Quaternion(0.1, 0.2, 0.3, 0.9, Quaternion.Format.XYZS)
                            >>> q_interp = Quaternion.slerp(q1, q2, 0.5)
        """
    @staticmethod
    def undefined() -> Quaternion:
        """
                        Create an undefined quaternion.
        
                        Returns:
                            Quaternion: An undefined quaternion.
        
                        Example:
                            >>> q = Quaternion.undefined()
                            >>> q.is_defined()  # False
        """
    @staticmethod
    def unit() -> Quaternion:
        """
                        Create a unit quaternion (identity rotation).
        
                        Returns:
                            Quaternion: A unit quaternion.
        
                        Example:
                            >>> q = Quaternion.unit()
                            >>> q.is_unitary()  # True
        """
    @staticmethod
    def xyzs(first_component: ostk.core.type.Real, second_component: ostk.core.type.Real, third_component: ostk.core.type.Real, fourth_component: ostk.core.type.Real) -> Quaternion:
        """
                        Create a quaternion in XYZS format.
        
                        Args:
                            first_component (float): The x component.
                            second_component (float): The y component.
                            third_component (float): The z component.
                            fourth_component (float): The s component.
        
                        Returns:
                            Quaternion: The quaternion in XYZS format.
        
                        Example:
                            >>> q = Quaternion.xyzs(0.0, 0.0, 0.0, 1.0)
        """
    def __add__(self, arg0: Quaternion) -> Quaternion:
        ...
    def __eq__(self, arg0: Quaternion) -> bool:
        ...
    def __iadd__(self, arg0: Quaternion) -> Quaternion:
        ...
    @typing.overload
    def __init__(self, first_component: ostk.core.type.Real, second_component: ostk.core.type.Real, third_component: ostk.core.type.Real, fourth_component: ostk.core.type.Real, format: typing.Any) -> None:
        """
                        Create a quaternion from four components and format.
        
                        Args:
                            first_component (float): First component (x or w depending on format).
                            second_component (float): Second component (y or x depending on format).
                            third_component (float): Third component (z or y depending on format).
                            fourth_component (float): Fourth component (w or z depending on format).
                            format (Quaternion.Format): The quaternion format (XYZS or SXYZ).
        
                        Example:
                            >>> q = Quaternion(0.0, 0.0, 0.0, 1.0, Quaternion.Format.XYZS)
                            >>> q = Quaternion(1.0, 0.0, 0.0, 0.0, Quaternion.Format.SXYZ)
        """
    @typing.overload
    def __init__(self, vector: numpy.ndarray[numpy.float64[4, 1]], format: typing.Any) -> None:
        """
                        Create a quaternion from a 4D vector and format.
        
                        Args:
                            vector (np.array): The 4D vector containing quaternion components.
                            format (Quaternion.Format): The quaternion format.
        
                        Example:
                            >>> vector = np.array([0.0, 0.0, 0.0, 1.0])
                            >>> q = Quaternion(vector, Quaternion.Format.XYZS)
        """
    @typing.overload
    def __init__(self, vector_part: numpy.ndarray[numpy.float64[3, 1]], scalar_part: ostk.core.type.Real) -> None:
        """
                        Create a quaternion from vector and scalar parts.
        
                        Args:
                            vector_part (np.array): The vector part (x, y, z components).
                            scalar_part (float): The scalar part (s component).
        
                        Example:
                            >>> vector_part = np.array([0.0, 0.0, 0.0])
                            >>> scalar_part = 1.0
                            >>> q = Quaternion(vector_part, scalar_part)
        """
    @typing.overload
    def __init__(self, quaternion: Quaternion) -> None:
        """
                        Create a quaternion by copying another quaternion.
        
                        Args:
                            quaternion (Quaternion): The quaternion to copy.
        
                        Example:
                            >>> original = Quaternion(0.0, 0.0, 0.0, 1.0, Quaternion.Format.XYZS)
                            >>> copy = Quaternion(original)
        """
    @typing.overload
    def __mul__(self, arg0: Quaternion) -> Quaternion:
        ...
    @typing.overload
    def __mul__(self, arg0: numpy.ndarray[numpy.float64[3, 1]]) -> numpy.ndarray[numpy.float64[3, 1]]:
        ...
    @typing.overload
    def __mul__(self, arg0: float) -> Quaternion:
        ...
    def __ne__(self, arg0: Quaternion) -> bool:
        ...
    def __pow__(self, arg0: float) -> Quaternion:
        ...
    def __repr__(self) -> str:
        ...
    def __rmul__(self, arg0: float) -> Quaternion:
        ...
    def __str__(self) -> str:
        ...
    def __truediv__(self, arg0: Quaternion) -> Quaternion:
        ...
    def angular_difference_with(self, quaternion: Quaternion) -> ...:
        """
                        Compute the angular difference with another quaternion.
        
                        Args:
                            quaternion (Quaternion): The quaternion to compare with.
        
                        Returns:
                            Angle: The angular difference.
        
                        Example:
                            >>> q1 = Quaternion.unit()
                            >>> q2 = Quaternion(0.1, 0.2, 0.3, 0.9, Quaternion.Format.XYZS)
                            >>> angle = q1.angular_difference_with(q2)
        """
    def conjugate(self) -> None:
        """
                        Conjugate the quaternion in-place.
        
                        Example:
                            >>> q = Quaternion(1.0, 2.0, 3.0, 4.0, Quaternion.Format.XYZS)
                            >>> q.conjugate()
        """
    def cross_multiply(self, quaternion: Quaternion) -> Quaternion:
        """
                        Perform cross multiplication with another quaternion.
        
                        Args:
                            quaternion (Quaternion): The quaternion to multiply with.
        
                        Returns:
                            Quaternion: The result of cross multiplication.
        
                        Example:
                            >>> q1 = Quaternion.unit()
                            >>> q2 = Quaternion(0.1, 0.2, 0.3, 0.9, Quaternion.Format.XYZS)
                            >>> result = q1.cross_multiply(q2)
        """
    def dot_multiply(self, quaternion: Quaternion) -> Quaternion:
        """
                        Perform dot multiplication with another quaternion.
        
                        Args:
                            quaternion (Quaternion): The quaternion to multiply with.
        
                        Returns:
                            Quaternion: The result of dot multiplication.
        
                        Example:
                            >>> q1 = Quaternion.unit()
                            >>> q2 = Quaternion(0.1, 0.2, 0.3, 0.9, Quaternion.Format.XYZS)
                            >>> result = q1.dot_multiply(q2)
        """
    def dot_product(self, quaternion: Quaternion) -> ostk.core.type.Real:
        """
                        Compute the dot product with another quaternion.
        
                        Args:
                            quaternion (Quaternion): The quaternion to compute dot product with.
        
                        Returns:
                            float: The dot product result.
        
                        Example:
                            >>> q1 = Quaternion.unit()
                            >>> q2 = Quaternion(0.1, 0.2, 0.3, 0.9, Quaternion.Format.XYZS)
                            >>> dot = q1.dot_product(q2)
        """
    def exp(self) -> Quaternion:
        """
                        Compute the exponential of the quaternion.
        
                        Returns:
                            Quaternion: The exponential of the quaternion.
        
                        Example:
                            >>> q = Quaternion(0.1, 0.2, 0.3, 0.0, Quaternion.Format.XYZS)
                            >>> exp_q = q.exp()
        """
    def get_scalar_part(self) -> ostk.core.type.Real:
        """
                        Get the scalar part of the quaternion.
        
                        Returns:
                            float: The scalar part.
        
                        Example:
                            >>> q = Quaternion(0.0, 0.0, 0.0, 1.0, Quaternion.Format.XYZS)
                            >>> q.get_scalar_part()  # 1.0
        """
    def get_vector_part(self) -> numpy.ndarray[numpy.float64[3, 1]]:
        """
                        Get the vector part of the quaternion.
        
                        Returns:
                            Vector3d: The vector part.
        """
    def inverse(self) -> None:
        """
                        Invert the quaternion in-place.
        
                        Example:
                            >>> q = Quaternion.unit()
                            >>> q.inverse()
        """
    def is_defined(self) -> bool:
        """
                        Check if the quaternion is defined.
        
                        Returns:
                            bool: True if the quaternion is defined, False otherwise.
        """
    def is_near(self, quaternion: Quaternion, angular_tolerance: typing.Any) -> bool:
        """
                        Check if the quaternion is near another quaternion.
        
                        Returns:
                            bool: True if the quaternion is near another quaternion, False otherwise.
        """
    def is_unitary(self, norm_tolerance: ostk.core.type.Real = ...) -> bool:
        """
                        Check if the quaternion is unitary.
        
                        Returns:
                            bool: True if the quaternion is unitary, False otherwise.
        """
    def log(self) -> Quaternion:
        """
                        Compute the natural logarithm of the quaternion.
        
                        Returns:
                            Quaternion: The natural logarithm of the quaternion.
        
                        Example:
                            >>> q = Quaternion.unit()
                            >>> log_q = q.log()
        """
    def norm(self) -> ostk.core.type.Real:
        """
                        Compute the norm (magnitude) of the quaternion.
        
                        Returns:
                            float: The norm of the quaternion.
        
                        Example:
                            >>> q = Quaternion(1.0, 2.0, 3.0, 4.0, Quaternion.Format.XYZS)
                            >>> magnitude = q.norm()
        """
    def normalize(self) -> None:
        """
                        Normalize the quaternion in-place.
        
                        Example:
                            >>> q = Quaternion(1.0, 1.0, 1.0, 1.0, Quaternion.Format.XYZS)
                            >>> q.normalize()
        """
    def pow(self, value: ostk.core.type.Real) -> Quaternion:
        """
                        Raise the quaternion to a power.
        
                        Args:
                            value (float): The exponent.
        
                        Returns:
                            Quaternion: The quaternion raised to the power.
        
                        Example:
                            >>> q = Quaternion.unit()
                            >>> powered = q.pow(2.0)
        """
    def rectify(self) -> None:
        """
                        Rectify the quaternion in-place (ensure positive scalar part).
        
                        Example:
                            >>> q = Quaternion(0.0, 0.0, 0.0, -1.0, Quaternion.Format.XYZS)
                            >>> q.rectify()
        """
    def rotate_vector(self, vector: numpy.ndarray[numpy.float64[3, 1]], norm_tolerance: ostk.core.type.Real = ...) -> numpy.ndarray[numpy.float64[3, 1]]:
        """
                        Rotate a vector using this quaternion.
        
                        Args:
                            vector (np.array): The 3D vector to rotate.
                            norm_tolerance (float, optional): Tolerance for normalization check.
        
                        Returns:
                            Vector3d: The rotated vector.
        
                        Example:
                            >>> q = Quaternion.unit()
                            >>> vector = np.array([1.0, 0.0, 0.0])
                            >>> rotated = q.rotate_vector(vector)
        """
    def s(self) -> ostk.core.type.Real:
        """
                        Get the s-coordinate of the quaternion.
        
                        Returns:
                            float: The s-coordinate.
        """
    def to_conjugate(self) -> Quaternion:
        """
                        Get the conjugate of the quaternion.
        
                        Returns:
                            Quaternion: The conjugate quaternion.
        
                        Example:
                            >>> q = Quaternion(1.0, 2.0, 3.0, 4.0, Quaternion.Format.XYZS)
                            >>> conjugate = q.to_conjugate()
        """
    def to_inverse(self) -> Quaternion:
        """
                        Get the inverse of the quaternion.
        
                        Returns:
                            Quaternion: The inverse quaternion.
        
                        Example:
                            >>> q = Quaternion.unit()
                            >>> inverse = q.to_inverse()
        """
    def to_normalized(self) -> Quaternion:
        """
                        Get a normalized copy of the quaternion.
        
                        Returns:
                            Quaternion: The normalized quaternion.
        
                        Example:
                            >>> q = Quaternion(1.0, 1.0, 1.0, 1.0, Quaternion.Format.XYZS)
                            >>> normalized = q.to_normalized()
        """
    @typing.overload
    def to_string(self) -> ostk.core.type.String:
        """
                        Convert the quaternion to string representation.
        
                        Returns:
                            str: String representation of the quaternion.
        
                        Example:
                            >>> q = Quaternion.unit()
                            >>> q.to_string()
        """
    @typing.overload
    def to_string(self, format: typing.Any) -> ostk.core.type.String:
        """
                        Convert the quaternion to string representation with specified format.
        
                        Args:
                            format (Quaternion.Format): The format for string representation.
        
                        Returns:
                            str: String representation of the quaternion.
        
                        Example:
                            >>> q = Quaternion.unit()
                            >>> q.to_string(Quaternion.Format.SXYZ)
        """
    def to_vector(self, format: typing.Any) -> numpy.ndarray[numpy.float64[4, 1]]:
        """
                        Convert the quaternion to a 4D vector.
        
                        Args:
                            format (Quaternion.Format): The format for the vector components.
        
                        Returns:
                            Vector4d: The quaternion as a 4D vector.
        
                        Example:
                            >>> q = Quaternion.unit()
                            >>> vector = q.to_vector(Quaternion.Format.XYZS)
        """
    def x(self) -> ostk.core.type.Real:
        """
                        Get the x-coordinate of the quaternion.
        
                        Returns:
                            float: The x-coordinate.
        """
    def y(self) -> ostk.core.type.Real:
        """
                        Get the y-coordinate of the quaternion.
        
                        Returns:
                            float: The y-coordinate.
        """
    def z(self) -> ostk.core.type.Real:
        """
                        Get the z-coordinate of the quaternion.
        
                        Returns:
                            float: The z-coordinate.
        """
class RotationMatrix:
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def columns(first_column: numpy.ndarray[numpy.float64[3, 1]], second_column: numpy.ndarray[numpy.float64[3, 1]], third_column: numpy.ndarray[numpy.float64[3, 1]]) -> RotationMatrix:
        """
                        Create a rotation matrix from column vectors.
        
                        Args:
                            first_column (Vector3d): The first column of the rotation matrix.
                            second_column (Vector3d): The second column of the rotation matrix.
                            third_column (Vector3d): The third column of the rotation matrix.
        
                        Returns:
                            RotationMatrix: A rotation matrix from column vectors.
        
                        Example:
                            >>> rot_matrix = RotationMatrix.columns(Vector3d(1.0, 0.0, 0.0), Vector3d(0.0, 1.0, 0.0), Vector3d(0.0, 0.0, 1.0))
        """
    @staticmethod
    def euler_angle(euler_angle: typing.Any) -> RotationMatrix:
        """
                        Create a rotation matrix from Euler angles.
        
                        Args:
                            euler_angle (EulerAngle): The Euler angles to convert.
        
                        Returns:
                            RotationMatrix: The equivalent rotation matrix.
        
                        Example:
                            >>> euler = EulerAngle.unit()
                            >>> rot_matrix = RotationMatrix.euler_angle(euler)
        """
    @staticmethod
    def quaternion(quaternion: Quaternion) -> RotationMatrix:
        """
                        Create a rotation matrix from a quaternion.
        
                        Args:
                            quaternion (Quaternion): The quaternion to convert.
        
                        Returns:
                            RotationMatrix: The equivalent rotation matrix.
        
                        Example:
                            >>> quat = Quaternion.unit()
                            >>> rot_matrix = RotationMatrix.quaternion(quat)
        """
    @staticmethod
    def rotation_vector(rotation_vector: RotationVector) -> RotationMatrix:
        """
                        Create a rotation matrix from a rotation vector.
        
                        Args:
                            rotation_vector (RotationVector): The rotation vector to convert.
        
                        Returns:
                            RotationMatrix: The equivalent rotation matrix.
        
                        Example:
                            >>> rot_vector = RotationVector.unit()
                            >>> rot_matrix = RotationMatrix.rotation_vector(rot_vector)
        """
    @staticmethod
    def rows(first_row: numpy.ndarray[numpy.float64[3, 1]], second_row: numpy.ndarray[numpy.float64[3, 1]], third_row: numpy.ndarray[numpy.float64[3, 1]]) -> RotationMatrix:
        """
                        Create a rotation matrix from row vectors.
        
                        Args:
                            first_row (Vector3d): The first row of the rotation matrix.
                            second_row (Vector3d): The second row of the rotation matrix.
                            third_row (Vector3d): The third row of the rotation matrix.
        
                        Returns:
                            RotationMatrix: A rotation matrix from row vectors.
        
                        Example:
                            >>> rot_matrix = RotationMatrix.rows(Vector3d(1.0, 0.0, 0.0), Vector3d(0.0, 1.0, 0.0), Vector3d(0.0, 0.0, 1.0))
        """
    @staticmethod
    def rx(rotation_angle: typing.Any) -> RotationMatrix:
        """
                        Create a rotation matrix for rotation around the X-axis.
        
                        Args:
                            rotation_angle (Angle): The angle of rotation around X-axis.
        
                        Returns:
                            RotationMatrix: A rotation matrix for X-axis rotation.
        
                        Example:
                            >>> rot_x = RotationMatrix.rx(Angle.degrees(90.0))
        """
    @staticmethod
    def ry(rotation_angle: typing.Any) -> RotationMatrix:
        """
                        Create a rotation matrix for rotation around the Y-axis.
        
                        Args:
                            rotation_angle (Angle): The angle of rotation around Y-axis.
        
                        Returns:
                            RotationMatrix: A rotation matrix for Y-axis rotation.
        
                        Example:
                            >>> rot_y = RotationMatrix.ry(Angle.degrees(90.0))
        """
    @staticmethod
    def rz(rotation_angle: typing.Any) -> RotationMatrix:
        """
                        Create a rotation matrix for rotation around the Z-axis.
        
                        Args:
                            rotation_angle (Angle): The angle of rotation around Z-axis.
        
                        Returns:
                            RotationMatrix: A rotation matrix for Z-axis rotation.
        
                        Example:
                            >>> rot_z = RotationMatrix.rz(Angle.degrees(90.0))
        """
    @staticmethod
    def undefined() -> RotationMatrix:
        """
                        Create an undefined rotation matrix.
        
                        Returns:
                            RotationMatrix: An undefined rotation matrix.
        
                        Example:
                            >>> undefined_matrix = RotationMatrix.undefined()
                            >>> undefined_matrix.is_defined()  # False
        """
    @staticmethod
    def unit() -> RotationMatrix:
        """
                        Create a unit rotation matrix (identity matrix).
        
                        Returns:
                            RotationMatrix: The 3x3 identity rotation matrix.
        
                        Example:
                            >>> unit_matrix = RotationMatrix.unit()
                            >>> matrix = unit_matrix.get_matrix()  # 3x3 identity matrix
        """
    def __eq__(self, arg0: RotationMatrix) -> bool:
        ...
    @typing.overload
    def __init__(self, matrix: numpy.ndarray[numpy.float64[3, 3]]) -> None:
        """
                        Create a rotation matrix from a 3x3 matrix.
        
                        Args:
                            matrix (Matrix3d): A 3x3 matrix representing the rotation.
        
                        Example:
                            >>> matrix = Matrix3d.identity()
                            >>> rotation_matrix = RotationMatrix(matrix)
        """
    @typing.overload
    def __init__(self, first_coefficient: ostk.core.type.Real, second_coefficient: ostk.core.type.Real, third_coefficient: ostk.core.type.Real, fourth_coefficient: ostk.core.type.Real, fifth_coefficient: ostk.core.type.Real, sixth_coefficient: ostk.core.type.Real, seventh_coefficient: ostk.core.type.Real, eighth_coefficient: ostk.core.type.Real, ninth_coefficient: ostk.core.type.Real) -> None:
        """
                        Create a rotation matrix from nine coefficients (row-major order).
        
                        Args:
                            first_coefficient (float): Matrix element (0,0).
                            second_coefficient (float): Matrix element (0,1).
                            third_coefficient (float): Matrix element (0,2).
                            fourth_coefficient (float): Matrix element (1,0).
                            fifth_coefficient (float): Matrix element (1,1).
                            sixth_coefficient (float): Matrix element (1,2).
                            seventh_coefficient (float): Matrix element (2,0).
                            eighth_coefficient (float): Matrix element (2,1).
                            ninth_coefficient (float): Matrix element (2,2).
        
                        Example:
                            >>> rot_matrix = RotationMatrix(1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0)
        """
    @typing.overload
    def __mul__(self, arg0: RotationMatrix) -> RotationMatrix:
        ...
    @typing.overload
    def __mul__(self, arg0: numpy.ndarray[numpy.float64[3, 1]]) -> numpy.ndarray[numpy.float64[3, 1]]:
        ...
    def __ne__(self, arg0: RotationMatrix) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __str__(self) -> str:
        ...
    def get_column_at(self, index: int) -> numpy.ndarray[numpy.float64[3, 1]]:
        """
                        Get a column of the rotation matrix at specified index.
        
                        Args:
                            index (int): The column index (0, 1, or 2).
        
                        Returns:
                            Vector3d: The column vector at the specified index.
        
                        Example:
                            >>> rot_matrix = RotationMatrix.unit()
                            >>> first_column = rot_matrix.get_column_at(0)  # [1, 0, 0]
        """
    def get_matrix(self) -> numpy.ndarray[numpy.float64[3, 3]]:
        """
                        Get the underlying 3x3 matrix.
        
                        Returns:
                            Matrix3d: The 3x3 rotation matrix.
        
                        Example:
                            >>> rot_matrix = RotationMatrix.unit()
                            >>> matrix = rot_matrix.get_matrix()
        """
    def get_row_at(self, index: int) -> numpy.ndarray[numpy.float64[3, 1]]:
        """
                        Get a row of the rotation matrix at specified index.
        
                        Args:
                            index (int): The row index (0, 1, or 2).
        
                        Returns:
                            Vector3d: The row vector at the specified index.
        
                        Example:
                            >>> rot_matrix = RotationMatrix.unit()
                            >>> first_row = rot_matrix.get_row_at(0)  # [1, 0, 0]
        """
    def is_defined(self) -> bool:
        """
                        Check if the rotation matrix is defined.
        
                        Returns:
                            bool: True if the rotation matrix is defined, False otherwise.
        
                        Example:
                            >>> rot_matrix = RotationMatrix(Matrix3d.identity())
                            >>> rot_matrix.is_defined()  # True
        """
    def to_transposed(self) -> RotationMatrix:
        """
                        Get the transpose of this rotation matrix.
        
                        Returns:
                            RotationMatrix: The transposed rotation matrix.
        
                        Example:
                            >>> rot_matrix = RotationMatrix.rx(Angle.degrees(90.0))
                            >>> transposed = rot_matrix.to_transposed()
        """
    def transpose(self) -> None:
        """
                        Transpose the rotation matrix in place.
        
                        Example:
                            >>> rot_matrix = RotationMatrix.rx(Angle.degrees(90.0))
                            >>> rot_matrix.transpose()
        """
class RotationVector:
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def euler_angle(euler_angle: typing.Any) -> RotationVector:
        """
                        Create a rotation vector from Euler angles.
        
                        Args:
                            euler_angle (EulerAngle): The Euler angles to convert.
        
                        Returns:
                            RotationVector: The equivalent rotation vector.
        
                        Example:
                            >>> ea = EulerAngle.zyx(Angle.degrees(30), Angle.degrees(45), Angle.degrees(60))
                            >>> rot_vector = RotationVector.euler_angle(ea)
        """
    @staticmethod
    def quaternion(quaternion: Quaternion) -> RotationVector:
        """
                        Create a rotation vector from a quaternion.
        
                        Args:
                            quaternion (Quaternion): The quaternion to convert.
        
                        Returns:
                            RotationVector: The equivalent rotation vector.
        
                        Example:
                            >>> q = Quaternion.unit()
                            >>> rot_vector = RotationVector.quaternion(q)
        """
    @staticmethod
    def rotation_matrix(rotation_matrix: typing.Any) -> RotationVector:
        """
                        Create a rotation vector from a rotation matrix.
        
                        Args:
                            rotation_matrix (RotationMatrix): The rotation matrix to convert.
        
                        Returns:
                            RotationVector: The equivalent rotation vector.
        
                        Example:
                            >>> rm = RotationMatrix.identity()
                            >>> rot_vector = RotationVector.rotation_matrix(rm)
        """
    @staticmethod
    def undefined() -> RotationVector:
        """
                        Create an undefined rotation vector.
        
                        Returns:
                            RotationVector: An undefined rotation vector.
        
                        Example:
                            >>> undefined_vector = RotationVector.undefined()
                            >>> undefined_vector.is_defined()  # False
        """
    @staticmethod
    def unit() -> RotationVector:
        """
                        Create a unit rotation vector (no rotation).
        
                        Returns:
                            RotationVector: A rotation vector representing no rotation.
        
                        Example:
                            >>> unit_vector = RotationVector.unit()
                            >>> angle = unit_vector.get_angle()  # 0 degrees
        """
    @staticmethod
    def x(angle: typing.Any) -> RotationVector:
        """
                        Create a rotation vector around the x-axis.
        
                        Args:
                            angle (Angle): The rotation angle around the x-axis.
        
                        Returns:
                            RotationVector: A rotation vector around the x-axis.
        
                        Example:
                            >>> rot_vector = RotationVector.x(Angle.degrees(90.0))
        """
    @staticmethod
    def y(angle: typing.Any) -> RotationVector:
        """
                        Create a rotation vector around the y-axis.
        
                        Args:
                            angle (Angle): The rotation angle around the y-axis.
        
                        Returns:
                            RotationVector: A rotation vector around the y-axis.
        
                        Example:
                            >>> rot_vector = RotationVector.y(Angle.degrees(90.0))
        """
    @staticmethod
    def z(angle: typing.Any) -> RotationVector:
        """
                        Create a rotation vector around the z-axis.
        
                        Args:
                            angle (Angle): The rotation angle around the z-axis.
        
                        Returns:
                            RotationVector: A rotation vector around the z-axis.
        
                        Example:
                            >>> rot_vector = RotationVector.z(Angle.degrees(90.0))
        """
    def __eq__(self, arg0: RotationVector) -> bool:
        ...
    @typing.overload
    def __init__(self, axis: numpy.ndarray[numpy.float64[3, 1]], angle: typing.Any) -> None:
        """
                        Create a rotation vector from axis and angle.
        
                        Args:
                            axis (np.array): The rotation axis (will be normalized).
                            angle (Angle): The rotation angle around the axis.
        
                        Example:
                            >>> axis = np.array([0.0, 0.0, 1.0])
                            >>> angle = Angle.degrees(90.0)
                            >>> rot_vector = RotationVector(axis, angle)
        """
    @typing.overload
    def __init__(self, vector: numpy.ndarray[numpy.float64[3, 1]], angle_unit: typing.Any) -> None:
        """
                        Create a rotation vector from a vector representation.
        
                        Args:
                            vector (np.array): The rotation vector (magnitude represents angle).
                            angle_unit (Angle.Unit): The unit of the angle in the vector magnitude.
        
                        Example:
                            >>> vector = np.array([0.0, 0.0, 1.5708])  # π/2 in z-axis
                            >>> rot_vector = RotationVector(vector, Angle.Unit.Radian)
        """
    def __ne__(self, arg0: RotationVector) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __str__(self) -> str:
        ...
    def get_angle(self) -> ...:
        """
                        Get the rotation angle.
        
                        Returns:
                            Angle: The rotation angle around the axis.
        
                        Example:
                            >>> rot_vector = RotationVector(axis, Angle.degrees(90.0))
                            >>> angle = rot_vector.get_angle()  # 90 degrees
        """
    def get_axis(self) -> numpy.ndarray[numpy.float64[3, 1]]:
        """
                        Get the rotation axis vector.
        
                        Returns:
                            Vector3d: The normalized rotation axis.
        
                        Example:
                            >>> rot_vector = RotationVector(np.array([1.0, 0.0, 0.0]), angle)
                            >>> axis = rot_vector.get_axis()  # [1.0, 0.0, 0.0]
        """
    def is_defined(self) -> bool:
        """
                        Check if the rotation vector is defined.
        
                        Returns:
                            bool: True if the rotation vector is defined, False otherwise.
        
                        Example:
                            >>> rot_vector = RotationVector(axis, angle)
                            >>> rot_vector.is_defined()  # True
        """
    def rectify(self) -> None:
        """
                        Rectify the rotation vector in-place (ensure angle is in [0, π]).
        
                        Example:
                            >>> rot_vector = RotationVector(axis, Angle.degrees(270.0))
                            >>> rot_vector.rectify()  # Converts to equivalent rotation with angle ≤ π
        """
    @typing.overload
    def to_string(self) -> ostk.core.type.String:
        """
                        Convert the rotation vector to string representation.
        
                        Returns:
                            str: String representation of the rotation vector.
        
                        Example:
                            >>> rot_vector = RotationVector.unit()
                            >>> rot_vector.to_string()
        """
    @typing.overload
    def to_string(self, precision: ostk.core.type.Integer) -> ostk.core.type.String:
        """
                        Convert the rotation vector to string representation with specified precision.
        
                        Args:
                            precision (int): The precision for floating point numbers.
        
                        Returns:
                            str: String representation of the rotation vector.
        
                        Example:
                            >>> rot_vector = RotationVector.unit()
                            >>> rot_vector.to_string(3)
        """
def set_quaternion_array(arg0: list[Quaternion]) -> None:
    ...
