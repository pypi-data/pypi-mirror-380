# MIT License
#
# Copyright (c) 2025 ericsmacedo
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Tests the CLI for the harmonic analysis function."""

import matplotlib.pyplot as plt
import numpy as np
from click.testing import CliRunner
from pytest import mark

from harm_analysis.cli import harm_analysis_cmd, spec_analysis_cmd


@mark.parametrize("cli_name", ["harm", "spec"])
def test_cli(monkeypatch, cli_name):
    """Test for harm_analysis function.

    Checks if the function can obtain results with less than 0.1 dB of error.
    """
    # test signal
    n = 2048
    fs = 1000
    t = np.arange(0, n / fs, 1 / fs)

    noise_pow_db = -70
    noise_std = 10 ** (noise_pow_db / 20)
    dc_level = 0.123456789

    random_state = np.random.RandomState(1234567890)
    noise = random_state.normal(loc=0, scale=noise_std, size=len(t))

    f1 = 100.13

    x = (
        dc_level
        + 2 * np.cos(2 * np.pi * f1 * t)
        + 0.01 * np.cos(2 * np.pi * f1 * 2 * t)
        + 0.005 * np.cos(2 * np.pi * f1 * 3 * t)
        + noise
    )

    # Save data to TXT file
    np.savetxt("test_data_cli.txt", x, delimiter="\n")

    runner = CliRunner()

    called = {}

    def fake_show():
        called["was_called"] = True

    monkeypatch.setattr(plt, "show", fake_show)

    if cli_name == "harm":
        result = runner.invoke(harm_analysis_cmd, ["test_data_cli.txt", "--fs", fs, "--plot"])
    elif cli_name == "spec":
        result = runner.invoke(spec_analysis_cmd, ["test_data_cli.txt", "--fs", fs, "--plot"])

    assert "was_called" in called

    assert result.exit_code == 0
