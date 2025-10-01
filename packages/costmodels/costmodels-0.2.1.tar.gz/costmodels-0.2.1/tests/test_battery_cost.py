import jax
import numpy as np
import pytest

from costmodels.models import BatteryCostModel


def test_run_battery_model():
    battery_power = 27.0
    battery_energy = 108.0
    state_of_health = np.hstack(
        [
            -1.7e-6 * np.arange(1.8e5) + 1,
            -2.5e-6 * np.arange(25 * 365 * 24 - 1.8e5) + 1,
        ]
    ).ravel()
    bcm = BatteryCostModel()
    res = bcm.run(
        battery_power=battery_power,
        battery_energy=battery_energy,
        state_of_health=state_of_health,
    )
    np.testing.assert_allclose(res.capex, 10.162827279138453)
    np.testing.assert_allclose(res.opex, 0.0)


def test_gradient_battery_model():
    battery_energy = 108.0
    state_of_health = np.hstack(
        [
            -1.7e-6 * np.arange(1.8e5) + 1,
            -2.5e-6 * np.arange(25 * 365 * 24 - 1.8e5) + 1,
        ]
    ).ravel()
    bcm = BatteryCostModel()

    @jax.jit
    def wrapper(battery_power):
        res = bcm.run(
            battery_power=battery_power,
            battery_energy=battery_energy,
            state_of_health=state_of_health,
        )
        return res.capex + res.opex

    grad_value_func = jax.jit(jax.value_and_grad(wrapper))
    grad_value_func(1.0)


def test_trying_to_override_static_field():
    battery_energy = 108.0
    state_of_health = np.hstack(
        [
            -1.7e-6 * np.arange(1.8e5) + 1,
            -2.5e-6 * np.arange(25 * 365 * 24 - 1.8e5) + 1,
        ]
    ).ravel()
    bcm = BatteryCostModel(
        battery_power=27.0,
        battery_energy=battery_energy,
        state_of_health=state_of_health,
    )
    with pytest.raises(ValueError, match="Cannot override static field"):
        bcm.run(plant_lifetime=30.0)
