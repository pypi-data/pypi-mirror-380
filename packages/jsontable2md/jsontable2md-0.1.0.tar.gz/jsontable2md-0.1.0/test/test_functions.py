#!/usr/bin/env python3
"""JsonTable2Md 関数テスト"""

import json
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from jsontable2md import (
    convert_file,
    InputFileError,
    InvalidJsonError,
)
from jsontable2md.json_converter import JSONTableConverter

FIXTURE_DIR = Path(__file__).parent
TEST_OUTPUT_FILE = FIXTURE_DIR / "_converted_test.json"
MISSING_INPUT_FILE = FIXTURE_DIR / "_missing_input.json"
MISSING_OUTPUT_FILE = FIXTURE_DIR / "_missing_output.json"
SAMPLE_OUTPUT_FILE = FIXTURE_DIR / "sample_output.json"


def generate_sample_output() -> Path:
    """Generate sample output JSON within the test directory."""
    input_file = FIXTURE_DIR / "sample_input.json"
    output_file = FIXTURE_DIR / "sample_output.json"

    converted = convert_file(input_file, output_file, overwrite=True)
    if not isinstance(converted, dict):
        raise RuntimeError("convert_file should return converted dict")

    return output_file


def _check_convert_file_generates_expected_output() -> None:
    input_file = FIXTURE_DIR / "sample_input.json"
    output_file = TEST_OUTPUT_FILE

    if output_file.exists():
        output_file.unlink()

    try:
        _ensure_sample_output_exists()
        result_dict = convert_file(input_file, output_file)
        if not isinstance(result_dict, dict):
            raise AssertionError("convert_file did not return dict")

        expected = json.loads(SAMPLE_OUTPUT_FILE.read_text(encoding="utf-8"))
        actual = json.loads(output_file.read_text(encoding="utf-8"))

        if actual != expected:
            raise AssertionError("Converted JSON does not match expected sample output")
    finally:
        if output_file.exists():
            output_file.unlink()


def _check_convert_file_missing_input() -> None:
    missing_file = MISSING_INPUT_FILE
    output_file = MISSING_OUTPUT_FILE

    if missing_file.exists():
        missing_file.unlink()
    if output_file.exists():
        output_file.unlink()

    try:
        try:
            convert_file(missing_file, output_file)
        except InputFileError:
            pass  # expected
        else:
            raise AssertionError("InputFileError was not raised for missing file")
    finally:
        if missing_file.exists():
            missing_file.unlink()
        if output_file.exists():
            output_file.unlink()


def _check_json_table_converter_matches_sample_output() -> None:
    converter = JSONTableConverter()
    input_payload = json.loads((FIXTURE_DIR / "sample_input.json").read_text(encoding="utf-8"))
    _ensure_sample_output_exists()
    expected_payload = json.loads(SAMPLE_OUTPUT_FILE.read_text(encoding="utf-8"))

    converted = converter.convert_json_data(input_payload)
    if converted != expected_payload:
        raise AssertionError("JSONTableConverter result does not match expected output")


def _ensure_sample_output_exists() -> None:
    if not SAMPLE_OUTPUT_FILE.exists():
        generate_sample_output()


def _check_overwrite_false_behavior() -> None:
    """既存出力ファイルがある状態で overwrite=False を指定した場合に OutputFileError になること。"""
    from jsontable2md import OutputFileError

    input_file = FIXTURE_DIR / "sample_input.json"
    output_file = FIXTURE_DIR / "_exists_output.json"

    # 事前にファイル生成
    output_file.write_text("{}", encoding="utf-8")
    try:
        try:
            convert_file(input_file, output_file, overwrite=False)
        except OutputFileError:
            pass  # expected
        else:
            raise AssertionError("OutputFileError not raised when overwrite=False and file exists")
    finally:
        if output_file.exists():
            output_file.unlink()


def run_all_checks() -> None:
    tests = [
        ("convert_file_generates_expected_output", _check_convert_file_generates_expected_output),
        ("convert_file_missing_input", _check_convert_file_missing_input),
        ("json_table_converter_matches_sample_output", _check_json_table_converter_matches_sample_output),
        ("convert_file_overwrite_false", _check_overwrite_false_behavior),
    ]

    for name, test_func in tests:
        test_func()
        print(f"[OK] {name}")


if __name__ == "__main__":
    run_all_checks()
    output_path = generate_sample_output()
    print(f"Sample output generated: {output_path}")


