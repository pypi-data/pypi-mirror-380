# Liquid Handling Automation with Opentrons

This project, OT Handler, provides a comprehensive solution for automating liquid handling tasks and more using the Opentrons OT-2 robot. It includes a `LiquidHandler` class for managing labware, pipettes, and modules, as well as a suite of tests to ensure reliable operation (error handling, managing volumes out of range, optimizing volumes). Check out the goals and benefits shared in this [presentation](https://drive.google.com/file/d/1lrXMCGwYBwRjmMwhOUil6Nrj9lzpu1pk/view?usp=sharing).

Before getting started with the liquid handler programming, it's worth reading the list of counter-intuitive quirks to be aware of when working with OpenTrons OT-2: [liquid_handling_quirks.md](./liquid_handling_quirks.md)

## Features

- **Liquid Handling**: Automate complex liquid handling tasks with support for multi-channel and single-channel pipetting.
- **Labware Management**: Load and manage labware on the OT-2 deck.
- **Module Integration**: Control temperature, shaking, and magnetic modules.
- **Error Handling**: Robust error handling for common issues like deck conflicts and volume mismatches.

Visit the [issue tracker](https://app.asana.com/0/1209175521795471/1209175611695523) to see the current list of issues and planned features.

## Version 0.2.0

Major new features and improvements in this version:

### Enhanced Liquid Handling
- **Tip Reuse Limiting**: New `limit_tip_reuse` parameter allows forcing tip changes after a specified number of uses
- **Advanced Blow-out Control**: New `source_on_tip_change` blow-out behavior for better liquid handling precision
- **Retention Time**: Added retention time parameter for transfers to improve accuracy
- **Overhead Liquid & Air Gap Tracking**: Enhanced tracking of overhead liquid and air gap volumes
- **Large Volume Handling**: Operations exceeding pipette max volume are automatically split into manageable operations

### Improved Configuration & Flexibility
- **Custom Labware Support**: Support for custom labware definitions folder via `labware_folder` parameter
- **Deck Layout Configuration**: Custom deck layout can be provided via JSON string or file path using `deck_layout` parameter
- **Column-wise Pipetting**: Optimized pipetting order that prioritizes column-wise operations for efficiency

### Enhanced Error Handling & Reliability
- **Graceful Error Recovery**: OutOfTipsError no longer halts all operations - failed operations are tracked and returned with reasons
- **Better Filter Tips Support**: Improved filter tip utilization for full volleys
- **Automatic Resource Management**: Improved homing and labware latch management on exit

### Previous Changes (v0.1.1)
- `opentrons.log` -> `ot_handler.log` and is now located in the working directory
- `default_layout.ot2` is now located in the working directory

## Setup

### Prerequisites

- **Opentrons App**: Ensure you have the latest version of the Opentrons app installed.
- **Submodule Setup**: We assume you are hosting your own GitHub repository for the liquid handling workflow and would like to include the OT Handler as a submodule to be able to edit both repositories while maintaining the dependency.

### Installation

You can install **OT Handler** directly from PyPI using pip:

```bash
pip install ot_handler
```

If you want to install the latest development version (from the GitHub development branch), you can do so with:

```bash
pip install git+https://github.com/BIIE-DeepIR/ot-handler.git@development
```

Alternatively, if you'd like to work on the codebase locally and contribute to OT Handler, clone the repository, check out the development branch explicitly, and install it in editable mode:

```bash
git clone https://github.com/BIIE-DeepIR/ot-handler.git
cd ot-handler
git checkout development
pip install -e .
```

### Installation directly on OT-2

In order to install OT Handler on your OT-2, you need to have the OT-2 connected to the wifi, connect to the device over SSH and then follow the installation instructions above. Ideally, you would connect OT-2 to internet only temporarily, unless you have taken the appropriate security measures.

More information on how to connect the OT-2 with WiFi and SSH, follow the section "How to connect to the OT2" below.

## Usage

### Using the LiquidHandler class to distribute liquid

```python
from ot_handler import LiquidHandler  # edit path if you cloned the submodule to another path

# Initialize the LiquidHandler in simulation mode
# New parameters: deck_layout for custom layouts, labware_folder for custom labware
lh = LiquidHandler(simulation=True, load_default=False)

# Load tips
lh.load_tips('opentrons_96_tiprack_300ul', "7")

# Load labware
sample_plate = lh.load_labware("nest_96_wellplate_100ul_pcr_full_skirt", 5, "sample plate")
reservoir = lh.load_labware("nest_12_reservoir_15ml", 3, "reservoir")

# Distribute 50 ul of liquid from the first well of the reservoir to each well in the sample plate
# The pipette is chosen automatically, and multi-dispense is used of new_tip is "once" or "on aspiration" or "never"
lh.distribute(
    volumes=50,
    source_well=reservoir.wells()[0],
    destination_wells=sample_plate.wells(),
    new_tip="once")

# Drops tips if any left on the pipettes and homes to robot to a safe position
lh.home()
```

### Example: Advanced liquid handling features

```python
from ot_handler import LiquidHandler

lh = LiquidHandler(simulation=True)

# Load labware
source_plate = lh.load_labware("nest_96_wellplate_100ul_pcr_full_skirt", "1")
dest_plate = lh.load_labware("nest_96_wellplate_100ul_pcr_full_skirt", "2")

# Transfer with advanced parameters
lh.transfer(
    volumes=[50] * 96,
    source_wells=source_plate.wells(),
    destination_wells=dest_plate.wells(),
    new_tip="once",
    limit_tip_reuse=10,  # Force tip change after 10 uses
    retention_time=2.0,  # Wait 2 seconds after aspiration
    blow_out="source_on_tip_change"  # Blow out to source when changing tips
)

lh.home()
```

### Example: Custom deck layout and labware

```python
from ot_handler import LiquidHandler

# Custom deck layout as JSON string or file path
custom_layout = {
    "labware": {},
    "multichannel_tips": {"7": "opentrons_96_tiprack_300ul"},
    "single_channel_tips": {"11": "opentrons_96_tiprack_20ul"},
    "modules": {"4": "temperature module gen2"}
}

# Initialize with custom configuration
lh = LiquidHandler(
    simulation=True,
    deck_layout=custom_layout,
    labware_folder="/path/to/custom/labware"
)

lh.home()
```

### Example: Saving a default layout

You can save your default deck layout to a file called `default_layout.ot2`, which is then loaded whenever `LiquidHandler(load_default=True)` (this is True if not otherwise specified). This way you don't need to load the deck layout on every script, rather, you only load the variable elements.

The easiest way to generate your layout file is by passing `add_to_default=True` to `lh.load_tips`, `lh.load_labware` or `lh.load_module`. This flag saves the default position, so you no longer have to load it. Please note, that any existing item in that deck position will be overwritten by the new object, if there are any conflicts.

```python
from ot_handler import LiquidHandler

lh = LiquidHandler(simulation=True, load_default=False)
lh.load_tips('opentrons_96_tiprack_300ul', "7", add_to_default=True)
lh.load_tips('opentrons_96_tiprack_300ul', "6", add_to_default=True, single_channel=True)
lh.load_tips('opentrons_96_tiprack_20ul', "11", add_to_default=True, single_channel=True)

lh.load_module(module_name="temperature module gen2", location="4", add_to_default=True)
lh.load_module(module_name="heaterShakerModuleV1", location="10", add_to_default=True)
lh.load_module(module_name="magnetic module gen2", location="9", add_to_default=True)
```

Here's an example of a `default_layout.ot2`, which is the recommended setup.

```json
{
    "labware": {},
    "multichannel_tips": {
        "7": "opentrons_96_tiprack_300ul"
    },
    "single_channel_tips": {
        "6": "opentrons_96_tiprack_300ul",
        "11": "opentrons_96_tiprack_20ul"
    },
    "modules": {
        "4": "temperature module gen2",
        "10": "heaterShakerModuleV1",
        "9": "magnetic module gen2"
    }
}
```

### Example: Rapid development

Below we illustrate the advantages of the LiquidHandler class:

```python
import random
from ot_handler import LiquidHandler

lh = LiquidHandler(simulation=True)
lh.set_temperature(8)

dna_plate = lh.load_labware("nest_96_wellplate_100ul_pcr_full_skirt", "2")
reservoir = lh.load_labware("nest_12_reservoir_15ml", "3")

# Adding 25 ul on the first two columns
volumes = [25] * 16

# Adding 10 ul on the third column
volumes += [25] * 8

# Adding random volumes on the rest
volumes += [random.randint(5, 50)] * 8 * 9

# Let's change the well at half point to ensure sufficient volume
source_wells = [reservoir.wells()[0]] * 48 + [reservoir.wells()[1]] * 48

lh.transfer(
    volumes,
    source_wells=source_wells,
    destination_wells=dna_plate.wells(),
    new_tip="once"
)

lh.home()
```

Without the class, the above would require much more programming, such as:

- Loading pipettes and tip racks
- Choosing the right pipette for each volume
- Changing the nozzle layout of the multichannel pipette to single mode and back
- If the volume exceeds the pipette range, repeating the liquid transfer until the volume is reached

In addition, the following operations would not be available on the native OpenTrons python SDK:

- Aspirating liquid once, and dispensing different volumes to multiple wells
- As single channel mode of multichannel mode cannot access the bottom well rows in the first three deck slots, the robot would crash
- Set temperature would be a blocking call

What makes the LiquidHandler particularly powerful is the fact that it optimizes the order of liquid handling operations to be able to cover maximum amount of wells with single aspiration. This effectively reduces time to transfer liquids when contamination is not an issue.

### Example: Using the Opentrons commands

```python
# The pipettes are stored in lh.p300_multi and lh.p20
lh.p300_multi.pick_up_tip()
lh.p300_multi.mix(repetitions=5, volume=100, location=sample_plate.wells("A1"))
lh.p300_multi.drop_tip()

# The protocol api can be accessed through lh.protocol_api
lh.protocol_api.home()
```

### Example: Operating attached modules

```python
# Engage magnets for magnetic bead separation, 5.4mm from labware bottom
lh.engage_magnets(5.4)

# Disengage magnets after separation
lh.disengage_magnets()

# Set the temperature to 8 C, but don't wait until it's reached
lh.set_temperature(
    temperature=8,
    wait=False
)

# Shake for 30 seconds and continue once done
lh.shake(
    speed=1000,
    duration=30,
    wait=True
)
```

### Comparison of Opentrons and OT Handler

The following scripts accomplishes the same objective: serial dilutions followed by cherry picking, using first the original Opentrons python SDK alone, and then using the OT Handler. The difference between the two is not only in code, but the number of liquid handling operations is lower.

```python
from liquid_handler import LiquidHandler

lh = LiquidHandler(simulation=True, load_default=True, api_version="2.20")

# Only load labware, the pipettes, tips and modules are saved in the default layout
labware = lh.load_labware("nuncu_96_wellplate_450ul", 2)
reservoir = lh.load_labware("nest_12_reservoir_15ml", 3)

# Distribute 40uL from reservoir A1 to the first 16 wells and 10uL for the next 16 of the labware
lh.distribute(
    [50] * 8 + [40] * 8 + [10]*16,
    reservoir["A1"],
    labware.wells()[:32]
)

# Add the sample from A2 of the reservoir to the first column
lh.distribute(
    10,
    reservoir["A2"],
    labware.columns()[0],
    new_tip="always"
)

# Serial dilution: 1:5, 1:4, 2:1, 2:1
for column_index in range(0, 4):
    lh.transfer(
        10 if column_index in [0, 1] else 20,
        labware.columns()[column_index],
        labware.columns()[column_index + 1],
        new_tip="always",
    )

# Cherry pick 25ul from list of wells to reservoir A3
cherry_pick_wells = ["A3", "B1", "B7", "C5"]
lh.pool(  # lh.consolidate also exists as an alias for consistency
    25,
    [labware[w] for w in cherry_pick_wells],
    reservoir["A3"]
)

# This command will additionally ensure pipettes drop tips
lh.home()
```

```python
import json
import opentrons
import opentrons.simulate

protocol = opentrons.simulate.get_protocol_api("2.20")

# Load labware
with open(f'labware/nuncu_96_wellplate_450ul.json') as labware_file:
    labware_def = json.load(labware_file)
labware = protocol.load_labware_from_definition(labware_def, 2)
reservoir = protocol.load_labware("nest_12_reservoir_15ml", 3)

# Load tips
p300_tips = protocol.load_labware('opentrons_96_tiprack_300ul', '7')
p20_tips = protocol.load_labware('opentrons_96_tiprack_20ul', '11')

# Load pipette
p300_multi = protocol.load_instrument('p300_multi', 'right', tip_racks=[p300_tips])
p20 = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[p20_tips])

# Distribute 40uL from reservoir A1 to the first 16 wells of the labware
p300_multi.distribute(
    [50, 40],
    reservoir['A1'],
    [labware["A1"], labware["A2"]],  # Even though destinations are single wells, whole columns are filled
)

# Distribute remaining 10uL with p20 from reservoir A1 to the next 16 wells of the labware
p20.distribute(
    10,
    reservoir['A1'],
    labware.wells()[16:32]
)

# Add the sample from A2 of the reservoir to the first column
p20.distribute(
    10,
    reservoir['A2'],
    labware.columns()[0],
    new_tip='always'
)

# Serial dilution: 1:5, 1:4, 2:1, 2:1
for column_index in range(0, 4):
    p20.transfer(
        10 if column_index in [0, 1] else 20,
        labware.columns()[column_index],
        labware.columns()[column_index + 1],
        new_tip='always'
    )

# Cherry pick 25ul from list of wells to reservoir A3
cherry_pick_wells = ["A3", "B1", "B7", "C5"]
# Problem: too high volume for single channel pipette, the larger pipette is multichannel
# We have to split volume to multiple rounds or operate the multichannel pipette in a single channel mode. This requires an additional tip rack

if option == "A":
    
    # Option A: multiple trips with single channel pipette
    p20.consolidate(
        25,
        [labware[w] for w in cherry_pick_wells],
        reservoir["A3"]
    )
else:

    # Option B: use multichannel pipette in single channel mode
    single_p300_tips = protocol.load_labware('opentrons_96_tiprack_300ul', '5')

    # Change to single channel mode
    if p300_multi.has_tip:
        p300_multi.drop_tip()
    p300_multi.configure_nozzle_layout(
        style=opentrons.protocol_api.SINGLE,
        start="A1",
        tip_racks=[single_p300_tips]
    )

    p300_multi.consolidate(
        25,
        [labware[w] for w in cherry_pick_wells if w != "B7"],
        reservoir["A3"]
    )

    # Handle B7 with p20, as the robot would crash and lose coordinates trying to access it
    p20.consolidate(
        25,
        labware["B7"],
        reservoir["A3"]
    )

    # Change back to original mode
    if p300_multi.has_tip:
        p300_multi.drop_tip()
    p300_multi.configure_nozzle_layout(
        style=opentrons.protocol_api.ALL,
        tip_racks=[p300_tips]
    )

# Home the robot
if p20.has_tip:
    p20.drop_tip()
if p300_multi.has_tip:
    p300_multi.drop_tip()
protocol.home()
```

### Accessing the log files

OT Handlre generates `ot_handler.log` logfile which contains information about the last run, and is overwritten every time you run the workflow. If something goes wrong, be sure to preserve this log file for troubleshooting.

### Running Tests

The project includes a suite of unit tests to verify the functionality of the `LiquidHandler` class. To run the tests:

``` bash
python -m unittest discover -s ./tests
```

## How to connect to the OT2

### Connecting OT-2 to WiFi

Generally, it is not recommended to connect the OT-2 to WiFi, because other people might accidentally connect to the robot, if there are many of them in the network. You can temporarily connect the robot to WiFi, for example to install a new python package:

1. Open OpenTrons app
2. Open robot settings
3. Open "Networking"
4. Select network SSID, e.g. "eth"
5. Select "EAP-PEAP with MS-CHAP v2"  (depends on your network configuration)
6. Provide the username, e.g. [ETH USERNAME]@bsse.ethz.ch
7. Provide the password

Remember to disconnect the robot from WiFi after by clicking the "Disconnect" button on the OpenTrons app.

### Get the IP address

Turn on the robot, wait until it's ready, open the OpenTrons app and open the robot settings. The IP address is shown under "Networking".

### SSH into the robot

ssh root@<IP ADDRESS, e.g. 169.254.32.33>
cd /var/lib/jupyter/notebooks/biie_workflows

If this doesn't work, you might need to create an SSH key pair and add the public key to the robot: [Setting up SSH access to your OT-2](https://support.opentrons.com/s/article/Setting-up-SSH-access-to-your-OT-2)
