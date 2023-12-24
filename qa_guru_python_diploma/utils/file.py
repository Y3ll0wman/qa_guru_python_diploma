def abs_path_from_project(relative_path: str):
    import qa_guru_python_diploma
    from pathlib import Path

    return (
        Path(qa_guru_python_diploma.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )
