# DMOJ Archive
An archive of my DMOJ submissions

**How to run the dmoj.py script**:
```
  mkdir your/dmoj/archive/location
  cd your/dmoj/archive/location
  cp my/dmoj/location/dmoj.py dmoj.py
  chmod a+x dmoj.py
  ./dmoj.py
```

- The `working` directory should contain half-done solutions that have not yet gotten AC on DMOJ.
- The `done` directory contains archives of the fastest submissions for any given problem.

**Caveats**:
- A `.dmoj_creds` file will created the first time you run `dmoj.py`, and will contain your username
and password in a decodable format. If you do not wish to create this file, simply type `N` when
prompted to write the `.dmoj_creds` file.

**TODO**:
- Merge submit, problem_info scripts into one file, and pass command-line arguments
- "Un-caps-ify" the submit script
