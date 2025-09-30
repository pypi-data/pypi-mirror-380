# SARAO Machine Learning Utility functions 

Machine Learning utils is a library for a convenient experience. It consists of helper functions for creating astronomy/machine learning tools.

## Installation 

```
pip install katmlutils

```

## Example

```
from katmlutils.utils import get_night_window
from datetime import datetime

# Get the night window for the proposed date
nightwindow = get_night_window(datetime.datetime.now())

nightwindow
```

