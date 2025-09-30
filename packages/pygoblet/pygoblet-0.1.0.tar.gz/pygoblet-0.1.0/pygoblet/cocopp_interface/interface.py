# Copyright (c) 2025 Alliance for Sustainable Energy, LLC

import os
import warnings
from pygoblet.cocopp_interface import testbed
from collections import defaultdict, OrderedDict

def log_coco_from_results(results, output_folder="output_data"):
    """
    Write .dat, .tdat, .mdat, and .info files in the COCOPP format from a list
    of solver/problem result dictionaries.

    :param results: List of dictionaries containing test information.
        Each dictionary should contain at least the keys:
        'solver', 'problem', 'func_id', 'n_dims',
        'log' (list of (fevals, gevals, fval)), 'min'
    :param output_folder: Directory to save the output files.
        Defaults to "output_data".
    """
    suite="pyGOBLET"
    logger_name="bbob"
    data_format="bbob-new2"
    coco_version="2.7.3"
    precision=1e-8

    os.makedirs(output_folder, exist_ok=True)
    # Group by solver, func_id, n_dims
    grouped = defaultdict(list)
    for res in results:
        key = (res['solver'], res['func_id'], res['n_dims'], res['problem'])
        grouped[key].append(res)
    for (solver, func_id, n_dims, problem), runs in grouped.items():
        func_id += 1
        alg_folder = os.path.join(output_folder, solver)
        os.makedirs(alg_folder, exist_ok=True)
        dat_folder = f"data_{solver}_f{func_id}"
        dat_path = os.path.join(alg_folder, dat_folder)
        os.makedirs(dat_path, exist_ok=True)
        dat_file = os.path.join(dat_path, f"{solver}_f{func_id}_DIM{n_dims}.dat")
        tdat_file = os.path.join(dat_path, f"{solver}_f{func_id}_DIM{n_dims}.tdat")
        mdat_file = os.path.join(dat_path, f"{solver}_f{func_id}_DIM{n_dims}.mdat")
        dat_rel_path = os.path.relpath(dat_file, alg_folder)
        evals_list = []
        fval_list = []
        min_val = None
        for res in runs:
            if 'min' in res and res['min'] is not None:
                min_val = res['min']
                break
        if min_val is None:
            warnings.warn(f"Minimum for {problem} in {n_dims}D is None, use smallest fval found as min and call this function again.")
            return
        # Saving the data as .dat, .tdat, and .mdat files is required to prevent
        # warning messages from COCOPP, although data is only read from one file
        with open(dat_file, 'w') as df, open(tdat_file, 'w') as tdf, open(mdat_file, 'w') as mdf:
            for i, res in enumerate(runs):
                for f in [df, tdf, mdf]:
                    f.write(f"%% iter/random seed: {i+1}\n")
                    f.write(f"%% algorithm: {solver}\n")
                    f.write("%% columns: fevals gevals fval\n")
                    f.write("% f evaluations | g evaluations | best noise-free fitness - Fopt\n")
                for entry in res['log']:
                    if len(entry) == 3:
                        fevals, _, fval = entry
                    elif len(entry) == 2:
                        fevals, fval = entry
                    else:
                        continue
                    for f in [df, tdf, mdf]:
                        f.write(f"{fevals} 0 {fval - min_val}\n")
                evals_list.append(res.get('evals', len(res['log'])))
                last_fval = res['log'][-1][2] if len(res['log'][-1]) > 2 else res['log'][-1][1]
                fval_list.append(last_fval)
        info_file = os.path.join(alg_folder, f"{solver}_f{func_id}_DIM{n_dims}.info")
        dat_rel_path = os.path.relpath(mdat_file, alg_folder)
        info_header = f"suite = '{suite}', funcId = {func_id}, DIM = {n_dims}, Precision = {precision:.3e}, algId = '{solver}', logger = '{logger_name}', data_format = '{data_format}', coco_version = '{coco_version}'"
        info_comment = f"% Run {solver} on {problem} in {n_dims}D"
        info_data = f"{dat_rel_path}, " + ", ".join([f"{i+1}:{evals_list[i]}|{fval_list[i] - min_val}" for i in range(len(runs))])
        with open(info_file, 'w') as inf:
            inf.write(info_header + "\n")
            inf.write(info_comment + "\n")
            inf.write(info_data + "\n")

def configure_testbed(problems, test_dimensions=[2, 4, 5, 8, 10, 12], n_solvers=1, groups=None):
    """
    Configure a custom COCOPP testbed for benchmarking solvers on problems.
    This function sets up the testbed with the provided solvers and problems,
    allowing the use of the COCOPP post-processing framework.

    test_dimensions must have exactly 6 dimensions. Using less will cause errors
    in COCOPP. Using more is not recommended as dimensions past the 6th will not
    be included in the ERT scatter plots, but will not cause errors.

    Once the testbed is configured, you can run the COCOPP post-processing
    framework on the results of the solvers using the `cocopp.main()` function.

    Passing data to `cocopp.main()` with less than 6 dimensions or with
    dimensions that do not match the `test_dimensions` can lead to unexpected
    behavior like repeated, missing, or incorrect graphs and data.

    :param problems: List of problem classes.
    :param test_dimensions: List of dimensions to test any n-dimensional
        problems on, defaults to ``[2, 4, 5, 8, 10, 12]``.
    :param n_solvers: Number of solvers tested, defaults to 1.
    :param groups: Optional dictionary mapping solver names to groups.
        These groups are used to create aggregate runtime profiles in COCOPP.
        If provided must be of the form of a ordered dict.
        For example, to group all problems together, use:
        ``groups=OrderedDict({"All": range(1, len(problems)+1)})``
    """
    testbed.CustomTestbed.dims = test_dimensions
    testbed.CustomTestbed.settings['dimensions_to_display'] = test_dimensions
    testbed.CustomTestbed.settings['goto_dimension'] = test_dimensions[3]
    testbed.CustomTestbed.settings['rldDimsOfInterest'] = [test_dimensions[2], test_dimensions[4]]
    testbed.CustomTestbed.settings['tabDimsOfInterest'] = [test_dimensions[2], test_dimensions[4]]
    testbed.CustomTestbed.settings['short_names'] = {id + 1: problem.__name__ for id, problem in enumerate(problems)}
    testbed.CustomTestbed.settings['functions_with_legend'] = (1, len(problems))
    testbed.CustomTestbed.settings['last_function_number'] = len(problems)

    if n_solvers == 1:
        testbed.CustomTestbed.func_cons_groups = OrderedDict({"All": range(1, len(problems)+1)})

    if groups is not None:
        testbed.CustomTestbed.func_cons_groups = groups
