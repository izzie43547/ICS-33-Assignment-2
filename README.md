# Traffic Light Simulation

A Python implementation of a four-way traffic intersection simulation with configurable traffic lights and timing.

## Features

- Simulates a four-way intersection with configurable lanes
- Supports through lanes and left-turn lanes
- Configurable signal timing (green, yellow, all-red clearance)
- Real-time simulation with console output
- Object-oriented design with clear separation of concerns

## Requirements

- Python 3.8+
- No external dependencies required

## Installation

1. Clone this repository
2. Navigate to the project directory

## Usage

Run the simulation with default settings:

```bash
python traffic.py
```

This will run a 2-minute simulation of a sample intersection with:
- North-South: 2 through lanes, 1 left-turn lane
- East-West: 1 through lane each way
- Configurable signal timings

## Project Structure

- `traffic.py`: Main simulation code
- `README.md`: This file

## Classes

- `Lane`: Represents a single lane in a direction
- `SignalPhase`: Manages timing for traffic signals
- `TrafficLight`: Controls one or more lanes with a traffic signal
- `IntersectionController`: Manages all traffic lights and simulation state

## Customization

You can modify the `create_sample_intersection()` function in `traffic.py` to:
- Change the number of lanes
- Adjust signal timings
- Add or remove traffic lights

## Example Output

```
Starting simulation...
[Time: 000s] North through lane, South through lane: Green (30s)
North left-turn lane: Red
East through lane, West through lane: Red
...
[Time: 030s] North through lane, South through lane: Yellow (4s)
...
[Time: 034s] ALL LANES: RED (clearance time)
...
[Time: 038s] East through lane, West through lane: Green (25s)
```

## License

This project is for educational purposes as part of UCI ICS 33.
