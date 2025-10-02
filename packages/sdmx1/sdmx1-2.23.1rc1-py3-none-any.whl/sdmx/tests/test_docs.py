"""Test code appearing in the documentation.

The 'network' mark is used to mark tests that will access the Internet. In order to run
these tests, a command-line argument must be given:

$ pytest -m network [...]
"""

import logging
import re
from typing import TYPE_CHECKING

import numpy as np
import pandas as pd
import pytest

import sdmx
from sdmx import Client
from sdmx.dictlike import DictLike
from sdmx.model.v21 import GenericDataSet
from sdmx.testing import assert_pd_equal

log = logging.getLogger(__name__)

if TYPE_CHECKING:
    import sdmx.message


@pytest.mark.network
def test_example() -> None:
    """Code from :file:`doc/example.rst`."""
    import sdmx

    estat = sdmx.Client("ESTAT")

    sm: "sdmx.message.StructureMessage" = estat.datastructure("UNE_RT_A")

    # Identify partial URNs for some code lists
    partial_urns = []
    for cl in sm.codelist.values():
        if cl.id in ("AGE", "UNIT", "SEX"):
            partial_urns.append(cl.urn.rpartition("=")[2])
    # These strings should be the ones hard-coded in example.rst
    log.info(f"for cl in {repr(partial_urns).strip('[]')}:")

    # NB Use partial URNs to match even if only single versions are stored under keys
    #    like "AGE"
    for cl in partial_urns:
        print(sdmx.to_pandas(sm.get(cl)))

    dm = estat.data("UNE_RT_A", key={"geo": "EL+ES+IE"}, params={"startPeriod": "2007"})

    data = sdmx.to_pandas(dm).xs("Y15-74", level="age", drop_level=False)

    data.loc[("A", "Y15-74", "PC_ACT", "T")]

    # Further checks per https://github.com/dr-leo/pandaSDMX/issues/157

    # DimensionDescriptor for the structure message
    dd1 = sm.structure.UNE_RT_A.dimensions  # type: ignore [attr-defined]

    # DimensionDescriptor retrieved whilst validating the data message
    dd2 = dm.data[0].structured_by.dimensions

    # DimensionDescriptors have same ID, components and order
    assert dd1 == dd2

    # One SeriesKey from the data message
    sk = list(dm.data[0].series.keys())[0]

    # Key values have same order as in the DSD
    assert dd1.order_key(sk) == sk


@pytest.mark.network
def test_doc_index1() -> None:
    """A code example that formerly appeared in doc/index.rst."""
    estat = Client("ESTAT")
    sm0 = estat.dataflow("UNE_RT_A")

    with pytest.raises(TypeError):
        # This presumes the DataStructureDefinition instance can conduct a
        # network request for its own content
        sm0.dataflow.UNE_RT_A.structure(request=True, target_only=False)

    # Same effect
    sm1 = estat.get(
        "datastructure",
        sm0.dataflow.UNE_RT_A.structure.id,
        params=dict(references="descendants"),
    )
    assert isinstance(sm1, sdmx.message.StructureMessage)

    # Even better: Client.get(…) should examine the class and ID of the object
    # structure = estat.get(flow_response.dataflow.UNE_RT_A.structure)

    # Show some codelists
    s = sdmx.to_pandas(sm1)
    expected = pd.Series(
        {
            "ACP": "African, Caribbean and Pacific Group of States, signatories of the "
            "Partnership Agreement",
            "ACP_AFR": "African ACP states",
            "ACP_CRB": "Caribbean ACP states",
            "ACP_PAC": "Pacific ACP states",
            "AD": "Andorra",
        },
        name="Geopolitical entity (reporting)",
    ).rename_axis("GEO")

    # StructureMessage is converted to DictLike
    assert isinstance(s, DictLike)
    # "codelist" key retrieves a second-level DictLike
    assert isinstance(s.codelist, DictLike)  # type: ignore [attr-defined]

    # Same effect
    # NB At some times (e.g. between 2024-03-15 and 2024-06-18) this query retrieves
    #    multiple versions of similar artefacts. A more explicit argument to get() that
    #    includes the version (like get("GEO(21.0)")) may be temporarily needed.
    s = sdmx.to_pandas(sm1.get("ESTAT:GEO"))
    assert_pd_equal(s.sort_index().head(), expected)


@pytest.mark.network
def test_doc_usage_structure():
    """Code examples in walkthrough.rst."""
    ecb = Client("ECB")

    ecb_via_proxy = Client("ECB", proxies={"http": "http://1.2.3.4:5678"})
    assert all(
        getattr(ecb_via_proxy.session, k) == v
        for k, v in (
            ("proxies", {"http": "http://1.2.3.4:5678"}),
            ("stream", False),
            ("timeout", 30.0),
        )
    )

    msg1 = ecb.categoryscheme(agency_id="all")

    assert msg1.response.url == (
        "https://data-api.ecb.europa.eu/service/categoryscheme/all/all/latest"
        "?references=parentsandsiblings"
    )

    # Check specific headers
    headers = msg1.response.headers
    assert re.fullmatch(
        r"application/vnd\.sdmx\.structure\+xml; ?version=2\.1",
        headers["Content-Type"],
    )
    assert {"Connection", "Date", "Server"} <= set(headers)

    # Removed: in pandaSDMX 0.x this was a convenience method that (for this
    # structure message) returned two DataStructureDefinitions. Contra the
    # spec, that assumes:
    # - There is 1 Categorization using the CategoryScheme; there could be
    #   many.
    # - The Categorization maps DataStructureDefinitions to Categories, when
    #   there could be many.
    # list(cat_response.category_scheme['MOBILE_NAVI']['07'])

    dfs = sdmx.to_pandas(msg1.dataflow).head()
    expected = pd.Series(
        {
            "AME": "AMECO",
            "BKN": "Banknotes statistics",
            "BLS": "Bank Lending Survey Statistics",
            "BOP": (
                "Euro Area Balance of Payments and International Investment "
                "Position Statistics"
            ),
            "BSI": "Balance Sheet Items",
        }
    )
    assert_pd_equal(dfs, expected)

    flows = ecb.dataflow()  # noqa: F841
    dsd_id = msg1.dataflow.EXR.structure.id
    assert dsd_id == "ECB_EXR1"

    refs = dict(references="all")
    msg2 = ecb.datastructure(resource_id=dsd_id, params=refs)
    dsd = msg2.structure[dsd_id]

    assert sdmx.to_pandas(dsd.dimensions) == [
        "FREQ",
        "CURRENCY",
        "CURRENCY_DENOM",
        "EXR_TYPE",
        "EXR_SUFFIX",
        "TIME_PERIOD",
    ]

    cl = sdmx.to_pandas(msg2.codelist["CL_CURRENCY"]).sort_index()
    expected = pd.Series(
        {
            "ADF": "Andorran Franc (1-1 peg to the French franc)",
            "ADP": "Andorran Peseta (1-1 peg to the Spanish peseta)",
            "AED": "United Arab Emirates dirham",
            "AFA": "Afghanistan afghani (old)",
            "AFN": "Afghanistan, Afghanis",
        },
        name="Currency code list",
    ).rename_axis("CL_CURRENCY")
    assert_pd_equal(cl.head(), expected)


# @pytest.mark.skip(reason="Temporarily offline on 2021-03-23")
@pytest.mark.network
def test_doc_usage_data():
    """Code examples in usage.rst."""
    ecb = Client("ECB")

    data_response = ecb.data(
        resource_id="EXR",
        key={"CURRENCY": "USD+JPY"},
        params={"startPeriod": "2016", "endPeriod": "2016-12-31"},
    )
    # # Commented: do the same without triggering requests for validation
    # data_response = ecb.data(resource_id='EXR', key='.JPY+USD...',
    #                          params={'startPeriod': '2016',
    #                                  'endPeriod': '2016-12-31'})
    data = data_response.data[0]

    assert type(data) is GenericDataSet

    # This message doesn't explicitly specify the remaining dimensions; unless
    # they are inferred from the SeriesKeys, then the DimensionDescriptor is
    # not complete
    # assert data.structured_by.dimensions[-1] == 'TIME_PERIOD'
    # data.dim_at_obs

    series_keys = list(data.series)

    assert len(series_keys) == 22

    series_keys[5]

    assert sorted(set(sk.FREQ.value for sk in data.series)) == "A D H M Q".split()

    daily = sdmx.to_pandas(data).xs("D", level="FREQ")
    assert len(daily) == 514

    assert_pd_equal(
        daily.tail().values, np.array([1.0446, 1.0445, 1.0401, 1.0453, 1.0541])
    )


def test_doc_howto_timeseries(specimen):
    with specimen("sg-ts.xml") as f:
        ds = sdmx.read_sdmx(f).data[0]

    # Convert to pd.Series and unstack the time dimension to columns
    base = sdmx.to_pandas(ds)
    s1 = base.unstack("TIME_PERIOD")

    # DatetimeIndex on columns
    s1.columns = pd.to_datetime(s1.columns)
    assert isinstance(s1.columns, pd.DatetimeIndex)

    # DatetimeIndex on index
    s2 = base.unstack("TIME_PERIOD").transpose()
    s2.index = pd.to_datetime(s2.index)
    assert isinstance(s2.index, pd.DatetimeIndex)

    # Same with pd.PeriodIndex
    s3 = s1.to_period(axis=1)
    assert isinstance(s3.columns, pd.PeriodIndex)
    assert s3.columns.freqstr == "M"

    s4 = s2.to_period(axis=0)
    assert isinstance(s4.index, pd.PeriodIndex)
    assert s4.index.freqstr == "M"
