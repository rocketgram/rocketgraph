# Rocketgraph

Powerful asynchronous library for telegra.ph.


## How to install

#### For development

```bash
pip install rocketgraph[aiohttp]
```

#### For production

```bash
pip install rocketgraph[aiohttp,ujson,uvloop]
```

## Dependencies

All dependencies are optional but you should install one of `aiohttp` and `tornado` to use framework.

`ujson` is highly recommended to speedup json parsing.

Also you can use `uvloop` as alternative to standard event loop.

* Python >= 3.7
* aiohttp >= 3.5.4
* ujson >= 1.35
* tornado >= 6.0.2
* uvloop >= 0.12.1

## Example

WIP

# Testing

Code tested automatically using `travis`. You can see build status **[here](https://travis-ci.com/vd2org/rocketgram)**.

To test code manually install and run `pytest`:

```bash
pip install pytest
python -m pytest
```