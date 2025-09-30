# [BO Study] Controlled Polymer Injection

> [!IMPORTANT]
> This is a higly customized setup for the 4-gates injection case

This documents presents; in detail, findings of a Bayesian-Optimization study on effects of certain polymer injection profiles.

## Hasty ADRs

**Problem-related:**
1. Injection profiles are considered as sigmoid-exponential curves $f(t) = \frac{\text{InjectionRate}}{1+e^{-\text{toggle}\cdot\text{MachineFactor}\cdot(t-t_0)}}$
   - Machine-specific ramp-up capabilities are modeled with a scalar factor
   - Injection gates can be initially active or inactive
   - $t_0$ is the time instance at which the gate injection is toggled
1. In metric computation, the meldline is included as a bad "weldline", although a meldline results in a lower penalty
1. Threshold values are carefully crafted to try and restrict the BO algorithms to regions of interest

**Technical:**
1. If remote mode is on, it assumes SLURM jobs are started through a REST daemon, with accounting enabled
1. Some function objects are forced to compute metric values they have nothing to do with

## Optimization setup

### Prerequisites

Here are the main prereqs to reproduce this study (checked ones are provided in this repo):

1. [ ] Access to Extend-based `blockUCoupledIMFoam` solver
1. [x] [FoamBO] version 1.0.0 with a YAML configuration `moo.yaml`
1. [x] A Foam-Extend 5 container, with solvers and associated tools;
   - Build one from `containers/imfoam.def` using [OpenFOAM Apptainer Containers]
1. [x] An injection case; modified to use the injection profiles. Optimization settings are
  gathered into `constant/gateSettings`. Explore `4GateDesign` case.
1. [ ] [Optional] A slurm cluster, supporting SLURM REST API and apptainer, try the [makeshift] one

### General workflow

- **Your local machine** runs `FoamBO` and oversees the optimization process
- If **remote mode** is on:
  - **The SLURM cluster** (through Docker containers) runs the cases suggested by `FoamBO`
  - Through an apptainer container that has the required solvers/tools
> [!NOTE]
> This has the effect of having "shell" trial cases on the local machine.
> The real cases are the copies on the cluster. Ideally you'd want to setup a shared mount
> to avoid excessive copying...
- If **local mode** is on:
  - Trials run locally, either with the apptainer container, or with binaries from the host

### Preparations

The typical preparation steps for such studies include:

1. Generate a starting configuration for FoamBO (already provided as `moo.yaml`)
   ```bash
   uv run foamBO --generate-config --config myBOStudy.yaml
   ```
1. Make sure `trials` and `artifacts` folders are next to `moo.yaml` file
1. Copy the `imfoam-dev.sif` container to the SLURM head node at `/home/slurmuser/imfoam-dev.sif`

## Optimization objectives

The following metrics are minimized. Note that these objectives are crafted so the optimization
problem is well-posed with enough contradictions between objectives:

1. **Weldline**
   - No weldline forming is the optimal result
   - If weldline formed, penalizing weldline cells in narrow injection canals
   - If weldline formed, penalizing weldline cells with temperature away from inlet temperatures
1. **Balanced filling**
   - Domain RHS and LHS should be filled simultaneously, using alpha volume as a metric
1. **Max inlet pressure**
   - Set to be an outcome constraint (less than 200 bars)
1. **Fill time**
   - Designed to counter the inlet pressure

**weldline** and **Balanced Filling** metrics are also used to early-stop trials if either
metric proves to be worse than the rest of the trials during simulations.

## Optimization parameter space

- **Machine ramp-up factor** helps in analyzing the effect of machine dead-time and responsiveness
- **Gate injection profile** for each gate represented by:
  - Injection start time
  - Injection max flow rate
  - Injection state initially

This results in 13 parameters (for 4 injection gates); with an estimate search space size of `3.34e23`

## Optimization Results

TBD

## Lessons learned, shortcomings

- While FoamBO provides "parameter constraints", which are linear relationships between members of
  parameter space, more complex behavior is desired but is probably hard to implement.
  - **Example problematic constraints**: Restricting the "total flow rate" accross the 4 gates to a value
    at any point in time.
  - **Ideal solution**: The generation strategy would generate trials that conform to this restriction
  - **Current potential solution**: Drop one gate's settings from the parameter space, and compute
    its injection profile according to the constraint.
  - **What can be done now**: only something like `rate1 + rate2 + rate3 + rate 4 <= 2.0`

[FoamBO]: https://github.com/FoamScience/OpenFOAM-Multi-Objective-Optimization
[makeshift]: https://github.com/FoamScience/hpc-makeshift-cluster
[OpenFOAM Apptainer Containers]: https://github.com/FoamScience/openfoam-apptainer-packaging
