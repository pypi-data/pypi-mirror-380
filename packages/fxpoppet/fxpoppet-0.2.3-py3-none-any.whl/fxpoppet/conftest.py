# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""Common unit test fixtures for fxpoppet."""

from pytest import fixture


@fixture
def tmp_session_adb_check(mocker):
    """Mock adb binary location lookup function"""
    mocker.patch("fxpoppet.adb_session.ADBSession._adb_check", return_value="fake_adb")
