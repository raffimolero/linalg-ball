# Linear Algebra (ball)

Most files taken from http://resources.codingthematrix.com/

## Setup

### 1. Install [uv](https://docs.astral.sh/uv/) (basically npm for python)

(Windows): Open **PowerShell** and run:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

(MacOS/Linux): Refer to [the Official uv Installation Guide on their site](https://docs.astral.sh/uv/getting-started/installation/)

Restart your IDE (e.g. VSCode), then verify:

```powershell
uv --version
```

### 2. Clone and install dependencies

```powershell
git clone https://github.com/raffimolero/linalg-ball.git
cd linalg-ball
uv sync
```

## Run tests

```powershell
uv run pytest --doctest-modules . -vv
```

## Run program

Sometimes the command is `py` or `python` instead of `python3`.
Whichever one it is, make sure that `py/python/python3 --version` gives 3.12 and up.

```powershell
python3 main.py
```

This will then show you a list of options.

```
Enter task (or exit):
> show
> identity
> translate
> scale
> rotate
> rotate about
> reflect y
> reflect x
> scale color
> grayscale
> reflect about
>
```

Simply type in which option you would like to choose and press enter.
Each one corresponds to a specific task in Lab 4.15 from 4.15.1 through 4.15.11.

This will open your browser and display an image with the specified transformation matrix applied to it. The image will be offset by (500,500)px to avoid going out of bounds for some transformations.

Once you're done inspecting the output, simply close the tab, return to the terminal, and **hit Enter again** before inputting the next task.

> Note: Inputting the next task will do nothing if you forget to hit enter after the previous task.

```
Hit Enter once the image is displayed....
```

When done, either use `Ctrl+C` or type `exit` to leave.

```
> exit
```
