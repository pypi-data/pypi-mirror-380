pyalienvaultcli
=========

Description
-----------
A simple Python script to interact with Alienvault OTX APIs from CLI.


Usage
-----
```
$ pip install pyalienvaultcli

$ pyalienvaultcli
usage: pyalienvaultcli.py [-h] [-k API_KEY] [-a {add}] -p PULSE_ID -i INPUT_FILE

version: 1.1

options:
  -h, --help            show this help message and exit
  -k, --api-key API_KEY
                        API key (could either be provided in the "SECRET_ALIENVAULT_API_KEY" env var)
  -a, --action {add}    Action to perform (default 'add')
  -p, --pulse_id PULSE_ID
                        Pulse ID to perform the requested action
  -i, --input-file INPUT_FILE
                        Input file as a list of newline-separated IoC
```
  

Changelog
---------
* version 1.1 - 2025-09-14: Publication on pypi.org and few fixes


Copyright and license
---------------------

pyalienvaultcli is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

pyalienvaultcli is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  

See the GNU Lesser General Public License for more details.

You should have received a copy of the GNU General Public License along with pyalienvaultcli. 
If not, see http://www.gnu.org/licenses/.

Contact
-------
* Thomas Debize < tdebize at mail d0t com >