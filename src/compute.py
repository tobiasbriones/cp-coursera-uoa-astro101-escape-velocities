#
#  Copyright (c) 2020 Tobias Briones. All rights reserved.
#
#  SPDX-License-Identifier: BSD-3-Clause
#
#  This file is part of Course Project at Coursera-UoA-Astro101: Escape
#  Velocities.
#
#  This source code is licensed under the BSD-3-Clause License found in the
#  LICENSE file in the root directory of this source tree or at
#  https://opensource.org/licenses/BSD-3-Clause.
#

"""
Provides functions that compute escape velocities.

Author: Tobias Briones
"""

import math
import constants

DEF_NUMBER_OF_DECIMALS = 4


def get_escape_velocity_meters_s(mass_kg, radius_km):
    radius_meters = radius_km * 1000
    sqrt_arg = (2 * constants.G * mass_kg) / radius_meters
    escape_velocity_meters_s = math.sqrt(sqrt_arg)
    return escape_velocity_meters_s


def get_escape_velocity_km_s(mass_kg, radius_km, decimals=DEF_NUMBER_OF_DECIMALS):
    escape_velocity_meters_s = get_escape_velocity_meters_s(mass_kg, radius_km)
    escape_velocity_km_s = escape_velocity_meters_s / 1000
    return round(escape_velocity_km_s, decimals)
