---
title: Handbook for Victoria 3 Interface Scripting
source: https://vic3.paradoxwikis.com/Handbook_for_Victoria_3_Interface_Scripting
pageid: 10117
categories: [Potentially_outdated, 1.9, Modding]
fetched: 2026-10-27
---
The **User Interface** is how players interact with Victoria 3. The interface is coded using a custom scripting language This language has no official name, but is referred to as "**GUIscript**" by the Modding Co-op. Currently, it is very poorly documented and less human-readable than [PDXscript](Introduction to the Paradox Scripting Language.md).

**GUIscript** is used for content contained in the `/game/gui` and `jomini/gui` folders.

Operations done solely in the interface are referred to as done *"in gui"* or as *"pure gui"* when no script-side functionality is used

*Note: This guide does not cover the Paradox Scripting Language which is used for scripted gameplay content.*

Please help with verifying or updating older sections of this article. At least some were last verified for [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) 1.9.

## Overview

### Basic Principles

In principle, GUIscript is similar to HTML. A `.gui` file is a tree of **parent** components and their **children**. Each component either creates a UI widget or sets the properties on its children.

```
window = {
    name = "my_panel"
    parentanchor = center
    size = { 500 300 }

    background = {
        using = default_background
    }

    vbox = {
        spacing = 8
        margin = { 16 16 }

        textbox = {
            text = "MY_PANEL_TITLE"
            fontsize = 22
        }

        textbox = {
            text = "MY_PANEL_BODY"
            autoresize = yes
            multiline = yes
        }

        button = {
            using = default_button
            size = { 0 40 }
            text = "MY_PANEL_CLOSE"
            onclick = "[PdxGuiWidget.AccessParent.AccessParent.Hide]"
        }
    }
}
```

For example, the above script can be explained as:

- Create a `window` with the `name` "my_panel", anchored at the `center` of its parent, with a `size` of 500px by 300px with a `background`
- Within the `background`, insert the settings defined by the template `default_background`
- Within the `window`, create a `vbox` with margins of 16px by 16x and a `spacing` of 8px between its children
- Within the `vbox`, create two `textbox` widgets and a `button` widget, each with their own settings

From this example, we have the following takeaways about GUIscript:

- The order in the file determines the order on the screen: what's "lower" in the code will be created later
- Most widgets can also contain other widgets. For example, there can be a `textbox` inside an `icon` inside a `button`. Nested elements, aka **children**, will be moved with their parent and can inherit properties from their parent
- A widget's position is set relative to the top left corner (either of the screen or the parent). This can be changed with `parentanchor` property
- Every element is opened and closed with curly brackets, like this: `container = { }`

There are also these important bits of information worth noting early on:

- Keys are either **widget kinds** or **properties**.
  - `vbox`, `textbox`, `button` and `background` create widgets
  - `size`, `spacing`, `text` and `onclick` set properties on the enclosing widget
- The `text` property is a **localization key** by default.
  - In the example above, `"MY_PANEL_TITLE"` is looked up in the localisation files, not printed literally
- Children **inherit properties** from their parents. Anything called within `[]` is an expression that is evaluated using the **datacontext** of the widget.
  - In the example above, we can see that the `button` widget started from its own context, and context-switches twice through two parents before executing the `Hide` command on its top-level parent

### File Structure

The user interface is defined by the files in the `/game/gui` and `jomini/gui` folders.

- Like scripted content, gui files can be edited by any text editor and are stored in plain text.
- All files within either `/gui` directory are loaded. Folder structure is ignored by the game engine *except in the case of scripted widgets*

Victoria 3 stores the vast majority of its graphical assets as `.dds` files. These are stored in the `/gfx` folder. The engine can also accept `.png` files in most cases, although this format is usually less space-efficient.

#### GUI Debug

Launching the game using the `-debug_mode` launch option will allow you to hotload changes to .gui files.

The engine will reload .gui files every time they are saved. The reload is usually immediate, although large changes can cause a more extensive reload of the interface.

#### Limitations

- It is only possible to switch context between contexts that have linking functions. For example, you cannot switch context between two countries without using script to feed a scope to the GUI

- The GUI cannot arbitrarily access script without use of an sgui.

## Interface Scripting & Construction

### How the Interface is Constructed

The displayed screen in Victoria 3 is produced by three cooperating layers:

```
   .gui file                      engine                      game script
┌──────────────────┐        ┌──────────────────┐        ┌──────────────────┐
│ widget tree      │  ───▶  │ layout, drawing, │  ◀───  │ triggers/effects │
│ + properties     │        │ input, animation │        │ scopes, values   │
│ + [ expressions ]│        │                  │        │ localisation     │
└──────────────────┘        └──────────────────┘        └──────────────────┘
```

Every interface in the game consists of these elements:

1. **Structure.** The `.gui` file declares a tree of widgets and sets properties on them. This is the part you will be working in most often.
2. **Presentation.** The engine lays the tree out, draws it, routes mouse and keyboard input, and runs animations. This
3. **Content.** Data-binding expressions, scripted GUIs, and localisation supply the text, numbers, lists and actions.

#### Widgets

The interface is built using **widgets**. In Victoria 3, a widget is a rectangle on screen with behavior attached. Every widget has:

| **Kind** | What it is (`window`, `vbox`, `button`, `textbox`, `icon`, ...) |
|---|---|
| **Properties** | How it is positioned, drawn and interacted with, etc. |
| **Children** | Other widgets nested inside of it. |

A widget's children are drawn on top of it and move with it. There is no separate "add child" call: nesting *is* the parent relationship.

### Built-in UI Components

Victoria 3 provides several basic components (kinds) to build interfaces. The kind is written as the key of the block:

```
vbox = {             # vbox is the kind
    spacing = 4
    textbox = { }    # textbox is the kind
}
```

#### Layout Widgets

| Kind | Purpose |
|---|---|
| `container` | A widget whose children keep their own absolute positions. Does not have a fixed size (but you can set maximumsize). Resizes automatically to fit all its children, including invisible ones. Use ignoreinvisible = yes to ignore them. Often used to group multiple elements to move them together. |
| `dynamicgridbox` | Is only used with datamodels. Arranges all the items vertically. Use flipdirection = yes to make it horizontal. Doesn't ignore invisible items by default. Use ignoreinvisible = yes to change it. Resized by the content and limited by minimumsize and maximumsize. Items can be of different size. Can become laggy with very long lists. |
| `fixedgridbox` | Similar to a dynamic box but all its items are of fixed size (it is essentially a table). Is only used with datamodels. Arranges all its items vertically. Use flipdirection = yes to make it horizontal. Cannot ignore invisible items. Can be fixed size, resized by the content and limited by minimumsize and maximumsize. Much better for performance with long lists. |
| `flowcontainer` | Arranges all its children in a horizontal row and resizes to fit them. Use direction = vertical to make it vertical. Wraps its children onto new rows or columns when it runs out of room. Doesn't ignore invisible children by default. Use ignoreinvisible = yes to change it. Can't have fixed size. Its children cannot have positions, as they are set automatically. If you need to adjust position of its child, you can put it inside a container or a widget and then change position relative to this parent. |
| `hbox` / `vbox` | Arranges all its children in a horizontal row and spreads them along its width. Vbox is the same but vertical. Can't have fixed size, instead resizes to fit its children or to the size of the parent, depending on the layout policy. Can be limited by minimumsize, maximumsize, min_width, max_width and margins. Ignores invisible children by default. Use ignoreinvisible = no to change this. Can optionally accept a datamodel (to create lists from game data). |
| `margin_widget` | Reserves a margin around a single child. Similar to a widget, but can be resized with margins. This allows us to make windows that resize to screens of different size, by setting height to 100% and margins to ~50 to show the hud. |
| `overlappingitembox` | Is only used with datamodels. Arranges all its items horizontally and overlaps them if the list is longer that the size of the box. Use flipdirection = yes to make it horizontal. Can be fixed size or autoresized. |
| `scrollarea` | A veiwport with scrollbars that appear if the content is bigger than its size. Scrollbars can be disabled with scrollbarpolicy_horizontal = always_off and scrollbarpolicy_vertical = always_off . Can be fixed size, resized by the content and limited by minimumsize and maximumsize. Game files primarily use a scrollbox type, which is a scrollarea with a background, scrollbar and margins. |
| `stackedwidget` | Shows one of its children at a time, selected by index. |
| `tabbar` | The button strip used by a tabwidget. |
| `tabwidget` | A tabbed container: a tab bar plus a stacked widget. |
| `widget` | The base widget. A bare rectangle that can be positioned, textured and shown or hidden, with no layout behaviour of its own. Clicking it will not bring it to the front If a child is outside of a window, it won't be clickable and won't show a tooltip. Use allow_outside = yes to change this. |
| `window` | A draggable, resizable top-level container. To enable movement, add movable = yes property. Can be fixed size or resized by its children. If a child is outside of a window, it won't be clickable and won't show a tooltip. Use allow_outside = yes to change this. Clicking a window will bring it to the front of other windows that share the same layer. Use PdxGuiWidget.StackTop or PdxGuiWidget.StackBottom to manipulate the order. |

#### Interaction Widgets

| Kind | Purpose |
|---|---|
| `button` | A clickable widget with over/down/disabled visual states. Accepts onclick and onrightclick . When adding a right click function, include button_ignore = none . Doesn't have a texture by default. Can be fixed size or resized by its children. A button without size can be used to add invisible hotkeys. |
| `button_group` | Keeps a set of checkbuttons mutually exclusive. |
| `checkbutton` | A toggle button with a checked state. |
| `colorpicker` | An HSV/RGB colour selection popup. |
| `dropDown` | A collapsing list of selectable items. |
| `scrollbar` | A draggable bar with decrement/increment buttons. |

#### Text Widgets

| Kind | Purpose |
|---|---|
| `editbox` | An editable single-line text field. |
| `textbox` | A non-editable block of text, with optional inline icons and text formatting. Can be fixed size or autoresized. Use elide = right or elide = left to cut off text that is too long Can be a single line or multiple, with multiline = yes . Game files primarily use types set in gui/shared/text.gui, like text_single . Use them to keep visual consistency and to type less code every time. |
| `texticon` | A textbox whose string may embed icon tokens. |

#### Visual Widgets

| Kind | Purpose |
|---|---|
| `background` | A texture drawn behind its parent widget. |
| `icon` | Draws a texture (optionally a sprite sheet) with an optional modify texture and glow. Can be used as a widget to store children. Can be flipped with mirror = horizontal or mirror = vertical . |
| `line` | A polyline or spline drawn between points. |
| `minimap` | Renders the map minimap texture. |
| `minimap_window` | The window that hosts the minimap. |
| `piechart` | A pie chart container. |
| `pieslice` | One slice of a piechart. |
| `plotline` | A line chart over a series of points. |
| `progressbar` | A horizontal or vertical bar showing a value in a range. |
| `treemapchart` | A treemap chart container. |
| `treemapslice` | One slice of a treemapchart. |

### Widget Properties

Properties are plain `key = value` entries. These are used to control the setting available to a given widget kind.

| Shape | Written as | Example |
|---|---|---|
| Boolean | `yes` / `no` | `visible = no` |
| Number | digits, optionally fractional or with `%` | `spacing = 10`, `size = { 100% 40 }` |
| Vector | two or more numbers in braces | `position = { 8 30 }` |
| Colour | four numbers in 0..1 | `tintcolor = { 0 0 0 0.6 }` |
| Token | a bare identifier | `direction = vertical` |
| Flags | identifiers joined by `\|` | `parentanchor = bottom\|hcenter` |
| String | quoted | `texture = "gfx/..."` |
| Expression | quoted, starts with `[` | `visible = "[IsInGame]"` |
| Block | braces | `size = { 280 132 }` |

### Data-binding and Inheritance

**Commands** are used when a widget needs to access or modify the gamestate. Command expressions are enclosed in quoted brackets `"[]"` and passed in as a widget property. Anything inside `"[]"` is evaluated by the game's data-binding engine. It starts from the widget's `datacontext` and is capable of chaining function calls and property accesses similar to dot linkage in PDXscript. For example:

```
visible  = "[Character.IsValid]"
text     = "[Character.GetName]"
tooltip  = "[Character.GetTooltip]"
onclick  = "[CharacterPanel.SelectCharacter(Character.Self)]"
```

Two properties control what an expression can access at runtime:

- `datacontext` pushes a new object as the root of `"[]"` for the widget and all of its children. By default, a widget inherits the datacontext of its parent.
- `datamodel` feeds a collection into a container, which instantiates its `item` block as a child for entry in the datamodel. Usually, each child will automatically inherit the datacontext of the specific object it has been provided from the datamodel.

```
dynamicgridbox = {
    datamodel = "[GetPlayer.GetStates]"
        item = { 
            textbox = {
                text = "[State.GetName]" 
            }
        }
    }
}
```

In the above example:

- The engine is instructed to create a `dynamicgridbox` widget.
- The `datamodel` property first changes context using `GetPlayer` (which returns the player's country), and then uses `GetStates` to retrieve a datamodel which contains a list of all states belonging to the country.
- `item` tells the engine to create a widget for every object in the datamodel provided by `GetStates`
- Any kinds or properties passed into `item` define what the spawned child widgets will contain.

#### Promotes and Functions

The data-binding engine operates through "contexts." These are analogous to the scopes of PDXscript in many ways. Predefined commands - promotes and functions - are used to move between objects, transform them, or retrieve information.

- **Promotes** return a game object, for example `Country.GetCapital` will change your context to the capital of that country
- **Functions** return a number, string, or boolean. For example `Country.GetArmyPowerProjection` will return the numerical value of that country's army power projection

### System Variables

### Type Casting

## Widget Usage and Properties

### window

### widget

### container

### dynamicgridbox / fixedgridbox

### flowcontainer

### hbox / vbox

### scrollarea

## Visuals & Appearance

### Textures

### Animation

## Interaction

### Callbacks

### Tooltips

### Focus

## User-Defined Types and Templates

### Types

### Templates

### Macros

## Scripted GUIs

### File Structure

### Invoking an SGUI

## Scripted Widgets

### Creating a Scripted Widget

### Registering a Scripted Widget

## Troubleshooting

### Known crash reasons

- Setting 100% size on hboxes and vboxes
- Using an `hbox` or `vbox` inside a `flowcontainer`
- Setting `resizeparent = yes` on multiple children in the same parent
- A type that references itself, this will lead to an endless loading screen until you run out of RAM

### Widget won't appear/disappear

- Syntax errors, like missing brackets or quotation marks
- Check for errors in the widget's `visible` property
- Make sure your types are set up correctly, they require the nest `types { type { } }` syntax, even if you've only created a single type in that file

## References

Modding
Return to top
| Documentation | [Defines](Defines.md) • [Effects](Effect.md) • [Event targets](Event target.md) • [Scopes](Scope.md) • [Triggers](Trigger.md) [Macros](Macro.md) • [Modifier types](Modifier types.md) • [On actions](https://vic3.paradoxwikis.com/On_actions) • [Script value](Script value.md) • [Variables](Variable.md) |
|---|---|

| Scripted content | [Decisions](Decision modding.md) • [Events](Event modding.md) • [History](History modding.md) • [Journal](Journal modding.md) • [Modifiers](Modifier modding.md) • Objectives • [Scripted gui](Scripted gui.md) |
|---|---|

| Scripted types | [Buildings](Building modding.md) • [Characters](Character modding.md) • Concepts • [Countries](Country modding.md) • [Culture](Culture modding.md) • [Decrees](Decree modding.md) • [Diplomacy](Diplomacy modding.md) • [Goods](Goods modding.md) • [Institutions](Institution modding.md) • [Interest groups](Interest group modding.md) • [Laws](Law modding.md) • Parties • [Pops](Pop modding.md) • [Power blocs](Power bloc modding.md) • [Religion](Religion modding.md) • Subject types • [Technology](Technology modding.md) • [Treaties](Treaty modding.md) • [War goals](War goal modding.md) |
|---|---|

| Map | [Map](Map modding.md) • [Geographic regions](Geographic region modding.md) • [States](State modding.md) |
|---|---|

| Interface | [Interface](Interface modding.md) • [GUI script](GUI script.md) • [Localization](Localization.md) • [Customizable localization](Localization.md) • [Script localization](Script localization.md) |
|---|---|

| Graphics | [3D Models](Model modding.md) • [Event images](Event images.md) • [Graphical Assets](Graphical asset modding.md) • Fonts • [Flags](Flag modding.md) |
|---|---|

| Audio | Music • [Sound](Sound modding.md) |
|---|---|

| Other | [AI](AI modding.md) • [Console commands](Console commands.md) • [Checksum](https://vic3.paradoxwikis.com/Checksum) • [Mods](Mod.md) • [Mod compatibility](Mod compatibility.md) • [Mod structure](Mod structure.md) • [Scripted tests](Scripted test.md) • [Troubleshooting](Troubleshooting.md) |
|---|---|

| Guides | [Mod translation](Mod translation.md) • [New country modding](New country modding.md) • [Save-game editing](Save-game editing.md) • [State modding guide](State modding guide.md) |
|---|---|
