__version__ = "1.0.0"

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, NoReturn

import yaml

from .colors import Color, Gradient
from .effect import Effect
from .layers.base import Layer
from .layers.breathing import BreathingLayer
from .layers.spectrum import SpectrumLayer
from .layers.static import StaticLayer
from .layers.wave import WaveLayer
from .layers.wheel import WheelLayer
from .math.vector import Vector

PROG_NAME = "polychromatic_effects_generator"


def exit_with_error(message: str, error_type: str = "error") -> NoReturn:
    sys.exit(f"{PROG_NAME}: {error_type}: {message}")


def value_or[K, V](dictionary: dict[K, V], key: K, default: V) -> V:
    if key in dictionary:
        return dictionary[key]
    else:
        return default


def value_or_exit[K, V](dictionary: dict[K, V], key: K, message: str) -> V | NoReturn:
    if key in dictionary:
        return dictionary[key]
    else:
        exit_with_error(message)


def check_type_or_exit[T](
    val: Any, expected_type: type[T], message: str
) -> T | NoReturn:
    if isinstance(val, expected_type):
        return val
    else:
        exit_with_error(message)


def check_list_type_or_exit[T](
    val: Any, expected_type: type[T], message: str
) -> list[T] | NoReturn:
    list_val = check_type_or_exit(val, list, message)

    for item in list_val:
        check_type_or_exit(item, expected_type, message)

    return list_val


def check_dict_type_or_exit[K, V](
    val: Any, expected_key_type: type[K], expected_value_type: type[V], message: str
) -> dict[K, V] | NoReturn:
    dict_val = check_type_or_exit(val, dict, message)

    for item in dict_val.items():
        # fmt: off
        if (
            not isinstance(item[0], expected_key_type) or
            not isinstance(item[1], expected_value_type)
        ):
            exit_with_error(message)
        # fmt: on

    return dict_val


def gradient_from_yaml_or_exit(
    args_dict: dict, layer_index: int
) -> Gradient | NoReturn:
    gradient_dict = check_dict_type_or_exit(
        value_or_exit(
            args_dict, "gradient", f"no 'gradient' arg for layer {layer_index}"
        ),
        float,
        Color,
        f"arg 'gradient' in layer {layer_index} must be a dict with float keys and color values",
    )

    try:
        gradient = Gradient(gradient_dict)
    except ValueError as e:
        exit_with_error(f"invalid gradient for layer {layer_index}: {e}")

    return gradient


def color_constructor(loader, node) -> Color:
    value = loader.construct_scalar(node)

    if len(value) != 6:
        exit_with_error(
            f"cannot parse '{value}' as color (expected 6 characters, got {len(value)})"
        )

    red_hex = value[0:2]
    green_hex = value[2:4]
    blue_hex = value[4:6]

    red_int, green_int, blue_int = map(
        lambda val: int(val, 16), [red_hex, green_hex, blue_hex]
    )

    return Color(red_int, green_int, blue_int)


def cli():
    # Parse args
    parser = argparse.ArgumentParser(PROG_NAME)

    parser.add_argument(
        "recipe",
        type=argparse.FileType("r"),
        help="path to effect recipe file",
    )
    parser.add_argument(
        "--output",
        "-o",
        type=argparse.FileType("w"),
        help="path to output file",
    )
    parser.add_argument("-v", "--version", action="version", version=__version__)

    args = parser.parse_args()

    # Add YAML constructors
    yaml.add_constructor("!color", color_constructor)
    yaml.add_implicit_resolver("!color", re.compile(r"^[\da-f]{6}$"))

    # Try to parse recipe file
    try:
        recipe = yaml.load(args.recipe, yaml.Loader)
    except yaml.YAMLError as e:
        exit_with_error(f"could not parse file:\n{e}")
    finally:
        args.recipe.close()

    # Check that the parsed YAML document is a dict
    recipe = check_type_or_exit(recipe, dict, "recipe must be a dict")

    # Extract data from recipe
    # Metadata
    metadata = check_type_or_exit(
        value_or(recipe, "metadata", {}), dict, "'metadata' must be a dict"
    )

    metadata_name = str(value_or(metadata, "name", Path(args.recipe.name).stem))
    metadata_author = str(value_or(metadata, "author", PROG_NAME))
    metadata_summary = str(value_or(metadata, "summary", f"Generated with {PROG_NAME}"))
    metadata_icon = str(value_or(metadata, "icon", "img/effects/sequence.svg"))

    # Device info
    device_info = check_type_or_exit(
        value_or_exit(recipe, "device", "recipe must have 'device' key"),
        dict,
        "'device' must be a dict",
    )

    device_name = str(
        value_or_exit(device_info, "name", "'device' must have 'name' key")
    )
    device_icon = str(value_or(device_info, "icon", ""))
    device_graphic = str(value_or(device_info, "graphic", ""))

    # Grid info
    grid_info = check_type_or_exit(
        value_or_exit(device_info, "grid", "'device' must have 'grid' key"),
        dict,
        "'grid' must be a dict",
    )

    grid_width = check_type_or_exit(
        value_or_exit(grid_info, "width", "'grid' must have 'width' key"),
        int,
        "'width' must be an int",
    )
    grid_height = check_type_or_exit(
        value_or_exit(grid_info, "height", "'grid' must have 'height' key"),
        int,
        "'height' must be an int",
    )

    # FPS, duration, looping
    duration = check_type_or_exit(
        value_or(recipe, "duration", 30), int, "'duration' must be an int"
    )
    fps = check_type_or_exit(
        value_or(recipe, "fps", duration), int, "'fps' must be an int"
    )
    loop = check_type_or_exit(
        value_or(recipe, "loop", True), bool, "'loop' must be a bool"
    )

    layers = check_list_type_or_exit(
        value_or_exit(recipe, "layers", "recipe must contain 'layers' list"),
        dict,
        "'layers' must be a list of dicts",
    )

    # Construct effect
    effect = Effect(grid_width, grid_height, duration, fps)

    # Add layers to effect
    for index, layer_info in enumerate(layers):
        layer_name = str(
            value_or_exit(layer_info, "name", "each layer must contain 'name' key")
        )

        layer_args = check_type_or_exit(
            value_or(layer_info, "args", {}),
            dict,
            f"'args' in layer {index} must be a dict",
        )

        layer: Layer
        match layer_name:
            case "breathing":
                colors = check_list_type_or_exit(
                    value_or_exit(
                        layer_args, "colors", f"no 'colors' arg for layer {index}"
                    ),
                    Color,
                    f"arg 'color' in layer {index} must be a list of colors",
                )

                layer = BreathingLayer(grid_width, grid_height, duration, colors)
            case "spectrum":
                gradient = gradient_from_yaml_or_exit(layer_args, index)

                layer = SpectrumLayer(grid_width, grid_height, duration, gradient)
            case "static":
                color = check_type_or_exit(
                    value_or_exit(
                        layer_args, "color", f"no 'color' arg for layer {index}"
                    ),
                    Color,
                    f"arg 'color' in layer {index} must be an html color",
                )

                layer = StaticLayer(grid_width, grid_height, duration, color)
            case "wave":
                gradient = gradient_from_yaml_or_exit(layer_args, index)

                direction = str(value_or(layer_args, "direction", "left"))
                if direction == "left":
                    direction = WaveLayer.Direction.LEFT
                elif direction == "right":
                    direction = WaveLayer.Direction.RIGHT
                else:
                    exit_with_error(
                        f"unknown value for arg 'direction' in layer {index}, "
                        "expected either 'left' or 'right', got '{direction}'"
                    )

                layer = WaveLayer(
                    grid_width, grid_height, duration, gradient, direction
                )
            case "wheel":
                gradient = gradient_from_yaml_or_exit(layer_args, index)

                direction = str(value_or(layer_args, "direction", "clockwise"))
                if direction == "clockwise":
                    direction = WheelLayer.Direction.CLOCKWISE
                elif direction == "counterclockwise":
                    direction = WheelLayer.Direction.COUNTERCLOCKWISE
                else:
                    exit_with_error(
                        f"unknown value for arg 'direction' in layer {index}, "
                        "expected either 'clockwise' or 'counterclockwise', got 'direction'"
                    )

                center = check_list_type_or_exit(
                    value_or(layer_args, "center", [grid_width / 2, grid_height / 2]),
                    float,
                    f"arg 'center' in layer {index} must be a list of floats",
                )
                if len(center) != 2:
                    exit_with_error(
                        f"arg 'center' in layer {index} must be a list with exactly 2 elements"
                    )
                center = Vector(center[0], center[1])

                layer = WheelLayer(
                    grid_width, grid_height, duration, gradient, direction, center
                )
            case _:
                exit_with_error(f"unknown layer '{layer_name}' at index {index}")

        layer_keys = value_or(layer_info, "keys", "all")
        if layer_keys == "all":
            for x in range(grid_width):
                for y in range(grid_height):
                    effect.add_layer_to_pixel(x, y, layer)
        else:
            layer_keys = check_list_type_or_exit(
                layer_keys,
                list,
                f"'keys' in layer {index} must be a list of key coordinates as lists (e.g. [0, 4])",
            )

            for key in layer_keys:
                if len(key) != 2:
                    exit_with_error(
                        f"key {key} in layer {index} has {len(key)} elements, expected 2"
                    )

                check_list_type_or_exit(
                    key,
                    int,
                    f"all elements of key {key} in layer {index} must be integers",
                )

                x = key[0]
                y = key[1]

                if x < 0 or x > grid_width:
                    exit_with_error(
                        f"x in key {key} of layer {index} is out of range 0-{grid_width}"
                    )

                if y < 0 or y > grid_height:
                    exit_with_error(
                        f"y in key {key} of layer {index} is out of range 0-{grid_height}"
                    )

                effect.add_layer_to_pixel(x, y, layer)

    print("Recipe parsed successfully! Rendering...")

    # Render layers
    # Store frames in polychromatic-friendly format
    json_frames: list[dict[str, dict[str, str]]] = []

    for frame_num in range(duration):
        frame_grid: dict[str, dict[str, str]] = {}

        for x in range(grid_width):
            frame_grid[str(x)] = {}

            for y in range(grid_height):
                frame_grid[str(x)][str(y)] = effect.render_pixel_at(
                    x, y, frame_num
                ).as_html()

        json_frames.append(frame_grid)

    # Construct JSON object
    json_effect = {
        # Metadata
        "name": metadata_name,
        "type": 3,  # Sequence
        "author": metadata_author,
        "icon": metadata_icon,
        "summary": metadata_summary,
        # Device info
        "map_device": device_name,
        "map_device_icon": device_icon,
        "map_graphic": device_graphic,
        # Grid size
        "map_cols": grid_width,
        "map_rows": grid_height,
        # Format info
        "save_format": 8,
        "revision": 1,
        # Frame info
        "fps": fps,
        "loop": loop,
        "frames": json_frames,
    }

    # Save JSON object to file
    if args.output:
        outfile = args.output
    else:
        outfile = Path(f"./{metadata_name}.json").open("w")

    json.dump(json_effect, outfile, indent=4)
    outfile.close()

    print(f"Done! Saved JSON effect file to {Path(outfile.name).absolute()}")


if __name__ == "__main__":
    cli()
