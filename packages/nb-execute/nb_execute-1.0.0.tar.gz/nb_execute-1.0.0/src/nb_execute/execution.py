import os, sys, time, tempfile, nbformat, asyncio
from nbclient import NotebookClient
from nbformat.v4 import new_output as NO
from jupyter_client import KernelManager

# Fix windows warning
if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# -------------------------------------------------------------------
# Execute Jupyter Notebooks, stopping on first error but still saving
# Like "jupyter execute" except that either (1. doesn't save on error) or (2. continues running after error)

def nb_execute(file: str):
    if not file.endswith(".ipynb"):
        file += ".ipynb"
    file = os.path.abspath(file)

    with open(file, encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)

    client = NotebookClient(nb, kernel_name="python3", timeout=None, stop_on_error=True)

    print(f'running...', end='')
    try:
        asyncio.run(client.async_execute())
    except Exception:
        # ignore any execution error but still save outputs/errors into the notebook
        pass
    finally:
        with open(file, "w", encoding="utf-8") as f:
            nbformat.write(nb, f)
        print(f'done')

    return file

# -------------------------------------------------------------------
# Execute Jupyter Notebooks with live updates, but without needing an active GUI/Client

def _atomic_write(nb, path):
    if sys.platform.startswith("win"):
        # Just overwrite to avoid PermissionError
        with open(path, "w", encoding="utf-8") as f:
            nbformat.write(nb, f)
            f.flush()
            os.fsync(f.fileno())

    else:
        d = os.path.dirname(os.path.abspath(path)) or "."
        fd, tmp = tempfile.mkstemp(dir=d, prefix=".nbtmp_", suffix=".ipynb")
        os.close(fd)
        with open(tmp, "w", encoding="utf-8") as f:
            nbformat.write(nb, f)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, path)


def nb_execute_live(nb_path: str, save_every: float = 1.0) -> str:
    """Execute notebook at nb_path, streaming outputs back to the file live."""
    nb_path = os.path.abspath(nb_path)
    with open(nb_path, encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)

    nb_dir = os.path.dirname(nb_path) or "."
    orig_cwd = os.getcwd()
    os.chdir(nb_dir)

    km = KernelManager(kernel_name="python3")
    km.start_kernel()
    kc = km.client()
    kc.start_channels()

    print(f'running...', end='')
    try:
        for cell in nb.cells:
            if cell.cell_type != "code":
                continue
            cell.outputs, cell.execution_count = [], None
            msg_id = kc.execute(cell.source, store_history=True, allow_stdin=False, stop_on_error=False)
            got_reply = saw_idle = False
            last_save = 0.0
            error_seen = False

            while True:
                # 1) IOPub: read one message (short timeout so we can save periodically)
                msg = None
                try:
                    msg = kc.get_iopub_msg(timeout=max(0.1, min(1.0, save_every)))
                except Exception:
                    pass
                if msg and msg.get("parent_header", {}).get("msg_id") == msg_id:
                    t = msg["header"]["msg_type"]
                    c = msg["content"]
                    if t == "status" and c.get("execution_state") == "idle":
                        saw_idle = True
                    elif t == "execute_input":
                        cell.execution_count = c.get("execution_count", cell.execution_count)
                    elif t == "stream":
                        if cell.outputs and cell.outputs[-1].output_type == "stream" and cell.outputs[-1].name == c["name"]:
                            cell.outputs[-1].text += c.get("text", "")
                        else:
                            cell.outputs.append(NO(output_type="stream", name=c["name"], text=c.get("text", "")))
                    elif t in ("display_data", "execute_result"):
                        cell.outputs.append(NO(
                            output_type=t,
                            data=c.get("data", {}),
                            metadata=c.get("metadata", {}),
                            execution_count=c.get("execution_count"),
                        ))
                    elif t == "update_display_data":
                        cell.outputs.append(NO(
                            output_type="update_display_data",
                            data=c.get("data", {}),
                            metadata=c.get("metadata", {}),
                        ))
                    elif t == "error":
                        cell.outputs.append(NO(
                            output_type="error",
                            ename=c.get("ename", ""),
                            evalue=c.get("evalue", ""),
                            traceback=c.get("traceback", []),
                        ))
                        error_seen = True
                        break
                    elif t == "clear_output" and not c.get("wait", False):
                        cell.outputs = []

                # 2) Shell: drain execute_reply if present
                try:
                    while True:
                        rep = kc.get_shell_msg(timeout=0.0)
                        if (
                            rep.get("parent_header", {}).get("msg_id") == msg_id
                            and rep["header"]["msg_type"] == "execute_reply"
                        ):
                            got_reply = True
                except Exception:
                    pass

                # 3) Periodic save
                now = time.time()
                if now - last_save >= save_every:
                    _atomic_write(nb, nb_path)
                    last_save = now

                # 4) Done for this cell?
                if got_reply and saw_idle:
                    break

            _atomic_write(nb, nb_path)  # final save per cell
            if error_seen:
                return nb_path  # stop entire run on first error

    finally:
        try:
            kc.stop_channels()
        except Exception:
            pass
        try:
            km.shutdown_kernel(now=True)
        except Exception:
            pass
        _atomic_write(nb, nb_path)
        os.chdir(orig_cwd)
        print('done')

    return nb_path
