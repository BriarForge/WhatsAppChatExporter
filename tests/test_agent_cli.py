import json
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def run_module(*args):
    return subprocess.run(
        [sys.executable, "-m", "Whatsapp_Chat_Exporter", *args],
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )


def test_openclaw_manifest_outputs_machine_readable_cli_contract():
    result = run_module("openclaw", "manifest", "--json")

    assert result.returncode == 0
    assert result.stderr == ""
    manifest = json.loads(result.stdout)
    assert manifest["schema"] == "dev.openclaw.cli-manifest.v1"
    assert manifest["name"] == "whatsapp-chat-exporter"
    assert "openclaw-whatsapp-exporter" in manifest["commands"]
    assert "hermes-whatsapp-exporter" in manifest["commands"]
    assert manifest["capabilities"]["github_markdown_export"] is True
    assert manifest["automation"]["non_interactive_flags"] == ["--no-banner"]


def test_hermes_manifest_alias_outputs_same_cli_contract():
    openclaw = json.loads(run_module("openclaw", "manifest", "--json").stdout)
    hermes = json.loads(run_module("hermes", "manifest", "--json").stdout)

    assert hermes == openclaw


def test_version_flag_is_machine_readable_without_banner():
    result = run_module("--version")

    assert result.returncode == 0
    assert result.stdout.startswith("whatsapp-chat-exporter ")
    assert "████" not in result.stdout


def test_device_modes_are_mutually_exclusive_for_agent_safety():
    result = run_module("--android", "--ios", "--no-banner")

    assert result.returncode == 2
    assert "You must define only one device type" in result.stderr


def test_pyproject_exposes_openclaw_and_hermes_console_scripts():
    pyproject = (PROJECT_ROOT / "pyproject.toml").read_text(encoding="utf8")

    assert 'openclaw-whatsapp-exporter = "Whatsapp_Chat_Exporter.__main__:main"' in pyproject
    assert 'hermes-whatsapp-exporter = "Whatsapp_Chat_Exporter.__main__:main"' in pyproject
