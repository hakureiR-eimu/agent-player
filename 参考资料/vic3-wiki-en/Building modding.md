---
title: Building modding
source: https://vic3.paradoxwikis.com/Building_modding
pageid: 5328
categories: [Potentially_outdated, 1.9, Modding]
fetched: 2026-10-27
---
Please help with verifying or updating older sections of this article. At least some were last verified for [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) 1.9.

Buildings
**Game folder The folder where the files for this type are stored. :** `folder/path/after_game`

---

**Icon folder The folder where base game icons for this type typically go. :** `gfx/interface/icons/building_icons`

---

**Injectable Can INJECT database functions be used with this type? :** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) yes **Replaceable Can REPLACE database functions be used with this type? :** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) yes

---

**Related game objects:** Building groups, Production method groups

[Buildings](https://vic3.paradoxwikis.com/Buildings) are one of the foundational pillars of Victoria 3. Thus plenty of mods will want to add new buildings to the game. Further, [production methods](Production method.md) are integral to the functioning of a building, and as such this page also contains an explanation on how to mod those.

## Building groups

Building groups
**Game folder The folder where the files for this type are stored. :** `folder/path/after_game`

---

**Injectable Can INJECT database functions be used with this type? :** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) yes **Replaceable Can REPLACE database functions be used with this type? :** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) yes

---

**Related game objects:** Buildings

Each building belongs to a *building group*. Building groups are defined in /Victoria 3/game/common/building_groups and follow the following basic format:

```
[building_group]= {
	category = [urban/rural/development]
	
	economy_of_scale = [yes/no]
	
	cash_reserves_max = [integer]
	
	should_auto_expand = { 
		[trigger]
	}
	
	economy_of_scale_ai_factor = [float]
}
```

Each building group needs its own unique script name; by convention this is `bg_[script_name]`. Building groups can also have parent groups, from which they inherit and can also overwrite characteristics. So for example:

```
bg_manufacturing = {
	category = urban

	always_possible = yes
	
	economy_of_scale = yes
	
	cash_reserves_max = 25000
	
	should_auto_expand = { 
		default_auto_expand_rule = yes
	}
	
	economy_of_scale_ai_factor = 4.0
}

bg_light_industry = {
	parent_group = bg_manufacturing

	lens = light_industry
	
	urbanization = 20
	infrastructure_usage_per_level = 2
}
```

Child groups inherit all values from their parents, but can also define more characteristics themselves and will overwrite their parents' characteristics. Buildings themselves can further overwrite even their category values.

| Characteristic | Default value | Description | Example vanilla group |
|---|---|---|---|
| parent_group = [parent_group_key] | unset | This group is considered a child of the specified group. | Most |
| category = urban/rural/development | unset | Which part of the UI the building appears in | Top level groups |
| always_possible = yes/no | no | Buildings in this group are always permitted regardless of resources in state. | Manufacturing, government buildings |
| economy_of_scale = yes/no | no | Non-subsistence buildings in this group get an economy of scale throughput modifier for each level. | Most |
| is_subsistence = yes/no | no | Buildings in this group are considered subsistence buildings that follow special rules. | Subsistence farms |
| is_government_funded = yes/no | no | Buildings in this group have their expenses paid for by the government. | Government buildings, Ports |
| default_building = [building_type_key] | unset | Specifies the default building type that will be built unless the state specifies a different one. | Most rural buildings |
| lens = [lens_key] | unset | Determines the lens buildings in this group will be sorted under. | Everything |
| auto_place_buildings = yes/no | no | Buildings in this group are created automatically | Urban centers, gold fields, subsistance |
| capped_by_resources = yes/no | no | Buildings in this group are capped based on state resources. See: [Resource caps and farm types](Building modding.md) | Resource buildings like oil derricks, whaling stations, rubber plantations, logging camps etc |
| discoverable_resource = yes/no | no | Buildings in this group use the discoverable resource entry in a state. See: [Resource caps and farm types](Building modding.md) | Oil derricks, rubber, gold fields |
| depletable_resource = yes/no | no | Buildings in this group use the depletion entry in a state. See: [Resource caps and farm types](Building modding.md) | Gold fields |
| can_use_slaves = yes/no | no | Buildings in this group can "hire" slaves | Agriculture, mines, construction |
| land_usage = urban/rural | unset | Which type of state resource the building uses: urban = Urbanization, rural = Arable Land. | Urban centers use urban, agriculture uses arable land |
| cash_reserves_max = [integer] | 0 | Maximum amount of £ (per level) that buildings in this group can store into their cash reserves. If set to 0, uses the value from the parent group. | Every non-government building |
| inheritable_construction = yes/no | no | A construction of this building group will survive a state changing hands or a split state merging | Monuments and canals |
| stateregion_max_level = yes/no | no | Any building types in this group with the has_max_level property consider its level restrictions on state-region rather than state level | Public infrastructure |
| urbanization = [integer] | 0 | The amount of urbanization buildings in this group provides per level | Rural is 5, urban industry and admin is 20, mines are 10, canals are 100 |
| should_auto_expand = [trigger] | unset | Conditions when buildings in this group should auto-expand if auto-expand is toggled on (trigger on more specific group or building type overrides) If this trigger has any contents at all, the game will think the building is potentially auto-expandable, so do not write triggers that can never evaluate to true here | Nearly everything uses the scripted trigger "default_auto_expand_rule = yes" |
| min/max_hiring_rate = [float] | define valueNDefines::NEconomy::DEFAULT_MIN_HIRING_RATE/DEFAULT_MAX_HIRING_RATE | How much of the building's staffing level can be hired in a single week | Ownership buildings use "hiring_rate = 1.0" |
| proportionality_limit = [float] | define valueNDefines::NEconomy::EMPLOYMENT_PROPORTIONALITY_LIMIT | How high is the building's tolerance for pop types being out of proportion? | Ownership buildings use "proportionality_limit = 1.0" |
| hires_unemployed_only = yes/no | no | Buildings in this group may only hire from the unemployment pool. | Subsistance |
| fired_pops_become_radical = no | yes | Fired pops (e.g. from downgrading) won't become radicals. Used in buildings which auto-downgrade like Subsistence farms. | Conscription Centers, Subsistence |
| is_military = yes | no | Buildings in this group are considered military | Military buildings |
| subsidized = yes | no | buildings of this group will by default start the game subsidized (has no effect after campaign start) | Private infrastructure |
| ignores_productivity_when_hiring = yes | no | Used for subsistence agriculture and ownership buildings, allows hiring even without productivity | Subsistence Agriculture, ownership buildings |
| economy_of_scale_ai_factor = 1.5 | unset | Influences how much the AI will value grouping buildings of this group in the same state to get a high economy of scale bonus | Various resources have 2.0, others 1.5, government has 5.0 |
| foreign_investment_ai_factor = 1.5 | unset | Influence how much the AI will value investing into buildings of this group in other countries | Resources average 1.0; others average 0.5 |

## Buildings

Buildings are defined in /Victoria 3/game/common/buildings and follow the basic format below:

```
[building] = {
	building_group = [building_group]
	icon = [path]
	city_type = none
	levels_per_mesh = 5

	production_method_groups = {
		[production_method_groups]
	}

	required_construction = [int]
	
}
```

Each building needs its own unique script name; by convention this is `building_[script_name]`. Most buildings have several more characteristics.

| Characteristic | Default value | Description | Example vanilla building |
|---|---|---|---|
| building_group = [bg_key] | unset | Reference to building group, building groups define common properties of similar buildings | Everything |
| icon = "path/to/texture" | unset | Building icon | Everything |
| buildable = yes/no | yes | Can this building be manually built | Gold fields, monuments, urban centers, etc. all have "no" |
| expandable = yes/no | yes | Can this building be manually expanded | Gold fields, monuments, urban centers |
| downsizeable = yes/no | yes | Can this building be manually downsized | Gold fields, monuments, urban centers |
| unique = yes/no | no | Only one level of this building type can be built in the world and never by private investors | Monuments |
| has_max_level = yes/no | no | A modifier must be defined to determine max level | Ports, construction industry, military |
| ignore_stateregion_max_level = yes | no | If the building's building group has stateregion_max_level = yes, override it for this building type. Used in ports to have each owner of a split state have their own limit. | Ports |
| enable_air_connection = yes/no | no | The region with that building built is considered for air travel. Only used for aesthetic zeppelins | Skyscraper |
| port = yes/no | no | The building can connect different market areas | Port |
| unlocking_technologies = { [technology] } | unset | List of required (any) technologies to be able to build this building | Synthetics Plant, and basically everything |
| can_build_government = { [trigger] } | unset | Custom trigger (state scope) for building requirements by the government | Only Opium plantations (checks if opium is banned or not) |
| can_build_private = { [trigger] } | unset | Custom trigger (state scope) for building requirements by private investors | Only Opium plantations (checks if opium is banned or not) |
| construction_points = [int32] | unset | Number of construction points required for construction. For easy reference, can use pre-made variable names found in /Victoria 3/game/common/script_values/building_values.txt | construction_cost_high, construction_cost_very_low, construction_cost_medium, etc. |
| construction_modifier = { [modifier_definition] } | unset | Applied to the construction camp at a scale of weekly construction output / construction_points. Commonly used to add an additional cost of construction that will be consumed over the duration of construction | Unused |
| owners = [pop_type_key] | unset | Dividends and investment pool, if not set determined by building group or production methods | Unused |
| ownership_type = no_ownership/self/other | unset | type of the building ownership, no_ownership - can't own other buildings, dividends if any are paid to the state; self - can own only itself, pays dividends to the owning buildings; other - building can own other buildings, pays dividends only to own pops | Most use self |
| economic_contribution = 0.0-1.0 | 1.0 | Multiplier for taxes/gdp from this building, 0.0 for no taxes/gdp | Unused |
| min_raise_to_hire = [fixed_point] | define valueNEconomy.MIN_RAISE_TO_HIRE | Minimum required increase in salary for an employee to switch to working at this workplace | Subsistence farms |
| naval = yes/no | no | Navy or army, default no, only applicable to military buildings, which is determined by building group | Naval Base |
| canal = [canal_type_key] | unset | Reference to canal type, if set, marks the building as a canal | Canals |
| ai_value = [script_value] | define valueNAI.BUILDING_BASE_VALUE or NAI.GOVERNMENT_BUILDING_BASE_VALUE | AI value | Tool workshops, railways, gold mines |
| ai_subsidies_weight = [script_value] | 1.0 | How important the AI considers subsidizing this building to be | Unused |
| slaves_role = [pop_type_key] | define valueNPops.DEFAULT_POP_TYPE | Defines which profession slaves can replace. | Subsistence farms (other buildings have it set in their category) |
| production_methods = { [production_method_groups] } | unset | Which production method groups the building has. See [Production methods](Building modding.md) section | Everything |
| possible = { [trigger] } | unset | Condition to decide if a building should be possible to be build. | Fishing ports check if coastal, industry checking if not enacted industry ban law |
| should_auto_expand = { [trigger] } | unset | Under which conditions we should auto-expand if auto-expand is toggled on (overrides building group if present). If this trigger has any contents at all, the game will think the building is potentially auto-expandable, so do not write triggers that can never evaluate to true here. | Government administration, railways |
| city_type = none (city/farm/mine/port/wood) | none | Which type of hub this building affects graphically | Everything |
| generates_residences = yes/no | yes | If the building adds graphical residencies to the city | Unused |
| terrain_manipulator = [terrain_manipulator_key] | unset | Graphical terrain manipulator updated by the building | Farms, forestry, mines, ports |
| levels_per_mesh = [int32] | unset | How many levels is needed to add 1 extra building on the map, default 1, most use 5 | Everything |
| residence_points_per_level = [int32] | 1 | How many total "residence points" this building adds to its hub to determine residential buildings created | Urban centers and barracks have 0 |
| statue = yes | no | special building type for power bloc statues | Power bloc statues |
| meshes = { [meshes] } | unset | List of meshes used for dynamic terrain placement | Unused |
| entity_not_constructed = { [meshes] } | unset | Special buildings can show an entity while not constructed | Greenwich observatory |
| entity_under_construction = { [meshes] } | unset | Overwrite for under construction entity for special buildings | Various monuments such as the Hagia Sophia |
| entity_constructed = { [meshes] } | unset | Overwrite to use constructed entity for special buildings | Various monuments such as the Hagia Sophia |
| locator = [locator_type] | unset | Locator type for special buildings | Every monument and canal |
| lens = [infrastructure] | unset | Override for which lens the building type should appear in, otherwise specified on building group | Trade center |
| background = "path/to/texture" | unset | Background texture for building registry items |  |
| company_headquarter = yes | unset | Building functions as headquarters for a company | Company Headquarter |

### Resource caps and farm types

Limited buildings are often capped based on [state region definitions](State modding.md). As an example:

```
STATE_CALIFORNIA = {
    id = 326
    subsistence_building = "building_subsistence_farm"
    provinces = { list of provinces }
    traits = { "state_trait_central_valley" "state_trait_northern_california_coastal_forests" }
    city = "x5EF8F5"
    port = "x1116AA"
    farm = "x7A5DA6"
    mine = "x4C2D30"
    wood = "x607BA8"
    arable_land = 300
    arable_resources = { "building_wheat_farm" "building_livestock_ranch" "building_cotton_plantation" "building_vineyard" }
    capped_resources = {
        building_iron_mine = 33
        building_sulfur_mine = 40
        building_logging_camp = 13
        building_fishing_wharf = 14
    }
    resource = {
        type = "building_gold_field"
        depleted_type = "building_gold_mine"
        undiscovered_amount = 12
    }
    resource = {
        type = "building_oil_rig"
        undiscovered_amount = 50
    }
    naval_exit_id = 3153
}
```

The following state characteristics are relevant for buildings

| subsistence_building | Which building will be used for the default subsistence type, must be something defined as a subsistence building. |
|---|---|
| arable_land | This sets how much arable land there is available in the state. Every building with `land_usage = rural` uses and shares this cap. |
| arable_resources | The list of buildings that can be built with this state's arable land. |
| capped_resources | How many buildings of each type can be built, used when the building uses `capped_by_resources = yes`. |
| undiscovered_amount | This is just like the other type of resource cap, however it is not immediately visible to the player and requires both tech and some time to be revealed. Building needs to have `discoverable_resource = yes.` |
| discovered_amount | Like undiscovered_amount, but discovered. Basically, how many buildings of this type can be built from game start, but for a building that has `discoverable_resource = yes.` |
| depleted_type | For buildings with `depletable_resource = yes`. Once this resource is depleted in this state (based on various random rolls defined in [Defines](Defines.md) or through the `force_resource_depletion` effect), replaces and deletes buildings of the initial type with the second type, with amount as new cap. |

#### Discovery and depletion

Resource discovery and depletion uses the values in the [Defines](Defines.md) under [NEconomy](Defines.md)

| Define | Default value | Dev comment |
|---|---|---|
| BASE_RESOURCE_DISCOVER_CHANCE | 0.02 | # Per day (1.0 = 1%) |
| EMPLOYMENT_RESOURCE_DEPLETE_CHANCE | 0.005 | # Multiplied by number of fully employed levels of the building |
| RESOURCE_DISCOVER_MIN_FRACTION | 0.2 | # Min fraction of resources that will be discovered for each successful roll |
| RESOURCE_DISCOVER_MAX_FRACTION | 0.5 | # Max fraction of resources that will be discovered for each successful roll |
| FULLY_DISCOVERED_RESOURCE_DEPLETE_CHANCE_MULT | 1.0 | # The chance of a resource depleting is multiplied by this when all of the resource has been discovered |
| RESOURCE_DEPLETE_MIN_AMOUNT | 2 | # Min amount of resources that will be depleted for each successful roll |
| RESOURCE_DEPLETE_MAX_AMOUNT | 5 | # Max amount of resources that will be depleted for each successful roll |

While they are mostly self-explanatory, a lot of the very specifics of discovery and depletion are still hidden in the game. Here is some additional info for context, some of it coming from testing.[But more testing or information is needed]

As soon as a nation has discovers a technology that allows the construction of a building that uses `discoverable_resource = yes`, the game will start rolling discovery of that resource for each state of that nation with still some "undiscovered building" left. That roll is happening every day, and uses the `BASE_RESOURCE_DISCOVER_CHANCE` value, which by default means a 0.02% chance per day per state. If the roll is successful, between 20% to 50% of all remaining `undiscovered_amount` will be available to be build. Further, every other nation with a declared interest in that state gets a notification.

There are also some events related to discovery, that use the command `force_resource_discovery`. For example, after a nation researches Pumpjacks, that nation automatically gets a free and instant discovery of oil in one of its states. Similarly, the (relatively common) Rubber event forces rubber discovery in your state or an adjacent state.

If the building has `depletable_resource = yes`, the game will roll for depletion of that building in every state. The base chance is 0.005% per day multiplied by each fully employed level. So, if a Gold Field has 8 levels and is fully employed, that means that building has a 0.04% chance every day to succeed at the depletion roll. If it succeeds, between 2-5 level caps of that building will be removed and replaced with the same amount of levels of the relevant building in that resource's `depleted_type` entry.

## Production methods

### Production method groups

Production method groups
**Game folder The folder where the files for this type are stored. :** `folder/path/after_game`

---

**Icon folder The folder where base game icons for this type typically go. :** `gfx/interface/icons/generic_icons`

---

**Injectable Can INJECT database functions be used with this type? :** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) yes **Replaceable Can REPLACE database functions be used with this type? :** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) yes

---

**Related game objects:** Buildings, Production methods

Production method groups are sets of mutually exclusive production methods a building has access to, e.g. Bakeries, Sweeteners, Baking Powder.

Production method groups are defined in /Victoria 3/game/common/production_method_groups and follow the basic format below:

```
[production_method_group] = {
	texture = [path]
	production_methods = {
		[production_method]
	}
}
```

Each production method group needs its own unique script name; by convention this is `pmg_[script_name]`. There can be any number of production methods within a group, but only one can be active at a time.

| Characteristic | Default value | Description |
|---|---|---|
| is_hidden_when_unavailable = yes/no | no | Whether PMs in this group are visible at all if they cannot currently be switched to. Used for monuments. |
| ai_selection = most_productive | most_profitable | Affects how the AI chooses between PMs. Current options: most_profitable, most_productive. Most productive useful for things like government admin or ports. |
| texture = "path/to/texture" | unset | Icon used in the Buildings tab when multiple of the same kind of building have different PMs, e.g. mixed automation |

### Production methods

Production methods
**Game folder The folder where the files for this type are stored. :** `folder/path/after_game`

---

**Icon folder The folder where base game icons for this type typically go. :** `gfx/interface/icons/production_method_icons`

---

**Injectable Can INJECT database functions be used with this type? :** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) yes **Replaceable Can REPLACE database functions be used with this type? :** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) yes

---

**Related game objects:** Production method groups, [Goods](Goods modding.md)

Production methods set the input and output for buildings, and thus are highly impactful for the game. Production methods are defined in /Victoria 3/game/common/production_methods and follow the basic format below:

```
[production_method] = {
	texture = [path]
	
	building_modifiers = {
		workforce_scaled = {
			[modifiers]
		}

		level_scaled = {
			[modifiers]
		}
	}
}
```

Each production method needs its own unique script name; by convention this is commonly `pm_[script_name]` and often includes the building name to distinguish related variants. The above is just the most common set-up, but there are many characteristics and options.

| Characteristic | Default value | Description | Example |
|---|---|---|---|
| texture = [path] | unset | Icon |  |
| is_default = yes/no | no | Is this the default pm for its group? If no pm in a group is designated as the default, the first defined pm is considered the default. PRCAL-9862: certain functions consider the pm with the name pm_default or default as the default. |  |
| required_input_goods = [key] | unset | The listed goods need to be locally available to activate this pm. Used to check if local good exists locally. | Every PM that uses Electricity has `required_input_goods = electricity` |
| unlocking_laws = { [laws] } | unset | List of (any of) laws required to be able to activate this pm | Worker Cooperative Ownership unlocking_laws = { law_cooperative_ownership } |
| disallowing_laws = { [laws] } | unset | Laws that block the usage of this pm. | Publicly Traded disallowing_laws = { law_command_economy law_cooperative_ownership } |
| unlocking_technologies = { [technologies] } | unset | List of (any of) technologies required to be able to activate this pm. Most PMs are unlocked through this. | Publicly Traded unlocking_technologies = { mutual_funds } |
| unlocking_production_methods = { [production_methods] } | unset | List of (any of) PMs required to be able to activate this pm. These must refer to pm keys on the same building. Primarily used for automation methods to require also more advanced "primary" production. | Artillery Foundry's Publicly Traded unlocking_production_methods = { pm_smoothbores pm_breech_loaders pm_recoiled_barrels } |
| unlocking_global_technologies = { [technologies] } | unset | List of (any of) technologies that need to be invented in the world to be able to activate this pm. | Unused in vanilla |
| unlocking_principles = { [principles] } | unset | List of (any of) power bloc principles required to activate this pm. | Efficient Canning Practices |
| unlocking_identity = [power_bloc_identity] | unset | Power bloc identity that enables this pm | Power bloc statue methods |
| replacement_if_valid = [production_method] | unset | Automatically switches from current method to the listed production method if that one is valid | Vacuum Packaging |
| is_hidden_when_unavailable = yes | no | Hides production method while it is not selectable | Efficient Canning Practices |
| ai_weight = [integer] | 1.0 | Base AI weight | Unused in vanilla |
| pollution_generation = [float] | 0 | How much pollution does this building add to its state region while this pm is active (total pollution in state region is scaled by arable land) | Every "production" pm uses this, from agriculture to industry. Most PMs start at 5 and increase to 10 and then 15 with more advanced PMs. Most agriculture sits around 5, most industry 10-15, with some like oil refinery power generation is at a whopping 75 pollution. |

Production method effects are generally expressed through [modifiers](Modifier types.md), these can apply to the country, state, or building, and can be scaled by the building level, employment percentage, or unscaled.

| Characteristic | Description | Example |
|---|---|---|
| country_modifiers = { [modifiers] } | These modifiers are applied to the country if this pm is active. | Government Administration's Vertical Filing Cabinets country_modifiers = { workforce_scaled = { country_bureaucracy_add = 65 } } |
| state_modifiers = { [modifiers] } | These modifiers are applied to the state if this pm is active. | Railroads' Steam Trains state_modifiers = { workforce_scaled = { state_infrastructure_add = 25 } } |
| building_modifiers = { [modifiers] } | These modifiers are applied to the building if this pm is active. This is the most common modifier, because it is here where goods input and output are commonly housed. | Government Administration's Vertical Filing Cabinets building_modifiers = { workforce_scaled = { goods_input_paper_add = 20 } level_scaled = { building_employment_clerks_add = 4000 } } |
| timed_modifiers = { [scripted modifiers] } | These scripted modifiers are applied to the building after pm is changed. Duration is BUILDING_TIMED_MODIFIER_WEEKS. Most commonly and exclusively used for shifting military PMs to cause a temporary debuff. | Barracks' Squad Infantry timed_modifiers = { pm_offense_defense_readjustment_minor } Unused since patch 1.5. |
| workforce_scaled = { [modifiers] } | These modifiers are multiplied by the building level, then scaled by the employment level of the building as a percentage. This is most commonly used with goods input and output. | Furniture Industry's Precision Tools workforce_scaled = { # input goods goods_input_hardwood_add = 25 goods_input_tools_add = 10 goods_input_wood_add = -25 # output goods goods_output_furniture_add = -55 goods_output_luxury_furniture_add = 55 } |
| level_scaled = { [modifiers] } | These modifiers are multiplied by the level of the building. Most commonly used with employment level. | Furniture Industry's Precision Tools level_scaled = { building_employment_shopkeepers_add = 1000 } |
| unscaled = { [modifiers] } | These modifiers remain static for any level or employment percentage. Used primarily for things like ownership shares, or for mortality. | Mines' Nitroglycerinunscaled = { building_laborers_mortality_mult = 0.3 building_machinists_mortality_mult = 0.2 building_engineers_mortality_mult = 0.1 } |

For how to implement new custom goods as input and output, see [Goods modding#Building use](Goods modding.md). A similar process applies to add other new effects such as custom professions.

## Map models

Feel that something is missing in this article?
+
Add it to this article
and help other players!
Please note the
style guidelines
.

## Building script documentation

### Building scope

The following [effects](Effect.md), [event targets](Event target.md), and [triggers](Trigger.md) can be used in building scope.

| Effect | Description | Example | Targets |
|---|---|---|---|
| add_modifier | Adds a timed modifier effect to object in scope | add_modifier = { name = static_modifier_name days/weeks/months/years = value (optional) #can use scripted values, negative values are permanent multiplier = value (optional) #multiplies the values of the static modifier is_decaying = yes (optional) #sets modifier to decay in strength over its duration } add_modifier = static_modifier_name #set as permanent modifier with no multiplier or decay |  |
| every_combat_unit | Iterate through all combat units of input scope | every_combat_unit = { limit = { <triggers> } #optional <effects> } | new_combat_unit |
| ordered_combat_unit | Iterate through all combat units of input scope | ordered_combat_unit = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | new_combat_unit |
| random_combat_unit | Iterate through all combat units of input scope | random_combat_unit = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | new_combat_unit |
| remove_modifier | Removes a timed modifier effect to object in scope | remove_modifier = static_modifier_name |  |
| set_subsidized | Sets whether a building is subsidized | set_subsidized = yes/no |  |

| Trigger | Description | Example | Targets |
|---|---|---|---|
| any_combat_unit | Iterate through all combat units of input scope | any_combat_unit = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | new_combat_unit |
| building_has_goods_shortage | Check if building has a shortage of any of its inputs | building_has_goods_shortage = yes/no | boolean |
| can_queue_building_levels | Checks if the building's owner could queue the provided number of additional levels without hitting a level or resource potential cap | can_queue_building_levels = number |  |
| cash_reserves_available | Evaluates a production building's available cash reserves | cash_reserves_available > 25000 | value |
| cash_reserves_ratio | Evaluates a production building's available cash reserve ratio compared to its maximum Returns 1 if the building has no maximum cash reserves | cash_reserves_ratio > 0.2 | value |
| country_ownership_fraction | Compares the fraction of this building's levels that are owned by a country | country_ownership_fraction > 0.5 | value |
| earnings | Compare a building's current annual earnings per employee | earnings >= 10 | value |
| fraction_of_levels_owned_by_country | Compares the fraction of total levels of a building a country or investors in that country owns | fraction_of_levels_owned_by_country = { target = c:GBR value > 0.5 } | value |
| has_active_production_method | Checks if a scoped building has the specified production method active | has_active_production_method = key |  |
| has_deployed_units | Check if a building supports any units which have been deployed outside of home HQ | has_deployed_units = yes/no | boolean |
| has_employee_slots_filled | Checks whether the amount of employees of a certain poptype are above or below a given percentage of the total amount the building can currently hire. I.e. if a building is at 80% (given as 0.8) of its current hiring capacity for Shopkeepers, for example. | has_employee_slots_filled = { pop_type = <pop type> percent = <0-1 value> } |  |
| has_failed_hires | Checks if a building failed to hire someone last week | has_failed_hires = yes/no | boolean |
| has_modifier | Check if a supported scope has a certain timed modifier | has_modifier = <key> |  |
| is_buildable | Check if a building is buildable = yes (default) | is_buildable = yes/no | boolean |
| is_building_group | True if scope is a building of given group | building_group = building |  |
| is_building_type | True if scope is a building of given type | is_building_type = building |  |
| is_government_funded | Check if a building is is_government_funded | is_government_funded = yes/no | boolean |
| is_subsidized | Check if a building is being subsidized | is_subsidized = yes/no | boolean |
| is_subsistence_building | Check if a building is a subsistence building | is_subsistence_building = yes/no | boolean |
| is_under_construction | Checks if building is under construction | is_under_construction = bool | boolean |
| levels_owned_by_country | Compares how many levels a country or investors in that country own in a building | levels_owned_by_country = { target = c:GBR value >= 1 } | value |
| occupancy | Evaluates a building's current occupancy | occupancy < 0.25 | value |
| private_ownership_fraction | Compares the fraction of this building's levels that are privately owned | private_ownership_fraction > 0.5 | value |
| self_ownership_fraction | Compares the fraction of this building's levels that are owned by the building itself | self_ownership_fraction > 0.5 | value |
| weekly_profit | Checks whether the profits the building has made this week are above or below a given value | weekly_profit >= 20.0 | value |

| Event target | Description | To scope |
|---|---|---|
| group | Scope from a building object or type to its group | building_group |
| level | Scope to the level of a building | value |
| level_after_queued_constructions | Scope to the level of a building after all queued constructions finish | value |
| market | Scope to the market of the object | market |
| modifier | Scope to the value of the modifier type of specified key belonging to the current object, example: modifier:country_influence_add | boolean, value |
| owner | Scope to the owner country of object | country |
| region | Scope to the strategic region of the object! | strategic_region |
| state | Scope to the state of the object | state |
| training_rate | Scope to the current maximum weekly training rate of a building | value |
| type | Scope from an object to its type | amendment_type, building_type, company_type, diplomatic_play_type, harvest_condition_type, institution_type, interest_group_type, law_type, political_movement_type, ship_type, strait_type |

### Building modifier types

`building_` [modifier types](Modifier types.md) apply their effects to buildings. When applied to a country, they affect all buildings owned by that country; likewise when applied to a state, they apply to all buildings in the state.

| Modifier type | Localization | Type | Format | Notes |
|---|---|---|---|---|
| building_academics_job_attractiveness_mult | Job Attractiveness for Academics | multiplicative | percent, good |  |
| building_academics_mortality_mult | Mortality of Academics | multiplicative | percent, bad |  |
| building_academics_shares_add | Academics Pop Ownership Shares | additive | neutral |  |
| building_academics_standard_of_living_add | Standard of Living for Academics | additive | good |  |
| building_aristocrats_job_attractiveness_mult | Job Attractiveness for Aristocrats | multiplicative | percent, good |  |
| building_aristocrats_shares_add | Aristocrats Pop Ownership Shares | additive | neutral |  |
| building_aristocrats_standard_of_living_add | Standard of Living for Aristocrats | additive | good |  |
| building_arms_industry_throughput_add | Arms Industries building Throughput | additive | percent, good |  |
| building_art_academy_throughput_add | Arts Academy building Throughput | additive | percent, good |  |
| building_artillery_foundry_throughput_add | Artillery Foundry building Throughput | additive | percent, good |  |
| building_automotive_industry_throughput_add | Automotive Industries building Throughput | additive | percent, good |  |
| building_barrack_throughput_add | Barracks building Throughput | additive | percent, good |  |
| building_bureaucrats_job_attractiveness_mult | Job Attractiveness for Bureaucrats | multiplicative | percent, good |  |
| building_bureaucrats_shares_add | Bureaucrats Pop Ownership Shares | additive | neutral |  |
| building_bureaucrats_standard_of_living_add | Standard of Living for Bureaucrats | additive | good |  |
| building_capitalists_job_attractiveness_mult | Job Attractiveness for Capitalists | multiplicative | percent, good |  |
| building_capitalists_shares_add | Capitalists Pop Ownership Shares | additive | neutral |  |
| building_capitalists_standard_of_living_add | Standard of Living for Capitalists | additive | good |  |
| building_cash_reserves_mult | Maximum Cash Reserves | multiplicative | percent, good |  |
| building_chemical_plant_throughput_add | Fertilizer Plants building Throughput | additive | percent, good |  |
| building_clergymen_job_attractiveness_mult | Job Attractiveness for Clergymen | multiplicative | percent, good |  |
| building_clergymen_shares_add | Clergymen Pop Ownership Shares | additive | neutral |  |
| building_clergymen_standard_of_living_add | Standard of Living for Clergymen | additive | good |  |
| building_clerks_job_attractiveness_mult | Job Attractiveness for Clerks | multiplicative | percent, good |  |
| building_clerks_shares_add | Clerks Pop Ownership Shares | additive | neutral |  |
| building_clerks_standard_of_living_add | Standard of Living for Clerks | additive | good |  |
| building_coal_mine_throughput_add | Coal Mines building Throughput | additive | percent, good |  |
| building_coffee_plantation_throughput_add | Coffee Plantations building Throughput | additive | percent, good |  |
| building_company_government_dividends_add | Company Government Dividends | additive | percent, neutral |  |
| building_company_worker_dividends_add | Company Workforce Dividends | additive | percent, neutral |  |
| building_construction_sector_throughput_add | Construction Sector building Throughput | additive | percent, good |  |
| building_cotton_plantation_throughput_add | Cotton Plantations building Throughput | additive | percent, good |  |
| building_dye_plantation_throughput_add | Dye Plantations building Throughput | additive | percent, good |  |
| building_economy_of_scale_level_cap_add | Economy of Scale Building Level Cap | additive | good |  |
| building_electrics_industry_throughput_add | Electrics Industries building Throughput | additive | percent, good |  |
| building_employment_academics_add | Academics Per Level | additive | neutral |  |
| building_employment_aristocrats_add | Aristocrats Per Level | additive | neutral |  |
| building_employment_bureaucrats_add | Bureaucrats Per Level | additive | neutral |  |
| building_employment_capitalists_add | Capitalists Per Level | additive | neutral |  |
| building_employment_clergymen_add | Clergymen Per Level | additive | neutral |  |
| building_employment_clerks_add | Clerks Per Level | additive | neutral |  |
| building_employment_engineers_add | Engineers Per Level | additive | neutral |  |
| building_employment_farmers_add | Farmers Per Level | additive | neutral |  |
| building_employment_laborers_add | Laborers Per Level | additive | neutral |  |
| building_employment_machinists_add | Machinists Per Level | additive | neutral |  |
| building_employment_officers_add | Officers Per Level | additive | neutral |  |
| building_employment_peasants_add | Peasants Per Level | additive | neutral |  |
| building_employment_shopkeepers_add | Shopkeepers Per Level | additive | neutral |  |
| building_employment_slaves_add | Slaves Per Level | additive | neutral |  |
| building_employment_soldiers_add | Servicemen Per Level | additive | neutral |  |
| building_engineers_job_attractiveness_mult | Job Attractiveness for Engineers | multiplicative | percent, good |  |
| building_engineers_mortality_mult | Mortality of Engineers | multiplicative | percent, bad |  |
| building_engineers_shares_add | Engineers Pop Ownership Shares | additive | neutral |  |
| building_engineers_standard_of_living_add | Standard of Living for Engineers | additive | good |  |
| building_explosives_factory_throughput_add | Explosives Factory building Throughput | additive | percent, good |  |
| building_farmers_job_attractiveness_mult | Job Attractiveness for Farmers | multiplicative | percent, good |  |
| building_farmers_standard_of_living_add | Standard of Living for Farmers | additive | good |  |
| building_fishing_wharf_throughput_add | Fishing Wharves building Throughput | additive | percent, good |  |
| building_food_industry_throughput_add | Food Industries building Throughput | additive | percent, good |  |
| building_furniture_manufactory_throughput_add | Furniture Manufacturies building Throughput | additive | percent, good |  |
| building_glassworks_throughput_add | Glassworks building Throughput | additive | percent, good |  |
| building_gold_field_throughput_add | Gold Fields building Throughput | additive | percent, good |  |
| building_gold_mine_throughput_add | Gold Mines building Throughput | additive | percent, good |  |
| building_goods_input_mult | Goods Input | multiplicative | percent, bad |  |
| building_government_administration_throughput_add | Government Administration building Throughput | additive | percent, good |  |
| building_iron_mine_throughput_add | Iron Mines building Throughput | additive | percent, good |  |
| building_job_attractiveness_mult | Job Attractiveness | multiplicative | percent, good |  |
| building_laborers_job_attractiveness_mult | Job Attractiveness for Laborers | multiplicative | percent, good |  |
| building_laborers_mortality_mult | Mortality of Laborers | multiplicative | percent, bad |  |
| building_laborers_shares_add | Laborers Pop Ownership Shares | additive | neutral |  |
| building_laborers_standard_of_living_add | Standard of Living for Laborers | additive | good |  |
| building_lead_mine_throughput_add | Lead Mines building Throughput | additive | percent, good |  |
| building_level_bureaucracy_cost_add | Building Level Bureaucracy Cost | additive | bad |  |
| building_livestock_ranch_throughput_add | Livestock Ranches building Throughput | additive | percent, good |  |
| building_machinists_job_attractiveness_mult | Job Attractiveness for Machinists | multiplicative | percent, good |  |
| building_machinists_mortality_mult | Mortality of Machinists | multiplicative | percent, bad |  |
| building_machinists_shares_add | Machinists Pop Ownership Shares | additive | neutral |  |
| building_machinists_standard_of_living_add | Standard of Living for Machinists | additive | good |  |
| building_maize_farm_throughput_add | Maize Farms building Throughput | additive | percent, good |  |
| building_millet_farm_throughput_add | Millet Farms building Throughput | additive | percent, good |  |
| building_minimum_incorporated_subsistence_employment_add | Protected Subsistence Employment in Incorporated States | additive | percent, neutral |  |
| building_minimum_wage_mult | Building Wage Target | multiplicative | percent, neutral |  |
| building_mobilization_cost_mult | Mobilization Goods Requirements | multiplicative | percent, bad |  |
| building_motor_industry_throughput_add | Motor Industries building Throughput | additive | percent, good |  |
| building_munition_plant_throughput_add | Munition Plants building Throughput | additive | percent, good |  |
| building_nationalization_cost_mult | Nationalization Compensation | multiplicative | percent, bad |  |
| building_nationalization_investment_return_add | Nationalization Investment Return | additive | percent, good |  |
| building_nationalization_radicals_mult | Radicals from Nationalization | multiplicative | percent, bad |  |
| building_naval_administration_hiring_rate_mult | Naval Administration Hiring Speed | multiplicative | percent, good |  |
| building_naval_administration_throughput_add | Naval Administration building Throughput | additive | percent, good |  |
| building_naval_administration_training_rate_add | Naval Administration Training Rate | additive | good |  |
| building_naval_administration_training_rate_mult | Naval Administration Training Rate | multiplicative | percent, good |  |
| building_officers_job_attractiveness_mult | Job Attractiveness for Officers | multiplicative | percent, good |  |
| building_officers_shares_add | Officers Pop Ownership Shares | additive | neutral |  |
| building_officers_standard_of_living_add | Standard of Living for Officers | additive | good |  |
| building_opium_plantation_throughput_add | Opium Plantations building Throughput | additive | percent, good |  |
| building_paper_mill_throughput_add | Paper Mills building Throughput | additive | percent, good |  |
| building_peasants_job_attractiveness_mult | Job Attractiveness for Peasants | multiplicative | percent, good |  |
| building_peasants_standard_of_living_add | Standard of Living for Peasants | additive | good |  |
| building_port_throughput_add | Port building Throughput | additive | percent, good |  |
| building_power_plant_throughput_add | Power Plants building Throughput | additive | percent, good |  |
| building_railway_throughput_add | Railway building Throughput | additive | percent, good |  |
| building_rice_farm_throughput_add | Rice Farms building Throughput | additive | percent, good |  |
| building_rubber_plantation_throughput_add | Rubber Plantations building Throughput | additive | percent, good |  |
| building_rye_farm_throughput_add | Rye Farms building Throughput | additive | percent, good |  |
| building_self_investment_chance_add | Building Self-Investment Chance | additive | percent, neutral |  |
| building_shipyard_throughput_add | Shipyards building Throughput | additive | percent, good |  |
| building_shopkeepers_job_attractiveness_mult | Job Attractiveness for Shopkeepers | multiplicative | percent, good |  |
| building_shopkeepers_shares_add | Shopkeepers Pop Ownership Shares | additive | neutral |  |
| building_shopkeepers_standard_of_living_add | Standard of Living for Shopkeepers | additive | good |  |
| building_silk_plantation_throughput_add | Silk Plantations building Throughput | additive | percent, good |  |
| building_slaves_mortality_mult | Mortality of Slaves | multiplicative | percent, bad |  |
| building_slaves_standard_of_living_add | Standard of Living for Slaves | additive | good |  |
| building_soldiers_job_attractiveness_mult | Job Attractiveness for Servicemen | multiplicative | percent, good |  |
| building_soldiers_shares_add | Servicemen Pop Ownership Shares | additive | neutral |  |
| building_soldiers_standard_of_living_add | Standard of Living for Servicemen | additive | good |  |
| building_steel_mill_throughput_add | Steel Mills building Throughput | additive | percent, good |  |
| building_subsistence_farm_throughput_add | Subsistence Farms building Throughput | additive | percent, good |  |
| building_subsistence_output_add | Subsistence Output | additive | neutral |  |
| building_subsistence_output_mult | Subsistence Output | multiplicative | percent, neutral |  |
| building_sugar_plantation_throughput_add | Sugar Plantations building Throughput | additive | percent, good |  |
| building_sulfur_mine_throughput_add | Sulfur Mines building Throughput | additive | percent, good |  |
| building_synthetics_plant_throughput_add | Synthetics Plants building Throughput | additive | percent, good |  |
| building_tea_plantation_throughput_add | Tea Plantations building Throughput | additive | percent, good |  |
| building_textile_mill_throughput_add | Textile Mills building Throughput | additive | percent, good |  |
| building_throughput_add | Throughput | additive | percent, good |  |
| building_tobacco_plantation_throughput_add | Tobacco Plantations building Throughput | additive | percent, good |  |
| building_tooling_workshop_throughput_add | Tooling Workshops building Throughput | additive | percent, good |  |
| building_trade_center_throughput_add | Trade Center building Throughput | additive | percent, good |  |
| building_training_rate_add | Training Rate | additive | good |  |
| building_training_rate_mult | Training Rate | multiplicative | percent, good |  |
| building_unincorporated_subsistence_output_mult | Subsistence Output in Unincorporated States | multiplicative | percent, good |  |
| building_unincorporated_throughput_add | Throughput in Unincorporated States | additive | percent, good |  |
| building_university_throughput_add | University building Throughput | additive | percent, good |  |
| building_urban_center_throughput_add | Urban Center building Throughput | additive | percent, good |  |
| building_vineyard_throughput_add | Vineyards building Throughput | additive | percent, good |  |
| building_whaling_station_throughput_add | Whaling Stations building Throughput | additive | percent, good |  |
| building_wheat_farm_throughput_add | Wheat Farms building Throughput | additive | percent, good |  |
| building_working_conditions_mult | Dangerous Working Conditions | multiplicative | percent, bad |  |

### Building group modifier types

`building_group_` [modifier types](Modifier types.md) apply their effects to all buildings in the group. When applied to a country, they affect all buildings in that group owned by that country; likewise when applied to a state, they apply to all buildings in that group in the state.

| Modifier type | Localization | Type | Format | Notes |
|---|---|---|---|---|
| building_group_bg_agriculture_allowed_collectivization_add | Minimum Worker-Owned Agriculture Building Levels | additive | percent, good |  |
| building_group_bg_agriculture_construction_efficiency_add | Agriculture Construction Efficiency | additive | percent, good |  |
| building_group_bg_agriculture_employee_mult | Agriculture Employees | multiplicative | percent, bad |  |
| building_group_bg_agriculture_farmers_mortality_mult | Mortality of Farmers employed in Agriculture | multiplicative | percent, bad |  |
| building_group_bg_agriculture_infrastructure_usage_mult | Infrastructure Usage of Agriculture buildings | multiplicative | percent, bad |  |
| building_group_bg_agriculture_laborers_mortality_mult | Mortality of Laborers employed in Agriculture | multiplicative | percent, bad |  |
| building_group_bg_agriculture_mortality_mult | Agriculture Employee Mortality | multiplicative | percent, bad |  |
| building_group_bg_agriculture_self_investment_chance_add | Agriculture Building Self-Investment Chance | additive | percent, neutral |  |
| building_group_bg_agriculture_standard_of_living_add | Agriculture Employee Standard of Living | additive | good |  |
| building_group_bg_agriculture_tax_mult | Agriculture Tax Income | multiplicative | percent, neutral |  |
| building_group_bg_agriculture_throughput_add | Agriculture Throughput | additive | percent, good |  |
| building_group_bg_arts_allowed_collectivization_add | Minimum Worker-Owned Arts Buildings Building Levels | additive | percent, good |  |
| building_group_bg_arts_throughput_add | Arts Buildings Throughput | additive | percent, good |  |
| building_group_bg_construction_infrastructure_usage_mult | Infrastructure Usage of Construction Sector buildings | multiplicative | percent, bad |  |
| building_group_bg_construction_laborers_mortality_mult | Mortality of Laborers employed in Construction | multiplicative | percent, bad |  |
| building_group_bg_extraction_allowed_collectivization_add | Minimum Worker-Owned Extraction Building Levels | additive | percent, good |  |
| building_group_bg_extraction_construction_efficiency_add | Extraction Construction Efficiency | additive | percent, good |  |
| building_group_bg_extraction_self_investment_chance_add | Extraction Building Self-Investment Chance | additive | percent, neutral |  |
| building_group_bg_extraction_throughput_add | Extraction Throughput | additive | percent, good |  |
| building_group_bg_fishing_employee_mult | Fishing Employees | multiplicative | percent, bad |  |
| building_group_bg_fishing_engineers_mortality_mult | Mortality of Engineers employed in Fishing Wharves | multiplicative | percent, bad |  |
| building_group_bg_fishing_laborers_mortality_mult | Mortality of Laborers employed in Fishing Wharves | multiplicative | percent, bad |  |
| building_group_bg_fishing_machinists_mortality_mult | Mortality of Machinists employed in Fishing Wharves | multiplicative | percent, bad |  |
| building_group_bg_fishing_mortality_mult | Fishing Employee Mortality | multiplicative | percent, bad |  |
| building_group_bg_fishing_standard_of_living_add | Fishing Employee Standard of Living | additive | good |  |
| building_group_bg_fishing_tax_mult | Fishing Tax Income | multiplicative | percent, neutral |  |
| building_group_bg_fishing_throughput_add | Fishing Industry Throughput | additive | percent, good |  |
| building_group_bg_government_construction_efficiency_add | Government Structures Construction Efficiency | additive | percent, good |  |
| building_group_bg_government_employee_mult | Government Employees | multiplicative | percent, bad |  |
| building_group_bg_government_mortality_mult | Government Employee Mortality | multiplicative | percent, bad |  |
| building_group_bg_government_standard_of_living_add | Government Employee Standard of Living | additive | good |  |
| building_group_bg_government_tax_mult | Government Tax Income | multiplicative | percent, neutral |  |
| building_group_bg_government_throughput_add | Government Structures Throughput | additive | percent, good |  |
| building_group_bg_heavy_industry_allowed_collectivization_add | Minimum Worker-Owned Heavy Industries Building Levels | additive | percent, good |  |
| building_group_bg_heavy_industry_construction_efficiency_add | Heavy Industries Construction Efficiency | additive | percent, good |  |
| building_group_bg_heavy_industry_engineers_mortality_mult | Mortality of Engineers employed in Heavy Industry | multiplicative | percent, bad |  |
| building_group_bg_heavy_industry_laborers_mortality_mult | Mortality of Laborers employed in Heavy Industry | multiplicative | percent, bad |  |
| building_group_bg_heavy_industry_machinists_mortality_mult | Mortality of Machinists employed in Heavy Industry | multiplicative | percent, bad |  |
| building_group_bg_heavy_industry_mortality_mult | Heavy Industry Employee Mortality | multiplicative | percent, bad |  |
| building_group_bg_heavy_industry_throughput_add | Heavy Industries Throughput | additive | percent, good |  |
| building_group_bg_infrastructure_construction_efficiency_add | Infrastructure Construction Efficiency | additive | percent, good |  |
| building_group_bg_infrastructure_employee_mult | Infrastructure Employees | multiplicative | percent, bad |  |
| building_group_bg_infrastructure_engineers_mortality_mult | Mortality of Engineers employed in Infrastructure | multiplicative | percent, bad |  |
| building_group_bg_infrastructure_laborers_mortality_mult | Mortality of Laborers employed in Infrastructure | multiplicative | percent, bad |  |
| building_group_bg_infrastructure_machinists_mortality_mult | Mortality of Machinists employed in Infrastructure | multiplicative | percent, bad |  |
| building_group_bg_infrastructure_mortality_mult | Infrastructure Employee Mortality | multiplicative | percent, bad |  |
| building_group_bg_infrastructure_self_investment_chance_add | Infrastructure Building Self-Investment Chance | additive | percent, neutral |  |
| building_group_bg_infrastructure_standard_of_living_add | Infrastructure Employee Standard of Living | additive | good |  |
| building_group_bg_infrastructure_tax_mult | Infrastructure Tax Income | multiplicative | percent, neutral |  |
| building_group_bg_infrastructure_throughput_add | Infrastructure Throughput | additive | percent, good |  |
| building_group_bg_light_industry_allowed_collectivization_add | Minimum Worker-Owned Light Industries Building Levels | additive | percent, good |  |
| building_group_bg_light_industry_construction_efficiency_add | Light Industries Construction Efficiency | additive | percent, good |  |
| building_group_bg_light_industry_laborers_mortality_mult | Mortality of Laborers employed in Light Industry | multiplicative | percent, bad |  |
| building_group_bg_light_industry_machinists_mortality_mult | Mortality of Machinists employed in Light Industry | multiplicative | percent, bad |  |
| building_group_bg_light_industry_throughput_add | Light Industries Throughput | additive | percent, good |  |
| building_group_bg_logging_employee_mult | Logging Industry Employees | multiplicative | percent, bad |  |
| building_group_bg_logging_engineers_mortality_mult | Mortality of Engineers employed in Logging | multiplicative | percent, bad |  |
| building_group_bg_logging_laborers_mortality_mult | Mortality of Laborers employed in Logging | multiplicative | percent, bad |  |
| building_group_bg_logging_machinists_mortality_mult | Mortality of Machinists employed in Logging | multiplicative | percent, bad |  |
| building_group_bg_logging_mortality_mult | Logging Industry Employee Mortality | multiplicative | percent, bad |  |
| building_group_bg_logging_slaves_mortality_mult | Mortality of Slaves employed in Logging | multiplicative | percent, bad |  |
| building_group_bg_logging_standard_of_living_add | Logging Industry Employee Standard of Living | additive | good |  |
| building_group_bg_logging_tax_mult | Logging Industry Tax Income | multiplicative | percent, neutral |  |
| building_group_bg_logging_throughput_add | Logging Industry Throughput | additive | percent, good |  |
| building_group_bg_logging_unincorporated_throughput_add | Forestries Throughput in Unincorporated States | additive | percent, good |  |
| building_group_bg_manor_houses_aristocrats_standard_of_living_add | Standard of Living of Aristocrats employed in Manor Houses | additive | good |  |
| building_group_bg_manufacturing_allowed_collectivization_add | Minimum Worker-Owned Manufacturing Industries Building Levels | additive | percent, good |  |
| building_group_bg_manufacturing_employee_mult | Manufacturing Employees | multiplicative | percent, bad |  |
| building_group_bg_manufacturing_engineers_mortality_mult | Mortality of Engineers employed in Manufacturing | multiplicative | percent, bad |  |
| building_group_bg_manufacturing_engineers_standard_of_living_add | Standard of Living of Engineers employed in Manufacturing | additive | good |  |
| building_group_bg_manufacturing_laborers_mortality_mult | Mortality of Laborers employed in Manufacturing | multiplicative | percent, bad |  |
| building_group_bg_manufacturing_laborers_standard_of_living_add | Standard of Living of Laborers employed in Manufacturing | additive | good |  |
| building_group_bg_manufacturing_machinists_mortality_mult | Mortality of Machinists employed in Manufacturing | multiplicative | percent, bad |  |
| building_group_bg_manufacturing_machinists_standard_of_living_add | Standard of Living of Machinists employed in Manufacturing | additive | good |  |
| building_group_bg_manufacturing_mortality_mult | Manufacturing Employee Mortality | multiplicative | percent, bad |  |
| building_group_bg_manufacturing_self_investment_chance_add | Manufacturing Industries Building Self-Investment Chance | additive | percent, neutral |  |
| building_group_bg_manufacturing_standard_of_living_add | Manufacturing Employee Standard of Living | additive | good |  |
| building_group_bg_manufacturing_tax_mult | Manufacturing Tax Income | multiplicative | percent, neutral |  |
| building_group_bg_manufacturing_throughput_add | Manufacturing Industries Throughput | additive | percent, good |  |
| building_group_bg_manufacturing_unincorporated_throughput_add | Manufacturing Industries Throughput in Unincorporated States | additive | percent, good |  |
| building_group_bg_military_construction_efficiency_add | Military Buildings Construction Efficiency | additive | percent, good |  |
| building_group_bg_military_industry_allowed_collectivization_add | Minimum Worker-Owned Military Industries Building Levels | additive | percent, good |  |
| building_group_bg_military_industry_construction_efficiency_add | Military Industries Construction Efficiency | additive | percent, good |  |
| building_group_bg_military_industry_engineers_mortality_mult | Mortality of Engineers employed in Military Industry | multiplicative | percent, bad |  |
| building_group_bg_military_industry_laborers_mortality_mult | Mortality of Laborers employed in Military Industry | multiplicative | percent, bad |  |
| building_group_bg_military_industry_machinists_mortality_mult | Mortality of Machinists employed in Military Industry | multiplicative | percent, bad |  |
| building_group_bg_military_industry_mortality_mult | Military Industry Employee Mortality | multiplicative | percent, bad |  |
| building_group_bg_military_industry_throughput_add | Military Industries Throughput | additive | percent, good |  |
| building_group_bg_military_throughput_add | Military Buildings Throughput | additive | percent, good |  |
| building_group_bg_mining_allowed_collectivization_add | Minimum Worker-Owned Mines Building Levels | additive | percent, good |  |
| building_group_bg_mining_employee_mult | Mining Employees | multiplicative | percent, bad |  |
| building_group_bg_mining_engineers_mortality_mult | Mortality of Engineers employed in Mines | multiplicative | percent, bad |  |
| building_group_bg_mining_engineers_standard_of_living_add | Standard of Living of Engineers employed in Mines | additive | good |  |
| building_group_bg_mining_laborers_mortality_mult | Mortality of Laborers employed in Mines | multiplicative | percent, bad |  |
| building_group_bg_mining_laborers_standard_of_living_add | Standard of Living of Laborers employed in Mines | additive | good |  |
| building_group_bg_mining_machinists_mortality_mult | Mortality of Machinists employed in Mines | multiplicative | percent, bad |  |
| building_group_bg_mining_machinists_standard_of_living_add | Standard of Living of Machinists employed in Mines | additive | good |  |
| building_group_bg_mining_mortality_mult | Mining Employee Mortality | multiplicative | percent, bad |  |
| building_group_bg_mining_slaves_mortality_mult | Mortality of Slaves employed in Mines | multiplicative | percent, bad |  |
| building_group_bg_mining_standard_of_living_add | Mining Employee Standard of Living | additive | good |  |
| building_group_bg_mining_tax_mult | Mining Tax Income | multiplicative | percent, neutral |  |
| building_group_bg_mining_throughput_add | Mines Throughput | additive | percent, good |  |
| building_group_bg_mining_unincorporated_throughput_add | Mines Throughput in Unincorporated States | additive | percent, good |  |
| building_group_bg_oil_extraction_employee_mult | Oil Industry Employees | multiplicative | percent, bad |  |
| building_group_bg_oil_extraction_engineers_mortality_mult | Mortality of Engineers employed in Oil Extraction | multiplicative | percent, bad |  |
| building_group_bg_oil_extraction_laborers_mortality_mult | Mortality of Laborers employed in Oil Extraction | multiplicative | percent, bad |  |
| building_group_bg_oil_extraction_machinists_mortality_mult | Mortality of Machinists employed in Oil Extraction | multiplicative | percent, bad |  |
| building_group_bg_oil_extraction_mortality_mult | Oil Industry Employee Mortality | multiplicative | percent, bad |  |
| building_group_bg_oil_extraction_standard_of_living_add | Oil Industry Employee Standard of Living | additive | good |  |
| building_group_bg_oil_extraction_tax_mult | Oil Industry Tax Income | multiplicative | percent, neutral |  |
| building_group_bg_oil_extraction_throughput_add | Oil Extractors Throughput | additive | percent, good |  |
| building_group_bg_plantations_allowed_collectivization_add | Minimum Worker-Owned Plantations Building Levels | additive | percent, good |  |
| building_group_bg_plantations_construction_efficiency_add | Plantations Construction Efficiency | additive | percent, good |  |
| building_group_bg_plantations_employee_mult | Plantation Employees | multiplicative | percent, bad |  |
| building_group_bg_plantations_farmers_mortality_mult | Mortality of Farmers employed on Plantations | multiplicative | percent, bad |  |
| building_group_bg_plantations_infrastructure_usage_mult | Infrastructure Usage of Plantations | multiplicative | percent, bad |  |
| building_group_bg_plantations_laborers_mortality_mult | Mortality of Laborers employed on Plantations | multiplicative | percent, bad |  |
| building_group_bg_plantations_mortality_mult | Plantation Employee Mortality | multiplicative | percent, bad |  |
| building_group_bg_plantations_self_investment_chance_add | Plantations Building Self-Investment Chance | additive | percent, neutral |  |
| building_group_bg_plantations_slaves_mortality_mult | Mortality of Slaves employed in Plantations | multiplicative | percent, bad |  |
| building_group_bg_plantations_standard_of_living_add | Plantation Employee Standard of Living | additive | good |  |
| building_group_bg_plantations_tax_mult | Plantation Tax Income | multiplicative | percent, neutral |  |
| building_group_bg_plantations_throughput_add | Plantations Throughput | additive | percent, good |  |
| building_group_bg_plantations_unincorporated_throughput_add | Plantations Throughput in Unincorporated States | additive | percent, good |  |
| building_group_bg_power_allowed_collectivization_add | Minimum Worker-Owned Power Plants Building Levels | additive | percent, good |  |
| building_group_bg_power_self_investment_chance_add | Power Plants Building Self-Investment Chance | additive | percent, neutral |  |
| building_group_bg_private_infrastructure_allowed_collectivization_add | Minimum Worker-Owned Private Infrastructure Building Levels | additive | percent, good |  |
| building_group_bg_ranching_allowed_collectivization_add | Minimum Worker-Owned Ranches Building Levels | additive | percent, good |  |
| building_group_bg_ranching_construction_efficiency_add | Ranches Construction Efficiency | additive | percent, good |  |
| building_group_bg_ranching_farmers_mortality_mult | Mortality of Farmers employed in Ranching | multiplicative | percent, bad |  |
| building_group_bg_ranching_infrastructure_usage_mult | Infrastructure Usage of Ranches | multiplicative | percent, bad |  |
| building_group_bg_ranching_laborers_mortality_mult | Mortality of Laborers employed in Ranching | multiplicative | percent, bad |  |
| building_group_bg_ranching_mortality_mult | Ranching Employee Mortality | multiplicative | percent, bad |  |
| building_group_bg_ranching_self_investment_chance_add | Ranches Building Self-Investment Chance | additive | percent, neutral |  |
| building_group_bg_ranching_standard_of_living_add | Ranching Employee Standard of Living | additive | good |  |
| building_group_bg_ranching_tax_mult | Ranching Tax Income | multiplicative | percent, neutral |  |
| building_group_bg_ranching_throughput_add | Ranches Throughput | additive | percent, good |  |
| building_group_bg_rubber_employee_mult | Rubber Industry Employees | multiplicative | percent, bad |  |
| building_group_bg_rubber_laborers_mortality_mult | Mortality of Laborers employed on Rubber Plantations | multiplicative | percent, bad |  |
| building_group_bg_rubber_mortality_mult | Rubber Industry Employee Mortality | multiplicative | percent, bad |  |
| building_group_bg_rubber_slaves_mortality_mult | Mortality of Slaves employed on Rubber Plantations | multiplicative | percent, bad |  |
| building_group_bg_rubber_standard_of_living_add | Rubber Industry Employee Standard of Living | additive | good |  |
| building_group_bg_rubber_tax_mult | Rubber Industry Tax Income | multiplicative | percent, neutral |  |
| building_group_bg_rubber_throughput_add | Rubber Plantations Throughput | additive | percent, good |  |
| building_group_bg_rubber_unincorporated_throughput_add | Rubber Plantations Throughput in Unincorporated States | additive | percent, good |  |
| building_group_bg_service_employee_mult | Urban Center Employees | multiplicative | percent, bad |  |
| building_group_bg_service_mortality_mult | Urban Center Employee Mortality | multiplicative | percent, bad |  |
| building_group_bg_service_standard_of_living_add | Urban Center Employee Standard of Living | additive | good |  |
| building_group_bg_service_tax_mult | Urban Center Tax Income | multiplicative | percent, neutral |  |
| building_group_bg_service_throughput_add | Service Industries Throughput | additive | percent, good |  |
| building_group_bg_subsistence_agriculture_allowed_collectivization_add | Minimum Worker-Owned Subsistence Agriculture Building Levels | additive | percent, good |  |
| building_group_bg_subsistence_agriculture_peasants_standard_of_living_add | Standard of Living of Peasants employed in Subsistence Agriculture | additive | good |  |
| building_group_bg_subsistence_ranching_allowed_collectivization_add | Minimum Worker-Owned Subsistence Ranching Building Levels | additive | percent, good |  |
| building_group_bg_subsistence_ranching_peasants_standard_of_living_add | Standard of Living of Peasants employed in Subsistence Ranching | additive | good |  |
| building_group_bg_whaling_employee_mult | Whaling Employees | multiplicative | percent, bad |  |
| building_group_bg_whaling_laborers_mortality_mult | Mortality of Laborers employed in Whaling Stations | multiplicative | percent, bad |  |
| building_group_bg_whaling_machinists_mortality_mult | Mortality of Machinists employed in Whaling Stations | multiplicative | percent, bad |  |
| building_group_bg_whaling_mortality_mult | Whaling Employee Mortality | multiplicative | percent, bad |  |
| building_group_bg_whaling_standard_of_living_add | Whaling Employee Standard of Living | additive | good |  |
| building_group_bg_whaling_tax_mult | Whaling Tax Income | multiplicative | percent, neutral |  |
| building_group_bg_whaling_throughput_add | Whaling Industry Throughput | additive | percent, good |  |

### Building GUI script

Main article:
GUI script
| Function | Arguments | Output | Description |
|---|---|---|---|
| AccessConsumedGoods |  | Unknown | Category: const |
| AccessModifier |  | Modifier | Category: const |
| AccessOwnerPopsList |  | PopList | Category: const |
| AccessPopsList |  | PopList | Category: const |
| AccessProducedGoods |  | Unknown | Category: const |
| AccessProductionMethod | ProductionMethodGroup | ProductionMethod | Category: const |
| AccessProductionMethodGroups |  | Unknown | Category: const |
| AccessSelf |  | Building | Category: const |
| AccessShortageGoods |  | Unknown | Category: const |
| AccessState |  | State | Category: const |
| AccessStateRegion |  | StateRegion | Category: const |
| CalcInfrastructureUsage |  | CFixedPoint |  |
| CalcInputAvailabilityOutputMult |  | CFixedPoint |  |
| CalcInputGoodsShortageTargetPenalty |  | CFixedPoint |  |
| CalcInputGoodsShortageTargetPenaltyFromGoods | Unknown | CFixedPoint |  |
| CalcUrbanizationProvided |  | int32 |  |
| CanBeAffectedByInputShortage | ModifierEntry | bool |  |
| CanBePrivatized |  | bool |  |
| CancelConstruction |  | Command |  |
| Downsize |  | Command |  |
| GetAdjustHiringTargetDesc |  | CString | Category: nonconst |
| GetAllEmployeesTransferDesc |  | CString | Category: nonconst |
| GetAllFailedHiresDesc |  | CString | Category: nonconst |
| GetArmyManpower |  | int64 | Category: nonconst |
| GetArmyReadinessStatusDesc |  | CString | Category: nonconst |
| GetAutoDownsizeTooltip |  | CString | Category: nonconst |
| GetAutoExpandTooltip |  | CString | Category: nonconst |
| GetAutoExpandTriggers |  | CString | Category: nonconst |
| GetAverageAnnualEarningsPerEmployee |  | CFixedPoint | Category: nonconst |
| GetAverageAnnualEarningsPerEmployeeFormatted |  | CString | Category: nonconst |
| GetAverageAnnualWage |  | CFixedPoint | Category: nonconst |
| GetAverageAnnualWageBreakdown |  | CString | Category: nonconst |
| GetAverageAnnualWageBreakdownForPopType | PopType | CString | Category: nonconst |
| GetAverageAnnualWageForPopType | PopType | CFixedPoint | Category: nonconst |
| GetAverageAnnualWageForPopTypeDesc | Unknown | CString | Category: nonconst |
| GetAverageAnnualWageSubsidies |  | CFixedPoint | Category: nonconst |
| GetAverageStandardOfLiving |  | CFixedPoint | Category: nonconst |
| GetBalance |  | CFixedPoint | Category: nonconst |
| GetBalanceDesc |  | CString | Category: nonconst |
| GetBuildingAssets |  | Unknown | Category: nonconst |
| GetBuildingGroupName |  | CString | Category: nonconst |
| GetBuildingOwnerships |  | Unknown | Category: nonconst |
| GetBuildingType |  | BuildingType | Category: nonconst |
| GetCancelConstructionTooltip |  | CString | Category: nonconst |
| GetCappedAssetsLong |  | Unknown | Category: nonconst |
| GetCappedAssetsLongRest |  | Unknown | Category: nonconst |
| GetCappedAssetsShort |  | Unknown | Category: nonconst |
| GetCappedAssetsShortRest |  | Unknown | Category: nonconst |
| GetCappedOwnersLong |  | Unknown | Category: nonconst |
| GetCappedOwnersLongRest |  | Unknown | Category: nonconst |
| GetCappedOwnersShort |  | Unknown | Category: nonconst |
| GetCappedOwnersShortRest |  | Unknown | Category: nonconst |
| GetCashReservesTrend |  | DataTrend | Category: nonconst |
| GetCasualtiesDesc |  | CString | Category: nonconst |
| GetChangeProductionMethodPopQualificationsWarningBreakdown | ProductionMethod | CString | Category: nonconst |
| GetCombatUnitCapacity |  | int32 | Category: nonconst |
| GetCombatUnitCapacityDesc |  | CString | Category: nonconst |
| GetCombatUnitProduction |  | CString | Category: nonconst |
| GetCombatUnitProductionBreakdown |  | CString | Category: nonconst |
| GetCombatUnitTypes |  | Unknown | Category: nonconst |
| GetCombatUnits |  | Unknown | Category: nonconst |
| GetCombatUnitsIcon |  | CString | Category: nonconst |
| GetCombatUnitsInFormation | MilitaryFormation | Unknown | Category: nonconst |
| GetCompany |  | Company | Category: nonconst |
| GetConstructionProgressPercentage |  | float | Category: nonconst |
| GetConstructionRemainingWeeksDesc |  | CString | Category: nonconst |
| GetConstructionSpeedPerWeek |  | CFixedPoint | Category: nonconst |
| GetConstructionSpeedPerWeekDesc |  | CString | Category: nonconst |
| GetConsumption | Goods | CFixedPoint | Category: nonconst |
| GetConsumptionDesc | Goods | CString | Category: nonconst |
| GetConsumptionValue | Goods | CFixedPoint | Category: nonconst |
| GetCurrentCashReserves |  | CFixedPoint | Category: nonconst |
| GetCustom | CustomLocalization | CString | Category: nonconst |
| GetDebugTooltip |  | CString | Category: nonconst |
| GetDefaultOutputGoods |  | Goods | Category: nonconst |
| GetDownsizeTooltip |  | CString | Category: nonconst |
| GetEarnings |  | CFixedPoint | Category: nonconst |
| GetEarningsPerEmployeeTrend |  | DataTrend | Category: nonconst |
| GetEmployeeCap |  | int64 | Category: nonconst |
| GetEmployeesBreakdown |  | CString | Category: nonconst |
| GetEmployeesTransferDesc | PopType | CString | Category: nonconst |
| GetEmploymentPercentage |  | CFixedPoint | Category: nonconst |
| GetEmploymentTooltip |  | CString | Category: nonconst |
| GetEstablishmentDate |  | CString | Category: nonconst |
| GetExpansionLevel |  | int32 | Category: nonconst |
| GetExpansionLevelBreakdown |  | CString | Category: nonconst |
| GetExpansionLevelBreakdownDesc |  | CString | Category: nonconst |
| GetExpansionLevelDesc |  | CString | Category: nonconst |
| GetExpansionLevelsInQueue |  | int32 | Category: nonconst |
| GetFailedHiresDesc | PopType | CString | Category: nonconst |
| GetGoodsShortageListDesc |  | CString | Category: nonconst |
| GetGovernmentExpenses |  | CFixedPoint | Category: nonconst |
| GetGovernmentExpensesDesc |  | CString | Category: nonconst |
| GetHQ |  | Hq | Category: nonconst |
| GetID |  | int32 | Category: nonconst |
| GetIDString |  | CString | Category: nonconst |
| GetIcon |  | Unknown | Category: nonconst |
| GetInfrastructureUsageBreakdown |  | CString | Category: nonconst |
| GetInputMult |  | CFixedPoint | Category: nonconst |
| GetInputMultDesc |  | CString | Category: nonconst |
| GetInputOutputTooltip |  | CString | Category: nonconst |
| GetInputShortagePenalty |  | CFixedPoint | Category: nonconst |
| GetLastIncome |  | CFixedPoint | Category: nonconst |
| GetLastMaterialExpenses |  | CFixedPoint | Category: nonconst |
| GetLastMaterialExpensesDesc |  | CString | Category: nonconst |
| GetLastRevenue |  | CFixedPoint | Category: nonconst |
| GetLastRevenueBalancedSI | CFixedPoint int32 | CString | Category: nonconst |
| GetLastSlaveBasket |  | int32 | Category: nonconst |
| GetLastSlaveBasketDesc |  | CString | Category: nonconst |
| GetLastSlaveUpkeep |  | CFixedPoint | Category: nonconst |
| GetLastSlaveUpkeepDesc |  | CString | Category: nonconst |
| GetLastWagesExpenses |  | CFixedPoint | Category: nonconst |
| GetLastWagesExpensesDesc |  | CString | Category: nonconst |
| GetManpowerCapacity |  | int64 | Category: nonconst |
| GetMaxCashReserves |  | CFixedPoint | Category: nonconst |
| GetMaxPopSize | PopType | int64 | Category: nonconst |
| GetMaxPopSizeDesc | PopType | CString | Category: nonconst |
| GetMilitaryFormations |  | Unknown | Category: nonconst |
| GetMobilizationRatio |  | CFixedPoint | Category: nonconst |
| GetModifier |  | Modifier | Category: nonconst |
| GetName |  | CString | Category: nonconst |
| GetNameNoFormatting |  | CString | Category: nonconst |
| GetNationalizeBuildingNoCompensationDesc | Unknown | CString | Category: nonconst |
| GetNationalizeBuildingWithCompensationDesc | Unknown | CString | Category: nonconst |
| GetNavyManpower |  | int64 | Category: nonconst |
| GetNoLevelsCanBeNationalizedDesc |  | CString | Category: nonconst |
| GetNoOfEmployed |  | int64 | Category: nonconst |
| GetNotHiringReasonDesc |  | CString | Category: nonconst |
| GetNumActiveUnitsProvidedToFormation | MilitaryFormation | int32 | Category: nonconst |
| GetNumEmployeesOfType | PopType | int64 | Category: nonconst |
| GetNumLevelsCanBeNationalized |  | int32 | Category: nonconst |
| GetNumOwnedLevels |  | int32 | Category: nonconst |
| GetNumUnitsOfCombatUnitType | CombatUnitType | int32 | Category: nonconst |
| GetNumUnitsOfCombatUnitTypeProvidedToFormation | Unknown Unknown | int32 | Category: nonconst |
| GetNumberOfCombatUnits |  | int32 | Category: nonconst |
| GetNumberOfFullyMobilizedBattalions |  | int32 | Category: nonconst |
| GetOutputPercentage | Goods | CFixedPoint | Category: nonconst |
| GetOutputRatio |  | CFixedPoint | Category: nonconst |
| GetOwner |  | Country | Category: nonconst |
| GetPopTypeFullyReplacedDesc | PopType | CString | Category: nonconst |
| GetPopTypeReplacementDesc | PopType | CString | Category: nonconst |
| GetPrivatizationTooltip |  | CString | Category: nonconst |
| GetProducedModifiers |  | Modifier | Category: nonconst |
| GetProduction | Goods | CFixedPoint | Category: nonconst |
| GetProductionDesc | Goods | CString | Category: nonconst |
| GetProductionMethodGroup | Unknown | ProductionMethodGroup | Category: nonconst |
| GetProductionValue | Goods | CFixedPoint | Category: nonconst |
| GetProfitability |  | CString | Category: nonconst |
| GetProfitabilityCompareIcon |  | CString | Category: nonconst |
| GetProfitabilityCompareIconInType |  | CString | Category: nonconst |
| GetProfitabilityInType |  | CString | Category: nonconst |
| GetProfitabilityInTypeTrend |  | DataTrend | Category: nonconst |
| GetProfitabilityRank |  | int32 | Category: nonconst |
| GetProfitabilityRankInType |  | int32 | Category: nonconst |
| GetProfitabilityTrend |  | DataTrend | Category: nonconst |
| GetQueueConstructionPopQualificationsWarningBreakdown |  | CString | Category: nonconst |
| GetQueueConstructionTooltip |  | CString | Category: nonconst |
| GetQueueMilitaryConstructionTooltip | MilitaryFormation CombatUnitType | CString | Category: nonconst |
| GetResetProductionMethodsToStandardTooltip |  | CString | Category: nonconst |
| GetSamplePops |  | Unknown | Category: nonconst |
| GetSizeTooltip |  | CString | Category: nonconst |
| GetState |  | State | Category: nonconst |
| GetStateRegion |  | StateRegion | Category: nonconst |
| GetStatusDesc |  | CString | Category: nonconst |
| GetSubsidies |  | CFixedPoint | Category: nonconst |
| GetSubsidiesDesc |  | CString | Category: nonconst |
| GetSubsidizeTooltip |  | CString | Category: nonconst |
| GetSubsistenceOutput |  | CFixedPoint | Category: nonconst |
| GetSubsistenceOutputDesc |  | CString | Category: nonconst |
| GetSubventions |  | CFixedPoint | Category: nonconst |
| GetTariffsPaid |  | CFixedPoint | Category: nonconst |
| GetTaxationRevenue |  | CFixedPoint | Category: nonconst |
| GetTaxationRevenueTooltip |  | CString | Category: nonconst |
| GetThroughputBonusCurrent |  | CFixedPoint | Category: nonconst |
| GetThroughputBonusTarget |  | CFixedPoint | Category: nonconst |
| GetThroughputDesc |  | CString | Category: nonconst |
| GetTimedModifiers |  | Unknown | Category: nonconst |
| GetTogglePrivatizationTooltip |  | CString | Category: nonconst |
| GetTooltip |  | CString | Category: nonconst |
| GetTooltipTag |  | CString | Category: nonconst |
| GetTotalConsumptionValue |  | CFixedPoint | Category: nonconst |
| GetTotalExpenses |  | CFixedPoint | Category: nonconst |
| GetTotalExpensesBalancedSI | CFixedPoint int32 | CString | Category: nonconst |
| GetTotalProductionValue |  | CFixedPoint | Category: nonconst |
| GetTradeRevenue |  | CFixedPoint | Category: nonconst |
| GetTrainingRate |  | int64 | Category: nonconst |
| GetTrainingRateDesc |  | CString | Category: nonconst |
| GetUnitsProvidedToFormationBreakdown | MilitaryFormation | CString | Category: nonconst |
| GetUrbanizationProvidedBreakdown |  | CString | Category: nonconst |
| GetWageRate |  | CFixedPoint | Category: nonconst |
| GetWorstGoodsShortage |  | Goods | Category: nonconst |
| HasAnyInputShortage |  | bool |  |
| HasConstructionQueued |  | bool |  |
| HasFailedHires |  | bool |  |
| HasGovernmentConstructionQueued |  | bool |  |
| HasInputGoods |  | bool |  |
| HasInputShortage | Goods | bool |  |
| HasMaximumInputShortage | Goods | bool |  |
| HasOutputGoods |  | bool |  |
| HasPrivateConstructionQueued |  | bool |  |
| HasReachedLevelCap |  | bool |  |
| HasSlaves |  | bool |  |
| HasTradeRevenue |  | bool |  |
| IsActive |  | bool |  |
| IsActiveStr |  | CString |  |
| IsAutoDownsizing |  | bool |  |
| IsAutoExpanding |  | bool |  |
| IsBeingHighlighted |  | bool |  |
| IsBeingTutorialHighlighted |  | bool |  |
| IsBuildingType | BuildingType | bool |  |
| IsCappedBuilding |  | bool |  |
| IsCurrentlyUnderConstruction |  | bool |  |
| IsDownsizeable |  | bool |  |
| IsExpandable |  | bool |  |
| IsGovernmentFunded |  | bool |  |
| IsMilitaryBuilding |  | bool |  |
| IsOwner | Country | bool |  |
| IsPinnedInOutliner |  | bool |  |
| IsPotentialQueueConstruction |  | bool |  |
| IsRoleFullyReplacedByAnotherPopType | PopType | bool |  |
| IsSelfFunded |  | bool |  |
| IsSubsidized |  | bool |  |
| IsSubsistenceBuilding |  | bool |  |
| IsUrbanCenter |  | bool |  |
| IsValid |  | bool |  |
| MakeScope |  | Scope |  |
| NationalizeBuildingLevels | int32 | Command |  |
| ProvidesUrbanization |  | bool |  |
| QueueConstruction |  | Command |  |
| QueueMilitaryConstruction | MilitaryFormation CombatUnitType | Command |  |
| ResetProductionMethodsToStandard |  | Command |  |
| Self |  | Building |  |
| ShouldShowAsHiring |  | bool |  |
| ShouldShowAsUnableToHire |  | bool |  |
| ShouldShowAsUnwillingToHire |  | bool |  |
| ShowLevelAndMaxLevel |  | bool |  |
| SortBuildings | CString | void |  |
| ToggleAutoExpand |  | Command |  |
| ToggleAutoExpandOff |  | Command |  |
| ToggleAutoExpandOn |  | Command |  |
| TogglePinInOutliner |  | void |  |
| TogglePrivatization |  | Command |  |
| ToggleSubsidies |  | Command |  |
| ToggleSubsidiesOff |  | Command |  |
| ToggleSubsidiesOn |  | Command |  |
| UsesInfrastructure |  | bool |  |

| Function | Arguments | Output | Description |
|---|---|---|---|
| AccessSelf |  | BuildingGroup | Category: const |
| GetCustom | CustomLocalization | CString | Category: nonconst |
| GetName |  | CString | Category: nonconst |
| GetNameNoFormatting |  | CString | Category: nonconst |
| GetTooltipTag |  | CString | Category: nonconst |
| IsBuildingGroup | BuildingGroup | bool |  |
| MakeScope |  | Scope |  |
| Self |  | BuildingGroup |  |

| Function | Arguments | Output | Description |
|---|---|---|---|
| AccessProductionMethodGroups |  | Unknown | Category: const |
| AccessSelf |  | BuildingType | Category: const |
| ActivateExpansionLens |  | void |  |
| CanBeAutoExpanded |  | bool |  |
| CanBeSubsidized |  | bool |  |
| CanSwitchOwner |  | bool |  |
| CreatedByUrbanization |  | bool |  |
| FiredPopsBecomeRadical |  | bool |  |
| GetBackground |  | Unknown | Category: nonconst |
| GetBuildingGroup |  | BuildingGroup | Category: nonconst |
| GetBuildingGroupName |  | CString | Category: nonconst |
| GetBuildingKindDesc | Country | CString | Category: nonconst |
| GetBuildingModifier |  | Modifier | Category: nonconst |
| GetConstructionCosts |  | CString | Category: nonconst |
| GetCountryModifier |  | Modifier | Category: nonconst |
| GetCustom | CustomLocalization | CString | Category: nonconst |
| GetDiscoveredResourceName |  | CString | Category: nonconst |
| GetExpansionMissingQualificationsDesc | Unknown Unknown | CString | Category: nonconst |
| GetExpansionProductivityDesc | Unknown Unknown | CString | Category: nonconst |
| GetExpansionProductivityImpact | Building State | CFixedPoint | Category: nonconst |
| GetExpansionProductivityImpactDesc | Building State | CString | Category: nonconst |
| GetExpansionRevenueImpact | Building State | CFixedPoint | Category: nonconst |
| GetExpansionRevenueImpactDesc | Building State | CString | Category: nonconst |
| GetID |  | int32 | Category: nonconst |
| GetIDString |  | CString | Category: nonconst |
| GetIcon |  | Unknown | Category: nonconst |
| GetKey |  | CString | Category: nonconst |
| GetModifierEffectsAsString |  | CString | Category: nonconst |
| GetMonopolyCompanyIn | Unknown | Company | Category: nonconst |
| GetMonopolyCountryIn | Unknown | Country | Category: nonconst |
| GetName |  | CString | Category: nonconst |
| GetNameNoFormatting |  | CString | Category: nonconst |
| GetNumAvailableStatesForBuilding |  | int32 | Category: nonconst |
| GetNumLevelsInCountryFormatted | Country | CString | Category: nonconst |
| GetNumLevelsInCountryRaw | Country | int32 | Category: nonconst |
| GetNumLevelsOwnedByCompanyFormatted | Company | CString | Category: nonconst |
| GetNumLevelsOwnedByCompanyRaw | Company | int32 | Category: nonconst |
| GetProductivitySpanDesc | Country | CString | Category: nonconst |
| GetRequiredConstruction |  | CFixedPoint | Category: nonconst |
| GetResetProductionMethodsToStandardTooltip |  | CString | Category: nonconst |
| GetStandardProductionMethodDesc | Unknown | CString | Category: nonconst |
| GetStateModifier |  | Modifier | Category: nonconst |
| GetTabName |  | CString | Category: nonconst |
| GetToggleMonopolyEffectDesc |  | CString | Category: nonconst |
| GetTooltip |  | CString | Category: nonconst |
| GetTooltipForBuilding | Building | CString | Category: nonconst |
| GetTooltipForState | Unknown | CString | Category: nonconst |
| GetTooltipTag |  | CString | Category: nonconst |
| GetUrbanizationProvidedBreakdown |  | CString | Category: nonconst |
| HasCompanyMonopoly | Unknown | bool |  |
| HasCountryMonopoly |  | bool |  |
| HasInputGoods |  | bool |  |
| HasMonopoly |  | bool |  |
| HasOutputGoods |  | bool |  |
| HasRequiredPrinciplesInCountry | Country | bool |  |
| HasRequiredTechnologiesInCountry | Country | bool |  |
| IsAlwaysSelfOwning |  | bool |  |
| IsBeingHighlighted |  | bool |  |
| IsBeingTutorialHighlighted |  | bool |  |
| IsBuildable |  | bool |  |
| IsBuildableInAnyState | Country | bool |  |
| IsCappedBuilding |  | bool |  |
| IsDownsizeable |  | bool |  |
| IsExpandable |  | bool |  |
| IsGovernmentFunded |  | bool |  |
| IsMilitaryBuilding |  | bool |  |
| IsRural |  | bool |  |
| IsSelfFunded |  | bool |  |
| IsSubsistenceBuilding |  | bool |  |
| IsUnique |  | bool |  |
| IsUrban |  | bool |  |
| IsUsingArableLand |  | bool |  |
| IssDevelopment |  | bool |  |
| MakeScope |  | Scope |  |
| ProvidesUrbanization |  | bool |  |
| RecruitsCombatUnits |  | bool |  |
| ResetProductionMethodsToStandard |  | Command |  |
| Self |  | BuildingType |  |
| ToggleMonopoly |  | Command |  |
| UsesInfrastructure |  | bool |  |

| Promote | Arguments | Output | Description |
|---|---|---|---|
| AccessModifier |  | Modifier | Category: const |
| AccessOwnerPopsList |  | PopList | Category: const |
| AccessPopsList |  | PopList | Category: const |
| AccessProductionMethod | ProductionMethodGroup | ProductionMethod | Category: const |
| AccessState |  | State | Category: const |
| AccessStateRegion |  | StateRegion | Category: const |
| GetBuildingType |  | BuildingType | Category: nonconst |
| GetCompany |  | Company | Category: nonconst |
| GetDefaultOutputGoods |  | Goods | Category: nonconst |
| GetHQ |  | Hq | Category: nonconst |
| GetModifier |  | Modifier | Category: nonconst |
| GetOwner |  | Country | Category: nonconst |
| GetProducedModifiers |  | Modifier | Category: nonconst |
| GetProductionMethodGroup | Unknown | ProductionMethodGroup | Category: nonconst |
| GetState |  | State | Category: nonconst |
| GetStateRegion |  | StateRegion | Category: nonconst |
| GetWorstGoodsShortage |  | Goods | Category: nonconst |
| MakeScope |  | Scope |  |

| Promote | Arguments | Output | Description |
|---|---|---|---|
| MakeScope |  | Scope |  |

| Promote | Arguments | Output | Description |
|---|---|---|---|
| GetBuildingGroup |  | BuildingGroup | Category: nonconst |
| GetBuildingModifier |  | Modifier | Category: nonconst |
| GetCountryModifier |  | Modifier | Category: nonconst |
| GetMonopolyCompanyIn | Unknown | Company | Category: nonconst |
| GetMonopolyCountryIn | Country | Country | Category: nonconst |
| GetStateModifier |  | Modifier | Category: nonconst |
| MakeScope |  | Scope |  |

## Localization

Main article:
Localization
Each building group, building, production method group and production method must be localized in a .yml file in the localization folder within your mod.

```
[building]: "X"
[building]_lens_option: "Expand X"
[building_group]: "X"
[production_method_group]: "X"
[production_method]: "X"
```

## References

Modding
Return to top
| Documentation | [Defines](Defines.md) • [Effects](Effect.md) • [Event targets](Event target.md) • [Scopes](Scope.md) • [Triggers](Trigger.md) [Macros](Macro.md) • [Modifier types](Modifier types.md) • [On actions](https://vic3.paradoxwikis.com/On_actions) • [Script value](Script value.md) • [Variables](Variable.md) |
|---|---|

| Scripted content | [Decisions](Decision modding.md) • [Events](Event modding.md) • [History](History modding.md) • [Journal](Journal modding.md) • [Modifiers](Modifier modding.md) • Objectives • [Scripted gui](Scripted gui.md) |
|---|---|

| Scripted types | Buildings • [Characters](Character modding.md) • Concepts • [Countries](Country modding.md) • [Culture](Culture modding.md) • [Decrees](Decree modding.md) • [Diplomacy](Diplomacy modding.md) • [Goods](Goods modding.md) • [Institutions](Institution modding.md) • [Interest groups](Interest group modding.md) • [Laws](Law modding.md) • Parties • [Pops](Pop modding.md) • [Power blocs](Power bloc modding.md) • [Religion](Religion modding.md) • Subject types • [Technology](Technology modding.md) • [Treaties](Treaty modding.md) • [War goals](War goal modding.md) |
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
