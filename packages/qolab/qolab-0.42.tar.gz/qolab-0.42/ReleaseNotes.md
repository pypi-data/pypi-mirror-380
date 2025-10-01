# version 0.42 (2025/09/30)

## bug fixes

- power supply __init__ is extended to take in account Keysight e36231a

# version 0.41 (2025/09/30)

## new

- added driver for Keysight e36231a power supply

# version 0.40 (2025/09/16)

## new

- added general spectrum analyzer class
- added Agilent E4405B spectrum analyzer hardware driver 

## changes

- scope save in gzipped format by default

# version 0.39 (2025/09/10)

## improvements

- make compatible with numpy < v2.0 where (concat alias was introduced).

# version 0.38 (2025/09/09)

## bug fixes

- SDS814x scope bug mitigation when hte memory depth exceeds scope's internal memory

# version 0.37 (2025/09/09)

## bug fixes

- USB handling for Windows in SDS814x.

# version 0.36 (2025/09/09)

## improvements

- Added USBkludge flag to init process for SDS814x, this allows
  it to be disabled by user if needed. There is a suspicion that
  misbehavior happens only at certain Windows/hardware combos.

# version 0.35 (2025/09/08)

## improvements

- Make better condition check

## bug fixes

- Fixed quotation marks to make python on Windows happy


# version 0.34 (2025/09/08)

## improvements

- Get rid of fmath flag when working with scope, driver should be
  able to infer it from the channel name, e.g. "F1". Currently,
  it is used only is SDS814x driver.
- getAllTtaces accepts channelsList of channels to grab, when it
  is not set, fall back to default: grabs all hardware channels.

# version 0.33 (2025/09/02)

## bug fixes

- Siglent SDS814x now can reliably gram Math channel
  - it turn out that there is no hardware decimation in Math/function
    channels

# version 0.32 (2025/08/29)

## bug fixes

- Siglent SDS1104 code now applies USB safety net only for Windows.


# version 0.31 (2025/08/28)

## bug fixes
- Fixed scopes `getWaveform` functions which was getting unexpected
  `fmath` argument which was introduced around v0.26 for 12bit Siglent
   scopes.

# version 0.30 (2025/01/14)

## compatibility breaking change
- If user request compression None, but filename indicates request for
  compression. We do compression in accordance with file name extension.
  This logic allows to utilize compression in old data saving scripts
  which unable to set compression explicitly.

# version 0.29 (2025/01/12)

## fixes
- speed up table reflow function 'ilocRowOrAdd' by factor of 10.
  pandas is extreemely slow with generation of arbitrary views,
  I converted tables to numpy, instead of using pandas builtins.


# version 0.28 (2025/01/12)

## new things
- Added function to calculate absorption per atom for Rb.
  It uses interpolation and significantly faster then calling
  for absorption directly. Another decision, it works per atom
  which makes it suitable for fast fitting of absorption spectra.


# version 0.27 (2025/01/09)

## new things
- ported Rb atom relevant calculations for D1 and D2 line
  from https://github.com/DawesLab/rubidium
    - we have absorption, pressure, density and other methods
    - introduce bug fixes and new formula for pressure calculation

## fixes
- reworked `tox.ini` to make it truly work
- code now is `black` formatted and `ruff` linter approved
- test with table reflow does not trigger `pandas` warning

