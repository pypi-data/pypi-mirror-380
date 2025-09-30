import random

import pytest

from ncca.ngl import Random


def test_vec2():
    Random.set_seed()
    v = Random.get_random_vec2()
    assert -1.0 <= v.x <= 1.0
    assert -1.0 <= v.y <= 1.0


def test_vec3():
    Random.set_seed()
    v = Random.get_random_vec3()
    assert -1.0 <= v.x <= 1.0
    assert -1.0 <= v.y <= 1.0
    assert -1.0 <= v.z <= 1.0


def test_point():
    Random.set_seed()
    v = Random.get_random_point(20, 20, 20)
    assert -20.0 <= v.x <= 20.0
    assert -20.0 <= v.y <= 20.0
    assert -20.0 <= v.z <= 20.0


def test_vec4():
    Random.set_seed()
    v = Random.get_random_vec4()
    assert -1.0 <= v.x <= 1.0
    assert -1.0 <= v.y <= 1.0
    assert -1.0 <= v.z <= 1.0
    # In the C++ version, w is 0.0, but the test checks for -1.0 to 1.0
    # The python version sets w to 0.0 so this will pass.
    assert -1.0 <= v.w <= 1.0


def test_random_number_default():
    Random.set_seed()
    v = Random.random_number()
    assert -1.0 <= v <= 1.0


def test_random_number_param():
    Random.set_seed()
    v = Random.random_number(2000.0)
    assert -2000.0 <= v <= 2000.0


def test_random_positive_number_default():
    Random.set_seed()
    v = Random.random_positive_number()
    assert 0.0 <= v <= 1.0


def test_random_positive_number_param():
    Random.set_seed()
    v = Random.random_positive_number(2000.0)
    assert 0.0 <= v <= 2000.0


def test_add_int_generator():
    Random.set_seed()
    Random.add_int_generator("test", lambda: random.randint(-100, 100))
    test = Random.get_int_from_generator_name("test")
    assert -100 <= test <= 100


def test_add_float_generator():
    Random.set_seed()
    Random.add_float_generator("test", lambda: random.uniform(0.0, 5.0))
    test = Random.get_float_from_generator_name("test")
    assert 0.0 <= test <= 5.0


def test_set_seed_value():
    Random.set_seed_value(42)
    val1 = Random.random_number()
    Random.set_seed_value(42)
    val2 = Random.random_number()
    assert val1 == val2


def test_get_float_from_generator_name_not_found():
    assert Random.get_float_from_generator_name("not_found") == pytest.approx(0.0)


def test_get_int_from_generator_name_not_found():
    assert Random.get_int_from_generator_name("not_found") == pytest.approx(0)


def test_get_random_colour3():
    v = Random.get_random_colour3()
    assert 0.0 <= v.x <= 1.0
    assert 0.0 <= v.y <= 1.0
    assert 0.0 <= v.z <= 1.0


def test_get_random_normalized_vec4():
    v = Random.get_random_normalized_vec4()
    assert v.length() == pytest.approx(1.0)


def test_get_random_normalized_vec2():
    v = Random.get_random_normalized_vec2()
    assert v.length() == pytest.approx(1.0)


def test_get_random_point_defaults():
    v = Random.get_random_point()
    assert -1.0 <= v.x <= 1.0
    assert -1.0 <= v.y <= 1.0
    assert -1.0 <= v.z <= 1.0


def test_get_random_colour4():
    v = Random.get_random_colour4()
    assert 0.0 <= v.x <= 1.0
    assert 0.0 <= v.y <= 1.0
    assert 0.0 <= v.z <= 1.0
    assert v.w == 1.0


def test_get_random_normalized_vec3():
    v = Random.get_random_normalized_vec3()
    assert v.length() == pytest.approx(1.0)
