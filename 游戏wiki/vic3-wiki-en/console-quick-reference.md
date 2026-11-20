---
title: Console 命令速查表（自动提取）
source: https://vic3.paradoxwikis.com/Console_commands
extracted_from: Console commands.md
fetched: 2026-10-27
---

共 156 条命令，自动提取自 [Console commands](Console%20commands.md)；完整说明（含 debug mode 开启方法、按键、注意事项）见原页。

| 命令 | 说明 |
|---|---|
| `add_journal_entry [journal entry type]` | Add a specific journal entry to the player country |
| `add_mandates [amount]` | Adds mandates to current power bloc |
| `add_supply_ships [amount]` | Adds a specific quantity of supply ships immediately. |
| `ai_evaluate_autonomous_construction [<building key> <state region key>]` | Prints AI debug data for selected state & building type. |
| `ai_evaluate_company [<company type key>]` | Prints AI debug data for selected company. |
| `ai_evaluate_government_construction [<building key> <state region key>]` | Prints AI debug data for selected state & building type. |
| `ai_evaluate_interest [<strategic region key>]` | Prints AI debug data for selected strategic region declared interest. |
| `ai_evaluate_mobilization` | Prints AI debug data for mobilization. |
| `ai_evaluate_privatization [<building key> <state region key>]` | Prints AI debug data for selected state & building type. |
| `ai_evaluate_production_method [<building key> <pm key> <state region key>]` | Prints AI debug data for selected production method in state for building type. |
| `ai_evaluate_state [<state region key> <country tag>]` | Prints AI strategic value for selected state. |
| `ai_evaluate_subject [<country tag>]` | Prints AI debug data for selected subject. |
| `ai_evaluate_trade_route [<goods key> <country tag>]` | Prints AI debug data for selected goods & country trade partner. |
| `ai_evaluate_treaty_port [<state region key> <country tag>]` | Prints AI treaty port score. |
| `ai_evaluate_wargoal [<wargoal type> <country tag> <state region key>]` | Prints AI debug data for wargoal. |
| `annex [<country tag/id>]` | Annexes a country |
| `annex_all` | Annexes all other countries |
| `callstack` | Print the callstack |
| `change_law` | Changes a Law to the specified key (like "law_monarchy", etc) |
| `check_pollution_level [state region tag]` | Print out pollution for specified state region |
| `check_save` | Checks that saving and loading is consistent |
| `clearlines` | Clear lines |
| `clearspawnedentities` | Clears entities spawned with spawnentity command |
| `coa_preview_window` | Open the Coat of Arms Preview Window |
| `compound_nodeeditor` | Compound Node Editor |
| `conquerall [country tag]` | Set all enemy provinces under our control. |
| `crash` | Cause the application to crash |
| `create_ai [self/all/tag]` | Creates AI for country or countries |
| `create_building_history` | Creates a game-history compliant .txt file of all buildings in the world / state ID as well as their PM / subsidy configurations. |
| `create_political_movement [<movement type key>]` | Creates a political movement |
| `create_pop_history` | Creates a dump in debug.log with a complete pop history |
| `create_state_region_data` | Creates a game-database compliant .txt file of all state regions in the world and their provinces/resources |
| `cthulhu` | ? |
| `data_types_explorer` | Opens the data types explorer dockable |
| `data_wrappers_stats [Filter]` | Prints statistics about data wrappers |
| `date [date in format yyyy.mm.dd.hh]` | Changes current date |
| `debug [arguments]` | Various debugging actions. See [console command arguments](Console commands.md). |
| `debug_lens_option` | toggles the cheat mode debug_lens_option |
| `debug_mode` | Toggles debug mode |
| `debugcharacters` | Creates a semi-colon delimited logfile with debug info regarding all characters. |
| `debugcountrybudgets` | Creates a semi-colon delimited logfile with debug info regarding all countries and their budgets. |
| `debugemployment` | Creates and appends a comma-delimited logfile with debug info regarding employment in the specified state ID. |
| `debugmarkets` | Creates a semi-colon delimited logfile with debug info regarding all goods and markets. |
| `debugpopconsumption` | Creates a semi-colon delimited logfile with debug info regarding all pops' consumption |
| `debugpopwealth` | Creates a semi-colon delimited logfile of the current wealth status of all pops. |
| `debugstates` | Write a semi-colon delimited logfile with debug info regarding all states. |
| `debugterrainweights` | Prints out the number of |
| `debugtheaters` | Write a semi-colon delimited logfile with debug info regarding all theaters. |
| `deiron` | Disables Ironman mode |
| `disable_ai [all/tag]` | Disables AI |
| `disable_pop_growth` | toggles the cheat mode disable_pop_growth |
| `disable_retooling` | toggles the cheat mode disable_retooling |
| `drawcmdsviewer` | Draw Cmds Viewer |
| `dump_data_types` | dumps the registered data types |
| `enable_ai [all/tag]` | Enables AI |
| `entity_editor` | Entity Editor Dockable |
| `escalate [<amount>]` | Adds escalation to player diplomatic plays. |
| `explorer` | Shows an object explorer window |
| `exportbuildings` | Write a semi-colon delimited logfile with all building type info |
| `fastbattle` | toggles the cheat mode fastbattle (battles take one tick)**(affects AI)** |
| `fastbuild` | toggles the cheat mode fastbuild (makes all constructions instant) **(affects AI)** |
| `fastbuildships` | Produces ships immediately. |
| `fastcivilwars` | toggles the cheat mode fastcivilwars |
| `fastcolonize` | toggles the cheat mode fastcolonize **(affects AI)** |
| `fastenact` | toggles the cheat mode fastenact (enactment of policies is instant) |
| `fasthire` | toggles the cheat mode fasthire |
| `fastincorporate` | toggles the cheat mode fastincorporate (makes incorporation of states take 1 day) |
| `fastinstitutions` | toggles the cheat mode fastinstitutions |
| `fastinterests` | toggles the cheat mode fastinterests |
| `fastlobbies` | toggles the cheat mode fastlobbies |
| `fastmobilize` | toggles the cheat mode fastmobilize |
| `fastmovements` | toggles the cheat mode fastmovements |
| `fastresearch` | toggles the cheat mode fastresearch |
| `fastrevolution` | toggles the cheat mode fastrevolution |
| `fastsecession` | toggles the cheat mode fastsecession |
| `fastsecretgoals` | toggles the cheat mode fastsecretgoals |
| `fasttravels` | toggles the cheat mode fasttravels |
| `find_unemployed` | Find and report all unemployed pops with an optional cutoff |
| `fix_state_regions` | Fix state regions. |
| `force_oos` | Make this client go out of sync in multiplayer |
| `generate_province_center_objects` | generates a file with meshes in the center of each province |
| `gui_animation_editor` | GUI Animation Timeline Dockable |
| `gui_editor` | Spawns gui editor (removed in 1.9) |
| `help [command name]` | Print out all console commands or a specific command description. |
| `hq_show_id` | toggles the cheat mode hq_show_id |
| `ig_devout` | Devout |
| `ig_industrialists` | Industrialists |
| `ig_intelligentsia` | Intelligentsia |
| `ig_landowners` | Landowners |
| `ig_petty_bourgeoisie` | Petite Bourgeoisie |
| `ig_rural_folk` | Rural Folk |
| `ig_trade_unions` | Trade Unions |
| `ignore_government_support` | toggles the cheat mode ignore_government_support |
| `ignore_power_bloc_requirements` | toggles the cheat mode ignore_power_bloc_requirements (leverage requirements to leave and join) |
| `invalidate_character [character id]` | Invalidate the modifier on the character with the specified ID |
| `invalidate_country [country id]` | Invalidate the modifier on the country with the specified ID |
| `invalidate_ig [interest group id]` | Invalidate the modifier on the interest group with the specified ID |
| `invalidate_state [state id]` | Invalidate the modifier on the state with the specified ID |
| `io_stats` | Toggles IO Stats |
| `kill_character [character name]` | kills the named character |
| `log_status` | Log Status Dockable |
| `log_ticktask_performance` | Start outputing ticktask performance data to profiling.log |
| `log_viewer` | Log Viewer Dockable |
| `map_editor` | Toggle map editor |
| `mapmode [mapmode]` | Switches to a given mapmode |
| `measure_frame_time ["start" or "stop" measuring]` | Measures avg/min/max frame time and prints the result to debug.log once stopped |
| `memory_stats` | Toggles Memory Stats |
| `minidump [file path]` | Creates a minidump |
| `money [amount]` | Adds specified amount of money |
| `net_debuginfo` | Print debug info about the networking layer |
| `net_stats` | Toggles Net Stats |
| `norevolution` | toggles the cheat mode norevolution |
| `nosecession` | toggles the cheat mode nosecession |
| `noshortages` | Prevents penalties for supply shortages in buildings |
| `nosupportloss` | Prevent countries from losing war support |
| `observe` | start observing the game |
| `particleeditor` | Particle Node Editor |
| `permitmarginalizedingovernment` | toggles the cheat mode permitmarginalizedingovernment |
| `pops_account_disconnect_steam` | Disconnect Paradox account from Steam |
| `pops_account_logout` | Logout from a POPS Account |
| `pops_account_status` | Show whether you are currently logged into POPS or not. |
| `popstat` | Prints out amount of active pops. |
| `portrait_editor` | Open the portrait editor |
| `print_gamestate_modifiers` | Prints Gamestate Modifiers |
| `province_borders [true/false]` | Toggles showing of province borders |
| `recalc_cached_data` | Recalculate cached gamestate data. |
| `release_mode` | Toggles release mode |
| `reload [file name]` | Reloads assets |
| `rendertype` | Reports what render backend is used |
| `research` | Acquire technologies |
| `save_game_analyzer` | Open the save game analyzer |
| `screenshot` | Take screenshot |
| `script_docs` | Prints script documentation |
| `settings` | Spawns a settings GUI with an optional argument for an initially selected category |
| `shader_editor` | Shader Editor Dockable |
| `show_goals` | Show AI goals. |
| `skip_migration` | toggles the cheat mode skip_migration |
| `sleep` | Sleep for specified amount of milliseconds |
| `social_debuginfo` | Print debug info about the social layer |
| `switchlanguage [language name]` | Reload localization files and switch language |
| `tag [country_tag]` | Switch control to another country |
| `testaipacts` | Test whether AI would dissolve current pacts |
| `testobjective [<subgoal key (optional)>]` | Tests objective triggered effects |
| `texturelist` | Texture List |
| `textureviewer` | Texture Viewer |
| `time` | What time is it? |
| `treatyport [<state region tag>]` | Takes treaty port in state region |
| `tweak` | Spawns a tweaker GUI |
| `update_distribution` | Updates garrison unit distribution in HQ of specified State ID |
| `update_employment` | Transfers employees between buildings in the specified state ID. |
| `validate_employment` | Print out unemployment in states. |
| `validate_income` | Print out countries with income deficits. |
| `validate_pops` | Ensures all pops have valid params and prints them to the error log otherwise. |
| `version` | Shows current build information, put 1 as second parameter for long version |
| `vsync` | Toggle main swapchains vsync |
| `yesmen` | AI will agree to all diplomatic proposals & sway offers from players |
