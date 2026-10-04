# Calculadora CLI

Una calculadora de consola desarrollada en Python para practicar una estructura de código modular y fácil de mantener.

El proyecto separa la interacción con el usuario de las operaciones aritméticas y la validación de entradas. Así, cada módulo tiene una responsabilidad concreta y el programa principal coordina el flujo.

## Funcionalidades

- Suma, resta, multiplicación y división.
- Validación de entradas numéricas.
- Comprobación de la operación seleccionada.
- Validación del divisor para evitar divisiones entre cero.

## Estructura

```text
Calculadora/
└── main/
    ├── Calculadora.py
    └── funciones/
        ├── funciones_aritmeticas.py
        └── funciones_validacion.py
```

- `Calculadora.py`: muestra el menú, recoge las entradas y coordina la operación elegida.
- `funciones_aritmeticas.py`: contiene las funciones de suma, resta, multiplicación y división.
- `funciones_validacion.py`: valida los números introducidos y el divisor.

## Ejecución

Requiere Python 3 y no utiliza dependencias externas. Desde la carpeta raíz del proyecto, ejecuta:

```bash
python3 main/Calculadora.py
```

## Decisiones de diseño

El proyecto está modularizado para separar responsabilidades:

- `Calculadora.py` gestiona el menú, la interacción con el usuario y el flujo de la aplicación.
- `funciones_aritmeticas.py` contiene las operaciones matemáticas.
- `funciones_validacion.py` valida los valores introducidos, incluida la prevención de divisiones entre cero.

## Estado y próximos pasos

El proyecto está en revisión para incorporar mejoras de forma progresiva. Las siguientes ideas son posibles líneas de trabajo; se priorizarán según avance el desarrollo:

- Añadir pruebas automatizadas para las operaciones y validaciones.
- Revisar el manejo de errores y evitar capturar excepciones más amplias de lo necesario.
- Evaluar la incorporación de números decimales y aumentar el numero de argumentos por función aritmética.
- Seguir mejorando la organización y legibilidad del código.

## Registro de cambios

Las mejoras de cada versión se documentan en la [sección Releases](https://github.com/Albertovmt/calculadora-cli/releases). Allí puedes consultar qué cambió y cuándo se publicó.