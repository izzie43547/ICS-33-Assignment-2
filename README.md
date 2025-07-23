# Traffic Light Simulation

A Python implementation of a four-way traffic intersection simulation with configurable traffic lights and timing, developed for UCI ICS 33 Assignment 2.

## Features

- Simulates a four-way intersection with configurable lanes (1-4 through lanes, 0-1 left-turn lane per direction)
- Supports through lanes and protected left-turn lanes
- Configurable signal timing (green: 20-45s, yellow: 3-5s, all-red clearance: 4s)
- Real-time simulation with console output and file logging
- Object-oriented design with clear separation of concerns
- Comprehensive unit testing

## Requirements

- Python 3.8+
- No external dependencies required

## Installation

1. Clone this repository
2. Navigate to the project directory

## Usage

### Running the Simulation

Run the simulation with default settings:

```bash
python traffic.py
```

This executes a 2-minute simulation of a sample intersection with:
- North-South: 2 through lanes, 1 left-turn lane
- East-West: 1 through lane each way
- Default signal timings (30s green, 4s yellow, 4s all-red clearance)

### Configuration

Modify the `create_sample_intersection()` function in `traffic.py` to customize:
- Number of lanes (1-4 through lanes, 0-1 left-turn lane per direction)
- Signal timings (within allowed ranges)
- Intersection layout

Example configuration:
```python
def create_sample_intersection():
    # North-South direction
    ns_phase = SignalPhase(green_time=35, yellow_time=4)  # 35s green, 4s yellow
    ew_phase = SignalPhase(green_time=25, yellow_time=3)  # 25s green, 3s yellow
    # ... rest of the configuration
```

### Output

The simulation outputs to both console and `simulation.log` with timestamps:
- Current state of all traffic lights
- Phase transitions
- Timing information

## Project Structure

- `traffic.py`: Main simulation code
- `test_traffic.py`: Unit tests for core functionality
- `analysis.pdf`: Runtime complexity analysis and design decisions
- `gen-ai.pdf`: Documentation of gen AI usage (extra credit)
- `simulation.log`: Log file with detailed simulation output
- `README.md`: This documentation

## Testing

Run all unit tests:

```bash
python -m unittest test_traffic.py -v
```

Test coverage includes:
- Lane creation and validation
- Signal phase timing constraints
- Traffic light state transitions
- Intersection controller logic

## Deliverables

1. `traffic.py`: Main implementation (80 points)
2. `test_traffic.py`: Unit tests for all classes and methods
3. `analysis.pdf`: Runtime complexity analysis and design documentation
4. `gen-ai.pdf`: Documentation of gen AI usage (5 points extra credit)

## Logging

The simulation logs detailed information to `simulation.log`, including:
- Timestamped state changes
- Phase transitions
- Configuration details
- Any warnings or errors

## Gen AI Usage (Extra Credit)

Documentation of any generative AI tools used during development is included in `gen-ai.pdf`, as per the assignment requirements for extra credit.

## Example Output

```
[00:00] NS through lanes: GREEN (30s), Left-turn: RED
[00:20] NS through lanes: YELLOW (4s), Left-turn: RED
[00:24] All lanes: RED (clearance time)
[00:28] EW through lanes: GREEN (30s)
[00:58] EW through lanes: YELLOW (4s)
[01:02] All lanes: RED (clearance time)
```

## License

This project is for educational purposes as part of UCI ICS 33.
