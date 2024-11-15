#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright 2024  darryl mcculley

#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     any later version.

#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.

#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.

from typing import Any, Optional, Literal
Int = int
Float = float

from pydantic import BaseModel
from random import choices as r_choices, seed as r_seed
from numpy.random import normal as r_normal, seed as n_seed

def seed(seed:int):
    n_seed(seed); r_seed(seed)
    return seed

class simd_func (BaseModel):
    def simulate(self):
        raise NotImplementedError()

class float (simd_func):
    func:Literal["float"]="float"
    mean:Float
    std:Float
    min:Float
    max:Float
    precision:Optional[Int]=3

    def simulate(self):
        value = r_normal(self.mean, self.std)
        while value < self.min or value > self.max:
            value = r_normal(self.mean, self.std)
        return round(value, self.precision)
    
class int (float, simd_func):
    func:Literal['int']="int"

    @classmethod
    def create(cls, values:list[int]):
        f = super().create(values=values)
        return cls(mean=f.mean, std=f.std, min=f.min, max=f.max)

    def simulate(self):
        return Int(super().simulate())

class choice (simd_func):
    func:Literal["choice"]="choice"
    choices:list[Any]
    weights:list[Int|Float]
    n:Optional[Int]=1

    def simulate(self):
        choice = r_choices(self.choices, weights=self.weights, k=self.n)
        if self.n == 1: return choice[0]
        return choice

class literal (simd_func):
    func:Literal["literal"]="literal"
    value:Any

    def simulate(self):
        return self.value