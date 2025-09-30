// Part of ImGui Bundle - MIT License - Copyright (c) 2022-2024 Pascal Thomet - https://github.com/pthom/imgui_bundle
#include "imgui_md_wrapper.h"

#ifdef HELLOIMGUI_HAS_OPENGL // Image rendering with markdown only works with OpenGl
#define CAN_RENDER_IMAGES
#endif

#include "hello_imgui/hello_imgui.h"
#include "immapp/snippets.h"

#include "imgui.h"
#include "imgui_md/imgui_md.h"
#include "immapp/code_utils.h"
#include "immapp/browse_to_url.h"

#include <fplus/fplus.hpp>
#include <string>
#include <vector>
#include <utility>
#include <map>
#include <memory>
#include <iostream>
#include <cassert>


namespace ImGuiMd
{

    namespace
    {
        // Factor applied to the font size before displaying
        // Case 1: Platforms which report screen size in "physical pixels": Windows (for "Dpi aware" apps), Linux (with Wayland)
        //    in case 1, fontDpiFactor = screenDpi / 96
        // Case 2: Platforms which report screen size in "density-independent pixels": macOS, iOS, Android, emscripten
        //    in case 2, fontDpiFactor = 1
        float fontDpiFactor()
        {
            auto dpiParams = HelloImGui::GetDpiAwareParams();
            float fontDpiFactor = dpiParams->DpiFontLoadingFactor();
            return fontDpiFactor;
        }

    }

    namespace ImGuiMdFonts
    {
        struct MarkdownEmphasis
        {
            bool italic = false;
            bool bold = false;
        };
        struct MarkdownTextStyle
        {
            MarkdownEmphasis markdownEmphasis;
            int headerLevel = 0;
        };

        static bool operator==(const MarkdownEmphasis& lhs, const MarkdownEmphasis& rhs) {
            return (lhs.italic == rhs.italic) && (lhs.bold == rhs.bold);
        }

        static std::vector<MarkdownEmphasis> AllEmphasisVariants()
        {
            return {
                { false, false },
                { false, true },
                { true, false },
                { true, true },
            };
        }


        float MarkdownFontOptions_FontSize(const MarkdownFontOptions &self, int headerLevel)
        {
            if (headerLevel <= 0)
                return self.regularSize * fontDpiFactor();
            else
            {
                int idxSizeFactors = headerLevel - 1;
                if (idxSizeFactors >= 6)
                    idxSizeFactors = 5;
                float multiplicationFactor = self.headerSizeFactors[idxSizeFactors];
                float fontSize = self.regularSize * fontDpiFactor() * multiplicationFactor;
                return fontSize;
            }
        };


        std::string MarkdownFontOptions_FontFilename(const MarkdownFontOptions &self, MarkdownEmphasis style)
        {
            std::string r = self.fontBasePath + "-";
            if (style.bold)
                r += "Bold";
            else
                r += "Regular";
            if (style.italic)
                r += "Italic";
            r += ".ttf";
            return r;
        }

        bool IsDefaultMarkdownEmphasis(const MarkdownEmphasis& style)
        {
            return !style.bold && !style.italic;
        }


        class FontCollection
        {
        public:
            FontCollection(const MarkdownFontOptions& options): mMarkdownFontOptions(options)
            {
                LoadFonts();
            }

            SizedFont GetFontCode() const
            {
                return {mFontCode, mMarkdownFontOptions.regularSize * fontDpiFactor()};
            }

            SizedFont GetDefaultFont() const
            {
                auto defaultMarkdownStyle = MarkdownTextStyle{};
                return GetFont(defaultMarkdownStyle);
            }

            SizedFont GetFont(const MarkdownTextStyle& _markdownTextStyle) const
            {
                MarkdownTextStyle markdownTextStyle = _markdownTextStyle;
                if (markdownTextStyle.headerLevel < 0)
                    markdownTextStyle.headerLevel = 0;

                float fontSize = MarkdownFontOptions_FontSize(mMarkdownFontOptions, markdownTextStyle.headerLevel);

                for (auto pair: mFonts)
                {
                    if (pair.first == markdownTextStyle.markdownEmphasis)
                        return SizedFont{ pair.second, fontSize };
                }
                IM_ASSERT(false && "Could not find font for markdown style");
            }
        private:
            void LoadFonts()
            {
                std::string error_message = R"(
Could not find required assets for ImGuiMd:
We need to find the following files in the assets:

assets/
├── fonts/
│     ├── Roboto/
│     │     ├── LICENSE.txt
│     │     ├── Roboto-Bold.ttf
│     │     ├── Roboto-BoldItalic.ttf
│     │     ├── Roboto-Regular.ttf
│     │     ├── Roboto-RegularItalic.ttf
│     ├── Inconsolata-Medium.ttf
│     └── fontawesome-webfont.ttf
└── images/
    └── markdown_broken_image.png

)";
                for (auto emphasisVariant: AllEmphasisVariants())
                {
                    std::string fontFile = MarkdownFontOptions_FontFilename(mMarkdownFontOptions, emphasisVariant);

                    // we shall not load the icons for all the fonts variants, since the font atlas
                    // texture might end up too big to fit in the GPU.
                    ImFont * font;
                    float defaultFontLoadingSize = 16.f;  // size at loading time (then Fonts can be resized to any size)
                    if (IsDefaultMarkdownEmphasis(emphasisVariant))
                        font = HelloImGui::LoadFontTTF_WithFontAwesomeIcons(fontFile, defaultFontLoadingSize);
                    else
                        font = HelloImGui::LoadFontTTF(fontFile, defaultFontLoadingSize);

                    if (font == nullptr)
                    {
                        fprintf(stderr, "%s", error_message.c_str());
                        IM_ASSERT(false);
                    }

                    mFonts.push_back(std::make_pair(emphasisVariant, font) );
                }

                float fontSize = MarkdownFontOptions_FontSize(mMarkdownFontOptions, 0);
                mFontCode = HelloImGui::LoadFontTTF(
                    "fonts/Inconsolata-Medium.ttf",
                    fontSize);
                if (mFontCode == nullptr) {
                    // SourceCodePro-Regular was the old default font for code
                    // we try to load it, to be nice with older users
                    mFontCode = HelloImGui::LoadFontTTF(
                        "fonts/SourceCodePro-Regular.ttf",
                        fontSize);
                }
                if (mFontCode == nullptr) {
                    fprintf(stderr, "%s", error_message.c_str());
                    IM_ASSERT(false);
                }
            }

            MarkdownFontOptions mMarkdownFontOptions;
            std::vector<std::pair<MarkdownEmphasis, ImFont*>> mFonts;
            ImFont* mFontCode;
        };

    } //namespace MdFonts

    struct MarkdownCollection
    {
        MarkdownCollection(const MarkdownFontOptions& options)
            : mFontCollection(options)
        {}
        ImGuiMdFonts::FontCollection mFontCollection;

#ifdef CAN_RENDER_IMAGES
        mutable std::map<std::string, HelloImGui::ImageAndSize > mLoadedImages;
#endif
    };


    class MarkdownRenderer : public imgui_md
    {
    private:
        MarkdownOptions *mMarkdownOptions;
        MarkdownCollection mMarkdownCollection;
        std::map<std::string, Snippets::SnippetData> mSnippets;
    public:
        MarkdownRenderer(MarkdownOptions* markdownOptions)
            : mMarkdownOptions(markdownOptions)
            , mMarkdownCollection(markdownOptions->fontOptions)
        {
        }

#ifdef CAN_RENDER_IMAGES
        std::map<std::string, HelloImGui::ImageAndSize >& ImageCache()
        {
            return mMarkdownCollection.mLoadedImages;
        }
#endif

        void Render(const std::string& s)
        {
            auto defaultSizedFont = mMarkdownCollection.mFontCollection.GetDefaultFont();
            ImGui::PushFont(defaultSizedFont.font, defaultSizedFont.size);

            const char * start = s.c_str();
            const char * end = start + s.size();
            this->print(start, end);
            ImGui::PopFont();
        }

        SizedFont get_font_code()
        {
            return mMarkdownCollection.mFontCollection.GetFontCode();
        }

        SizedFont GetFont(const MarkdownFontSpec& fontSpec)
        {
            ImGuiMdFonts::MarkdownTextStyle markdownTextStyle;
            markdownTextStyle.headerLevel = fontSpec.headerLevel;
            markdownTextStyle.markdownEmphasis.bold = fontSpec.bold;
            markdownTextStyle.markdownEmphasis.italic = fontSpec.italic;
            return mMarkdownCollection.mFontCollection.GetFont(markdownTextStyle);
        }


    private:
        imgui_md::MdSizedFont get_font() const override
        {
            if (m_is_code)
            {
                // https://github.com/mekhontsev/imgui_md does not handle correctly code blocks
                // so that we will never reach here...
                auto fontCode = mMarkdownCollection.mFontCollection.GetFontCode();
                return imgui_md::MdSizedFont{ fontCode.font, fontCode.size };
            }
            else
            {
                ImGuiMdFonts::MarkdownTextStyle markdownTextStyle;
                markdownTextStyle.headerLevel = m_hlevel;
                markdownTextStyle.markdownEmphasis.bold = m_is_strong;
                markdownTextStyle.markdownEmphasis.italic = m_is_em;
                auto font  = mMarkdownCollection.mFontCollection.GetFont(markdownTextStyle);
                return imgui_md::MdSizedFont{ font.font, font.size };
            }
        };

        void open_url() const override
        {
            if (mMarkdownOptions->callbacks.OnOpenLink)
                mMarkdownOptions->callbacks.OnOpenLink(m_href);
        }

        bool get_image(image_info& nfo) const override
        {
            if (! mMarkdownOptions->callbacks.OnImage)
                return false;

            std::optional<MarkdownImage> mdImage = mMarkdownOptions->callbacks.OnImage(m_img_src);

            if (! mdImage.has_value())
                return false;

            // Image size adaptive depending on the resolution scale
            {
                float k = HelloImGui::DpiFontLoadingFactor();
                nfo.size = ImVec2(mdImage->size.x * k, mdImage->size.y * k);
            }

            nfo.texture_id = mdImage->texture_id;
            nfo.uv0 = mdImage->uv0;
            nfo.uv1 = mdImage->uv1;

            return true;
        }

        void html_div(const std::string& divClass, bool openingDiv) override
        {
            if (!mMarkdownOptions->callbacks.OnHtmlDiv)
                return;

            mMarkdownOptions->callbacks.OnHtmlDiv(divClass, openingDiv);
        }

        void render_code_block() override
        {
            auto code_without_last_empty_lines = [](const std::string code_)
            {
                // remove last line if empty
                std::string code = code_;
                {
                    auto lines = fplus::split_lines(true, code);
                    if (lines.size() > 0)
                    {
                        if (fplus::trim_whitespace(lines.back()).size() == 0)
                            lines.pop_back();
                        code = fplus::join(std::string("\n"), lines);
                    }
                }
                return code;
            };

            ImGui::PushID(m_code_block.c_str());
            if (mSnippets.find(m_code_block) == mSnippets.end())
            {
                mSnippets[m_code_block] = Snippets::SnippetData();
                auto& snippet = mSnippets[m_code_block];
                snippet.Palette = Snippets::SnippetTheme::Mariana;
                snippet.Code = code_without_last_empty_lines(m_code_block);

                // set language
                if (fplus::to_lower_case(m_code_block_language) == "cpp")
                    snippet.Language = Snippets::SnippetLanguage::Cpp;
                else if (fplus::to_lower_case(m_code_block_language) == "c")
                    snippet.Language = Snippets::SnippetLanguage::C;
                else if (fplus::to_lower_case(m_code_block_language) == "python")
                    snippet.Language = Snippets::SnippetLanguage::Python;
                else if (fplus::to_lower_case(m_code_block_language) == "glsl")
                    snippet.Language = Snippets::SnippetLanguage::Glsl;
                else if (fplus::to_lower_case(m_code_block_language) == "sql")
                    snippet.Language = Snippets::SnippetLanguage::Sql;
                else if (fplus::to_lower_case(m_code_block_language) == "lua")
                    snippet.Language = Snippets::SnippetLanguage::Lua;
                else if (fplus::to_lower_case(m_code_block_language) == "angelscript")
                    snippet.Language = Snippets::SnippetLanguage::AngelScript;

                snippet.ShowCursorPosition = false;
            }

            ImGui::SetCursorPosX(0.f);
            auto& snippet = mSnippets[m_code_block];
            Snippets::ShowCodeSnippet(snippet);

            ImGui::PopID();
        }

    };


    // Global renderer
    std::unique_ptr<MarkdownRenderer> gMarkdownRenderer;

    // Global options
    MarkdownOptions gMarkdownOptions;

    void DeInitializeMarkdown()
    {
        gMarkdownRenderer.release();
    }

    void InitializeMarkdown(const MarkdownOptions& options)
    {
        static bool wasCalledAlready = false;
        if (wasCalledAlready)
        {
            //std::cerr << "InitializeMarkdown can only be called once at application startup!\n";
            return;
        }

        gMarkdownOptions = options;
        wasCalledAlready = true;
    }


    void Render(const std::string& markdownString)
    {
        if (!gMarkdownRenderer)
        {
            std::cerr << "ImGuiMd::Render : Markdown was not initialized!\n";
            return;
        }
        gMarkdownRenderer->Render(markdownString);
    }

    std::function<void(void)> GetFontLoaderFunction()
    {
        auto fontLoaderFunction = []()
        {
            gMarkdownRenderer = std::make_unique<MarkdownRenderer>(&gMarkdownOptions);
        };
        return fontLoaderFunction;
    }


    void OnOpenLink_Default(const std::string& url)
    {
        if (strncmp(url.c_str(), "http", strlen("http")) != 0)
        {
            std::cerr << "ImGuiMd::OnOpenLink_Default url \"" << url << "\" should start with http!\n";
            return;
        }
        ImmApp::BrowseToUrl(url.c_str());
    }


    std::optional<MarkdownImage> OnImage_Default(const std::string& image_path)
    {
#ifdef CAN_RENDER_IMAGES
        if (!gMarkdownRenderer)
        {
            std::cerr << "Did you initialize ImGuiMd?\n";
            return std::nullopt;
        }

        auto & imageCache = gMarkdownRenderer->ImageCache();
        if (imageCache.find(image_path) == imageCache.end())
        {
            std::string errorImage = "images/markdown_broken_image.png";
            if (HelloImGui::AssetExists(image_path))
                imageCache[image_path] = HelloImGui::ImageAndSizeFromAsset(image_path.c_str());
            else if (HelloImGui::AssetExists(errorImage))
                    imageCache[image_path] = HelloImGui::ImageAndSizeFromAsset(errorImage.c_str());
            else
                return std::nullopt;
        }

        const auto& imageInfo = imageCache.at(image_path);

        MarkdownImage r;

        r.texture_id = imageInfo.textureId;
        r.size = imageInfo.size;
        r.uv0 = { 0,0 };
        r.uv1 = {1,1};
        r.col_tint = { 1,1,1,1 };
        r.col_border = { 0,0,0,0 };
        return r;
#else
        return std::nullopt;
#endif
    }

    SizedFont GetCodeFont()
    {
        return gMarkdownRenderer->get_font_code();
    }

    SizedFont GetFont(const MarkdownFontSpec& fontSpec)
    {
        return gMarkdownRenderer->GetFont(fontSpec);
    }


    // Renders a markdown string (after having unindented its main indentation)
    void RenderUnindented(const std::string& markdownString)
    {
        Render(CodeUtils::UnindentMarkdown(markdownString));
    }

} // namespace ImGuiMdBrowser
