# Sharing is Caring: A KSM Performance Study
## CS 695 Project



# Performance Characterization Study of Kernel Samepage Merging (KSM)

## Introduction
This repository contains the code and findings from a performance characterization study of Kernel Samepage Merging (KSM) conducted in a virtualized environment managed by VirtualBox Manager. The study aimed to evaluate KSM's behavior under different workloads and configuration parameters.

## Experiment Setup
- Virtual machines (VMs) were created using VirtualBox Manager, each running an instance of Ubuntu (22.04) Linux. Specifications of VM are:
  - CPU Cores: 2
  - RAM: 4GB
- Workloads were generated using the stress command to simulate various system stress scenarios.
- Python script was used to monitor `/sys/kernel/mm/ksm` parameters and collect performance metrics.

## Experiments
- VM with No Workloads
  - Enable the KSM using command ``` echo 1 > /sys/kernel/mm/ksm/run ```.
  - Run the .py script to start appending the values in an output file (.csv).
  - Turn on a VM and wait for some time so that it can reach the saturation point then turn on the second VM and do the same.
  - Make plots for the extracted data and analyze the plots.

- VMs with stress command running
  - Procedure is same as the last one, just this time run stress command this time.
    ```stress--vm <number_of_worker_threads>--vm-bytes <bytes_per_worker>```
  - Make plots and analyze them.

- Without KSM enabled
  - Run command ```vmstat 5 > <output_file>``` to get the stats in the output filfe every 5 seconds.
  - Now, run both the VMs and see the stats.
  - Once the values become consistent, enable the KSM.
  - Again wait for some time, and then run stress command on the VMs.
  - Make plots and analyze them.

## Data
Data was collected in CSV files (https://docs.google.com/spreadsheets/d/1wBj4yQyTHBXGi6IxTjVH1b_Ff69FTtqzJpP0qgCuD2o/edit?usp=sharing).

## Findings
- KSM demonstrated effectiveness in reducing memory duplication and optimizing memory utilization.
- `General_profit` increased over time (with an initial dip), indicating the benefits of memory deduplication by KSM.
- Fluctuations in `general_profit` were observed due to workload variability and dynamic memory usage.
- The dip in `pages_shared` during stress workload on both VMs highlighted the impact of increased memory demand on KSM's efficiency.

## Conclusion
The study underscores the importance of KSM in enhancing memory management efficiency and system scalability in virtualized environments. Further research could explore advanced optimization techniques and integration with other memory management solutions to address evolving system requirements.

