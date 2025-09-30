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
from collections import deque
from dataclasses import dataclass, field
from typing import Deque

from .shift_register import ShiftRegister


@dataclass(frozen=True)
class State:
    clock: int = 0
    program_counter: int = 0
    pin_directions: int = 0
    pin_values: int = 0
    transmit_fifo: Deque[int] = field(default_factory=deque)
    receive_fifo: Deque[int] = field(default_factory=deque)
    input_shift_register: ShiftRegister = field(
        default_factory=lambda: ShiftRegister(0, 0)
    )
    output_shift_register: ShiftRegister = field(
        default_factory=lambda: ShiftRegister(0, 32)
    )
    x_register: int = 0
    y_register: int = 0
