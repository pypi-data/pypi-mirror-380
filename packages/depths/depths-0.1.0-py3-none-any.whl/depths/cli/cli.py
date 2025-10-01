# ======================================================================
# (A) FILE PATH & IMPORT PATH
# depths/cli/cli.py  →  import path: depths.cli.cli
# ======================================================================

# ======================================================================
# (B) FILE OVERVIEW (concept & significance in v0.1.0)
# Typer-based command-line interface to manage the OTLP/HTTP server:
#   • init   → create a new instance layout and baseline configs
#   • start  → run uvicorn serving depths.cli.app:app (foreground/background)
#   • stop   → terminate a background server via stored PID
#
# The CLI is the operational companion to the service: it standardizes
# instance paths, boot flags, and safe shutdown across platforms.
# ======================================================================

# ======================================================================
# (C) IMPORTS & GLOBALS (what & why)
# typer                         → ergonomic CLI commands/options
# os, sys, subprocess, signal   → process control & environment
# Path                          → instance directories & pid/log files
#
# Globals:
#   app                 → Typer root application
#   DEFAULT_HOST/PORT   → sensible defaults for OTLP/HTTP binding
# Helper:
#   _instance_paths()   → canonical layout of per-instance paths
# ======================================================================

from __future__ import annotations

import os
import signal
import subprocess
import sys
from pathlib import Path

import typer

app = typer.Typer(help="depths CLI")

DEFAULT_HOST = "0.0.0.0"
DEFAULT_PORT = 4318 


def _instance_paths(instance_id: str, instance_dir: Path) -> dict:
    """
    Compute canonical paths for an instance (root, config dir, pid file, log file).

    Overview (v0.1.0 role):
        Normalizes how the CLI and server agree on where to read/write artifacts.
        Ensures the configs directory exists.

    Args:
        instance_id: Logical instance identifier.
        instance_dir: Base directory containing all instances.

    Returns:
        Dict with keys: {'root', 'cfg', 'pid', 'log'}.
    """
    # --- DEVELOPER NOTES -------------------------------------------------
    # - Keep names stable; app.py reads DEPTHS_INSTANCE_* env vars set by 'start'.

    inst_root = instance_dir / instance_id
    cfg_dir = inst_root / "configs"
    cfg_dir.mkdir(parents=True, exist_ok=True)
    pid_file = cfg_dir / "server.pid"
    log_file = inst_root / "server.log"
    return {"root": inst_root, "cfg": cfg_dir, "pid": pid_file, "log": log_file}


@app.command("init")
def init(
    instance_id: str = typer.Option("default", "--instance-id", "-I", help="Unique ID for this depths instance"),
    instance_dir: Path = typer.Option(Path("./depths_data"), "--dir", "-D", help="Root directory to store local data"),
):
    """
    Initialize a new Depths instance on disk.

    Overview (v0.1.0 role):
        Creates the directory skeleton and baseline configs by instantiating a
        DepthsLogger once (which lays out configs/ and index/). S3 config is
        optional; local-only is supported.

    Args:
        instance_id: Name for the instance root folder.
        instance_dir: Parent directory under which the instance folder is created.

    Returns:
        None (prints status and tips; exits with non-zero on pre-existence).
    """
    # --- DEVELOPER NOTES -------------------------------------------------
    # - Mirrors DepthsLogger's on-disk structure; does not start the server.
    # - S3Config.from_env() may fail; we swallow to allow local bootstrap.

    from depths.core.config import S3Config, DepthsLoggerOptions
    from depths.core.logger import DepthsLogger

    if (instance_dir / instance_id).exists():
        typer.echo(f"Instance '{instance_id}' already exists at {(instance_dir / instance_id)}", err=True)
        raise typer.Exit(code=1)
    
    _instance_paths(instance_id, instance_dir)  

    s3 = None
    try:
        s3 = S3Config.from_env()
    except Exception:
        s3 = None
    DepthsLogger(instance_id=instance_id, instance_dir=str(instance_dir), s3=s3, options=DepthsLoggerOptions())
    typer.echo(f"Initialized depths instance '{instance_id}' at {(instance_dir / instance_id)}")
    typer.echo("Tip: set your S3 env vars if you want S3 persistence.")


@app.command("start")
def start(
    instance_id: str = typer.Option("default", "--instance-id","-I", help="Instance to start"),
    instance_dir: Path = typer.Option(Path("./depths_data"), "--dir","-D", help="Root directory for instance data"),
    host: str = typer.Option(DEFAULT_HOST, "--host","-H", help="Bind host for OTLP/HTTP"),
    port: int = typer.Option(DEFAULT_PORT, "--port","-P", help="Bind port for OTLP/HTTP (4318 by spec)"),
    reload: bool = typer.Option(False, "--reload", "-R", help="Auto-reload server on code changes"),
    foreground: bool = typer.Option(False, "--foreground", "-F", help="Run in foreground and show Uvicorn TUI logs"),
):
    """
    Start the OTLP/HTTP server (depths.cli.app:app) via uvicorn.

    Overview (v0.1.0 role):
        Offers two modes:
          • Foreground: run uvicorn in-process (best signals; interactive logs).
          • Background: daemonize uvicorn, write pidfile, and append logs.

    Args:
        instance_id: Instance to serve.
        instance_dir: Parent directory containing the instance folder.
        host: Bind address (default 0.0.0.0).
        port: Bind port (OTLP/HTTP default 4318).
        reload: Enable code reload (only supported with --foreground).
        foreground: Do not daemonize; run in the current terminal.

    Returns:
        None (prints process info and where logs live).

    Raises:
        typer.Exit: On invalid state (missing instance, existing pidfile, bad flags).
    """
    # --- DEVELOPER NOTES -------------------------------------------------
    # - For background mode, we write DEPTHS_INSTANCE_* env so the app module
    #   can discover the intended instance from within the uvicorn process.
    # - We attempt to pick the serving PID (child) when possible (psutil).
    # - Reload spawns children; in background it confuses PID tracking—hence disallowed.
    # - PID selection logic: Most recent child is typically the server

    instance_dir = instance_dir.resolve()

    if not (instance_dir / instance_id).exists():
        typer.echo(
            f"Instance '{instance_id}' does not exist at {(instance_dir / instance_id)}. "
            f"Run 'depths init -I {instance_id}' first.",
            err=True,
        )
        raise typer.Exit(code=1)

    paths = _instance_paths(instance_id, instance_dir)

    os.environ["DEPTHS_INSTANCE_ID"] = instance_id
    os.environ["DEPTHS_INSTANCE_DIR"] = str(instance_dir)

    if foreground:
        import uvicorn
        typer.echo(f"Starting depths server for '{instance_id}' on http://{host}:{port} (foreground)...")
        uvicorn.run(
            "depths.cli.app:app",
            host=host,
            port=port,
            log_level="info",
            reload=reload,
        )
        return

    if reload:
        typer.echo("`--reload` is only supported with `--foreground` to ensure correct PID handling.", err=True)
        raise typer.Exit(code=2)

    if paths["pid"].exists():
        typer.echo(f"Server already running (pid file {paths['pid']}).", err=True)
        raise typer.Exit(code=1)

    env = os.environ.copy()
    cmd = [
        sys.executable, "-m", "uvicorn", "depths.cli.app:app",
        "--host", host, "--port", str(port),
        "--log-level", "info",
    ]

    logf = open(paths["log"], "a", encoding="utf-8")
    proc = subprocess.Popen(cmd, env=env, stdout=logf, stderr=logf, close_fds=True)

    serving_pid = proc.pid
    try:
        import time
        time.sleep(0.35)  
        try:
            import psutil  
            p = psutil.Process(proc.pid)
            kids = p.children(recursive=True)
            if kids:
                serving_pid = kids[-1].pid  
        except Exception:
            pass
    finally:
        paths["pid"].write_text(str(serving_pid))

    typer.echo(f"Started depths server for '{instance_id}' on http://{host}:{port} (pid={serving_pid}). Logs: {paths['log']}")

@app.command("stop")
def stop(
    instance_id: str = typer.Option("default", "--instance-id", "-I", help="Instance to stop"),
    instance_dir: Path = typer.Option(Path("./depths_data"), "--dir", "-D", help="Root directory for instance data"),
    force: bool = typer.Option(False, "--force", "-F", help="Force kill if graceful stop fails"),
):
    """
    Stop a background server using the stored PID (and children when possible).

    Overview (v0.1.0 role):
        Reads the pidfile emitted by 'start', sends terminate/kill as needed,
        and cleans up the pidfile.

    Args:
        instance_id: Instance whose server should be stopped.
        instance_dir: Parent directory containing the instance.
        force: Escalate to SIGKILL (where available) on failure.

    Returns:
        None (prints result; exits non-zero on failures).

    Raises:
        typer.Exit: On missing/invalid pidfile or kill errors.
    """
    # --- DEVELOPER NOTES -------------------------------------------------
    # - Prefers psutil to terminate the whole process tree (children before parent).
    # - Falls back to os.kill when psutil isn't available (best-effort).
    # - Always attempt to unlink the pidfile at the end.

    instance_dir = instance_dir.resolve()
    paths = _instance_paths(instance_id, instance_dir)

    if not paths["pid"].exists():
        typer.echo("No pid file found; server not running?", err=True)
        raise typer.Exit(code=1)

    try:
        pid = int(paths["pid"].read_text().strip())
    except Exception:
        typer.echo("Invalid pid file.", err=True)
        raise typer.Exit(code=1)

    try:
        try:
            import psutil
            procs = []
            try:
                p = psutil.Process(pid)
                procs.append(p)
                procs.extend(p.children(recursive=True))
            except psutil.NoSuchProcess:
                typer.echo("Process not found; cleaning up pid file.")
            else:
                for pr in reversed(procs): 
                    try:
                        pr.terminate()
                    except psutil.NoSuchProcess:
                        pass
                gone, alive = psutil.wait_procs(procs, timeout=3.0)
                if alive:
                    for pr in alive:
                        try:
                            pr.kill()
                        except psutil.NoSuchProcess:
                            pass
        except ImportError:
            try:
                os.kill(pid, signal.SIGTERM)
            except ProcessLookupError:
                typer.echo("Process not found; cleaning up pid file.")
            except Exception as e:
                if force:
                    try:
                        os.kill(pid, signal.SIGKILL if hasattr(signal, "SIGKILL") else signal.SIGTERM)
                    except Exception as e2:
                        typer.echo(f"Force kill failed: {e2}", err=True)
                        raise typer.Exit(code=1)
                else:
                    typer.echo(f"Failed to stop process: {e}", err=True)
                    raise typer.Exit(code=1)
    finally:
        try:
            paths["pid"].unlink(missing_ok=True)
        except Exception:
            pass

    typer.echo(f"Stopped depths server for '{instance_id}'.")


if __name__ == "__main__":
    app()
