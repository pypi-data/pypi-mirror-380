from alidaparse.input import *


def test_inparam():
    param = InParamFactory.from_cli(
        name="param_name", param_type=int, required=True, argv=["--param_name", "42"]
    )
    assert param.param_name == "param_name"
    assert param.param_value == 42
