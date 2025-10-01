import subprocess

from toucan.utils import logger


def git_checkout_and_pull(repo_root, branch):
    _execute_shell_command(f'{repo_root}/utils/shell_scripts/git_checkout.sh {repo_root} {branch}')


def commit_push_daily(project_root, report_name):
    _execute_shell_command(
        f'{project_root}/utils/shell_scripts/git_add_commit_push_daily_summary.sh {project_root} {report_name}'
    )


def _execute_shell_command(command):
    """
    Helper function to execute a shell command and log the output. Also checks the returncode and exits if needed.
    :param command: Shell command to execute
    """
    output = subprocess.run(command, shell=True, capture_output=True)  # noqa: S602
    logger.info(f'stdout of command `{command}`:\n{output.stdout.decode()}')
    if output.returncode != 0:
        logger.error(
            f'Command `{command}` exited with return code {output.returncode} and the following output:\n'
            f'{output.stderr.decode()}'
        )
        exit(1)
