from pathlib import Path
from huggingface_hub import snapshot_download


def download_checkpoints(
    repo_id: str = "ByteDance/MegaTTS3",
    local_dir: str | Path | None = None,
    *,
    token: str | None = None,
    revision: str | None = None,
    use_symlinks: bool = False,
) -> Path:
    dest = Path(local_dir) if local_dir is not None else Path.cwd() / "checkpoints"
    dest.mkdir(parents=True, exist_ok=True)

    snapshot_download(
        repo_id=repo_id,
        local_dir=str(dest),
        local_dir_use_symlinks=use_symlinks,
        revision=revision,
        token=token,
    )

    return dest
