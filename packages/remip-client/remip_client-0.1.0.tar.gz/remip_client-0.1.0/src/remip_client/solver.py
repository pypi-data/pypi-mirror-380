import json
import logging

import requests
from pulp import LpProblem, LpSolver, constants


logger = logging.getLogger(__name__)


def get_logging_level(level_label: str):
    return int(getattr(logging, level_label.upper()))


class ReMIPSolver(LpSolver):
    """
    A PuLP solver that uses the MIP Solver API.
    Works in both CPython and Pyodide environments.
    """

    def __init__(
        self, base_url="http://localhost:8000", stream=True, timeout=None, **kwargs
    ):
        super().__init__(**kwargs)
        self.base_url = base_url
        self.stream = stream
        self.timeout = timeout

    def actualSolve(self, lp: LpProblem) -> int:
        """
        Solves the problem by sending it to the MIP Solver API.
        """
        return self.solve(lp)

    def solve(self, lp: LpProblem) -> int:
        """
        Solves the problem by sending it to the MIP Solver API.
        """
        problem_dict = lp.toDict()
        solution = None

        try:
            url = f"{self.base_url}/solve"
            params = {}
            if self.stream:
                params["stream"] = "sse"
            if self.timeout is not None:
                params["timeout"] = self.timeout

            if not self.stream:
                # Non-streaming case
                response = requests.post(
                    url,
                    params=params,
                    json=problem_dict,
                    timeout=None,  # This is the client-side request timeout, not the solver timeout
                )
                response.raise_for_status()
                solution = response.json()
            else:
                # Streaming case
                response = requests.post(
                    url,
                    params=params,
                    json=problem_dict,
                    timeout=None,  # This is the client-side request timeout, not the solver timeout
                    stream=True,
                )
                response.raise_for_status()
                current_event = None
                for line in response.iter_lines():
                    line = line.decode("utf-8")
                    if not line:  # Skip empty lines
                        continue
                    if line.startswith("event: "):
                        current_event = line[7:]  # Remove "event: " prefix
                    elif line.startswith("data: "):
                        if current_event is None:
                            continue
                        data = json.loads(line[6:])  # Remove "data: " prefix
                        match current_event:
                            case "result":
                                # Handle both cases: data contains solution directly or nested in solution field
                                if "solution" in data:
                                    solution = data["solution"]
                                else:
                                    solution = data
                            case "log":
                                logger.log(
                                    get_logging_level(data.get("level", "info")),
                                    f"[{data.get('timestamp')}] {data.get('message')}",
                                )
                            case "metric":
                                logger.log(
                                    get_logging_level(data.get("level", "info")),
                                    f"[{data.get('timestamp')}] Iter: {data.get('iteration')}, "
                                    f"Obj: {data.get('objective_value')}, Gap: {data.get('gap')}",
                                )
                            case _:
                                # Ignore unknown event
                                continue
        except requests.exceptions.RequestException as e:
            logger.warning(f"Could not connect to API: {e}")
            lp.status = constants.LpStatusNotSolved
            return lp.status
        except Exception as e:
            logger.warning(f"An unexpected error occurred: {e}")
            lp.status = constants.LpStatusNotSolved
            return lp.status

        if solution is None:
            logger.warning("Did not receive solution from server.")
            lp.status = constants.LpStatusNotSolved
            return lp.status

        status_map = {
            "optimal": constants.LpStatusOptimal,
            "infeasible": constants.LpStatusInfeasible,
            "unbounded": constants.LpStatusUnbounded,
            "not solved": constants.LpStatusNotSolved,
            "timelimit": constants.LpStatusNotSolved,
        }
        lp.status = status_map.get(solution["status"], constants.LpStatusUndefined)
        if solution.get("objective_value") is not None:
            lp.objective.value = solution["objective_value"]

        if lp.status == constants.LpStatusOptimal:
            for var in lp.variables():
                if var.name in solution["variables"]:
                    var.varValue = solution["variables"][var.name]

            # Store additional solution information
            lp.mip_gap = solution.get("mip_gap")
            lp.slacks = solution.get("slacks")
            lp.duals = solution.get("duals")
            lp.reduced_costs = solution.get("reduced_costs")

        return lp.status
