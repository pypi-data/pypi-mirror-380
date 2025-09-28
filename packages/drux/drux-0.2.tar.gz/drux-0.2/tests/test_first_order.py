"""Tests for the first-order model implementation in drux package."""

from pytest import raises
from numpy import isclose
from re import escape
from math import exp
from drux import FirstOrderModel

TEST_CASE_NAME = "first-order model tests"
M0, k = 0.1, 0.003
SIM_DURATION, SIM_TIME_STEP = 1000, 10
RELATIVE_TOLERANCE = 1e-1


def test_first_order_parameters():
    model = FirstOrderModel(M0=M0, k=k)
    assert model._parameters.M0 == M0
    assert model._parameters.k == k


def test_invalid_parameters():
    with raises(ValueError, match=escape("Entire releasable amount of drug (M0) must be non-negative.")):
        FirstOrderModel(M0=-M0, k=k).simulate(duration=SIM_DURATION, time_step=SIM_TIME_STEP)

    with raises(ValueError, match=escape("Release rate (k) must be non-negative.")):
        FirstOrderModel(M0=M0, k=-k).simulate(duration=SIM_DURATION, time_step=SIM_TIME_STEP)


def test_first_order_simulation():  # Reference: https://europepmc.org/article/pmc/3425064
    model = FirstOrderModel(M0=M0, k=k)
    profile = model.simulate(duration=SIM_DURATION, time_step=SIM_TIME_STEP)
    actual_release = [M0 * (1 - exp(-k * t)) for t in range(0, 1001, 10)]
    assert all(isclose(p, a, rtol=RELATIVE_TOLERANCE) for p, a in zip(profile, actual_release))


def test_first_order_simulation_errors():
    model = FirstOrderModel(M0=M0, k=k)

    with raises(ValueError, match="Duration and time step must be positive values"):
        model.simulate(duration=-100, time_step=10)

    with raises(ValueError, match="Duration and time step must be positive values"):
        model.simulate(duration=100, time_step=-10)

    with raises(ValueError, match="Time step cannot be greater than duration"):
        model.simulate(duration=10, time_step=20)


def test_first_order_plot1():
    model = FirstOrderModel(M0=M0, k=k)
    model.simulate(duration=SIM_DURATION, time_step=SIM_TIME_STEP)
    fig, ax = model.plot()
    assert fig is not None
    assert ax is not None
    assert ax.get_title() == model._plot_parameters["title"]
    assert ax.get_xlabel() == model._plot_parameters["xlabel"]
    assert ax.get_ylabel() == model._plot_parameters["ylabel"]
    assert [text.get_text() for text in ax.get_legend().get_texts()] == [model._plot_parameters["label"]]


def test_first_order_plot2():
    model = FirstOrderModel(M0=M0, k=k)
    model.simulate(duration=SIM_DURATION, time_step=SIM_TIME_STEP)
    fig, ax = model.plot(title="test-title", xlabel="test-xlabel", ylabel="test-ylabel", label="test-label")
    assert fig is not None
    assert ax is not None
    assert ax.get_title() == "test-title"
    assert ax.get_xlabel() == "test-xlabel"
    assert ax.get_ylabel() == "test-ylabel"
    assert [text.get_text() for text in ax.get_legend().get_texts()] == ["test-label"]


def test_first_order_plot_error():
    model = FirstOrderModel(M0=M0, k=k)

    with raises(ValueError, match=escape("No simulation data available. Run simulate() first.")):
        model.plot()

    model._time_points = [0]  # manually set time points to simulate error (TODO: it will be caught with prior errors)
    # manually set a too short profile to simulate error (TODO: it will be caught with prior errors)
    model._release_profile = [0.0]
    with raises(ValueError, match="Release profile is too short to calculate release rate."):
        model.plot()


def test_first_order_release_rate():  # Reference: https://www.wolframalpha.com/input?i=get+the+derivative+of+M0*exp%28-k*t%29+with+respect+to+t
    model = FirstOrderModel(M0=M0, k=k)
    model.simulate(duration=SIM_DURATION, time_step=SIM_TIME_STEP)
    rate = model.get_release_rate()
    actual_rate = [k * M0 * exp(-k * t) for t in range(0, 1001, 10)]
    assert all(isclose(r, a, rtol=1e-1) for r, a in zip(rate, actual_rate))


def test_first_order_release_rate_error():
    model = FirstOrderModel(M0=M0, k=k)

    with raises(ValueError, match=escape("No simulation data available. Run simulate() first.")):
        model.get_release_rate()

    model._time_points = [0]  # manually set time points to simulate error (TODO: it will be caught with prior errors)
    # manually set a too short profile to simulate error (TODO: it will be caught with prior errors)
    model._release_profile = [0.0]
    with raises(ValueError, match="Release profile is too short to calculate release rate."):
        model.get_release_rate()


def test_first_order_time_for_release():  # Reference: https://www.wolframalpha.com/input?i=solve+for+t+in+0.1+*+%281+-+exp%28-0.003*t%29%29+%3D+0.5*+0.1+*+%281-+exp%28-0.003*1000%29%29
    model = FirstOrderModel(M0=M0, k=k)
    model.simulate(duration=SIM_DURATION, time_step=SIM_TIME_STEP)
    tx = model.time_for_release(0.5 * model._release_profile[-1])
    assert isclose(tx, 220, rtol=1e-2)


def test_first_order_time_for_release_error():
    model = FirstOrderModel(M0=M0, k=k)

    with raises(ValueError, match=escape("No simulation data available. Run simulate() first.")):
        model.time_for_release(0.5)
    model.simulate(duration=SIM_DURATION, time_step=SIM_TIME_STEP)

    with raises(ValueError, match="Target release must be non-negative."):
        model.time_for_release(-0.1)

    with raises(ValueError, match="Target release exceeds maximum release of the simulated duration."):
        model.time_for_release(model._release_profile[-1] + 0.1)
