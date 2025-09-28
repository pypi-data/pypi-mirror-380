![Static Badge](https://img.shields.io/badge/Python->=3.6-3776AB?style=for-the-badge&logo=Python&logoColor=white) ![Static Badge](https://img.shields.io/badge/MyPy-Checked-3776AB?style=for-the-badge&logo=Python&logoColor=white) ![Static Badge](https://img.shields.io/badge/PyTest-Added-3776AB?style=for-the-badge&logo=Python&logoColor=white)

<p align="center">
    <a href="https://github.com/treizd/CompleTime">
        <img src="https://github.com/treizd/assets/blob/main/completime.png?raw=true" alt="CompleTime" width="256">
    </a>
    <br>
    <b>Time completion library</b>
</p>

## CompleTime
License: MIT


# Example usage (short)
``` python
import completime

@completime.timer()
def main():
    for _ in range(1000000): w = _ ** 2

if __name__ == "__main__":
    main() # Function main took 0:00:00.127524
```

### Donate
If you enjoy using my library, you can support me by donating.

- `UQB-7m2USzQ451d9orgD4iECLD0FL_BV-zzk3i--bdRl51ho` - TON
- `TUbvCEDE5wpVRsbLmuU8JfkWY4gNcBNbrx` - USDT TRC20

### Key Features
- **Easy**: No need to make code dirtier. Use decorators.
- **Type-hinted**: Mostly well-type hinted. Easy to use for other developers.

### Installing
``` bash
pip3 install completime
```

### Verifying installation
``` python shell
>>> import completime
>>> completime.__version__
'x.y.z'
```