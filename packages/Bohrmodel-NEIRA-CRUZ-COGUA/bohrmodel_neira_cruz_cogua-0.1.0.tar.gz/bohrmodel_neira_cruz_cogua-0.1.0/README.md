# BohrModel: Modelo del Átomo de Bohr

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![GitHub Repo](https://img.shields.io/badge/GitHub-repo-blue.svg)](https://github.com/XxyamzxX/-tomo_bohr)

---

## Descripción

**BohrModel** es una librería en Python que implementa el modelo del átomo de Bohr para átomos hidrogenoides.  
Permite realizar cálculos de **niveles de energía**, **radios de órbitas**, **transiciones electrónicas** y generar **representaciones gráficas** de manera interactiva.

El paquete está diseñado siguiendo buenas prácticas de **desarrollo de software científico**, con modularidad, pruebas unitarias y documentación clara.

---

## Características

- Cálculo de niveles de energía de electrones en un átomo hidrogenoide.
- Cálculo de radios de órbitas electrónicas.
- Cálculo de transiciones electrónicas: energía, frecuencia y longitud de onda de los fotones.
- Representación gráfica de niveles de energía y órbitas electrónicas.
- Menú interactivo en consola para seleccionar propiedades y gráficos.
- Modular: cálculos de energía, radios, transiciones y gráficos en módulos separados.

---

## Instalación

Se recomienda usar un **entorno virtual**:

```bash
git clone https://github.com/XxyamzxX/-tomo_bohr.git
cd -tomo_bohr
pip install -e .


-tomo_bohr/
│── pyproject.toml
│── README.md
│   └── bohrmodel/
│       ├── energia.py
│       ├── radios.py
│       ├── transiciones.py
│       ├── graficos.py
│       └── atom.py



