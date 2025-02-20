from netmiko import Netmiko

# List of devices to connect to
devices = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.101",
        "username": "student",
        "password": "Meilab123",
        "port": "22",
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.102",
        "username": "student",
        "password": "Meilab123",
        "port": "22",
    },
    {
    "device_type": "cisco_ios",
        "ip": "192.168.1.103",
        "username": "student",
        "password": "Meilab123",
        "port": "22",
    }
    # Add more devices to the list if needed
]

# Loop through each device
for device in devices:
    try:
        # Establish connection to device
        net_connect = Netmiko(**device)

        # Send 'show version' command and capture output
        output = net_connect.send_command("show version")

        # Disconnect from the device
        net_connect.disconnect()

        # Extract and print uptime
        uptime_start = output.find("uptime is")
        if uptime_start != -1:
            uptime_end = uptime_start + 38  # Approximate length of the uptime string
            uptime = output[uptime_start:uptime_end]
            print(f"{device['ip']} => Uptime: {uptime}")

        # Extract and print Configuration Register
        config_register_start = output.find("Configuration register is")
        if config_register_start != -1:
            config_register_end = config_register_start + 30  # Length of the line for the config register
            config_register = output[config_register_start:config_register_end]
            print(f"{device['ip']} => {config_register}")

        print("-" * 40)  # Divider for clarity

    except Exception as e:
        print(f"Failed")
