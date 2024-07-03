# Example script to measure system power utilization

def measure_power_utilization(system_utilization_percent):
    # Example: calculate power utilization based on system utilization percentage
    cpu_power = system_utilization_percent * 0.75  # Example calculation
    nic_power = system_utilization_percent * 0.5   # Example calculation
    tdp_power = system_utilization_percent * 0.8   # Example calculation

    return {
        'CPU Power': cpu_power,
        'NIC Power': nic_power,
        'TDP Power': tdp_power
    }

if __name__ == "__main__":
    utilization_percent = 100  # Example utilization percentage
    power_metrics = measure_power_utilization(utilization_percent)
    print("Power Metrics:")
    for component, power in power_metrics.items():
        print(f"{component}: {power} Watts")
