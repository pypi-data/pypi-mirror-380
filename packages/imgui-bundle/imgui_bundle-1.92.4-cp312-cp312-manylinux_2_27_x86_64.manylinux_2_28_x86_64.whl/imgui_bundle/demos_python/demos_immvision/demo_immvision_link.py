import os.path

import numpy as np

from imgui_bundle import immvision, immapp, imgui, imgui_md
from imgui_bundle.demos_python import demo_utils

immvision.use_rgb_color_order()

this_dir = os.path.dirname(__file__)
image = demo_utils.imread_pil(demo_utils.demos_assets_folder() + "/images/tennis.jpg")
channels = [np.ascontiguousarray(image[:, :, i]) for i in range(image.shape[2])]

params_rgb = immvision.ImageParams()
params_rgb.image_display_size = (300, 0)
params_rgb.zoom_key = "some_common_zoom_key"

params_channels = immvision.ImageParams()
params_channels.image_display_size = (300, 0)
params_channels.zoom_key = "some_common_zoom_key"


def demo_gui():
    imgui_md.render_unindented(
        "If two images params share the same ZoomKey, then the images will pan in sync. Pan and zoom the image with the mouse and the mouse wheel"
    )

    immvision.image("RGB", image, params_rgb)
    for i, channel in enumerate(channels):
        immvision.image(f"channel {i}", channel, params_channels)
        imgui.same_line()
    imgui.new_line()


if __name__ == "__main__":
    immapp.run(demo_gui, window_size=(1000, 800), with_markdown=True)
