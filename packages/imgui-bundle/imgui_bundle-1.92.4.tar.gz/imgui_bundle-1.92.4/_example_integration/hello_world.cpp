// Part of ImGui Bundle - MIT License - Copyright (c) 2022-2024 Pascal Thomet - https://github.com/pthom/imgui_bundle
#include "immapp/immapp.h"
#ifdef IMGUI_BUNDLE_WITH_IMPLOT
#include "implot/implot.h"
#endif
#include "imgui_md_wrapper.h"

#include <cmath>


void DemoImplot()
{
    static std::vector<double> x, y1, y2;
    if (x.empty())
    {
        double pi = 3.1415;
        for (int i = 0; i < 1000; ++i)
        {
            double x_ = pi * 4. * (double)i / 1000.;
            x.push_back(x_);
            y1.push_back(cos(x_));
            y2.push_back(sin(x_));
        }
    }

    ImGuiMd::Render("# This is the plot of _cosinus_ and *sinus*");
#ifdef IMGUI_BUNDLE_WITH_IMPLOT
    if (ImPlot::BeginPlot("Plot"))
    {
        ImPlot::PlotLine("y1", x.data(), y1.data(), (int)x.size());
        ImPlot::PlotLine("y2", x.data(), y2.data(), (int)x.size());
        ImPlot::EndPlot();
    }
#endif
}


void Gui()
{
    ImGuiMd::RenderUnindented(R"(
            # Dear ImGui Bundle
            [Dear ImGui Bundle](https://github.com/pthom/imgui_bundle) is a bundle for [Dear ImGui](https://github.com/ocornut/imgui.git), including various useful libraries from its ecosystem.
            It enables to easily create ImGui applications in C++, as well as in Python.

            This is an example of markdown widget, with an included image:

            ![world](images/world.png)

            ---
            And below is a graph created with ImPlot:
        )");

    DemoImplot();

    ImGui::Separator();
    ImGuiMd::RenderUnindented("*Note: the icon of this application is defined by `assets/app_settings/icon.png`*");
}


int main(int , char *[])
{
#ifdef ASSETS_LOCATION
    HelloImGui::SetAssetsFolder(ASSETS_LOCATION);
#endif

    HelloImGui::SimpleRunnerParams runnnerParams;
    runnnerParams.guiFunction = Gui;
    runnnerParams.windowSize = {600, 800};

    ImmApp::AddOnsParams addOnsParams;
    addOnsParams.withMarkdown = true;
    addOnsParams.withImplot = true;

    ImmApp::Run(runnnerParams, addOnsParams);
    return 0;
}
