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
