# python-usajobsapi

A Python wrapper for the [USAJOBS REST API](https://developer.usajobs.gov/). The package aims to provide a simple SDK interface for discovering and querying job postings from USAJOBS using Python.

## Features

- Lightweight client for the USAJOBS REST API endpoints
- Leverage type hinting and validation for endpoint parameters
- Map endpoint results to Python objects

### Supported Endpoints

This package primarily aims to support searching and retrieval of active and past job listings. However, updates are planned to add support for all other documented endpoints.

Currently, the following endpoints are supported:

- [Job Search API](https://developer.usajobs.gov/api-reference/get-api-search) (`/api/Search`)

## Installation

### From PyPI

```bash
pip install python-usajobsapi
```

or, with [astral-uv](https://docs.astral.sh/uv/):

```bash
uv add python-usajobsapi
```

### From source

```bash
git clone https://github.com/your-username/python-usajobsapi.git
cd python-usajobsapi
pip install .
```

## Usage

Register for a USAJOBS API key and set a valid User-Agent before making requests.

```python
from usajobsapi import USAJobsClient

client = USAJobsClient(auth_user="name@example.com", auth_key="YOUR_API_KEY")
results = client.search_jobs(keyword="data scientist", location_names=["Atlanta", "Georgia"]).search_result.jobs()
for job in results:
    print(job.position_title)
```

## Contributing

Contributions are welcome! To get started:

1. Fork the repository and create a new branch.
2. Create a virtual environment and install development dependencies.
3. Run the test suite with `pytest` and ensure all tests pass.
4. Submit a pull request describing your changes.

Please open an issue first for major changes to discuss your proposal.

## License

Distributed under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html). See [LICENSE](LICENSE) for details.

## Project Status

This project is under active development and its API may change. Changes to the [USAJOBS REST API documentation](https://developer.usajobs.gov/) shall be monitored and incorporated into this project in a reasonable amount of time. Feedback and ideas are appreciated.

## Contact

Questions or issues? Please open an issue on the repository's issue tracker.
