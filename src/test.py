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
Defines the expected values to test the results.

Author: Tobias Briones
"""

import escape_velocities as ev

CORRECT_VALUES = {
    "earth": 11.1814,
    "moon": 2.3747,
    "mars": 5.0063,
    "jupiter": 60.1732,
    "sun": 617.5894,
    "white_dwarf": 6668.2498,
    "neutron_star": 192782.8831,
    "black_hole": 171744.6425
}


def check(expected, computed, label):
    """Checks the test result, if wrong then prints a fail message."""
    success = True

    if expected != computed:
        success = False
        print("FAILED TEST AT: ", label)
    return success


def from_result_to_int(test_result):
    """Maps the boolean test_result param to: True -> 1, False -> 0."""
    return 1 if test_result else 0


def report(succeeded):
    """
    Prints the final report of this test suite. It includes passed and failed tests.
    """
    number_of_tests = len(CORRECT_VALUES)
    failed = number_of_tests - succeeded

    print("Tests completed. Succeeded: %d, Failed: %d" % (succeeded, failed))


def run():
    succeeded_count = 0

    result = check(CORRECT_VALUES["earth"], ev.EARTH_ESCAPE_VELOCITY_KM_S, "Earth")
    succeeded_count += from_result_to_int(result)

    result = check(CORRECT_VALUES["moon"], ev.MOON_ESCAPE_VELOCITY_KM_S, "Moon")
    succeeded_count += from_result_to_int(result)

    result = check(CORRECT_VALUES["mars"], ev.MARS_ESCAPE_VELOCITY_KM_S, "Mars")
    succeeded_count += from_result_to_int(result)

    result = check(CORRECT_VALUES["jupiter"], ev.JUPITER_ESCAPE_VELOCITY_KM_S, "Jupiter")
    succeeded_count += from_result_to_int(result)

    result = check(CORRECT_VALUES["sun"], ev.SUN_ESCAPE_VELOCITY_KM_S, "Sun")
    succeeded_count += from_result_to_int(result)

    result = check(CORRECT_VALUES["white_dwarf"], ev.WHITE_DWARF_ESCAPE_VELOCITY_KM_S, "White Dwarf")
    succeeded_count += from_result_to_int(result)

    result = check(CORRECT_VALUES["neutron_star"], ev.NEUTRON_STAR_ESCAPE_VELOCITY_KM_S, "Neutron Star")
    succeeded_count += from_result_to_int(result)

    result = check(CORRECT_VALUES["black_hole"], ev.BLACK_HOLE_ESCAPE_VELOCITY_KM_S, "Black Hole")
    succeeded_count += from_result_to_int(result)

    report(succeeded_count)


run()
