"""Tests for making sure experimental imports work as expected."""

import textwrap

import pytest

from sklearn_dual.utils._testing import assert_run_python_script_without_output
from sklearn_dual.utils.fixes import _IS_WASM


@pytest.mark.xfail(_IS_WASM, reason="cannot start subprocess")
def test_imports_strategies():
    # Make sure different import strategies work or fail as expected.

    # Since Python caches the imported modules, we need to run a child process
    # for every test case. Else, the tests would not be independent
    # (manually removing the imports from the cache (sys.modules) is not
    # recommended and can lead to many complications).
    pattern = "IterativeImputer is experimental"
    good_import = """
    from sklearn_dual.experimental import enable_iterative_imputer
    from sklearn_dual.impute import IterativeImputer
    """
    assert_run_python_script_without_output(
        textwrap.dedent(good_import), pattern=pattern
    )

    good_import_with_ensemble_first = """
    import sklearn_dual.ensemble
    from sklearn_dual.experimental import enable_iterative_imputer
    from sklearn_dual.impute import IterativeImputer
    """
    assert_run_python_script_without_output(
        textwrap.dedent(good_import_with_ensemble_first),
        pattern=pattern,
    )

    bad_imports = f"""
    import pytest

    with pytest.raises(ImportError, match={pattern!r}):
        from sklearn_dual.impute import IterativeImputer

    import sklearn_dual.experimental
    with pytest.raises(ImportError, match={pattern!r}):
        from sklearn_dual.impute import IterativeImputer
    """
    assert_run_python_script_without_output(
        textwrap.dedent(bad_imports),
        pattern=pattern,
    )
