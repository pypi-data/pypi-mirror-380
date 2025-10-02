import re
from pathlib import Path

import pytest
from rich.style import Style

from tuitorial import Focus, ImageStep, Step
from tuitorial.parse_yaml import (
    InvalidYamlError,
    _parse_chapter,
    _parse_focus,
    _parse_step,
    parse_yaml_config,
)
from tuitorial.widgets import _BetweenTuple, _RangeTuple, _StartsWithTuple


@pytest.fixture
def valid_yaml_config() -> str:
    """Config string for tests."""
    return """
    chapters:
      - title: "Chapter 1"
        code: |
          print("Hello")
        steps:
          - description: "First step"
            focus:
              - type: literal
                text: "print"
                style: "bold blue"
      - title: "Bullet Points"
        type: bullet_points
        bullet_points:
          - text: "Point 1"
            extra: "Extra 1"
          - text: "Point 2"
            extra: "Extra 2"
        style: "green bold"
    """


@pytest.fixture
def invalid_yaml_config() -> str:
    """Config string for tests."""
    return """
    chapters:
      - title: "Invalid Chapter"
        steps:
          - description: "Invalid focus"
            focus:
              - type: unknown
                pattern: "test"
    """


def test_parse_valid_yaml_config(valid_yaml_config, tmp_path):
    """Test parsing a valid YAML config."""
    yaml_file = tmp_path / "config.yaml"
    yaml_file.write_text(valid_yaml_config)

    chapters, _ = parse_yaml_config(str(yaml_file))

    assert len(chapters) == 2
    assert chapters[0].title == "Chapter 1"
    assert chapters[1].title == "Bullet Points"
    assert chapters[0].steps[0].focuses[0].type.name == "LITERAL"
    assert chapters[0].steps[0].focuses[0].style == Style(bold=True, color="blue")


def test_parse_invalid_yaml_config(invalid_yaml_config: str, tmp_path: Path):
    """Test parsing a YAML config with an invalid focus type."""
    yaml_file = tmp_path / "invalid.yaml"
    yaml_file.write_text(invalid_yaml_config)

    with pytest.raises(InvalidYamlError, match="Invalid focus type: 'unknown'"):
        parse_yaml_config(str(yaml_file))


def test_parse_focus_literal():
    """Test parsing a literal focus."""
    focus_data = {"type": "literal", "text": "test", "style": "red", "word_boundary": False}
    focus = _parse_focus(focus_data)
    assert focus.type == Focus.type.LITERAL
    assert focus.pattern == "test"
    assert focus.style == Style.parse("red")


def test_parse_focus_regex():
    """Test parsing a regex focus."""
    focus_data = {"type": "regex", "pattern": ".*", "style": "yellow"}
    focus = _parse_focus(focus_data)
    assert focus.type == Focus.type.REGEX
    assert focus.pattern == re.compile(".*")
    assert focus.style == Style.parse("yellow")


def test_parse_focus_line() -> None:
    """Test parsing a line focus."""
    focus_data = {"type": "line", "line_number": 3, "style": "blue"}
    focus = _parse_focus(focus_data)
    assert focus.type == Focus.type.LINE
    assert focus.pattern == 3
    assert focus.style == Style.parse("blue")


def test_parse_focus_range() -> None:
    """Test parsing a range focus."""
    focus_data = {"type": "range", "start": 1, "end": 5, "style": "green"}
    focus = _parse_focus(focus_data)
    assert isinstance(focus.pattern, _RangeTuple)
    assert focus.type == Focus.type.RANGE
    assert focus.pattern.start == 1
    assert focus.pattern.end == 5
    assert focus.style == Style.parse("green")


def test_parse_focus_startswith() -> None:
    """Test parsing a startswith focus."""
    focus_data = {
        "type": "startswith",
        "text": "prefix",
        "style": "cyan",
        "from_start_of_line": True,
    }
    focus = _parse_focus(focus_data)
    assert isinstance(focus.pattern, _StartsWithTuple)
    assert focus.type == Focus.type.STARTSWITH
    assert focus.pattern.text == "prefix"
    assert focus.style == Style.parse("cyan")
    assert focus.pattern.from_start_of_line


def test_parse_focus_between() -> None:
    """Test parsing a between focus."""
    focus_data = {
        "type": "between",
        "start_pattern": "start",
        "end_pattern": "end",
        "style": "magenta",
        "inclusive": False,
        "multiline": False,
        "match_index": 2,
        "greedy": True,
    }
    focus = _parse_focus(focus_data)
    assert focus.type == Focus.type.BETWEEN
    assert isinstance(focus.pattern, _BetweenTuple)
    assert focus.pattern.start_pattern == "start"
    assert focus.pattern.end_pattern == "end"
    assert focus.style == Style.parse("magenta")
    assert focus.pattern.inclusive is False
    assert focus.pattern.multiline is False
    assert focus.pattern.match_index == 2
    assert focus.pattern.greedy is True


def test_parse_step_with_multiple_focus() -> None:
    """Test parsing a step with multiple focuses."""
    step_data = {
        "description": "Multiple Focus Step",
        "focus": [
            {"type": "literal", "text": "a", "style": "red"},
            {"type": "regex", "pattern": "\\d+", "style": "blue"},
        ],
    }
    step = _parse_step(step_data)
    assert isinstance(step, Step)
    assert step.description == "Multiple Focus Step"
    assert len(step.focuses) == 2
    assert step.focuses[0].type == Focus.type.LITERAL
    assert step.focuses[1].type == Focus.type.REGEX


def test_parse_chapter_with_code_file(tmp_path):
    """Test parsing a chapter with a code file."""
    code_file = tmp_path / "code.py"
    code_file.write_text('print("Code from file")')
    chapter_data = {"title": "Code File Chapter", "code_file": str(code_file), "steps": []}
    chapter = _parse_chapter(chapter_data)
    assert chapter.title == "Code File Chapter"
    assert chapter.code == 'print("Code from file")'


def test_parse_chapter_with_embedded_code():
    """Test parsing a chapter with embedded code."""
    chapter_data = {
        "title": "Embedded Code Chapter",
        "code": 'print("Embedded code")',
        "steps": [],
    }
    chapter = _parse_chapter(chapter_data)
    assert chapter.title == "Embedded Code Chapter"
    assert chapter.code == 'print("Embedded code")'


def test_parse_bullet_point_chapter():
    """Test parsing a bullet point chapter."""
    chapter_data = {
        "title": "Bullet Points",
        "type": "bullet_points",
        "bullet_points": [
            {"text": "Point 1", "extra": "Extra 1"},
            {"text": "Point 2", "extra": "Extra 2"},
            "Point 3",
        ],
        "marker": "1.",
        "style": "yellow bold",
    }
    chapter = _parse_chapter(chapter_data)
    assert chapter.title == "Bullet Points"
    assert chapter.code == "1. Point 1\n2. Point 2\n3. Point 3"  # Check generated code
    assert len(chapter.steps) == 3
    assert chapter.steps[0].description == "Extra 1"
    assert chapter.steps[1].description == "Extra 2"
    assert chapter.steps[2].description == ""


def test_parse_focus_literal_with_match_index():
    """Test parsing a literal focus with match_index."""
    focus_data = {
        "type": "literal",
        "text": "test",
        "style": "red",
        "match_index": 2,
    }
    focus = _parse_focus(focus_data)
    assert focus.type == Focus.type.LITERAL
    assert focus.pattern == "test"
    assert focus.style == Style.parse("red")
    assert focus.extra["match_index"] == 2


def test_parse_focus_literal_with_list_match_index():
    """Test parsing a literal focus with a list for match_index."""
    focus_data = {
        "type": "literal",
        "text": "test",
        "style": "red",
        "match_index": [1, 3],
    }
    focus = _parse_focus(focus_data)
    assert focus.type == Focus.type.LITERAL
    assert focus.pattern == "test"
    assert focus.style == Style.parse("red")
    assert focus.extra["match_index"] == [1, 3]


def test_parse_forcus_markdown():
    """Test parsing a markdown focus."""
    focus_data = {"type": "markdown"}
    focus = _parse_focus(focus_data)
    assert focus.type == Focus.type.MARKDOWN


def test_parse_step_with_image():
    """Test parsing a step with an image."""
    step_data = {
        "description": "Image Step",
        "image": "image.png",
        "width": 100,
        "height": 200,
        "halign": "center",
    }
    step = _parse_step(step_data)
    assert isinstance(step, ImageStep)
    assert step.description == "Image Step"
    assert step.image == "image.png"
    assert step.width == 100
    assert step.height == 200
    assert step.halign == "center"


@pytest.mark.parametrize(
    "type_",
    [
        "literal",
        "regex",
        "line",
        "range",
        "startswith",
        "between",
        "line_containing",
        "syntax",
        "markdown",
    ],
)
def test_validate_yaml(type_):
    """Test validating a YAML file."""
    with pytest.raises(InvalidYamlError, match="Invalid key 'wrong'"):
        _parse_focus({"type": type_, "wrong": "key"})


def test_validate_focus_data():
    with pytest.raises(InvalidYamlError, match="Each focus must have a 'type' key"):
        _parse_focus({"missing": "keytype"})


def test_parsing_examples():
    examples_dir = Path(__file__).parent.parent / "examples"
    for example_file in examples_dir.glob("*.yaml"):
        parse_yaml_config(example_file)


def test_validate_step_data():
    with pytest.raises(InvalidYamlError, match="Invalid key 'wrong' for Step"):
        _parse_step({"description": "Test", "wrong": "key"})
    with pytest.raises(InvalidYamlError, match="Each step must have a 'description' key"):
        _parse_step({"missing": "description"})
    with pytest.raises(InvalidYamlError, match="A step cannot have both 'image' and 'focus' keys"):
        _parse_step({"description": "Test", "image": "image.png", "focus": []})
    with pytest.raises(InvalidYamlError, match="Invalid key 'wrong_image_key' for ImageStep"):
        _parse_step({"description": "Test", "image": "", "wrong_image_key": "image.png"})


def test_validate_chapter_data():
    with pytest.raises(InvalidYamlError, match="Each chapter must have a 'title' key"):
        _parse_chapter({})
    with pytest.raises(
        InvalidYamlError,
        match="A chapter cannot have both 'code_file' and 'code' keys",
    ):
        _parse_chapter({"title": "Test", "code_file": "file.py", "code": "print('test')"})
    with pytest.raises(InvalidYamlError, match="Unknown chapter type"):
        _parse_chapter({"title": "Test", "type": "invalid_type"})
    with pytest.raises(InvalidYamlError, match="Invalid key 'invalid_key' for chapter"):
        _parse_chapter({"title": "Test", "invalid_key": "value"})
    with pytest.raises(InvalidYamlError, match="Missing 'bullet_points' key"):
        _parse_chapter({"title": "Test", "type": "bullet_points"})
    with pytest.raises(InvalidYamlError, match="Invalid 'bullet_points' format"):
        _parse_chapter({"title": "Test", "type": "bullet_points", "bullet_points": "invalid"})
    with pytest.raises(InvalidYamlError, match="Invalid key 'invalid' for bullet points chapter"):
        _parse_chapter(
            {"title": "Test", "type": "bullet_points", "bullet_points": [], "invalid": "invalid"},
        )
