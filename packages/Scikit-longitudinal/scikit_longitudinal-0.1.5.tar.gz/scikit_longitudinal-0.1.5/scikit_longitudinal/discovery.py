# flake8: noqa: E126
# pylint: disable=C1802
import inspect
import pkgutil
from importlib import import_module
from operator import itemgetter
from pathlib import Path
from typing import Any, List, Tuple, Union

_MODULE_TO_IGNORE = {
    "tests",
    "externals",
    "setup",
    "conftest",
    "experimental",
    "estimator_checks",
    "sklearn_fork",
    "pipeline",
    "templates",
}


def all_scikit_longitudinal_estimators(type_filter: Union[str, List[str], None] = None) -> List[Tuple[str, Any]]:
    """Get a list of all estimators from `sklearn`.

    This function crawls the module and gets all classes that inherit
    from BaseEstimator. Classes that are defined in test-modules are not
    included.

    Parameters
    ----------
    type_filter : {"classifier", "regressor", "cluster", "transformer"} \
            or list of such str, default=None
        Which kind of estimators should be returned. If None, no filter is
        applied and all estimators are returned.  Possible values are
        'classifier', 'regressor', 'cluster' and 'transformer' to get
        estimators only of these specific types, or a list of these to
        get the estimators that fit at least one of the types.

    Returns
    -------
    estimators : list of tuples
        List of (name, class), where ``name`` is the class name as string
        and ``class`` is the actual type of the class.

    """
    # lazy import to avoid circular imports from sklearn.base
    from sklearn.base import BaseEstimator  # pylint: disable=C0415

    from .templates import (  # pylint: disable=C0415
        CustomClassifierMixinEstimator,
        CustomTransformerMixinEstimator,
        DataPreparationMixin,
    )

    def is_abstract(c):
        if not hasattr(c, "__abstractmethods__"):
            return False
        if not len(c.__abstractmethods__):
            return False
        return True

    all_classes = []
    root = str(Path(__file__).parent)  # sklearn package
    # Ignore deprecation warnings triggered at import time and from walking
    # packages
    for _, module_name, _ in pkgutil.walk_packages(path=[root], prefix="scikit_longitudinal."):
        module_parts = module_name.split(".")
        if any(part in _MODULE_TO_IGNORE for part in module_parts) or "._" in module_name:
            continue

        module = import_module(module_name)
        classes = inspect.getmembers(module, inspect.isclass)
        classes = [(name, est_cls) for name, est_cls in classes if not name.startswith("_")]

        all_classes.extend(classes)

    all_classes = set(all_classes)
    estimators = [
        c
        for c in all_classes
        if (
            (issubclass(c[1], CustomTransformerMixinEstimator) and c[0] != "CustomTransformerMixinEstimator")
            or (issubclass(c[1], CustomClassifierMixinEstimator) and c[0] != "CustomClassifierMixinEstimator")
            or (issubclass(c[1], DataPreparationMixin) and c[0] != "DataPreparationMixin")
            or (
                issubclass(c[1], BaseEstimator)
                and c[0]
                in [
                    "LexicoGradientBoostingClassifier",
                    "LexicoRandomForestClassifier",
                    "LexicoDecisionTreeClassifier",
                    "LexicoDecisionTreeRegressor",
                    "LexicoDeepForestClassifier",
                ]
            )
        )
    ]
    # get rid of abstract base classes
    estimators = [c for c in estimators if not is_abstract(c[1])]

    if type_filter is not None:
        if not isinstance(type_filter, list):
            type_filter = [type_filter]
        else:
            type_filter = list(type_filter)  # copy
        filtered_estimators = []
        filters = {
            "classifier": CustomClassifierMixinEstimator,
            "transformer": CustomTransformerMixinEstimator,
            "data_preparation": DataPreparationMixin,
        }
        for name, mixin in filters.items():
            if name in type_filter:
                type_filter.remove(name)
                if name == "classifier":
                    filtered_estimators.extend(
                        [
                            est
                            for est in estimators
                            if (
                                issubclass(est[1], mixin)
                                or (
                                    issubclass(est[1], BaseEstimator)
                                    and est[0]
                                    in [
                                        "LexicoGradientBoostingClassifier",
                                        "LexicoRandomForestClassifier",
                                        "LexicoDecisionTreeClassifier",
                                        "LexicoDecisionTreeRegressor",
                                        "LexicoDeepForestClassifier",
                                    ]
                                )
                            )
                        ]
                    )
                else:
                    filtered_estimators.extend([est for est in estimators if issubclass(est[1], mixin)])
        estimators = filtered_estimators
        if type_filter:
            raise ValueError(
                "Parameter type_filter must be 'classifier', "
                "'transformer', 'data_preparation' or "
                "None, got"
                f" {repr(type_filter)}."
            )

    # drop duplicates, sort for reproducibility
    # itemgetter is used to ensure the sort does not extend to the 2nd item of
    # the tuple
    return sorted(set(estimators), key=itemgetter(0))
