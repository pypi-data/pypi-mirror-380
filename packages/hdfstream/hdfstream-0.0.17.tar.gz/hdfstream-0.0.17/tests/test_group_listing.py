#!/bin/env python

import hdfstream
import numpy as np
import pytest
from test_data import snap_data

@pytest.mark.vcr
def test_root_group_listing(eagle_snap_file):

    # Open the root HDF5 group and check its contents
    root_group = eagle_snap_file()["/"]
    expected_groups = set(["Config","Constants","HashTable","Header","Parameters",
                           "PartType0","PartType1","RuntimePars","Units"])
    assert set(root_group.keys()) == expected_groups

@pytest.mark.vcr
def test_parttype1_group_listing(eagle_snap_file):

    # Open a HDF5 group and check its contents
    ptype1 = eagle_snap_file()["/PartType1"]
    expected_datasets = set(["Coordinates", "GroupNumber", "ParticleIDs",
                            "SubGroupNumber", "Velocity"])
    assert set(ptype1.keys()) == expected_datasets
    for name in ptype1.keys():
        assert isinstance(ptype1[name], hdfstream.RemoteDataset)

@pytest.mark.vcr
def test_group_attributes(eagle_snap_file):

    # Open a HDF5 group and check its attributes:
    # Here we compare values decoded from the mock http response to pickled
    # test data which was extracted from the snapshot with h5py.
    header = eagle_snap_file()["/Header"]
    assert set(header.attrs.keys()) == set(snap_data["header"].keys())
    for name in header.attrs.keys():
        assert np.all(header.attrs[name] == snap_data["header"][name])

@pytest.mark.vcr
def test_parttype1_group_visit(eagle_snap_file):

    # Open a HDF5 group
    ptype1 = eagle_snap_file()["/PartType1"]

    # Use the visit method to make a list of members
    members = []
    ptype1.visit(lambda name : members.append(name))
    expected_datasets = set(["Coordinates", "GroupNumber", "ParticleIDs",
                            "SubGroupNumber", "Velocity"])
    assert set(members) == expected_datasets

@pytest.mark.vcr
def test_parttype1_group_visititems(eagle_snap_file):

    # Open a HDF5 group
    ptype1 = eagle_snap_file()["/PartType1"]

    # Use the visititems method to make a dict of members
    members = {}
    def store_object(name, obj):
        members[name] = obj
    ptype1.visititems(store_object)
    expected_datasets = set(["Coordinates", "GroupNumber", "ParticleIDs",
                             "SubGroupNumber", "Velocity"])
    assert set(members.keys()) == expected_datasets
    for name, obj in members.items():
        assert ptype1[name] is obj
