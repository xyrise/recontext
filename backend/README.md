# ReconText Backend

## Usage

Simply run

```console
pip install -r requirements.txt
```

to install the dependencies, then run

```console
python -m hypercorn main:app --bind 0.0.0.0:80
```

to serve the backend API.
