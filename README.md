# Juego de Nave Espacial

Juego 2D desarrollado en Python utilizando la librería Pygame.
Controla una nave, esquiva obstáculos y enemigos.

## Tecnologías principales

- Python 3.x
- Pygame (instalado vía `requirements.txt`)

## Estructura del proyecto

- **main.py**: Punto de entrada; inicializa Pygame y gestiona el bucle principal del juego.
- **sprites/**: Contiene las clases y objetos Sprite (heredan de `pygame.sprite.Sprite`).
- **assets/**: Imágenes, sonidos y fuentes usadas en el juego.
- **links.txt**: Enlaces originales de los recursos externos.
- **requirements.txt**: Lista de dependencias.

## Instalación

```bash
# Clonar el repositorio
git clone https://github.com/Franco-Miguez/space-game.git
cd space-game

# Crear entorno virtual (opcional pero recomendado)
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Instalar dependencias
pip install -r requirements.txt
```

## Uso

```bash
python main.py
```

El juego abrirá una ventana donde podrás pilotar la nave.

## Controles

- **Mouse**: Mover la nave y disparar con el botón izquierdo

## Créditos y recursos

Los recursos gratuitos empleados en este proyecto provienen de:

- Imágenes y sprites: www.freepik.es
- Efectos de sonido: freesound.org
- Fuentes: www.dafont.com

Consulta los enlaces originales en `links.txt`.

## Licencia

Este proyecto está bajo la **licencia MIT**. Siéntete libre de usarlo y modificarlo.
