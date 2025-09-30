# Digamma Prime (`digamma-ep`)

Sistema simbólico para auditoria de modelos com métricas de divergência estrutural, temporal e algébrica.

Symbolic audit framework for comparing models, tracking divergence, and teaching algebraic structure.

---

## 📦 Instalação / Installation

```bash
pip install digamma-ep


#Basic Usage

from epe_maria import phi, delta_phi, phi_star

f = lambda x: x**2 + 2*x + 1
g = lambda x: x**2 + x + 1

print(phi(f, g))        # Divergência estrutural
print(delta_phi(f, g))  # Divergência de taxa
print(phi_star(f, g))   # Métrica de fusão

#Tests

pytest test_benchmark.py
pytest test_monitor.py

#Documentation
See examples and explanations in docs/ep_documentacao

#About
Created by Cerene Rúbio
License: MIT