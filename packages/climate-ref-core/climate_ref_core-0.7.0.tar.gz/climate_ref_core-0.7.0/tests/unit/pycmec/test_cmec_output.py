import pytest

from climate_ref_core.pycmec.metric import CMECGenerateJsonSchema
from climate_ref_core.pycmec.output import CMECOutput


@pytest.fixture
def cmec_right_output_dict():
    return {
        "provenance": {
            "environment": {
                "OS": "LINUX",
                "Package": "ILAMB",
                "Machine": "Frontier",
                "Variable": "Biomass",
            },
            "modeldata": ["./modeldata", "./othermodels"],
            "obsdata": {
                "GlobalCarbon": {
                    "version": "5.1",
                    "title": "Global forest live biomass carbon",
                },
                "NBCD2000": {
                    "version": "unknown",
                    "name": "National Biomass and Carbon data set for the Year 2000",
                },
            },
            "log": "cmec_output.log",
        },
        "index": "index.html",
        "data": {
            "gpp_bias": {
                "filename": "gpp_bias.nc",
                "long_name": "mean gpp bias",
                "description": "bias",
            }
        },
        "html": None,
        "diagnostics": None,
        "plots": None,
    }


def test_output_right(cmec_right_output_dict):
    CMECOutput.model_validate(cmec_right_output_dict)


def test_output_read_json(cmec_right_output_dict, datadir):
    assert CMECOutput.load_from_json(json_file=datadir / "cmec_output_sample.json")


def test_output_update(cmec_right_output_dict):
    add_sname = "awesome_fig1"
    add_plots = {
        "long_name": "awesome figure",
        "filename": "fig_1.jpg",
        "description": "test add plots",
    }

    add_html = {
        "long_name": "index html page",
        "filename": "index.html",
        "description": "test add html",
    }

    cmec_output = CMECOutput(**cmec_right_output_dict)

    cmec_output.update("plots", short_name=add_sname, dict_content=add_plots)

    cmec_output.update("html", short_name="index", dict_content=add_html)

    assert cmec_output["plots"]["awesome_fig1"]["long_name"] == "awesome figure"
    assert cmec_output["plots"]["awesome_fig1"]["filename"] == "fig_1.jpg"
    assert cmec_output["plots"]["awesome_fig1"]["description"] == "test add plots"

    assert cmec_output["html"]["index"]["long_name"] == "index html page"
    assert cmec_output["html"]["index"]["filename"] == "index.html"
    assert cmec_output["html"]["index"]["description"] == "test add html"


def test_output_create_template():
    assert CMECOutput.create_template() == {
        "index": "index.html",
        "provenance": {
            "environment": {},
            "modeldata": [],
            "obsdata": {},
            "log": "cmec_output.log",
        },
        "data": {},
        "html": {},
        "diagnostics": {},
        "plots": {},
    }


def test_output_extras(cmec_right_output_dict):
    cmec_right_output_dict["extradict"] = {}

    CMECOutput(**cmec_right_output_dict)


def test_output_data_extras(cmec_right_output_dict):
    cmec_right_output_dict["data"]["gpp_bias"]["extradict"] = {}

    CMECOutput(**cmec_right_output_dict)


def test_output_json_schema(data_regression):
    cmec_model_schema = CMECOutput.model_json_schema(schema_generator=CMECGenerateJsonSchema)

    data_regression.check(cmec_model_schema)
