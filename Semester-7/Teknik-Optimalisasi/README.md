# Teknik Optimalisasi (Semester 7)
> **Author**: Marchell Adi Pratama

---

## Domain Overview & Technical Specifications

This directory contains metaheuristic optimization algorithms including Particle Swarm Optimization (PSO) and Harmony Search (HS) applied to multi-objective network routing and parameter tuning.

### Pipeline Architecture

```text
Semester-7/Teknik-Optimalisasi/
 notebooks/
 Particle_Swarm_Optimization_Network_Routing.ipynb # Multi-Objective Delay/Energy PSO Routing
 PSO untuk Optimasi Rute Jaringan.ipynb # Communication Graph Shortest Path PSO
 Harmony Search.ipynb # Pitch Adjustment & Memory Harmony Search
```

---

## Metaheuristic Optimization Specifications

| Algorithm Notebook | Objective Function | Swarm / Harmony Parameters | Convergence Target |
| :--- | :--- | :--- | :--- |
| `Particle_Swarm_Optimization_Network_Routing.ipynb` | f(x) = 0.6 * delay + 0.4 * energy | N=5, C1=2.0, C2=2.0, w=0.7 | Optimal Network Delay |
| `Harmony Search.ipynb` | Continuous Benchmark Function | HMCR = 0.9, PAR = 0.3 | Global Fitness Minimum |

---

## Execution Quickstart

```bash
jupyter notebook Semester-7/Teknik-Optimalisasi/notebooks/
```
