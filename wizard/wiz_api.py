from __future__ import annotations
from typing import Dict, Any
from pywizlight import wizlight, discovery, PilotBuilder, bulb, PilotParser
from pywizlight.scenes import get_id_from_scene_name, SCENES


def get_scene_names():
    return [name for _, name in SCENES.items()]


async def search() -> list[wizlight]:
    bulbs = await discovery.discover_lights(broadcast_space="192.168.1.255")
    return bulbs


async def turn_off(bulb: wizlight):
    await bulb.turn_off()


async def setBulb(bulb: wizlight, rgb=None, brightness=None, scene=None):
    if scene is not None:
        scene = get_id_from_scene_name(scene)
        builder = PilotBuilder(scene=scene)
    else:
        builder = PilotBuilder(rgb=rgb, brightness=brightness)

    await bulb.turn_on(builder)


def bulb_from(*args, ip, mac=None):
    return wizlight(ip=ip, mac=mac)


async def getState(bulb: wizlight) -> PilotParser:
    curr = await bulb.updateState()

    return curr


async def main():
    bulbs = await search()
    # await setBulb(bulbs[0], rgb=(0, 0, 255), brightness=60)
    state = await getState(bulbs[0])
    print(state)


def parser_to_builder(parser: PilotParser) -> PilotBuilder:
    return PilotBuilder(
        warm_white=parser.get_warm_white(),
        cold_white=parser.get_cold_white(),
        speed=parser.get_speed(),
        scene=parser.get_scene_id() or None,
        rgb=parser.get_rgb(),
        rgbw=parser.get_rgbw(),
        rgbww=parser.get_rgbww(),
        brightness=parser.get_brightness(),
        colortemp=parser.get_colortemp(),
        state=parser.get_state(),
        ratio=parser.get_ratio()
    )


def parser_to_dict(parser: PilotParser) -> Dict[str, Any]:
    return {"warm_white": parser.get_warm_white() or None,
            "cold_white": parser.get_cold_white() or None,
            "speed": parser.get_speed() or None,
            "scene": parser.get_scene_id() or None,
            "rgb": parser.get_rgb() if None not in parser.get_rgb() else None,
            "rgbw": parser.get_rgbw(),
            "rgbww": parser.get_rgbww(),
            "brightness": parser.get_brightness() or None,
            "colortemp": parser.get_colortemp() or None,
            "state": parser.get_state() or None,
            "ratio": parser.get_ratio() or None
            }


def parser_dict_to_builder(parser_dict: Dict[str, Any]) -> PilotBuilder:
    return PilotBuilder(
        warm_white=parser_dict["warm_white"],
        cold_white=parser_dict["cold_white"],
        speed=parser_dict["speed"],
        scene=parser_dict["scene"],
        rgb=parser_dict["rgb"],
        rgbw=parser_dict["rgbw"],
        rgbww=parser_dict["rgbww"],
        brightness=parser_dict["brightness"],
        colortemp=parser_dict["colortemp"],
        state=parser_dict["state"],
        ratio=parser_dict["ratio"]
    )


if __name__ == "__main__":
    import asyncio
    asyncio.get_event_loop().run_until_complete(main())
