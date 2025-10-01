"""Formulation of the inverse Poisson problem in a square domain."""

import warnings
import requests
import torch
from io import BytesIO
from ... import Condition
from ... import LabelTensor
from ...operator import laplacian
from ...domain import CartesianDomain
from ...equation import Equation, FixedValue
from ...problem import SpatialProblem, InverseProblem
from ...utils import custom_warning_format, check_consistency

warnings.formatwarning = custom_warning_format
warnings.filterwarnings("always", category=ResourceWarning)


def _load_tensor_from_url(url, labels, timeout=10):
    """
    Downloads a tensor file from a URL and wraps it in a LabelTensor.

    This function fetches a `.pth` file containing tensor data, extracts it,
    and returns it as a LabelTensor using the specified labels. If the file
    cannot be retrieved (e.g., no internet connection), a warning is issued
    and None is returned.

    :param str url: URL to the remote `.pth` tensor file.
    :param list[str] | tuple[str] labels: Labels for the resulting LabelTensor.
    :param int timeout: Timeout for the request in seconds.
    :return: A LabelTensor object if successful, otherwise None.
    :rtype: LabelTensor | None
    """
    # Try to download the tensor file from the given URL
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        tensor = torch.load(
            BytesIO(response.content), weights_only=False
        ).tensor.detach()
        return LabelTensor(tensor, labels)

    # If the request fails, issue a warning and return None
    except requests.exceptions.RequestException as e:
        warnings.warn(
            f"Could not download data for 'InversePoisson2DSquareProblem' "
            f"from '{url}'. Reason: {e}. Skipping data loading.",
            ResourceWarning,
        )
        return None


def laplace_equation(input_, output_, params_):
    """
    Implementation of the laplace equation.

    :param LabelTensor input_: Input data of the problem.
    :param LabelTensor output_: Output data of the problem.
    :param dict params_: Parameters of the problem.
    :return: The residual of the laplace equation.
    :rtype: LabelTensor
    """
    force_term = torch.exp(
        -2 * (input_.extract(["x"]) - params_["mu1"]) ** 2
        - 2 * (input_.extract(["y"]) - params_["mu2"]) ** 2
    )
    delta_u = laplacian(output_, input_, components=["u"], d=["x", "y"])
    return delta_u - force_term


class InversePoisson2DSquareProblem(SpatialProblem, InverseProblem):
    r"""
    Implementation of the inverse 2-dimensional Poisson problem in the square
    domain :math:`[0, 1] \times [0, 1]`,
    with unknown parameter domain :math:`[-1, 1] \times [-1, 1]`.
    The `"data"` condition is added only if the required files are
    downloaded successfully.

    :Example:
        >>> problem = InversePoisson2DSquareProblem()
    """

    output_variables = ["u"]
    x_min, x_max = -2, 2
    y_min, y_max = -2, 2
    spatial_domain = CartesianDomain({"x": [x_min, x_max], "y": [y_min, y_max]})
    unknown_parameter_domain = CartesianDomain({"mu1": [-1, 1], "mu2": [-1, 1]})

    domains = {
        "g1": CartesianDomain({"x": [x_min, x_max], "y": y_max}),
        "g2": CartesianDomain({"x": [x_min, x_max], "y": y_min}),
        "g3": CartesianDomain({"x": x_max, "y": [y_min, y_max]}),
        "g4": CartesianDomain({"x": x_min, "y": [y_min, y_max]}),
        "D": CartesianDomain({"x": [x_min, x_max], "y": [y_min, y_max]}),
    }

    conditions = {
        "g1": Condition(domain="g1", equation=FixedValue(0.0)),
        "g2": Condition(domain="g2", equation=FixedValue(0.0)),
        "g3": Condition(domain="g3", equation=FixedValue(0.0)),
        "g4": Condition(domain="g4", equation=FixedValue(0.0)),
        "D": Condition(domain="D", equation=Equation(laplace_equation)),
    }

    def __init__(self, load=True, data_size=1.0):
        """
        Initialization of the :class:`InversePoisson2DSquareProblem`.

        :param bool load: If True, it attempts to load data from remote URLs.
            Set to False to skip data loading (e.g., if no internet connection).
        :param float data_size: The fraction of the total data to use for the
            "data" condition. If set to 1.0, all available data is used.
            If set to 0.0, no data is used. Default is 1.0.
        :raises ValueError: If `data_size` is not in the range [0.0, 1.0].
        :raises ValueError: If `data_size` is not a float.
        """
        super().__init__()

        # Check consistency
        check_consistency(load, bool)
        check_consistency(data_size, float)
        if not 0.0 <= data_size <= 1.0:
            raise ValueError(
                f"data_size must be in the range [0.0, 1.0], got {data_size}."
            )

        # Load data if requested
        if load:

            # Define URLs for input and output data
            input_url = (
                "https://github.com/mathLab/PINA/raw/refs/heads/master"
                "/tutorials/tutorial7/data/pts_0.5_0.5"
            )
            output_url = (
                "https://github.com/mathLab/PINA/raw/refs/heads/master"
                "/tutorials/tutorial7/data/pinn_solution_0.5_0.5"
            )

            # Define input and output data
            input_data = _load_tensor_from_url(
                input_url, ["x", "y", "mu1", "mu2"]
            )
            output_data = _load_tensor_from_url(output_url, ["u"])

            # Add the "data" condition
            if input_data is not None and output_data is not None:
                n_data = int(input_data.shape[0] * data_size)
                self.conditions["data"] = Condition(
                    input=input_data[:n_data], target=output_data[:n_data]
                )
