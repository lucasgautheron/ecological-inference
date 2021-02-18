"""Test plot utils."""
import pytest
import numpy as np

from pyei import data
from pyei.plot_utils import *  # pylint:disable=wildcard-import,unused-wildcard-import
from pyei.two_by_two import TwoByTwoEI


@pytest.fixture(scope="session")
def example_two_by_two_data():
    """"""
    sc_data = data.Datasets.Santa_Clara.to_dataframe()
    group_fractions = np.array(sc_data["pct_e_asian_vote"])
    T = np.array(sc_data["pct_for_hardy2"])
    N = np.array(sc_data["total2"])
    demographic_group_name = "e_asian"
    candidate_name = "Hardy"
    precinct_names = sc_data["precinct"]
    return {
        "group_fractions": group_fractions,
        "votes_fractions": votes_fractions,
        "precint_pops": precint_pops,
        "demographic_group_name": demographic_group_name,
        "candidate_name": candidate_name,
        "precinct_names": precinct_names,
    }


@pytest.fixture(scope="session")
def example_two_by_two_ei(example_two_by_two_data): # pylint: disable=redefined-outer-name
    """"""
    ei_ex = TwoByTwoEI(model_name="king99_pareto_modification", pareto_scale=8, pareto_shape=2)
    ei_ex.fit(
        example_two_by_two_data["group_fractions"],
        example_two_by_two_data["votes_fractions"],
        example_two_by_two_data["precint_pops"],
        demographic_group_name=example_two_by_two_data["demographic_group_name"],
        candidate_name=example_two_by_two_data["candidate_name"],
        precinct_names=example_two_by_two_data["precinct_names"],
    )
    return ei_ex


def test_tomography_plot(example_two_by_two_data):
    tomography_plot(
        example_two_by_two_data["group_fractions"],
        example_two_by_two_data["votes_fractions"],
        example_two_by_two_data["demographic_group_name"],
        example_two_by_two_data["candidate_name"],
    )


def test_ei_plot_and_plot_summary(example_two_by_two_ei): # pylint: disable=redefined-outer-name
    # TODO: maybe uncouple this to test the plot utils piece alone
    axes = example_two_by_two_ei.plot()
    assert len(axes) == 2  ## one axis each for boxplot and kde


def test_ei_plot_kdes(example_two_by_two_ei): # pylint: disable=redefined-outer-name
    # TODO: maybe uncouple this to test the plot utils piece alone
    ax = example_two_by_two_ei.plot_kde()
    assert ax is not None


def test_ei_plot_boxplot(example_two_by_two_ei): # pylint: disable=redefined-outer-name
    # TODO: maybe uncouple this to test the plot utils piece alone
    ax = example_two_by_two_ei.plot_boxplot()
    assert ax is not None


def test_ei_plot_intervals(example_two_by_two_ei): # pylint: disable=redefined-outer-name
    # TODO: maybe uncouple this to test the plot utils piece alone
    ax = example_two_by_two_ei.plot_intervals()
    assert ax is not None


def test_ei_precinct_level_plots(example_two_by_two_ei):# pylint: disable=redefined-outer-name
    # TODO: maybe uncouple this to test the plot utils piece alone
    ax = example_two_by_two_ei.precinct_level_plot()
    assert ax is not None


def test_ei_plot_intervals_by_precinct(example_two_by_two_ei): # pylint: disable=redefined-outer-name
    # TODO: maybe uncouple this to test the plot utils piece alone
    ax = example_two_by_two_ei.plot_intervals_by_precinct()
    assert ax is not None
