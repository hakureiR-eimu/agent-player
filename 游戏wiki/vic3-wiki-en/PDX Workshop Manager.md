---
title: PDX Workshop Manager
source: https://vic3.paradoxwikis.com/PDX_Workshop_Manager
pageid: 9897
categories: [Modding_tools, Modding]
fetched: 2026-10-27
---
Modding tool
: PDX Workshop Manager
PDX Workshop Manager
---

Type
Steam Workshop
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

Other
Download
PDX Workshop Manager
---

Type
Steam Workshop
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

Other
Download
**pdx-workshop-manager** is a tool to publish paradox mods, to the steam workshop in a repeatable and configurable way.

There are both **Windows** and **Linux** builds. If requested a **MacOSX** build can be added.

Thanks to [nnnn20430](https://github.com/nnnn20430) for creating a go based wrapper of the original steamworks API.

## Features

- Updating the workshop **name** for different languages based on configuration or the `metadata.json`
- Updating the workshop **tags** based on the tags in the `metadata.json`
- Updating the workshop **description** for different languages based on configured files
- Updating the workshop **thumbnail**
- Adding a **change note** to workshop update based on a configured directory

## How does it work?

The tool will parse the `metadata.json` of either a provided configured mod or each configured mod and then publish the mod to the steam workshop.

## Configuration

The tool is configured using a json file.

### Attributes

- **REQUIRED** `game` steam app id of the game to upload for
- **REQUIRED** `mods`a list of mods that can be uploaded
- **REQUIRED** `id` id of the mod to upload, if kept `0` it will create the mod on the first upload and replace the id with the newly created one
- **REQUIRED** `directory` location of the mod, either a relative path from the executable or an absolute path
- **REQUIRED** `thumbnail` thumbnail file located in the mod directory (defaults to `thumbnail.png`)
- **OPTIONAL** `names` map of steam [api language code](https://partner.steamgames.com/doc/store/localization/languages) to localized mod names (defaults to the name defined in the `metadata.json`)
- **OPTIONAL** `descriptions` map of steam [api language code](https://partner.steamgames.com/doc/store/localization/languages) to file containing the localized steam description bbcode
- **OPTIONAL** `change-note-directory` directory containing files with version based change notes (see change notes)

### Example JSON config

```
{
  "game": 529340,
  "mods": [
    {
      "id": 0,
      "directory": "/Path/To/Mod",
      "thumbnail": "thumbnail.png",
      "names": {
        "english": "Your mod name"
      },
      "descriptions": {
        "english": "/Path/To/Bbcode/File/STEAM_PAGE.bbcode"
      },
      "change-note-directory": "/Path/To/Change/Note/Directory"
    }
  ]
}
```

## Adding Workshop Change Notes

The application will try to add change notes if a `change-note-directory` is defined.

It does this by reading the `version` attribute from the `metadata.json` and adding a `.bbcode` at the end.

So if a mod has the version `1.0.1` it will try to find a file called `1.0.1.bbcode` in the change note directory.

**NOTE** The upload will **not** fail if there is no corresponding change note, but just warn about it in the console output.

## Usage

First download the latest release from the Releases page of the repository:

- https://github.com/kaiser-chris/pdx-workshop-manager/releases

The ZIP may be marked as a *Virus*. This is a **false positive**!

If you do not trust this, then you can build it yourself.

### Graphical UI

Download the GUI version and after unzipping it simply run the provided executable.

The application will open a new browser window with the GUI.

It will allow you to set up mods to be uploaded and do the upload. **Make sure to save your changes before clicking upload.**

**NOTE** If no browser window opens, you can find a link to the GUI in the command line window.

### Command Line

Then, after configuration it, you can run the application by double-clicking, or running it in the terminal like this:

```
.\pdx-workshop-manager.exe
```

By default, the application expects the config file to be in the same folder as the executable and will upload **all** mods configured in it.

**NOTE** You need to have steam running and be logged in for the tool to work!

All optional commands can be found in the help dialog. Help dialog (`.\pdx-workshop-manager.exe -h`):

```
Usage of pdx-workshop-manager:
  -config string
    	Path to the config file (default "manager-config.json")
  -mod uint
    	Configured workshop mod id or 0 for all mods (default 0)
```

### Usage Tip

If you do not know how to open the command line on Windows:

- Open the folder containing the `pdx-deepl.exe`
- Click into the top address bar of the explorer
- Clear it
- Write `cmd` and press enter
- Now you should have a command line window open

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
