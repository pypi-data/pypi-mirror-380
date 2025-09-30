# Part of ImGui Bundle - MIT License - Copyright (c) 2022-2025 Pascal Thomet - https://github.com/pthom/imgui_bundle
from imgui_bundle import imgui, immapp, imgui_md, has_submodule
HAS_IMMVISION = has_submodule("immvision")
if HAS_IMMVISION:
    from imgui_bundle import immvision  # noqa: F401
import importlib.util  # noqa: E402
from imgui_bundle.demos_python import demo_utils  # noqa: E402


HAS_OPENCV = importlib.util.find_spec("cv2") is not None


if HAS_IMMVISION:
    from imgui_bundle.demos_python import demos_immvision


def demo_gui():
    if not HAS_IMMVISION:
        imgui.text("Dear ImGui Bundle was compiled without support for ImmVision")
        return

    imgui_md.render_unindented(
        """
        # ImmVision
        [ImmVision](https://github.com/pthom/immvision) is an immediate image debugger.
        It is based on OpenCv and can analyse RGB & float, images with 1 to 4 channels.

        Whereas *imgui_tex_inspect* is dedicated to texture analysis, *immvision* is more dedicated to image processing and computer vision.

        Open the demos below by clicking on their title.
    """
    )

    if imgui.collapsing_header("Display images"):
        demos_immvision.demo_immvision_display.demo_gui()
        demo_utils.show_python_vs_cpp_file("demos_immvision/demo_immvision_display")
    if imgui.collapsing_header("Link images zoom"):
        demos_immvision.demo_immvision_link.demo_gui()
        demo_utils.show_python_vs_cpp_file("demos_immvision/demo_immvision_link")
    if imgui.collapsing_header("Image inspector"):
        demos_immvision.demo_immvision_inspector.demo_gui()
        demo_utils.show_python_vs_cpp_file("demos_immvision/demo_immvision_inspector")
    if HAS_OPENCV:
        if imgui.collapsing_header("Example with image processing"):
            demos_immvision.demo_immvision_process.demo_gui()
            demo_utils.show_python_vs_cpp_file(
                "demos_immvision/demo_immvision_process", nb_lines=40
            )


def main():
    immapp.run(demo_gui, window_size=(1000, 800), with_markdown=True)


if __name__ == "__main__":
    demo_utils.set_hello_imgui_demo_assets_folder()
    main()
