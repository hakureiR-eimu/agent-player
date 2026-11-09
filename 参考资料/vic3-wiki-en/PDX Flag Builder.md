---
title: PDX Flag Builder
source: https://vic3.paradoxwikis.com/PDX_Flag_Builder
pageid: 9974
categories: [Modding_tools, Modding]
fetched: 2026-10-27
---
Modding tool
: PDX Flag Builder
PDX Flag Builder
Type
Flag Builder
---

Author(s)
Bahmut
---

Status
Released
---

Github
Link
---

Download
Link
PDX Flag Builder
Type
Flag Builder
---

Author(s)
Bahmut
---

Status
Released
---

Github
Link
---

Download
Link
**pdx-flag-builder** is a tool to build flags for Victoria 3 and Europa Universalis 5.

Example Screensho

## Usage

### Installation

Download the zip for your system from the [releases page](https://github.com/kaiser-chris/pdx-flag-builder/releases), extract it anywhere and run `pdx-flag-builder`.

On Linux the tool needs a distribution with glibc 2.38 or newer, such as Ubuntu 24.04, Debian 13 or Fedora 39, and its file dialogs need `zenity` or `kdialog`, one of which most desktops already have.

### Setup

The tool reads its flags and textures from the game and from your mods:

1. Open **Settings** (`Ctrl+,`).
2. Click **Add Folder** and then **Browse...**, and pick the game's `game` folder or the root folder of a mod.
3. Add as many folders as you like. A folder further down the list overrides the ones above it, the way a mod overrides the game.
4. Click **Save**.

### Finding a flag

**Databases → Flag Database** lists every coat of arms that was found, with a preview. **Databases → Texture Database** lists the patterns and emblems. Type into the search box to narrow a list down, and click a column header to sort it.

Click a flag to open it. **File → New Flag** starts from an empty one.

### Editing

The **Layers** panel lists the coat of arms and its layers. Click one to edit it in the **Selected Layer** panel:

- The coat of arms has its name, its pattern and its colours.
- An emblem has its texture, its colours, a mask that limits it to one colour of the pattern, and its placements: position, scale and rotation.
- A sub flag draws another coat of arms, with an offset and a scale.

Add layers with **Add Layer**, or straight from the texture database with **Add as Layer** and **Set as Pattern**, or from the flag database with **Add as Sub Flag**. The arrows next to a layer move it up and down; the layers further down are drawn on top.

Number fields are changed by dragging across them. Double-click one to type a number instead. Hold **Shift** while dragging for bigger steps, **Alt** for finer ones.

To move a placement with the keyboard, click the flag and use the arrow keys:

| Keys | Effect |
|---|---|
| Arrow keys | Move the selected placement |
| **Ctrl** + arrow keys | Scale it |
| **Alt** + left and right | Turn it |
| **Shift** with any of them | Ten times bigger steps |

**Ctrl+Z** undoes and **Ctrl+Y** redoes.

### Saving and exporting

| Menu entry | Effect |
|---|---|
| **File → Save** (`Ctrl+S`) | Writes the flag back into the file it came from. Only its own definition changes; the rest of the file stays as it is. |
| **File → Save To File...** (`Ctrl+Shift+S`) | Puts the flag into a file of your choosing, replacing a flag of the same name in it or adding it at the end. |
| **File → Copy Script** | Copies the flag's script to the clipboard. |
| **File → Export Image...** | Saves the flag as a 768 × 512 PNG image. |

Values a file wrote with `@variables` or `@[expressions]` are saved as the numbers they came to.

The tool asks before it throws away unsaved changes.

### Settings

**Settings → Interface Scale** makes the whole interface larger for high resolution displays. **View → Reset Layout** puts the panels back where they started.

Settings are stored in `%AppData%\pdx-flag-builder` on Windows and in `~/.config/pdx-flag-builder` on Linux.

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
