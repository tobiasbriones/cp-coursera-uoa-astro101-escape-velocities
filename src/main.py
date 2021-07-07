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
Prints the results!

Author: Tobias Briones
"""

import escape_velocities as ev

print()
print("Escape velocities (km/s):")
print()

print("Earth: ", ev.EARTH_ESCAPE_VELOCITY_KM_S)
print("Moon: ", ev.MOON_ESCAPE_VELOCITY_KM_S)
print("Mars: ", ev.MARS_ESCAPE_VELOCITY_KM_S)
print("Jupiter: ", ev.JUPITER_ESCAPE_VELOCITY_KM_S)
print("Sun: ", ev.SUN_ESCAPE_VELOCITY_KM_S)
print("White Dwarf: ", ev.WHITE_DWARF_ESCAPE_VELOCITY_KM_S)
print("Neutron Star: ", ev.NEUTRON_STAR_ESCAPE_VELOCITY_KM_S)
print("Black Hole: ", ev.BLACK_HOLE_ESCAPE_VELOCITY_KM_S)
