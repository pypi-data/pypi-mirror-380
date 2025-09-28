"""
Smart Port Conflict Detection for Arduino MCP Server
Proactively detects port usage conflicts and provides helpful guidance
"""

import os
import subprocess
import logging
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass
class PortUsage:
    """Information about a process using a port"""
    pid: int
    command: str
    user: str
    fd_type: str
    process_name: str

    def __str__(self) -> str:
        return f"{self.process_name} (PID {self.pid}) by {self.user}"


class PortConflictDetector:
    """Detects and reports serial port usage conflicts"""

    def __init__(self):
        self.common_arduino_processes = {
            'arduino': 'Arduino IDE',
            'arduino-cli': 'Arduino CLI',
            'platformio': 'PlatformIO',
            'pio': 'PlatformIO CLI',
            'esptool': 'ESP Flash Tool',
            'avrdude': 'AVR Programming Tool',
            'python': 'Python Script (possibly MCP server)',
            'minicom': 'Minicom Terminal',
            'screen': 'GNU Screen',
            'picocom': 'Picocom Terminal',
            'cu': 'Unix Terminal',
            'putty': 'PuTTY',
            'tio': 'TIO Terminal'
        }

    async def check_port_usage(self, port: str) -> Optional[List[PortUsage]]:
        """
        Check if a serial port is being used by another process
        Returns list of processes using the port, or None if available
        """
        try:
            # Try lsof first (most detailed info)
            usage = await self._check_with_lsof(port)
            if usage:
                return usage

            # Fallback to fuser if lsof fails
            usage = await self._check_with_fuser(port)
            if usage:
                return usage

            # Try direct file access test
            if await self._test_direct_access(port):
                # Port is busy but we can't identify the process
                return [PortUsage(
                    pid=0,
                    command="unknown",
                    user="unknown",
                    fd_type="unknown",
                    process_name="Unknown Process"
                )]

            return None  # Port is available

        except Exception as e:
            logger.warning(f"Error checking port usage for {port}: {e}")
            return None

    async def _check_with_lsof(self, port: str) -> Optional[List[PortUsage]]:
        """Check port usage using lsof command"""
        try:
            result = subprocess.run(
                ['lsof', port],
                capture_output=True,
                text=True,
                timeout=5
            )

            if result.returncode == 0 and result.stdout:
                return self._parse_lsof_output(result.stdout)

        except (subprocess.TimeoutExpired, FileNotFoundError, subprocess.SubprocessError):
            pass
        return None

    async def _check_with_fuser(self, port: str) -> Optional[List[PortUsage]]:
        """Check port usage using fuser command"""
        try:
            result = subprocess.run(
                ['fuser', port],
                capture_output=True,
                text=True,
                timeout=5
            )

            if result.returncode == 0 and result.stdout.strip():
                pids = [int(pid.strip()) for pid in result.stdout.split() if pid.strip().isdigit()]
                return [await self._get_process_info(pid) for pid in pids]

        except (subprocess.TimeoutExpired, FileNotFoundError, subprocess.SubprocessError, ValueError):
            pass
        return None

    async def _test_direct_access(self, port: str) -> bool:
        """Test if port is accessible by trying to open it briefly"""
        try:
            import serial
            # Very brief test - just try to open and immediately close
            with serial.Serial(port, timeout=0.1) as ser:
                pass
            return False  # Successfully opened, so available
        except (serial.SerialException, PermissionError, FileNotFoundError):
            # If we can't open it, something else might be using it
            # But could also be permissions or non-existent port
            if Path(port).exists():
                return True  # Port exists but can't open - likely in use
            return False  # Port doesn't exist

    def _parse_lsof_output(self, output: str) -> List[PortUsage]:
        """Parse lsof output to extract process information"""
        processes = []
        lines = output.strip().split('\n')[1:]  # Skip header

        for line in lines:
            parts = line.split(None, 8)  # Split into max 9 parts
            if len(parts) >= 8:
                try:
                    processes.append(PortUsage(
                        pid=int(parts[1]),
                        command=parts[0],
                        user=parts[2],
                        fd_type=parts[4],
                        process_name=parts[0]
                    ))
                except ValueError:
                    continue

        return processes

    async def _get_process_info(self, pid: int) -> PortUsage:
        """Get detailed process information for a PID"""
        try:
            # Get process name and command from /proc/pid/comm and /proc/pid/cmdline
            comm_path = f"/proc/{pid}/comm"
            cmdline_path = f"/proc/{pid}/cmdline"

            process_name = "unknown"
            command = "unknown"

            if Path(comm_path).exists():
                with open(comm_path, 'r') as f:
                    process_name = f.read().strip()

            if Path(cmdline_path).exists():
                with open(cmdline_path, 'r') as f:
                    cmdline = f.read().replace('\0', ' ').strip()
                    command = cmdline if cmdline else process_name

            # Get user from process status
            user = "unknown"
            try:
                result = subprocess.run(['ps', '-p', str(pid), '-o', 'user='],
                                      capture_output=True, text=True, timeout=2)
                if result.returncode == 0:
                    user = result.stdout.strip()
            except:
                pass

            return PortUsage(
                pid=pid,
                command=command,
                user=user,
                fd_type="chr",
                process_name=process_name
            )

        except Exception:
            return PortUsage(
                pid=pid,
                command="unknown",
                user="unknown",
                fd_type="unknown",
                process_name="unknown"
            )

    def generate_conflict_message(self, port: str, usage: List[PortUsage]) -> str:
        """Generate a helpful error message for port conflicts"""
        if not usage:
            return f"Port {port} is available"

        message_parts = [f"❌ **Port {port} is currently in use:**\n"]

        for proc in usage:
            # Try to identify the type of application
            app_type = self._identify_application_type(proc.process_name.lower())

            if proc.pid > 0:
                message_parts.append(f"  • **{app_type}** - {proc} (FD: {proc.fd_type})")
            else:
                message_parts.append(f"  • **{app_type}** - Process details unavailable")

        message_parts.extend([
            "\n**🔧 Suggested Solutions:**",
            self._get_solutions_for_processes(usage),
            "\n**💡 Quick Commands:**"
        ])

        # Add specific commands based on detected processes
        commands = self._get_suggested_commands(port, usage)
        message_parts.extend(commands)

        return "\n".join(message_parts)

    def _identify_application_type(self, process_name: str) -> str:
        """Identify the type of application using the port"""
        for pattern, app_name in self.common_arduino_processes.items():
            if pattern in process_name:
                return app_name
        return "Unknown Application"

    def _get_solutions_for_processes(self, usage: List[PortUsage]) -> str:
        """Generate process-specific solutions"""
        solutions = []

        for proc in usage:
            process_lower = proc.process_name.lower()

            if 'arduino' in process_lower:
                solutions.append("  1. Close Arduino IDE serial monitor (Tools → Serial Monitor)")
            elif 'platformio' in process_lower:
                solutions.append("  1. Stop PlatformIO monitor: `pio device monitor --exit`")
            elif 'python' in process_lower:
                solutions.append("  1. Stop the Python script/MCP server using the port")
            elif any(term in process_lower for term in ['minicom', 'screen', 'picocom', 'cu']):
                solutions.append(f"  1. Exit the terminal program: {proc.process_name}")
            elif 'esptool' in process_lower or 'avrdude' in process_lower:
                solutions.append("  1. Wait for programming/flashing to complete")
            else:
                solutions.append(f"  1. Stop or close {proc.process_name}")

        if not solutions:
            solutions.append("  1. Identify and close the application using the port")

        solutions.append("  2. Unplug and reconnect the Arduino device")
        solutions.append("  3. Try a different USB port")

        return "\n".join(solutions)

    def _get_suggested_commands(self, port: str, usage: List[PortUsage]) -> List[str]:
        """Generate helpful commands based on detected processes"""
        commands = []

        valid_pids = [proc.pid for proc in usage if proc.pid > 0]

        if valid_pids:
            commands.append(f"  • **Kill process:** `kill {' '.join(map(str, valid_pids))}`")
            commands.append(f"  • **Force kill:** `kill -9 {' '.join(map(str, valid_pids))}`")

        commands.extend([
            f"  • **Check port:** `lsof {port}`",
            f"  • **List all processes:** `fuser {port}`",
            "  • **List Arduino ports:** Use `serial_list_ports` with `arduino_only=true`"
        ])

        return commands


# Global instance for easy access
port_checker = PortConflictDetector()