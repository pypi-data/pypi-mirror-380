# rosa-python-client

Pypi: [rosa-python-client](https://pypi.org/project/rosa-python-client/)  
A utility to run ROSA commands in CLI

## Release new version

### requirements:

* Export GitHub token

```bash
export GITHUB_TOKEN=<your_github_token>
```
* [release-it](https://github.com/release-it/release-it)

```bash

sudo npm install --global release-it
npm install --save-dev @release-it/bumper
```
Note: execute outside the repository directory (for example `~/`)

### usage:

* To create a new release, run:

```bash
git main
git pull
release-it # Follow the instructions
```

## Installation

From source using [poetry](https://github.com/python-poetry/poetry).

```
git clone https://github.com/RedHatQE/rosa-python-client.git
cd rosa-python-client
poetry install
```

From pypi:

```bash
pip install rosa-python-client --user
```

## Known Limitations:

Although rose cli support args with ` ` (space) when using this module we only accept arg=value

rosa cli accept: `rosa create cluster --cluster-name mycluster`  
when called with this module the command should be: `rosa create cluster --cluster-name=mycluster`  
