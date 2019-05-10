# Getting IMDB data

You can download the entire [IMDB dataset](https://www.imdb.com/interfaces/) and extract the files to the `data` folder. Once this is done rename the files which makes more sense while you load the data in Python using Pandas.

# Prerequisites

* Python
* Pandas
* Modin
* Matplotlib

# Environment Setup

## Windows

On Windows, you would need the [Windows Subsystem for Linux (WSL)](https://docs.microsoft.com/en-us/windows/wsl/install-win10) to run Pandas with Modin. You might need to install the update on your Windows 10 machine or enable it from the Add/Remove Program. There is a dependency Modin uses (ray) which is not available on Windows. After WSL is enabled, you can use the same commands as you use on Linux to install the other dependecies/prerequisites.

## Linux

Python is install by default on all major Linux distribution. You can then install other dependencies by using the `pip` commands.