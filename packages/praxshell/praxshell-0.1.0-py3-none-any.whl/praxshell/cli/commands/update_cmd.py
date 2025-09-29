import os
import shutil
import tempfile
import zipfile
import urllib.request
from pathlib import Path
import re

from praxshell.cli.utils.display import print_info, print_success, print_warning, print_error
from praxshell.config.constants import VAULT_REPO_ZIP, TRUSTED_VAULT_URLS, DEV_VAULT_PATTERNS

LOCAL_VAULT_PATH = Path(__file__).resolve().parent.parent.parent / "vault"

def get_github_zip_folder_name(zip_url: str) -> str:
    """
    Given a GitHub zip URL, returns the extracted folder name.
    Example: praxvault-main
    """
    m = re.match(r"https://github\.com/[^/]+/([^/]+)/archive/refs/heads/(.+)\.zip", zip_url)
    if m:
        repo, branch = m.groups()
        branch_folder = branch.replace("/", "-")
        return f"{repo}-{branch_folder}"
    else:
        base = zip_url.rsplit("/", 1)[-1]
        return base.replace(".zip", "")

def update_vault(merge: bool = False, vault_url: str = None):
    vault_url = vault_url or VAULT_REPO_ZIP
    print_info(f"Updating PraxVault (merge={merge}) from {vault_url}...")

    if vault_url not in TRUSTED_VAULT_URLS:
        if not any(re.match(pat, vault_url) for pat in DEV_VAULT_PATTERNS):
            try:
                confirm = input("[?] Unverified URL. Proceed? (y/n): ").strip().lower()
            except EOFError:
                confirm = "n"
            if confirm not in {"y", "yes"}:
                print_warning("Aborted vault update.")
                return

    with tempfile.TemporaryDirectory() as tmpdir:
        zip_path = Path(tmpdir) / "vault.zip"
        try:
            print_info("Fetching latest vault zip from GitHub...")
            urllib.request.urlretrieve(vault_url, zip_path)
            print_info("Download complete, extracting...")

            with zipfile.ZipFile(zip_path, "r") as zip_ref:
                zip_ref.extractall(tmpdir)

            folder_name = get_github_zip_folder_name(vault_url)
            extracted_dir = Path(tmpdir) / folder_name

            if not extracted_dir.exists():
                print_error(f"Extracted folder not found: {extracted_dir}")
                return

            if not merge:
                if LOCAL_VAULT_PATH.exists():
                    shutil.rmtree(LOCAL_VAULT_PATH)
                shutil.move(str(extracted_dir), str(LOCAL_VAULT_PATH))
                print_success(f"PraxVault updated at {LOCAL_VAULT_PATH}")
            else:
                for root, _, files in os.walk(extracted_dir):
                    rel_dir = os.path.relpath(root, extracted_dir)
                    target_dir = LOCAL_VAULT_PATH / rel_dir
                    target_dir.mkdir(parents=True, exist_ok=True)
                    for f in files:
                        src_file = Path(root) / f
                        dst_file = target_dir / f
                        if not dst_file.exists():
                            shutil.copy2(src_file, dst_file)
                            print_info(f"Added new file: {dst_file.relative_to(LOCAL_VAULT_PATH)}")
                print_success(f"PraxVault merged into {LOCAL_VAULT_PATH}")
        except Exception as e:
            print_error(f"Failed to update vault: {e}")

def handle_update(arg: str):
    tokens = arg.strip().split()
    if not tokens:
        print_info("Update PraxVault. Usage: update vault [merge]")
        return

    subcmd = tokens[0]
    merge = (len(tokens) > 1 and tokens[1] == "merge")

    if subcmd == "vault":
        update_vault(merge=merge)
    else:
        print_error(f"Unknown update target: {subcmd}")
