# dependency-license-closure

## Français

Calculer les obligations déclarées de branches de dépendances.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m dependency_license_closure examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Traverse le graphe de dépendances déclaré et conserve les branches de licence alternatives ; chaque choix est une liste de licences conjointes, sans analyser arbitrairement du texte SPDX.

### Limites

Étiquettes de travail seulement, pas avis juridique, analyse des fichiers, compatibilité de licences ou obligations complètes. Licence inconnue rend la cartographie incomplète.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Compute declared license obligations across dependency branches.

Synthetic data; no network access or secret required.

```sh
python -m dependency_license_closure examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Traverses declared dependencies and preserves alternative license branches; each choice is a list of conjunctive licenses, without arbitrarily parsing SPDX text.

### Limits

Working labels only, not legal advice, file analysis, license compatibility or complete obligations. Unknown license makes mapping incomplete.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Calcular obligaciones declaradas en ramas de dependencias.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m dependency_license_closure examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Recorre dependencias declaradas y conserva ramas de licencia alternativas; cada opción es lista de licencias conjuntas, sin analizar texto SPDX arbitrariamente.

### Límites

Solo etiquetas de trabajo, no asesoría jurídica, análisis de archivos, compatibilidad ni obligaciones completas. Licencia desconocida vuelve incompleto el mapa.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://spdx.github.io/spdx-spec/v2.3/SPDX-license-expressions/
