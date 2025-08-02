# Traffic Light Simulation

A Python implementation of a four-way traffic intersection simulation with configurable traffic lights and timing, created for UCI ICS 33 Assignment 2.

## Features

- Simulates a four-way intersection with configurable lanes (1-4 through lanes, 0-1 left-turn lanes per direction)
- Supports through lanes and left-turn lanes with protected left turns
- Configurable signal timing (green: 20-45s, yellow: 3-5s, all-red clearance: 4s)
- Time-based simulation with clear state transitions
- Object-oriented design with proper encapsulation
- Comprehensive unit test coverage

## Requirements

- Python 3.8+
- No external dependencies required
- `unittest` (included in Python standard library) for running tests

## Installation

1. Clone this repository or download the project files
2. Navigate to the project directory

## Usage

### Running the Simulation

Run the simulation with default settings:

```bash
python traffic.py
```

This will run a 2-minute (120-second) simulation of a sample intersection with:
- North-South: 2 through lanes, 1 left-turn lane
- East-West: 1 through lane each way
- Default signal timings (NS: 30s green, 3s yellow, 4s all-red)

### Running Tests

To run the unit tests:

```bash
python -m unittest test_traffic.py -v
```

## Project Structure

- `traffic.py`: Main simulation code with all class implementations
- `test_traffic.py`: Unit tests for all components
- `README.md`: This documentation file
- `gen-ai.pdf`: Documentation of AI tool usage (extra credit)

## Class Documentation

### `Lane`
Represents a single traffic lane with direction and type (through/left-turn).

### `SignalPhase`
Manages timing for traffic signals with validation for:
- Green time (20-45 seconds)
- Yellow time (3-5 seconds)
- All-red clearance time (default: 4 seconds)

### `TrafficLight`
Controls one or more lanes with a traffic signal, handling state transitions between:
- GREEN
- YELLOW
- RED

### `IntersectionController`
Manages the entire intersection, including:
- Traffic light coordination
- Phase transitions
- Simulation timing
- State management

## Customization

You can modify the `create_sample_intersection()` function in `traffic.py` to:
- Change the number of lanes in each direction
- Adjust signal timings (within allowed ranges)
- Add or remove traffic lights
- Modify the simulation duration

## Example Output

```
Starting simulation...
[Time: 000s] NS through lanes: GREEN (30s), Left-turn: RED
[Time: 030s] NS through lanes: YELLOW (3s), Left-turn: RED
[Time: 033s] All lanes: RED (clearance 4s)
[Time: 037s] NS left-turn: GREEN (15s), Through: RED
[Time: 052s] NS left-turn: YELLOW (3s)
[Time: 055s] All lanes: RED (clearance 4s)
[Time: 059s] EW through lanes: GREEN (25s), NS: RED
```

## Testing

The test suite includes tests for:
- Lane creation and properties
- Signal phase validation
- Traffic light state transitions
- Intersection controller logic
- Phase timing and transitions

To run all tests:
```bash
python -m unittest test_traffic.py -v
```

## Submission

### Files to Submit
1. `traffic.py` - Main implementation
2. `test_traffic.py` - Unit tests
3. `README.md` - This documentation
4. (Optional) `gen-ai.pdf` - AI tool usage documentation for extra credit

### Grading
- **Code Implementation (45 points)**: Correctness, design, and style
- **Testing (25 points)**: Coverage and quality of unit tests
- **Documentation (20 points)**: Code comments and README
- **Functionality (10 points)**: Meets all specified requirements
- **Extra Credit (5 points)**: AI tool usage documentation

## License

This project is for educational purposes as part of UCI ICS 33.
