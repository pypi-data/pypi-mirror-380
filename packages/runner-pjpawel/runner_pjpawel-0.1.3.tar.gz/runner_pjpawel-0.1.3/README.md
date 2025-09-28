# runner (runner-pjpawel)
Universal runner with builder objects to run async, threaded or group commands

*Build for my research projects to run multiple scenarios with retry with one command*

#### *Remember! This project is on early stage of development* 

### Install
```shell
pip install runner-pjpawel
```

### Build runner
1. Create Runner class.
```python
from runner_pjpawel import Runner
runner = Runner()
```
2. Add commands. Use prepared `Command` classes in `runner.commands` module or classes that extends `runnner.command.BaseCommand`
```python
from runner_pjpawel.command.common import ShellCommand
shell = ShellCommand("uname -a")
runner.add_command(shell)
```
3. Invoke `run` or `run_sync` method.
```python
runner.run_sync()
```

### Build your commands

You can build you own command. To do so, create class that extend class `BaseCommand`.
You have to override `_do_work` method.


### Full examples

1. Simplest example
```python
from runner_pjpawel import Runner
from runner_pjpawel.command import ShellCommand

r = Runner(show_progress_bar=False)
r.add_command(ShellCommand("uname"))
r.run_sync()
    
```




