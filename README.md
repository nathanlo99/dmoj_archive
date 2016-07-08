# DMOJ Archive
An archive of my DMOJ submissions

**How to run the `dmoj.py` script**:
```
  mkdir your/dmoj/archive/location
  cd your/dmoj/archive/location
  mkdir done working
  cp my/dmoj/location/dmoj.py dmoj.py
  chmod a+x dmoj.py
  ./dmoj.py
```

- The `working` directory should contain half-done solutions that have not yet gotten AC on DMOJ.
- The `done` directory contains archives of the fastest submissions for any given problem.

**Caveats**:
- A `.dmoj_creds` file will created the first time you run `dmoj.py`, and will contain your username and password
in a decodable format. As such, simply edit the code in `dmoj.py` if you do not wish to write this file.

**Known problems**:
- Not all source languages are supported (extension mappings are not complete)
- The script does not check if your credentials are valid

**TODO**:
- Add source languages
- Check valid credentials
- Make option to not write file
- Check existence of 'done' and 'working' directories and create them automatically
