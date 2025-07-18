import unittest
from traffic import (
    Direction, LaneType, LightState, 
    Lane, SignalPhase, TrafficLight, IntersectionController
)


class TestTrafficLightSimulation(unittest.TestCase):
    def test_lane_creation(self):
        """Test that lanes are created with correct direction and type."""
        lane = Lane(Direction.NORTH, LaneType.THROUGH)
        self.assertEqual(lane.direction, Direction.NORTH)
        self.assertEqual(lane.lane_type, LaneType.THROUGH)
        self.assertEqual(str(lane), "North through lane")

    def test_signal_phase_validation(self):
        """Test that signal phase validates timing values."""
        # Valid signal phase
        phase = SignalPhase(green_time=30, yellow_time=4)
        self.assertEqual(phase.green_time, 30)
        self.assertEqual(phase.yellow_time, 4)
        self.assertEqual(phase.all_red_time, 4)  # default

        # Test invalid green time
        with self.assertRaises(ValueError):
            SignalPhase(green_time=10, yellow_time=3)  # green_time too low
        with self.assertRaises(ValueError):
            SignalPhase(green_time=50, yellow_time=3)  # green_time too high

        # Test invalid yellow time
        with self.assertRaises(ValueError):
            SignalPhase(green_time=30, yellow_time=2)  # yellow_time too low
        with self.assertRaises(ValueError):
            SignalPhase(green_time=30, yellow_time=6)  # yellow_time too high

    def test_traffic_light_transitions(self):
        """Test traffic light state transitions."""
        lane = Lane(Direction.NORTH, LaneType.THROUGH)
        phase = SignalPhase(green_time=30, yellow_time=3)
        light = TrafficLight([lane], phase)
        
        # Initial state should be RED with 0 time remaining
        self.assertEqual(light.current_state, LightState.RED)
        self.assertEqual(light.time_remaining, 0)
        
        # Set next state to GREEN and update
        light.set_next_state(LightState.GREEN)
        self.assertTrue(light.update(0))  # Should transition immediately
        self.assertEqual(light.current_state, LightState.GREEN)
        self.assertEqual(light.time_remaining, 30)
        
        # Update with time passing
        self.assertFalse(light.update(10))  # 20s remaining
        self.assertEqual(light.time_remaining, 20)
        
        # Let time run out, should transition to YELLOW
        self.assertTrue(light.update(20))
        self.assertEqual(light.current_state, LightState.YELLOW)
        self.assertEqual(light.time_remaining, 3)
        
        # Let yellow time run out, should transition to RED
        self.assertTrue(light.update(3))
        self.assertEqual(light.current_state, LightState.RED)

    def test_intersection_controller(self):
        """Test intersection controller with a simple setup."""
        controller = IntersectionController()
        
        # Add a simple traffic light
        lane = Lane(Direction.NORTH, LaneType.THROUGH)
        phase = SignalPhase(green_time=30, yellow_time=3, all_red_time=2)
        controller.add_traffic_light("NS_through", TrafficLight([lane], phase))
        
        # Initialize the controller
        controller.initialize()
        self.assertEqual(controller.current_phase, "NS")
        
        # Check initial state
        light = controller.traffic_lights["NS_through"]
        self.assertEqual(light.current_state, LightState.GREEN)
        self.assertEqual(light.time_remaining, 30)
        
        # Simulate time passing
        controller.update(25)  # 5s left in green
        self.assertEqual(light.time_remaining, 5)
        
        # Let green time run out, should go to yellow
        controller.update(5)
        self.assertEqual(light.current_state, LightState.YELLOW)
        self.assertEqual(light.time_remaining, 3)
        
        # Let yellow time run out, should go to all-red
        controller.update(3)
        self.assertEqual(controller.all_red_time, 2)  # All-red clearance time
        
        # Let all-red time run out, should switch to next phase (EW)
        controller.update(2)
        self.assertEqual(controller.current_phase, "EW")


if __name__ == "__main__":
    unittest.main()
