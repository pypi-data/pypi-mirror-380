import asyncio
import re
import tempfile
import time

import pytest

from time_my_func import dump, set_enabled, timeit


# -----------------------
# Helper to capture output
# -----------------------
def run_and_capture(func, capsys, is_async=False):
    if is_async:
        asyncio.run(func())
    else:
        func()
    return capsys.readouterr().out


# -----------------------
# Global toggle tests
# -----------------------
def test_global_toggle_disabled(capsys):
    set_enabled(False)  # Disable timing

    @timeit()
    def f():
        time.sleep(0.001)

    out = run_and_capture(f, capsys)
    assert out == ""

    set_enabled(True)  # Re-enable for other tests


def test_global_toggle_reenabled(capsys):
    set_enabled(False)

    @timeit()
    def f1():
        time.sleep(0.001)

    out1 = run_and_capture(f1, capsys)
    assert out1 == ""

    set_enabled(True)

    @timeit()
    def f2():
        time.sleep(0.001)

    out2 = run_and_capture(f2, capsys)
    assert "[f2]" in out2
    assert re.search(r"\d+\.\d{1,3} (ns|µs|us|ms|s|m)", out2)


# -----------------------
# Sync functions tests
# -----------------------
def test_sync_auto_unit(capsys):
    @timeit()
    def f():
        sum(range(1000))
    out = run_and_capture(f, capsys)
    assert "[f]" in out
    assert re.search(r"\d+\.\d{1,3} (ns|µs|ms|s|m)", out)


def test_sync_forced_units(capsys):
    @timeit(unit="ms", decimals=4)
    def f():
        time.sleep(0.01)
    out = run_and_capture(f, capsys)
    assert re.search(r"\d+\.\d{4} ms", out)


def test_sync_exception_prints_time(capsys):
    @timeit()
    def f():
        raise ValueError("fail")
    with pytest.raises(ValueError):
        run_and_capture(f, capsys)
    out = capsys.readouterr().out
    assert "[f]" in out
    assert re.search(r"\d+\.\d{1,3} (ns|µs|ms|s|m)", out)


# -----------------------
# Async function tests
# -----------------------
@pytest.mark.asyncio
async def test_async_function(capsys):
    @timeit()
    async def f():
        await asyncio.sleep(0.01)
    await f()
    out = capsys.readouterr().out
    assert "[f]" in out
    assert re.search(r"\d+\.\d{1,3} (ns|µs|ms|s|m)", out)


@pytest.mark.asyncio
async def test_async_exception_prints_time(capsys):
    @timeit()
    async def f():
        await asyncio.sleep(0.001)
        raise RuntimeError("fail")
    with pytest.raises(RuntimeError):
        await f()
    out = capsys.readouterr().out
    assert "[f]" in out
    assert re.search(r"\d+\.\d{1,3} (ns|µs|ms|s|m)", out)


# -----------------------
# Decimal places and unit tests
# -----------------------
@pytest.mark.parametrize("unit,pattern", [
    ("ns", r"\d+\.\d{3} ns"),
    ("us", r"\d+\.\d{3} µs"),
    ("µs", r"\d+\.\d{3} µs"),
    ("ms", r"\d+\.\d{3} ms"),
    ("s", r"\d+\.\d{3} s"),
    ("m", r"\d+\.\d{3} m"),
])
def test_sync_units(capsys, unit, pattern):
    @timeit(unit=unit)
    def f():
        time.sleep(0.001)
    out = run_and_capture(f, capsys)
    assert re.search(pattern, out)


def test_sync_custom_decimals(capsys):
    @timeit(unit="ms", decimals=5)
    def f():
        time.sleep(0.01)
    out = run_and_capture(f, capsys)
    assert re.search(r"\d+\.\d{5} ms", out)


# -----------------------
# Dump function tests
# -----------------------
def test_dump_output(capsys):
    @timeit(verbose=True)
    def f10():
        time.sleep(0.002)

    @timeit(verbose=True)
    def f20():
        time.sleep(0.001)

    f10()
    f20()
    f20()

    dump_output = capsys.readouterr().out
    # dump() prints aggregated results
    dump()
    captured = capsys.readouterr().out
    assert "[f10]" in captured
    assert "[f20]" in captured
    assert "calls=1" in captured
    assert "calls=2" in captured


def test_dump_to_file(tmp_path):
    file_path = tmp_path / "timing_results.txt"

    @timeit()
    def f():
        time.sleep(0.001)

    f()
    dump(file=str(file_path))

    content = file_path.read_text()
    assert "[f]" in content
    assert "calls=1" in content
