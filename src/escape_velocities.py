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
Defines constants for storing the requested escape velocities.

Author: Tobias Briones
"""

import constants as cons
import compute

EARTH_ESCAPE_VELOCITY_KM_S = compute.get_escape_velocity_km_s(
    cons.EARTH_MASS_KG,
    cons.EARTH_RADIUS_KM
)

MOON_ESCAPE_VELOCITY_KM_S = compute.get_escape_velocity_km_s(
    cons.MOON_MASS_KG,
    cons.MOON_RADIUS_KM
)

MARS_ESCAPE_VELOCITY_KM_S = compute.get_escape_velocity_km_s(
    cons.MARS_MASS_KG,
    cons.MARS_RADIUS_KM
)

JUPITER_ESCAPE_VELOCITY_KM_S = compute.get_escape_velocity_km_s(
    cons.JUPITER_MASS_KG,
    cons.JUPITER_RADIUS_KM
)

SUN_ESCAPE_VELOCITY_KM_S = compute.get_escape_velocity_km_s(
    cons.SUN_MASS_KG,
    cons.SUN_RADIUS_KM
)

WHITE_DWARF_ESCAPE_VELOCITY_KM_S = compute.get_escape_velocity_km_s(
    cons.WHITE_DWARF_MASS_KG,
    cons.WHITE_DWARF_RADIUS_KM
)

NEUTRON_STAR_ESCAPE_VELOCITY_KM_S = compute.get_escape_velocity_km_s(
    cons.NEUTRON_STAR_MASS_KG,
    cons.NEUTRON_STAR_RADIUS_KM
)

BLACK_HOLE_ESCAPE_VELOCITY_KM_S = compute.get_escape_velocity_km_s(
    cons.BLACK_HOLE_MASS_KG,
    cons.BLACK_HOLE_RADIUS_KM
)
