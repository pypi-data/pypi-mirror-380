# CHANGELOG

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.4.0] - 2025-09-29

### Added

- Added comprehensive type annotations and mypy static type checking integration
- **NamedColor Enum**: Exposed `NamedColor` enum class to improve developer experience when using colors. The enum provides easy access to all supported named colors with autocompletion and type safety.
- **Text Shaping Support**: Added advanced text shaping capabilities including kerning, ligatures, and proper complex script rendering (Arabic, emoji sequences). Text now renders with correct character connections and spacing adjustments.

### Fixed

- Fixed SVG rendering with custom font files being embedded. It was not working because a wrong SVG tag was being used.
- Fixed SVG font family normalization by removing spaces and commas from font identifiers to prevent rendering issues.
- Fixed text wrapping when no width constraint is specified, avoiding unnecessary wrap calculations.

### Changed

- Exclude development files from package distribution (/.github, /docs, /examples, /tests, .gitignore, *.yml, *.yaml)
- **BREAKING**: `text_stroke()` behavior now aligns with CSS standards. The stroke is now rendered centered on the text outline (half inside, half outside) instead of only outward. This matches `-webkit-text-stroke` behavior but will make stroked text appear visually thicker. Existing designs using this feature may need adjustment.

## [1.3.3] - 2025-09-27

### Fixed

- Fixed `RuntimeError: Failed to get; Likely no parameter` when using static font file. This error is happening only in some cases (maybe because of the font file, system, or skia version).

## [1.3.1] - 2025-09-14

### Fixed

- Fixed transparency handling in `BitmapImage.to_pillow()` method. The method now properly unpremultiplies alpha values from Skia's premultiplied format to Pillow's straight alpha format.

## [1.3.0] - 2025-09-13

### Added

- **Render Tree Access**: Both `BitmapImage` and `VectorImage` now expose a `render_tree` property that provides access to the hierarchical structure of rendered nodes with their bounds information. This allows users to inspect and interact with individual elements after rendering.
- **NodeType Enum**: New `NodeType` enum with values `TEXT`, `ROW`, `COLUMN`, and `ELEMENT` for type-safe node identification.
- **RenderNode Class**: New `RenderNode` class that represents nodes in the render tree, featuring:
  - `bounds`: Bounding box information for each node
  - `children`: Access to child nodes in the hierarchy
  - `node_type`: Type-safe node identification using `NodeType` enum
  - `visit_children()`: Method to recursively traverse child nodes
  - `find_nodes_by_type()`: Method to find all nodes of a specific type
- **Scale Factor Support**: New `scale_factor` parameter in `Canvas.render()` method allows rendering images at larger sizes. All dimensions (width, height, fonts, etc.) are scaled proportionally.
- **Extended Named Colors**: Added support for many additional named colors including extended CSS color names.

## [1.2.1] - 2025-09-07

### Fixed

- Fixed a major layout bug causing incorrect text wrapping in containers with multiple flexible children (e.g., a `Row`). Text now correctly calculates its available width based on siblings, preventing overflow.

## [1.2.0] - 2025-09-06

### Added

- New `'fill-available'` size mode allows elements to grow and fill the remaining space within a `Row` or `Column`, enabling more complex and fluid layouts.
- **Text Wrapping**: Added automatic text wrapping support. Text now automatically wraps to multiple lines when placed in containers with fixed widths. A new `.text_wrap()` method controls this behavior with `"normal"` (default, wrapping enabled) and `"nowrap"` (wrapping disabled) values.

### Fixed

- Use `position()`/`absolute_position()` in container (row or column) with children was causing unexpected exception

## [1.1.1] - 2025-08-09

### Fixed

- Fixed `stretch` alignment in Row/Column with nested descendants (two or more levels) causing unexpected exceptions

## [1.1.0] - 2025-08-09

### Added

- Documentation for builder classes was improved
- Support `stretch` for `horizontal_align()` and `vertical_align()` in `Row` and `Column` builders

### Changed

- Width and height are not calculated indivdually, it allows using parent with `fit-content` width (or height) and children with `percent` width (or height). For example, last version didn't admit child with `50%` width if the parent has fixed width but `fit-content` height.

### Fixed

- Render empty text line was throwing an unexpected exception

## [1.0.0] - 2025-08-04

### Added

-   **Component-Based Layout Engine**: PicTex is now a full-fledged layout engine. You can compose complex visuals by nesting `Row`, `Column`, `Text`, and `Image` builders.
-   **Layout Builders**: New `Row` and `Column` builders to arrange elements horizontally or vertically.
-   **Layout Control**:
    -   New `.horizontal_distribution()` and `.vertical_distribution()` methods for `Row` and `Column` to control main-axis spacing (`center`, `space-between`, etc.).
    -   New `.vertical_align()` and `.horizontal_align()` methods for `Row` and `Column` to control cross-axis alignment.
    -   New `.gap()` method on containers to set a consistent space between children.
-   **`Image` Builder**: A new first-class builder for adding and styling images.
-   **Sizing System**:
    -   New `.size()` method on all builders to set explicit dimensions.
    -   Support for `'fit-content'`, `'fit-background-image'`, and percentage (`'50%'`) sizing modes.
-   **Positioning System**:
    -   New `.position()` method to position an element relative to its parent's content area.
    -   New `.absolute_position()` method to position an element relative to the root canvas.
-   **Border Support**: New `.border()` method to add borders with `width`, `color`, and `style` (`'solid'`, `'dashed'`, `'dotted'`).
-   **Background Images**: New `.background_image()` method to set a background on any element, with support for `'cover'`, `'contain'`, and `'tile'` modes.

### Changed

-   **BREAKING**: The shadow API is now declarative.
    -   `add_text_shadow()` is replaced by `text_shadows(*shadows: Shadow)`.
    -   `add_box_shadow()` is replaced by `box_shadows(*shadows: Shadow)`.
    -   **Migration**: You must now import and instantiate the `Shadow` class, e.g., `.text_shadows(Shadow(offset=(2,2)))`. This allows multiple shadows to be set in a single call and enables overriding.
-   **BREAKING**: The `background_radius()` method was renamed to `.border_radius()`. It now accepts percentage values (e.g., `'50%'`) and can take 1, 2, or 4 arguments to control each corner individually.
-   **BREAKING**: The `Canvas()` constructor can't receive a `Style` instance anymore.
-   **BREAKING**: The `outline_stroke()` method was renamed to `text_stroke()`.
-   **BREAKING**: The `alignment()` method was renamed to `text_align()`.
-   **BREAKING**: The default padding was changed from `10` to `0`.
-   **BREAKING**: Each text box now has a larger height than before.
-   **BREAKING**: Shadows are ignored when the result is exported as an SVG image. It was supported in version 0.3.x.

## [0.3.1] - 2025-08-03

### Added

- Documentation for user-facing classes was improved

## [0.3.0] - 2025-07-16

### Added

- Render image as SVG. A new method was added in the Canvas class: `render_as_svg()`.
- If a character can't be rendered by the fonts provided, a system font for it will be searched.

### Fixed

- **Bug in font fallbacks**: when a font fallback was used for a glyph, the next characters was also rendered using the fallback, even when the primary font supported them (more info on issue #2).

### Changed
- `Canvas.font_family(...)` and `Canvas.font_fallbacks(...)` now support a `Path` object instance in addition to a string.
- The default font family now is the system font (it was `Arial`)
- If the primary font or any fallback font is not found, a warning is generated, and that font is ignored.

## [0.2.1] - 2025-07-10

### Added

- **Configurable Font Smoothing:** Added a `.font_smoothing()` method to the `Canvas` to control the text anti-aliasing strategy. This allows users to choose between `'subpixel'` (default, for maximum sharpness on LCDs) and `'standard'` (grayscale, for universal compatibility).

### Fixed

- **Text Rendering Quality:** Resolved a major issue where text could appear aliased or pixelated. The new default font smoothing (`'subpixel'`) ensures crisp, high-quality text output out-of-the-box.

## [0.2.0] - 2025-07-10

### Added

- **Font Fallback System:** Implemented a robust font fallback mechanism. `pictex` now automatically finds a suitable font for characters not present in the primary font, including emojis and special symbols. A `canvas.font_fallbacks()` method was added for user-defined fallbacks.

## [0.1.0] - 2025-07-09

- Initial release.
