import asyncio
import json
import signal
import sys
from typing import List


def cli_worker():
    import argparse

    parser = argparse.ArgumentParser(description='NatsWork Worker')
    parser.add_argument('--queues', default='default', help='Comma-separated queues')
    parser.add_argument('--concurrency', type=int, default=10, help='Workers per queue')
    parser.add_argument('--servers', default='nats://localhost:4222', help='NATS servers')

    args = parser.parse_args()

    queues = [q.strip() for q in args.queues.split(',')]
    servers = [s.strip() for s in args.servers.split(',')]

    print("Starting NatsWork worker...")
    print(f"Queues: {queues}")
    print(f"Concurrency: {args.concurrency}")
    print(f"Servers: {servers}")

    asyncio.run(_run_worker(queues, args.concurrency, servers))


async def _run_worker(queues: List[str], concurrency: int, servers: List[str]):
    from natswork_client.nats_client import NatsConnectionManager

    try:
        from natswork_server.nats_client import JetStreamClient, StreamManager
        from natswork_server.worker_pool import WorkerPoolManager
    except ImportError:
        print("Error: natswork-server not installed. Install with: pip install natswork-server")
        sys.exit(1)

    connection_manager = NatsConnectionManager(servers)
    await connection_manager.connect()

    js_client = JetStreamClient(connection_manager)
    stream_manager = StreamManager(js_client)

    for queue in queues:
        await stream_manager.ensure_job_stream(queue)

    worker_manager = WorkerPoolManager(connection_manager)

    for queue in queues:
        await worker_manager.start_pool(queue, concurrency)
        print(f"Started {concurrency} workers for queue '{queue}'")

    shutdown_event = asyncio.Event()

    def signal_handler(signum, frame):
        print(f"\nReceived signal {signum}, shutting down...")
        shutdown_event.set()

    for sig in [signal.SIGTERM, signal.SIGINT]:
        signal.signal(sig, signal_handler)

    print("Worker ready. Press Ctrl+C to stop.")

    try:
        await shutdown_event.wait()
    finally:
        print("Shutting down...")
        await worker_manager.shutdown()
        await connection_manager.disconnect()
        print("Stopped")


def cli_dispatch():
    import argparse

    parser = argparse.ArgumentParser(description='Dispatch NatsWork Job')
    parser.add_argument('job_class', help='Job class name')
    parser.add_argument('--args', help='JSON arguments')
    parser.add_argument('--sync', action='store_true', help='Wait for result')
    parser.add_argument('--timeout', type=int, default=30, help='Sync timeout')
    parser.add_argument('--servers', default='nats://localhost:4222', help='NATS servers')

    args = parser.parse_args()

    asyncio.run(_dispatch_job(args))


async def _dispatch_job(args):
    from natswork_client.client import NatsWorkClient
    from natswork_client.job import JobRegistry

    job_class = JobRegistry.get_job_class(args.job_class)
    if not job_class:
        print(f"Error: Job class not found: {args.job_class}", file=sys.stderr)
        sys.exit(1)

    job_args = []
    job_kwargs = {}
    if args.args:
        parsed = json.loads(args.args)
        if isinstance(parsed, list):
            job_args = parsed
        elif isinstance(parsed, dict):
            job_kwargs = parsed

    servers = [s.strip() for s in args.servers.split(',')]
    client = NatsWorkClient(servers=servers)

    try:
        await client.connect()

        if args.sync:
            result = await client.perform_sync(
                job_class, *job_args, timeout=args.timeout, **job_kwargs
            )
            print(f"Result: {result}")
        else:
            job_id = await client.perform_async(job_class, *job_args, **job_kwargs)
            print(f"Job dispatched: {job_id}")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    finally:
        await client.disconnect()


def cli_list_jobs():
    from natswork_client.job import JobRegistry

    jobs = JobRegistry.list_all_jobs()

    if not jobs:
        print("No jobs registered")
        return

    print("Registered Jobs:")
    print("-" * 60)

    for job_name, config in jobs.items():
        print(f"Job: {job_name}")
        print(f"  Queue: {config.queue}")
        print(f"  Retries: {config.retries}")
        print(f"  Timeout: {config.timeout}s")
        print()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        command = sys.argv[1]
        sys.argv = sys.argv[1:]

        if command == 'worker':
            cli_worker()
        elif command == 'dispatch':
            cli_dispatch()
        elif command == 'list-jobs':
            cli_list_jobs()
        else:
            print(f"Unknown command: {command}")
            print("Available commands: worker, dispatch, list-jobs")
            sys.exit(1)
    else:
        print("Usage: python -m natswork_client.cli <command>")
        print("Commands: worker, dispatch, list-jobs")
        sys.exit(1)
