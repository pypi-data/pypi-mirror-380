import asyncio
from agi_env import AgiEnv
from flight import Flight  # assuming your Flight class is here
from flight.flight_args import FlightArgs
from datetime import date
from pathlib import Path

async def main():
    env = AgiEnv(active_app=Path(__file__).expanduser().parents[1], verbose=True)

    # Instantiate Flight with your parameters
    flight = Flight(
        env=env,
        args=FlightArgs(
            data_source="file",
            data_uri="data/flight/dataset",
            files="csv/*",
            nfile=1,
            nskip=0,
            nread=0,
            sampling_rate=10.0,
            datemin=date(2020, 1, 1),
            datemax=date(2021, 1, 1),
            output_format="parquet",
        ),
    )

    # Example list of workers to pass to build_distribution
    workers = {'worker1':2, 'worker2':3}

    # Call build_distribution (await if async)
    result = flight.build_distribution(workers)

    print(result)

if __name__ == '__main__':
    asyncio.run(main())
