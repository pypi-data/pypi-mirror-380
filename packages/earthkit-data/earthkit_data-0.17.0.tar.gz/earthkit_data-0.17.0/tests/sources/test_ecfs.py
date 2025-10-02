#!/usr/bin/env python3

# (C) Copyright 2020 ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

import pytest

from earthkit.data import from_source
from earthkit.data.testing import NO_ECFS


@pytest.mark.long_test
@pytest.mark.download
@pytest.mark.ecfs
@pytest.mark.skipif(NO_ECFS, reason="No access to ECFS")
def test_ecfs_download():
    s = from_source(
        "ecfs",
        "ec:/cgr/test.grib",
    )
    assert len(s) == 2


if __name__ == "__main__":
    from earthkit.data.testing import main

    main(__file__)
