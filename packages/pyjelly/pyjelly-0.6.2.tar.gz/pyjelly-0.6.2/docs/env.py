"""
MkDocs macros plugin configuration for pyjelly documentation.

Defines custom macros used in Markdown docs:
- `python_version()`: current package version (from TAG env or git)
- `proto_version()`: current Jelly proto version (from PROTO_TAG or git)
- `git_link(file)`: deep link to source on GitHub
- `proto_link(page)`: link to W3ID Jelly proto docs
- `python_package_version[_minor]`: current PyPI version(s)

These macros are used in versioned builds and cross-version linking.

See: https://mkdocs-macros-plugin.readthedocs.io/en/latest/
"""

# ruff: noqa: PGH004
# ruff: noqa
import os
import subprocess


def define_env(env):
    # Override for use in local development
    proto_tag_raw = os.environ.get("PROTO_TAG", None)
    if proto_tag_raw is not None:
        print(f"PROTO_TAG env var is set to {proto_tag_raw}")
    else:
        try:
            proto_tag_raw = subprocess.check_output(
                ["git", "describe", "--tags"],
                cwd="submodules/protobuf",
                encoding="utf-8",
            ).strip()
        except subprocess.CalledProcessError as e:
            print("Failed to call git: ", e.returncode, e.stderr)
            raise

    try:
        python_tag_raw = subprocess.check_output(
            ["git", "describe", "--tags"], encoding="utf-8"
        ).strip()
    except subprocess.CalledProcessError as e:
        print("Failed to call git: ", e.returncode, e.stderr)
        raise

    tag_env_var = os.environ.get("TAG", "dev")
    if tag_env_var == "dev":
        print("Warning: TAG env var is not set, using dev as default")

    def proto_tag():
        if proto_tag_raw.count("-") > 1:
            if python_version() == "dev":
                print(
                    f"Warning: proto tag ({proto_tag_raw}) contains more than one hyphen, using dev instead"
                )
                return "dev"
            new_tag = "-".join(proto_tag_raw.split("-")[:2])
            print(
                f"Warning: proto tag ({proto_tag_raw}) contains more than one hyphen. Using {new_tag} instead. To fix this, you must update the protobuf_shared submodule to some stable tag."
            )
            return new_tag
        return proto_tag_raw

    @env.macro
    def python_version():
        if tag_env_var == "dev":
            return tag_env_var
        if tag_env_var == "main":
            return "dev"
        return tag_env_var.replace("v", "")

    @env.macro
    def python_package_version():
        """Returns the current python package version, as published to PyPI."""
        v = python_version()
        if v == "dev":
            return python_tag_raw.split("-")[0].replace("v", "")
        return v

    @env.macro
    def python_package_version_minor():
        """Return the current MINOR python package version, as published to PyPI."""
        v = python_package_version()
        return ".".join(v.split(".")[:2]) + ".x"

    @env.macro
    def git_tag():
        return os.environ.get("TAG", "main")

    @env.macro
    def git_link(file: str):
        tag = git_tag()
        return f"https://github.com/Jelly-RDF/pyjelly/blob/{tag}/{file}"

    @env.macro
    def proto_version():
        if python_version() == "dev":
            return "dev"
        tag = proto_tag()
        if "-" in tag:
            tag = tag[: tag.rindex("-")]
        return tag.replace("v", "")

    @env.macro
    def proto_link(page: str = ""):
        version = proto_version()
        return f"https://w3id.org/jelly/{version}/{page}"

    @env.macro
    def code_example(file_name, start=None, end=None):
        try:
            lines = open(f"examples/{file_name}").read().splitlines(keepends=True)
        except:
            return "```python\n\n```"
        start_index = 0 if not start or start < 1 else start - 1
        end_index = len(lines) if not end or end < 1 else end
        if start_index < 0:
            start_index = 0
        if end_index > len(lines):
            end_index = len(lines)
        if start_index >= end_index:
            return "```python\n\n```"
        return "```python\n" + "".join(lines[start_index:end_index]) + "```"

    @env.macro
    def code_example_box(file_name):
        name = f"examples/{file_name}"
        with open(name, "r") as f:
            code = f.read()
        code = code.replace("\n", "\n    ")
        return f"""
??? example "Example: {file_name} (click to expand)"

    **[:octicons-code-24: Source code on GitHub]({git_link(name)})**

    ```python title="{file_name}" linenums="1"
    {code}
    ```
"""

    @env.macro
    def snippet_raw_lines(path, start, end):
        with open(path, "r") as f:
            lines = f.readlines()
        if start < 1:
            start = 1
        if end > len(lines):
            end = len(lines)
        if start > end:
            return (
                f"Error: invalid range {start}-{end} for file with {len(lines)} lines."
            )
        snippet = "".join(lines[start - 1 : end])
        return snippet

    @env.macro
    def snippet_admonition(
        path, start, end, title="Snippet", expanded=True, kind="note"
    ):
        marker = "???+" if expanded else "???"
        snippet = snippet_raw_lines(path, start, end)

        if snippet.startswith("Error:"):
            inner = f"""```text
{snippet}
```"""
        else:
            inner = f"```python\n{snippet}```"
        indented = "\n".join(
            ("    " + line) if line.strip() != "" else "" for line in inner.splitlines()
        )
        return f'{marker} {kind} "{title}"\n{indented}'

    def transform_nav_item(item):
        if list(item.values())[0] == "https://w3id.org/jelly/":
            return {list(item.keys())[0]: proto_link("")}
        return item

    env.conf["nav"] = [transform_nav_item(item) for item in env.conf["nav"]]
