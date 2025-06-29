from typing import Optional


class Coords2D:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"[{self.x}, {self.y}]"

    def __eq__(self, other) -> bool:
        if isinstance(other, Coords2D):
            return self.x == other.x and self.y == other.y
        if isinstance(other, list):
            return [self.x, self.y] == other
        return False


class Coords3D(Coords2D):
    def __init__(self, x: int = 0, y: int = 0, z: int = 0) -> None:
        super().__init__(x, y)
        self.z = z

    def __repr__(self) -> str:
        return f"[{self.x}, {self.y}, {self.z}]"

    def __eq__(self, other) -> bool:
        if isinstance(other, Coords3D):
            return self.x == other.x and self.y == other.y and self.z == other.z
        if isinstance(other, list):
            return [self.x, self.y, self.z] == other
        return False


class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(
        self,
        name: str,
        weight: int,
        coords: Optional[Coords2D | list[int]] = None
    ) -> None:
        self.name = name
        self.weight = weight

        if coords is None:
            coords = Coords2D()
        elif isinstance(coords, list):
            coords = Coords2D(*coords)

        self.coords = coords

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"

    def go_forward(self, step: int = 1) -> None:
        self.coords.y += step

    def go_back(self, step: int = 1) -> None:
        self.coords.y -= step

    def go_right(self, step: int = 1) -> None:
        self.coords.x += step

    def go_left(self, step: int = 1) -> None:
        self.coords.x -= step


class FlyingRobot(BaseRobot):
    def __init__(
        self,
        name: str,
        weight: int,
        coords: Optional[Coords3D | list[int]] = None
    ) -> None:
        if coords is None:
            coords = Coords3D()
        elif isinstance(coords, list):
            coords = Coords3D(*coords)

        super().__init__(name, weight, coords)

    def go_up(self, step: int = 1) -> None:
        self.coords.z += step

    def go_down(self, step: int = 1) -> None:
        self.coords.z -= step


class DeliveryDrone(FlyingRobot):
    def __init__(
        self,
        name: str,
        weight: int,
        max_load_weight: int,
        coords: Optional[Coords3D | list[int]] = None,
        current_load: Optional[Cargo] = None
    ) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None