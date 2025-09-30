# cooltime-guard

A micro library to **guard execution with a cooldown interval**.
It ensures that a block of code runs only after a specified minimum time has passed since the previous execution.
If not enough time has passed, it waits (`time.sleep`) automatically before running.

## Features

- Simple and lightweight
- Context manager support with with syntax
- Guarantees a minimum interval between executions
- Useful for hardware control, API calls, or any resource that needs cooldown

## Examples

A simple example:

```python
import time
import cooltime_guard

# create a guard with 5ms interval
guard = cooltime_guard.Guard(interval=0.005)

def f():
    start = time.time()
    with guard:
        # ... Access to resources requiring a 5ms cooldown ...
        return time.time() - start

print(f()) #=> Nearly 0
print(f()) #=> Nearly 0.005
print(f()) #=> Nearly 0.005
time.sleep(0.01)
print(f()) #=> Nearly 0
```

When controlling LEDs that require a minimum interval of 1ms to light up properly:

```python
import cooltime_guard

# create a guard with 5ms interval
cg = cooltime_guard.Guard(interval=0.005)

def led_flash():
    with cg:
        GPIO.Pin(15).flash()
```

## Use cases

- Hardware access that requires cooldown (e.g., LEDs, sensors, actuators)
- API clients that must avoid calling too frequently
- Rate-limiting function calls without complex frameworks

## Notes

- `Guard` does not perform lock control for threading/multiprocessing. Therefore, if code blocks execute in parallel, the intended behavior may not occur. In such cases, use locks in conjunction with guards.

## License

[MIT License](./LICENSE)
