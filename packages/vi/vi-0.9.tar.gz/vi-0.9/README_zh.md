# VI - 向量解释器

[![PyPI version](https://badge.fury.io/py/vi.svg)](https://badge.fury.io/py/vi)
[![Python versions](https://img.shields.io/pypi/pyversions/vi.svg)](https://pypi.org/project/vi/)
[![License: GPL v2](https://img.shields.io/badge/License-GPL%20v2-blue.svg)](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html)

Vi（向量解释器）是一个用于生物物理设计平台的计算和分析工具包。它支持用户提交的任务自动并行执行，提供了一个完整的分子模拟工作流解决方案。

## ✨ 主要特性

- 🚀 **自动并行处理**: 用户提交的任务自动在集群中并行执行
- 📝 **YAML 配置**: 使用简单的 YAML 配置文件描述算法和工作流
- 🔧 **模块化设计**: 支持动态加载模块，易于扩展和定制
- 🖥️ **分布式架构**: 支持 Linux 集群部署
- 🔄 **工作流管理**: 完整的任务调度和状态管理
- 📊 **多种计算引擎**: 集成多种分子模拟和计算工具

## 📦 核心模块

- **General**: 框架和公共工具库
- **Compute**: 计算引擎（支持 Gaussian、LAMMPS 等）
- **Ensemble**: 系综和统计分析
- **Interpreter**: YAML 配置解析器
- **Scheduler**: 任务调度系统
- **Parallel**: 并行计算支持

## 🚀 快速开始

### 安装

使用 pip 安装：

```bash
pip install vi
```

或者从源码安装：

```bash
git clone https://github.com/lhrkkk/vi.git
cd vi
python setup.py install
```

### 基本使用

1. **创建配置文件** (`task.yml`):

```yaml
# 示例：分子动力学模拟任务
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

2. **提交任务**:

```bash
labkit push task.yml
```

3. **启动工作节点**:

```bash
# 前端服务器
labkit front

# 计算节点
labkit worker
```

## 🏗️ 系统架构

### 集群部署

Vi 设计用于 Linux 集群环境：

- **前端服务器**: 运行 `labkit front`，需要 beanstalkd 和 MongoDB
- **计算节点**: 运行 `labkit worker`
- **客户端**: 使用 `labkit push` 提交任务

### 工作流程

1. 用户编写 YAML 配置文件描述计算任务
2. 使用 `labkit push` 提交任务到队列
3. 集群自动分配资源并行执行任务
4. 返回计算结果

## 📝 配置文件语法

Vi 使用 YAML 格式的配置文件，支持以下语法：

### 基本结构

```yaml
# 列表
- item1
- item2

# 映射
key: value

# 循环控制
- module: some.module
  repeat: 100
  until: convergence_condition
```

### 高级功能

- **条件执行**: 支持 `until` 条件
- **循环控制**: 支持 `repeat` 参数
- **变量赋值**: 支持动态变量
- **模块参数**: 灵活的参数传递

## 🔧 命令行工具

Vi 提供了一系列命令行工具：

- `labkit`: 主命令行界面
- `labkit-api`: API 服务器
- `labkit front`: 前端服务
- `labkit worker`: 工作节点
- `labkit push`: 任务提交

## 🛠️ 开发和扩展

### 添加新模块

1. 在相应目录下创建新的 Python 模块
2. 实现所需的计算功能
3. 在 YAML 配置中引用新模块

### 模块开发原则

- **数据驱动**: 以 conformer、ensemble 等数据结构为核心
- **松耦合**: 模块间通过配置文件解耦
- **可测试**: 支持开发时模块化测试

## 📋 系统要求

- **Python**: 2.7, 3.6+
- **操作系统**: Linux (推荐)
- **依赖**: beanstalkd, MongoDB
- **集群**: 支持 PBS/SLURM 等作业调度系统

## 📚 文档和支持

- **GitHub**: https://github.com/lhrkkk/vi
- **问题反馈**: https://github.com/lhrkkk/vi/issues
- **许可证**: GPL v2

## 👥 贡献

欢迎贡献代码！请遵循以下步骤：

1. Fork 项目
2. 创建功能分支
3. 提交更改
4. 发送 Pull Request

## 📄 许可证

本项目使用 GPL v2 许可证。详见 [LICENSE](LICENSE) 文件。

## 👨‍💻 作者

- **作者**: lhr
- **邮箱**: airhenry@gmail.com
- **主页**: http://about.me/air.henry

---

**Vi 让分子模拟变得简单而强大！** 🧬✨