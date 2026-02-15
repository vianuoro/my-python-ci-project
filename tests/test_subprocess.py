import pytest
from app.subprocess import run_shell_command


def test_run_simple_echo_command():
    """Test basic echo command"""
    result = run_shell_command("echo 'Hello World'")
    assert result == "Hello World"


def test_run_command_with_pipes():
    """Test command with pipes and shell features"""
    result = run_shell_command("echo 'hello world' | tr '[:lower:]' '[:upper:]'")
    assert result == "HELLO WORLD"


def test_run_command_with_error():
    """Test that errors are properly caught and returned"""
    result = run_shell_command("ls /nonexistent_directory")
    assert "Error occurred:" in result


def test_run_command_returns_string():
    """Test that output is returned as a string"""
    result = run_shell_command("echo 'test'")
    assert isinstance(result, str)


def test_run_command_strips_whitespace():
    """Test that output is stripped of trailing whitespace"""
    result = run_shell_command("echo 'test'")
    assert result == "test"
    assert not result.endswith("\n")
