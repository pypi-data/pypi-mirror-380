from bluer_objects import README

from bluer_sbc.designs.consts import assets2


image_template = assets2 + "bluer-swallow/design/head-v1/{}?raw=true"

marquee = README.Items(
    [
        {
            "name": "bluer-swallow head",
            "marquee": image_template.format("01.jpg"),
            "url": "./bluer_sbc/docs/bluer-swallow-head.md",
        }
    ]
)

items = README.Items(
    [
        {
            "marquee": image_template.format(f"{index+1:02}.jpg"),
            "name": "",
        }
        for index in range(6)
    ]
)
