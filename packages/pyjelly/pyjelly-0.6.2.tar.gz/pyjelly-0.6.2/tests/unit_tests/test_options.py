from __future__ import annotations

import io
from unittest.mock import Mock

import pytest
from _pytest.monkeypatch import MonkeyPatch

import pyjelly.options as op
from pyjelly import jelly
from pyjelly.errors import JellyAssertionError, JellyConformanceError
from pyjelly.options import (
    MIN_NAME_LOOKUP_SIZE,
    MIN_VERSION,
    LookupPreset,
    StreamParameters,
    StreamTypes,
)
from pyjelly.parse.decode import options_from_frame
from pyjelly.parse.ioutils import get_options_and_frames


@pytest.mark.parametrize(
    ("physical_type", "logical_type"),
    VALID_STREAM_TYPE_COMBINATIONS := [
        (jelly.PHYSICAL_STREAM_TYPE_TRIPLES, jelly.LOGICAL_STREAM_TYPE_FLAT_TRIPLES),
        (jelly.PHYSICAL_STREAM_TYPE_TRIPLES, jelly.LOGICAL_STREAM_TYPE_GRAPHS),
        (jelly.PHYSICAL_STREAM_TYPE_TRIPLES, jelly.LOGICAL_STREAM_TYPE_SUBJECT_GRAPHS),
        (jelly.PHYSICAL_STREAM_TYPE_TRIPLES, jelly.LOGICAL_STREAM_TYPE_UNSPECIFIED),
        (jelly.PHYSICAL_STREAM_TYPE_QUADS, jelly.LOGICAL_STREAM_TYPE_FLAT_QUADS),
        (jelly.PHYSICAL_STREAM_TYPE_QUADS, jelly.LOGICAL_STREAM_TYPE_DATASETS),
        (jelly.PHYSICAL_STREAM_TYPE_QUADS, jelly.LOGICAL_STREAM_TYPE_NAMED_GRAPHS),
        (
            jelly.PHYSICAL_STREAM_TYPE_QUADS,
            jelly.LOGICAL_STREAM_TYPE_TIMESTAMPED_NAMED_GRAPHS,
        ),
        (jelly.PHYSICAL_STREAM_TYPE_QUADS, jelly.LOGICAL_STREAM_TYPE_UNSPECIFIED),
        (jelly.PHYSICAL_STREAM_TYPE_GRAPHS, jelly.LOGICAL_STREAM_TYPE_FLAT_QUADS),
        (jelly.PHYSICAL_STREAM_TYPE_GRAPHS, jelly.LOGICAL_STREAM_TYPE_DATASETS),
        (jelly.PHYSICAL_STREAM_TYPE_GRAPHS, jelly.LOGICAL_STREAM_TYPE_NAMED_GRAPHS),
        (
            jelly.PHYSICAL_STREAM_TYPE_GRAPHS,
            jelly.LOGICAL_STREAM_TYPE_TIMESTAMPED_NAMED_GRAPHS,
        ),
        (jelly.PHYSICAL_STREAM_TYPE_GRAPHS, jelly.LOGICAL_STREAM_TYPE_UNSPECIFIED),
        (jelly.PHYSICAL_STREAM_TYPE_UNSPECIFIED, jelly.LOGICAL_STREAM_TYPE_UNSPECIFIED),
        (
            jelly.PHYSICAL_STREAM_TYPE_UNSPECIFIED,
            jelly.LOGICAL_STREAM_TYPE_FLAT_TRIPLES,
        ),
        (jelly.PHYSICAL_STREAM_TYPE_UNSPECIFIED, jelly.LOGICAL_STREAM_TYPE_GRAPHS),
        (
            jelly.PHYSICAL_STREAM_TYPE_UNSPECIFIED,
            jelly.LOGICAL_STREAM_TYPE_SUBJECT_GRAPHS,
        ),
        (jelly.PHYSICAL_STREAM_TYPE_UNSPECIFIED, jelly.LOGICAL_STREAM_TYPE_UNSPECIFIED),
        (jelly.PHYSICAL_STREAM_TYPE_UNSPECIFIED, jelly.LOGICAL_STREAM_TYPE_FLAT_QUADS),
        (jelly.PHYSICAL_STREAM_TYPE_UNSPECIFIED, jelly.LOGICAL_STREAM_TYPE_DATASETS),
        (
            jelly.PHYSICAL_STREAM_TYPE_UNSPECIFIED,
            jelly.LOGICAL_STREAM_TYPE_NAMED_GRAPHS,
        ),
        (
            jelly.PHYSICAL_STREAM_TYPE_UNSPECIFIED,
            jelly.LOGICAL_STREAM_TYPE_TIMESTAMPED_NAMED_GRAPHS,
        ),
    ],
)
def test_stream_types_ok(
    physical_type: jelly.PhysicalStreamType,
    logical_type: jelly.LogicalStreamType,
) -> None:
    StreamTypes(physical_type=physical_type, logical_type=logical_type)


@pytest.mark.parametrize(
    ("physical_type", "logical_type"),
    [
        (jelly.PHYSICAL_STREAM_TYPE_TRIPLES, jelly.LOGICAL_STREAM_TYPE_FLAT_QUADS),
        (jelly.PHYSICAL_STREAM_TYPE_TRIPLES, jelly.LOGICAL_STREAM_TYPE_DATASETS),
        (jelly.PHYSICAL_STREAM_TYPE_TRIPLES, jelly.LOGICAL_STREAM_TYPE_NAMED_GRAPHS),
        (
            jelly.PHYSICAL_STREAM_TYPE_TRIPLES,
            jelly.LOGICAL_STREAM_TYPE_TIMESTAMPED_NAMED_GRAPHS,
        ),
        (jelly.PHYSICAL_STREAM_TYPE_QUADS, jelly.LOGICAL_STREAM_TYPE_FLAT_TRIPLES),
        (jelly.PHYSICAL_STREAM_TYPE_QUADS, jelly.LOGICAL_STREAM_TYPE_GRAPHS),
        (jelly.PHYSICAL_STREAM_TYPE_QUADS, jelly.LOGICAL_STREAM_TYPE_SUBJECT_GRAPHS),
        (jelly.PHYSICAL_STREAM_TYPE_GRAPHS, jelly.LOGICAL_STREAM_TYPE_FLAT_TRIPLES),
        (jelly.PHYSICAL_STREAM_TYPE_GRAPHS, jelly.LOGICAL_STREAM_TYPE_GRAPHS),
        (jelly.PHYSICAL_STREAM_TYPE_GRAPHS, jelly.LOGICAL_STREAM_TYPE_SUBJECT_GRAPHS),
    ],
)
def test_stream_types_error(
    physical_type: jelly.PhysicalStreamType,
    logical_type: jelly.LogicalStreamType,
) -> None:
    with pytest.raises(JellyAssertionError):
        StreamTypes(physical_type=physical_type, logical_type=logical_type)


@pytest.mark.parametrize(
    ("generalized_statements", "rdf_star"), [(0, 0), (0, 1), (1, 0), (1, 1)]
)
def test_optional_fields(generalized_statements: int, rdf_star: int) -> None:
    mock_frame = Mock()
    mock_row = Mock()
    mock_options = Mock()

    defaults = {
        "physical_type": jelly.PHYSICAL_STREAM_TYPE_TRIPLES,
        "logical_type": jelly.PHYSICAL_STREAM_TYPE_UNSPECIFIED,
        "max_name_table_size": 1000,
        "max_prefix_table_size": 100,
        "max_datatype_table_size": 100,
        "stream_name": "",
        "generalized_statements": bool(generalized_statements),
        "rdf_star": bool(rdf_star),
        "version": 1,
    }

    for key, value in defaults.items():
        setattr(mock_options, key, value)

    mock_row.options = mock_options
    mock_frame.rows = [mock_row]

    result = options_from_frame(mock_frame, delimited=True)

    assert result.params.generalized_statements == defaults["generalized_statements"]
    assert result.params.rdf_star == defaults["rdf_star"]


@pytest.mark.parametrize(
    ("generalized_statements", "rdf_star"), [(0, 0), (0, 1), (1, 0), (1, 1)]
)
def test_stream_parameters(generalized_statements: int, rdf_star: int) -> None:
    mock_options = Mock()

    defaults = {
        "physical_type": jelly.PHYSICAL_STREAM_TYPE_TRIPLES,
        "logical_type": jelly.PHYSICAL_STREAM_TYPE_UNSPECIFIED,
        "max_name_table_size": 1000,
        "max_prefix_table_size": 100,
        "max_datatype_table_size": 100,
        "stream_name": "",
        "generalized_statements": bool(generalized_statements),
        "rdf_star": bool(rdf_star),
        "version": 1,
    }

    for key, value in defaults.items():
        setattr(mock_options, key, value)

    params = StreamParameters(
        stream_name=mock_options.stream_name,
        generalized_statements=mock_options.generalized_statements,
        rdf_star=mock_options.rdf_star,
        version=mock_options.version,
        delimited=True,
    )
    assert params.generalized_statements == mock_options.generalized_statements
    assert params.rdf_star == mock_options.rdf_star


def test_lookup_preset_validation() -> None:
    with pytest.raises(JellyConformanceError):
        LookupPreset(max_names=MIN_NAME_LOOKUP_SIZE - 1)
    p = LookupPreset.small()
    assert (p.max_names, p.max_prefixes, p.max_datatypes) == (128, 32, 32)


def test_stream_parameters_version() -> None:
    s1 = StreamParameters(namespace_declarations=False)
    assert s1.version == MIN_VERSION
    s2 = StreamParameters(namespace_declarations=True)
    assert s2.version == 2


def test_stream_options_invalid_version(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(op, "MIN_VERSION", 10)
    monkeypatch.setattr(op, "MAX_VERSION", 5)

    with pytest.raises(JellyConformanceError) as excinfo:
        StreamParameters(namespace_declarations=True)

    msg = str(excinfo.value)
    assert "Version must be between 10 and 5" in msg


def test_get_options_and_frames_delimited_only_empty() -> None:
    with pytest.raises(JellyConformanceError) as exc:
        get_options_and_frames(io.BytesIO(b"\x00\x00\x00"))
    assert "No non-empty frames found" in str(exc.value)


def test_get_options_and_frames_non_delimited_empty() -> None:
    with pytest.raises(JellyConformanceError) as exc:
        get_options_and_frames(io.BytesIO(b""))
    assert "only contains an empty frame" in str(exc.value)


def test_get_options_and_frames_non_delimited_success_only_return() -> None:
    opts_msg = jelly.RdfStreamOptions(
        stream_name="test",
        physical_type=jelly.PHYSICAL_STREAM_TYPE_TRIPLES,
        generalized_statements=False,
        rdf_star=False,
        max_name_table_size=8,
        max_prefix_table_size=8,
        max_datatype_table_size=8,
        logical_type=jelly.LOGICAL_STREAM_TYPE_FLAT_TRIPLES,
        version=1,
    )
    frame = jelly.RdfStreamFrame(rows=[jelly.RdfStreamRow(options=opts_msg)])
    data = frame.SerializeToString(deterministic=True)

    options, frames_iter = get_options_and_frames(io.BytesIO(data))

    assert options.stream_types.physical_type == jelly.PHYSICAL_STREAM_TYPE_TRIPLES
    assert options.stream_types.logical_type == jelly.LOGICAL_STREAM_TYPE_FLAT_TRIPLES

    frames = list(frames_iter)
    assert len(frames) == 1
    assert isinstance(frames[0], jelly.RdfStreamFrame)
    assert frames[0].rows[0].options == opts_msg
