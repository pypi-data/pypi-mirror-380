#!/bin/env python

import pytest
from hdfstream import RemoteDirectory

@pytest.mark.vcr
def test_root_listing(server_url):

    import hdfstream
    root = hdfstream.open(server_url, "/")
    assert isinstance(root, RemoteDirectory)

@pytest.mark.vcr
def test_eagle_dir_listing(server_url):

    import hdfstream
    eagle_dir = hdfstream.open(server_url, "/EAGLE")
    fm_dir = eagle_dir["Fiducial_models"]
    assert len(fm_dir) == 9
    expected_files = set(["description.md", "labels.msgpack"])
    assert set(fm_dir.files.keys()) == expected_files
    for name in fm_dir.files:
        assert isinstance(fm_dir[name], hdfstream.RemoteFile)
    expected_dirs = set(["RefL0012N0188", "RefL0025N0376", "RefL0025N0752", "RecalL0025N0752",
                         "RefL0050N0752", "AGNdT9L0050N0752", "RefL0100N1504"])
    assert set(fm_dir.directories.keys()) == expected_dirs

@pytest.mark.vcr
def test_eagle_file_listing(server_url):

    import hdfstream
    snap_dir = hdfstream.open(server_url,
                              "/EAGLE/Fiducial_models/RefL0012N0188/snapshot_028_z000p000")
    expected_files = set([f"snap_028_z000p000.{i}.hdf5" for i in range(16)])
    assert set(snap_dir.keys()) == expected_files
    assert set(snap_dir.files.keys()) == expected_files
    for filename in expected_files:
        f = snap_dir[filename]
        assert isinstance(f, hdfstream.RemoteFile)
        assert f.is_hdf5()
