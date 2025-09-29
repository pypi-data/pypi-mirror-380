"""
Run Tool - 2-State command execution for AI agents.

Features:
- Single run_command() entry point with unified command handling
- States: IDLE (no process) and RUNNING (active process)
- Non-interactive: Auto-kill on timeout, return results immediately
- Interactive: Wait for timeout, return output + control choices
- Special command handling: '', 'C-c', '>>> input', new commands
- Automatic state refresh and process completion detection
"""

import os
import subprocess
import time
import select
import sys
import threading
import queue
from typing import Dict, Any, Optional
from datetime import datetime, timedelta


class RunTool:
    """2-State command execution tool with unified interface."""

    def __init__(self):
        self.active_process: Optional[Dict] = None  # Process info when RUNNING
        self.last_output_time: Optional[datetime] = None  # Track output collection
        self.completed_process_output: Optional[Dict] = None  # Output from completed process
        self.default_timeout = 300

    def run_command(
        self,
        command: str,
        timeout: int = 300,
        interactive: bool = False
    ) -> Dict[str, Any]:
        """
        Execute commands with 2-state management: IDLE (ready) or RUNNING (active process).

        USAGE:
        - Non-interactive: Quick commands, auto-kills on timeout
        - Interactive: Long tasks needing input, returns control choices on timeout
        - Control commands when RUNNING: '' (continue), 'C-c' (kill), '>>> input' (send input)

        EXAMPLES:
        run_command('npm test', timeout=60, interactive=False)  # Normal command
        run_command('C-c')  # Control: kill running process
        run_command('>>> 5')  # Control: send 5 as input to the program

        COMMON ERRORS:
        - "Another command running": Use 'C-c' to kill or wait for completion
        - "Command timed out": Process killed after timeout in non-interactive mode

        Args:
            command: Command to execute or control command ('', 'C-c', '>>> input')
            timeout: Maximum execution time in seconds (default: 300)
            interactive: If True, wait for timeout and return control choices
        Returns:
            Dict with execution results and state information
        """
        # Step 1: Check current state
        current_state = self._get_state()

        # Step 2: Refresh state (detect completion)
        state_changed = self._refresh_state()

        # Step 3: Get new state after refresh
        new_state = self._get_state()

        # Step 4: Route command based on state and command type
        if command.startswith('>>> '):
            return self._handle_input(command[4:], timeout, current_state, new_state)
        elif command == 'C-c':
            return self._handle_kill(current_state, new_state)
        elif command == '':
            return self._handle_continue(timeout, current_state, new_state)
        else:
            return self._handle_new_command(command, timeout, interactive, current_state, new_state)

    def _get_state(self) -> str:
        """Get current state: IDLE or RUNNING."""
        return "RUNNING" if self.active_process is not None else "IDLE"

    def _refresh_state(self) -> bool:
        """Check if RUNNING process has completed. Returns True if state changed."""
        if self.active_process is None:
            return False

        process = self.active_process["process"]
        return_code = process.poll()

        if return_code is not None:
            # Process completed - mark completion and preserve output for later retrieval
            self._mark_process_completed()

            # Save the completed process info for unread output handling
            self.completed_process_output = self._get_unread_output()

            # Clear active process to transition to IDLE state
            self.active_process = None
            return True  # State changed from RUNNING to IDLE

        return False  # Still running

    def _collect_available_output(self):
        """Enhanced non-blocking collection of available output optimized for Linux/WSL."""
        if self.active_process is None:
            return [], []

        process = self.active_process["process"]
        proc_info = self.active_process
        new_stdout = []
        new_stderr = []

        try:
            # Linux/WSL optimized approach with better timing
            import select
            import sys

            # Use threading approach for reliable output collection
            # Increased timeout for better WSL/Linux compatibility
            try:
                if process.stdout.readable():
                    import threading
                    import queue

                    def read_lines_robust(pipe, q, max_lines=10):
                        """Read multiple lines with better error handling."""
                        try:
                            lines_read = 0
                            while lines_read < max_lines:
                                line = pipe.readline()
                                if line:
                                    q.put(line.rstrip())
                                    lines_read += 1
                                else:
                                    break
                        except:
                            pass

                    # Try stdout with increased timeout
                    q = queue.Queue()
                    t = threading.Thread(target=read_lines_robust, args=(process.stdout, q))
                    t.daemon = True
                    t.start()
                    t.join(0.2)  # Increased from 50ms to 200ms for better WSL compatibility

                    try:
                        while True:
                            line = q.get_nowait()
                            new_stdout.append(line)
                            proc_info["stdout_lines"].append(line)
                    except queue.Empty:
                        pass

                    # Try stderr with increased timeout
                    q = queue.Queue()
                    t = threading.Thread(target=read_lines_robust, args=(process.stderr, q))
                    t.daemon = True
                    t.start()
                    t.join(0.2)  # Increased from 50ms to 200ms for better WSL compatibility

                    try:
                        while True:
                            line = q.get_nowait()
                            new_stderr.append(line)
                            proc_info["stderr_lines"].append(line)
                    except queue.Empty:
                        pass

            except:
                # Fallback to select-based approach
                try:
                    ready, _, _ = select.select([process.stdout, process.stderr], [], [], 0.2)

                    for pipe in ready:
                        try:
                            # Try to read multiple lines when available
                            for _ in range(5):  # Read up to 5 lines per call
                                line = pipe.readline()
                                if line:
                                    line = line.rstrip()
                                    if pipe == process.stdout:
                                        new_stdout.append(line)
                                        proc_info["stdout_lines"].append(line)
                                    else:
                                        new_stderr.append(line)
                                        proc_info["stderr_lines"].append(line)
                                else:
                                    break
                        except:
                            pass
                except:
                    pass

        except:
            # If anything fails, just return what we have
            pass

        return new_stdout, new_stderr

    def _mark_process_completed(self):
        """Mark process as completed without complex output collection."""
        if self.active_process is None:
            return

        process = self.active_process["process"]
        proc_info = self.active_process

        # Just mark the completion - don't try to collect remaining output
        proc_info["end_time"] = datetime.now()
        proc_info["return_code"] = process.returncode

    def _get_unread_output(self) -> Dict[str, Any]:
        """Get output since last collection time."""
        if self.active_process is None:
            # If no active process, check if we have saved completed process output
            if self.completed_process_output is not None:
                output = self.completed_process_output
                self.completed_process_output = None  # Clear after retrieval
                return output
            return {"stdout": [], "stderr": []}

        proc_info = self.active_process
        last_time = self.last_output_time or proc_info["start_time"]

        # For now, return all output (can be refined to track read positions)
        return {
            "stdout": proc_info["stdout_lines"],
            "stderr": proc_info["stderr_lines"],
            "return_code": proc_info.get("return_code"),
            "duration": (proc_info.get("end_time", datetime.now()) - proc_info["start_time"]).total_seconds()
        }

    def _handle_new_command(self, command: str, timeout: int, interactive: bool,
                           current_state: str, new_state: str) -> Dict[str, Any]:
        """Handle new command execution based on state."""
        # Check for state transition (RUNNING -> IDLE)
        if current_state == "RUNNING" and new_state == "IDLE":
            # Process just completed, show unread output and reject new command
            unread_output = self._get_unread_output()
            # Clear the completed process
            self.active_process = None
            return {
                "success": False,
                "state": "IDLE",
                "error": "Previous command completed with unread output",
                "unread_output": unread_output,
                "message": "Previous command finished. Please review output and try your new command again."
            }

        # Reject if still RUNNING
        if new_state == "RUNNING":
            return {
                "success": False,
                "state": "RUNNING",
                "error": "Cannot run new command while another is running",
                "active_command": self.active_process.get("command", "unknown"),
                "suggestions": [
                    "Use '' to continue and get output",
                    "Use 'C-c' to kill the running process",
                    "Use '>>> input' to send input to the process"
                ]
            }

        # State is IDLE, can execute new command
        if interactive:
            return self._start_interactive(command, timeout)
        else:
            return self._run_non_interactive(command, timeout)

    def _handle_continue(self, timeout: int, current_state: str, new_state: str) -> Dict[str, Any]:
        """Handle continue command ('')."""
        if current_state == "IDLE":
            return {
                "success": False,
                "state": "IDLE",
                "error": "No active process to continue",
                "message": "Start an interactive command first"
            }

        if current_state == "RUNNING" and new_state == "IDLE":
            # Process completed during gap, return completion info
            unread_output = self._get_unread_output()
            self.active_process = None
            return {
                "success": True,
                "state": "IDLE",
                "completed": True,
                "output": unread_output,
                "message": "Process completed during wait period"
            }

        # Process still running, wait for timeout
        return self._wait_and_collect_output(timeout)

    def _handle_kill(self, current_state: str, new_state: str) -> Dict[str, Any]:
        """Handle kill command ('C-c')."""
        if current_state == "IDLE":
            return {
                "success": False,
                "state": "IDLE",
                "error": "No active process to kill",
                "message": "No process is currently running"
            }

        if current_state == "RUNNING" and new_state == "IDLE":
            # Process already completed
            unread_output = self._get_unread_output()
            self.active_process = None
            return {
                "success": True,
                "state": "IDLE",
                "already_completed": True,
                "output": unread_output,
                "message": "Process had already completed"
            }

        # Process is still running, kill it
        return self._kill_process()

    def _handle_input(self, input_text: str, timeout: int, current_state: str, new_state: str) -> Dict[str, Any]:
        """Handle input command ('>>> text')."""
        if current_state == "IDLE":
            return {
                "success": False,
                "state": "IDLE",
                "error": "No active process to send input to",
                "message": "Start an interactive command first"
            }

        if current_state == "RUNNING" and new_state == "IDLE":
            # Process completed, input not applicable
            unread_output = self._get_unread_output()
            self.active_process = None
            return {
                "success": False,
                "state": "IDLE",
                "error": "Command completed, input not applicable",
                "output": unread_output,
                "message": "Process finished before input could be sent"
            }

        # Send input and wait for timeout
        return self._send_input_and_wait(input_text, timeout)

    def _run_non_interactive(self, command: str, timeout: int) -> Dict[str, Any]:
        """Execute command in non-interactive mode - auto-kill on timeout with complete output collection."""
        try:
            start_time = datetime.now()

            # Use Popen for better control over output collection
            process = subprocess.Popen(
                command,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                stdin=subprocess.PIPE,
                text=True,
                bufsize=1  # Line buffering for better real-time output
            )

            try:
                # Try to complete normally within timeout
                stdout, stderr = process.communicate(timeout=timeout)
                end_time = datetime.now()
                duration = (end_time - start_time).total_seconds()

                return {
                    "success": True,
                    "state": "IDLE",
                    "command": command,
                    "exit_code": process.returncode,
                    "stdout": stdout,
                    "stderr": stderr,
                    "duration": duration,
                    "timeout": timeout,
                    "killed_on_timeout": False,
                    "start_time": start_time.isoformat(),
                    "end_time": end_time.isoformat(),
                    "message": f"Command completed with exit code {process.returncode} in {duration:.2f}s"
                }

            except subprocess.TimeoutExpired:
                # Timeout occurred - collect output before killing
                end_time = datetime.now()
                duration = (end_time - start_time).total_seconds()

                # Collect any output that's available before termination
                collected_stdout = ""
                collected_stderr = ""

                try:
                    # Try to get partial output with very short timeout
                    stdout, stderr = process.communicate(timeout=0.1)
                    collected_stdout = stdout or ""
                    collected_stderr = stderr or ""
                except subprocess.TimeoutExpired:
                    # Process didn't respond, force termination and collect what we can
                    process.terminate()
                    try:
                        stdout, stderr = process.communicate(timeout=2.0)
                        collected_stdout = stdout or ""
                        collected_stderr = stderr or ""
                    except subprocess.TimeoutExpired:
                        # Force kill if terminate didn't work
                        process.kill()
                        try:
                            stdout, stderr = process.communicate(timeout=1.0)
                            collected_stdout = stdout or ""
                            collected_stderr = stderr or ""
                        except:
                            # Final fallback - use empty strings if everything fails
                            pass

                return {
                    "success": False,
                    "state": "IDLE",
                    "command": command,
                    "exit_code": -1,
                    "stdout": collected_stdout,
                    "stderr": collected_stderr,
                    "duration": duration,
                    "timeout": timeout,
                    "killed_on_timeout": True,
                    "error": f"Command timed out after {timeout}s and was killed",
                    "start_time": start_time.isoformat(),
                    "end_time": end_time.isoformat(),
                    "message": f"Command killed after {timeout}s timeout"
                }

        except Exception as e:
            return {
                "success": False,
                "state": "IDLE",
                "command": command,
                "error": f"Failed to execute command: {str(e)}",
                "suggestions": [
                    "Check if the command syntax is correct",
                    "Verify that required programs are installed"
                ]
            }

    def _start_interactive(self, command: str, timeout: int) -> Dict[str, Any]:
        """Start interactive command and wait for timeout."""
        try:
            start_time = datetime.now()
            self.last_output_time = start_time

            # Start process with improved buffering
            process = subprocess.Popen(
                command,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                stdin=subprocess.PIPE,
                text=True,
                bufsize=1  # Line buffering for better real-time output in Linux/WSL
            )

            # Store active process info
            self.active_process = {
                "process": process,
                "command": command,
                "start_time": start_time,
                "timeout": timeout,
                "stdout_lines": [],
                "stderr_lines": [],
                "last_output_time": start_time
            }

            # Wait for timeout and collect output
            return self._wait_and_collect_output(timeout)

        except Exception as e:
            self.active_process = None
            return {
                "success": False,
                "state": "IDLE",
                "command": command,
                "error": f"Failed to start interactive command: {str(e)}",
                "suggestions": [
                    "Check if the command is valid",
                    "Ensure required programs are installed"
                ]
            }

    def _wait_and_collect_output(self, timeout: int) -> Dict[str, Any]:
        """Simple timeline-based output collection with timeout."""
        if self.active_process is None:
            return {
                "success": False,
                "state": "IDLE",
                "error": "No active process"
            }

        process = self.active_process["process"]
        proc_info = self.active_process

        # Timeline points
        t3_start = datetime.now()  # t3: when user sent command
        t4_target = t3_start + timedelta(seconds=timeout)  # target t4

        # Collect gap output (t2→t3) - output that accumulated while user was deciding
        gap_start_lines_stdout = len(proc_info.get("stdout_lines", []))
        gap_start_lines_stderr = len(proc_info.get("stderr_lines", []))

        try:
            # Simple wait loop with periodic output collection
            while datetime.now() < t4_target:
                # Check if process completed early
                return_code = process.poll()
                if return_code is not None:
                    # Process completed before timeout (t4 < t3 + timeout)
                    t4_actual = datetime.now()
                    self._mark_process_completed()

                    # For completed processes, ensure we get all remaining output
                    try:
                        # Use communicate() to get any remaining output since process is done
                        remaining_stdout, remaining_stderr = process.communicate(timeout=2.0)
                        if remaining_stdout and remaining_stdout.strip():
                            for line in remaining_stdout.split('\n'):
                                if line.strip():
                                    proc_info.setdefault("stdout_lines", []).append(line.rstrip())
                        if remaining_stderr and remaining_stderr.strip():
                            for line in remaining_stderr.split('\n'):
                                if line.strip():
                                    proc_info.setdefault("stderr_lines", []).append(line.rstrip())
                    except subprocess.TimeoutExpired:
                        # If communicate times out, the process might be stuck - kill it
                        try:
                            process.kill()
                            remaining_stdout, remaining_stderr = process.communicate(timeout=1.0)
                            if remaining_stdout and remaining_stdout.strip():
                                for line in remaining_stdout.split('\n'):
                                    if line.strip():
                                        proc_info.setdefault("stdout_lines", []).append(line.rstrip())
                            if remaining_stderr and remaining_stderr.strip():
                                for line in remaining_stderr.split('\n'):
                                    if line.strip():
                                        proc_info.setdefault("stderr_lines", []).append(line.rstrip())
                        except:
                            pass
                    except:
                        # If communicate fails completely, fall back to the non-blocking method
                        self._collect_available_output()

                    # Return gap output + completion output
                    all_stdout = proc_info.get("stdout_lines", [])
                    all_stderr = proc_info.get("stderr_lines", [])

                    gap_output = {
                        "stdout": all_stdout[gap_start_lines_stdout:],
                        "stderr": all_stderr[gap_start_lines_stderr:],
                        "return_code": return_code,
                        "duration": (t4_actual - proc_info["start_time"]).total_seconds(),
                        "completed_early": True,
                        "actual_end_time": t4_actual.isoformat()
                    }

                    self.active_process = None
                    return {
                        "success": True,
                        "state": "IDLE",
                        "completed": True,
                        "command": proc_info["command"],
                        "output": gap_output,
                        "message": f"Command completed with exit code {return_code}"
                    }

                # Collect available output periodically (non-blocking)
                self._collect_available_output()

                # Small sleep to prevent busy waiting
                time.sleep(0.1)

            # Timeout reached, process still running (t4 = t3 + timeout)
            t4_timeout = datetime.now()

            # Enhanced final collection at timeout - try harder to get output
            for _ in range(3):  # Try multiple times to ensure we get all available output
                self._collect_available_output()
                time.sleep(0.05)  # Small delay between attempts

            # Return gap output + timeout period output
            all_stdout = proc_info.get("stdout_lines", [])
            all_stderr = proc_info.get("stderr_lines", [])

            timeout_output = {
                "stdout": all_stdout[gap_start_lines_stdout:],
                "stderr": all_stderr[gap_start_lines_stderr:],
                "total_stdout_lines": len(all_stdout),
                "total_stderr_lines": len(all_stderr),
                "timeout": timeout,
                "still_running": True,
                "timeout_end": t4_timeout.isoformat()
            }

            self.last_output_time = t4_timeout

            return {
                "success": True,
                "state": "RUNNING",
                "timeout_reached": True,
                "command": proc_info["command"],
                "output": timeout_output,
                "control_options": [
                    "Send '' to continue for another timeout period",
                    "Send 'C-c' to kill the process",
                    "Send '>>> <input>' to send input to the process"
                ],
                "message": f"Timeout reached after {timeout}s, process still running"
            }

        except Exception as e:
            return {
                "success": False,
                "state": "RUNNING",
                "error": f"Error collecting output: {str(e)}"
            }

    def _send_input_and_wait(self, input_text: str, timeout: int) -> Dict[str, Any]:
        """Send input to process and wait for timeout - simple approach."""
        if self.active_process is None:
            return {
                "success": False,
                "state": "IDLE",
                "error": "No active process"
            }

        try:
            process = self.active_process["process"]

            # Send input first - don't try to read output immediately
            process.stdin.write(input_text + '\n')
            process.stdin.flush()

            # Longer delay to let input be processed (especially for interactive programs)
            time.sleep(0.5)

            # Now wait for timeout and collect output using timeline approach
            return self._wait_and_collect_output(timeout)

        except Exception as e:
            return {
                "success": False,
                "state": "RUNNING",
                "error": f"Failed to send input: {str(e)}"
            }

    def _kill_process(self) -> Dict[str, Any]:
        """Kill the active process with progressive termination and output capture."""
        if self.active_process is None:
            return {
                "success": False,
                "state": "IDLE",
                "error": "No active process to kill"
            }

        try:
            process = self.active_process["process"]
            command = self.active_process["command"]
            proc_info = self.active_process

            # Collect any final output before killing
            self._collect_available_output()
            final_output = {
                "stdout": proc_info["stdout_lines"],
                "stderr": proc_info["stderr_lines"]
            }

            # Progressive termination with output collection
            collected_stdout = ""
            collected_stderr = ""
            method = "terminated"
            return_code = None

            try:
                # First try terminate with output collection
                process.terminate()
                stdout, stderr = process.communicate(timeout=2.0)
                collected_stdout = stdout or ""
                collected_stderr = stderr or ""
                return_code = process.returncode
                method = "terminated"
            except subprocess.TimeoutExpired:
                try:
                    # Force kill if terminate didn't work
                    process.kill()
                    stdout, stderr = process.communicate(timeout=1.0)
                    collected_stdout = stdout or ""
                    collected_stderr = stderr or ""
                    return_code = process.returncode
                    method = "force killed"
                except subprocess.TimeoutExpired:
                    # Final fallback
                    return_code = -9
                    method = "force killed (no response)"
                except Exception:
                    return_code = -9
                    method = "force killed (error)"

            # Merge any additional output collected during termination
            if collected_stdout.strip():
                for line in collected_stdout.split('\n'):
                    if line.strip():
                        final_output["stdout"].append(line.rstrip())

            if collected_stderr.strip():
                for line in collected_stderr.split('\n'):
                    if line.strip():
                        final_output["stderr"].append(line.rstrip())

            self.active_process = None

            return {
                "success": True,
                "state": "IDLE",
                "killed": True,
                "command": command,
                "method": method,
                "return_code": return_code,
                "output": final_output,
                "message": f"Process {method} successfully"
            }

        except Exception as e:
            return {
                "success": False,
                "state": "RUNNING",
                "error": f"Failed to kill process: {str(e)}"
            }

    # Legacy methods for compatibility (these should not be used with new 2-state design)
    def get_output(self, max_lines: int = 100) -> Dict[str, Any]:
        """Legacy method - should not be used with 2-state design."""
        return {
            "success": False,
            "error": "get_output() is deprecated. Use run_command() with control commands.",
            "message": "Use '' to continue, 'C-c' to kill, or '>>> input' to send input"
        }

    def send_input(self, input_text: str) -> Dict[str, Any]:
        """Legacy method - should not be used with 2-state design."""
        return {
            "success": False,
            "error": "send_input() is deprecated. Use run_command() with '>>> input' format.",
            "message": f"Use run_command('>>> {input_text}', timeout, True) instead"
        }

    def stop_process(self, force: bool = False) -> Dict[str, Any]:
        """Legacy method - should not be used with 2-state design."""
        return {
            "success": False,
            "error": "stop_process() is deprecated. Use run_command() with 'C-c' command.",
            "message": "Use run_command('C-c', timeout, True) instead"
        }

    def get_status(self) -> Dict[str, Any]:
        """Get current tool status."""
        state = self._get_state()

        if state == "IDLE":
            return {
                "success": True,
                "state": state,
                "active_process": None,
                "message": "No active process"
            }

        # Refresh state first
        self._refresh_state()
        current_state = self._get_state()

        if current_state == "IDLE":
            return {
                "success": True,
                "state": current_state,
                "active_process": None,
                "message": "Process just completed"
            }

        proc_info = self.active_process
        return {
            "success": True,
            "state": current_state,
            "active_process": {
                "command": proc_info["command"],
                "pid": proc_info["process"].pid,
                "start_time": proc_info["start_time"].isoformat(),
                "runtime": (datetime.now() - proc_info["start_time"]).total_seconds(),
                "stdout_lines": len(proc_info["stdout_lines"]),
                "stderr_lines": len(proc_info["stderr_lines"])
            },
            "message": "Process running"
        }

