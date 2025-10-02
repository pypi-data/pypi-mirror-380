# PyShipProto Build and Release

This directory contains the scripts for building and releasing the `pyshipproto` Python package.

## Local Development

### Requirements
- Python 3.8+
- grpcio-tools
- setuptools
- wheel

### Building Locally

1. Install dependencies:
```bash
pip install grpcio-tools setuptools wheel
```

2. Generate the package:
```bash
python generate_lib.py 2.6.3  # Replace with desired version
```

3. The built package will be in the `dist/` directory:
- `pyshipproto-2.6.3-py3-none-any.whl` - Wheel distribution
- `pyshipproto-2.6.3.tar.gz` - Source distribution

### Installing Locally

```bash
pip install dist/pyshipproto-2.6.3-py3-none-any.whl
```

## GitHub Actions Release

### Automatic Release via GitHub Actions

The project uses GitHub Actions for automated builds and releases to PyPI.

#### Prerequisites

1. **PyPI Account**: You need a PyPI account with access to the `pyshipproto` package
2. **PyPI API Token**: Generate at https://pypi.org/manage/account/token/
3. **GitHub Secret**: Add the token as `PYPI_API_TOKEN` in repository settings

#### Running the Workflow

1. Go to the Actions tab in GitHub
2. Select "Build PyShipProto V2" workflow
3. Click "Run workflow"
4. Enter the version number (e.g., "2.6.3")
5. Click "Run workflow"

The workflow will:
- Generate the protobuf files
- Build the Python package
- Check the package with twine
- Upload to PyPI (if token is configured)

### Manual PyPI Upload

If you need to upload manually:

```bash
# Install twine
pip install twine

# Check the package
twine check dist/*

# Upload to PyPI
twine upload dist/* --username __token__ --password pypi-YOUR-TOKEN-HERE
```

## Version History

- 2.6.2: Added support for protobuf 4.x, 5.x, and 6.x
- 2.6.0-2.6.1: Initial releases with Python 3.11/3.12 support
- 2.5.0: Previous stable version

## Troubleshooting

### Import Error: runtime_version
If you get an error about `runtime_version` not found, ensure you have a compatible protobuf version:
```bash
pip install 'protobuf>=4.21.0,<7.0.0'
```

### GitHub Actions Fails
- Check that `PYPI_API_TOKEN` is set in repository secrets
- Ensure the version number doesn't already exist on PyPI
- Check the workflow logs for specific error messages

## Dependencies

The package requires:
- `grpcio>=1.48.0`
- `grpcio-tools>=1.48.0`
- `protobuf>=4.21.0,<7.0.0`

These are automatically installed when you install pyshipproto.