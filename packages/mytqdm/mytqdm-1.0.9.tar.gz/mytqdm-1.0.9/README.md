# MyTqdm
See and share your tqdm state everywhere with everyone on [mytqdm.app](https://mytqdm.app)!

<a href="https://www.buymeacoffee.com/padmalcom" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>

## Installation
```pip install mytqdm```

## Registration
Register an account on [mytqdm.app](https://mytqdm.app) to obtain your custom API key.

## Usage
- Import via ```from mytqdm import mytqdm``` and use ```mytqdm``` instead of ```tqdm```.
- Provide your ```api_key``` in the mytqdm constructor. Optionally provide a ```title```.

Example:
```
from mytqdm import mytqdm

MY_API_KEY = "..."
for i in mytqdm(range(10000), api_key=MY_API_KEY, title="Our progress to make POs happy."):
    ...
```





