import asyncio
import subprocess
import logging
import re

_LOGGER = logging.getLogger(__name__)

def close_process(process):
    process.stdin.close()
    process.stdout.close()
    process.stderr.close()
    process.wait()

async def run_command(command):
    """Run a bluetoothctl command and return the output."""
    proc = await asyncio.create_subprocess_exec(
        "bluetoothctl",
        *command.split(),
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )

    try:
        stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout=10.0)
        return {"stdout": stdout, "stderr": stderr, "returncode": proc.returncode}
    except asyncio.TimeoutError:
        proc.kill()
        await proc.wait()
        raise TimeoutError(f"bluetoothctl command timed out: {command}")
    except Exception as e:
        proc.kill()
        await proc.wait()
        raise RuntimeError(f"Command failed: {command} - {str(e)}")

def start_bluetoothctl():
    """Start bluetoothctl as an interactive process."""
    return subprocess.Popen(
        ["bluetoothctl"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1024,
    )

async def send_command_in_process(process, command, delay=2):
    """Send a command to the bluetoothctl process and wait for a response."""
    process.stdin.write(f"{command}\n")
    process.stdin.flush()
    await asyncio.sleep(delay)

async def is_device_connected(address):
    """Check if a Bluetooth device is connected by its MAC address."""
    cmdout = await run_command("devices Connected")
    target_address = address.lower().encode()

    for line in cmdout["stdout"].splitlines():
        # Check if line starts with "Device" followed by MAC address
        if line.lower().startswith(b"device " + target_address):
            return True
    return False

async def is_device_bonded(address):
    """Check if a Bluetooth device is bonded by its MAC address."""
    cmdout = await run_command("devices Bonded")
    target_address = address.lower().encode()

    for line in cmdout["stdout"].splitlines():
        # Check if line starts with "Device" followed by MAC address
        if line.lower().startswith(b"device " + target_address):
            return True
    return False

async def is_device_paired(address):
    """Check if a Bluetooth device is paired by its MAC address."""
    cmdout = await run_command("devices Paired")
    target_address = address.lower().encode()

    for line in cmdout["stdout"].splitlines():
        # Check if line starts with "Device" followed by MAC address
        if line.lower().startswith(b"device " + target_address):
            return True
    return False

async def get_first_manufacturer_data_byte(mac_address: str) -> int:
    """
    Returns the first byte of ManufacturerData.Value for a BLE device using bluetoothctl.
    Returns None if not found.
    """
    # Run bluetoothctl info and capture output
    cmd = ["bluetoothctl", "info", mac_address]
    proc = await asyncio.create_subprocess_exec(
        *cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )

    # Wait for completion (timeout: 10 sec)
    try:
        stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout=10)
    except asyncio.TimeoutError:
        proc.kill()
        await proc.wait()
        _LOGGER.error("bluetoothctl command timed out")
        return None

    # Parse output
    lines = stdout.decode().splitlines()

    for i, line in enumerate(lines):
        if "ManufacturerData.Value" in line:
            # The next line contains the hex bytes (e.g., "cc 64 62 64")
            if (i + 1) < len(lines):
                hex_str = re.search(r"([0-9a-fA-F]{2})", lines[i + 1].strip())
                if hex_str:
                    return int(hex_str.group(1), 16)
    return None
