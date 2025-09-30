# Copyright 2021, 2022, 2023 Nathan Young
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from typing import Callable, Literal
from .state import State


def clock_cycles_reached(target_value: int) -> Callable[[int, State], bool]:
    return lambda _, state: state.clock >= target_value


def always(_: State) -> Literal[True]:
    return True


def negate(predicate: Callable[[State], bool]) -> Callable[[State], bool]:
    def wrapper(state: State) -> bool:
        return not predicate(state)

    return wrapper


def gpio_low(pin_number: int, state: State) -> bool:
    return not gpio_high(pin_number, state)


def gpio_high(pin_number: int, state: State) -> bool:
    return state.pin_values & (1 << pin_number) != 0


def transmit_fifo_empty(state: State) -> bool:
    return len(state.transmit_fifo) == 0


def transmit_fifo_full(state: State) -> bool:
    return len(state.transmit_fifo) == 4


def receive_fifo_empty(state: State) -> bool:
    return len(state.receive_fifo) == 0


def receive_fifo_full(state: State) -> bool:
    return len(state.receive_fifo) == 4


def x_register_equals_zero(state: State) -> bool:
    return state.x_register == 0


def x_register_not_equal_to_zero(state: State) -> bool:
    return state.x_register != 0


def y_register_equals_zero(state: State) -> bool:
    return state.y_register == 0


def y_register_not_equal_to_zero(state: State) -> bool:
    return state.y_register != 0


def x_register_not_equal_to_y_register(state: State) -> bool:
    return state.x_register != state.y_register


def input_shift_register_full(state: State) -> bool:
    return state.input_shift_register.counter == 32


def output_shift_register_empty(state: State) -> bool:
    return state.output_shift_register.counter == 32
