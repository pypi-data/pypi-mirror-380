from typing import Union


def requires_dependency(
    module: str,
    library_name: Union[str, None] = None,
    package_name: Union[str, None] = None
):
    """
    A decorator to include a library/module as optional
    but required to be able to do some functionality.
    Those libraries will not be included as main 
    dependencies in the poetry file, but will appear as
    optional.

    The parameters:
    - `module`: The name with the library is imported
    in the project.
    - `library_name`: The name of the project in which
    you are using it (the one the 'pyproject.toml' file
    belongs to).
    - `package_name`: The name you need to use when
    installing (that is also set as optional in the
    .toml file).

    Example of use:
    - `@requires_dependency('PIL', 'yta_file', 'pillow')

    You must declare those libraries within the
    'pyproject.toml' file like this:

    `[tool.poetry.group.optional]
    optional = true
    [tool.poetry.group.optional.dependencies]
    faster_whisper = ">=1.0.2,<2.0.0"`
    """
    def decorator(
        func
    ):
        def wrapper(
            *args,
            **kwargs
        ):
            try:
                __import__(module)
            except ImportError:
                message = f'The function "{func.__name__}" needs the "{module}" installed.'

                message = (
                    f'{message} You can install it with this command: pip install {library_name}[{package_name}]'
                    if package_name else
                    message
                )

                raise ImportError(message)
            
            return func(*args, **kwargs)
        return wrapper
    return decorator