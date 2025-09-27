![Static Badge](https://img.shields.io/badge/Python->=3.6-3776AB?style=for-the-badge&logo=Python&logoColor=white) ![Static Badge](https://img.shields.io/badge/MyPy-Checked-3776AB?style=for-the-badge&logo=Python&logoColor=white) ![Static Badge](https://img.shields.io/badge/PyTest-Added-3776AB?style=for-the-badge&logo=Python&logoColor=white)

<p align="center">
    <a href="https://github.com/treizd/NumSystems">
        <img src="https://github.com/treizd/assets/blob/main/IMG_4473.PNG?raw=true" alt="NumerSys" width="256">
    </a>
    <br>
    <b>Powerful numeral systems conversion library</b>
</p>

## NumerSys
License: MIT


# Example usage (short)
``` python
import numersys


def main():
    result = numersys.convert("1010", 2, 10)
    print(result)

if __name__ == "__main__":
    main() # "10"
```

### Donate
If you enjoy using my library, you can support me by donating.

- `UQB-7m2USzQ451d9orgD4iECLD0FL_BV-zzk3i--bdRl51ho` - TON
- `TUbvCEDE5wpVRsbLmuU8JfkWY4gNcBNbrx` - USDT TRC20

### Key Features
- **Easy**: Makes working with numeral systems easier.
- **Type-hinted**: Types and methods are all type-hinted, enabling excellent editor support.
- **Fast**: Caching is enabled for making conversions much faster.

### Installing
``` bash
pip3 install numersys
```

### Verifying installation
``` python shell
>>> import numersys
>>> numersys.__version__
'x.y.z'
```