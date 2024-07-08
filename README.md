# Power-
# System Telemetry and Power Utilization

This repository contains scripts to collect telemetry data from system components (CPU, memory, NIC, and TDP) and measure system power utilization based on a specified system utilization percentage.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [Collecting Telemetry Data](#collecting-telemetry-data)
  - [Measuring Power Utilization](#measuring-power-utilization)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project provides Python scripts to monitor and analyze system performance metrics such as CPU usage, memory usage, network activity (NIC), and thermal design power (TDP). By collecting telemetry data and calculating power utilization, users can gain insights into system resource consumption under varying workloads.

## Features

- **Telemetry Data Collection**: Collects real-time metrics from CPU, memory, NIC, and TDP.
- **Power Utilization Measurement**: Calculates power consumption metrics for CPU, NIC, and TDP based on specified utilization percentages.

## Prerequisites

Ensure you have the following installed on your system:

- Python 3.x
- `psutil` library (`pip install psutil`)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Deekshi9182/Power-.git
    cd system-telemetry-power-utilization
    ```

2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Collecting Telemetry Data

The `collect_telemetry_data.py` script continuously logs system metrics:

1. Save the following script as `collect_telemetry_data.py`:

    ```python
    import psutil
    import time
    import logging

    # Configure logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def collect_telemetry_data(interval):
        """
        Collect telemetry data from CPU, memory, NIC, and TDP at regular intervals.

        Parameters:
        interval (int): The interval in seconds between telemetry data collections.
        """
        try:
            while True:
                # CPU metrics
                cpu_percent = psutil.cpu_percent(interval=1)
                cpu_freq = psutil.cpu_freq().current

                # Memory metrics
                mem = psutil.virtual_memory()
                mem_percent = mem.percent

                # Network metrics
                net_io = psutil.net_io_counters()
                nic_bytes_sent = net_io.bytes_sent
                nic_bytes_recv = net_io.bytes_recv

                # Read TDP or other power-related data from system files
                tdp_value = read_tdp_from_file()

                # Output telemetry data
                logging.info(f"CPU Percent: {cpu_percent}%")
                logging.info(f"CPU Frequency: {cpu_freq} MHz")
                logging.info(f"Memory Percent: {mem_percent}%")
                logging.info(f"NIC Bytes Sent: {nic_bytes_sent} bytes")
                logging.info(f"NIC Bytes Received: {nic_bytes_recv} bytes")
                logging.info(f"TDP Value: {tdp_value}")

                time.sleep(interval)  # Adjust interval as needed
        except Exception as e:
            logging.error(f"An error occurred while collecting telemetry data: {e}")

    def read_tdp_from_file():
        """
        Read TDP value from a system file.
        
        Returns:
        float: The TDP value read from the system file.
        """
        try:
            # Replace this with the actual implementation to read TDP value from your system
            tdp_value = 100.0  # Example value
            logging.info(f"TDP Value read from file: {tdp_value}")
            return tdp_value
        except Exception as e:
            logging.error(f"An error occurred while reading TDP value: {e}")
            return None

    if __name__ == "__main__":
        try:
            # Interval in seconds between telemetry data collections
            interval = 5
            logging.info(f"Starting telemetry data collection with an interval of {interval} seconds.")
            collect_telemetry_data(interval)
        except KeyboardInterrupt:
            logging.info("Telemetry data collection stopped by user.")
    ```

2. Run the script:
    ```sh
    python collect_telemetry_data.py
    ```

### Measuring Power Utilization

The `measure_power_utilization.py` script calculates power consumption metrics:

1. Save the following script as `measure_power_utilization.py`:

    ```python
    import argparse
    import logging

    # Configure logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def measure_power_utilization(system_utilization_percent, multipliers):
        """
        Calculate power utilization based on system utilization percentage and given multipliers.

        Parameters:
        system_utilization_percent (float): The percentage of system utilization.
        multipliers (dict): A dictionary containing the multipliers for CPU, NIC, and TDP power calculations.

        Returns:
        dict: A dictionary with calculated power utilization for CPU, NIC, and TDP.
        """
        try:
            # Validate system utilization percentage
            if not (0 <= system_utilization_percent <= 100):
                raise ValueError("System utilization percent must be between 0 and 100.")
            
            logging.info("Calculating power utilization for system utilization percent: %s%%", system_utilization_percent)

            # Calculate power utilization for each component
            cpu_power = system_utilization_percent * multipliers['cpu']
            nic_power = system_utilization_percent * multipliers['nic']
            tdp_power = system_utilization_percent * multipliers['tdp']

            power_metrics = {
                'CPU Power': cpu_power,
                'NIC Power': nic_power,
                'TDP Power': tdp_power
            }

            logging.info("Power utilization calculated successfully.")
            return power_metrics

        except Exception as e:
            logging.error("Error calculating power utilization: %s", e)
            raise

    def parse_arguments():
        """
        Parse command-line arguments.

        Returns:
        Namespace: A namespace containing the parsed arguments.
        """
        parser = argparse.ArgumentParser(description='Measure system power utilization based on utilization percentage.')
        parser.add_argument('-u', '--utilization', type=float, default=100, help='System utilization percentage (0-100)')
        return parser.parse_args()

    if __name__ == "__main__":
        try:
            # Parse command-line arguments
            args = parse_arguments()
            utilization_percent = args.utilization

            logging.info("System utilization percent input: %s%%", utilization_percent)

            # Define multipliers for power calculations
            multipliers = {
                'cpu': 0.75,  # Multiplier for CPU power calculation
                'nic': 0.5,   # Multiplier for NIC power calculation
                'tdp': 0.8    # Multiplier for TDP power calculation
            }

            # Measure power utilization
            power_metrics = measure_power_utilization(utilization_percent, multipliers)

            # Print the power metrics
            print("Power Metrics:")
            for component, power in power_metrics.items():
                print(f"{component}: {power:.2f} Watts")

        except Exception as e:
            logging.error("An error occurred: %s", e)
    ```

2. Run the script with the desired system utilization percentage:
    ```sh
    python measure_power_utilization.py -u 75
    ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
