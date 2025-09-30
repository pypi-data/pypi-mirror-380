import pickle

import numpy as np

from psr import ParametricSR, config


def test_psr():

    n_feat = 5
    X = np.abs(np.random.random((100, n_feat)))
    y = (
        3 * X[:, 0]
        + 0.5 * X[:, 1] ** 2
        + 2 * X[:, 2]
        + np.abs(np.random.normal(0, 0.1, size=100))
        + 1e-5
    )

    psr_model = ParametricSR(
        random_state=42,
        n_gen=3,
        n_per_gen=10,
        n_elite=3,
        n_survivor=3,
        n_jobs=2,
        optimize_with="curve_fit",
        curve_fit_y_scaling=None,
        minimize_scoring="rmse",
        scoring="rmse",
        filter_func=4,
        penalty_func=0.003,
        n_gen_no_change=2,
        verbose=0,
    )

    psr_model.fit(X, y)
    y_pred = psr_model.predict(X, refit=False)

    assert hasattr(psr_model, "best_estimator_"), "Model has not been fitted"

    psr_model_serialized = pickle.dumps(psr_model)

    with config.inplace_update():
        psr_model_deserialized = pickle.loads(psr_model_serialized)
    assert hasattr(psr_model_deserialized, "best_estimator_"), "Serialization failed"

    seed_expressions = (["add", "add", "X2", 1, "C1"], ["add", "add", "X2", 0.5, "C1"])
    psr_model.add_seeds(seeds=seed_expressions, init=True, apply_filter=False)
    psr_model.fit([X] * 3, [y] * 3, batch_weight=[0.2, 0.3, 0.5])
    assert hasattr(psr_model, "best_estimator_"), "Model has not been fitted"
    psr_model_serialized = pickle.dumps(psr_model)

    assert len(psr_model._trackers[0]) == len(
        seed_expressions
    ), "Seed expressions not added properly"
    assert len(psr_model._raw_scores[0]) == len(
        seed_expressions
    ), "Seed expressions not scored properly"
    assert len(psr_model._fitness_scores[0]) == len(
        seed_expressions
    ), "Seed expressions not evaluated properly"

    with config.inplace_update():
        psr_model_deserialized = pickle.loads(psr_model_serialized)
    assert hasattr(psr_model_deserialized, "best_estimator_"), "Serialization failed"
