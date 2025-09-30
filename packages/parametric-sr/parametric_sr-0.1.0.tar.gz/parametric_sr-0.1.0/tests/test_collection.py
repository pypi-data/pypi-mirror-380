import pytest

from psr import FuncUnit, PSRCollection


def test_collection():
    psr_collection = PSRCollection()

    with pytest.raises(ValueError):
        psr_collection.variables.select()

    psr_collection.variables.express_add(5)

    a = psr_collection.select(42)[1]
    b = psr_collection.select(42)[1]
    assert a == b, "Selections with the same seed should be identical"

    a = psr_collection.select(42, size=10)[1]
    assert len(a) == 10, "Select should return the specified number of choices"

    choice_1 = psr_collection.iselect(42)
    assert isinstance(choice_1, FuncUnit), "Selected item should be a FuncUnit"

    choice_2 = psr_collection.iselect(42)
    assert choice_1 == choice_2, "Selections with the same seed should be identical"

    if choice_1.is_immutable:
        assert (
            choice_1 is choice_2
        ), "Immutable selections should return the same instance"
    else:
        assert (
            choice_1 is not choice_2
        ), "Mutable selections should return new instances (copies)"

    # repeat again to reduce random success probability
    choice_3 = psr_collection.iselect(42)
    assert choice_1 == choice_3, "Selections with the same seed should be identical"

    n = 10
    choices_4 = psr_collection.pselect(42, size=n)
    assert len(choices_4) == n, "pselect should return the specified number of choices"
    assert all(
        choice.arity > 0 for choice in choices_4
    ), "pselect should return `FuncUnit` with arity > 0"

    choices_5 = psr_collection.nselect(42, size=n)
    assert all(
        choice.arity == 0 for choice in choices_5
    ), "nselect should return `FuncUnit` with arity == 0"
