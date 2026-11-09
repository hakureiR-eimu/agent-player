---
title: State modding
source: https://vic3.paradoxwikis.com/State_modding
pageid: 5744
categories: [Potentially_outdated, 1.9, Modding]
fetched: 2026-10-27
---
Please help with verifying or updating older sections of this article. At least some were last verified for [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) 1.9.

[States](https://vic3.paradoxwikis.com/States), or more properly state regions, are defined parts of the game map which contain pops and buildings, and are the primary layer for interactions on the map. State regions are defined in map_data/state_regions.

## Example state region

State regions are defined as a list of 'provinces', along with several characteristics.

```
STATE_SVEALAND = {
    id = 1
    subsistence_building = "building_subsistence_pastures"
    provinces = { "x0974E5" "x216569" "x24A2F1" "x298E7B" "x317138" "x36F523" "x3844C0" "x3E2C22" "x404643" "x41C729" "x432E07" "x45B6EF" "x4628A5" "x4836F2" "x4B02EB" "x4C9918" "x4FA424" "x604060" "x62D0D4" "x656512" "x6CF949" "x6E95C2" "x6F40EC" "x823263" "x8AC21D" "x90845E" "x93C3BC" "x93C76C" "x9686A5" "x9BBBE3" "xA001A0" "xA08021" "xA6C31B" "xA82FF7" "xA86C50" "xA9078A" "xB3F1FB" "xB90566" "xB9391F" "xBC0288" "xC0C0E0" "xC480A5" "xC8AEAF" "xCBFD28" "xCF16B1" "xD155CE" "xD702F7" "xD96FB9" "xE6C5FC" "xE7A6D6" "xE9B084" "xEA6A0F" "xEB5D5F" "xEFA14D" "xF08323" "xF48646" "xF8E400" "xFCCAFA" }
    traits = { "state_trait_bergslagen" "state_trait_scandinavian_forests" "state_trait_natural_harbors" }
    city = "x9686A5"
    port = "x93C3BC"
    farm = "xF48646"
    mine = "x6F40EC"
    wood = "x4C9918"
    arable_land = 30
    arable_resources = { "bg_rye_farms" "bg_livestock_ranches" }
    capped_resources = {
        bg_iron_mining = 36
        bg_lead_mining = 18
        bg_logging = 23
        bg_fishing = 11
    }
    resource = {
        type = "bg_oil_extraction"
        undiscovered_amount = 5
    }
    naval_exit_id = 3000
}
```

## Base characteristics

Each state region is defined with its unique script name and unique ID number. The script name also acts as a [localization](Localization.md) key.

All state regions must contain one or more 'provinces' tiles from the `provinces.png` map image. Provinces are defined by the six-digit [hex color](http://en.wikipedia.org/wiki/Web_colors#Hex_triplet) in that image, each prefixed by the letter `x` and optionally enclosed in double quotes.

Naval state regions (which define [sea nodes](Naval warfare.md)) contain precisely these characteristics and no more.

Example naval state region:

```
STATE_BALTIC_SEA = {
    id = 3000
    provinces = { "x08FAFA" }
}
```

## Additional characteristics

Land regions have a number of other characteristics.

### Impassable and prime land

States can have a list of impassable and prime land provinces. Both are relevant for split states as they affect the proportion of resources allocated to each state. Impassable provinces are not counted for the split state proportion and additionally block military fronts from forming. Prime land provinces give five times the weight for the split state proportion[1].

Both lists should only include provinces defined for the state region and should not include provinces from each other.

Example:

```
    provinces = { "x029E85" "x04BB3B" "x1C7417" "x2A3D46" "x42973E" "x4408AB" "x445D59" "x477680" "x4DD36E" "x56FE77" "x60FDC2" "x638173" "x6D4CDF" "x706E00" "x71D428" "x76E306" "x7FFBF0" "x8A69A7" "x939612" "x9910E9" "xA5A916" "xA67A6E" "xA6D36E" "xA91194" "xAD54BC" "xB7B05B" "xBC374E" "xC29C28" "xCF4105" "xD735DB" "xE02CB6" "xE3C4F2" "xF37396" "xF8375D" "xF9BDCB" "xFCFD83" "xFF8539" "xFFE074" }
    impassable = { "xA5A916" "xBC374E" "x04BB3B" "x9910E9" "xCF4105" "x477680" "x56FE77" }
    prime_land = { "xE02CB6" "x60FDC2" "x42973E" }
```

### Hubs

Hubs are defined provinces that represent a city within the state region. Visually, each type of hub appears and grows based on the number of buildings related to its type in the state region. Most hubs have no game mechanic interaction aside from updating the road/rail network by their presence or absence; port hubs define the location of treaty ports.

| Hub | Buildings |
|---|---|
| City | Everything not included in other hubs |
| Farm | All agriculture and plantations |
| Mine | All mines and oil rigs |
| Port | Shipyards and Military Shipyards Fishing and Whaling Industries Ports and Naval Bases |
| Wood | Logging Camps |

Hubs can overlap, such that the same province is two or more hubs, and not every state region has every type of hub, notably inland states have no port hub. Each hub is defined by listing the province which is used for that hub.

### State traits

Some state regions have a defined [state trait](https://vic3.paradoxwikis.com/State_trait). These are listed in a block `traits` with each trait listed in quotes with its script name. State traits are defined in common/state_traits.

A state trait is defined with a unique script name – which also acts as a localization key, an icon, and typically a modifier. State traits can also have a disabling technology, which suppresses its modifier or a technology required for colonization, which prevents colonization of state regions with the trait until that technology is researched.

Example state trait:

```
state_trait_severe_malaria = {
    icon = "gfx/interface/icons/state_trait_icons/severe_malaria.dds"
	
	required_techs_for_colonization = { "quinine" }
	disabling_technologies = { "malaria_prevention" }
	
	modifier = {
		state_non_homeland_colony_growth_speed_mult = -0.95
		state_non_homeland_mortality_mult = 0.25
	}
}
```

Effects can also add or remove state traits to state regions during gameplay.

### Resources

Resources in a state region come in a few types: arable land and resources, capped resources, and individual resources. In all cases, the resources are defined as [buildings](Building modding.md) and many of the resource characteristics are defined by the building's characteristics.

#### Arable land

Arable land is defined simply as an integer, along with a list of buildings that use arable land in the state region.

Example:

```
    arable_land = 30
    arable_resources = { "building_rye_farm" "building_livestock_ranch" }
```

Unutilized arable land is always taken up by a subsistence building, which is defined for each state region as the specific type of building, for example `subsistence_building = "building_subsistence_pastures"`.

The amount of arable land available can be changed by effect during gampeplay.

#### Capped resources

Capped resources are a block of buildings with a maximum level defined for each. These resources are always visible from the start of the game.

Example:

```
    capped_resources = {
        building_iron_mine = 36
        building_lead_mine = 18
        building_logging_camp = 23
        building_fishing_wharf = 11
    }
```

The amount or presence of a capped resource in a state region can be changed during gameplay.

#### Individual resources

Individual resources are similar to capped resources, but each one is defined in its own block. Most often these are used for discoverable resources, which are not immediately visible in game, and instead are revealed periodically once the state's owner has the required technology researched. Additionally, if a building is set as depletable, this block can define which building replaces it when it is depleted.

Example:

```
    resource = {
        type = "building_gold_field"
        depleted_type = "building_gold_mine"
        undiscovered_amount = 12
    }
    resource = {
        type = "building_rubber_plantation"
        discovered_amount = 10
        undiscovered_amount = 6
    }
    resource = {
        type = "building_oil_rig"
        undiscovered_amount = 5
    }
```

### Naval exit

Coastal state regions should have a `naval_exit_id`, which is simply the state region ID of a sea region. This defines which sea region/sea node is adjacent to this state region, for the purposes of shipping lanes and naval invasions.

## State history

See also:
New state modding
Starting state ownership is defined in common/history/states. Unmodified Victoria 3 puts all state history in the file `00_states.txt`, but it can be split into separate files for mods.

State history files use a block `STATES` which includes a number of state regions.

```
STATES = {
	s:STATE_LOWER_EGYPT = {
		create_state = {
			country = c:EGY
			owned_provinces = { x409060 x2050A0 x7ABE4B x50D0E0 x5011E0 x48E2A5 x6F13AD xD050E0 xF47AAA xA0D020 xC09060 xC37990 }
		}
		
		add_homeland = cu:misri
	}
    s:STATE_IONIAN_ISLANDS = {
		create_state = {
			country = c:ION
			owned_provinces = { x4B79CA x405060 }
		}	
		# Homelands and claims are defined on the state region, not for individual states
		add_homeland = cu:greek
		add_claim = c:GRE
	}
    s:STATE_BALUCHISTAN = {
		create_state = {
			country = c:OMA
			owned_provinces = { "xB7B2BD" }
		}
		create_state = {
			country = c:KAL
			owned_provinces = { "x0279A0" "x0BAF8C" "x1161D9" "x1D0224" "x2B7441" "x35754E" "x3C9B5F" "x43F4B8" "x4529BD" "x4B2EAD" "x4DC3FF" "x4F800F" "x556C63" "x56CF62" "x5CBA3C" "x61D696" "x626396" "x62BEAA"  "x6D6D6B" "x782112" "x7D60E7" "x8DC922" "x954C12" "x97C017" "xA3655B" "xB2AAA7" "xBAE3D2" "xBB836E" "xC6D9E8" "xCD77FD" "xD4EC50" "xD6DD8A" "xDEE571" "xDF30A0"  "xE7A309" "xE92A58" "xEC696F" "xF78D0D"  "x1EF53E" }
		}
		create_state = {
			country = c:MAK
			owned_provinces = { "x978421" "x4E09C5" "xF9577D" "x45F2DD" "x113E0B" "x7FE584" "xC070E0" "xC6E602" "xB0F79E" "x407060" "x951063" "x8ED831" "x2E7961" "xE87BBF" "x968562" "x675BCE" "x2FF46D" }
		}
		create_state = {
			country = c:KAN
			owned_provinces = { "xE712E1" "xF1414C" "x17D8AB" "x3EFD1E" "x109CC0" "x4070E0" "x9EED5C" "xA55509" "xD575B0" }
		}
		
		add_homeland = cu:baluchi
		add_homeland = cu:pashtun
	}
}
```

State regions are called with `s:<state region name>` and can be given homelands and country claims. Each state region must have at least one state created from it.

Each created state is defined from a state region with the effect `create_state`, which requires the owning country and a list of provinces. The list of provinces can be part or all of the state region. The state can also be defined with a `state_type`, states are incorporated by default, but can be defined as `unincorporated`. Note that a country's capital state is automatically and immediately incorporated, regardless of the state history.

Countries that start the game with Colonial Affairs also start with colonies in every owned state region that also contains a neighboring decentralized nation. These initial colonies ignore colonial claims.

The states defined in common/history/states are referenced in common/history/buildings and common/history/pops, so take care to update all relevant files when changing the starting setup.

## State script documentation

The following [effects](Effect.md), [event targets](Event target.md), and [triggers](Trigger.md) can be used in either state or state region scope. A few can be used in either scope.

### State scope

| Effect | Description | Example | Targets |
|---|---|---|---|
| activate_building | Activate a building in a state | activate_building = { building = building_key } |  |
| activate_production_method | Activates the named production method for buildings of a certain type in country/state | activate_production_method = { building_type = building_key production_method = production_method_key } |  |
| add_acceptance | Adds an acceptance delta for a culture in a state | add_acceptance = { culture = cu:romanian value = -10 } |  |
| add_cultural_community | Adds a cultural community for the target culture in the scoped state. | scope:some_state = { add_cultural_community = cu:zulu } | culture |
| add_culture_standard_of_living_modifier | Apply a standard of living modifier in the scoped state for the given culture. Other than the required culture argument, this effect has the same syntax as add_modifier. | add_culture_standard_of_living_modifier = { culture = culture_scope days/weeks/months/years = value (optional) #can use scripted values, negative values are permanent multiplier = value (optional) #multiplies the values of the static modifier is_decaying = yes (optional) #sets modifier to decay in strength over its duration } |  |
| add_loyalists_in_state | Adds loyalists to pops in the scoped state. All parameters except value are optional. | value is the percentage of each pop that will move towards loyalism. if interest_group is specified pops gain loyalists based on their ig membership. pop type and strata are mutually exclusive. add_radicals_in_state = { value = 0.2 interest_group = <scope/ig:key> pop_type = <scope/pop_type:key> strata = <key> culture = <scope/cu:key> religion = <scope/rel:key> } |  |
| add_modifier | Adds a timed modifier effect to object in scope | add_modifier = { name = static_modifier_name days/weeks/months/years = value (optional) #can use scripted values, negative values are permanent multiplier = value (optional) #multiplies the values of the static modifier is_decaying = yes (optional) #sets modifier to decay in strength over its duration } add_modifier = static_modifier_name #set as permanent modifier with no multiplier or decay |  |
| add_radicals_in_state | Adds radicals to pops in the scoped state. All parameters except value are optional. | value is the percentage of each pop that will move towards radicalism. if interest_group is specified pops gain radicals based on their ig membership. pop type and strata are mutually exclusive. add_radicals_in_state = { value = 0.2 interest_group = <scope/ig:key> pop_type = <scope/pop_type:key> strata = <key> culture = <scope/cu:key> religion = <scope/rel:key> } |  |
| add_religion_standard_of_living_modifier | Apply a standard of living modifier in the scoped state for the given religion. Other than the required religion argument, this effect has the same syntax as add_modifier. | add_religion_standard_of_living_modifier = { religion = religion_scope days/weeks/months/years = value (optional) #can use scripted values, negative values are permanent multiplier = value (optional) #multiplies the values of the static modifier is_decaying = yes (optional) #sets modifier to decay in strength over its duration } |  |
| cede_treaty_port | Cedes a treaty port in scope state to target country | cede_treaty_port = scope/country | country |
| convert_population | Changes X% of the different religion population to the specified religion. | convert_population = { target = rel:catholic value = 0.5 } |  |
| create_building | Creates a building in the scoped state. Supported values are: | building = <building> activate_production_methods = { <production_methods> } subsidized = yes/no reserves = [0..1] (percentage of cash reserves the building should be created with) add_ownership = { (mutually exclusive with level) country = { (give ownership levels to a specific country) country = s:GBR (country script target) levels = 5 } country = { (give ownership levels to a specific building) type = building_financial_district (building type that will get ownership levels, should be self or other ownership type) region = STATE_SINAI (region where owning building is placed) country = s:GBR (country script target for a region) levels = 3 } } level = arable_land/integer(mutually exclusive with add_ownership) If level is arable_land, the building will be of the necessary level to exhaust all available arable land in the state. If level is an integer, the building will be of that level Please note: this effect works a little differently if there already is a building of the specified type in the state. If that happens: 1. the level will be the maximum between the scripted level and the level of the existing building 2. the cash reserves will be the maximum between the scripted value and the existing cash reserves |  |
| create_mass_migration | Initiates mass migration of a specific culture from a origin country to a scoped state | create_mass_migration = { origin = c:GBR culture = cu:english } |  |
| create_pop | Creates a pop in the scoped state |  |  |
| deactivate_building | Deactivate a building in a state | deactivate_building = { building = building_key } |  |
| every_harvest_condition | Iterate through all harvest conditions affecting a state, state region, strategic region, or country | every_harvest_condition = { limit = { <triggers> } #optional <effects> } | harvest_condition |
| every_neighbouring_state | Iterate through all states neighbouring current scope Note British spelling | every_neighbouring_state = { limit = { <triggers> } #optional <effects> } | state |
| every_scope_building | Iterate through all buildings in a: state, country | every_scope_building = { limit = { <triggers> } #optional <effects> } | building |
| every_scope_culture | Iterate through all cultures in the scope | every_scope_culture = { limit = { <triggers> } #optional <effects> } | culture |
| every_scope_pop | Iterate through all pops in a: country, state, interest group, culture | every_scope_pop = { limit = { <triggers> } #optional <effects> } | pop |
| every_scope_strait | Iterate through all straits with a land endpoint in the scoped state or country | every_scope_strait = { limit = { <triggers> } #optional <effects> } | strait |
| every_sea_node_adjacent_state | Iterate through all states that share a sea node with a state | every_sea_node_adjacent_state = { limit = { <triggers> } #optional <effects> } | state |
| force_resource_depletion | Forces a resource depletion in state | force_resource_depletion = bg_gold_mining |  |
| force_resource_discovery | Forces a resource discovery in state | force_resource_discovery = bg_gold_mining |  |
| kill_population_in_state | Kills a number of individuals in the population in the scoped state. | All parameters except percent are optional. Pop type and strata cannot be used at the same time. kill_population = { value = <integer value> culture = <scope/cu:key> religion = <scope/rel:key> interest_group = <scope/ig:key> pop_type = <scope/pop_type:key> strata = <key> } |  |
| kill_population_percent_in_state | Kills a percentage of the population in the scoped state. | All parameters except percent are optional. Pop type and strata cannot be used at the same time. kill_population_percent = { percent = <decimal value> culture = <scope/cu:key> religion = <scope/rel:key> interest_group = <scope/ig:key> pop_type = <scope/pop_type:key> strata = <key> } |  |
| liberate_slaves | Frees all slaves in the country/state | liberate_slaves = yes |  |
| ordered_harvest_condition | Iterate through all harvest conditions affecting a state, state region, strategic region, or country | ordered_harvest_condition = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | harvest_condition |
| ordered_neighbouring_state | Iterate through all states neighbouring a state region | ordered_neighbouring_state = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | state |
| ordered_province | Iterate through all Provinces in the scoped State | ordered_province = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | province |
| ordered_scope_building | Iterate through all buildings in a: state, country | ordered_scope_building = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | building |
| ordered_scope_culture | Iterate through all cultures in the scope | ordered_scope_culture = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | culture |
| ordered_scope_pop | Iterate through all pops in a: country, state, interest group, culture | ordered_scope_pop = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | pop |
| ordered_scope_strait | Iterate through all straits with a land endpoint in the scoped state or country | ordered_scope_strait = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | strait |
| ordered_sea_node_adjacent_state | Iterate through all states that share a sea node with a state | ordered_sea_node_adjacent_state = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | state |
| random_harvest_condition | Iterate through all harvest conditions affecting a state, state region, strategic region, or country | random_harvest_condition = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | harvest_condition |
| random_neighbouring_state | Iterate through all states neighbouring a state region | random_neighbouring_state = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | state |
| random_province | Iterate through all Provinces in the scoped State | random_province = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | province |
| random_scope_building | Iterate through all buildings in a: state, country | random_scope_building = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | building |
| random_scope_culture | Iterate through all cultures in the scope | random_scope_culture = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | culture |
| random_scope_pop | Iterate through all pops in a: country, state, interest group, culture | random_scope_pop = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | pop |
| random_scope_strait | Iterate through all straits with a land endpoint in the scoped state or country | random_scope_strait = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | strait |
| random_sea_node_adjacent_state | Iterate through all states that share a sea node with a state | random_sea_node_adjacent_state = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | state |
| remove_building | Remove all levels of a building in the scope state | remove_building = building_key |  |
| remove_modifier | Removes a timed modifier effect to object in scope | remove_modifier = static_modifier_name |  |
| remove_resource_potential | Remove a building type from the resource potentials of a state region | remove_resource_potential = building_iron_mine |  |
| reset_hub_names | Resets the names of all hubs in a scoped state | reset_hub_names = yes |  |
| reset_state_name | Resets the name of a scoped state | reset_state_name = yes |  |
| set_available_for_autonomous_investment | Sets a building type as available for autonomous investment in the current scoped State | set_available_for_autonomous_investment = building type scope | building_type |
| set_devastation | Set devastation to a state region or state |  |  |
| set_hub_name | Sets the name of a hub in a scoped state to a localization string | set_state_name = { type = city ( can be any hub type city/port/farm/mine/wood ) name = HUB_NAME_STATE_KIEV_city_ukrainian } |  |
| set_hub_names | Sets the names of all the hubs in a scoped state to localization strings based on the name of the state region, the type of hub and a specified suffix | set_hub_names = ukrainian |  |
| set_state_name | Sets the name of a scoped state to a localization string | set_state_name = STATE_KIEV_ukrainian |  |
| set_state_owner | Set State Owner | set_state_owner = scope | country |
| set_state_type | Sets a state to a certain type (incorporated, unincorporated, treaty_port) |  |  |
| start_building_construction | Start constructing a building in a scoped state as a government construction | start_building_construction = building_barracks |  |
| start_privately_funded_building_construction | Start constructing a building in a scoped state as a private construction | start_privately_funded_building_construction = building_barracks |  |
| unset_available_for_autonomous_investment | Sets a building type as unavailable for autonomous investment in the current scoped State | unset_available_for_autonomous_investment = building type scope | building_type |

| Trigger | Description | Example | Targets |
|---|---|---|---|
| any_harvest_condition | Iterate through all harvest conditions affecting a state, state region, strategic region, or country | any_harvest_condition = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | harvest_condition |
| any_neighbouring_state | Iterate through all states neighbouring a state region | any_neighbouring_state = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | state |
| any_province | Iterate through all Provinces in the scoped State | any_province = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | province |
| any_scope_building | Iterate through all buildings in a: state, country | any_scope_building = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | building |
| any_scope_culture | Iterate through all cultures in the scope | any_scope_culture = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | culture |
| any_scope_pop | Iterate through all pops in a: country, state, interest group, culture | any_scope_pop = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | pop |
| any_scope_strait | Iterate through all straits with a land endpoint in the scoped state or country | any_scope_strait = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | strait |
| any_sea_node_adjacent_state | Iterate through all states that share a sea node with a state | any_sea_node_adjacent_state = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | state |
| arable_land | Check arable land in state | arable_land > 10 | value |
| available_jobs | Checks the state's number of available jobs in non-subsistence buildings | available_jobs > 10000 | value |
| blockade_level | Compare to state's blockade level | blockade_level > 0.1 | value |
| can_activate_production_method | Checks if the building of a particular type in scoped state is able to active the specified production method | can_activate_production_method = { building_type = <key> production_method = <key> } |  |
| can_construct_building | Checks if 1 level of <building_type> can be constructed in a scoped state | can_construct_building = <building_type> |  |
| check_area | Compares areas of object to another object |  |  |
| cultural_acceptance_delta | Compare the current local delta (modification) to a culture's acceptance in the scoped state | cultural_acceptance_delta = { target = cu:romanian value < -10 } | value |
| culture_percent_state | Checks that a state's population has a certain percentage of a specific culture | scope:example_state = { culture_percent_state = { target = cu:dixie value >= 0.2 } } | value |
| devastation | Compares the devastation of a given state | devastation > 5 | value |
| free_arable_land | Check free arable land in state | free_arable_land > 0 | value |
| has_active_building | True if a state has an active building type | has_active_building = building |  |
| has_assimilating_pops | Check if a state has any pops currently in the process of assimilating. |  | boolean |
| has_building | True if a state/market/state region/country has a building type | has_building = building |  |
| has_claim_by | Checks if a state is claimed by a country | any_state = { owner = root has_claim_by = c:MEX } | country |
| has_converting_pops | Check if a state has any pops currently in the process of converting. |  | boolean |
| has_cultural_community | Checks if a culture has a cultural community in the scoped state. | has_cultural_community = <culture> |  |
| has_decree | Checks if scope state has a particular type of decree | has_decree = <key> |  |
| has_famine | Check if state or country has famine | has_famine = yes/no | boolean |
| has_mobilizing_unit | Checks if any Building in a scoped State maintains any Combat Units that are currently mobilizing | has_mobilizing_unit = bool | boolean |
| has_modifier | Check if a supported scope has a certain timed modifier | has_modifier = <key> |  |
| has_port_state | Check if scoped state has at least one port | has_port = yes/no | boolean |
| has_potential_resource | Checks if the specificed building group is allowed in the scoped state. Used to check if a state can potentially produce a resource | has_potential_resource = bg_rubber_plantations | building_group |
| has_state_trait | Checks if scoped state has a certain trait | has_state_trait = key |  |
| ig_state_pol_strength_share | True if IG in scope has scripted political strength in state | ig_state_pol_strength_share = { target = scope:target_ig value = 0.3 } | value |
| incorporation_progress | Check incorporation progress in state | incorporation_progress > 0.25 | value |
| infrastructure | Compares the infrastructure value of a given state | infrastructure > 10 | value |
| infrastructure_delta | Compares the infrastructure balance of a given state | infrastructure_delta > 0 | value |
| infrastructure_usage | Compares the infrastructure usage value of a given state | infrastructure_usage > 10 | value |
| is_being_bombarded | Checks if a state is currently being port bombarded by a hostile fleet |  | boolean |
| is_blockaded_by | Checks if a state is blockaded by a country |  | country |
| is_capital | Check if state is the capital of the owner = bool |  | boolean |
| is_coastal | Check if state borders a (non-impassable) sea region | is_coastal = yes/no | boolean |
| is_homeland_of_country_cultures | Checks if state is homeland of any of the target country's primary cultures | is_homeland_of_country_cultures = <country> | country |
| is_in_revolt | Check if a state has any chance to split off into a revolutionary or seceding country | is_in_revolt = yes/no. | boolean |
| is_incorporated | Check if state is incorporated = bool |  | boolean |
| is_isolated_from_market | Check if a state is isolated from its market |  | boolean |
| is_largest_state_in_region | Check if state is the largest in the state region = bool |  | boolean |
| is_mass_migration_target | Mass migration target is state. | is_mass_migration_target = yes | boolean |
| is_mass_migration_target_for_culture | Scoped state is a mass migration target for the specified culture. | is_mass_migration_target_for_culture = scope:my_culture | culture |
| is_potential_treaty_port | Checks if the scoped state has the potential to become a treaty port for target country | is_potential_treaty_port = c:FRA | country |
| is_production_method_active | Checks if the building of a particular type in scoped state has the specified production method active | is_production_method_active = { building_type = <key> production_method = <key> } |  |
| is_sea_adjacent | Check if state borders a sea region (regular or impassable) | is_sea_adjacent = yes/no | boolean |
| is_slave_state | Check if a state employs or has the potential to employ slaves. |  | boolean |
| is_split_state | Checks if the scoped state is a split state. | scope:example_state = { is_split_state = yes } | boolean |
| is_strategic_objective | Checks if the scoped State is a Strategic Objective of a Country | is_strategic_objective = <country> | country |
| is_target_of_wargoal | Checks if state is target of any wargoal in wars involving a specific country | has_war_goal = <country> | country |
| is_treaty_port | Checks if the scoped state is a treaty port | is_treaty_port = yes/no | boolean |
| is_under_colonization | Check if state is under colonization | is_under_colonization = yes/no | boolean |
| is_world_market_hub | Check if state is a world market hub | is_world_market_hub = yes | boolean |
| literacy_rate | Checks if a pop, state or country has a certain amount of literacy | literacy = value | value |
| loyalist_fraction | Compares loyalist fraction in pops in state or country, all parameters except value are optional | loyalist_fraction = { value = <script_value> pop_type = <key> strata = <key> culture = <key/scope> religion = <key/scope> } | value |
| loyalists | Compares the loyalty in a given state, i.e. the fraction of Loyalists | loyalists > 0.2 | value |
| market_access | Checks the market access of the scoped state | market_access > 0.8 | value |
| most_prominent_revolting_interest_group | Checks if the most prominent revolting interest group in the scoped state has the given interest group type. Evaluates false if the scoped state is not in revolt. | most_prominent_revolting_interest_group = ig_landowners |  |
| num_cultural_communities | Check cultural communities in state | num_cultural_communities > 5 | value |
| obstinance | Compares state obstinance | obstinance > 0.5 | value |
| political_strength_share | Checks the political strength share of a pop type, religion or culture in a country or state. Exactly one of pop_type, religion or culture must be specified. | political_strength_share = { pop_type/religion/culture = <key/scope> value <compare operator> <value> } | value |
| pollution_generation | Compare total pollution generation across all buildings in the state |  | value |
| pop_type_percent_state | Checks that a state's population has a certain percentage of a specific pop type | scope:example_state = { pop_type_percent_state = { target = pop_type:laborer value <= 0.8 } } | value |
| population_by_culture | Compare the current population of a target culture in the scoped state | population_by_culture = { target = cu:romanian value > 2500 } | value |
| primary_cultures_percent_state | Checks that a state's population has a certain percentage of the country's primary cultures | scope:example_state = { primary_cultures_percent_state >= 0.2 } | value |
| radical_fraction | Compares radical fraction in pops in state or country, all parameters except value are optional | radical_fraction = { value = <script_value> pop_type = <key> strata = <key> culture = <key/scope> religion = <key/scope> } | value |
| relative_infrastructure | Compares the infrastructure to infrastructure usage of a state | relative_infrastructure > 1.1 | value |
| religion_percent_state | Checks that a state's population has a certain percentage of a specific religion | scope:example_state = { religion_percent_state = { target = rel:catholic value <= 0.8 } } | value |
| state_cultural_acceptance | Checks how accepted a pop of the target culture is in the scoped state | state_cultural_acceptance = { target = cu:french value >= 50 | value |
| state_exports | Compare total units of exports from scope to target state (if set) or world state in general (if no state specified) | state_exports = { target = state scope (optional) goods = key (optional) value >= 100 } | value |
| state_has_building_group_levels | Checks the sum of building levels for a building group in a state | state_has_building_group_levels = { type = bg_heavy_industry value >= 100 } | value |
| state_has_building_levels | Checks the sum of building levels for a state | state_has_building_levels >= 10 | value |
| state_has_building_type_levels | Checks the sum of building levels for a building type in a state | state_has_building_type_levels = { target = bt:building_barracks value >= 100 } | value |
| state_has_goods_shortage | Check if state has a shortage on any of its building inputs | state_has_goods_shortage = yes/no | boolean |
| state_has_national_awakening | Checks if the scoped state is in a state region with an active national awakening map marker | state_has_national_awakening = yes/no | boolean |
| state_imports | Compare total units of imports from target to scope state | state_imports = { target = state scope (optional) goods = key (optional) value >= 100 } | value |
| state_is_eligible_as_mass_migration_target | Check if state can receive a mass migration at all. | any_state = { state_is_eligible_as_mass_migration_target = yes } | boolean |
| state_population | Checks the total population of the scoped state | state_population <= 250000 | value |
| state_religious_acceptance | Checks how accepted a pop of the given religion is in the the scoped state | state_religious_acceptance = { target = rel:catholic value >= 50 | value |
| state_trade | Compare total units of goods traded between scope state and target state (if set) or world state in general (if no state specified) | state_trade = { target = state scope (optional) goods = key (optional) value >= 100 } | value |
| state_unemployment_rate | Checks the unemployment rate (percentage) in the scoped state | state_unemployment_rate > 0.1 | value |
| tax_capacity | Checks the taxation capacity of the scoped state | tax_capacity > 50 | value |
| tax_capacity_usage | Checks the taxation capacity usage of the scoped state | tax_capacity_usage > 50 | value |
| total_urbanization | Compares the total urbanization of a given state | total_urbanization > 5 | value |
| turmoil | Compares the turmoil in a given state, i.e. the fraction of Radicals | turmoil > 0.2 | value |
| wealth_share | Checks the wealth political strength share of a pop type, religion or culture in a country or state. Exactly one of pop_type, religion or culture must be specified. | wealth_share = { pop_type/religion/culture = <key/scope> value <compare operator> <value> } | value |
| world_market_access | Checks the world market access of the scoped state | world_market_access > 0.8 | value |

| Event target | Description | To scope |
|---|---|---|
| ai_state_value | Scope to target country AI desire to own scope state (example: value = ai_state_value:root) | value |
| ai_treaty_port_value | Scope to target country AI desire to have a treaty port in scope state (example: value = ai_treaty_port_value:root) | value |
| average_expected_sol | Get the average expected Standard of Living of the scope | value |
| average_sol | Get the average Standard of Living of the scope | value |
| b | Scope to the building of specified key in the state, example: b:building_port | building |
| controller | Scope to the controller of the object | country |
| decree_cost | Scope to a state's cost for a certain decree authority > decree_cost:decree_road_maintaintenance | value |
| gdp | Get the scoped country's yearly predicted GDP | value |
| land_controller_hq | Returns the province or state controller land HQ | hq |
| land_hq | Returns the province or state owner local land HQ | hq |
| market | Scope to the market of the object | market |
| mass_migration_culture | Scope to the mass migration target culture of a state | culture |
| migration_pull | Get the migration pull for a state or the mass migration pull for a country. | value |
| modifier | Scope to the value of the modifier type of specified key belonging to the current object, example: modifier:country_influence_add | boolean, value |
| nf | Scope to a Decree of specified key applied to the state, example: nf:decree_road_maintaintenance | decree |
| num_provinces | Get the scoped entity's current number of provinces | value |
| num_world_market_hub_trade_center_levels | Get the total number of trade center levels associated with scope world market hub state | value |
| owner | Scope to the owner country of object | country |
| population_below_expected_sol | Scope to the current percentage of the state's population that are below their expected standard of living (0-1) | value |
| region | Scope to the strategic region of the object! | strategic_region |
| sg | Scope from a state to the StateGoods with the specified key, example: sg:wood | state_goods |
| state_region | Scope to the state region of a state | state_region |
| theater | Scope from a BattleSide or State to its theater | theater |
| world_market_hub | Scope to the world market hub state associated with the scoped state | state |

### State region scope

| Effect | Description | Example | Targets |
|---|---|---|---|
| add_arable_land | Add/remove arable land from a state region |  |  |
| add_claim | Adds scoped state region as a claim for target country | add_claim = scope/country | country |
| add_devastation | Add/remove devastation from a state region |  |  |
| add_homeland | Adds scoped state region as Homeland for target culture | add_homeland = cu:culture | culture |
| add_pollution | Increase/decrease pollution level in a scoped state region | add_pollution = 10 |  |
| add_state_trait | add state trait in a scoped state region | add_state_trait = <state_trait_name> |  |
| create_state | creates a state in a state region |  |  |
| every_harvest_condition | Iterate through all harvest conditions affecting a state, state region, strategic region, or country | every_harvest_condition = { limit = { <triggers> } #optional <effects> } | harvest_condition |
| every_neighbouring_state | Iterate through all states neighbouring current scope Note British spelling | every_neighbouring_state = { limit = { <triggers> } #optional <effects> } | state |
| every_scope_country | Iterate through all countries with a presence in the supported scope (currently: market, state_region, strategic region) | every_scope_country = { limit = { <triggers> } #optional <effects> } | country |
| every_scope_interest_marker | Iterate through all interest markers in a: country, state_region, strategic region | every_scope_interest_marker = { limit = { <triggers> } #optional <effects> } | interest_marker |
| every_scope_state | Iterate through all states including provinces from a: country, state_region, theater, front, or strait | every_scope_state = { limit = { <triggers> } #optional <effects> } | state |
| finish_harvest_condition | Finish a harvest condition of type in the scoped state region | finish_harvest_condition = <key> |  |
| ordered_harvest_condition | Iterate through all harvest conditions affecting a state, state region, strategic region, or country | ordered_harvest_condition = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | harvest_condition |
| ordered_neighbouring_state | Iterate through all states neighbouring a state region | ordered_neighbouring_state = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | state |
| ordered_scope_country | Iterate through all countries with a presence in the supported scope (currently: market, state_region, strategic region) | ordered_scope_country = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country |
| ordered_scope_interest_marker | Iterate through all interest markers in a: country, state_region, strategic region | ordered_scope_interest_marker = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | interest_marker |
| ordered_scope_state | Iterate through all states including provinces from a: country, state_region, theater, front, or strait | ordered_scope_state = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | state |
| random_harvest_condition | Iterate through all harvest conditions affecting a state, state region, strategic region, or country | random_harvest_condition = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | harvest_condition |
| random_neighbouring_state | Iterate through all states neighbouring a state region | random_neighbouring_state = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | state |
| random_scope_country | Iterate through all countries with a presence in the supported scope (currently: market, state_region, strategic region) | random_scope_country = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country |
| random_scope_interest_marker | Iterate through all interest markers in a: country, state_region, strategic region | random_scope_interest_marker = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | interest_marker |
| random_scope_state | Iterate through all states including provinces from a: country, state_region, theater, front, or strait | random_scope_state = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | state |
| remove_claim | Removes scoped state region as a claim for target country | add_claim = scope/country | country |
| remove_homeland | Removes scoped state region as Homeland for target culture | remove_homeland = cu:culture | culture |
| remove_resource_potential | Remove a building type from the resource potentials of a state region | remove_resource_potential = building_iron_mine |  |
| remove_state_trait | remove state trait in a scoped state region | remove_state_trait = <state_trait_name> |  |
| set_devastation | Set devastation to a state region or state |  |  |
| set_owner_of_provinces | Gives a set of provinces in a state region to a specific country | set_owner_of_provinces = { country = <scope> provinces = { <province list> } } |  |
| start_harvest_condition | Start a harvest condition of type (or refresh it if already exists) in the scoped state region | start_harvest_condition = <key> |  |
| start_harvest_condition_with_params | Start a harvest condition of type in scoped state region where intensity and duration(in days) are optionally provided | start_harvest_condition_with_params = { type = flood intensity = 5 (optional) duration = 5 (optional) } |  |

| Trigger | Description | Example | Targets |
|---|---|---|---|
| any_harvest_condition | Iterate through all harvest conditions affecting a state, state region, strategic region, or country | any_harvest_condition = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | harvest_condition |
| any_neighbouring_state | Iterate through all states neighbouring a state region | any_neighbouring_state = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | state |
| any_scope_country | Iterate through all countries with a presence in the supported scope (currently: market, strategic region) | any_scope_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country |
| any_scope_interest_marker | Iterate through all interest markers in a: country, strategic region | any_scope_interest_marker = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | interest_marker |
| any_scope_state | Iterate through all states including provinces from a: country, state_region, theater, front, or strait | any_scope_state = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | state |
| check_area | Compares areas of object to another object |  |  |
| contains_capital_of | Checks if scoped state region contains the capital of target tag | contains_capital_of = country scope/tag |  |
| has_building | True if a state/market/state region/country has a building type | has_building = building |  |
| has_harvest_condition | Check if the scoped state region has a harvest condition of type | has_harvest_condition = drought |  |
| infrastructure | Compares the infrastructure value of a given state | infrastructure > 10 | value |
| infrastructure_delta | Compares the infrastructure balance of a given state | infrastructure_delta > 0 | value |
| infrastructure_usage | Compares the infrastructure usage value of a given state | infrastructure_usage > 10 | value |
| is_homeland | Checks if scoped state region is a homeland of target culture | is_homeland = culture scope/name |  |
| is_state_region_land | Check if the state region is on land |  | boolean |
| pollution_amount | Compare state region pollution |  | value |
| remaining_undepleted | Check remaining amount of resource, like gold mines in a state | remaining_undepleted = { type = bg_gold_mining amount > 1 } | value |

| Event target | Description | To scope |
|---|---|---|
| market | Scope to the market of the object | market |
| num_provinces | Get the scoped entity's current number of provinces | value |
| region | Scope to the strategic region of the object! | strategic_region |
| region_state | Scope to the state owned by the target country, (example: region_state:BIC) | state |

### State modifier types

`state_` modifier types apply their effects to states. When applied to a country, they affect all states owned by that country; likewise when applied to a state region, they apply to all states in the region.

For reasons of length, this table does not include the set of modifier types for culture or religion based standard of living, `state_[type]_standard_of_living_add`.

| Modifier type | Localization | Type | Format | Notes |
|---|---|---|---|---|
| state_academics_investment_pool_contribution_add | Academics Investment Pool contribution | additive | percent, good |  |
| state_academics_investment_pool_efficiency_mult | Academics Investment Pool contribution efficiency | multiplicative | percent, good |  |
| state_academics_mortality_mult | Mortality of Academics | multiplicative | percent, bad |  |
| state_allow_assimilation_in_homeland_bool | Assimilation in Homeland States Allowed | boolean | good |  |
| state_allow_assimilation_without_presence_bool | Assimilation to Primary Culture Always Allowed | boolean | good |  |
| state_allow_conversion_without_presence_bool | Conversion to State Religion Always Allowed | boolean | good |  |
| state_aristocrats_investment_pool_contribution_add | Aristocrats Investment Pool contribution | additive | percent, good |  |
| state_aristocrats_investment_pool_efficiency_mult | Aristocrats Investment Pool contribution efficiency | multiplicative | percent, good |  |
| state_aristocrats_mortality_mult | Mortality of Aristocrats | multiplicative | percent, bad |  |
| state_assimilation_mult | Assimilation | multiplicative | percent, good |  |
| state_birth_rate_mult | Birth Rate | multiplicative | percent, good |  |
| state_blockade_resistance_add | Blockade Resistance | additive | good |  |
| state_building_barrack_max_level_add | Barracks Max Level | additive | good |  |
| state_building_conscription_center_max_level_add | Maximum Conscription Limit | additive | good |  |
| state_building_construction_sector_max_level_add | Construction Sector Max Level | additive | good |  |
| state_building_naval_fortification_max_level_add | Naval Fortification Max Level | additive | good |  |
| state_bureaucracy_population_base_cost_factor_mult | Bureaucracy Population Cost Multiplier | multiplicative | percent, bad |  |
| state_bureaucrats_investment_pool_contribution_add | Bureaucrats Investment Pool contribution | additive | percent, good |  |
| state_bureaucrats_investment_pool_efficiency_mult | Bureaucrats Investment Pool contribution efficiency | multiplicative | percent, good |  |
| state_buy_orders_ammunition_add | Ammunition Buy Orders | additive | neutral |  |
| state_buy_orders_artillery_add | Artillery Buy Orders | additive | neutral |  |
| state_buy_orders_small_arms_add | Small Arms Buy Orders | additive | neutral |  |
| state_capitalists_investment_pool_contribution_add | Capitalists Investment Pool contribution | additive | percent, good |  |
| state_capitalists_investment_pool_efficiency_mult | Capitalists Investment Pool contribution efficiency | multiplicative | percent, good |  |
| state_clergymen_investment_pool_contribution_add | Clergymen Investment Pool contribution | additive | percent, good |  |
| state_clergymen_investment_pool_efficiency_mult | Clergymen Investment Pool contribution efficiency | multiplicative | percent, good |  |
| state_clerks_investment_pool_contribution_add | Clerks Investment Pool contribution | additive | percent, good |  |
| state_clerks_investment_pool_efficiency_mult | Clerks Investment Pool contribution efficiency | multiplicative | percent, good |  |
| state_colony_growth_creation_factor | Colonial Growth Generation | multiplicative | good |  |
| state_colony_growth_speed_mult | Colony Growth Speed | multiplicative | percent, good |  |
| state_conscription_rate_add | Conscription Rate | additive | percent, good |  |
| state_conscription_rate_mult | Conscriptable Battalions | multiplicative | percent, good |  |
| state_construction_mult | State Construction Efficiency | multiplicative | percent, good |  |
| state_contiguous_incorporation_speed_mult | Contiguous Incorporation Speed | multiplicative | percent, good |  |
| state_control_strait_bool | Control Strait | boolean | good |  |
| state_conversion_mult | Conversion | multiplicative | percent, good |  |
| state_decree_cost_mult | Decree Cost | multiplicative | percent, bad |  |
| state_dependent_political_participation_add | Dependent Enfranchisement | additive | percent, good |  |
| state_dependent_wage_add | Yearly Dependents Income | additive | good |  |
| state_dependent_wage_mult | Dependents Income | multiplicative | percent, good |  |
| state_devastation_decay_mult | Devastation Recovery | multiplicative | percent, good |  |
| state_disallow_incorporation_bool | State Incorporation Disallowed | boolean | bad |  |
| state_education_access_add | Education Access | additive | percent, good |  |
| state_education_access_wealth_add | Education Access (Wealth-based) | additive | percent, good |  |
| state_engineers_investment_pool_contribution_add | Engineers Investment Pool contribution | additive | percent, good |  |
| state_engineers_investment_pool_efficiency_mult | Engineers Investment Pool contribution efficiency | multiplicative | percent, good |  |
| state_expected_sol_from_literacy | Minimum Expected Standard of Living from Literacy |  | bad |  |
| state_expected_sol_mult | Minimum Expected Standard of Living | multiplicative | percent, bad |  |
| state_export_advantage_mult | Trade Advantage for Exports | multiplicative | percent, good |  |
| state_farmers_investment_pool_contribution_add | Farmers Investment Pool contribution | additive | percent, good |  |
| state_farmers_investment_pool_efficiency_mult | Farmers Investment Pool contribution efficiency | multiplicative | percent, good |  |
| state_farmers_mortality_mult | Mortality of Farmers | multiplicative | percent, bad |  |
| state_food_security_add | Food Security | additive | percent, good |  |
| state_fortification_bombardment_resistance_add | Naval Fortification Bombardment Resistance | additive | good |  |
| state_fortification_naval_battle_mult | Naval Fortification Battle Defense | multiplicative | percent, good |  |
| state_fortification_naval_invasion_add | Naval Fortification Invasion Defense | additive | good |  |
| state_free_state_pop_support_movement_anti_slavery_mult | Abolitionist Movement Pop Attraction in non-Slave States | multiplicative | percent, neutral |  |
| state_harvest_condition_disease_outbreak_duration_mult | Disease Outbreak Harvest Condition Duration | multiplicative | percent, bad |  |
| state_harvest_condition_disease_outbreak_impact_mult | Disease Outbreak Harvest Condition Impact | multiplicative | percent, bad |  |
| state_harvest_condition_drought_duration_mult | Drought Harvest Condition Duration | multiplicative | percent, bad |  |
| state_harvest_condition_drought_impact_mult | Drought Harvest Condition Impact | multiplicative | percent, bad |  |
| state_harvest_condition_earthquake_duration_mult | Earthquake Harvest Condition Duration | multiplicative | percent, bad |  |
| state_harvest_condition_earthquake_impact_mult | Earthquake Harvest Condition Impact | multiplicative | percent, bad |  |
| state_harvest_condition_extreme_winds_duration_mult | Extreme Winds Harvest Condition Duration | multiplicative | percent, bad |  |
| state_harvest_condition_extreme_winds_impact_mult | Extreme Winds Harvest Condition Impact | multiplicative | percent, bad |  |
| state_harvest_condition_flood_duration_mult | Flood Harvest Condition Duration | multiplicative | percent, bad |  |
| state_harvest_condition_flood_impact_mult | Flood Harvest Condition Impact | multiplicative | percent, bad |  |
| state_harvest_condition_heatwave_duration_mult | Heatwave Harvest Condition Duration | multiplicative | percent, bad |  |
| state_harvest_condition_heatwave_impact_mult | Heatwave Harvest Condition Impact | multiplicative | percent, bad |  |
| state_harvest_condition_tsunami_duration_mult | Tsunami Harvest Condition Duration | multiplicative | percent, bad |  |
| state_harvest_condition_tsunami_impact_mult | Tsunami Harvest Condition Impact | multiplicative | percent, bad |  |
| state_harvest_condition_wildfire_duration_mult | Wildfire Harvest Condition Duration | multiplicative | percent, bad |  |
| state_harvest_condition_wildfire_impact_mult | Wildfire Harvest Condition Impact | multiplicative | percent, bad |  |
| state_import_advantage_mult | Trade Advantage for Imports | multiplicative | percent, good |  |
| state_incorporation_speed_mult | Incorporation Speed | multiplicative | percent, good |  |
| state_infrastructure_add | Infrastructure | additive | good |  |
| state_infrastructure_from_automobiles_consumption_add | Infrastructure from Pop Automobiles Consumption | additive | good |  |
| state_infrastructure_from_population_add | Infrastructure per 100.0K Population | additive | good |  |
| state_infrastructure_from_population_max_add | Maximum Infrastructure from Population | additive | good |  |
| state_infrastructure_from_population_max_mult | Maximum Infrastructure from Population | multiplicative | percent, good |  |
| state_infrastructure_from_population_mult | Infrastructure per 100.0K Population | multiplicative | percent, good |  |
| state_infrastructure_mult | Infrastructure | multiplicative | percent, good |  |
| state_institution_impact_add | Impact of Institutions | additive | percent, good |  |
| state_laborers_investment_pool_contribution_add | Laborers Investment Pool contribution | additive | percent, good |  |
| state_laborers_investment_pool_efficiency_mult | Laborers Investment Pool contribution efficiency | multiplicative | percent, good |  |
| state_laborers_mortality_mult | Mortality of Laborers | multiplicative | percent, bad |  |
| state_literacy_growth_add | Literacy Growth | additive | percent, good |  |
| state_lower_strata_expected_sol_add | Minimum Expected Standard of Living for the Lower Strata | additive | neutral |  |
| state_loyalism_increases_cultural_erasure_mult | Loyalism increases for the Cultural Erasure Status | multiplicative | percent, good |  |
| state_loyalism_increases_full_acceptance_mult | Loyalism increases for the Full Acceptance Status | multiplicative | percent, good |  |
| state_loyalism_increases_open_prejudice_mult | Loyalism increases for the Open Prejudice Status | multiplicative | percent, good |  |
| state_loyalism_increases_second_rate_citizen_mult | Loyalism increases for the Second-class Citizen Status | multiplicative | percent, good |  |
| state_loyalism_increases_violent_hostility_mult | Loyalism increases for the Violent Hostility Status | multiplicative | percent, good |  |
| state_loyalists_from_political_movements_mult | Loyalists from Political Movements | multiplicative | percent, good |  |
| state_machinists_investment_pool_contribution_add | Machinists Investment Pool contribution | additive | percent, good |  |
| state_machinists_investment_pool_efficiency_mult | Machinists Investment Pool contribution efficiency | multiplicative | percent, good |  |
| state_machinists_mortality_mult | Mortality of Machinists | multiplicative | percent, bad |  |
| state_market_access_price_impact | Market Access Price Impact |  | percent, neutral |  |
| state_max_trade_advantage_from_capacity_add | Maximum Trade Advantage from Capacity | additive | percent, good |  |
| state_middle_strata_expected_sol_add | Minimum Expected Standard of Living for the Middle Strata | additive | neutral |  |
| state_migration_pull_add | Migration Attraction | additive | good |  |
| state_migration_pull_mult | Migration Attraction | multiplicative | percent, good |  |
| state_migration_pull_unincorporated_mult | Migration Attraction in Unincorporated States | multiplicative | percent, good |  |
| state_migration_quota_mult | Migration Quota | multiplicative | percent, neutral |  |
| state_minimum_incorporated_subsistence_arable_land_add | Minimum Subsistence Land Share in Incorporated States | additive | percent, neutral |  |
| state_mortality_mult | Mortality | multiplicative | percent, bad |  |
| state_mortality_turmoil_mult | Mortality per Turmoil | multiplicative | percent, bad |  |
| state_mortality_wealth_mult | Mortality per Wealth | multiplicative | percent, bad |  |
| state_non_contiguous_incorporation_speed_mult | Non-Contiguous Incorporation Speed | multiplicative | percent, good |  |
| state_non_homeland_colony_growth_speed_mult | Colony Growth Speed in non-Homeland States | multiplicative | percent, good |  |
| state_non_homeland_mortality_mult | Mortality in non-Homeland States | multiplicative | percent, bad |  |
| state_officers_investment_pool_contribution_add | Officers Investment Pool contribution | additive | percent, good |  |
| state_officers_investment_pool_efficiency_mult | Officers Investment Pool contribution efficiency | multiplicative | percent, good |  |
| state_peasants_consumption_multiplier_add | Goods consumption for Peasants | additive | percent, bad |  |
| state_peasants_education_access_add | Education Access for Peasants | additive | percent, good |  |
| state_peasants_internal_migration_disallowed_bool | Disallowed Internal Migration for Peasants | boolean | bad |  |
| state_peasants_mass_migration_disallowed_bool | Disallowed Mass Migration for Peasants | boolean | bad |  |
| state_peasants_mortality_mult | Mortality of Peasants | multiplicative | percent, bad |  |
| state_political_strength_from_wealth_mult | Political Strength from Wealth | multiplicative | percent, neutral |  |
| state_political_strength_from_welfare_mult | Political Strength when receiving Welfare | multiplicative | percent, neutral |  |
| state_pollution_generation_add | Generated Pollution | additive | bad |  |
| state_pollution_reduction_health_mult | Pollution Health Effects Reduction | multiplicative | percent, bad |  |
| state_pop_pol_str_add | Universal Pop Political Strength | additive | neutral |  |
| state_pop_pol_str_mult | Universal Pop Political Strength | multiplicative | percent, neutral |  |
| state_pop_qualifications_mult | Qualifications | multiplicative | percent, good |  |
| state_pop_support_movement_anarchist_add | Anarchist Movement Pop Attraction | additive | neutral |  |
| state_pop_support_movement_anarchist_mult | Anarchist Movement Pop Attraction | multiplicative | percent, neutral |  |
| state_pop_support_movement_anti_slavery_add | Abolitionist Movement Pop Attraction | additive | neutral |  |
| state_pop_support_movement_anti_slavery_mult | Abolitionist Movement Pop Attraction | multiplicative | percent, neutral |  |
| state_pop_support_movement_bonapartist_add | Bonapartist Movement Pop Attraction | additive | neutral |  |
| state_pop_support_movement_bonapartist_mult | Bonapartist Movement Pop Attraction | multiplicative | percent, neutral |  |
| state_pop_support_movement_carlist_add | Carlist Movement Pop Attraction | additive | neutral |  |
| state_pop_support_movement_carlist_mult | Carlist Movement Pop Attraction | multiplicative | percent, neutral |  |
| state_pop_support_movement_communist_add | Communist Movement Pop Attraction | additive | neutral |  |
| state_pop_support_movement_communist_mult | Communist Movement Pop Attraction | multiplicative | percent, neutral |  |
| state_pop_support_movement_corporatist_add | Corporatist Movement Pop Attraction | additive | neutral |  |
| state_pop_support_movement_corporatist_mult | Corporatist Movement Pop Attraction | multiplicative | percent, neutral |  |
| state_pop_support_movement_cultural_majority_add | Cultural Majority Movement Pop Attraction | additive | neutral |  |
| state_pop_support_movement_cultural_majority_mult | Cultural Majority Movement Pop Attraction | multiplicative | percent, neutral |  |
| state_pop_support_movement_cultural_minority_add | Cultural Minority Movement Pop Attraction | additive | neutral |  |
| state_pop_support_movement_cultural_minority_mult | Cultural Minority Movement Pop Attraction | multiplicative | percent, neutral |  |
| state_pop_support_movement_fascist_add | Fascist Movement Pop Attraction | additive | neutral |  |
| state_pop_support_movement_fascist_mult | Fascist Movement Pop Attraction | multiplicative | percent, neutral |  |
| state_pop_support_movement_feminist_add | Feminist Movement Pop Attraction | additive | neutral |  |
| state_pop_support_movement_feminist_mult | Feminist Movement Pop Attraction | multiplicative | percent, neutral |  |
| state_pop_support_movement_german_national_add | German National Movement Pop Attraction | additive | neutral |  |
| state_pop_support_movement_german_national_mult | German National Movement Pop Attraction | multiplicative | percent, neutral |  |
| state_pop_support_movement_india_pan_national_add | Indian National Movement Pop Attraction | additive | neutral |  |
| state_pop_support_movement_india_pan_national_mult | Indian National Movement Pop Attraction | multiplicative | percent, neutral |  |
| state_pop_support_movement_italian_national_add | Italian National Movement Pop Attraction | additive | neutral |  |
| state_pop_support_movement_italian_national_mult | Italian National Movement Pop Attraction | multiplicative | percent, neutral |  |
| state_pop_support_movement_labor_add | Labor Movement Pop Attraction | additive | neutral |  |
| state_pop_support_movement_labor_mult | Labor Movement Pop Attraction | multiplicative | percent, neutral |  |
| state_pop_support_movement_land_reform_add | Peasant Movement Pop Attraction | additive | neutral |  |
| state_pop_support_movement_land_reform_mult | Peasant Movement Pop Attraction | multiplicative | percent, neutral |  |
| state_pop_support_movement_legitimist_add | Legitimist Movement Pop Attraction | additive | neutral |  |
| state_pop_support_movement_legitimist_mult | Legitimist Movement Pop Attraction | multiplicative | percent, neutral |  |
| state_pop_support_movement_liberal_add | Liberal Movement Pop Attraction | additive | neutral |  |
| state_pop_support_movement_liberal_mult | Liberal Movement Pop Attraction | multiplicative | percent, neutral |  |
| state_pop_support_movement_miguelist_add | Miguelist Movement Pop Attraction | additive | neutral |  |
| state_pop_support_movement_miguelist_mult | Miguelist Movement Pop Attraction | multiplicative | percent, neutral |  |
| state_pop_support_movement_modernizer_add | Modernization Movement Pop Attraction | additive | neutral |  |
| state_pop_support_movement_modernizer_mult | Modernization Movement Pop Attraction | multiplicative | percent, neutral |  |
| state_pop_support_movement_nihilist_add | Nihilist Movement Pop Attraction | additive | neutral |  |
| state_pop_support_movement_nihilist_mult | Nihilist Movement Pop Attraction | multiplicative | percent, neutral |  |
| state_pop_support_movement_orleanist_add | Orleanist Movement Pop Attraction | additive | neutral |  |
| state_pop_support_movement_orleanist_mult | Orleanist Movement Pop Attraction | multiplicative | percent, neutral |  |
| state_pop_support_movement_positivist_add | Positivist Movement Pop Attraction | additive | neutral |  |
| state_pop_support_movement_positivist_mult | Positivist Movement Pop Attraction | multiplicative | percent, neutral |  |
| state_pop_support_movement_pro_slavery_add | Pro-Slavery Movement Pop Attraction | additive | neutral |  |
| state_pop_support_movement_pro_slavery_mult | Pro-Slavery Movement Pop Attraction | multiplicative | percent, neutral |  |
| state_pop_support_movement_radical_add | Radical Movement Pop Attraction | additive | neutral |  |
| state_pop_support_movement_radical_mult | Radical Movement Pop Attraction | multiplicative | percent, neutral |  |
| state_pop_support_movement_reactionary_add | Reactionary Movement Pop Attraction | additive | neutral |  |
| state_pop_support_movement_reactionary_mult | Reactionary Movement Pop Attraction | multiplicative | percent, neutral |  |
| state_pop_support_movement_religious_majority_add | Religious Majority Movement Pop Attraction | additive | neutral |  |
| state_pop_support_movement_religious_majority_mult | Religious Majority Movement Pop Attraction | multiplicative | percent, neutral |  |
| state_pop_support_movement_religious_minority_add | Religious Minority Movement Pop Attraction | additive | neutral |  |
| state_pop_support_movement_religious_minority_mult | Religious Minority Movement Pop Attraction | multiplicative | percent, neutral |  |
| state_pop_support_movement_royalist_absolutist_add | Absolutist Movement Pop Attraction | additive | neutral |  |
| state_pop_support_movement_royalist_absolutist_mult | Absolutist Movement Pop Attraction | multiplicative | percent, neutral |  |
| state_pop_support_movement_royalist_constitutional_add | Royalist Movement Pop Attraction | additive | neutral |  |
| state_pop_support_movement_royalist_constitutional_mult | Royalist Movement Pop Attraction | multiplicative | percent, neutral |  |
| state_pop_support_movement_slave_revolt_add | Slave Revolt Movement Pop Attraction | additive | neutral |  |
| state_pop_support_movement_slave_revolt_mult | Slave Revolt Movement Pop Attraction | multiplicative | percent, neutral |  |
| state_pop_support_movement_socialist_add | Socialist Movement Pop Attraction | additive | neutral |  |
| state_pop_support_movement_socialist_mult | Socialist Movement Pop Attraction | multiplicative | percent, neutral |  |
| state_pop_support_movement_utilitarian_add | Utilitarian Movement Pop Attraction | additive | neutral |  |
| state_pop_support_movement_utilitarian_mult | Utilitarian Movement Pop Attraction | multiplicative | percent, neutral |  |
| state_pop_support_movement_yugoslav_national_add | state_pop_support_movement_yugoslav_national_add | additive | neutral |  |
| state_pop_support_movement_yugoslav_national_mult | German National Movement Pop Attraction | multiplicative | percent, neutral |  |
| state_radicalism_increases_cultural_erasure_mult | Radicalism increases for the Cultural Erasure Status | multiplicative | percent, bad |  |
| state_radicalism_increases_full_acceptance_mult | Radicalism increases for the Full Acceptance Status | multiplicative | percent, bad |  |
| state_radicalism_increases_open_prejudice_mult | Radicalism increases for the Open Prejudice Status | multiplicative | percent, bad |  |
| state_radicalism_increases_second_rate_citizen_mult | Radicalism increases for the Second-class Citizen Status | multiplicative | percent, bad |  |
| state_radicalism_increases_violent_hostility_mult | Radicalism increases for the Violent Hostility Status | multiplicative | percent, bad |  |
| state_radicals_and_loyalists_from_sol_change_mult | Radicals and Loyalists from Standard of Living changes | multiplicative | percent, neutral |  |
| state_radicals_from_political_movements_mult | Radicals from Political Movements | multiplicative | percent, bad |  |
| state_sell_orders_ammunition_add | Ammunition Sell Orders | additive | neutral |  |
| state_sell_orders_artillery_add | Artillery Sell Orders | additive | neutral |  |
| state_sell_orders_grain_add | Grain Sell Orders | additive | neutral |  |
| state_sell_orders_small_arms_add | Small Arms Sell Orders | additive | neutral |  |
| state_shopkeepers_investment_pool_contribution_add | Shopkeepers Investment Pool contribution | additive | percent, good |  |
| state_shopkeepers_investment_pool_efficiency_mult | Shopkeepers Investment Pool contribution efficiency | multiplicative | percent, good |  |
| state_slave_import_mult | Slave Imports | multiplicative | percent, good |  |
| state_slaves_mortality_mult | Mortality of Slaves | multiplicative | percent, bad |  |
| state_soldiers_investment_pool_contribution_add | Servicemen Investment Pool contribution | additive | percent, good |  |
| state_soldiers_investment_pool_efficiency_mult | Servicemen Investment Pool contribution efficiency | multiplicative | percent, good |  |
| state_soldiers_mortality_mult | Mortality of Servicemen | multiplicative | percent, bad |  |
| state_standard_of_living_add | Standard of Living | additive | good |  |
| state_subvention_export_add | Maximum Subventions on Exports | additive | percent, neutral |  |
| state_subvention_import_add | Maximum Subventions on Imports | additive | percent, neutral |  |
| state_tariff_export_add | Maximum Tariffs on Exports | additive | percent, neutral |  |
| state_tariff_import_add | Maximum Tariffs on Imports | additive | percent, neutral |  |
| state_tax_capacity_add | Taxation Capacity | additive | good |  |
| state_tax_capacity_mult | Taxation Capacity | multiplicative | percent, good |  |
| state_tax_collection_mult | Tax Collection | multiplicative | percent, neutral |  |
| state_tax_waste_add | Tax Waste | additive | percent, bad |  |
| state_trade_advantage_from_capacity_add | Trade Advantage from Capacity | additive | percent, good |  |
| state_trade_advantage_mult | Trade Advantage | multiplicative | percent, good |  |
| state_trade_advantage_same_religion_add | Trade Advantage with Co-Religionists | additive | good |  |
| state_trade_capacity_add | Trade Capacity | additive | good |  |
| state_trade_capacity_mult | Trade Capacity | multiplicative | percent, good |  |
| state_trade_center_max_limit_add | Trade Center Max Level | additive | good |  |
| state_trade_quantity_mult | Traded Quantity | multiplicative | percent, good |  |
| state_turmoil_effects_mult | State Penalties from Turmoil | multiplicative | percent, bad |  |
| state_unincorporated_starting_wages_mult | Starting Wages in Unincorporated States | multiplicative | percent, neutral |  |
| state_upper_strata_expected_sol_add | Minimum Expected Standard of Living for the Upper Strata | additive | neutral |  |
| state_urbanization_per_level_add | Urbanization per Urban Center | additive | neutral |  |
| state_urbanization_per_level_mult | Urbanization per Urban Center | multiplicative | percent, bad |  |
| state_weekly_trades_add | Weekly Trades | additive | good |  |
| state_welfare_payments_add | Welfare Payments | additive | percent, neutral |  |
| state_welfare_payments_mult | Welfare Payments Multiplier | multiplicative | percent, neutral |  |
| state_working_adult_ratio_add | Workforce Ratio | additive | percent, good |  |

### State GUI script

Main article:
GUI script
| Function | Arguments | Output | Description |
|---|---|---|---|
| AbandonColony |  | Command |  |
| AccessAllBuiltRuralBuildings |  | Unknown | Category: const |
| AccessBuilding | BuildingType | Building | Category: const |
| AccessBuildings |  | Unknown | Category: const |
| AccessCappedRuralBuildings |  | Unknown | Category: const |
| AccessDecrees |  | Unknown | Category: const |
| AccessDevelopmentBuildings |  | Unknown | Category: const |
| AccessMarket |  | Market | Category: const |
| AccessModifier |  | Modifier | Category: const |
| AccessOwner |  | Country | Category: const |
| AccessPopCultures |  | Unknown | Category: const |
| AccessPopInterestGroups |  | Unknown | Category: const |
| AccessPopReligions |  | Unknown | Category: const |
| AccessPopTypes |  | Unknown | Category: const |
| AccessPopsList |  | PopList | Category: const |
| AccessSelf |  | State | Category: const |
| AccessShippingLanesFromThisState | Province | Unknown | Category: const |
| AccessShippingLanesOnlyGoodsTransferFromThisState | Province | Unknown | Category: const |
| AccessShippingLanesOnlyPortConnectionsFromThisState | Province | Unknown | Category: const |
| AccessShippingLanesOnlySupplyRoutesFromThisState | Province | Unknown | Category: const |
| AccessSubsistenceBuilding |  | Building | Category: const |
| AccessUncappedRuralBuildings |  | Unknown | Category: const |
| AccessUrbanBuildings |  | Unknown | Category: const |
| CalcPopInstitutionBureaucracyCost |  | CFixedPoint |  |
| CalcSupplyToDemandRatio | Goods | CFixedPoint |  |
| CalcTaxCapacity |  | CFixedPoint |  |
| CalcTaxCapacityBalance |  | CFixedPoint |  |
| CalcTaxCapacityUsage |  | CFixedPoint |  |
| CalcTurmoil |  | CFixedPoint |  |
| GetAdditionalSOLFactorsDescAll |  | CString | Category: nonconst |
| GetAdditionalSOLFactorsDescMiddle |  | CString | Category: nonconst |
| GetAdditionalSOLFactorsDescPoor |  | CString | Category: nonconst |
| GetAdditionalSOLFactorsDescRich |  | CString | Category: nonconst |
| GetAnnualPopNetMigration |  | int64 | Category: nonconst |
| GetArableLandCapacity |  | int32 | Category: nonconst |
| GetAverageAnnualWage |  | CFixedPoint | Category: nonconst |
| GetAverageAnnualWageDesc |  | CString | Category: nonconst |
| GetAverageStandardOfLivingAll |  | CFixedPoint | Category: nonconst |
| GetAverageStandardOfLivingMiddle |  | CFixedPoint | Category: nonconst |
| GetAverageStandardOfLivingPoor |  | CFixedPoint | Category: nonconst |
| GetAverageStandardOfLivingRich |  | CFixedPoint | Category: nonconst |
| GetBaseBureaucracyCostRaw |  | CFixedPoint | Category: nonconst |
| GetBasePopBureaucracyCostRaw |  | CFixedPoint | Category: nonconst |
| GetBestTexture |  | Unknown | Category: nonconst |
| GetBestTextureEffect |  | CString | Category: nonconst |
| GetBlockadeEffectsDesc |  | CString | Category: nonconst |
| GetBlockadeLevel |  | CFixedPoint | Category: nonconst |
| GetBuilding | BuildingType | Building | Category: nonconst |
| GetBuildingsWithGovernmentExpenses |  | Unknown | Category: nonconst |
| GetBuildingsWithTaxationRevenue |  | Unknown | Category: nonconst |
| GetBureaucracyCost |  | CFixedPoint | Category: nonconst |
| GetBureaucracyCostDesc |  | CString | Category: nonconst |
| GetCapitalEffectsDesc |  | CString | Category: nonconst |
| GetCityHubName |  | CString | Category: nonconst |
| GetClaimsDesc |  | CString | Category: nonconst |
| GetColonizers | CString | CString | Category: nonconst |
| GetColonyCompany |  | Company | Category: nonconst |
| GetColonyGrowthDateDesc |  | CString | Category: nonconst |
| GetColonyGrowthModifierDesc |  | CString | Category: nonconst |
| GetColonyProgress |  | CFixedPoint | Category: nonconst |
| GetColonyProgressAsDays |  | int32 | Category: nonconst |
| GetColonyProgressAsFloat |  | float | Category: nonconst |
| GetColonyProvinceProgressDesc |  | CString | Category: nonconst |
| GetColonyTransferName |  | CString | Category: nonconst |
| GetColor |  | CVector4f | Category: nonconst |
| GetConscriptionLimit |  | int32 | Category: nonconst |
| GetConscriptionLimitDesc |  | CString | Category: nonconst |
| GetConstructionEfficiency |  | CFixedPoint | Category: nonconst |
| GetConstructionEfficiencyForBuildingType | BuildingType | CFixedPoint | Category: nonconst |
| GetConstructionEfficiencyForBuildingTypeTooltip | BuildingType | CString | Category: nonconst |
| GetConstructionEfficiencyTooltip |  | CString | Category: nonconst |
| GetController |  | Country | Category: nonconst |
| GetCountry |  | Country | Category: nonconst |
| GetCulturalCommunities |  | Unknown | Category: nonconst |
| GetCurrentBlockadeStrength |  | CFixedPoint | Category: nonconst |
| GetCustom | CustomLocalization | CString | Category: nonconst |
| GetDailyColonyProgress |  | CFixedPoint | Category: nonconst |
| GetDevastationDailyChange |  | CFixedPoint | Category: nonconst |
| GetDevastationDailyChangeBreakdown |  | CString | Category: nonconst |
| GetDevastationEffects |  | CString | Category: nonconst |
| GetDevastationLevel |  | CFixedPoint | Category: nonconst |
| GetEnemyWithHighestOccupation |  | Country | Category: nonconst |
| GetExpectedSOLFactorsDescAll |  | CString | Category: nonconst |
| GetExpectedSOLFactorsDescMiddle |  | CString | Category: nonconst |
| GetExpectedSOLFactorsDescPoor |  | CString | Category: nonconst |
| GetExpectedSOLFactorsDescRich |  | CString | Category: nonconst |
| GetExpectedStandardOfLivingAll |  | CFixedPoint | Category: nonconst |
| GetExpectedStandardOfLivingMiddle |  | CFixedPoint | Category: nonconst |
| GetExpectedStandardOfLivingPoor |  | CFixedPoint | Category: nonconst |
| GetExpectedStandardOfLivingRich |  | CFixedPoint | Category: nonconst |
| GetExportRevenue | Goods | CFixedPoint | Category: nonconst |
| GetExportedAmount | Goods | CFixedPoint | Category: nonconst |
| GetExports |  | Unknown | Category: nonconst |
| GetFamineDesc |  | CString | Category: nonconst |
| GetFarmHubName |  | CString | Category: nonconst |
| GetForestryHubName |  | CString | Category: nonconst |
| GetFormattedStandardOfLivingAll |  | CString | Category: nonconst |
| GetFormattedStandardOfLivingLabelAll |  | CString | Category: nonconst |
| GetFormattedStandardOfLivingLabelMiddle |  | CString | Category: nonconst |
| GetFormattedStandardOfLivingLabelPoor |  | CString | Category: nonconst |
| GetFormattedStandardOfLivingLabelRich |  | CString | Category: nonconst |
| GetFormattedStandardOfLivingMiddle |  | CString | Category: nonconst |
| GetFormattedStandardOfLivingPoor |  | CString | Category: nonconst |
| GetFormattedStandardOfLivingRich |  | CString | Category: nonconst |
| GetFreeArableLandAfterInactiveQueuedEntry |  | CString | Category: nonconst |
| GetGDPContribution |  | CFixedPoint | Category: nonconst |
| GetGDPContributionPercentage |  | CFixedPoint | Category: nonconst |
| GetGDPGoodsContribution | Unknown | CFixedPoint | Category: nonconst |
| GetGDPGoodsContributionBreakdown |  | CString | Category: nonconst |
| GetGDPGoodsContributionPercentage | Unknown | CFixedPoint | Category: nonconst |
| GetGdpRatioOwnedBy | Unknown | CFixedPoint | Category: nonconst |
| GetGdpRatioOwnedByDesc | Country | CString | Category: nonconst |
| GetGoodsSortedByGDP |  | Unknown | Category: nonconst |
| GetGovernmentExpenses |  | CFixedPoint | Category: nonconst |
| GetHarvestConditions |  | Unknown | Category: nonconst |
| GetHomelandsDesc |  | CString | Category: nonconst |
| GetID |  | int32 | Category: nonconst |
| GetIDString |  | CString | Category: nonconst |
| GetImportRevenue | Goods | CFixedPoint | Category: nonconst |
| GetImportedAmount | Goods | CFixedPoint | Category: nonconst |
| GetImports |  | Unknown | Category: nonconst |
| GetIncorporationPartialEffectsDesc |  | CString | Category: nonconst |
| GetIncorporationProgress |  | CFixedPoint | Category: nonconst |
| GetIncorporationTimeDesc |  | CString | Category: nonconst |
| GetIncorporationTimeLeft |  | CString | Category: nonconst |
| GetInfrastructure |  | CFixedPoint | Category: nonconst |
| GetInfrastructureBalance |  | CFixedPoint | Category: nonconst |
| GetInfrastructureDesc |  | CString | Category: nonconst |
| GetInfrastructureUsage |  | CFixedPoint | Category: nonconst |
| GetInfrastructureUsageDesc |  | CString | Category: nonconst |
| GetInsufficientQualificationsForAvailablePositionsDesc |  | CString | Category: nonconst |
| GetInvasions |  | Unknown | Category: nonconst |
| GetJobseekersDesc |  | CString | Category: nonconst |
| GetLiteracy |  | CFixedPoint | Category: nonconst |
| GetMarket |  | Market | Category: nonconst |
| GetMarketAccess |  | CFixedPoint | Category: nonconst |
| GetMarketAccessDesc |  | CString | Category: nonconst |
| GetMarketAccessStatus |  | CString | Category: nonconst |
| GetMarketCapitalEffectsDesc |  | CString | Category: nonconst |
| GetMassMigrationCulture |  | Culture | Category: nonconst |
| GetMassMigrationEndDate |  | CString | Category: nonconst |
| GetMassMigrationOriginCountry |  | Country | Category: nonconst |
| GetMaxBattalions |  | int32 | Category: nonconst |
| GetMaxImbalance |  | CFixedPoint | Category: nonconst |
| GetMaxImbalanceScaledByBasePrice |  | CFixedPoint | Category: nonconst |
| GetMaxPotentialFor | Building | int32 | Category: nonconst |
| GetMigrationAndSlaveTradeDetailsDesc |  | CString | Category: nonconst |
| GetMigrationDesc |  | CString | Category: nonconst |
| GetMigrationDetailsDesc |  | CString | Category: nonconst |
| GetMigrationLabel |  | CString | Category: nonconst |
| GetMigrationPull |  | CFixedPoint | Category: nonconst |
| GetMigrationPullDesc |  | CString | Category: nonconst |
| GetMineHubName |  | CString | Category: nonconst |
| GetModifier |  | Modifier | Category: nonconst |
| GetName |  | CString | Category: nonconst |
| GetNameNoFormatting |  | CString | Category: nonconst |
| GetNameWithCountryFlag |  | CString | Category: nonconst |
| GetNextColonyProvince |  | Province | Category: nonconst |
| GetNonPotentialDiploPlays |  | Unknown | Category: nonconst |
| GetNumArableLandReservedForSubsistence |  | int32 | Category: nonconst |
| GetNumBaseFreeArableLand |  | int32 | Category: nonconst |
| GetNumBuildingsAffectedByGoodsShortage |  | int32 | Category: nonconst |
| GetNumColonizers |  | int32 | Category: nonconst |
| GetNumConstructableUrbanBuildings |  | int32 | Category: nonconst |
| GetNumConsumed | Goods | CFixedPoint | Category: nonconst |
| GetNumFreeArableLand |  | int32 | Category: nonconst |
| GetNumInactiveQueuedArableLandEntry |  | CString | Category: nonconst |
| GetNumJobseekers |  | int64 | Category: nonconst |
| GetNumLoyalists |  | int64 | Category: nonconst |
| GetNumObstinanceSupporters |  | int64 | Category: nonconst |
| GetNumOfObstinatePopsFromMovement | Unknown | int64 | Category: nonconst |
| GetNumProduced | Goods | CFixedPoint | Category: nonconst |
| GetNumProvinces |  | int32 | Category: nonconst |
| GetNumRadicals |  | int64 | Category: nonconst |
| GetNumSubsistenceWorkingAdults |  | int64 | Category: nonconst |
| GetNumUnemployedWorkingAdults |  | int64 | Category: nonconst |
| GetNumUsedArableLand |  | int32 | Category: nonconst |
| GetNumUsedArableLandFullyBuilt |  | int32 | Category: nonconst |
| GetNumUsedArableLandFullyBuiltEntry |  | CString | Category: nonconst |
| GetNumUsedArableLandUnderConstruction |  | int32 | Category: nonconst |
| GetNumUsedArableLandUnderConstructionEntry |  | CString | Category: nonconst |
| GetNumberOfPopsMiddle |  | int64 | Category: nonconst |
| GetNumberOfPopsPoor |  | int64 | Category: nonconst |
| GetNumberOfPopsRich |  | int64 | Category: nonconst |
| GetObstinance |  | CFixedPoint | Category: nonconst |
| GetObstinanceDesc |  | CString | Category: nonconst |
| GetObstinanceEffectScale |  | CFixedPoint | Category: nonconst |
| GetObstinanceEffectsDesc |  | CString | Category: nonconst |
| GetObstinanceFromMovement | Unknown | CFixedPoint | Category: nonconst |
| GetOccupant |  | Country | Category: nonconst |
| GetOccupantsTooltip |  | CString | Category: nonconst |
| GetOccupationPiechartData |  | Unknown | Category: nonconst |
| GetOwner |  | Country | Category: nonconst |
| GetPlanInvasionDesc |  | CString | Category: nonconst |
| GetPolStrForCulture | Culture | int64 | Category: nonconst |
| GetPolStrForReligion | Religion | int64 | Category: nonconst |
| GetPollutionGeneration |  | CFixedPoint | Category: nonconst |
| GetPollutionGenerationDesc |  | CString | Category: nonconst |
| GetPollutionHealthEffectsReduction |  | CFixedPoint | Category: nonconst |
| GetPollutionHealthEffectsReductionDesc |  | CString | Category: nonconst |
| GetPopBirthrate |  | CFixedPoint | Category: nonconst |
| GetPopCultureDesc |  | CString | Category: nonconst |
| GetPopCultureDescByIndex | Unknown | CString | Category: nonconst |
| GetPopGrowthDesc |  | CString | Category: nonconst |
| GetPopMortality |  | CFixedPoint | Category: nonconst |
| GetPopNetGrowth |  | int64 | Category: nonconst |
| GetPopReligionDesc |  | CString | Category: nonconst |
| GetPopReligionDescByIndex | Unknown | CString | Category: nonconst |
| GetPopTotalChange |  | int64 | Category: nonconst |
| GetPops |  | Unknown | Category: nonconst |
| GetPopulationForCulture | Culture | int64 | Category: nonconst |
| GetPopulationForReligion | Religion | int64 | Category: nonconst |
| GetPopulationRatioBelowExpectedStandardOfLiving |  | CFixedPoint | Category: nonconst |
| GetPopulationSize |  | int64 | Category: nonconst |
| GetPortHubName |  | CString | Category: nonconst |
| GetPotentialDecrees |  | Unknown | Category: nonconst |
| GetPotentialDiploPlays |  | Unknown | Category: nonconst |
| GetPotentialLabor |  | int64 | Category: nonconst |
| GetPotentialPopTypeQualificationsDesc |  | CString | Category: nonconst |
| GetPotentialProductionForCountry | Goods Country | CFixedPoint | Category: nonconst |
| GetPotentialProductionForCountryDesc | Goods Country | CString | Category: nonconst |
| GetPotentialQualifications | PopType | int64 | Category: nonconst |
| GetPotentialQualificationsBreakdown | PopType | CString | Category: nonconst |
| GetPotentialQualificationsDesc |  | CString | Category: nonconst |
| GetPotentialUrbanBuildings |  | Unknown | Category: nonconst |
| GetProductionInfo |  | Unknown | Category: nonconst |
| GetRequiredBlockadeStrength |  | CFixedPoint | Category: nonconst |
| GetSamplePops |  | Unknown | Category: nonconst |
| GetSlaveExportMarkersDesc |  | CString | Category: nonconst |
| GetSlaveImportMarkerDesc |  | CString | Category: nonconst |
| GetSlaveTradeDetailsDesc |  | CString | Category: nonconst |
| GetStateRegion |  | StateRegion | Category: nonconst |
| GetSubsistenceBuilding |  | Building | Category: nonconst |
| GetTaxCapacityDesc |  | CString | Category: nonconst |
| GetTaxCapacityEffectsDesc |  | CString | Category: nonconst |
| GetTaxCapacityUsageDesc |  | CString | Category: nonconst |
| GetTaxationRevenue |  | CFixedPoint | Category: nonconst |
| GetTheater | Unknown | Theater | Category: nonconst |
| GetTimedModifiers |  | Unknown | Category: nonconst |
| GetTimedModifiersBreakdown |  | CString | Category: nonconst |
| GetTooltipTag |  | CString | Category: nonconst |
| GetTotalConsumption |  | CFixedPoint | Category: nonconst |
| GetTotalConvoysFromShippingLanesViaState | Province | int32 | Category: nonconst |
| GetTotalExportRevenue |  | CFixedPoint | Category: nonconst |
| GetTotalExportedAmount |  | CFixedPoint | Category: nonconst |
| GetTotalImportRevenue |  | CFixedPoint | Category: nonconst |
| GetTotalImportedAmount |  | CFixedPoint | Category: nonconst |
| GetTotalLabor |  | int64 | Category: nonconst |
| GetTotalPolStr |  | int64 | Category: nonconst |
| GetTotalPortConnectionsViaState | Province | int32 | Category: nonconst |
| GetTotalProduction |  | CFixedPoint | Category: nonconst |
| GetTradeCapacity |  | int32 | Category: nonconst |
| GetTradeCapacityBalance |  | int32 | Category: nonconst |
| GetTradeCapacityDesc |  | CString | Category: nonconst |
| GetTradeCapacityUsage |  | int32 | Category: nonconst |
| GetTradeCapacityUsageDesc |  | CString | Category: nonconst |
| GetTradePotential |  | CFixedPoint | Category: nonconst |
| GetTradePotentialDesc |  | CString | Category: nonconst |
| GetTurmoilEffects |  | CString | Category: nonconst |
| GetUrbanization |  | int32 | Category: nonconst |
| GetUrbanizationBuildingsMaxLevelDesc |  | CString | Category: nonconst |
| GetUrbanizationDesc |  | CString | Category: nonconst |
| GetUrbanizationNeededPerLevelFormatted |  | CString | Category: nonconst |
| GetUrbanizationNeededPerLevelRaw |  | int32 | Category: nonconst |
| GetWeeklyEmigration |  | int64 | Category: nonconst |
| GetWeeklyImmigration |  | int64 | Category: nonconst |
| GetWeeklyPopNetMigration |  | int64 | Category: nonconst |
| GetWeeklySlaveExport |  | int64 | Category: nonconst |
| GetWeeklySlaveImport |  | int64 | Category: nonconst |
| GetWorldMarketAccess |  | CFixedPoint | Category: nonconst |
| GetWorldMarketAccessDesc |  | CString | Category: nonconst |
| GetWorldMarketAccessFormatted |  | CString | Category: nonconst |
| GetYearlyGDP |  | CFixedPoint | Category: nonconst |
| GetYearsToIncorporate |  | CFixedPoint | Category: nonconst |
| HasAnyGoodsShortage |  | bool |  |
| HasBuildingGoodsShortage | Unknown | bool |  |
| HasClaims |  | bool |  |
| HasConstructionQueued |  | bool |  |
| HasDevastation |  | bool |  |
| HasDiscoverableResources |  | bool |  |
| HasFamine |  | bool |  |
| HasGoodsShortage | Unknown | bool |  |
| HasHomelands |  | bool |  |
| HasInsufficientQualificationsForAvailablePositions |  | bool |  |
| HasOccupation |  | bool |  |
| HasPopGoodsShortage | Unknown | bool |  |
| HasSlaveExportMarkers |  | bool |  |
| HasTimedModifiers |  | bool |  |
| HasTurmoilEffects |  | bool |  |
| IncorporateState |  | Command |  |
| IsBeingColonized |  | bool |  |
| IsBeingHighlighted |  | bool |  |
| IsBeingTutorialHighlighted |  | bool |  |
| IsCapitalState |  | bool |  |
| IsCoastal |  | bool |  |
| IsColonizationPaused |  | bool |  |
| IsColonyProgressBlockedByInactiveInterest |  | bool |  |
| IsCompanyColony |  | bool |  |
| IsContested |  | bool |  |
| IsEligibleForMassMigration |  | bool |  |
| IsFullyOccupied |  | bool |  |
| IsGrowingColony |  | bool |  |
| IsImportingSlaves |  | bool |  |
| IsIncorporated |  | bool |  |
| IsIncorporating |  | bool |  |
| IsIsolatedFromMarket |  | bool |  |
| IsMarketCapital |  | bool |  |
| IsMassMigrationTarget |  | bool |  |
| IsOwner | Country | bool |  |
| IsPinnedInOutliner |  | bool |  |
| IsSlaveState |  | bool |  |
| IsSplitState |  | bool |  |
| IsStrategicObjective | Country | bool |  |
| IsTreatyPort |  | bool |  |
| IsUnincorporated |  | bool |  |
| IsValid |  | bool |  |
| IsValidInvasionTarget |  | bool |  |
| IsWorldMarketHub |  | bool |  |
| IsZoomingToCapital |  | bool |  |
| MakeScope |  | Scope |  |
| PanCamera |  | void |  |
| PredictBureaucracyCost |  | CFixedPoint |  |
| Self |  | State |  |
| SortBuildings | Unknown | void |  |
| SortBuildingsWithOrder | Unknown Unknown | void |  |
| TogglePauseColonization |  | Command |  |
| TogglePinInOutliner |  | void |  |
| UnincorporateState |  | Command |  |
| ZoomExtraCloseToCapital |  | void |  |
| ZoomToCapital |  | void |  |

| Function | Arguments | Output | Description |
|---|---|---|---|
| AccessLargestStateOwner |  | Country | Category: const |
| AccessSelf |  | StateRegion | Category: const |
| AccessStrategicRegion |  | StrategicRegion | Category: const |
| AccessTraits |  | Unknown | Category: const |
| Colonize |  | Command |  |
| GetAdjacentLandStateRegionsDesc |  | CString | Category: nonconst |
| GetAdjacentSeaStateRegionsDesc |  | CString | Category: nonconst |
| GetCityHubName |  | CString | Category: nonconst |
| GetColonizeTooltip |  | CString | Category: nonconst |
| GetCustom | CustomLocalization | CString | Category: nonconst |
| GetFarmHubName |  | CString | Category: nonconst |
| GetForestryHubName |  | CString | Category: nonconst |
| GetID |  | int32 | Category: nonconst |
| GetLargestStateInRegion |  | State | Category: nonconst |
| GetLargestStateOwner |  | Country | Category: nonconst |
| GetMineHubName |  | CString | Category: nonconst |
| GetName |  | CString | Category: nonconst |
| GetNameNoFormatting |  | CString | Category: nonconst |
| GetNavalExitStateRegionDesc |  | CString | Category: nonconst |
| GetPollutionEffects |  | CString | Category: nonconst |
| GetPollutionImpact |  | CFixedPoint | Category: nonconst |
| GetPollutionImpactDailyChange |  | CFixedPoint | Category: nonconst |
| GetPollutionImpactTargetLevel |  | CFixedPoint | Category: nonconst |
| GetPollutionLevel |  | CFixedPoint | Category: nonconst |
| GetPortHubName |  | CString | Category: nonconst |
| GetSeaInfrastructure | Country | CFixedPoint | Category: nonconst |
| GetSeaInfrastructureDesc | Country | CString | Category: nonconst |
| GetStatesDesc |  | CString | Category: nonconst |
| GetStrategicRegion |  | StrategicRegion | Category: nonconst |
| GetTooltipTag |  | CString | Category: nonconst |
| IsSplitState |  | bool |  |
| IsValid |  | bool |  |
| MakeScope |  | Scope |  |
| PanCamera |  | void |  |
| Self |  | StateRegion |  |

| Function | Arguments | Output | Description |
|---|---|---|---|
| AccessSelf |  | StateTrait | Category: const |
| GetCustom | CustomLocalization | CString | Category: nonconst |
| GetModifiersDesc |  | CString | Category: nonconst |
| GetName |  | CString | Category: nonconst |
| GetTexture |  | Unknown | Category: nonconst |
| GetTooltipTag |  | CString | Category: nonconst |
| GetUnlocks |  | CString | Category: nonconst |
| MakeScope |  | Scope |  |
| Self |  | StateTrait |  |

| Promote | Arguments | Output | Description |
|---|---|---|---|
| AccessBuilding | BuildingType | Building | Category: const |
| AccessMarket |  | Market | Category: const |
| AccessModifier |  | Modifier | Category: const |
| AccessOwner |  | Country | Category: const |
| AccessPopsList |  | PopList | Category: const |
| AccessStateRegion |  | StateRegion | Category: const |
| AccessSubsistenceBuilding |  | Building | Category: const |
| GetBuilding | BuildingType | Building | Category: nonconst |
| GetColonyCompany |  | Company | Category: nonconst |
| GetController |  | Country | Category: nonconst |
| GetCountry |  | Country | Category: nonconst |
| GetEnemyWithHighestOccupation |  | Country | Category: nonconst |
| GetFoodSecurity |  | FoodSecurity | Category: nonconst |
| GetMarket |  | Market | Category: nonconst |
| GetMassMigrationCulture |  | Culture | Category: nonconst |
| GetMassMigrationOriginCountry |  | Country | Category: nonconst |
| GetModifier |  | Modifier | Category: nonconst |
| GetNextColonyProvince |  | Province | Category: nonconst |
| GetOccupant |  | Country | Category: nonconst |
| GetOwner |  | Country | Category: nonconst |
| GetStateRegion |  | StateRegion | Category: nonconst |
| GetSubsistenceBuilding |  | Building | Category: nonconst |
| GetTheater | Country | Theater | Category: nonconst |
| MakeScope |  | Scope |  |

| Promote | Arguments | Output | Description |
|---|---|---|---|
| AccessLargestStateOwner |  | Country | Category: const |
| AccessStrategicRegion |  | StrategicRegion | Category: const |
| GetLargestStateInRegion |  | State | Category: nonconst |
| GetLargestStateOwner |  | Country | Category: nonconst |
| GetStrategicRegion |  | StrategicRegion | Category: nonconst |
| MakeScope |  | Scope |  |

| Promote | Arguments | Output | Description |
|---|---|---|---|
| MakeScope |  | Scope |  |

## Strategic region

[Strategic regions](Strategic region.md) are collections of state regions. They provide the basis for both diplomatic interests and military HQs. Strategic regions are defined in common/strategic_regions.

Each strategic region is defined as a unique script name, which also acts as a localization key, a capital province, percentage RGB map color, list of states, and optionally a graphical culture.

Example:

```
strategic_region_name = {
	capital_province = province_id	# The province ID for the capital of the state, determines where the UI panel for the interest markers present appears
	map_color = { R% G% B% }		# The percentage of R G B colour for this region for the diplomatic map mode
	states = { state_key_list }		# The states included in this strategic region specified by key
	graphical_culture = "script_name" # Defines which style is used for on-map building models, "European/Western" is the "default" style and left undefined
}
```

Each state can be included in only one strategic region. Naval state regions are also included in strategic regions, one per state. These naval strategic regions do not have a capital province, map color, or graphical culture.

Example naval strategic region:

```
region_baltic_sea = {
	states = { STATE_BALTIC_SEA }
}
```

### Effects, event targets, and triggers

The following are effects, event targets, and triggers that can be used in strategic region scope.

| Effect | Description | Example | Targets |
|---|---|---|---|
| every_harvest_condition | Iterate through all harvest conditions affecting a state, state region, strategic region, or country | every_harvest_condition = { limit = { <triggers> } #optional <effects> } | harvest_condition |
| every_neighbouring_state | Iterate through all states neighbouring current scope Note British spelling | every_neighbouring_state = { limit = { <triggers> } #optional <effects> } | state |
| every_scope_country | Iterate through all countries with a presence in the supported scope (currently: market, state_region, strategic region) | every_scope_country = { limit = { <triggers> } #optional <effects> } | country |
| every_scope_interest_marker | Iterate through all interest markers in a: country, state_region, strategic region | every_scope_interest_marker = { limit = { <triggers> } #optional <effects> } | interest_marker |
| every_scope_state | Iterate through all states including provinces from a: country, state_region, theater, front, or strait | every_scope_state = { limit = { <triggers> } #optional <effects> } | state |
| ordered_harvest_condition | Iterate through all harvest conditions affecting a state, state region, strategic region, or country | ordered_harvest_condition = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | harvest_condition |
| ordered_neighbouring_state | Iterate through all states neighbouring a state region | ordered_neighbouring_state = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | state |
| ordered_scope_country | Iterate through all countries with a presence in the supported scope (currently: market, state_region, strategic region) | ordered_scope_country = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country |
| ordered_scope_interest_marker | Iterate through all interest markers in a: country, state_region, strategic region | ordered_scope_interest_marker = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | interest_marker |
| ordered_scope_state | Iterate through all states including provinces from a: country, state_region, theater, front, or strait | ordered_scope_state = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | state |
| random_harvest_condition | Iterate through all harvest conditions affecting a state, state region, strategic region, or country | random_harvest_condition = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | harvest_condition |
| random_neighbouring_state | Iterate through all states neighbouring a state region | random_neighbouring_state = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | state |
| random_scope_country | Iterate through all countries with a presence in the supported scope (currently: market, state_region, strategic region) | random_scope_country = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country |
| random_scope_interest_marker | Iterate through all interest markers in a: country, state_region, strategic region | random_scope_interest_marker = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | interest_marker |
| random_scope_state | Iterate through all states including provinces from a: country, state_region, theater, front, or strait | random_scope_state = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | state |

| Trigger | Description | Example | Targets |
|---|---|---|---|
| any_harvest_condition | Iterate through all harvest conditions affecting a state, state region, strategic region, or country | any_harvest_condition = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | harvest_condition |
| any_neighbouring_state | Iterate through all states neighbouring a state region | any_neighbouring_state = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | state |
| any_scope_country | Iterate through all countries with a presence in the supported scope (currently: market, strategic region) | any_scope_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country |
| any_scope_interest_marker | Iterate through all interest markers in a: country, strategic region | any_scope_interest_marker = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | interest_marker |
| any_scope_state | Iterate through all states including provinces from a: country, state_region, theater, front, or strait | any_scope_state = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | state |
| check_area | Compares areas of object to another object |  |  |
| has_diplomatic_play | Check if strategic region has a diplomatic play or not |  | boolean |

| Event target | Description | To scope |
|---|---|---|
| ai_colonization_value | Scope to target country AI desire to colonize a strategic region (example: value = ai_colonization_value:root) | value |

### Strategic region GUI script

Main article:
GUI script
| Function | Arguments | Output | Description |
|---|---|---|---|
| AccessFirstDiplomaticPlay |  | DiplomaticPlay | Category: const |
| AccessSelf |  | StrategicRegion | Category: const |
| GetConvoyRaidsDesc |  | CString | Category: nonconst |
| GetCustom | CustomLocalization | CString | Category: nonconst |
| GetFirstDiplomaticPlay |  | DiplomaticPlay | Category: nonconst |
| GetIndex |  | uint32 | Category: nonconst |
| GetInterest | Unknown | Interest | Category: nonconst |
| GetInterests |  | Unknown | Category: nonconst |
| GetLastConvoyRaidingCountriesToTargetDesc | Country | CString | Category: nonconst |
| GetLastConvoyRaidingDamageBy | Country | int32 | Category: nonconst |
| GetLastConvoyRaidingDamageEnemyReductionDesc | Country | CString | Category: nonconst |
| GetLastConvoyRaidingDamageReductionDesc | Country | CString | Category: nonconst |
| GetLastConvoyRaidingDamageTo | Country | int32 | Category: nonconst |
| GetLastConvoyRaidingTargetCountriesByAttackerDesc | Country | CString | Category: nonconst |
| GetName |  | CString | Category: nonconst |
| GetNameNoFormatting |  | CString | Category: nonconst |
| GetTooltipTag |  | CString | Category: nonconst |
| GetTotalGDP |  | CFixedPoint | Category: nonconst |
| HasDiplomaticPlay |  | bool |  |
| IsLand |  | bool |  |
| IsValid |  | bool |  |
| MakeScope |  | Scope |  |
| Self |  | StrategicRegion |  |

| Promote | Arguments | Output | Description |
|---|---|---|---|
| AccessFirstDiplomaticPlay |  | DiplomaticPlay | Category: const |
| GetFirstDiplomaticPlay |  | DiplomaticPlay | Category: nonconst |
| GetInterest | Unknown | Interest | Category: nonconst |
| MakeScope |  | Scope |  |

## References

1. ↑ Based on the define `SPLIT_STATE_PRIME_LAND_WEIGHT`

Modding
Return to top
| Documentation | [Defines](Defines.md) • [Effects](Effect.md) • [Event targets](Event target.md) • [Scopes](Scope.md) • [Triggers](Trigger.md) [Macros](Macro.md) • [Modifier types](Modifier types.md) • [On actions](https://vic3.paradoxwikis.com/On_actions) • [Script value](Script value.md) • [Variables](Variable.md) |
|---|---|

| Scripted content | [Decisions](Decision modding.md) • [Events](Event modding.md) • [History](History modding.md) • [Journal](Journal modding.md) • [Modifiers](Modifier modding.md) • Objectives • [Scripted gui](Scripted gui.md) |
|---|---|

| Scripted types | [Buildings](Building modding.md) • [Characters](Character modding.md) • Concepts • [Countries](Country modding.md) • [Culture](Culture modding.md) • [Decrees](Decree modding.md) • [Diplomacy](Diplomacy modding.md) • [Goods](Goods modding.md) • [Institutions](Institution modding.md) • [Interest groups](Interest group modding.md) • [Laws](Law modding.md) • Parties • [Pops](Pop modding.md) • [Power blocs](Power bloc modding.md) • [Religion](Religion modding.md) • Subject types • [Technology](Technology modding.md) • [Treaties](Treaty modding.md) • [War goals](War goal modding.md) |
|---|---|

| Map | [Map](Map modding.md) • [Geographic regions](Geographic region modding.md) • States |
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
