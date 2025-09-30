# -*- coding: utf-8 -*-

import os
import numpy as np
import pytest

from qa4sm_reader.img import QA4SMImg
from qa4sm_reader import globals


@pytest.fixture
def testfile_path():
    testfile = '0-ERA5_LAND.swvl1_with_1-C3S_combined.sm_with_2-SMOS_IC.Soil_Moisture.nc'
    testfile_path = os.path.join(os.path.dirname(__file__), '..', 'tests',
                                 'test_data', 'basic', testfile)

    return testfile_path


@pytest.fixture
def img(testfile_path):
    img = QA4SMImg(testfile_path, ignore_empty=False)

    return img


# todo: update with correct CI .nc file
@pytest.fixture
def ci_img():
    testfile = "0-ERA5.swvl1_with_1-ESA_CCI_SM_combined.sm_with_2-ESA_CCI_SM_combined.sm_with_3-ESA_CCI_SM_combined.sm_with_4-ESA_CCI_SM_combined.sm.CI.nc"
    testfile_path = os.path.join(os.path.dirname(__file__), '..', 'tests',
                                 'test_data', 'tc', testfile)
    img = QA4SMImg(testfile_path, ignore_empty=False)

    return img


@pytest.fixture
def metadata_img():
    testfile = "0-ISMN.soil_moisture_with_1-C3S.sm.nc"
    testfile_path = os.path.join(os.path.dirname(__file__), '..', 'tests',
                                 'test_data', 'metadata', testfile)
    img = QA4SMImg(testfile_path, ignore_empty=False)

    return img


def test_load_data(testfile_path):
    unloaded = QA4SMImg(testfile_path, load_data=False)
    assert 'varnames' not in unloaded.__dict__.keys()


def test_extent(testfile_path, img):
    extent = QA4SMImg(testfile_path,
                      extent=(48.300000000000004, 123.60000000000002,
                              -43.49999999999241, -9.799999999994327))
    assert img.extent != extent.extent
    assert img.extent == (48.300000000000004, 153.60000000000002,
                          -43.49999999999241, -9.799999999994327)


def test_metrics(testfile_path, img):
    metrics = QA4SMImg(testfile_path, metrics=['R'])
    assert metrics.common != img.common
    assert metrics.double != img.double
    assert 'R' in metrics.double.keys()


def test_load_vars(img):
    Vars = img._load_vars()
    assert len(Vars) == len(img.varnames)
    Metr_Vars = img._load_vars(only_metrics=True)
    assert len(Metr_Vars) == len(Vars) - 22


def test_iter_vars(img):
    for Var in img._iter_vars(type="metric"):
        assert Var.g in ['common', 'pairwise', 'triple']
    for Var in img._iter_vars(type="metric", filter_parms={'metric': 'R'}):
        assert Var.varname in [
            'R_between_0-ERA5_LAND_and_2-SMOS_IC',
            'R_between_0-ERA5_LAND_and_1-C3S_combined'
        ]


def test_iter_metrics(img):
    for Metr in img._iter_metrics(**{'g': 'pairwise'}):
        assert Metr.name in globals.metric_groups['pairwise']


def test_group_vars(img):
    Vars = img.group_vars(filter_parms={'metric': 'R'})
    names = [Var.varname for Var in Vars]
    assert names == [
        'R_between_0-ERA5_LAND_and_1-C3S_combined',
        'R_ci_lower_between_0-ERA5_LAND_and_1-C3S_combined',
        'R_ci_upper_between_0-ERA5_LAND_and_1-C3S_combined',
        'R_between_0-ERA5_LAND_and_2-SMOS_IC',
        'R_ci_lower_between_0-ERA5_LAND_and_2-SMOS_IC',
        'R_ci_upper_between_0-ERA5_LAND_and_2-SMOS_IC'
    ]


def test_group_metrics(img):
    common, double, triple = img.group_metrics(['R'])
    assert common == {}
    assert triple == {}
    assert list(double.keys()) == ['R']


def test_load_metrics(img):
    assert len(img.metrics.keys()) == len(globals.metric_groups['common']) + len(
        globals.metric_groups['pairwise']) - 2


def test_ds2df(img):
    df = img._ds2df()
    assert len(df.columns) == len(img.varnames) - 3  # minus lon, lat, gpi


def test_metric_df(img):
    df = img.metric_df(['R'])
    print(list(df.columns))
    assert list(df.columns) == [
        'R_between_0-ERA5_LAND_and_1-C3S_combined',
        'R_ci_lower_between_0-ERA5_LAND_and_1-C3S_combined',
        'R_ci_upper_between_0-ERA5_LAND_and_1-C3S_combined',
        'R_between_0-ERA5_LAND_and_2-SMOS_IC',
        'R_ci_lower_between_0-ERA5_LAND_and_2-SMOS_IC',
        'R_ci_upper_between_0-ERA5_LAND_and_2-SMOS_IC',
        globals.TEMPORAL_SUB_WINDOW_NC_COORD_NAME,
        'idx',
    ]


def test_metrics_in_file(img):
    """Test that all metrics are initialized correctly"""
    assert list(img.common.keys()) == globals.metric_groups['common']
    for m in img.double.keys():  # tau is not in the results
        assert m in globals.metric_groups['pairwise']
    assert list(img.triple.keys()) == []  # this is not the TC test case

    # with merged return value
    ms = img.metrics
    for m in ms:
        assert any([m in l for l in list(globals.metric_groups.values())])


def test_vars_in_file(img):
    """Test that all variables are initialized correctly"""
    vars = []
    for Var in img._iter_vars(type="metric"):
        vars.append(Var.varname)
    vars_should = ['n_obs']
    # since the valination is non-TC
    for metric in globals.metric_groups['pairwise']:
        vars_should.append(
            '{}_between_0-ERA5_LAND_and_1-C3S_combined'.format(metric))
        vars_should.append(
            '{}_between_0-ERA5_LAND_and_2-SMOS_IC'.format(metric))
    vars_should = np.sort(np.array(vars_should))
    vars = np.sort(
        np.array(vars + [
            'p_tau_between_0-ERA5_LAND_and_1-C3S_combined',
            'p_tau_between_0-ERA5_LAND_and_2-SMOS_IC',
            'tau_between_0-ERA5_LAND_and_1-C3S_combined',
            'tau_between_0-ERA5_LAND_and_2-SMOS_IC'
        ]))
    assert all(vars == vars_should)


def test_find_groups(img):
    """Test that all metrics for a specific group can be collected"""
    common_group = []
    for name, Metric in img.common.items():
        assert Metric.name in globals.metric_groups['common']
        assert len(Metric.variables) == 1
        common_group.append(name)
    double_group = []
    for name, Metric in img.double.items():

        assert Metric.name in globals.metric_groups['pairwise']
        if name in [
                'p_R', 'p_rho', 'RMSD', 'mse', 'mse_corr', 'mse_bias',
                'mse_var', 'RSS', 'status'
        ]:
            assert len(Metric.variables) == 2
        else:
            assert len(Metric.variables) == 6
        double_group.append(name)

    assert img.triple == {}


def test_variable_datasets(img):
    """Test the metadata associated with the ref dataset of the double group variables"""
    for Var in img._iter_vars(type="metric", filter_parms={'g': 2}):
        ref_ds, metric_ds, other_ds, _ = Var.get_varmeta()
        assert ref_ds[1]['short_name'] == 'ERA5_LAND'
        assert ref_ds[1]['pretty_name'] == 'ERA5-Land'
        assert other_ds is None


def test_ref_meta(img):
    """Test the metadata associated with the ref dataset of the image"""
    ref_meta = img.datasets.ref
    assert ref_meta['short_name'] == 'ERA5_LAND'
    assert ref_meta['pretty_name'] == 'ERA5-Land'
    assert ref_meta['short_version'] == 'ERA5_LAND_V20190904'
    assert ref_meta['pretty_version'] == 'v20190904'
    assert ref_meta['pretty_title'] == 'ERA5-Land (v20190904)'


def test_var_meta(img):
    """Test datasets associated with a specific variable"""
    for Var in img._iter_vars(type="metric",
                              filter_parms={
                                  'varname':
                                  'R_between_0-ERA5_LAND_and_1-C3S_combined'
                              }):
        ref_id, ref_meta = Var.ref_ds
        assert ref_id == 0
        assert ref_meta['short_name'] == 'ERA5_LAND'
        assert ref_meta['pretty_name'] == 'ERA5-Land'
        assert ref_meta['pretty_version'] == 'v20190904'

        metric_id, metric_meta = Var.metric_ds
        assert metric_id == 1
        assert metric_meta['short_name'] == 'C3S_combined'
        assert metric_meta['pretty_name'] == 'C3S SM combined'
        assert metric_meta['pretty_version'] == 'v202012'


def test_metric_stats(img):
    """Test the function metric_stats"""
    for name, Metric in img.metrics.items():
        stats = img._metric_stats(name)
        group = Metric.g
        if stats:  # empty variables return an empty list
            if group == 0:
                assert len(stats) == 1
            elif group == 2:
                assert len(stats) == 2


def test_stats_df(img):
    """Test the stats dataframe"""
    df = img.stats_df()
    empty_metrics = 0
    for name, Metric in img.metrics.items():
        stats = img._metric_stats(name)
        if not stats:  # find metrics without values
            if Metric.g == 1: # don't know what was meant here, g was defined as 0,2 or 3
                empty_metrics += 1
            elif Metric.g == 'pairwise':  # stats table has an entry for metric, for sat dataset (in common and triple metrics)
                empty_metrics += 2

    tot_stats = len(
        img.common.keys()) + 2 * len(img.double.keys()) - empty_metrics
    assert tot_stats == 27
    glob_stats = len(globals.metric_groups['common']) + 2 * len(
        globals.metric_groups['pairwise']) - empty_metrics
    assert glob_stats == 31

    # We drop the corr. significance statistics
    assert len(df.index) == tot_stats - 4
    assert len(df.index) == glob_stats - 8


def test_res_info(img):
    assert list(img.res_info.keys()) == ['value', 'units']
    assert list(img.res_info.values()) == [0.1, 'deg']


# ---- Test image where some variables are confidence intervals ----
def test_testfile(ci_img):
    someCIs = [
        "RMSD_ci_lower_between_0-ERA5_and_1-ESA_CCI_SM_combined",
        "RMSD_ci_upper_between_0-ERA5_and_1-ESA_CCI_SM_combined"
    ]
    for CI_varname in someCIs:
        assert CI_varname in ci_img.varnames


def test_cis(ci_img):
    assert ci_img.has_CIs


def test_ci_in_vars(ci_img):
    """Test that CI Variables are correctly assigned to a metric"""
    for CI_varname in ci_img._iter_vars(type="metric",
                                        filter_parms={
                                            "metric": "RMSD",
                                            "metric_ds":
                                            "2-ESA_CCI_SM_combined"
                                        }):
        assert CI_varname in [
            "RMSD_ci_lower_between_0-ERA5_and_2-ESA_CCI_SM_combined",
            "RMSD_ci_upper_between_0-ERA5_and_2-ESA_CCI_SM_combined"
        ]


# todo: test for img.metadata property (with updated file)
