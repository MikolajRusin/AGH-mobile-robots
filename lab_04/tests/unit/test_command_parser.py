import pytest

from src.command_parser import (
    parse_wheel_command, command_from_line,
    commands_from_text
)


@pytest.mark.parametrize('line, expected', [
    ('0.10,0.10,1.0', (0.10, 0.10, 1.0)),
    ('0.25, 0.25,1.0', (0.25, 0.25, 1.0)),
    ('0.45,0.45, 1.0', (0.45, 0.45, 1.0)),
    ('0.75, 0.45, 1.0', (0.75, 0.45, 1.0))
])
def test_parse_wheel_command(line, expected):
    parsed_command = parse_wheel_command(line)
    assert parsed_command == expected


@pytest.mark.parametrize('line, expected', [
    ('0.10,1.0', (0.10, 0.10, 1.0)),
    ('1.0', (0.25, 0.25, 1.0))
])
def test_parse_wheel_invalid_command(line, expected):
    with pytest.raises(ValueError):
        parsed_command = parse_wheel_command(line)


@pytest.mark.parametrize('line, expected_velocity, expected_omega, expected_duration',[
    ('0.10,0.10,1.0', 0.10, 0.0, 1.0),
    ('0.25,0.25,1.0', 0.25, 0.0, 1.0),
])
def test_command_from_line(
    line,
    expected_velocity,
    expected_omega,
    expected_duration,
):
    command = command_from_line(line, wheel_base=0.5)
    assert command.v == pytest.approx(expected_velocity)
    assert command.omega == pytest.approx(expected_omega)
    assert command.duration == pytest.approx(expected_duration)


def test_command_from_line_invalid_wheel_base():
    with pytest.raises(ValueError):
        command_from_line('0.10,0.10,1.0', wheel_base=0.0)


def test_commands_from_text_single_command():
    commands = commands_from_text('0.10,0.10,1.0', wheel_base=0.5)
    assert len(commands) == 1
    assert commands[0].v == pytest.approx(0.10)
    assert commands[0].omega == pytest.approx(0.0)
    assert commands[0].duration == pytest.approx(1.0)


def test_commands_from_text_multiple_commands():
    commands = commands_from_text(
        '0.10,0.10,1.0\n0.20,0.30,2.0',
        wheel_base=0.5
    )
    assert len(commands) == 2

    assert commands[0].v == pytest.approx(0.10)
    assert commands[0].omega == pytest.approx(0.0)
    assert commands[0].duration == pytest.approx(1.0)

    assert commands[1].v == pytest.approx(0.25)
    assert commands[1].omega == pytest.approx(0.2)
    assert commands[1].duration == pytest.approx(2.0)


def test_commands_from_text_ignores_empty_lines():
    commands = commands_from_text(
        '0.10,0.10,1.0\n\n0.20,0.30,2.0\n',
        wheel_base=0.5
    )
    assert len(commands) == 2


def test_commands_from_text_empty_text():
    commands = commands_from_text('', wheel_base=0.5)
    assert commands == []


def test_commands_from_text_invalid_line():
    with pytest.raises(ValueError):
        commands_from_text('0.10,0.10,1.0\ninvalid', wheel_base=0.5)