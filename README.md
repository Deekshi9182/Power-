# Power-

## Overview
This repository contains tools and scripts to measure the power utilization of a system based on CPU, memory, NIC, and TDP. It allows you to run traffic to achieve a specific system utilization percentage and collect telemetry data.

## Features
- Collect telemetry data from CPU, memory, NIC, and TDP.
- Run traffic to achieve 100% system utilization using containers.
- Measure and record system power utilization.
- Generate a comprehensive report on power measurement and system utilization.

## Usage
1. Configure system knobs in `config/system_knobs.json`.
2. Run `scripts/collect_telemetry.sh` to collect initial telemetry data.
3. Run `scripts/run_traffic.sh` to start the traffic generator container.
4. Run `scripts/measure_power.sh` to measure power utilization.
5. Run `scripts/generate_report.py` to generate a report.

## Requirements
- Python 3.x
- Docker
- jq (for JSON processing in shell scripts)

## Setup
1. Clone this repository.
2. Install the required dependencies.
3. Configure the system knobs.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
