# ETA Components

This is a component library for the mathematical modeling of industrial production sites.
Currently it provides models for energy converters, such as CHPs, absorption chillers and
energy storages, networks to connect these components to and basic models to mock energy
sources and sinks.

The energy converter models are largely based on Baumgärtner (2020):
"Optimization of low-carbon energy systems from industrial to national scale" p. 128 ff.

## Components

* A large variety of energy converters:
    * AbsorptionChiller,
    * GasBoiler and ElectrodeBoiler,
    * Chp,
    * AirWaterCompressionChiller and WaterWaterCompressionChiller,
    * DryCooler,
    * ParallelHX and CounterCurrentHX,
    * AirWaterHeatPump and WaterWaterHeatPump and
    * HeatStorage and ColdStorage.
* Networks to enforce energy balance across all connected components:
    * GasNetwork,
    * ElectricalNetwork and
    * HeatingNetwork and CoolingNetwork.
* Environments to provide access to shared parameters:
    * AmbientEnvironment.
* Traders to buy and sell energy across the system's boundaries:
    * SimpleBuyer and SimpleSeller.
* Mock models for fixed energy sources and sinks, such as waste heat sources or cooling demands:
    * SimpleHeatingSource, SimpleCoolingSource and SimpleElectricitySource,
    * SimpleHeatingSink, SimpleCoolingSink and SimpleElectricitySink and
    * HeatBuffer, CoolBuffer and ElectricalBuffer.
* Frameworks that manage all models and provide a central solver interface.
    * SingleLevelFramework and SingleLevelUnitCommitmentFramework.

## Features

* On/off operating decisions for all converters.
* Part-load efficiency for all converters.
* Buying decisions for all converters.
* Automated objective function that minimizes the cost of all traders.
* Plotting of each network's energy production and consumption.
* Indices not only for time steps but also for typical periods and stochastic samples.

## What's not implemented yet

* Investment and maintenance cost for all converters.
* Continuous sizing of all converters.
* Objective function for minimization of emissions.
* Sellers and buyers for cooling energy.
    * At the moment these must be implemented with buyers or sellers, respectively (because of negative heat flow).
* Variable temperatures for the networks à la Thermal Dependencies paper.
* Framework for bilevel problems.
* Starting cost, ramp limits and maximum starts per time for relevant equipments.
* Measures for increasing efficiency.
* Material data models for production processes.

## Requirements

* Python 3.10 or higher,
* CPLEX installed, and it is in the system's PATH.

## Installation

To install the project along with its development dependencies, execute the following command:

    poetry install

Followed by

    poetry run pre-commit install

After this you are ready to perform the first commits to the repository.

Pre-commit ensures that the repository accepts your commit, automatically fixes some code styling problems and provides some hints for better coding.

## Usage

The entire system is modeled as **energy flows**, thus no volume flows are explicitly implemented.
Each converter, trader or energy source or sink must be connected to its corresponding network(s).
The networks then enforce an energy balance across all connected components so that energy production
and consumption match for each time step. The energy flows are implemented in a thermodynamic contex with each
network as the system's boundary. Thus, inlet energy is positive and outlet energy is negative.

E.g. a gas boiler has a negative gas consumption (because it flows out of the gas network) and a positive heat
production
(because it flows into the heating network). The same goes for electrical energy. Attention is required when
using cooling producers or consumers, as cooling producers move heat out of the cooling network (negative production)
and cooling consumers move heat into the network (positive consumption).

## Quick start

```python
import eta_components.milp_component_library.units.equipment.sources_sinks
import eta_components.milp_component_library as mcl

fw = mcl.frameworks.SingleLevel(n_samples=1, n_periods=1, n_time_steps=2)

heating_net = mcl.networks.HeatingFluid("Heating_network",
                                        {"T_hot": 273.15 + 90, "T_cold": 273.15 + 50, "cp": 4190,
                                         "rho": 998},
                                        fw)
gas_net = mcl.networks.Gas("Gas_network", {}, fw)
electrical_net = mcl.networks.Electrical("Electrical_network", {}, fw)

chp = mcl.operational.Chp(
    "CHP",
    {"P_out_nom": 1000, "eta": 0.9, "pfr_plr_bpts": ((0.6, 0.5), (1, 1)), "eta_th": 0.6},
    fw,
    hot_network=heating_net,
    electrical_network=electrical_net,
    gas_network=gas_net,
)
cleaning_machine = mcl.sources_sinks.SimpleHeatingSink(
    "Cleaning_machine",
    {"P_in": {(1, 1, 1): -500, (1, 1, 2): -400}},
    fw,
    heating_network=heating_net)
gas_supplier = mcl.traders.SimpleSeller("Gas_supplier",
                                        {"unit_price": {(1, 1, 1): 2, (1, 1, 2): 5},
                                         "emissions_per_unit": 0},
                                        fw,
                                        network=gas_net)
electrical_buffer = mcl.sources_sinks.VariableElectricalSink("Buffer", {},
                                                             fw,
                                                             electrical_network=electrical_net)

fw.join_models()
fw.set_objective("cost")
fw.solve()
```

## Example

There are examples in the folder /examples.

## License

Refer to the LICENSE file distributed with this package.

### Adding dependencies
Adding dependencies to the project can be done via

    poetry add <package-name>@latest
