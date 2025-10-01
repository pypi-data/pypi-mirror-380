#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2020-2025 Félix Chénier

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


__author__ = "Félix Chénier"
__copyright__ = "Copyright (C) 2020-2025 Félix Chénier"
__email__ = "chenier.felix@uqam.ca"
__license__ = "Apache 2.0"


import kineticstoolkit_extensions.pushrimkinetics as pk
import numpy as np
import os


this_folder = os.path.dirname(__file__)


TEST_CALIBRATION_MATRIX = {
    "gains": np.array([-0.106, 0.106, 0.094, 0.022, -0.022, 0.0234999]),
    "offsets": np.array([0.0, 10.0, 0.0, 0.0, 0.0, 0.0]),
    "transducer": "smartwheel",
}


def test_read_smartwheel():
    """Test that read_file works similarly for SW's csv and txt files."""
    kinetics_csv = pk.read_smartwheel(
        this_folder + "/data/pushrimkinetics_propulsion.csv"
    )

    kinetics_txt = pk.read_smartwheel(
        this_folder + "/data/pushrimkinetics_propulsion.txt"
    )

    smaller = min(kinetics_csv.time.shape[0], kinetics_txt.time.shape[0])

    assert np.allclose(
        kinetics_csv.data["Channels"][0:smaller],
        kinetics_txt.data["Channels"][0:smaller],
    )
    assert (
        np.std(
            kinetics_csv.data["Angle"][0:smaller]
            - kinetics_txt.data["Angle"][0:smaller]
        )
        < 1e-4
    )


def test_remove_offsets():
    """Test that remove_offsets works with and without a baseline."""
    kinetics = pk.read_smartwheel(
        this_folder + "/data/pushrimkinetics_offsets_propulsion.csv"
    )

    baseline = pk.read_smartwheel(
        this_folder + "/data/pushrimkinetics_offsets_baseline.csv"
    )

    no_offsets1 = pk.remove_offsets(kinetics)
    no_offsets2 = pk.remove_offsets(kinetics, baseline)

    # Assert that all force differences are within 1 N
    assert np.all(
        np.abs(no_offsets1.data["Forces"] - no_offsets2.data["Forces"]) < 1
    )

    # Assert that all moment differences are within 0.1 Nm
    assert np.all(
        np.abs(no_offsets1.data["Moments"] - no_offsets2.data["Moments"]) < 0.1
    )


def test_apply_calibration():
    """Test that force calculation is similar to precalculated forces."""
    kinetics = pk.read_smartwheel(
        this_folder + "/data/pushrimkinetics_offsets_propulsion.csv"
    )

    test = kinetics.copy()
    test = pk.apply_calibration(
        test,
        **TEST_CALIBRATION_MATRIX,
        reference_frame="hub",
    )

    assert np.allclose(
        np.mean(np.abs(test.data["Forces"]), axis=0),
        np.mean(np.abs(kinetics.data["Forces"]), axis=0),
        atol=2,
    )
    assert np.allclose(
        np.std(np.abs(test.data["Forces"]), axis=0),
        np.std(np.abs(kinetics.data["Forces"]), axis=0),
        atol=2,
    )
    assert np.allclose(
        np.mean(np.abs(test.data["Moments"]), axis=0),
        np.mean(np.abs(kinetics.data["Moments"]), axis=0),
        atol=2,
    )
    assert np.allclose(
        np.std(np.abs(test.data["Moments"]), axis=0),
        np.std(np.abs(kinetics.data["Moments"]), axis=0),
        atol=2,
    )


def test_calculate_velocity_power():
    """No-regression test for calculate_velocity and calculate_power."""
    kinetics = pk.read_smartwheel(
        this_folder + "/data/pushrimkinetics_offsets_propulsion.csv"
    )

    kinetics = pk.calculate_velocity(kinetics)
    assert np.allclose(
        [
            np.mean(kinetics.data["Velocity"]),
            np.std(kinetics.data["Velocity"]),
        ],
        [2.875997177730561, 0.8584197191949383],
    )

    kinetics = pk.calculate_power(kinetics)
    assert np.allclose(
        kinetics.data["Velocity"] * kinetics.data["Moments"][:, 2],
        kinetics.data["Power"],
    )


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
