import os
import json
import tempfile
import shutil
import unittest
from click.testing import CliRunner
import subprocess
import sys

from dorplan.cli import cli, DorPlanCli
from dorplan.tests.data.graph_coloring import GraphColoring


class TestCliGraphColoring(unittest.TestCase):
    def setUp(self):
        self.app = GraphColoring
        self.engine = next(iter(self.app.solvers.values()))
        self.cli_app = DorPlanCli(self.app, self.engine)
        self.runner = CliRunner()
        self.tmpdir = tempfile.mkdtemp()
        self.test_case = self.app().test_cases[0]
        self.instance_path = os.path.join(self.tmpdir, "instance.json")
        with open(self.instance_path, "w") as f:
            json.dump(self.test_case["instance"], f)

    def tearDown(self):
        shutil.rmtree(self.tmpdir)

    def test_solve_instance_json(self):
        output_path = os.path.join(self.tmpdir, "out.json")
        result = self.runner.invoke(
            cli,
            [
                "solve-instance",
                "--instance",
                self.instance_path,
                "--output-path",
                output_path,
            ],
            obj=self.cli_app,
        )
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Solution saved in", result.output)
        self.assertTrue(os.path.exists(output_path))

    def test_solve_instance_test_flag(self):
        output_path = os.path.join(self.tmpdir, "out.json")
        result = self.runner.invoke(
            cli,
            [
                "solve-instance",
                "--test",
                "--output-path",
                output_path,
            ],
            obj=self.cli_app,
        )
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Solution saved in", result.output)
        self.assertTrue(os.path.exists(output_path))

    def test_get_report(self):
        solution_path = os.path.join(self.tmpdir, "solution.json")
        # Generate a solution using the CLI first
        self.runner.invoke(
            cli,
            [
                "solve-instance",
                "--instance",
                self.instance_path,
                "--output-path",
                solution_path,
            ],
            obj=self.cli_app,
        )
        report_path = os.path.join(self.tmpdir, "report.html")
        result = self.runner.invoke(
            cli,
            [
                "get-report",
                "--instance",
                self.instance_path,
                "--solution",
                solution_path,
                "--report-path",
                report_path,
            ],
            obj=self.cli_app,
        )
        if result.exit_code:
            print(result)
            print(result.output)
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Report saved in", result.output)
        self.assertTrue(os.path.exists(report_path))

    def test_solve_instance_no_instance(self):
        result = self.runner.invoke(
            cli,
            [
                "solve-instance",
            ],
            obj=self.cli_app,
        )
        self.assertNotEqual(result.exit_code, 0)
        self.assertTrue(
            "No instance was provided" in result.output or result.exit_code != 0
        )

    def test_get_report_no_instance(self):
        result = self.runner.invoke(
            cli,
            [
                "get-report",
            ],
            obj=self.cli_app,
        )
        self.assertNotEqual(result.exit_code, 0)
        self.assertTrue(
            "No instance was provided" in result.output or result.exit_code != 0
        )

    def test_logging_to_file_subprocess_ortools(self):
        log_content = self.run_example_in_process("ortools")
        self.assertTrue(log_content.strip())  # Check log file is not empty
        self.assertIn("Starting CP-SAT solver v9.14.6206", log_content)

    def test_logging_to_file_subprocess_pulp(self):
        log_content = self.run_example_in_process("pulp")
        self.assertTrue(log_content.strip())  # Check log file is not empty
        self.assertIn("Running HiGHS", log_content)

    def test_logging_to_file_subprocess_timefold(self):
        log_content = self.run_example_in_process("timefold")
        self.assertTrue(log_content.strip())  # Check log file is not empty
        self.assertIn("timefold.solver", log_content)

    def run_example_in_process(self, my_solver: str, timeout: int = 2) -> str:
        log_path = os.path.join(self.tmpdir, "log.txt")
        output_path = os.path.join(self.tmpdir, "out.json")
        example_script = os.path.join(
            os.path.dirname(__file__), "../example/example_cli.py"
        )
        # Prepare CLI command as a subprocess
        cmd = [
            sys.executable,
            example_script,
            "solve-instance",
            "--instance",
            self.instance_path,
            "--output-path",
            output_path,
            "-c",
            "logPath",
            log_path,
            "-c",
            "solver",
            my_solver,
            "-c",
            "timeLimit",
            str(timeout),
        ]
        env = os.environ.copy()
        env["PYTHONPATH"] = os.pathsep.join(sys.path)
        result = subprocess.run(cmd, env=env, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, msg=result.stderr)
        self.assertTrue(os.path.exists(log_path))
        with open(log_path, "r") as f:
            log_content = f.read()
        return log_content


if __name__ == "__main__":
    unittest.main()
