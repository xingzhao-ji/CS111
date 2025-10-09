# A Kernel Seedling
This module prints the total number of processes that are running right now.

## Building
To build the module, run this command in the same directory where the make file is located 
```shell
make
```

## Running
To insert the module into the kernel, use this command
```shell
sudo insmod proc_count.ko
```
To run the kernel module to see the number of processes running, use this command
```shell
cat /proc/count
```
Results:
138

## Cleaning Up
To clean up the binary that we created, use this command
```shell
make clean
```
To remove module from the kernel, use this command
```shell
sudo rmmod proc_count
```

## Testing
To test the program using a python script, use this command
```python
python -m unittest
```
Results:
```
...
---------------------
Ran 3 tests in 17.026s

OK
```

Report which kernel release version you tested your module on
(hint: use `uname`, check for options with `man uname`).
It should match release numbers as seen on https://www.kernel.org/.
To see the kernel release version, use this command 
```shell
uname -r -s -v
```
Results:
Linux 5.14.8-arch1-1 #1 SMP PREEMAT Sun, 26 Sep 2021 19:36:15 +0000
