# cutter
All-in-one console tool for text manipulation, such as grep, sed, cut, tr, awk etc.

## Examples

Get all system users:\
`$ cat /etc/passwd | cutter --split=":" --format="{0}"`

Get all system users and homes:\
`$ cat /etc/passwd | cutter --split=":" --format="{0}          {5}"`

Get all numbers of the current kernel version:\
`$ uname -a | cutter --split --format="{6}" --search-and-replace=/-/./ --split="." --format="{0} {1} {2} {3}"`

Get interface names:\
`$ ip link | cutter --filter="UP" --search-and-replace=/:// --split --format="{1}"`

Get all IPv4 addresses:\
`$ ip addr | cutter --filter="inet " --search-and-replace="&/& &" --split --format="{1}"`

Get all running process and command line:\
`$ ps aux | cutter --nfilter="[" --nfilter="/cutter " --nfilter="ps aux" --substring=/65//`


