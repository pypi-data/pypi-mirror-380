from multiprocessing import Pool, cpu_count
import warnings

import numpy as np
from numpy.typing import NDArray

from psr import Expression, ExpressionBuilder, config

from tests.test_utils import Add, Sub, Mul, X1, X2, C1, One


def test_expression_basics():
    # Create Expression nodes - always use a copy of the function units
    add1: Expression[NDArray] = Expression(Add.copy())
    add2: Expression[NDArray] = Expression(Add.copy())
    x1: Expression[NDArray] = Expression(X1.copy())
    x2: Expression[NDArray] = Expression(X2.copy())
    c1: Expression[NDArray] = Expression(C1.copy())
    one: Expression[NDArray] = Expression(One.copy())

    # Build the expression tree
    # add1: (X2 + 1) + C1
    add1.add_child(add2, validate=False)
    add1.add_child(c1, validate=False)
    add2.add_child(x2, validate=False)
    add2.add_child(one, validate=False)

    # Refresh the expression - this will check the structure and update any necessary indices
    add1.refresh()

    # Test the format method
    formatted_expression = add1.format()
    assert formatted_expression == "(X2 + 1) + C1", "Expression format is incorrect"

    # Test the evaluation of the expression
    X = np.array([[1, 2], [3, 4], [5, 6]])
    C = np.array([-5, 10])
    result = add1(X, C)
    assert np.allclose(result, [-2, 0, 2]), "Expression evaluation is incorrect"

    # Test the fitting process
    answer = 3.14159
    X = np.random.random((10, 2))
    y = X[:, 1] + answer + 1
    _, fit_result = add1.fit(X, y, return_result=True)
    assert fit_result is not None, "Fitting should return a result"
    if isinstance(fit_result, tuple):
        assert np.isclose(answer, fit_result[0][0]), "Fitting result is incorrect"
    else:
        assert np.isclose(answer, fit_result.x[0]), "Fitting result is incorrect"

    # check visualization - this should run successfully
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=DeprecationWarning)
        add1.visualize()


def test_expression_import_export():

    # create "(X2 + 1) + C1"
    lst = ["add", "add", "X2", 1, "C_s1"]
    expression_1 = Expression.import_list(lst.copy())
    assert isinstance(
        expression_1, Expression
    ), "Import should return an Expression object"

    # check if the imported expression is correct
    answer = 3.14159  # should be within (-5, 5)
    X = np.random.random((10, 2))
    y = X[:, 1] + answer + 1
    assert np.allclose(
        y, expression_1(X, C=[answer, 0.0])
    ), "Imported expression is arithmetically incorrect"

    lst_export = expression_1.export_list()
    assert lst == lst_export, f"Exported list does not match the original: {lst_export}"

    expression_2 = Expression.import_list(lst_export)
    assert (
        expression_1 == expression_2 and expression_1 is not expression_2
    ), "Imported expression should be equal but not the same object"


def expression_evolution(random_state: int = 42):
    min_height, max_height = 0, 4
    builder = ExpressionBuilder(min_height=min_height, max_height=max_height)
    builder.psr_collection.variables.express_add(5)

    tracker_1 = builder.init("full", random_state=random_state, return_tracker=True)
    expression_1 = tracker_1.to_expression()
    assert (
        expression_1.height == max_height
    ), f"Expected height {max_height}, got {expression_1.height}"
    assert tracker_1.how == "init-full", "Expected init method 'init-full'"

    tracker_2 = builder.init("balanced", random_state=random_state, return_tracker=True)
    expression_2 = tracker_2.to_expression()
    assert (
        expression_2.height == max_height
    ), f"Expected height {max_height}, got {expression_2.height}"
    assert tracker_2.how == "init-balanced", "Expected init method 'init-balanced'"

    tracker_3 = builder.init("full", random_state=random_state, return_tracker=True)
    expression_3 = tracker_3.to_expression()
    assert (
        expression_1 == expression_3
    ), "Expected the same expression from init with same random state"

    tracker_4 = builder.crossover(
        expression_1, expression_2, random_state=random_state, return_tracker=True
    )
    expression_4 = tracker_4.to_expression()
    assert (
        min_height <= expression_4.height <= max_height
    ), f"Expected height between {min_height} and {max_height}, got {expression_4.height}"
    assert tracker_4.how == "crossover", "Expected crossover method"

    tracker_5 = builder.mutation_subtree(
        expression_1, random_state=random_state, return_tracker=True, how="test"
    )
    expression_5 = tracker_5.to_expression()
    assert (
        min_height <= expression_5.height <= max_height
    ), f"Expected height between {min_height} and {max_height}, got {expression_5.height}"
    assert tracker_5.how == "test", "Expected mutation method 'test'"

    tracker_6 = builder.mutation_hoist(
        expression_1, random_state=random_state, return_tracker=True
    )
    expression_6 = tracker_6.to_expression()
    assert (
        tracker_6.how == "mutation-hoist"
    ), "Expected mutation method 'mutation-hoist'"

    tracker_7 = builder.mutation_point(
        expression_1, random_state=random_state, return_tracker=True
    )
    expression_7 = tracker_7.to_expression()
    assert (
        min_height <= expression_7.height <= max_height
    ), f"Expected height between {min_height} and {max_height}, got {expression_7.height}"
    assert (
        tracker_7.how == "mutation-point"
    ), "Expected mutation method 'mutation-point'"

    tracker_8 = builder.crossover_mutation(
        expression_1,
        expression_2,
        "point",
        random_state=random_state,
        return_tracker=True,
    )
    expression_8 = tracker_8.to_expression()
    assert (
        min_height <= expression_8.height <= max_height
    ), f"Expected height between {min_height} and {max_height}, got {expression_8.height}"
    assert tracker_8.how == (
        "crossover",
        "mutation-point",
    ), "Expected tracker method ('crossover', 'mutation-point')"

    tracker_9 = builder.crossover_mutation(
        expression_1,
        expression_2,
        random_state=random_state,
        return_tracker=True,
    )
    expression_9 = tracker_9.to_expression()
    assert (
        min_height <= expression_9.height <= max_height
    ), f"Expected height between {min_height} and {max_height}, got {expression_9.height}"
    assert (
        isinstance(tracker_9.how, tuple)
        and tracker_9.how[0] == "crossover"
        and tracker_9.how[1].startswith("mutation-")
    ), "Expected tracker method ('crossover', 'mutation-***')"

    tracker_10 = builder.build_once()
    assert isinstance(tracker_10.how, str) and tracker_10.how.startswith(
        "init-"
    ), "Expected tracker method to start with 'init-'"

    tracker_11 = builder.build_once(src=[expression_1, tracker_7, expression_9])
    assert not (
        isinstance(tracker_11.how, str) and tracker_11.how.startswith("init-")
    ), "Expected tracker method to be non-init"

    return tracker_11


def test_expression_evolution(random_state: int = 42):
    expression_evolution(random_state=random_state)


def test_expression_evolution_parallel():

    min_height, max_height = 0, 4
    builder = ExpressionBuilder(min_height=min_height, max_height=max_height)
    builder.psr_collection.variables.express_add(5)

    random_states = [42, 3417]
    with config.multiprocessing(), Pool(processes=min(2, cpu_count())) as pool:
        results = pool.map(test_expression_evolution, random_states)


if __name__ == "__main__":
    test_expression_basics()
    test_expression_import_export()
    test_expression_evolution()
    test_expression_evolution_parallel()
