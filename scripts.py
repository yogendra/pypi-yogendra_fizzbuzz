import subprocess

def test():
    """
    Run all unittests. Equivalent to:
    `poetry run python -u -m pytest`
    """
    subprocess.run(
        ['python', '-u', '-m', 'pytest', '-v']
    )
