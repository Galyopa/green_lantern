import pytest
from lonely_robot import Robot, Asteroid, MissAsteroidError


class TestRobotCreation:
    def test_parameters(self):
        x, y = 10, 15
        asteroid = Asteroid(x + 1, y + 1)
        direction = "E"
        robot = Robot(x, y, asteroid, direction)
        assert robot.x == 10
        assert robot.y == 15
        assert robot.direction == direction
        assert robot.asteroid == asteroid

    @pytest.mark.parametrize(
        "asteroid_size,robot_coordinates",
        (
                ((15, 25), (26, 30)),
                ((15, 25), (26, 24)),
                ((15, 25), (15, 27)),
        )
    )
    def test_check_if_robot_on_asteroid(self, asteroid_size, robot_coordinates):
        with pytest.raises(MissAsteroidError):
            asteroid = Asteroid(*asteroid_size)
            Robot(*robot_coordinates, asteroid, "W")

class TestTurns:
    def setup(self):
        x, y = 10, 15
        self.asteroid = Asteroid(x + 1, y + 1)

    @pytest.mark.parametrize(
        "curent_direction,expected_direction",
        (
                ("N", "W"),
                ("W", "S"),
                ("S", "E"),
        )
    )
    def test_turn_left(self, curent_direction, expected_direction):
        robot = Robot(x, y, asteroid, curent_direction)
        robot.turn_left()
        assert robot.direction == expected_direction

