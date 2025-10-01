import socket
import multiprocessing as mp
import time
import typer
from typing_extensions import Annotated
from m61.common import setup_logger, CHUNK_SIZE, get_free_memory
from m61.exceptions import MemoryErrorDetected

logger = setup_logger("m61-client")
app = typer.Typer()


def client_worker(server_ip, server_port, total_bytes=None, duration_sec=None, queue=None):
    """Worker process that connects to server and sends data"""
    total_sent = 0
    start_time = time.time()
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((server_ip, server_port))
            logger.info(f"[{mp.current_process().name}] Connected to {server_ip}:{server_port}")

            payload = b"x" * CHUNK_SIZE
            while True:
                if total_bytes and total_sent >= total_bytes:
                    break
                if duration_sec and (time.time() - start_time) >= duration_sec:
                    break

                free_mem = get_free_memory()
                if free_mem and free_mem < CHUNK_SIZE * 2:
                    raise MemoryErrorDetected("Low memory detected, stopping client worker")

                s.sendall(payload)
                total_sent += len(payload)

                if total_sent % (10 * 1024**3) == 0:  # every 10 GiB
                    logger.info(f"[{mp.current_process().name}] Sent {total_sent / (1024**3):.2f} GiB")

    except Exception as e:
        logger.error(f"[{mp.current_process().name}] Error: {e}")

    if queue:
        queue.put(total_sent)


@app.command()
def main(
    server_ip: Annotated[str, typer.Option(help="Server IP address")],
    server_port: Annotated[int, typer.Option(help="Server port")] = 5000,
    size_gib: Annotated[int, typer.Option(help="Total size to send in GiB")] = None,
    duration_sec: Annotated[int, typer.Option(help="Duration to send data (seconds)")] = None,
    workers: Annotated[int, typer.Option(help="Number of parallel client workers")] = 1,
):
    """CLI entrypoint for m61-client"""
    try:
        if not size_gib and not duration_sec:
            print("You must specify either --size-gib or --duration-sec")
            raise typer.Exit(code=1)

        total_bytes = size_gib * (1024**3) if size_gib else None
        queue = mp.Queue()
        processes = []

        for _ in range(workers):
            p = mp.Process(
                target=client_worker,
                args=(server_ip, server_port, total_bytes, duration_sec, queue),
                daemon=True,
            )
            p.start()
            processes.append(p)

        total_sent = 0
        for p in processes:
            p.join()
        while not queue.empty():
            total_sent += queue.get()

        logger.info(f"Total sent across all workers: {total_sent / (1024**3):.2f} GiB")

    except Exception as e:
        logger.error(f"Client error: {e}")


if __name__ == "__main__":
    app()
