from gym_tracker_analysis.config import PATHS


def test_paths_resolve_inside_project_root():
    for value in vars(PATHS).values():
        assert value == PATHS.root or PATHS.root in value.parents
