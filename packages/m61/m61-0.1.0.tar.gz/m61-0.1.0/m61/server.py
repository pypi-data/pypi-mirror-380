import socket
import multiprocessing as mp
import time
import typer
from typing_extensions import Annotated
from m61.common import setup_logger, CHUNK_SIZE, get_free_memory
from m61.exceptions import MemoryErrorDetected

logger = setup_logger("m61-server")
app = typer.Typer()


def server_worker(conn, addr, output, queue=None):
    total_received = 0
    last_log_time = time.time()

    try:
        logger.info(f"[{mp.current_process().name}] Connection from {addr}")
        with conn, open(output, "ab") as f:
            while True:
                free_mem = get_free_memory()
                if free_mem and free_mem < CHUNK_SIZE * 2:
                    raise MemoryErrorDetected("Low memory detected, stopping server worker")

                data = conn.recv(CHUNK_SIZE)
                if not data:
                    break
                f.write(data)
                total_received += len(data)

                # 10분 단위 로그
                if time.time() - last_log_time >= 600:
                    logger.info(f"[{mp.current_process().name}] Received {total_received / (1024**3):.2f} GiB so far")
                    last_log_time = time.time()

        logger.info(f"[{mp.current_process().name}] Closed {addr}, total received={total_received / (1024**3):.2f} GiB")

    except Exception as e:
        logger.error(f"[{mp.current_process().name}] Error: {e}")

    if queue:
        queue.put(total_received)


class Server:
    def __init__(self, host, port, output, max_workers=4):
        self.host = host
        self.port = port
        self.output = output
        self.max_workers = max_workers

    def start(self):
        """Start server main loop"""
        queue = mp.Queue()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((self.host, self.port))
            s.listen(128)
            logger.info(
                f"Server listening on {self.host}:{self.port} with up to {self.max_workers} workers"
            )

            active_procs = []

            while True:
                conn, addr = s.accept()
                p = mp.Process(
                    target=server_worker,
                    args=(conn, addr, self.output, queue),
                    daemon=True,
                )
                p.start()
                active_procs.append(p)

                # cleanup old processes
                if len(active_procs) > self.max_workers * 2:
                    for proc in active_procs[: self.max_workers]:
                        proc.join(timeout=0.1)
                    active_procs = [p for p in active_procs if p.is_alive()]


@app.command()
def main(
    host: Annotated[str, typer.Option(help="Server bind IP")] = "0.0.0.0",
    port: Annotated[int, typer.Option(help="Server port")] = 5000,
    output: Annotated[str, typer.Option(help="Output file path")] = "received_data.bin",
    max_workers: Annotated[int, typer.Option(help="Maximum parallel processes")] = 4,
):
    """CLI entrypoint for m61-server"""
    try:
        server = Server(host, port, output, max_workers)
        server.start()
    except Exception as e:
        logger.error(f"Server error: {e}")


if __name__ == "__main__":
    app()
