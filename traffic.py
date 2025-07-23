from enum import Enum, auto
from typing import List, Dict, Optional
from dataclasses import dataclass, field
import time
from datetime import timedelta


class Direction(Enum):
    """Enum representing the four cardinal directions."""
    NORTH = "North"
    SOUTH = "South"
    EAST = "East"
    WEST = "West"


class LaneType(Enum):
    """Enum representing the type of lane."""
    THROUGH = "through"
    LEFT_TURN = "left-turn"


class LightState(Enum):
    """Enum representing the possible traffic light states."""
    GREEN = auto()
    YELLOW = auto()
    RED = auto()


@dataclass
class Lane:
    """Represents a single lane in a traffic direction.
    
    Attributes:
        direction: The direction of the lane (N, S, E, W)
        lane_type: The type of lane (through or left-turn)
    """
    direction: Direction
    lane_type: LaneType

    def __str__(self) -> str:
        return f"{self.direction.value} {self.lane_type.value} lane"


@dataclass
class SignalPhase:
    """Manages the timing for a traffic signal phase.
    
    Attributes:
        green_time: Duration of green light in seconds (20-45)
        yellow_time: Duration of yellow light in seconds (3-5)
        all_red_time: Duration of all-red clearance time in seconds (default 4)
    """
    green_time: int  # 20-45 seconds
    yellow_time: int  # 3-5 seconds
    all_red_time: int = 4  # Default clearance time

    def __post_init__(self):
        """Validate the timing values."""
        if not 20 <= self.green_time <= 45:
            raise ValueError("Green time must be between 20 and 45 seconds")
        if not 3 <= self.yellow_time <= 5:
            raise ValueError("Yellow time must be between 3 and 5 seconds")
        if self.all_red_time < 0:
            raise ValueError("All-red time cannot be negative")


class TrafficLight:
    """Represents a traffic light controlling one or more lanes.
    
    Attributes:
        lanes: List of lanes controlled by this traffic light
        signal_phase: The timing configuration for this light
        current_state: Current state of the light (GREEN, YELLOW, RED)
        time_remaining: Time remaining in current state in seconds
    """
    def __init__(self, lanes: List[Lane], signal_phase: SignalPhase):
        self.lanes = lanes
        self.signal_phase = signal_phase
        self.current_state = LightState.RED
        self.time_remaining = 0
        self._next_state = LightState.GREEN
        self._direction_str = ", ".join(str(lane) for lane in lanes)
        # Initialize with the current state's time
        self._update_state_time()

    def _update_state_time(self) -> None:
        """Update the time remaining based on current state."""
        if self.current_state == LightState.GREEN:
            self.time_remaining = self.signal_phase.green_time
        elif self.current_state == LightState.YELLOW:
            self.time_remaining = self.signal_phase.yellow_time
        else:  # RED
            self.time_remaining = 0

    def update(self, seconds: int = 1) -> bool:
        """Update the traffic light state based on elapsed time.
        
        Args:
            seconds: Number of seconds to advance the simulation
            
        Returns:
            bool: True if the light state changed, False otherwise
            
        Time Complexity: O(1) - Constant time operations, no loops or recursion.
                        Simple arithmetic and state checks.
        """
        # Handle state transitions when time is up
        if self.time_remaining > 0:
            self.time_remaining = max(0, self.time_remaining - seconds)
            
            # If time ran out, transition to next state
            if self.time_remaining == 0:
                return self._transition()
        # Handle immediate transition when time_remaining is 0 and we're waiting to transition
        elif (self.time_remaining == 0 and 
              self.current_state == LightState.RED and 
              self._next_state == LightState.GREEN):
            return self._transition()
            
        return False

    def _transition(self) -> bool:
        """Transition to the next state in the cycle."""
        if self.current_state == LightState.GREEN:
            self.current_state = LightState.YELLOW
        elif self.current_state == LightState.YELLOW:
            self.current_state = LightState.RED
        elif self.current_state == LightState.RED and self._next_state == LightState.GREEN:
            self.current_state = LightState.GREEN
        else:
            return False
            
        # Update the time for the new state
        self._update_state_time()
        return True

    def set_next_state(self, next_state: LightState) -> None:
        """Set the next state for the traffic light.
        
        Note: This only sets the next state when transitioning from RED to GREEN.
        Other transitions are automatic (GREEN->YELLOW->RED).
        """
        self._next_state = next_state
        
        # If we're setting next state to GREEN and we're currently RED,
        # and there's no time remaining, prepare for immediate transition
        if (next_state == LightState.GREEN and 
            self.current_state == LightState.RED and 
            self.time_remaining == 0):
            # Don't transition immediately, just set up for the next update
            pass

    def __str__(self) -> str:
        state_str = self.current_state.name.capitalize()
        time_str = f" ({self.time_remaining}s)" if self.time_remaining > 0 else ""
        return f"{self._direction_str}: {state_str}{time_str}"


class IntersectionController:
    """Controls the traffic lights at a four-way intersection."""
    def __init__(self):
        self.traffic_lights: Dict[str, TrafficLight] = {}
        self.current_phase: Optional[str] = None
        self.all_red_time = 0
        self.sim_time = 0
        self._phases = ["NS", "EW"]  # Simple two-phase cycle for now
        self._phase_index = 0

    def add_traffic_light(self, name: str, traffic_light: TrafficLight) -> None:
        """Add a traffic light to the intersection."""
        self.traffic_lights[name] = traffic_light

    def initialize(self) -> None:
        """Initialize the intersection controller and start the first phase."""
        if not self.traffic_lights:
            raise ValueError("No traffic lights added to the intersection")
        
        # Set initial state
        self.current_phase = self._phases[0]
        self._update_traffic_lights()

    def _update_traffic_lights(self) -> None:
        """Update all traffic lights based on the current phase.
        
        Time Complexity: O(n) where n is the number of traffic lights in the intersection.
                       Each light is checked and potentially updated in constant time.
        """
        for name, light in self.traffic_lights.items():
            if name.startswith(self.current_phase):
                if light.current_state != LightState.GREEN:
                    light.current_state = LightState.GREEN
                    light._update_state_time()
            else:
                if light.current_state != LightState.RED:
                    light.current_state = LightState.RED
                    light._update_state_time()

    def update(self, seconds: int = 1) -> None:
        """Update the intersection state by the given number of seconds.
        
        Time Complexity: O(n) where n is the number of traffic lights in the intersection.
                       The method processes each traffic light once, and each operation
                       on the lights is O(1). The active_lights list comprehension is O(n).
        """
        self.sim_time += seconds
        
        if self.all_red_time > 0:
            # During all-red clearance time
            self.all_red_time = max(0, self.all_red_time - seconds)
            if self.all_red_time == 0:
                # Clearance time over, switch to next phase
                self._phase_index = (self._phase_index + 1) % len(self._phases)
                self.current_phase = self._phases[self._phase_index]
                self._update_traffic_lights()  # O(n)
        else:
            # Check if any light needs to transition
            active_lights = [light for name, light in self.traffic_lights.items() 
                           if name.startswith(self.current_phase)]  # O(n)
            
            # Update all lights - O(n) * O(1) for each light's update
            for light in self.traffic_lights.values():
                light_was_updated = light.update(seconds)  # O(1)
                
                # If an active light just turned yellow to red, start all-red phase
                if (light_was_updated and 
                    light in active_lights and  # O(1) for set lookup
                    light.current_state == LightState.RED and 
                    light._next_state == LightState.GREEN):
                    self.all_red_time = light.signal_phase.all_red_time

    def get_status(self) -> str:
        """Get the current status of all traffic lights.
        
        Returns:
            str: Formatted status string showing the state of all traffic lights
            
        Time Complexity: O(n) where n is the number of traffic lights in the intersection.
                       Each light's status is converted to a string exactly once.
        """
        status = [f"[Time: {self.sim_time:03d}s] "]
        if self.all_red_time > 0:
            status.append("ALL LANES: RED (clearance time)")
        else:
            for light in self.traffic_lights.values():
                status.append(str(light))  # O(1) per light
        return "\n".join(status)  # O(n) for joining n+1 strings

    def simulate(self, duration: int, time_step: int = 1) -> None:
        """Run the simulation for the specified duration.
        
        Args:
            duration: Total simulation time in seconds
            time_step: Time step for each iteration in seconds
        """
        self.initialize()
        print("Starting simulation...")
        print(self.get_status())
        
        for _ in range(0, duration, time_step):
            self.update(time_step)
            print(self.get_status())
            time.sleep(0.1)  # Small delay for readability


def create_sample_intersection() -> IntersectionController:
    """Create a sample intersection with the specified configuration."""
    controller = IntersectionController()
    
    # North-South direction (2 through lanes, 1 left turn)
    ns_through1 = Lane(Direction.NORTH, LaneType.THROUGH)
    ns_through2 = Lane(Direction.SOUTH, LaneType.THROUGH)
    ns_left = Lane(Direction.NORTH, LaneType.LEFT_TURN)
    
    # East-West direction (1 through lane each way, no left turns)
    ew_through = Lane(Direction.EAST, LaneType.THROUGH)
    we_through = Lane(Direction.WEST, LaneType.THROUGH)
    
    # Create traffic lights with appropriate signal phases
    # Using 30s green time for through traffic and 20s for left turns (minimum allowed)
    controller.add_traffic_light(
        "NS_through", 
        TrafficLight([ns_through1, ns_through2], SignalPhase(green_time=30, yellow_time=4))
    )
    controller.add_traffic_light(
        "NS_left", 
        TrafficLight([ns_left], SignalPhase(green_time=20, yellow_time=3))
    )
    controller.add_traffic_light(
        "EW_through", 
        TrafficLight([ew_through, we_through], SignalPhase(green_time=25, yellow_time=4))
    )
    
    return controller


if __name__ == "__main__":
    # Create and run a sample simulation
    intersection = create_sample_intersection()
    intersection.simulate(duration=120)  # Run for 2 minutes
