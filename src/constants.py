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
Defines mass and radius constants of important celestial objects.

Author: Tobias Briones
"""

G = 6.67e-11

EARTH_MASS_KG = 5.97e24
EARTH_RADIUS_KM = 6370

MOON_MASS_KG = 0.0123 * EARTH_MASS_KG
MOON_RADIUS_KM = 1737

MARS_MASS_KG = 0.107 * EARTH_MASS_KG
MARS_RADIUS_KM = 3400

JUPITER_MASS_KG = 317.8 * EARTH_MASS_KG
JUPITER_RADIUS_KM = 69900

SUN_MASS_KG = 1.99e30
SUN_RADIUS_KM = 696000

WHITE_DWARF_MASS_KG = 1.005 * SUN_MASS_KG
WHITE_DWARF_RADIUS_KM = 6000

NEUTRON_STAR_MASS_KG = 1.4 * SUN_MASS_KG
NEUTRON_STAR_RADIUS_KM = 10

BLACK_HOLE_MASS_KG = 15 * SUN_MASS_KG
BLACK_HOLE_RADIUS_KM = 135
