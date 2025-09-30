# VI - Molecular Simulation Package

[![PyPI version](https://badge.fury.io/py/vi.svg)](https://badge.fury.io/py/vi)
[![Python versions](https://img.shields.io/pypi/pyversions/vi.svg)](https://pypi.org/project/vi/)
[![License: GPL v2](https://img.shields.io/badge/License-GPL%20v2-blue.svg)](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html)

Vi is a computational toolkit for biophysical design platforms that supports automatic parallel execution of user-submitted tasks, providing a complete molecular simulation workflow solution.

## ✨ Key Features

- 🚀 **Automatic Parallel Processing**: User-submitted tasks are automatically executed in parallel on clusters
- 📝 **YAML Configuration**: Use simple YAML configuration files to describe algorithms and workflows
- 🔧 **Modular Design**: Supports dynamic module loading, easy to extend and customize
- 🖥️ **Distributed Architecture**: Supports Linux cluster deployment
- 🔄 **Workflow Management**: Complete task scheduling and status management
- 📊 **Multiple Compute Engines**: Integrated with various molecular simulation and computational tools

## 📦 Core Modules

- **General**: Framework and common utility library
- **Compute**: Computation engines (supports Gaussian, LAMMPS, etc.)
- **Ensemble**: Ensemble and statistical analysis
- **Interpreter**: YAML configuration parser
- **Scheduler**: Task scheduling system
- **Parallel**: Parallel computing support

## 🚀 Quick Start

### Installation

Install using pip:

```bash
pip install vi
```

Or install from source:

```bash
git clone https://github.com/lhrkkk/vi.git
cd vi
python setup.py install
```

### Basic Usage

1. **Create a configuration file** (`task.yml`):

```yaml
# Example: Molecular dynamics simulation task
- module: compute.gaussian
  input_file: molecule.xyz
  method: B3LYP
  basis_set: 6-31G*

- module: ensemble.analysis
  trajectory: output.traj
  properties:
    - energy
    - rmsd
```

2. **Submit task**:

```bash
labkit push task.yml
```

3. **Start worker nodes**:

```bash
# Frontend server
labkit front

# Compute nodes
labkit worker
```

## 🏗️ System Architecture

### Cluster Deployment

Vi is designed for Linux cluster environments:

- **Frontend Server**: Run `labkit front`, requires beanstalkd and MongoDB
- **Compute Nodes**: Run `labkit worker`
- **Client**: Use `labkit push` to submit tasks

### Workflow

1. Users write YAML configuration files to describe computational tasks
2. Use `labkit push` to submit tasks to the queue
3. Cluster automatically allocates resources and executes tasks in parallel
4. Returns computational results

## 📝 Configuration File Syntax

Vi uses YAML format configuration files with the following syntax:

### Basic Structure

```yaml
# Lists
- item1
- item2

# Mappings
key: value

# Loop control
- module: some.module
  repeat: 100
  until: convergence_condition
```

### Advanced Features

- **Conditional Execution**: Support for `until` conditions
- **Loop Control**: Support for `repeat` parameters
- **Variable Assignment**: Support for dynamic variables
- **Module Parameters**: Flexible parameter passing

## 🔧 Command Line Tools

Vi provides a series of command line tools:

- `labkit`: Main command line interface
- `labkit-api`: API server
- `labkit front`: Frontend service
- `labkit worker`: Worker nodes
- `labkit push`: Task submission

## 🛠️ Development and Extension

### Adding New Modules

1. Create new Python modules in the appropriate directory
2. Implement required computational functionality
3. Reference new modules in YAML configuration

### Module Development Principles

- **Data-Driven**: Core data structures like conformer, ensemble
- **Loose Coupling**: Modules decoupled through configuration files
- **Testable**: Support modular testing during development

## 📋 System Requirements

- **Python**: 2.7, 3.6+
- **Operating System**: Linux (recommended)
- **Dependencies**: beanstalkd, MongoDB
- **Cluster**: Supports job schedulers like PBS/SLURM

## 📚 Documentation and Support

- **GitHub**: https://github.com/lhrkkk/vi
- **Issue Tracker**: https://github.com/lhrkkk/vi/issues
- **License**: GPL v2

## 👥 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the project
2. Create a feature branch
3. Commit your changes
4. Send a Pull Request

## 📄 License

This project is licensed under GPL v2. See [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

- **Author**: lhr
- **Email**: airhenry@gmail.com
- **Homepage**: http://about.me/air.henry

---

**Vi makes molecular simulation simple and powerful!** 🧬✨