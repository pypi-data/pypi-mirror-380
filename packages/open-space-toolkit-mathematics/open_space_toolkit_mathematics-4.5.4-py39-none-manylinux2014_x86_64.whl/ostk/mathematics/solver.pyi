from __future__ import annotations
import numpy
import ostk.core.type
import typing
__all__ = ['NumericalSolver']
class NumericalSolver:
    class LogType:
        """
        Members:
        
          NoLog
        
          LogConstant
        
          LogAdaptive
        """
        LogAdaptive: typing.ClassVar[NumericalSolver.LogType]  # value = <LogType.LogAdaptive: 2>
        LogConstant: typing.ClassVar[NumericalSolver.LogType]  # value = <LogType.LogConstant: 1>
        NoLog: typing.ClassVar[NumericalSolver.LogType]  # value = <LogType.NoLog: 0>
        __members__: typing.ClassVar[dict[str, NumericalSolver.LogType]]  # value = {'NoLog': <LogType.NoLog: 0>, 'LogConstant': <LogType.LogConstant: 1>, 'LogAdaptive': <LogType.LogAdaptive: 2>}
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
    class StepperType:
        """
        Members:
        
          RungeKutta4
        
          RungeKuttaCashKarp54
        
          RungeKuttaFehlberg78
        
          RungeKuttaDopri5
        """
        RungeKutta4: typing.ClassVar[NumericalSolver.StepperType]  # value = <StepperType.RungeKutta4: 0>
        RungeKuttaCashKarp54: typing.ClassVar[NumericalSolver.StepperType]  # value = <StepperType.RungeKuttaCashKarp54: 1>
        RungeKuttaDopri5: typing.ClassVar[NumericalSolver.StepperType]  # value = <StepperType.RungeKuttaDopri5: 3>
        RungeKuttaFehlberg78: typing.ClassVar[NumericalSolver.StepperType]  # value = <StepperType.RungeKuttaFehlberg78: 2>
        __members__: typing.ClassVar[dict[str, NumericalSolver.StepperType]]  # value = {'RungeKutta4': <StepperType.RungeKutta4: 0>, 'RungeKuttaCashKarp54': <StepperType.RungeKuttaCashKarp54: 1>, 'RungeKuttaFehlberg78': <StepperType.RungeKuttaFehlberg78: 2>, 'RungeKuttaDopri5': <StepperType.RungeKuttaDopri5: 3>}
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
    def default() -> NumericalSolver:
        """
                            Create a default numerical solver.
        
                            Returns:
                                NumericalSolver: A solver with default settings.
        
                            Example:
                                >>> solver = NumericalSolver.default()
                                >>> solver.is_defined()  # True
        """
    @staticmethod
    def string_from_log_type(log_type: typing.Any) -> ostk.core.type.String:
        """
                            Get string representation of a log type.
        
                            Args:
                                log_type (NumericalSolver.LogType): The log type.
        
                            Returns:
                                str: String representation of the log type.
        
                            Example:
                                >>> NumericalSolver.string_from_log_type(NumericalSolver.LogType.NoLog)
        """
    @staticmethod
    def string_from_stepper_type(stepper_type: typing.Any) -> ostk.core.type.String:
        """
                            Get string representation of a stepper type.
        
                            Args:
                                stepper_type (NumericalSolver.StepperType): The stepper type.
        
                            Returns:
                                str: String representation of the stepper type.
        
                            Example:
                                >>> NumericalSolver.string_from_stepper_type(NumericalSolver.StepperType.RungeKutta4)
        """
    @staticmethod
    def undefined() -> NumericalSolver:
        """
                            Create an undefined numerical solver.
        
                            Returns:
                                NumericalSolver: An undefined solver.
        
                            Example:
                                >>> solver = NumericalSolver.undefined()
                                >>> solver.is_defined()  # False
        """
    def __eq__(self, arg0: NumericalSolver) -> bool:
        ...
    def __init__(self, log_type: typing.Any, stepper_type: typing.Any, time_step: ostk.core.type.Real, relative_tolerance: ostk.core.type.Real, absolute_tolerance: ostk.core.type.Real) -> None:
        """
                            Create a numerical solver with specified parameters.
        
                            Args:
                                log_type (NumericalSolver.LogType): The logging type for the solver.
                                stepper_type (NumericalSolver.StepperType): The stepper algorithm to use.
                                time_step (float): The time step for integration.
                                relative_tolerance (float): The relative tolerance for adaptive steppers.
                                absolute_tolerance (float): The absolute tolerance for adaptive steppers.
        
                            Example:
                                >>> solver = NumericalSolver(
                                ...     NumericalSolver.LogType.NoLog,
                                ...     NumericalSolver.StepperType.RungeKutta4,
                                ...     1.0, 1e-12, 1e-12
                                ... )
        """
    def __ne__(self, arg0: NumericalSolver) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __str__(self) -> str:
        ...
    def get_absolute_tolerance(self) -> ostk.core.type.Real:
        """
                            Get the absolute tolerance of the solver.
        
                            Returns:
                                float: The absolute tolerance value.
        
                            Example:
                                >>> solver = NumericalSolver.default()
                                >>> abs_tol = solver.get_absolute_tolerance()
        """
    def get_log_type(self) -> ...:
        """
                            Get the log type of the solver.
        
                            Returns:
                                NumericalSolver.LogType: The log type.
        
                            Example:
                                >>> solver = NumericalSolver.default()
                                >>> log_type = solver.get_log_type()
        """
    def get_observed_state_vectors(self) -> list[tuple[numpy.ndarray[numpy.float64[m, 1]], float]]:
        """
                            Get the observed state vectors from the last integration.
        
                            Returns:
                                list: List of observed state vectors during integration.
        
                            Example:
                                >>> solver = NumericalSolver.default()
                                >>> # After performing integration...
                                >>> states = solver.get_observed_state_vectors()
        """
    def get_relative_tolerance(self) -> ostk.core.type.Real:
        """
                            Get the relative tolerance of the solver.
        
                            Returns:
                                float: The relative tolerance value.
        
                            Example:
                                >>> solver = NumericalSolver.default()
                                >>> rel_tol = solver.get_relative_tolerance()
        """
    def get_stepper_type(self) -> ...:
        """
                            Get the stepper type of the solver.
        
                            Returns:
                                NumericalSolver.StepperType: The stepper type.
        
                            Example:
                                >>> solver = NumericalSolver.default()
                                >>> stepper_type = solver.get_stepper_type()
        """
    def get_time_step(self) -> ostk.core.type.Real:
        """
                            Get the time step of the solver.
        
                            Returns:
                                float: The time step value.
        
                            Example:
                                >>> solver = NumericalSolver.default()
                                >>> time_step = solver.get_time_step()
        """
    @typing.overload
    def integrate_duration(self, arg0: numpy.ndarray[numpy.float64[m, 1]], arg1: ostk.core.type.Real, arg2: typing.Any) -> tuple[numpy.ndarray[numpy.float64[m, 1]], float]:
        """
                            Integrate a system of differential equations for a specified duration.
        
                            Args:
                                state_vector (StateVector): Initial state vector.
                                duration_in_seconds (float): Integration duration in seconds.
                                system_of_equations (callable): Function defining the system of ODEs.
                                                               Signature: f(x, dxdt, t) -> StateVector
        
                            Returns:
                                StateVector: Final state vector after integration.
        
                            Example:
                                >>> def equations(x, dxdt, t):
                                ...     dxdt[0] = x[1]  # dx/dt = v
                                ...     dxdt[1] = -x[0]  # dv/dt = -x (harmonic oscillator)
                                ...     return dxdt
                                >>> solver = NumericalSolver.default()
                                >>> initial_state = [1.0, 0.0]  # x=1, v=0
                                >>> final_state = solver.integrate_duration(initial_state, 1.0, equations)
        """
    @typing.overload
    def integrate_duration(self, arg0: numpy.ndarray[numpy.float64[m, 1]], arg1: list[ostk.core.type.Real], arg2: typing.Any) -> list[tuple[numpy.ndarray[numpy.float64[m, 1]], float]]:
        """
                            Integrate a system of differential equations at multiple duration points.
        
                            Args:
                                state_vector (StateVector): Initial state vector.
                                duration_array (list): Array of duration values in seconds.
                                system_of_equations (callable): Function defining the system of ODEs.
                                                               Signature: f(x, dxdt, t) -> StateVector
        
                            Returns:
                                list: State vectors at each duration point.
        
                            Example:
                                >>> def equations(x, dxdt, t):
                                ...     dxdt[0] = x[1]  # dx/dt = v
                                ...     dxdt[1] = -x[0]  # dv/dt = -x (harmonic oscillator)
                                ...     return dxdt
                                >>> solver = NumericalSolver.default()
                                >>> initial_state = [1.0, 0.0]
                                >>> durations = [0.5, 1.0, 1.5]
                                >>> states = solver.integrate_duration(initial_state, durations, equations)
        """
    @typing.overload
    def integrate_time(self, arg0: numpy.ndarray[numpy.float64[m, 1]], arg1: ostk.core.type.Real, arg2: ostk.core.type.Real, arg3: typing.Any) -> tuple[numpy.ndarray[numpy.float64[m, 1]], float]:
        """
                            Integrate a system of differential equations from start to end time.
        
                            Args:
                                state_vector (StateVector): Initial state vector.
                                start_time (float): Integration start time.
                                end_time (float): Integration end time.
                                system_of_equations (callable): Function defining the system of ODEs.
                                                               Signature: f(x, dxdt, t) -> StateVector
        
                            Returns:
                                StateVector: Final state vector at end time.
        
                            Example:
                                >>> def equations(x, dxdt, t):
                                ...     dxdt[0] = x[1]  # dx/dt = v
                                ...     dxdt[1] = -x[0]  # dv/dt = -x (harmonic oscillator)
                                ...     return dxdt
                                >>> solver = NumericalSolver.default()
                                >>> initial_state = [1.0, 0.0]
                                >>> final_state = solver.integrate_time(initial_state, 0.0, 2.0, equations)
        """
    @typing.overload
    def integrate_time(self, arg0: numpy.ndarray[numpy.float64[m, 1]], arg1: ostk.core.type.Real, arg2: list[ostk.core.type.Real], arg3: typing.Any) -> list[tuple[numpy.ndarray[numpy.float64[m, 1]], float]]:
        """
                            Integrate a system of differential equations at specified time points.
        
                            Args:
                                state_vector (StateVector): Initial state vector.
                                start_time (float): Integration start time.
                                time_array (list): Array of time points to evaluate at.
                                system_of_equations (callable): Function defining the system of ODEs.
                                                               Signature: f(x, dxdt, t) -> StateVector
        
                            Returns:
                                list: State vectors at each time point.
        
                            Example:
                                >>> def equations(x, dxdt, t):
                                ...     dxdt[0] = x[1]  # dx/dt = v
                                ...     dxdt[1] = -x[0]  # dv/dt = -x (harmonic oscillator)
                                ...     return dxdt
                                >>> solver = NumericalSolver.default()
                                >>> initial_state = [1.0, 0.0]
                                >>> times = [0.5, 1.0, 1.5, 2.0]
                                >>> states = solver.integrate_time(initial_state, 0.0, times, equations)
        """
    def is_defined(self) -> bool:
        """
                            Check if the numerical solver is defined.
        
                            Returns:
                                bool: True if the solver is defined, False otherwise.
        
                            Example:
                                >>> solver = NumericalSolver.default()
                                >>> solver.is_defined()  # True
        """
