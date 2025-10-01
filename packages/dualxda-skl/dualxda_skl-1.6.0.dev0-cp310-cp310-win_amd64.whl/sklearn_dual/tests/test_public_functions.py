from importlib import import_module
from inspect import signature
from numbers import Integral, Real

import pytest

from sklearn_dual.utils._param_validation import (
    Interval,
    InvalidParameterError,
    generate_invalid_param_val,
    generate_valid_param,
    make_constraint,
)


def _get_func_info(func_module):
    module_name, func_name = func_module.rsplit(".", 1)
    module = import_module(module_name)
    func = getattr(module, func_name)

    func_sig = signature(func)
    func_params = [
        p.name
        for p in func_sig.parameters.values()
        if p.kind not in (p.VAR_POSITIONAL, p.VAR_KEYWORD)
    ]

    # The parameters `*args` and `**kwargs` are ignored since we cannot generate
    # constraints.
    required_params = [
        p.name
        for p in func_sig.parameters.values()
        if p.default is p.empty and p.kind not in (p.VAR_POSITIONAL, p.VAR_KEYWORD)
    ]

    return func, func_name, func_params, required_params


def _check_function_param_validation(
    func, func_name, func_params, required_params, parameter_constraints
):
    """Check that an informative error is raised when the value of a parameter does not
    have an appropriate type or value.
    """
    # generate valid values for the required parameters
    valid_required_params = {}
    for param_name in required_params:
        if parameter_constraints[param_name] == "no_validation":
            valid_required_params[param_name] = 1
        else:
            valid_required_params[param_name] = generate_valid_param(
                make_constraint(parameter_constraints[param_name][0])
            )

    # check that there is a constraint for each parameter
    if func_params:
        validation_params = parameter_constraints.keys()
        unexpected_params = set(validation_params) - set(func_params)
        missing_params = set(func_params) - set(validation_params)
        err_msg = (
            "Mismatch between _parameter_constraints and the parameters of"
            f" {func_name}.\nConsider the unexpected parameters {unexpected_params} and"
            f" expected but missing parameters {missing_params}\n"
        )
        assert set(validation_params) == set(func_params), err_msg

    # this object does not have a valid type for sure for all params
    param_with_bad_type = type("BadType", (), {})()

    for param_name in func_params:
        constraints = parameter_constraints[param_name]

        if constraints == "no_validation":
            # This parameter is not validated
            continue

        # Mixing an interval of reals and an interval of integers must be avoided.
        if any(
            isinstance(constraint, Interval) and constraint.type == Integral
            for constraint in constraints
        ) and any(
            isinstance(constraint, Interval) and constraint.type == Real
            for constraint in constraints
        ):
            raise ValueError(
                f"The constraint for parameter {param_name} of {func_name} can't have a"
                " mix of intervals of Integral and Real types. Use the type"
                " RealNotInt instead of Real."
            )

        match = (
            rf"The '{param_name}' parameter of {func_name} must be .* Got .* instead."
        )

        err_msg = (
            f"{func_name} does not raise an informative error message when the "
            f"parameter {param_name} does not have a valid type. If any Python type "
            "is valid, the constraint should be 'no_validation'."
        )

        # First, check that the error is raised if param doesn't match any valid type.
        with pytest.raises(InvalidParameterError, match=match):
            func(**{**valid_required_params, param_name: param_with_bad_type})
            pytest.fail(err_msg)

        # Then, for constraints that are more than a type constraint, check that the
        # error is raised if param does match a valid type but does not match any valid
        # value for this type.
        constraints = [make_constraint(constraint) for constraint in constraints]

        for constraint in constraints:
            try:
                bad_value = generate_invalid_param_val(constraint)
            except NotImplementedError:
                continue

            err_msg = (
                f"{func_name} does not raise an informative error message when the "
                f"parameter {param_name} does not have a valid value.\n"
                "Constraints should be disjoint. For instance "
                "[StrOptions({'a_string'}), str] is not a acceptable set of "
                "constraint because generating an invalid string for the first "
                "constraint will always produce a valid string for the second "
                "constraint."
            )

            with pytest.raises(InvalidParameterError, match=match):
                func(**{**valid_required_params, param_name: bad_value})
                pytest.fail(err_msg)


PARAM_VALIDATION_FUNCTION_LIST = [
    "sklearn_dual.calibration.calibration_curve",
    "sklearn_dual.cluster.cluster_optics_dbscan",
    "sklearn_dual.cluster.compute_optics_graph",
    "sklearn_dual.cluster.estimate_bandwidth",
    "sklearn_dual.cluster.kmeans_plusplus",
    "sklearn_dual.cluster.cluster_optics_xi",
    "sklearn_dual.cluster.ward_tree",
    "sklearn_dual.covariance.empirical_covariance",
    "sklearn_dual.covariance.ledoit_wolf_shrinkage",
    "sklearn_dual.covariance.log_likelihood",
    "sklearn_dual.covariance.shrunk_covariance",
    "sklearn_dual.datasets.clear_data_home",
    "sklearn_dual.datasets.dump_svmlight_file",
    "sklearn_dual.datasets.fetch_20newsgroups",
    "sklearn_dual.datasets.fetch_20newsgroups_vectorized",
    "sklearn_dual.datasets.fetch_california_housing",
    "sklearn_dual.datasets.fetch_covtype",
    "sklearn_dual.datasets.fetch_kddcup99",
    "sklearn_dual.datasets.fetch_lfw_pairs",
    "sklearn_dual.datasets.fetch_lfw_people",
    "sklearn_dual.datasets.fetch_olivetti_faces",
    "sklearn_dual.datasets.fetch_rcv1",
    "sklearn_dual.datasets.fetch_openml",
    "sklearn_dual.datasets.fetch_species_distributions",
    "sklearn_dual.datasets.get_data_home",
    "sklearn_dual.datasets.load_breast_cancer",
    "sklearn_dual.datasets.load_diabetes",
    "sklearn_dual.datasets.load_digits",
    "sklearn_dual.datasets.load_files",
    "sklearn_dual.datasets.load_iris",
    "sklearn_dual.datasets.load_linnerud",
    "sklearn_dual.datasets.load_sample_image",
    "sklearn_dual.datasets.load_svmlight_file",
    "sklearn_dual.datasets.load_svmlight_files",
    "sklearn_dual.datasets.load_wine",
    "sklearn_dual.datasets.make_biclusters",
    "sklearn_dual.datasets.make_blobs",
    "sklearn_dual.datasets.make_checkerboard",
    "sklearn_dual.datasets.make_circles",
    "sklearn_dual.datasets.make_classification",
    "sklearn_dual.datasets.make_friedman1",
    "sklearn_dual.datasets.make_friedman2",
    "sklearn_dual.datasets.make_friedman3",
    "sklearn_dual.datasets.make_gaussian_quantiles",
    "sklearn_dual.datasets.make_hastie_10_2",
    "sklearn_dual.datasets.make_low_rank_matrix",
    "sklearn_dual.datasets.make_moons",
    "sklearn_dual.datasets.make_multilabel_classification",
    "sklearn_dual.datasets.make_regression",
    "sklearn_dual.datasets.make_s_curve",
    "sklearn_dual.datasets.make_sparse_coded_signal",
    "sklearn_dual.datasets.make_sparse_spd_matrix",
    "sklearn_dual.datasets.make_sparse_uncorrelated",
    "sklearn_dual.datasets.make_spd_matrix",
    "sklearn_dual.datasets.make_swiss_roll",
    "sklearn_dual.decomposition.sparse_encode",
    "sklearn_dual.feature_extraction.grid_to_graph",
    "sklearn_dual.feature_extraction.img_to_graph",
    "sklearn_dual.feature_extraction.image.extract_patches_2d",
    "sklearn_dual.feature_extraction.image.reconstruct_from_patches_2d",
    "sklearn_dual.feature_selection.chi2",
    "sklearn_dual.feature_selection.f_classif",
    "sklearn_dual.feature_selection.f_regression",
    "sklearn_dual.feature_selection.mutual_info_classif",
    "sklearn_dual.feature_selection.mutual_info_regression",
    "sklearn_dual.feature_selection.r_regression",
    "sklearn_dual.inspection.partial_dependence",
    "sklearn_dual.inspection.permutation_importance",
    "sklearn_dual.isotonic.check_increasing",
    "sklearn_dual.isotonic.isotonic_regression",
    "sklearn_dual.linear_model.enet_path",
    "sklearn_dual.linear_model.lars_path",
    "sklearn_dual.linear_model.lars_path_gram",
    "sklearn_dual.linear_model.lasso_path",
    "sklearn_dual.linear_model.orthogonal_mp",
    "sklearn_dual.linear_model.orthogonal_mp_gram",
    "sklearn_dual.linear_model.ridge_regression",
    "sklearn_dual.manifold.locally_linear_embedding",
    "sklearn_dual.manifold.smacof",
    "sklearn_dual.manifold.spectral_embedding",
    "sklearn_dual.manifold.trustworthiness",
    "sklearn_dual.metrics.accuracy_score",
    "sklearn_dual.metrics.auc",
    "sklearn_dual.metrics.average_precision_score",
    "sklearn_dual.metrics.balanced_accuracy_score",
    "sklearn_dual.metrics.brier_score_loss",
    "sklearn_dual.metrics.calinski_harabasz_score",
    "sklearn_dual.metrics.check_scoring",
    "sklearn_dual.metrics.completeness_score",
    "sklearn_dual.metrics.class_likelihood_ratios",
    "sklearn_dual.metrics.classification_report",
    "sklearn_dual.metrics.cluster.adjusted_mutual_info_score",
    "sklearn_dual.metrics.cluster.contingency_matrix",
    "sklearn_dual.metrics.cluster.entropy",
    "sklearn_dual.metrics.cluster.fowlkes_mallows_score",
    "sklearn_dual.metrics.cluster.homogeneity_completeness_v_measure",
    "sklearn_dual.metrics.cluster.normalized_mutual_info_score",
    "sklearn_dual.metrics.cluster.silhouette_samples",
    "sklearn_dual.metrics.cluster.silhouette_score",
    "sklearn_dual.metrics.cohen_kappa_score",
    "sklearn_dual.metrics.confusion_matrix",
    "sklearn_dual.metrics.consensus_score",
    "sklearn_dual.metrics.coverage_error",
    "sklearn_dual.metrics.d2_absolute_error_score",
    "sklearn_dual.metrics.d2_log_loss_score",
    "sklearn_dual.metrics.d2_pinball_score",
    "sklearn_dual.metrics.d2_tweedie_score",
    "sklearn_dual.metrics.davies_bouldin_score",
    "sklearn_dual.metrics.dcg_score",
    "sklearn_dual.metrics.det_curve",
    "sklearn_dual.metrics.explained_variance_score",
    "sklearn_dual.metrics.f1_score",
    "sklearn_dual.metrics.fbeta_score",
    "sklearn_dual.metrics.get_scorer",
    "sklearn_dual.metrics.hamming_loss",
    "sklearn_dual.metrics.hinge_loss",
    "sklearn_dual.metrics.homogeneity_score",
    "sklearn_dual.metrics.jaccard_score",
    "sklearn_dual.metrics.label_ranking_average_precision_score",
    "sklearn_dual.metrics.label_ranking_loss",
    "sklearn_dual.metrics.log_loss",
    "sklearn_dual.metrics.make_scorer",
    "sklearn_dual.metrics.matthews_corrcoef",
    "sklearn_dual.metrics.max_error",
    "sklearn_dual.metrics.mean_absolute_error",
    "sklearn_dual.metrics.mean_absolute_percentage_error",
    "sklearn_dual.metrics.mean_gamma_deviance",
    "sklearn_dual.metrics.mean_pinball_loss",
    "sklearn_dual.metrics.mean_poisson_deviance",
    "sklearn_dual.metrics.mean_squared_error",
    "sklearn_dual.metrics.mean_squared_log_error",
    "sklearn_dual.metrics.mean_tweedie_deviance",
    "sklearn_dual.metrics.median_absolute_error",
    "sklearn_dual.metrics.multilabel_confusion_matrix",
    "sklearn_dual.metrics.mutual_info_score",
    "sklearn_dual.metrics.ndcg_score",
    "sklearn_dual.metrics.pair_confusion_matrix",
    "sklearn_dual.metrics.adjusted_rand_score",
    "sklearn_dual.metrics.pairwise.additive_chi2_kernel",
    "sklearn_dual.metrics.pairwise.chi2_kernel",
    "sklearn_dual.metrics.pairwise.cosine_distances",
    "sklearn_dual.metrics.pairwise.cosine_similarity",
    "sklearn_dual.metrics.pairwise.euclidean_distances",
    "sklearn_dual.metrics.pairwise.haversine_distances",
    "sklearn_dual.metrics.pairwise.laplacian_kernel",
    "sklearn_dual.metrics.pairwise.linear_kernel",
    "sklearn_dual.metrics.pairwise.manhattan_distances",
    "sklearn_dual.metrics.pairwise.nan_euclidean_distances",
    "sklearn_dual.metrics.pairwise.paired_cosine_distances",
    "sklearn_dual.metrics.pairwise.paired_distances",
    "sklearn_dual.metrics.pairwise.paired_euclidean_distances",
    "sklearn_dual.metrics.pairwise.paired_manhattan_distances",
    "sklearn_dual.metrics.pairwise.pairwise_distances_argmin_min",
    "sklearn_dual.metrics.pairwise.pairwise_kernels",
    "sklearn_dual.metrics.pairwise.polynomial_kernel",
    "sklearn_dual.metrics.pairwise.rbf_kernel",
    "sklearn_dual.metrics.pairwise.sigmoid_kernel",
    "sklearn_dual.metrics.pairwise_distances",
    "sklearn_dual.metrics.pairwise_distances_argmin",
    "sklearn_dual.metrics.pairwise_distances_chunked",
    "sklearn_dual.metrics.precision_recall_curve",
    "sklearn_dual.metrics.precision_recall_fscore_support",
    "sklearn_dual.metrics.precision_score",
    "sklearn_dual.metrics.r2_score",
    "sklearn_dual.metrics.rand_score",
    "sklearn_dual.metrics.recall_score",
    "sklearn_dual.metrics.roc_auc_score",
    "sklearn_dual.metrics.roc_curve",
    "sklearn_dual.metrics.root_mean_squared_error",
    "sklearn_dual.metrics.root_mean_squared_log_error",
    "sklearn_dual.metrics.top_k_accuracy_score",
    "sklearn_dual.metrics.v_measure_score",
    "sklearn_dual.metrics.zero_one_loss",
    "sklearn_dual.model_selection.cross_val_predict",
    "sklearn_dual.model_selection.cross_val_score",
    "sklearn_dual.model_selection.cross_validate",
    "sklearn_dual.model_selection.learning_curve",
    "sklearn_dual.model_selection.permutation_test_score",
    "sklearn_dual.model_selection.train_test_split",
    "sklearn_dual.model_selection.validation_curve",
    "sklearn_dual.neighbors.kneighbors_graph",
    "sklearn_dual.neighbors.radius_neighbors_graph",
    "sklearn_dual.neighbors.sort_graph_by_row_values",
    "sklearn_dual.preprocessing.add_dummy_feature",
    "sklearn_dual.preprocessing.binarize",
    "sklearn_dual.preprocessing.label_binarize",
    "sklearn_dual.preprocessing.normalize",
    "sklearn_dual.preprocessing.scale",
    "sklearn_dual.random_projection.johnson_lindenstrauss_min_dim",
    "sklearn_dual.svm.l1_min_c",
    "sklearn_dual.tree.export_graphviz",
    "sklearn_dual.tree.export_text",
    "sklearn_dual.tree.plot_tree",
    "sklearn_dual.utils.gen_batches",
    "sklearn_dual.utils.gen_even_slices",
    "sklearn_dual.utils.resample",
    "sklearn_dual.utils.safe_mask",
    "sklearn_dual.utils.extmath.randomized_svd",
    "sklearn_dual.utils.class_weight.compute_class_weight",
    "sklearn_dual.utils.class_weight.compute_sample_weight",
    "sklearn_dual.utils.graph.single_source_shortest_path_length",
]


@pytest.mark.parametrize("func_module", PARAM_VALIDATION_FUNCTION_LIST)
def test_function_param_validation(func_module):
    """Check param validation for public functions that are not wrappers around
    estimators.
    """
    func, func_name, func_params, required_params = _get_func_info(func_module)

    parameter_constraints = getattr(func, "_skl_parameter_constraints")

    _check_function_param_validation(
        func, func_name, func_params, required_params, parameter_constraints
    )


PARAM_VALIDATION_CLASS_WRAPPER_LIST = [
    ("sklearn_dual.cluster.affinity_propagation", "sklearn_dual.cluster.AffinityPropagation"),
    ("sklearn_dual.cluster.dbscan", "sklearn_dual.cluster.DBSCAN"),
    ("sklearn_dual.cluster.k_means", "sklearn_dual.cluster.KMeans"),
    ("sklearn_dual.cluster.mean_shift", "sklearn_dual.cluster.MeanShift"),
    ("sklearn_dual.cluster.spectral_clustering", "sklearn_dual.cluster.SpectralClustering"),
    ("sklearn_dual.covariance.graphical_lasso", "sklearn_dual.covariance.GraphicalLasso"),
    ("sklearn_dual.covariance.ledoit_wolf", "sklearn_dual.covariance.LedoitWolf"),
    ("sklearn_dual.covariance.oas", "sklearn_dual.covariance.OAS"),
    ("sklearn_dual.decomposition.dict_learning", "sklearn_dual.decomposition.DictionaryLearning"),
    (
        "sklearn_dual.decomposition.dict_learning_online",
        "sklearn_dual.decomposition.MiniBatchDictionaryLearning",
    ),
    ("sklearn_dual.decomposition.fastica", "sklearn_dual.decomposition.FastICA"),
    ("sklearn_dual.decomposition.non_negative_factorization", "sklearn_dual.decomposition.NMF"),
    ("sklearn_dual.preprocessing.maxabs_scale", "sklearn_dual.preprocessing.MaxAbsScaler"),
    ("sklearn_dual.preprocessing.minmax_scale", "sklearn_dual.preprocessing.MinMaxScaler"),
    ("sklearn_dual.preprocessing.power_transform", "sklearn_dual.preprocessing.PowerTransformer"),
    (
        "sklearn_dual.preprocessing.quantile_transform",
        "sklearn_dual.preprocessing.QuantileTransformer",
    ),
    ("sklearn_dual.preprocessing.robust_scale", "sklearn_dual.preprocessing.RobustScaler"),
]


@pytest.mark.parametrize(
    "func_module, class_module", PARAM_VALIDATION_CLASS_WRAPPER_LIST
)
def test_class_wrapper_param_validation(func_module, class_module):
    """Check param validation for public functions that are wrappers around
    estimators.
    """
    func, func_name, func_params, required_params = _get_func_info(func_module)

    module_name, class_name = class_module.rsplit(".", 1)
    module = import_module(module_name)
    klass = getattr(module, class_name)

    parameter_constraints_func = getattr(func, "_skl_parameter_constraints")
    parameter_constraints_class = getattr(klass, "_parameter_constraints")
    parameter_constraints = {
        **parameter_constraints_class,
        **parameter_constraints_func,
    }
    parameter_constraints = {
        k: v for k, v in parameter_constraints.items() if k in func_params
    }

    _check_function_param_validation(
        func, func_name, func_params, required_params, parameter_constraints
    )
