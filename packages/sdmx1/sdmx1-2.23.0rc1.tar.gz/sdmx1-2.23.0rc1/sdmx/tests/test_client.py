import json
import logging
import re
from io import BytesIO
from typing import TYPE_CHECKING

import pandas as pd
import pytest
from requests import HTTPError, PreparedRequest

import sdmx
from sdmx.util.requests import save_response

if TYPE_CHECKING:
    from pathlib import Path

    from requests import Session

    from sdmx import Client
    from sdmx.testing.data import SpecimenCollection


def test_deprecated_request(caplog) -> None:
    message = "Request class will be removed in v3.0; use Client(…)"
    with pytest.warns(DeprecationWarning, match=re.escape(message)):
        sdmx.Request("ECB")

    assert caplog.record_tuples == [("sdmx.client", logging.WARNING, message)]


def test_read_sdmx(tmp_path: "Path", specimen: "SpecimenCollection") -> None:
    # Copy the file to a temporary file with an urecognizable suffix
    target = tmp_path / "foo.badsuffix"
    with specimen("flat.json", opened=False) as original:
        target.open("w").write(original.read_text())

    # With unknown file extension, read_sdmx() peeks at the file content
    sdmx.read_sdmx(target)

    # Format can be inferred from an already-open file without extension
    with specimen("flat.json") as f:
        sdmx.read_sdmx(f)

    # Exception raised when the file contents don't allow to guess the format
    bad_file = BytesIO(b"#! neither XML nor JSON")
    with pytest.raises(RuntimeError, match="cannot infer SDMX message format from "):
        sdmx.read_sdmx(bad_file)

    # Using the format= argument forces a certain reader to be used
    with pytest.raises(json.JSONDecodeError):
        sdmx.read_sdmx(bad_file, format="JSON")


class TestClient:
    @pytest.fixture
    def client(
        self, testsource: str, session_with_stored_responses: "Session"
    ) -> "Client":
        """A :class:`Client` connected to a non-existent test source."""
        return sdmx.Client(testsource, session=session_with_stored_responses)

    def test_init(self) -> None:
        with pytest.warns(
            DeprecationWarning, match=re.escape("Client(…, log_level=…) parameter")
        ):
            sdmx.Client(log_level=logging.ERROR)

        # Invalid source name raise an exception
        with pytest.raises(ValueError):
            sdmx.Client("noagency")

    # Regular methods
    def test_clear_cache(self, client: "Client") -> None:
        client.clear_cache()

    def test_session_attrs0(
        self, caplog: "pytest.LogCaptureFixture", client: "Client"
    ) -> None:
        # Deprecated attributes
        with pytest.warns(DeprecationWarning, match="Setting Client.timeout"):
            client.timeout = 300

        with pytest.warns(DeprecationWarning, match="Getting Client.timeout"):
            assert client.timeout == 300

        client.get(
            "datastructure",
            dry_run=True,
            verify=True,  # Session attribute
            allow_redirects=False,  # Argument to Session.send()
        )

        assert not any("replaces" in m for m in caplog.messages)
        caplog.clear()

        # Same, with different values
        client.get(
            "datastructure",
            dry_run=True,
            verify=False,
            allow_redirects=True,
            timeout=123,
        )

        # Messages are logged
        assert "Client.session.verify=False replaces True" in caplog.messages
        assert (
            "Client.get() args {'allow_redirects': True, 'timeout': 123} replace "
            "{'allow_redirects': False}" in caplog.messages
        )

    def test_session_attrs1(
        self, testsource: str, session_with_stored_responses: "Session"
    ) -> None:
        with pytest.raises(ValueError):
            sdmx.Client(testsource, session=session_with_stored_responses, verify=False)

    def test_dir(self, client: "Client") -> None:
        """dir() includes convenience methods for resource endpoints."""
        expected = {
            "cache",
            "clear_cache",
            "get",
            "preview_data",
            "series_keys",
            "session",
            "source",
            "timeout",
        }
        expected |= set(ep.name for ep in sdmx.Resource)
        assert set(filter(lambda s: not s.startswith("_"), dir(client))) == expected

    @pytest.mark.network
    def test_request_get_args(self) -> None:
        ESTAT = sdmx.Client("ESTAT")

        # Client._make_key accepts '+'-separated values
        args = dict(
            resource_id="UNE_RT_A",
            key={"geo": "EL+ES+IE"},
            params={"startPeriod": "2007"},
            dry_run=True,
            use_cache=True,
        )
        # Store the URL
        url = ESTAT.data(**args).url

        # Using an iterable of key values gives the same URL
        args["key"] = {"geo": ["EL", "ES", "IE"]}
        assert ESTAT.data(**args).url == url

        # Using a direct string for a key gives the same URL
        args["key"] = "....EL+ES+IE"  # No specified values for first 4 dimensions
        assert ESTAT.data(**args).url == url

        # Giving 'provider' is redundant for a data request, causes a warning
        with pytest.warns(UserWarning, match="'agency_id' argument is redundant"):
            ESTAT.data(
                "UNE_RT_A",
                key={"geo": "EL+ES+IE"},
                params={"startPeriod": "2007"},
                agency_id="ESTAT",
            )

        # Using an unknown endpoint is an exception
        with pytest.raises(KeyError):
            ESTAT.get("badendpoint", "id")

        # TODO test Client.get(obj) with IdentifiableArtefact subclasses

    def test_get0(self, client: "Client") -> None:
        """:meth:`.get` handles mixed query parameters correctly."""
        req = client.get(
            "dataflow", detail="full", params={"references": "none"}, dry_run=True
        )
        assert isinstance(req, PreparedRequest)
        assert (
            "https://example.com/sdmx-rest/dataflow/TEST/all/latest?detail=full&"
            "references=none" == req.url
        )

    def test_get1(self, client: "Client") -> None:
        """Exceptions are raised on invalid arguments."""
        # Exception is raised on unrecognized arguments
        exc = "Unexpected/unhandled parameters {'foo': 'bar'}"
        with pytest.raises(ValueError, match=exc):
            client.get("datastructure", foo="bar")

    def test_getattr(self, client: "Client") -> None:
        with pytest.raises(AttributeError):
            client.notanendpoint()

    # @pytest.mark.skip(reason="Temporarily offline on 2021-03-23")
    @pytest.mark.network
    def test_preview_data(self) -> None:
        ECB = sdmx.Client("ECB")

        # List of keys can be retrieved
        keys = ECB.preview_data("EXR")
        assert isinstance(keys, list)

        # Count of keys can be determined
        assert len(keys) > 1000

        # A filter can be provided, resulting in fewer keys
        keys = ECB.preview_data("EXR", {"CURRENCY": "CAD+CHF+CNY"})
        N = 33
        assert N >= len(keys)

        # Result can be converted to pandas object
        keys_df = sdmx.to_pandas(keys)
        assert isinstance(keys_df, pd.DataFrame)
        assert N >= len(keys_df)

    def test_request_from_args(
        self, caplog: "pytest.LogCaptureFixture", client: "Client"
    ) -> None:
        # Raises for invalid resource type
        # TODO Move this test; this error is no longer handled in _request_from_args()
        kwargs = dict(resource_type="foo")
        with pytest.raises(AttributeError):
            client._request_from_args(kwargs)

        # Raises for not implemented endpoint
        _id = "OECD_JSON"
        with pytest.raises(NotImplementedError, match=f"{_id} does not implement"):
            sdmx.Client(_id).get("datastructure")

        # Raises for invalid key type
        with pytest.raises(TypeError, match="must be str or dict; got int"):
            client.get("data", key=12345)

        # Warns for deprecated argument
        with pytest.warns(
            DeprecationWarning, match="validate= keyword argument to Client.get"
        ):
            client.get("datastructure", validate=False, dry_run=True)

    # TODO update or remove
    @pytest.mark.xfail(reason="SDMX 3.0.0 is now supported → no exception raised")
    def test_v3_unsupported(self, client: "Client") -> None:
        """Client raises an exception when an SDMX 3.0 message is returned."""
        df_id, key = "DATAFLOW", ".KEY2.KEY3..KEY5"

        save_response(
            client.session,
            "GET",
            url=f"{client.source.url}/data/{df_id}/{key}",
            content="""<?xml version='1.0' encoding='UTF-8'?>
<mes:Structure xmlns:mes="http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message">
</mes:Structure>""".encode(),
            headers={"Content-type": "application/vnd.sdmx.data+xml; version=3.0.0"},
        )

        with pytest.raises(
            ValueError, match="can't determine a reader for response content type"
        ):
            client.get("data", resource_id=df_id, key=key)


@pytest.mark.network
@pytest.mark.xfail(
    reason="Flaky; see https://github.com/khaeru/sdmx/issues/148", raises=HTTPError
)
def test_read_url0() -> None:
    """URL can be queried without instantiating Client."""
    sdmx.read_url(
        "https://sdw-wsrest.ecb.europa.eu/service/datastructure/ECB/ECB_EXR1/latest?"
        "references=all"
    )


def test_read_url1() -> None:
    """Exception is raised on invalid arguments."""
    with pytest.raises(
        ValueError, match=r"{'foo': 'bar'} supplied with get\(url=...\)"
    ):
        sdmx.read_url("https://example.com", foo="bar")
