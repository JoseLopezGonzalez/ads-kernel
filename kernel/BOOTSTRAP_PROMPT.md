Estás en el repositorio ADS de CONTROL de un producto. NO es el repositorio del código.

Un ADS Project gobierna un PRODUCTO, y el producto puede estar repartido entre varios
repositorios Git independientes. El código vive en las FUENTES declaradas en SOURCES.toml,
y aparece como repositorios hermanos de éste dentro del workspace:

    <workspace>/
    ├── ads/        estás aquí: gobierno, PROFILE, estado, items, decisiones, contratos
    ├── frontend/   código, con su Git independiente
    └── backend/    código, con su Git independiente

Lee íntegramente PROJECT.md, PROFILE.md, SOURCES.toml, kernel/KERNEL.md y todos los
ficheros de packs/.

Estos documentos son la semilla y la autoridad conceptual del proyecto.
El KERNEL define cómo trabajas. Los PACKS aportan el saber hacer de esta clase de
proyecto. El PROFILE define qué construimos aquí. SOURCES.toml dice de qué repositorios
está hecho.

Sobre las fuentes:
  · si SOURCES.toml no declara ninguna, es correcto: este producto todavía no tiene código,
    y decidir su arquitectura física es parte del Circuito 0;
  · NO concluyas que algo no existe porque no esté dentro de este repositorio. Comprueba
    primero: python3 tooling/workspace.py status
  · para materializar las que falten: python3 tooling/workspace.py init [ids]
  · NO copies el PROFILE, el estado, la memoria, los ADR globales, el kernel ni los packs
    dentro de una fuente. Una verdad vive en un sitio, y ese sitio es este repositorio.
  · escribe SÓLO en las fuentes que tu paquete declara. Leer una no autoriza a modificarla.

Inicia el Circuito 0 — Bootstrap de la organización IA.
NO implementes funcionalidades del producto. NO elijas stack definitivo.
NO diseñes arquitectura de producto.

Tu gate de salida está fijado en G22 y no es negociable por ti: los 10 entregables,
dentro del timebox declarado en el PROFILE. Si se agota sin cumplirlo, PARA y emite
un Owner Decision explicando qué falta y por qué.

Tu PRIMER entregable es AGENTS.md compilado (<400 líneas), imperativo y comprobable,
a partir de KERNEL + PACKS + PROFILE. En kernel/templates/AGENTS_EXAMPLE.md tienes uno de otro
proyecto: úsalo como ejemplo de forma y densidad, nunca de contenido.

Antes de tomar decisiones estructurales, investiga las capacidades actuales REALES
de las herramientas agentic que vas a usar, y registra la evidencia con fecha (G33).

Verifica primero que el contrato K0 del PROFILE está completo. Si falta algún
apartado obligatorio, pídemelo antes de continuar.

Al terminar cada sesión: entrada en docs/JOURNAL.md y push de este repositorio. Los
repositorios de código tienen su propio ciclo: rama, commits, push y PR por fuente, y su
convergencia se declara en un Integration Set, nunca dando por integrado el producto porque
se haya fusionado un PR.

Empieza confirmándome en dos líneas qué has entendido que vamos a construir y cuál
es mi definición de éxito. Si tu resumen no coincide con lo que yo tenía en la
cabeza, es mejor descubrirlo ahora.
