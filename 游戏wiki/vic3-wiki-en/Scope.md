---
title: Scope
source: https://vic3.paradoxwikis.com/Scope
pageid: 3458
categories: [Potentially_outdated, 1.10, Expand, Modding]
fetched: 2026-10-27
---
Please help with verifying or updating older sections of this article. At least some were last verified for [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) 1.10.

**Scopes** are code objects used with most [effects](Effect.md) and [triggers](Trigger.md). These represent game objects such as countries, states, interest groups, and so on. The current scope is the context in which triggers are evaluated and effects executed.

Most scripted content has a specific scope, such as `country` or `state` as its "base" or **root** scope. Scopes are linked to each other via **event targets** which allows for context switching. Within effects and triggers, iterators and [event targets](Event target.md) also can set scopes.

Most scopes are a particular instance of a game object, determined when the scope is called. Certain scopes refer to game object *types* instead; these generally have the word type in their script name.

*The full list of available scope types an be found in ~/Paradox Interactive/logs/event_scopes.log*

## Overview

### Database Scopes

*Scope* most often refers to an instance of an object defined in the game's database. The definition in the database is reffered to as a scope's **type**. A database scope usually has the following three characteristics:

- Script can read information from it, using [triggers](https://vic3.paradoxwikis.com/Triggers)
- Script can write information to it, using [effects](https://vic3.paradoxwikis.com/Effects)
- Script can switch from one scope to another using [event targets](https://vic3.paradoxwikis.com/Event_targets)The majority of database scopes are generated both during initial game loading (such as map data, laws, goods, etc.) while others are generated during history execution (states, pops, markets, etc.). Scope are also created on runtime via code (character spawns, country rebellions, pop splitting, etc.) or can be created on-demand by script by saving scopes.

### Primitive scope

Numbers, booleans (yes/no) and flag values (`flag:some_string`) are so-called **primitive scopes**. They cannot be modified or accessed, and while "numbers are scopes" can possibly be a confusing statement to beginners, it is useful to know to better understand some advanced functionalities or error logging.

## Scopes and scripting

*Unless specified otherwise, the term "scope" will always refer to a database scope.*

The majority of scripting, both triggers and effects, are done "*in scope*." Triggers and effects have specific scopes they function in and thus the script that calls them must be in the correct scope. in order to correctly check or affect the gamestate.

For example, the `set_ideology` effect must be run in a character scope:

Similarly, the `gold_reserves` trigger must be run in a country scope:

Some effects and triggers work in multiple scope types, and others do not require a specific scope at all, meaning they can be used nearly anywhere. Scopeless script is sometimes referred to as "global", "any", or "none" scope. In the [effect](Effect.md), [trigger](Trigger.md), and [event target](Event target.md) tables, script that does not require a specific scope is noted with `none`.

### Root scope

Scripted content usually has a "base" scope that is provided by the game engine depending on where its execution originated from. This is called the **root** scope. For most scripted content, this is the *country scope*. Depending on the script's origin, certain other saved scopes may be provided by the game engine, such as `scope:target` or `scope:first_country`. This is very common if the scripted started from an on_action.

### Top scope

The `top_scope` is a temporary and abstract object created by the game to manage and display information in localization or GUI.

### Objects and types

Scopes are generally objects, themselves instances of a **type**.

Types are global definitions, setting the base characteristics of their objects, such as default primary cultures and capital in a country definition. For example, an individual building is an object, and the definition of that builind is a type. Most types have limited or no scoping available. Some objects do not have a distinct type or are themselves a type, such as cultures and religions. Types generally have a limited set of effects and triggers that can be run in their scope, and they generally cannot hold variables or static modifiers.

## Accessing and using scopes

Main article:
Event target

### Changing Scope

**Event targets** (also called *Scope Links*) allow us to switch from one scope to another (called "scoping" by the community; reffered to as "context switching" by programmers). The scope can be changed multiple times by opening further nested script blocks. Each time a new block is opened, indentation should be increased. When the block is closed, indentation should be decreased. Keeping a clean indentation helps understanding at a glance in what context [triggers](Trigger.md) and [effects](Effect.md) are interpreted. For example:

```
# This starts in the country scope
ruler = {
  interest_group = {
    add_modifier = modifier_failed_coup
  }
}
```

Certain event targets also **require data** to function. For example:

```
# This is the country event target. In this case, the target scopes to a country with the GBR definition.
c:GBR = {}

# This is the state region target. In this case, the target scopes to the STATE_ATTICA state region.
s:STATE_ATTICA = {}

# This is the market goods target. In this case, the target scopes to the meat good within a market scope.
market = {
  mg:meat = {}
}
 
```

Certain event targets are **global links**. This means that they can be invoked from any scope. For example:

```
# This will always scope to a country with the definition "FRA"
c:FRA

# This will always scope to the "catholic" religion
rel:catholic

# This will always scope to the "liberal" ideology
ideology:ideology_liberal
```

Scope event targets come in two types, contextual or specified.

**Contextual event targets** almost always must be used in a relevant scope, as they refer to scopes relevant to the current scope, such as the capital state or ruler of a country.

| Event target | Description | From scope | To scope |
|---|---|---|---|
| active_law | Scope to the scoped country's active law in the named law group (active_law:lawgroup_trade_policy) | country | law |
| ai_army_comparison | Scope to comparative army strength between two countries (example: value = ai_army_comparison:root) | country | value |
| ai_colonization_value | Scope to target country AI desire to colonize a strategic region (example: value = ai_colonization_value:root) | strategic_region | value |
| ai_gdp_comparison | Scope to comparative GDP between two countries (example: value = ai_army_comparison:root) | country | value |
| ai_ideological_opinion | Scope to AI ideological opinion of scope country on target country (example: value = ai_ideological_opinion:root) | country | value |
| ai_navy_comparison | Scope to comparative navy strength between two countries (example: value = ai_navy_comparison:root) | country | value |
| ai_state_value | Scope to target country AI desire to own scope state (example: value = ai_state_value:root) | state | value |
| ai_subject_value | Scope to AI desire of target country to have scope country as a subject (example: value = ai_subject_value:root) | country | value |
| ai_transit_rights_value | Scope to AI desire of to have transit rights through target country (example: value = ai_transit_rights_value:root) | country | value |
| ai_treaty_export_value | Scope to target country AI desire to export scoped market good (example: value = ai_market_export_value:root) | market_goods | value |
| ai_treaty_fairness | Scope to AI evaluation of how fair (to both sides) it considers existing treaty articles with the target country to be (example: value = ai_treaty_fairness_score:root) | country | value |
| ai_treaty_import_value | Scope to target country AI desire to import scoped market good through treaties (example: value = ai_market_import_value:root) | market_goods | value |
| ai_treaty_port_value | Scope to target country AI desire to have a treaty port in scope state (example: value = ai_treaty_port_value:root) | state | value |
| ai_treaty_trade_value | Scope to target country AI desire to import and export scoped market good (example: value = ai_market_trade_value:root) | market_goods | value |
| ai_treaty_value | Scope to AI evaluation of how favorable to itself it considers existing treaty articles with the target country to be (example: value = ai_treaty_value:root) | country | value |
| amended_treaty | Scope to the treaty the scoped treaty is amending | treaty, treaty_options | treaty |
| army_size | Number of battalions of scope country, excluding currently raised conscripts. | country | value |
| army_size_including_conscripts | Number of battalions of scope country, including currently raised conscripts. | country | value |
| army_size_including_raised_conscripts | Number of battalions of scope country, including currently raised conscripts but excluding unraised conscripts. | country | value |
| attached_law | Links from an amendment scope to the law the amendment is attached to | amendment | law |
| attacker_side | Scope from a battle to the BattleSide corresponding to the attacker | battle | battle_side |
| attacker_warleader | Scope to the attacker warleader of a war | war | country |
| average_defense | Returns the average defense of units on Front on the same side as Country | front | value |
| average_expected_sol | Get the average expected Standard of Living of the scope | country, state | value |
| average_offense | Returns the average offense of units on Front on the same side as Country | front | value |
| average_progressiveness | Get the average progressiveness of the scoped character or interest group | character, interest_group | value |
| average_sol | Get the average Standard of Living of the scope | country, state | value |
| b | Scope to the building of specified key in the state, example: b:building_port | state | building |
| base_price | Get the base price of the scoped good | goods | value |
| battle | Scope from a battle side to the battle itself | battle_side | battle |
| binding_period | Get the original binding period in days when the treaty was signed for the scoped treaty | treaty, treaty_options | value |
| building | Scope to the related building | new_combat_unit | building |
| building_levels | Get the total number of non-subsistence building levels of the scoped country | country | value |
| cached_ai_coastal_population | Scope to total coastal population recorded in AI spending variables (example: value = cached_ai_coastal_population) | country | value |
| cached_ai_incorporated_coastal_population | Scope to total incorporated coastal population recorded in AI spending variables (example: value = cached_ai_incorporated_coastal_population) | country | value |
| cached_ai_incorporated_population | Scope to total incorporated population recorded in AI spending variables (example: value = cached_ai_incorporated_population) | country | value |
| cached_ai_overseas_subject_population | Scope to total population in direct non-adjacent subjects recorded in AI spending variables (example: value = cached_ai_overseas_subject_population) | country | value |
| cached_ai_subject_population | Scope to total population in direct subjects recorded in AI spending variables (example: value = cached_ai_subject_population) | country | value |
| cached_ai_total_population | Scope to total population recorded in AI spending variables (example: value = cached_ai_total_population) | country | value |
| cached_ai_unincorporated_coastal_population | Scope to total unincorporated coastal population recorded in AI spending variables (example: value = cached_ai_unincorporated_coastal_population) | country | value |
| cached_ai_unincorporated_population | Scope to total unincorporated population recorded in AI spending variables (example: value = cached_ai_unincorporated_population) | country | value |
| capital | Scope to the capital state of a country | country | state |
| civil_war | Scope to the civil war started by the scoped (revolutionary) political movement. | political_movement | civil_war |
| civil_war_origin_country | Scope to the origin country of a civil war country | country | country |
| colonial_growth_per_colony | Scope to the country's colonial growth per colony value (example: colonial_growth_per_colony > 0) | country | value |
| combat_width | Scope to combat width multiplier of scope province | province | value |
| command_limit_num_units | Get the baseline number of units from their military formation a commander would normally get, depending on their command limit | character | value |
| commander | Scope from a military formation to its commander character | military_formation | character |
| commander_military_formation | Scope to the Military Formation of a Character. | character | military_formation |
| company | Scope to the scoped country's company of the named company type (company:company_rheinmetall) | country | company |
| compare_complex_value | A comparison trigger that needs a parsable string parameter that will return its value in the context it is used eg: scope:root.number_of(armies) | varies | value |
| compare_value | A comparison trigger that will return its value in the context it is used eg: root.gold | varies | value |
| controller | Scope to the controller of the object | province, state | country |
| country | Scope to the country of a military formation or ship | military_formation, ship | country |
| country_definition | Scope to country's definition | country | country_definition |
| credit | Scope to the current amount of max credit the country can take | country | value |
| culture | Scope to pop's or character's culture | character, new_combat_unit, political_movement, pop | culture |
| current_hq | Returns the current HQ of the scoped military formation (may not be valid if the formation is not currently stationed in an HQ) | military_formation | hq |
| currently_active_law_in_group | Scope from a law to the currently active law in that group | law | law |
| currently_enacting_law | Scope from a country to the law that they're currently enacting | country | law |
| decree_cost | Scope to a state's cost for a certain decree authority > decree_cost:decree_road_maintaintenance | state | value |
| defender_side | Scope from a battle to the BattleSide corresponding to the defender | battle | battle_side |
| defender_warleader | Scope to the defender warleader of a war | war | country |
| defense | Returns the unit's defense rating (including impact from their commander) | new_combat_unit | value |
| demoralized | Returns the unit's number of demoralized manpower | new_combat_unit | value |
| detection | Links from a fleet scope to the total detection of the ships in the fleet | military_formation | value |
| diplomatic_pact_expense_ratio | Scope to the ratio of diplomatic pact expenses to income for this country, clamped 0-1 (example: value = diplomatic_pact_expense_ratio) | country | value |
| diplomatic_pact_other_country | Scope to the other country of the diplomatic pact in scope, example: diplomatic_pact_other_country(root) | diplomatic_pact | country |
| diplomatic_play | Scope from a war to its diplomatic play | war | diplomatic_play |
| enforced_on_country | Scope to the enforced_on_country of an enforced treaty | treaty | country |
| enforcer_country | Scope to the enforcer_country of an enforced treaty | treaty | country |
| executive | Scope from a company to its executive character | company | character |
| first_country | Scope to the first_country of any of: diplomatic pact treaty treaty options treaty article's treaty treaty article options (for mutual article types only) | diplomatic_pact, treaty, treaty_article, treaty_article_options, treaty_options | country |
| flagship | Get the flagship of the scoped country | country | ship |
| front | Scope to a front from various scopes From a battle to the front where it takes place From a character to the front where they are at or travelling towards From a military formation to the front it is currently at From a province to the front that contains it From an invasion to the invasion front | battle, character, invasion, military_formation, province | front |
| front_length | Returns the number of provinces in Front | front | value |
| gdp | Get the scoped country's yearly predicted GDP | country, state | value |
| get_ruler_for | Scopes from country to a character that would be ruler, under the given transfer of power type get_ruler_for:parliamentary_elective = { effects... } | country | character |
| goal_value | Scope to the journal entry's goal value | journal_entry | value |
| goods | Scope to the goods traded by a trade route | market_goods, state_goods | goods |
| government_size | Get the scoped country's current number of Parties & independent IGs in government | country | value |
| group | Scope from a building object or type to its group | building, building_type | building_group |
| heir | Scope to the heir of a country | country | character |
| home_country | Scopes to the home country of an exile | character, pop | country |
| home_hq | Returns the home HQ of the scoped military formation | military_formation | hq |
| ideology | Dual use Scope to a ideology from its name (ideology:ideology_anarchist) Scope to the ideology of the scoped character | character, none | ideology |
| ig | Scope to the interest group of specified key belonging to the country, example: ig:ig_armed_forces | country, political_movement | interest_group |
| imposed_law | Scope from a country to the law currently imposed on them (enacting or not) | country | law |
| imposer_of_law | Scope from a country to the country currently imposing a law on them | country, law | country |
| income | Get the current weekly income of the scoped country | country | value |
| income_transfer_expenses | Scope to the amount of money scope country is transferring to other countries via treaties & pacts (example:income_transfer_expenses >= 100) | country | value |
| income_transfer_relative_expenses | Scope to the fraction of their income country is transferring to other countries via treaties & pacts (example:income_transfer_relative_expenses >= 0.2) | country | value |
| infamy | Scope to infamy of scope country (example: infamy >= 2) | country | value |
| initiator | Scope to the initiator of the object | diplomatic_play | country |
| input_building_type | Scope to the building type input in a treaty article | treaty_article, treaty_article_options | building_type |
| input_company | Scope to the company input in a treaty article | treaty_article, treaty_article_options | company |
| input_country | Scope to the country input in a treaty article | treaty_article, treaty_article_options | country |
| input_goods | Scope to the goods input in a treaty article | treaty_article, treaty_article_options | goods |
| input_law | Scope to the law input in a treaty article | treaty_article, treaty_article_options | law_type |
| input_market_goods | Scope to the market goods input in a treaty article (example: input_market_goods:root) | treaty_article, treaty_article_options | market_goods |
| input_quantity | Scope to the quantity input in a treaty article | treaty_article, treaty_article_options | value |
| input_ship | Scope to the ship input in a treaty article | treaty_article, treaty_article_options | ship |
| input_state | Scope to the state input in a treaty article | treaty_article, treaty_article_options | state |
| input_strategic_region | Scope to the strategic region input in a treaty article | treaty_article, treaty_article_options | strategic_region |
| institution | Scope to a country's institution from its name (institution:institution_health_system) | country | institution |
| interest_group | Scope to the interest group of the character! | character | interest_group |
| interest_group_type | Scope to the type of the scoped character's interest group | character | interest_group_type |
| invasion | Returns the invasion of the scoped front if any | front | invasion |
| invasion_attacker | If used in an invasion scope, scope to the country executing the invasion. | invasion | country |
| invasion_defender | If used in an invasion scope, scope to the country the attacked state is controlled by. | invasion | country |
| investment | Scope to current investment level in an institution (example: investment < investment_max) | institution | value |
| investment_max | Scope to the country's current maximum investment level in an institution (example: investment < investment_max) | institution | value |
| investment_pool_income | Get the current weekly investment pool income of the scoped country | country | value |
| is_setup | Scope to true/false if gamestate is being initialized! | none | boolean |
| je | Scope to the journal entry of specified key belonging to the country, example: je:je_antarctica | country | journal_entry |
| je_tutorial | Scope to the active tutorial lesson's journal entry (do not use this outside tutorial) | none | journal_entry |
| land_controller_hq | Returns the province or state controller land HQ | province, state | hq |
| land_hq | Returns the province or state owner local land HQ | province, state | hq |
| largest_exporting_market | Scope to the largest exporting market for the scope market good to the local market | market_goods | market |
| largest_importing_market | Scope to the largest importing market for the scope market good from the local market | market_goods | market |
| law_type | Scope to a law type from its name (law_type:law_protected_speech) or from a scoped law | law, none | law_type |
| leader | Scope to the leader of the interest group | interest_group | character |
| legitimacy | Scope to the current amount of legitimacy in country | country | value |
| level | Scope to the level of a building | building | value |
| level_after_queued_constructions | Scope to the level of a building after all queued constructions finish | building | value |
| lobby_foreign_anti_clout | Scope to the total clout of all anti-country foreign policy lobbies targeting a specific country (lobby_foreign_anti_clout:root >= 0.2) | country | value |
| lobby_foreign_pro_clout | Scope to the total clout of all pro-country foreign policy lobbies targeting a specific country (lobby_foreign_pro_clout:root >= 0.2) | country | value |
| lobby_in_government_foreign_anti_clout | Scope to the total clout of all anti-country foreign policy lobbies in government targeting a specific country (lobby_in_government_foreign_anti_clout:root >= 0.2) | country | value |
| lobby_in_government_foreign_pro_clout | Scope to the total clout of all pro-country foreign policy lobbies in government targeting a specific country (lobby_in_government_foreign_pro_clout:root >= 0.2) | country | value |
| lobby_join_weight | Scope to the join weight of an interest group to a particular lobby (lobby_join_weight:root >= 5) | interest_group | value |
| lobby_war_opposition | Scope to the total clout of all lobbies that oppose the scoped war (lobby_war_opposition:root >= 0.2) | country | value |
| lobby_war_support | Scope to the total clout of all lobbies that support the scoped war (lobby_war_support:root >= 0.2) | country | value |
| manpower | Returns the unit's manpower | new_combat_unit | value |
| market | Scope to the market of the object | building, country, market, market_goods, province, state, state_goods, state_region | market |
| market_capital | Scope to the market capital of a country | country | state |
| market_export_cap | Get the maximum amount of goods the market can export based on it's production of the scoped MarketGoods | market_goods | value |
| market_import_cap | Get the maximum amount of goods the market can import based on it's consumption of the scoped MarketGoods | market_goods | value |
| mass_migration_culture | Scope to the mass migration target culture of a state | state | culture |
| mg | Scope from a market to the MarketGoods with the specified key, (example: mg:tools) | market | market_goods |
| migration_pull | Get the migration pull for a state or the mass migration pull for a country. | country, state | value |
| military_expenses | Get the current military expenses (slaves, wages and goods) of the scoped country | country | value |
| military_expenses_share | Get the current share of military expenses (slaves, wages and goods) relative to the total expenses of the scoped country | country | value |
| mobilization | Returns the unit's mobilization value between 0 and 1 | new_combat_unit | value |
| modifier | Scope to the value of the modifier type of specified key belonging to the current object, example: modifier:country_influence_add | battle_side, building, character, country, interest_group, market, power_bloc, state | boolean, value |
| momentum | Get the scoped party's raw momentum | party | value |
| morale | Returns the unit's morale | new_combat_unit | value |
| most_desired_law | Scope to the law type that political movement most desires to be enacted (if any). | political_movement | law_type |
| mutual_trade_value_with_country | Scope to the total base value of goods traded in trade routes between the two markets (example: mutual_trade_value_with_country:root >= 1000) | country | value |
| named_script_value | A script value that will calculate and returns its value in the context it is used | none | color, value |
| national_awakening_state_region | Links from a culture scope to the state region with an active national awakening for that culture | culture | state_region |
| naval_combat_power | Scope to the country's navy combat power (example: naval_combat_power > 100) | country | value |
| naval_controller_hq | Returns the province or state controller navy HQ | province | hq |
| naval_hostility_average_damage_dealt | Scope to average damage dealt by this country in naval hostilities it initiated over the lookback period. Returns -1 if no hostilities found. | country | value |
| naval_hq | Returns the province or state owner local navy HQ | province | hq |
| naval_vulnerability | Scope to a country's naval vulnerability score based on trade reliance and coastal GDP share, capped at a define maximum | country | value |
| navy_size | Number of flotillas of scope country. | country | value |
| nf | Scope to a Decree of specified key applied to the state, example: nf:decree_road_maintaintenance | state | decree |
| num_active_interests | Scope to the number of active interests a country has num_active_interests > 5 | country | value |
| num_active_natural_interests | Scope to the number of active natural interests a country has num_active_natural_interests > 5 | country | value |
| num_active_plays | Get the current number of active Diplomatic Plays the scoped country started | country | value |
| num_active_ships | Get the number of active ships for a country, commander or military formation OR Get the number of active ships for military formations in the province that are allied to the specified country | character, country, military_formation, province | value |
| num_active_ships_in_battle | Get the number of active ships in battle for a country, commander or military formation OR Get the number of active ships in battle for military formations in the province that are allied to the specified country | character, country, military_formation, province | value |
| num_active_ships_not_in_battle | Get the number of active ships not in battle for a country, commander or military formation OR Get the number of active ships not in battle for military formations in the province that are allied to the specified country | character, country, military_formation, province | value |
| num_admirals | Scope to the country's number of admirals | country | value |
| num_alliances | Get the total number of alliances of the scoped country (example: num_alliances:root >= 2) | country | value |
| num_alliances_and_defensive_pacts_with_allies | Scope to the number of alliances target country has with allies of scope country (example: num_alliances_and_defensive_pacts_with_allies:root >= 2) | country | value |
| num_alliances_and_defensive_pacts_with_rivals | Scope to the number of alliances & defensive pacts target country has with rivals of scope country (example: num_alliances_and_defensive_pacts_with_rivals:root >= 2) | country | value |
| num_battalions | Returns the number of active battalions under a commander | character | value |
| num_characters | Scope to the country's number of characters | country | value |
| num_colony_projects | Get the scoped country's current number of incomplete / in progress colony projects | country | value |
| num_commanderless_units | Number of units in a MilitaryFormation which currently don't have a commander due to commanders Command Limit. Obs: defeated commanders do not command units, i.e., the more defeated commanders, the more commanderless units. | military_formation | value |
| num_commanders | Scope to the country's number of commanders | country | value |
| num_defending_battalions | Returns the total number of units in battle on Front on the same side as Country, example: num_defending_battalions(root) | front | value |
| num_defensive_pacts | Scope to the number of defensive pacts target country has in total (example: num_defensive_pacts >= 2) | country | value |
| num_garrison_units | Returns the number of units garrisoned in a HQ | hq | value |
| num_generals | Scope to the country's number of generals | country | value |
| num_income_transfer_pacts | Scope to the number of income-transferring (to others) pacts target country has in total (example: num_income_transfer_pacts >= 2) | country | value |
| num_income_transfer_treaty_articles | Scope to the number of income-transferring (to others) treaty articles target country has in total (example: num_income_transfer_treaty_articles >= 2) | country | value |
| num_income_transfers | Scope to the number of income-transferring (to others) pacts and treaty articles target country has in total (example: num_income_transfers >= 2) | country | value |
| num_incorporated_states | Get the scoped country's current number of incorporated states | country | value |
| num_interests | Scope to the number of interests a country has (including inactive) num_interests > 5 | country | value |
| num_mandates | Scope to the number of available mandates of the scoped power bloc (power_bloc.num_mandates > 0) | power_bloc | value |
| num_mobilized_battalions | Returns the number of fully mobilized units under a General | character | value |
| num_natural_interests | Scope to the number of natural interests a country has (including inactive) num_natural_interests > 5 | country | value |
| num_non_destroyed_ships | Get the number of non-destroyed ships for a country, commander or military formation OR Get the number of non-destroyed ships for military formations in the province that are allied to the specified country | character, country, military_formation, province | value |
| num_non_destroyed_ships_in_battle | Get the number of non-destroyed ships in battle for a country, commander or military formation OR Get the number of non-destroyed ships in battle for military formations in the province that are allied to the specified country | character, country, military_formation, province | value |
| num_non_destroyed_ships_not_in_battle | Get the number of non-destroyed ships not in battle for a country, commander or military formation OR Get the number of non-destroyed ships not in battle for military formations in the province that are allied to the specified country | character, country, military_formation, province | value |
| num_obligations_earned | Scope from a country to the number of obligations others owe them (=which they have earned) | country | value |
| num_pending_events | Scope to the number of pending events in scope country, generally or for a specified category num_pending_events > 0 num_pending_events:enactment > 0 | country | value |
| num_politicians | Scope to the country's number of politicians | country | value |
| num_positive_relations | Get the current number of countries with positive Relation with the scoped country | country | value |
| num_provinces | Get the scoped entity's current number of provinces | front, state, state_region | value |
| num_queued_constructions | Scope to the number of queued constructions target country has in total (example: num_queued_constructions >= 2) | country | value |
| num_queued_government_constructions | Scope to the number of queued government constructions target country has in total (example: num_queued_government_constructions >= 2) | country | value |
| num_queued_private_constructions | Scope to the number of queued private constructions target country has in total (example: num_queued_private_constructions >= 2) | country | value |
| num_rivals | Scope to the number of rivals target country has in total (example: num_rivals >= 2) | country | value |
| num_ruling_igs | Get the scoped country's current number of IGs in government | country | value |
| num_shared_rivals | Scope to the number of shared rivals scope country has with target country (example: num_shared_rivals:root >= 2) | country | value |
| num_ships | Get the number of ships for a country, commander or military formation OR Get the number of ships for military formations in the province that are allied to the specified country | character, country, military_formation, province | value |
| num_ships_in_battle | Get the number of ships in battle for a country, commander or military formation OR Get the number of ships in battle for military formations in the province that are allied to the specified country | character, country, military_formation, province | value |
| num_ships_not_in_battle | Get the number of ships not in battle for a country, commander or military formation OR Get the number of ships not in battle for military formations in the province that are allied to the specified country | character, country, military_formation, province | value |
| num_states | Get the scoped country's current number of states | country | value |
| num_total_battalions | Returns the total number of units on Front on the same side as Country, example: num_total_battalions(root) | front | value |
| num_unincorporated_states | Get the scoped country's current number of unincorporated states | country | value |
| num_units | Get the number of active units for a commander or military formation Get the number of active units for military formations in the province that are allied to the specified country | character, military_formation, province | value |
| num_units_in_battle | Get the number of active units in battle for a commander or military formation Get the number of active units in battle for military formations in the province that are allied to the specified country | character, military_formation, province | value |
| num_units_not_in_battle | Get the number of active units not in battle for a commander or military formation Get the number of active units not in battle for military formations in the province that are allied to the specified country | character, military_formation, province | value |
| num_units_share | Share of units a commander has considering his command limit. Example: if the character has 30 Command Limit, the fleet has 60 total Command Limit, and the formation has 50 total flotillas, then the character should get 25 flotillas for their battle) | character | value |
| num_world_market_hub_trade_center_levels | Get the total number of trade center levels associated with scope world market hub state | state | value |
| offense | Returns the unit's offense rating (including impact from their commander) | new_combat_unit | value |
| opposing_commander | Scope from a character in battle to the character on the other side of the battle | character | character |
| opposite_battle_side | Scope from a battle side to its opposite | battle_side | battle_side |
| overlord | Scope to the direct overlord of the country in scope | country | country |
| owner | Scope to the owner country of object | building, character, company, country, decree, institution, interest_group, interest_marker, journal_entry, law, market, market_goods, military_formation, new_combat_unit, political_movement, pop, province, state | country |
| owning_company | Scope to the company owning the scoped country | country | company |
| parent_law_type | Links from an amendment scope to the law type that is considered the amendment's parent | amendment | law_type |
| participants | Get the total number of participating countries in the scoped market | market | value |
| party | Scope to the party that an IG is supporting | interest_group | party |
| pirated_trade_value_by | Scope to the average weekly base value of goods pilfered from this country by a target country (example: pirated_trade_value_by:root >= 50) | country | value |
| player_owed_obligation_days_left | Scope to number of days left on an obligation in diplomatic relations scope (example: obligation_days_left >= 2) | diplomatic_relations | value |
| political_movement | If used in a character scope, scope to the political movement that character supports. If used in a revolution civil war scope, scope to the movement that started the revolution. If used in an interest group scope, scope to the group's dominant movement. | character, civil_war | political_movement |
| pop_weight_modifier_scale | Get the Pop's weight modifier scale multiplier | pop | value |
| popularity | Get the scoped character's popularity, normally ranging between -100 and +100 | character | value |
| population_below_expected_sol | Scope to the current percentage of the state's population that are below their expected standard of living (0-1) | state | value |
| power_bloc | Scope to the power bloc for the scoped country | country | power_bloc |
| power_bloc_leader | Scope to the leader country of the scoped power bloc | power_bloc | country |
| power_projection | Get the power projection value of the scoped formation, unit, or ship | military_formation, new_combat_unit, ship | value |
| power_struggle_contender | Scope to the contender country if there is a power struggle | power_bloc | country |
| prev | The previous scope | none | varies |
| principal | Get the current debt principal of the country | country | value |
| prosperity | Scope to the amount of prosperity for scope company (example: prosperity >= 2) | company | value |
| province | Scope from a battle side to the province in which the battle is being fought | battle_side | province |
| py | Scope to the active party of specified key belonging to the country, example: py:communist_party | country | party |
| region | Scope to the strategic region of the object! | building, diplomatic_play, hq, interest_marker, province, state, state_region | strategic_region |
| region_state | Scope to the state owned by the target country, (example: region_state:BIC) | state_region | state |
| relations | Scope to relations between two countries (example: relations:root >= 2) | country | value |
| relations_change_rate | Scope to daily change in relations progress between two countries (example: relations_change_rate:root > 0) | country | value |
| religion | Scope to country or country definition's primary religion or pop religion | character, country, country_definition, political_movement, pop | religion |
| remaining_binding_period | Get the current remaining binding period in days for the scoped treaty | treaty, treaty_options | value |
| required_construction | Get the required amount of construction for scope building type | building_type | value |
| root | The head of the current top scope eg: receiver of an event, taker of a decision | none | varies |
| ruler | Scope to the ruler of a country | country | character |
| scope_relations | Scope to relations value in diplomatic relations scope (example: scope_relations >= 2) | diplomatic_relations | value |
| scope_tension | Scope to tension value in diplomatic relations scope (example: scope_tension >= 2) | diplomatic_relations | value |
| screening | Links from a fleet scope to the total screening of the ships in the fleet | military_formation | value |
| second_country | Scope to the second_country of any of: diplomatic pact treaty treaty options treaty article's treaty treaty article options (for mutual article types only) | diplomatic_pact, treaty, treaty_article, treaty_article_options, treaty_options | country |
| sg | Scope from a state to the StateGoods with the specified key, example: sg:wood | state | state_goods |
| ship_fleet | Links from a ship scope to the ship fleet | ship | military_formation |
| ship_group | Scope from a ship to its group or Scope to a ship group from its name (ship_group:ship_group_capital_ships) | none, ship | ship_group |
| shipping_lane | Scope to the shipping lane for the military formation, or treaty article (goods transfer) | military_formation, treaty_article | shipping_lanes |
| slaves_role | Scope from building type to its slaves role pop type | building_type | pop_type |
| source_country | Scope to the source_country of any of: treaty article (for directed article types only) treaty article options (for directed article types only) | treaty_article, treaty_article_options | country |
| sponsor | Links from an amendment scope to the interest group that sponsored the amendment | amendment | interest_group |
| state | Scope to the state of the object | building, market, pop, province | state |
| state_region | Scope to the state region of a state | state | state_region |
| target | Scope to the target of the object | diplomatic_catalyst, diplomatic_play, journal_entry, political_lobby | varies |
| target_country | Scope to the target_country of any of: treaty article (for directed article types only) treaty article options (for directed article types only) | treaty_article, treaty_article_options | country |
| technology_being_researched | Scope to the current technology a country is researching | country | technology |
| techs_researched | Scope to the current amount of techs researched of a country | country | value |
| tension | Scope to tension between two countries (example: tension:root >= 2) | country | value |
| theater | Scope from a BattleSide or State to its theater | battle_side, state | theater |
| this | The current scope | none | varies |
| top_overlord | Scope to the top overlord of the country in scope | country | country |
| total_crew_needed | Get the total crew needed by all ships of a country | country | value |
| total_export_value | Scope to the total value of scope country's exports to the world market (example: total_export_value >= 1000) | country | value |
| total_import_value | Scope to the total value of scope country's imports from the world market (example: total_import_value >= 1000) | country | value |
| total_marine_capacity | Get the total marine capacity across all fleets of a country | country | value |
| total_pirated_trade_value | Scope to the total average weekly base value of goods pilfered via piracy between two countries in a diplomatic relations scope (example: total_pirated_trade_value >= 100) | diplomatic_relations | value |
| total_trade_value | Scope to the total value of scope country's trade with the world market (example: total_trade_value >= 1000) | country | value |
| trade_center | Scope to the trade center state of the market! | market | state |
| training_rate | Scope to the current maximum weekly training rate of a building | building | value |
| treaty | Scope to the treaty a treaty article belongs to | treaty_article | treaty |
| treaty_exports | Get the current number of treaty (NOT world market) exports of the good to the market of the scoped MarketGoods | market_goods | value |
| treaty_imports | Get the current number of treaty (NOT world market) imports of the good to the market of the scoped MarketGoods | market_goods | value |
| type | Scope from an object to its type | amendment, building, company, diplomatic_catalyst, diplomatic_play, harvest_condition_area, institution, interest_group, law, political_lobby, political_movement, ship, strait | amendment_type, building_type, company_type, diplomatic_play_type, harvest_condition_type, institution_type, interest_group_type, law_type, political_movement_type, ship_type, strait_type |
| value | A numeric literal value eg: 1, 5.2, -6 | none | value |
| var | Reference a previous set variable in scope via its name eg: var:mortal_enemy | varies | varies |
| visibility | Links from a fleet scope to the total visibility of the ships in the fleet | military_formation | value |
| vulnerability | Links from a fleet scope to the total vulnerability of the ships in the fleet | military_formation | value |
| war | Scope from a diplomatic play to its war | diplomatic_play | war |
| weekly_prosperity_change | Scope to the weekly prosperity change for scope company (example: weekly_prosperity_change >= 2) | company | value |
| workplace | Scope to the workplace of a pop | pop | building |
| world_market_hub | Scope to the world market hub state associated with the scoped state | state | state |

**Specified event targets** are often scopeless as they refer to a specific object. Some specified event targets still require a certain scope as they refer to an instance of a type, rather than a unique object. Specified scope event targets typically use a colon `:` followed by a script key, such as a building type, country tag, or state region. A few use parentheses instead.

| Event target | Description | From scope | To scope |
|---|---|---|---|
| active_law | Scope to the scoped country's active law in the named law group (active_law:lawgroup_trade_policy) | country | law |
| ai_army_comparison | Scope to comparative army strength between two countries (example: value = ai_army_comparison:root) | country | value |
| ai_colonization_value | Scope to target country AI desire to colonize a strategic region (example: value = ai_colonization_value:root) | strategic_region | value |
| ai_gdp_comparison | Scope to comparative GDP between two countries (example: value = ai_army_comparison:root) | country | value |
| ai_ideological_opinion | Scope to AI ideological opinion of scope country on target country (example: value = ai_ideological_opinion:root) | country | value |
| ai_navy_comparison | Scope to comparative navy strength between two countries (example: value = ai_navy_comparison:root) | country | value |
| ai_state_value | Scope to target country AI desire to own scope state (example: value = ai_state_value:root) | state | value |
| ai_subject_value | Scope to AI desire of target country to have scope country as a subject (example: value = ai_subject_value:root) | country | value |
| ai_transit_rights_value | Scope to AI desire of to have transit rights through target country (example: value = ai_transit_rights_value:root) | country | value |
| ai_treaty_export_value | Scope to target country AI desire to export scoped market good (example: value = ai_market_export_value:root) | market_goods | value |
| ai_treaty_fairness | Scope to AI evaluation of how fair (to both sides) it considers existing treaty articles with the target country to be (example: value = ai_treaty_fairness_score:root) | country | value |
| ai_treaty_import_value | Scope to target country AI desire to import scoped market good through treaties (example: value = ai_market_import_value:root) | market_goods | value |
| ai_treaty_port_value | Scope to target country AI desire to have a treaty port in scope state (example: value = ai_treaty_port_value:root) | state | value |
| ai_treaty_trade_value | Scope to target country AI desire to import and export scoped market good (example: value = ai_market_trade_value:root) | market_goods | value |
| ai_treaty_value | Scope to AI evaluation of how favorable to itself it considers existing treaty articles with the target country to be (example: value = ai_treaty_value:root) | country | value |
| amendment_type | Scope to an amendment type from its name (amendment_type:key) | none | amendment_type |
| array_define | Reference the value of a numeric value in an array define: array_define:Namespace\|Name\|Index. Index is 0-based. | none | value |
| average_defense | Returns the average defense of units on Front on the same side as Country | front | value |
| average_offense | Returns the average offense of units on Front on the same side as Country | front | value |
| b | Scope to the building of specified key in the state, example: b:building_port | state | building |
| bg | Scope to a building group from its name (bg:bg_logging) | none | building_group |
| bt | Scope to a building type, example: bt:building_tooling_workshops | none | building_type |
| c | Scope to the country with specified tag, example: c:GBR | none | country |
| catalyst_type | Scope to a diplomatic catalyst type from its name (catalyst_type:catalyst_relations_level_improved) | none | diplomatic_catalyst_type |
| cd | Scope to the country definition with specified tag, example: cd:FRA | none | country_definition |
| company | Scope to the scoped country's company of the named company type (company:company_rheinmetall) | country | company |
| company_type | Scope to a company type from its name (company_type:company_rheinmetall) | none | company_type |
| compare_complex_value | A comparison trigger that needs a parsable string parameter that will return its value in the context it is used eg: scope:root.number_of(armies) | varies | value |
| cu | Scope to the culture with specified key, example: cu:welsh | none | culture |
| decree_cost | Scope to a state's cost for a certain decree authority > decree_cost:decree_road_maintaintenance | state | value |
| define | Reference the value of a numeric or color define: define:Namespace\|Name | none | value |
| diplomatic_pact_other_country | Scope to the other country of the diplomatic pact in scope, example: diplomatic_pact_other_country(root) | diplomatic_pact | country |
| flag | A localization key, ex. flag:the_boss | none | flag |
| g | Scope to the goods with specified key, example: g:iron | none | goods |
| get_ruler_for | Scopes from country to a character that would be ruler, under the given transfer of power type get_ruler_for:parliamentary_elective = { effects... } | country | character |
| global_productivity | Scope to global productivity values (example: global_productivity:high_threshold) | none | value |
| global_var | Reference a previous set global variable via its name eg: global_var:important_thing | none | varies |
| harvest_condition_type | Scope to a harvest condition type from its name (harvest_condition_type:drought) | none | harvest_condition_type |
| i | Scope to ideology specified by key, example: i:ideology_patriarchal | none | ideology |
| identity | Scope to the power bloc identity from its name (identity:key) | none | power_bloc_identity |
| ideology | Dual use Scope to a ideology from its name (ideology:ideology_anarchist) Scope to the ideology of the scoped character | character, none | ideology |
| ig | Scope to the interest group of specified key belonging to the country, example: ig:ig_armed_forces | country, political_movement | interest_group |
| ig_trait | Scope to the Interest Group trait with specified key, example: ig_trait:ig_trait_xenophobia | none | interest_group_trait |
| ig_type | Scope to an interest group type, example: ig_type:ig_landowners | none | interest_group_type |
| infamy_threshold | Scope to infamy level threshold for comparison purposes (infamy_threshold:infamous) | none | value |
| input_market_goods | Scope to the market goods input in a treaty article (example: input_market_goods:root) | treaty_article, treaty_article_options | market_goods |
| institution | Scope to a country's institution from its name (institution:institution_health_system) | country | institution |
| je | Scope to the journal entry of specified key belonging to the country, example: je:je_antarctica | country | journal_entry |
| law_type | Scope to a law type from its name (law_type:law_protected_speech) or from a scoped law | law, none | law_type |
| lobby_foreign_anti_clout | Scope to the total clout of all anti-country foreign policy lobbies targeting a specific country (lobby_foreign_anti_clout:root >= 0.2) | country | value |
| lobby_foreign_pro_clout | Scope to the total clout of all pro-country foreign policy lobbies targeting a specific country (lobby_foreign_pro_clout:root >= 0.2) | country | value |
| lobby_in_government_foreign_anti_clout | Scope to the total clout of all anti-country foreign policy lobbies in government targeting a specific country (lobby_in_government_foreign_anti_clout:root >= 0.2) | country | value |
| lobby_in_government_foreign_pro_clout | Scope to the total clout of all pro-country foreign policy lobbies in government targeting a specific country (lobby_in_government_foreign_pro_clout:root >= 0.2) | country | value |
| lobby_join_weight | Scope to the join weight of an interest group to a particular lobby (lobby_join_weight:root >= 5) | interest_group | value |
| lobby_type | Scope to a political lobby type from its name (lobby_type:lobby_pro_country) | none | political_lobby_type |
| lobby_war_opposition | Scope to the total clout of all lobbies that oppose the scoped war (lobby_war_opposition:root >= 0.2) | country | value |
| lobby_war_support | Scope to the total clout of all lobbies that support the scoped war (lobby_war_support:root >= 0.2) | country | value |
| local_var | Reference a previous set local variable via its name eg: local_var:person_of_interest | none | varies |
| mg | Scope from a market to the MarketGoods with the specified key, (example: mg:tools) | market | market_goods |
| mobilization_option | Scope to a mobilization option from its name (mobilization_option:key) | none | mobilization_option |
| modifier | Scope to the value of the modifier type of specified key belonging to the current object, example: modifier:country_influence_add | battle_side, building, character, country, interest_group, market, power_bloc, state | boolean, value |
| movement_type | Scope to a political movement type from its name (movement_type:movement_religious_majority) | none | political_movement_type |
| mutual_trade_value_with_country | Scope to the total base value of goods traded in trade routes between the two markets (example: mutual_trade_value_with_country:root >= 1000) | country | value |
| naval_hostility_damage | Scope to damage points inflicted by this country against another in active naval hostilities (example: naval_hostility_damage:root >= 50) | country | value |
| nf | Scope to a Decree of specified key applied to the state, example: nf:decree_road_maintaintenance | state | decree |
| num_active_ships | Get the number of active ships for a country, commander or military formation OR Get the number of active ships for military formations in the province that are allied to the specified country | character, country, military_formation, province | value |
| num_active_ships_in_battle | Get the number of active ships in battle for a country, commander or military formation OR Get the number of active ships in battle for military formations in the province that are allied to the specified country | character, country, military_formation, province | value |
| num_active_ships_not_in_battle | Get the number of active ships not in battle for a country, commander or military formation OR Get the number of active ships not in battle for military formations in the province that are allied to the specified country | character, country, military_formation, province | value |
| num_alliances | Get the total number of alliances of the scoped country (example: num_alliances:root >= 2) | country | value |
| num_alliances_and_defensive_pacts_with_allies | Scope to the number of alliances target country has with allies of scope country (example: num_alliances_and_defensive_pacts_with_allies:root >= 2) | country | value |
| num_alliances_and_defensive_pacts_with_rivals | Scope to the number of alliances & defensive pacts target country has with rivals of scope country (example: num_alliances_and_defensive_pacts_with_rivals:root >= 2) | country | value |
| num_defending_battalions | Returns the total number of units in battle on Front on the same side as Country, example: num_defending_battalions(root) | front | value |
| num_non_destroyed_ships | Get the number of non-destroyed ships for a country, commander or military formation OR Get the number of non-destroyed ships for military formations in the province that are allied to the specified country | character, country, military_formation, province | value |
| num_non_destroyed_ships_in_battle | Get the number of non-destroyed ships in battle for a country, commander or military formation OR Get the number of non-destroyed ships in battle for military formations in the province that are allied to the specified country | character, country, military_formation, province | value |
| num_non_destroyed_ships_not_in_battle | Get the number of non-destroyed ships not in battle for a country, commander or military formation OR Get the number of non-destroyed ships not in battle for military formations in the province that are allied to the specified country | character, country, military_formation, province | value |
| num_pending_events | Scope to the number of pending events in scope country, generally or for a specified category num_pending_events > 0 num_pending_events:enactment > 0 | country | value |
| num_shared_rivals | Scope to the number of shared rivals scope country has with target country (example: num_shared_rivals:root >= 2) | country | value |
| num_ships | Get the number of ships for a country, commander or military formation OR Get the number of ships for military formations in the province that are allied to the specified country | character, country, military_formation, province | value |
| num_ships_in_battle | Get the number of ships in battle for a country, commander or military formation OR Get the number of ships in battle for military formations in the province that are allied to the specified country | character, country, military_formation, province | value |
| num_ships_not_in_battle | Get the number of ships not in battle for a country, commander or military formation OR Get the number of ships not in battle for military formations in the province that are allied to the specified country | character, country, military_formation, province | value |
| num_ships_of_group | Number of ships of the provided ship group in the scoped country or military formation | country, military_formation | value |
| num_total_battalions | Returns the total number of units on Front on the same side as Country, example: num_total_battalions(root) | front | value |
| num_units | Get the number of active units for a commander or military formation Get the number of active units for military formations in the province that are allied to the specified country | character, military_formation, province | value |
| num_units_in_battle | Get the number of active units in battle for a commander or military formation Get the number of active units in battle for military formations in the province that are allied to the specified country | character, military_formation, province | value |
| num_units_not_in_battle | Get the number of active units not in battle for a commander or military formation Get the number of active units not in battle for military formations in the province that are allied to the specified country | character, military_formation, province | value |
| p | Scope to province specified by hex key, example: p:x1A6E5B | none | province |
| pirated_trade_value_by | Scope to the average weekly base value of goods pilfered from this country by a target country (example: pirated_trade_value_by:root >= 50) | country | value |
| play_type | Scope to a diplomatic play type from its name (play_type:dp_default_treaty_article) | none | diplomatic_play_type |
| pop_type | Scope to a pop type from its name (pop_type:laborers) | none | pop_type |
| principle | Scope to the power bloc principle from its name (principle:key) | none | power_bloc_principle |
| principle_group | Scope to the power bloc principle group from its name (principle_group:key) | none | power_bloc_principle_group |
| py | Scope to the active party of specified key belonging to the country, example: py:communist_party | country | party |
| rank_value | Scope to rank value of a particular country rank (rank_value:great_power) | none | value |
| region_state | Scope to the state owned by the target country, (example: region_state:BIC) | state_region | state |
| rel | Scope to the religion with specified key, example: rel:catholic | none | religion |
| relations | Scope to relations between two countries (example: relations:root >= 2) | country | value |
| relations_change_rate | Scope to daily change in relations progress between two countries (example: relations_change_rate:root > 0) | country | value |
| relations_threshold | Scope to relations threshold level for comparison purposes (relations_threshold:warm) | none | value |
| s | Scope to state region specified by key, example: s:STATE_UTAH | none | state_region |
| scope | Reference a previously saved scope via its name eg: scope:target | none | varies |
| sg | Scope from a state to the StateGoods with the specified key, example: sg:wood | state | state_goods |
| ship_group | Scope from a ship to its group or Scope to a ship group from its name (ship_group:ship_group_capital_ships) | none, ship | ship_group |
| ship_type | Scope to a ship type from its name (ship_type:ship_type_frigate) | none | ship_type |
| sr | Scope to the strategic region of specified key, example: sr:region_persia | none | strategic_region |
| strait_trade_importance_by | Scope to the trade importance of goods this country is trading through straits controlled by a target country. Accumulated value is multiplied by STRAIT_FULL_CONTROL_TRADE_IMPORTANCE_MULT for straits where the controller controls both sides (example: strait_trade_importance_by:root >= 100) | country | value |
| strait_type | Scope to a strait type from its name (strait_type:key) | none | strait_type |
| tension | Scope to tension between two countries (example: tension:root >= 2) | country | value |
| tension_threshold | Scope to tension level threshold for comparison purposes (tension_threshold:warm) | none | value |
| unit_type | Scope to a combat unit type from its name (unit_type:key) | none | combat_unit_type |
| var | Reference a previous set variable in scope via its name eg: var:mortal_enemy | varies | varies |

*Available event targets are shown in docs/event_targets.log . This includes information about supported input and output scopes.*

### Chaining scopes

Scopes can be chained using **dot linkage** like this: `a.b.c.` This is sometimes referred to as "scope stacking" or "dot chains". This allows quickly changing through scopes without having to create a new block for each scope level. Dot linkage is not available for iterators.

For example, to check if any country has a capital in a certain strategic region, either of the following methods return the same result:

Without dot linkage

```
any_country = {
    capital = {
        region = sr:<region_name>
    }
}

ruler = {
    interest_group = {
        ig_clout = #
    }
}
```

With dot linkage

```
any_country = {
    capital.region = sr:<region_name>
}

ruler.interest_group.ig_clout = #
```

### Scope assertion

`?=` is the assertion operator. This checks that the scoped object exists before attempting a comparison or scoping to it for script execution.

For example, this script:

```
capital ?= state_region.s:STATE_HOME_COUNTIES
```

Is functionally identical to this script:

```
exists = capital
capital = state_region.s:STATE_HOME_COUNTIES
```

This helps avoid errors from unset/null scopes and makes your script more compact. However, if you *need* the error printed in the event of a null scope – such as when debugging, you should allow the error to be printed by using `=`.

### Special targets

`root` - The *origin scope* of a particular script instance. This depends on where the script was executed from. While this is often the country scope, this is neither a convention nor consistent. If the root scope has been provided, script can switch back to it or use it as a comparison at any time. *Note:* *The root scope is not inherently the player or country scope, although this is often the case.*

`prev` - The *previous scope* in your scope chain. This can be used to access an object available from within a specific scope and quickly return to your original scope. The `prev` target can be chained to "walk backwards" through a scope chain, i.e. `prev.prev = {}`, though this is not recommended beyond two steps.

`this` - The *current scope*. This is used to compare the identity of an object once you've scoped to it. This is commonly used with **iterators** or in situations where you are not sure if the scoped object is the one you want (for example, a journal entry being gated to a single country).

### Saved scopes

A **saved scope** is a script-defined event target that points to a specific scope. Saved scopes persist only for the duration of an **effect chain** (called an event chain in the docs). Saving an object to a scope allows you to access that scope further downstream in your script. If necessary, they can also be manually cleared using the `clear_saved_scope` effect.

Scopes are saved using the `save_scope_as` effect and accessed with the `scope:` event target. For example:

```
# This effect saves a country with poor relations and then triggers a diplomatic incident with them.
random_country = {
  limit = {
    relations:root < relations_threshold:neutral
  }
  save_scope_as = unfriendly_country
}
create_diplomatic_incident = {
  target = scope:unfriendly_country
  value = 10
}
```

Saved scopes are **forwarded to events and effects called from script**. Saved scopes persist until the end of the effect chain, at which point they are discarded. If an effect chain begins from an on_action or certain other systems, the game engine will sometimes forward scopes that are relevant to that on_action, such `scope:target` or `scope:recipient` Only scopes that are available at the time the effect is called will be forwarded. For example:

```
ruler = {
  save_scope_as = ruler_scope # this scope will be forwarded to ruler_event.1
}
trigger_event = ruler_event.1
capital = {
  save_scope_as = capital_scope # this scope was saved after the trigger_event effect, and thus will not be forwarded to ruler_event.1
}
 
```

Saved scopes can be passed from the UI to scripted guis or script values/custom localization with `AddScope`:

- `"[ScriptedGui.Execute( GuiScope.SetRoot( GetPlayer.MakeScope ).AddScope( 'target', CharacterWindow.GetCharacter.MakeScope ).End )]"`
- `"[GuiScope.SetRoot( GetPlayer.MakeScope ).AddScope( 'target', CharacterWindow.GetCharacter.MakeScope).ScriptValue('sval_name')|0]"`

### Value triggers

Some triggers can be used in value comparison triggers - those triggers can also be used as scope links that return `value` scope and can therefore be used at the end of scope stacking.

Such triggers will usually have the following line in their documentation:

`Traits: <, <=, =, !=, >, >=`

## Iterators

**Iterators** – also called lists – are [effects](Effect.md) or [triggers](Trigger.md) which iterate through all eligible scopes of a certain type, returning them for checking triggers or executing effects.

There are four types of iterators, one for triggers and three for effects.

| Prefix | Description |
|---|---|
| any_<name> | Trigger scope, checks that any returned scope returns true for contained triggers. Can use count op value or percent op value to check a specified amount or ratio With count = all or percent = 1 , it requires all scopes to return true Can use filter = { <triggers> } with count or percent to limit returned scopes |
| every_<name> | Effect scope, executes effects on all returned scopes Can use limit = { <triggers> } to narrow the scopes returned |
| ordered_<name> | Effect scope, executes effects on returned scopes, by default only first scope in ordering is returned Uses order_by = value to determine the ordering, ordered from most positive to most negative Can use limit = { <triggers> } to narrow the scopes returned Can use position = int to select a different position in order, 0-indexed Can use min = int and max = value to limit which and how many scopes are returned in the ordering Can use check_range_bounds = no to prevent error logging if the number of returned scopes is less than the range betweem min and max |
| random_<name> | Effect scope, executes effects on a single random returned scope Can use limit = { <triggers> } to narrow the scopes returned Can use weight = { mtth_blocks } to weight the random selection |

### Trigger iterators

See also:
Trigger
Trigger iterators all start with `any_` and return true if any scope meets the contained triggers. This behavior can be changed with the parameter `count op int value` or `percent op value [0-1]` when then requires at least the specified number or percent of the scope to meet the contained triggers. These use the usual [comparison operators](Trigger.md).

If `count` or `percent` are used, another parameter `filter` can be used to limit which scopes are considered.

When negated, trigger iterators behave like `count = all` is set by default, such that it returns true if no scope meets the contained triggers; actually setting `count = all`, however, inverts the behavior back to returning true if any scope does not meet the contained triggers.

| Trigger | Description | Example | Scopes | Targets |
|---|---|---|---|---|
| any_active_law | Iterate through all active laws in a country | any_active_law = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | law |
| any_active_party | Iterate through all active political parties in a country | any_active_party = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | party |
| any_character | Iterate through all characters globally | any_character = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | character |
| any_character_in_exile_pool | Iterate through characters in the exile pool | any_character_in_exile_pool = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | character |
| any_character_in_void | Iterate through characters in the void | any_character_in_void = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | character |
| any_character_role | Iterate through all roles of the scoped character | any_character_role = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | character | character_role |
| any_civil_war | Iterate through all civil wars related to the scoped country | any_civil_war = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | civil_war |
| any_cobelligerent_in_diplo_play | Iterate through all co-belligerents of scope country in all diplomatic plays (includes wars) | any_cobelligerent_in_diplo_play = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | country |
| any_cobelligerent_in_war | Iterate through all co-belligerents of scope country in all wars | any_cobelligerent_in_war = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | country |
| any_combat_unit | Iterate through all combat units of input scope | any_combat_unit = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | battle, building, front, hq, military_formation | new_combat_unit |
| any_company | Iterate through all companies in a country | any_company = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | company |
| any_country | Iterate through all countries globally | any_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | country |
| any_country_in_<georegion_short_name> | Iterate through all countries in the specified geographic region | any_country_in_<georegion_short_name> = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | country |
| any_country_strategic_region | Iterate through all strategic regions containing states owned by the scoped country | any_country_strategic_region = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | strategic_region |
| any_decentralized_country | Iterate through all countries that are decentralized | any_decentralized_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | country |
| any_diplomatic_catalyst | Iterate through all diplomatic catalysts in the recent memory of a country | any_diplomatic_catalyst = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | diplomatic_catalyst |
| any_diplomatic_play | Iterate through all diplomatic plays globally | any_diplomatic_play = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | diplomatic_play |
| any_diplomatically_relevant_country | Iterate through all diplomatically relevant countries of a country scope | any_diplomatically_relevant_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | country |
| any_direct_subject | Any country directly below current in hierarchy | any_direct_subject = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | country |
| any_enemy_in_diplo_play | Iterate through all enemies of scope country in all diplomatic plays (includes wars) | any_enemy_in_diplo_play = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | country |
| any_enemy_in_war | Iterate through all enemies of scope country in all wars | any_enemy_in_war = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | country |
| any_harvest_condition | Iterate through all harvest conditions affecting a state, state region, strategic region, or country | any_harvest_condition = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, state, state_region, strategic_region | harvest_condition |
| any_in_global_list | Iterate through all items in global list. | any_in_global_list = { list = name / variable = name <count=num/all> / <percent=fixed_point> <triggers> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list | none |  |
| any_in_hierarchy | Any country in current hierarchy, including current | any_in_hierarchy = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | country |
| any_in_list | Iterate through all items in list. | any_in_list = { list = name / variable = name <count=num/all> / <percent=fixed_point> <triggers> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list | none |  |
| any_in_local_list | Iterate through all items in local list. | any_in_local_list = { list = name / variable = name <count=num/all> / <percent=fixed_point> <triggers> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list | none |  |
| any_influenced_interest_group | Iterate through all interest groups influenced by a political movement | any_influenced_interest_group = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | political_movement | interest_group |
| any_interest_group | Iterate through all interest groups in a country | any_interest_group = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | interest_group |
| any_key_in_global_variable_map | Iterate through all keys in a global variable map. | any_key_in_global_variable_map = { variable = name filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | none |
| any_key_in_local_variable_map | Iterate through all keys in a local variable map. | any_key_in_local_variable_map = { variable = name filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | none |
| any_key_in_variable_map | Iterate through all keys in a variable map. | any_key_in_variable_map = { variable = name filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | none |
| any_law | Iterate through all laws in a country | any_law = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | law |
| any_lobby_member | Iterate through all interest group members of a lobby | any_lobby_member = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | political_lobby | interest_group |
| any_market | Iterate through all markets globally | any_market = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | market |
| any_market_goods | Iterate through all active (market) goods in a market | any_market_goods = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | market | market_goods |
| any_member | Iterate through all interest group members of a party | any_member = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | party | interest_group |
| any_military_formation | Iterate through all military formations currently present at input scope | any_military_formation = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, front, hq | military_formation |
| any_neighbouring_state | Iterate through all states neighbouring a state region | any_neighbouring_state = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, state, state_region, strategic_region | state |
| any_overlord_or_above | Any country above current in hierarchy | any_overlord_or_above = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | country |
| any_owned_country | Iterate through all countries owned by the scoped company | any_owned_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | company | country |
| any_participant | Any of two participants of the diplomatic pact in a scope | any_participant = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | diplomatic_pact | country |
| any_political_lobby | Iterate through all political lobbies in a country or interest group | any_political_lobby = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, interest_group | political_lobby |
| any_political_movement | Iterate through all political movements in a country | any_political_movement = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | political_movement |
| any_possible_amendment_type | Iterate through amendment types that could be added to the scoped law | any_possible_amendment_type = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | law | amendment_type |
| any_potential_party | Iterate through all potential political parties in a country | any_potential_party = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | party |
| any_power_bloc | Iterate through all power blocs | any_power_bloc = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | power_bloc |
| any_power_bloc_member | Iterate through all members of the scoped power bloc including the leader | any_power_bloc_member = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | power_bloc | country |
| any_preferred_law | Iterate through all active and possible laws in an interest group's country, ordered by how much they prefer that law | any_preferred_law = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | interest_group | law |
| any_primary_culture | Primary cultures of the scoped country or country definition | any_primary_culture = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, country_definition | culture |
| any_province | Iterate through all Provinces in the scoped State | any_province = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | state | province |
| any_province_in_<georegion_short_name> | Iterate through all provinces in the specified geographic region | any_province_in_<georegion_short_name> = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | province |
| any_rival_country | Any country that is being rivaled by the country in a scope | any_rival_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | country |
| any_rivaling_country | Any country that is rivaling the country in a scope | any_rivaling_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | country |
| any_scope_admiral | Iterate through all admirals in a: country, interest group, or military formation | any_scope_admiral = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, front, interest_group, military_formation | character |
| any_scope_ally | Iterate through all allies to a: country | any_scope_ally = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | country |
| any_scope_amendment | Iterate through amendments of the scoped law | any_scope_amendment = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | law | amendment |
| any_scope_army | Iterate through all armies currently present at input scope | any_scope_army = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, front, hq | military_formation |
| any_scope_article | Iterate through articles of the scoped treaty | any_scope_article = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | treaty | treaty_article |
| any_scope_article_option | Iterate through article_options of the scoped treaty or treaty_options | any_scope_article_option = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | treaty, treaty_options | treaty_article_options |
| any_scope_building | Iterate through all buildings in a: state, country | any_scope_building = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, state | building |
| any_scope_character | Iterate through all characters in a: country, interest group, or front | any_scope_character = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, front, interest_group, military_formation | character |
| any_scope_country | Iterate through all countries with a presence in the supported scope (currently: market, strategic region) | any_scope_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | market, state_region, strategic_region | country |
| any_scope_culture | Iterate through all cultures in the scope | any_scope_culture = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, state | culture |
| any_scope_diplomatic_pact | Any diplomatic pact of the country in a scope | any_scope_diplomatic_pact = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | diplomatic_pact |
| any_scope_fleet | Iterate through all fleets currently present at input scope | any_scope_fleet = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, hq | military_formation |
| any_scope_front | Iterate through all Fronts related to the scoped War | any_scope_front = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | war | front |
| any_scope_general | Iterate through all generals in a: country, interest group, front, or military formation | any_scope_general = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, front, interest_group, military_formation | character |
| any_scope_held_interest_marker | Iterate through all interest markers held by a country | any_scope_held_interest_marker = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | interest_marker |
| any_scope_homeland_state | Iterate through all states that are a homeland for the scoped culture, or a homeland of any primary culture of the scoped country | any_scope_homeland_state = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | character, country | state |
| any_scope_initiator_ally | Iterate through all allies to an initiator in a: diplomatic play | any_scope_initiator_ally = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | diplomatic_play | country |
| any_scope_interest_marker | Iterate through all interest markers in a: country, strategic region | any_scope_interest_marker = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, state_region, strategic_region | interest_marker |
| any_scope_je_involved | Iterate through all involved in a journal entry | any_scope_je_involved = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | journal_entry | country |
| any_scope_play_involved | Iterate through all involved in a: diplomatic play | any_scope_play_involved = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | diplomatic_play | country |
| any_scope_politician | Iterate through all politicians in a: country or interest group | any_scope_politician = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, front, interest_group, military_formation | character |
| any_scope_pop | Iterate through all pops in a: country, state, interest group, culture | any_scope_pop = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, culture, interest_group, state | pop |
| any_scope_regional_hqs | Iterate through regional HQs of the scoped company | any_scope_regional_hqs = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | company | building |
| any_scope_ship | Iterate through all ships in a country or military formation | any_scope_ship = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, military_formation | ship |
| any_scope_state | Iterate through all states including provinces from a: country, state_region, theater, front, or strait | any_scope_state = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, front, state_region, strait, strategic_region, theater | state |
| any_scope_strait | Iterate through all straits with a land endpoint in the scoped state or country | any_scope_strait = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, state | strait |
| any_scope_target_ally | Iterate through all allies to a target in a: diplomatic play | any_scope_target_ally = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | diplomatic_play | country |
| any_scope_theater | Iterate through all theaters in a: country | any_scope_theater = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | theater |
| any_scope_treaty | Iterate through in force treaties binding the scoped country | any_scope_treaty = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | treaty |
| any_scope_violate_sovereignty_interested_parties | Iterate through all countries that would be interested if country in scope has their sovereignty violated | any_scope_violate_sovereignty_interested_parties = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | country |
| any_scope_violate_sovereignty_wars | Iterate through all relevant wars if target country had their sovereignty violated by scoped country | any_scope_violate_sovereignty_wars = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | war |
| any_scope_war | Iterate through all wars related to the scope | any_scope_war = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | war |
| any_sea_node_adjacent_state | Iterate through all states that share a sea node with a state | any_sea_node_adjacent_state = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | state | state |
| any_state | Iterate through all states globally | any_state = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | state |
| any_state_in_<georegion_short_name> | Iterate through all states in the specified geographic region | any_state_in_<georegion_short_name> = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | state |
| any_state_region | Iterate through all state regions | any_state_region = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | state_region |
| any_state_region_in_<georegion_short_name> | Iterate through all state regions in the specified geographic region | any_state_region_in_<georegion_short_name> = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | state_region |
| any_strategic_objective | Iterate through all Strategic Objective states from the scoped Country | any_strategic_objective = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | state |
| any_strategic_region | Iterate through all strategic regions globally | any_strategic_region = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | strategic_region |
| any_strategic_region_in_<georegion_short_name> | Iterate through all strategic regions in the specified geographic region | any_strategic_region_in_<georegion_short_name> = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | strategic_region |
| any_subject_of_subject | Any country below direct subjects in hierarchy | any_subject_of_subject = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | country |
| any_subject_or_below | Any country below current in hierarchy | any_subject_or_below = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | country |
| any_supporting_character | Iterate through all characters that support the scoped political movement | any_supporting_character = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | political_movement | character |
| any_treaty | Iterate through treaties (both in force and drafts) | any_treaty = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | treaty |
| any_valid_mass_migration_culture | Lists for cultures in the scoped country that are valid for mass migration | any_valid_mass_migration_culture = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | culture |
| any_war_participant | Iterate through all participants in a war | any_war_participant = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | war | country |

### Effect iterators

See also:
Effect
Effect iterators begin with `every_`, `ordered_`, and `random_`. `every_` iterators apply their effects to all returned scopes, `ordered_` iterators order their returned scopes by a value comparison and apply their effects to the first in the ordering, and `random_` iterators apply their effects to a single random returned scope.

All three can use the parameter `limit` to apply triggers that limit which scopes are returned. If the limit triggers are specific enough, such that they return only a single scope, all three types of iterator are effectively identical.

`ordered_` iterators can return a scope besides the first by using the parameter `position = int` which is 0-indexed. Additionally, the parameters `min = int` and `max = value` can be used to limit how many and which scopes are returned in the ordering. `min` sets the "top" position, using the same 0-indexing as `position`, while `max` determines the number of scopes to return, from the floored value given. If not specified, `min = 0` and `max = 1`. Setting `min` without setting `max` considers `max` as equal to the iterator's list size. Use `check_range_bounds = no` to prevent error logging when using min or max, otherwise using a min or max higher than the list size gives and error.

| Effect | Description | Example | Scopes | Targets |
|---|---|---|---|---|
| every_active_law | Iterate through all active laws in a country | every_active_law = { limit = { <triggers> } #optional <effects> } | country | law |
| every_active_party | Iterate through all active political parties in a country | every_active_party = { limit = { <triggers> } #optional <effects> } | country | party |
| every_character | Iterate through all characters globally | every_character = { limit = { <triggers> } #optional <effects> } | none | character |
| every_character_in_exile_pool | Iterate through characters in the exile pool | every_character_in_exile_pool = { limit = { <triggers> } #optional <effects> } | none | character |
| every_character_in_void | Iterate through characters in the void | every_character_in_void = { limit = { <triggers> } #optional <effects> } | none | character |
| every_character_role | Iterate through all roles of the scoped character | every_character_role = { limit = { <triggers> } #optional <effects> } | character | character_role |
| every_civil_war | Iterate through all civil wars related to the scoped country | every_civil_war = { limit = { <triggers> } #optional <effects> } | country | civil_war |
| every_cobelligerent_in_diplo_play | Iterate through all co-belligerents of scope country in all diplomatic plays (includes wars) | every_cobelligerent_in_diplo_play = { limit = { <triggers> } #optional <effects> } | country | country |
| every_cobelligerent_in_war | Iterate through all co-belligerents of scope country in all wars | every_cobelligerent_in_war = { limit = { <triggers> } #optional <effects> } | country | country |
| every_combat_unit | Iterate through all combat units of input scope | every_combat_unit = { limit = { <triggers> } #optional <effects> } | battle, building, front, hq, military_formation | new_combat_unit |
| every_company | Iterate through all companies in a country | every_company = { limit = { <triggers> } #optional <effects> } | country | company |
| every_country | Iterate through all countries globally | every_country = { limit = { <triggers> } #optional <effects> } | none | country |
| every_country_in_<georegion_short_name> | Iterate through all countries in the specified geographic region | every_country_in_<georegion_short_name> = { limit = { <triggers> } #optional <effects> } | none | country |
| every_country_strategic_region | Iterate through all strategic regions containing states owned by the scoped country | every_country_strategic_region = { limit = { <triggers> } #optional <effects> } | country | strategic_region |
| every_decentralized_country | Iterate through all countries that are decentralized | every_decentralized_country = { limit = { <triggers> } #optional <effects> } | none | country |
| every_diplomatic_catalyst | Iterate through all diplomatic catalysts in the recent memory of a country | every_diplomatic_catalyst = { limit = { <triggers> } #optional <effects> } | country | diplomatic_catalyst |
| every_diplomatic_play | Iterate through all diplomatic plays globally | every_diplomatic_play = { limit = { <triggers> } #optional <effects> } | none | diplomatic_play |
| every_diplomatically_relevant_country | Iterate through all diplomatically relevant countries of a country scope | every_diplomatically_relevant_country = { limit = { <triggers> } #optional <effects> } | country | country |
| every_direct_subject | Any country directly below current in hierarchy | every_direct_subject = { limit = { <triggers> } #optional <effects> } | country | country |
| every_enemy_in_diplo_play | Iterate through all enemies of scope country in all diplomatic plays (includes wars) | every_enemy_in_diplo_play = { limit = { <triggers> } #optional <effects> } | country | country |
| every_enemy_in_war | Iterate through all enemies of scope country in all wars | every_enemy_in_war = { limit = { <triggers> } #optional <effects> } | country | country |
| every_harvest_condition | Iterate through all harvest conditions affecting a state, state region, strategic region, or country | every_harvest_condition = { limit = { <triggers> } #optional <effects> } | country, state, state_region, strategic_region | harvest_condition |
| every_in_global_list | Iterate through all items in global list. | every_in_global_list = { list = name or variable = name limit = { <triggers> } (optional) <effects> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list | none |  |
| every_in_hierarchy | Any country in current hierarchy, including current | every_in_hierarchy = { limit = { <triggers> } #optional <effects> } | country | country |
| every_in_list | Iterate through all items in list. | every_in_list = { list = name or variable = name limit = { <triggers> } (optional) <effects> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list | none |  |
| every_in_local_list | Iterate through all items in local list. | every_in_local_list = { list = name or variable = name limit = { <triggers> } (optional) <effects> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list | none |  |
| every_influenced_interest_group | Iterate through all interest groups influenced by a political movement | every_influenced_interest_group = { limit = { <triggers> } #optional <effects> } | political_movement | interest_group |
| every_interest_group | Iterate through all interest groups in a country | every_interest_group = { limit = { <triggers> } #optional <effects> } | country | interest_group |
| every_key_in_global_variable_map | Iterate through all keys in a global variable map. | every_key_in_global_variable_map = { variable = name of the map limit = { <triggers> } <effects> } | none |  |
| every_key_in_local_variable_map | Iterate through all keys in a local variable map. | every_key_in_local_variable_map = { variable = name of the map limit = { <triggers> } <effects> } | none |  |
| every_key_in_variable_map | Iterate through all keys in a variable map. | every_key_in_variable_map = { variable = name of the map limit = { <triggers> } <effects> } | none |  |
| every_law | Iterate through all laws in a country | every_law = { limit = { <triggers> } #optional <effects> } | country | law |
| every_lobby_member | Iterate through all interest group members of a lobby | every_lobby_member = { limit = { <triggers> } #optional <effects> } | political_lobby | interest_group |
| every_market | Iterate through all markets globally | every_market = { limit = { <triggers> } #optional <effects> } | none | market |
| every_market_goods | Iterate through all active (market) goods in a market | every_market_goods = { limit = { <triggers> } #optional <effects> } | market | market_goods |
| every_member | Iterate through all interest group members of a party | every_member = { limit = { <triggers> } #optional <effects> } | party | interest_group |
| every_military_formation | Iterate through all military formations currently present at input scope | every_military_formation = { limit = { <triggers> } #optional <effects> } | country, front, hq | military_formation |
| every_neighbouring_state | Iterate through all states neighbouring current scope Note British spelling | every_neighbouring_state = { limit = { <triggers> } #optional <effects> } | country, state, state_region, strategic_region | state |
| every_overlord_or_above | Any country above current in hierarchy | every_overlord_or_above = { limit = { <triggers> } #optional <effects> } | country | country |
| every_owned_country | Iterate through all countries owned by the scoped company | every_owned_country = { limit = { <triggers> } #optional <effects> } | company | country |
| every_participant | Any of two participants of the diplomatic pact in a scope | every_participant = { limit = { <triggers> } #optional <effects> } | diplomatic_pact | country |
| every_political_lobby | Iterate through all political lobbies in a country or interest group | every_political_lobby = { limit = { <triggers> } #optional <effects> } | country, interest_group | political_lobby |
| every_political_movement | Iterate through all political movements in a country | every_political_movement = { limit = { <triggers> } #optional <effects> } | country | political_movement |
| every_possible_amendment_type | Iterate through amendment types that could be added to the scoped law | every_possible_amendment_type = { limit = { <triggers> } #optional <effects> } | law | amendment_type |
| every_potential_party | Iterate through all potential political parties in a country | every_potential_party = { limit = { <triggers> } #optional <effects> } | country | party |
| every_power_bloc | Iterate through all power blocs | every_power_bloc = { limit = { <triggers> } #optional <effects> } | none | power_bloc |
| every_power_bloc_member | Iterate through all members of the scoped power bloc including the leader | every_power_bloc_member = { limit = { <triggers> } #optional <effects> } | power_bloc | country |
| every_preferred_law | Iterate through all active and possible laws in an interest group's country, ordered by how much they prefer that law | every_preferred_law = { limit = { <triggers> } #optional <effects> } | interest_group | law |
| every_primary_culture | Primary cultures of the scoped country or country definition | every_primary_culture = { limit = { <triggers> } #optional <effects> } | country, country_definition | culture |
| every_province | Iterate through all Provinces in the scoped State | every_province = { limit = { <triggers> } #optional <effects> } | province | state |
| every_province_in_<georegion_short_name> | Iterate through all Provinces in the specified geographic region | every_province_in_<georegion_short_name> = { limit = { <triggers> } #optional <effects> } | none | province |
| every_rival_country | Any country that is being rivaled by the country in a scope | every_rival_country = { limit = { <triggers> } #optional <effects> } | country | country |
| every_rivaling_country | Any country that is rivaling the country in a scope | every_rivaling_country = { limit = { <triggers> } #optional <effects> } | country | country |
| every_scope_admiral | Iterate through all admirals in a: country, interest group, or military formation | every_scope_admiral = { limit = { <triggers> } #optional <effects> } | country, front, interest_group, military_formation | character |
| every_scope_ally | Iterate through all allies to a: country | every_scope_ally = { limit = { <triggers> } #optional <effects> } | country | country |
| every_scope_amendment | Iterate through amendments of the scoped law | every_scope_amendment = { limit = { <triggers> } #optional <effects> } | law | amendment |
| every_scope_army | Iterate through all armies currently present at input scope | every_scope_army = { limit = { <triggers> } #optional <effects> } | country, front, hq | military_formation |
| every_scope_article | Iterate through articles of the scoped treaty | every_scope_article = { limit = { <triggers> } #optional <effects> } | treaty | treaty_article |
| every_scope_article_option | Iterate through article_options of the scoped treaty or treaty_options | every_scope_article_option = { limit = { <triggers> } #optional <effects> } | treaty, treaty_options | treaty_article_options |
| every_scope_building | Iterate through all buildings in a: state, country | every_scope_building = { limit = { <triggers> } #optional <effects> } | country, state | building |
| every_scope_character | Iterate through all characters in a: country, interest group, or front | every_scope_character = { limit = { <triggers> } #optional <effects> } | country, front, interest_group, military_formation | character |
| every_scope_country | Iterate through all countries with a presence in the supported scope (currently: market, state_region, strategic region) | every_scope_country = { limit = { <triggers> } #optional <effects> } | market, state_region, strategic_region | country |
| every_scope_culture | Iterate through all cultures in the scope | every_scope_culture = { limit = { <triggers> } #optional <effects> } | country, state | culture |
| every_scope_diplomatic_pact | Any diplomatic pact of the country in a scope | every_scope_diplomatic_pact = { limit = { <triggers> } #optional <effects> } | country | diplomatic_pact |
| every_scope_fleet | Iterate through all fleets currently present at input scope | every_scope_fleet = { limit = { <triggers> } #optional <effects> } | country, hq | military_formation |
| every_scope_front | Iterate through all Fronts related to the scoped War | every_scope_front = { limit = { <triggers> } #optional <effects> } | war | front |
| every_scope_general | Iterate through all generals in a: country, interest group, front, or military formation | every_scope_general = { limit = { <triggers> } #optional <effects> } | country, front, interest_group, military_formation | character |
| every_scope_held_interest_marker | Iterate through all interest markers held by a country | every_scope_held_interest_marker = { limit = { <triggers> } #optional <effects> } | country | interest_marker |
| every_scope_homeland_state | Iterate through all states that are a homeland for the scoped culture, or a homeland of any primary culture of the scoped country | every_scope_homeland_state = { limit = { <triggers> } #optional <effects> } | country, culture | state |
| every_scope_initiator_ally | Iterate through all allies to an initiator in a: diplomatic play | every_scope_initiator_ally = { limit = { <triggers> } #optional <effects> } | diplomatic_play | country |
| every_scope_interest_marker | Iterate through all interest markers in a: country, state_region, strategic region | every_scope_interest_marker = { limit = { <triggers> } #optional <effects> } | country, state_region, strategic_region | interest_marker |
| every_scope_je_involved | Iterate through all involved in a journal entry | every_scope_je_involved = { limit = { <triggers> } #optional <effects> } | journal_entry | country |
| every_scope_play_involved | Iterate through all involved in a: diplomatic play | every_scope_play_involved = { limit = { <triggers> } #optional <effects> } | diplomatic_play | country |
| every_scope_politician | Iterate through all politicians in a: country or interest group | every_scope_politician = { limit = { <triggers> } #optional <effects> } | country, front, interest_group, military_formation | character |
| every_scope_pop | Iterate through all pops in a: country, state, interest group, culture | every_scope_pop = { limit = { <triggers> } #optional <effects> } | country, culture, interest_group, state | pop |
| every_scope_regional_hqs | Iterate through regional HQs of the scoped company | every_scope_regional_hqs = { limit = { <triggers> } #optional <effects> } | company | building |
| every_scope_ship | Iterate through all ships in a country or military formation | every_scope_ship = { limit = { <triggers> } #optional <effects> } | country, military_formation | ship |
| every_scope_state | Iterate through all states including provinces from a: country, state_region, theater, front, or strait | every_scope_state = { limit = { <triggers> } #optional <effects> } | country, front, state_region, strait, strategic_region, theater | state |
| every_scope_strait | Iterate through all straits with a land endpoint in the scoped state or country | every_scope_strait = { limit = { <triggers> } #optional <effects> } | country, state | strait |
| every_scope_target_ally | Iterate through all allies to a target in a: diplomatic play | every_scope_target_ally = { limit = { <triggers> } #optional <effects> } | diplomatic_play | country |
| every_scope_theater | Iterate through all theaters in a: country | every_scope_theater = { limit = { <triggers> } #optional <effects> } | country | theater |
| every_scope_treaty | Iterate through in force treaties binding the scoped country | every_scope_treaty = { limit = { <triggers> } #optional <effects> } | country | treaty |
| every_scope_violate_sovereignty_interested_parties | Iterate through all countries that would be interested if country in scope has their sovereignty violated | every_scope_violate_sovereignty_interested_parties = { limit = { <triggers> } #optional <effects> } | country | country |
| every_scope_violate_sovereignty_wars | Iterate through all relevant wars if target country had their sovereignty violated by scoped country | every_scope_violate_sovereignty_wars = { limit = { <triggers> } #optional <effects> } | country | war |
| every_scope_war | Iterate through all wars related to the scope | every_scope_war = { limit = { <triggers> } #optional <effects> } | country | war |
| every_sea_node_adjacent_state | Iterate through all states that share a sea node with a state | every_sea_node_adjacent_state = { limit = { <triggers> } #optional <effects> } | state | state |
| every_state | Iterate through all states globally | every_state = { limit = { <triggers> } #optional <effects> } | none | state |
| every_state_in_<georegion_short_name> | Iterate through all states in the specified geographic region | every_state_in_<georegion_short_name> = { limit = { <triggers> } #optional <effects> } | none | state |
| every_state_region | Iterate through all state regions | every_state_region = { limit = { <triggers> } #optional <effects> } | none | state_region |
| every_state_region_<georegion_short_name> | Iterate through all state regions in the specified geographic region | every_state_region_<georegion_short_name> = { limit = { <triggers> } #optional <effects> } | none | state_region |
| every_strategic_objective | Iterate through all Strategic Objective states from the scoped Country | every_strategic_objective = { limit = { <triggers> } #optional <effects> } | country | state |
| every_strategic_region | Iterate through all strategic regions globally | every_strategic_region = { limit = { <triggers> } #optional <effects> } | none | strategic_region |
| every_strategic_region_in_<georegion_short_name> | Iterate through all strategic regions in the specified geographic region | every_strategic_region_in_<georegion_short_name> = { limit = { <triggers> } #optional <effects> } | none | strategic_region |
| every_subject_of_subject | Any country below direct subjects in hierarchy | every_subject_of_subject = { limit = { <triggers> } #optional <effects> } | country | country |
| every_subject_or_below | Any country below current in hierarchy | every_subject_or_below = { limit = { <triggers> } #optional <effects> } | country | country |
| every_supporting_character | Iterate through all characters that support the scoped political movement | every_supporting_character = { limit = { <triggers> } #optional <effects> } | political_movement | character |
| every_treaty | Iterate through treaties (both in force and drafts) | every_treaty = { limit = { <triggers> } #optional <effects> } | none | treaty |
| every_valid_mass_migration_culture | Lists for cultures in the scoped country that are valid for mass migration | every_valid_mass_migration_culture = { limit = { <triggers> } #optional <effects> } | country | culture |
| every_war_participant | Iterate through all participants in a war | every_war_participant = { limit = { <triggers> } #optional <effects> } | war | country |
| ordered_active_law | Iterate through all active laws in a country | ordered_active_law = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | law |
| ordered_active_party | Iterate through all active political parties in a country | ordered_active_party = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | party |
| ordered_character | Iterate through all characters globally | ordered_character = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | character |
| ordered_character_in_exile_pool | Iterate through characters in the exile pool | ordered_character_in_exile_pool = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | character |
| ordered_character_in_void | Iterate through characters in the void | ordered_character_in_void = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | character |
| ordered_character_role | Iterate through all roles of the scoped character | ordered_character_role = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | character | character_role |
| ordered_civil_war | Iterate through all civil wars related to the scoped country | ordered_civil_war = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | civil_war |
| ordered_cobelligerent_in_diplo_play | Iterate through all co-belligerents of scope country in all diplomatic plays (includes wars) | ordered_cobelligerent_in_diplo_play = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | country |
| ordered_cobelligerent_in_war | Iterate through all co-belligerents of scope country in all wars | ordered_cobelligerent_in_war = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | country |
| ordered_combat_unit | Iterate through all combat units of input scope | ordered_combat_unit = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | battle, building, front, hq, military_formation | new_combat_unit |
| ordered_company | Iterate through all companies in a country | ordered_company = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | company |
| ordered_country | Iterate through all countries globally | ordered_country = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | country |
| ordered_country_in_<georegion_short_name> | Iterate through all countries in the specified geographic region | ordered_country_in_<georegion_short_name> = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | country |
| ordered_country_strategic_region | Iterate through all strategic regions containing states owned by the scoped country | ordered_country_strategic_region = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | strategic_region |
| ordered_decentralized_country | Iterate through all countries that are decentralized | ordered_decentralized_country = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | country |
| ordered_diplomatic_catalyst | Iterate through all diplomatic catalysts in the recent memory of a country | ordered_diplomatic_catalyst = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | diplomatic_catalyst |
| ordered_diplomatic_play | Iterate through all diplomatic plays globally | ordered_diplomatic_play = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | diplomatic_play |
| ordered_diplomatically_relevant_country | Iterate through all diplomatically relevant countries of a country scope | ordered_diplomatically_relevant_country = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | country |
| ordered_direct_subject | Any country directly below current in hierarchy | ordered_direct_subject = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | country |
| ordered_enemy_in_diplo_play | Iterate through all enemies of scope country in all diplomatic plays (includes wars) | ordered_enemy_in_diplo_play = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | country |
| ordered_enemy_in_war | Iterate through all enemies of scope country in all wars | ordered_enemy_in_war = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | country |
| ordered_harvest_condition | Iterate through all harvest conditions affecting a state, state region, strategic region, or country | ordered_harvest_condition = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, state, state_region, strategic_region | harvest_condition |
| ordered_in_global_list | Iterate through all items in global list. list = name or variable = name | ordered_in_global_list = { list = name or variable = name limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; minimum value of ordering comparison to consider max = script_value #optional, default inf; maximum value of ordering comparison to consider check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list | none |  |
| ordered_in_hierarchy | Any country in current hierarchy, including current | ordered_in_hierarchy = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | country |
| ordered_in_list | Iterate through all items in list. | ordered_in_list = { list = name or variable = name limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; minimum value of ordering comparison to consider max = script_value #optional, default inf; maximum value of ordering comparison to consider check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list | none |  |
| ordered_in_local_list | Iterate through all items in local list. list = name or variable = name | ordered_in_local_list = { list = name or variable = name limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; minimum value of ordering comparison to consider max = script_value #optional, default inf; maximum value of ordering comparison to consider check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list | none |  |
| ordered_influenced_interest_group | Iterate through all interest groups influenced by a political movement | ordered_influenced_interest_group = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | political_movement | interest_group |
| ordered_interest_group | Iterate through all interest groups in a country | ordered_interest_group = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | interest_group |
| ordered_key_in_global_variable_map | Iterate through all keys in a global variable map. | ordered_key_in_global_variable_map = { variable = name of the map limit = { <triggers> } order_by = script_value position = int min = int max = script_value check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max <effects> } | none |  |
| ordered_key_in_local_variable_map | Iterate through all keys in a local variable map. | ordered_key_in_local_variable_map = { variable = name of the map limit = { <triggers> } order_by = script_value position = int min = int max = script_value check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max <effects> } | none |  |
| ordered_key_in_variable_map | Iterate through all keys in a variable map. | ordered_key_in_variable_map = { variable = name of the map limit = { <triggers> } order_by = script_value position = int min = int max = script_value check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max <effects> } | none |  |
| ordered_law | Iterate through all laws in a country | ordered_law = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | law |
| ordered_lobby_member | Iterate through all interest group members of a lobby | ordered_lobby_member = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | political_lobby | interest_group |
| ordered_market | Iterate through all markets globally | ordered_market = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | market |
| ordered_market_goods | Iterate through all active (market) goods in a market | ordered_market_goods = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | market | market_goods |
| ordered_member | Iterate through all interest group members of a party | ordered_member = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | party | interest_group |
| ordered_military_formation | Iterate through all military formations currently present at input scope | ordered_military_formation = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, front, hq | military_formation |
| ordered_neighbouring_state | Iterate through all states neighbouring a state region | ordered_neighbouring_state = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, state, state_region, strategic_region | state |
| ordered_overlord_or_above | Any country above current in hierarchy | ordered_overlord_or_above = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | country |
| ordered_owned_country | Iterate through all countries owned by the scoped company | ordered_owned_country = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | company | country |
| ordered_participant | Any of two participants of the diplomatic pact in a scope | ordered_participant = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | diplomatic_pact | country |
| ordered_political_lobby | Iterate through all political lobbies in a country or interest group | ordered_political_lobby = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, interest_group | political_lobby |
| ordered_political_movement | Iterate through all political movements in a country | ordered_political_movement = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | political_movement |
| ordered_possible_amendment_type | Iterate through amendment types that could be added to the scoped law | ordered_possible_amendment_type = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | law | amendment_type |
| ordered_potential_party | Iterate through all potential political parties in a country | ordered_potential_party = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | party |
| ordered_power_bloc | Iterate through all power blocs | ordered_power_bloc = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | power_bloc |
| ordered_power_bloc_member | Iterate through all members of the scoped power bloc including the leader | ordered_power_bloc_member = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | power_bloc | country |
| ordered_preferred_law | Iterate through all active and possible laws in an interest group's country, ordered by how much they prefer that law | ordered_preferred_law = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | interest_group | law |
| ordered_primary_culture | Primary cultures of the scoped country or country definition | ordered_primary_culture = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, country_definition | culture |
| ordered_province | Iterate through all Provinces in the scoped State | ordered_province = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | state | province |
| ordered_province_in_<georegion_short_name> | Iterate through all Provinces in the specified geographic region | ordered_province_in_<georegion_short_name> = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | province |
| ordered_rival_country | Any country that is being rivaled by the country in a scope | ordered_rival_country = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | country |
| ordered_rivaling_country | Any country that is rivaling the country in a scope | ordered_rivaling_country = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | country |
| ordered_scope_admiral | Iterate through all admirals in a: country, interest group, or military formation | ordered_scope_admiral = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, front, interest_group, military_formation | character |
| ordered_scope_ally | Iterate through all allies to a: country | ordered_scope_ally = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | country |
| ordered_scope_amendment | Iterate through amendments of the scoped law | ordered_scope_amendment = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | law | amendment |
| ordered_scope_army | Iterate through all armies currently present at input scope | ordered_scope_army = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, front, hq | military_formation |
| ordered_scope_article | Iterate through articles of the scoped treaty | ordered_scope_article = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | treaty | treaty_article |
| ordered_scope_article_option | Iterate through article_options of the scoped treaty or treaty_options | ordered_scope_article_option = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | treaty, treaty_options | treaty_article_options |
| ordered_scope_building | Iterate through all buildings in a: state, country | ordered_scope_building = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, state | building |
| ordered_scope_character | Iterate through all characters in a: country, interest group, or front | ordered_scope_character = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, front, interest_group, military_formation | character |
| ordered_scope_country | Iterate through all countries with a presence in the supported scope (currently: market, state_region, strategic region) | ordered_scope_country = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | market, state_region, strategic_region | country |
| ordered_scope_culture | Iterate through all cultures in the scope | ordered_scope_culture = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, state | culture |
| ordered_scope_diplomatic_pact | Any diplomatic pact of the country in a scope | ordered_scope_diplomatic_pact = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | diplomatic_pact |
| ordered_scope_fleet | Iterate through all fleets currently present at input scope | ordered_scope_fleet = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, hq | military_formation |
| ordered_scope_front | Iterate through all Fronts related to the scoped War | ordered_scope_front = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | war | front |
| ordered_scope_general | Iterate through all generals in a: country, interest group, front, or military formation | ordered_scope_general = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, front, interest_group, military_formation | character |
| ordered_scope_held_interest_marker | Iterate through all interest markers held by a country | ordered_scope_held_interest_marker = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | interest_marker |
| ordered_scope_homeland_state | Iterate through all states that are a homeland for the scoped culture, or a homeland of any primary culture of the scoped country | ordered_scope_homeland_state = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, culture | state |
| ordered_scope_initiator_ally | Iterate through all allies to an initiator in a: diplomatic play | ordered_scope_initiator_ally = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | diplomatic_play | country |
| ordered_scope_interest_marker | Iterate through all interest markers in a: country, state_region, strategic region | ordered_scope_interest_marker = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, state_region, strategic_region | interest_marker |
| ordered_scope_je_involved | Iterate through all involved in a journal entry | ordered_scope_je_involved = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | journal_entry | country |
| ordered_scope_play_involved | Iterate through all involved in a: diplomatic play | ordered_scope_play_involved = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | diplomatic_play | country |
| ordered_scope_politician | Iterate through all politicians in a: country or interest group | ordered_scope_politician = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, front, interest_group, military_formation | character |
| ordered_scope_pop | Iterate through all pops in a: country, state, interest group, culture | ordered_scope_pop = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, culture, interest_group, state | pop |
| ordered_scope_regional_hqs | Iterate through regional HQs of the scoped company | ordered_scope_regional_hqs = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | company | building |
| ordered_scope_ship | Iterate through all ships in a country or military formation | ordered_scope_ship = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, military_formation | ship |
| ordered_scope_state | Iterate through all states including provinces from a: country, state_region, theater, front, or strait | ordered_scope_state = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, front, state_region, strait, strategic_region, theater | state |
| ordered_scope_strait | Iterate through all straits with a land endpoint in the scoped state or country | ordered_scope_strait = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, state | strait |
| ordered_scope_target_ally | Iterate through all allies to a target in a: diplomatic play | ordered_scope_target_ally = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | diplomatic_play | country |
| ordered_scope_theater | Iterate through all theaters in a: country | ordered_scope_theater = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | theater |
| ordered_scope_treaty | Iterate through in force treaties binding the scoped country | ordered_scope_treaty = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | treaty |
| ordered_scope_violate_sovereignty_interested_parties | Iterate through all countries that would be interested if country in scope has their sovereignty violated | ordered_scope_violate_sovereignty_interested_parties = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | country |
| ordered_scope_violate_sovereignty_wars | Iterate through all relevant wars if target country had their sovereignty violated by scoped country | ordered_scope_violate_sovereignty_wars = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | war |
| ordered_scope_war | Iterate through all wars related to the scope | ordered_scope_war = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | war |
| ordered_sea_node_adjacent_state | Iterate through all states that share a sea node with a state | ordered_sea_node_adjacent_state = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | state | state |
| ordered_state | Iterate through all states globally | ordered_state = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | state |
| ordered_state_in_<georegion_short_name> | Iterate through all states in the specified geographic region | ordered_state_in_<georegion_short_name> = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | state |
| ordered_state_region | Iterate through all state regions | ordered_state_region = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | state_region |
| ordered_state_region_in_<georegion_short_name> | Iterate through all state regions in the specified geographic region | ordered_state_region_in_<georegion_short_name> = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | state_region |
| ordered_strategic_objective | Iterate through all Strategic Objective states from the scoped Country | ordered_strategic_objective = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | state |
| ordered_strategic_region | Iterate through all strategic regions globally | ordered_strategic_region = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | strategic_region |
| ordered_strategic_region_in_<georegion_short_name> | Iterate through all strategic regions in the specified geographic region | ordered_state_region_in_<georegion_short_name> = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | strategic_region |
| ordered_subject_of_subject | Any country below direct subjects in hierarchy | ordered_subject_of_subject = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | country |
| ordered_subject_or_below | Any country below current in hierarchy | ordered_subject_or_below = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | country |
| ordered_supporting_character | Iterate through all characters that support the scoped political movement | ordered_supporting_character = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | political_movement | character |
| ordered_treaty | Iterate through treaties (both in force and drafts) | ordered_treaty = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | treaty |
| ordered_valid_mass_migration_culture | Lists for cultures in the scoped country that are valid for mass migration | ordered_valid_mass_migration_culture = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | culture |
| ordered_war_participant | Iterate through all participants in a war | ordered_war_participant = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | war | country |
| random_active_law | Iterate through all active laws in a country | random_active_law = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | law |
| random_active_party | Iterate through all active political parties in a country | random_active_party = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | party |
| random_character | Iterate through all characters globally | random_character = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | character |
| random_character_in_exile_pool | Iterate through characters in the exile pool | random_character_in_exile_pool = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | character |
| random_character_in_void | Iterate through characters in the void | random_character_in_void = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | character |
| random_character_role | Iterate through all roles of the scoped character | random_character_role = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | character | character_role |
| random_civil_war | Iterate through all civil wars related to the scoped country | random_civil_war = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | civil_war |
| random_cobelligerent_in_diplo_play | Iterate through all co-belligerents of scope country in all diplomatic plays (includes wars) | random_cobelligerent_in_diplo_play = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | country |
| random_cobelligerent_in_war | Iterate through all co-belligerents of scope country in all wars | random_cobelligerent_in_war = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | country |
| random_combat_unit | Iterate through all combat units of input scope | random_combat_unit = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | battle, building, front, hq, military_formation | new_combat_unit |
| random_company | Iterate through all companies in a country | random_company = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | company |
| random_country | Iterate through all countries globally | random_country = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | country |
| random_country_in_<georegion_short_name> | Iterate through all countries in the specified geographic region | random_country_in_<georegion_short_name> = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | country |
| random_country_strategic_region | Iterate through all strategic regions containing states owned by the scoped country | random_country_strategic_region = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | strategic_region |
| random_decentralized_country | Iterate through all countries that are decentralized | random_decentralized_country = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | country |
| random_diplomatic_catalyst | Iterate through all diplomatic catalysts in the recent memory of a country | random_diplomatic_catalyst = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | diplomatic_catalyst |
| random_diplomatic_play | Iterate through all diplomatic plays globally | random_diplomatic_play = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | diplomatic_play |
| random_diplomatically_relevant_country | Iterate through all diplomatically relevant countries of a country scope | random_diplomatically_relevant_country = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | country |
| random_direct_subject | Any country directly below current in hierarchy | random_direct_subject = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | country |
| random_enemy_in_diplo_play | Iterate through all enemies of scope country in all diplomatic plays (includes wars) | random_enemy_in_diplo_play = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | country |
| random_enemy_in_war | Iterate through all enemies of scope country in all wars | random_enemy_in_war = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | country |
| random_harvest_condition | Iterate through all harvest conditions affecting a state, state region, strategic region, or country | random_harvest_condition = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, state, state_region, strategic_region | harvest_condition |
| random_in_global_list | Iterate through all items in global list. | random_in_global_list = { list = name or variable = name limit = { <triggers> } (optional) weight = { mtth } (optional) <effects> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list | none |  |
| random_in_hierarchy | Any country in current hierarchy, including current | random_in_hierarchy = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | country |
| random_in_list | Iterate through all items in list. | random_in_list = { list = name or variable = name limit = { <triggers> } (optional) weight = { mtth } (optional) <effects> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list | none |  |
| random_in_local_list | Iterate through all items in local list. | random_in_local_list = { list = name or variable = name limit = { <triggers> } (optional) weight = { mtth } (optional) <effects> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list | none |  |
| random_influenced_interest_group | Iterate through all interest groups influenced by a political movement | random_influenced_interest_group = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | political_movement | interest_group |
| random_interest_group | Iterate through all interest groups in a country | random_interest_group = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | interest_group |
| random_key_in_global_variable_map | Iterate through all keys in a global variable map. | random_key_in_global_variable_map = { variable = name of the map limit = { <triggers> } weight = { mtth } (optional) <effects> } | none |  |
| random_key_in_local_variable_map | Iterate through all keys in a local variable map. | random_key_in_local_variable_map = { variable = name of the map limit = { <triggers> } weight = { mtth } (optional) <effects> } | none |  |
| random_key_in_variable_map | Iterate through all keys in a variable map. | random_key_in_variable_map = { variable = name of the map limit = { <triggers> } weight = { mtth } (optional) <effects> } | none |  |
| random_law | Iterate through all laws in a country | random_law = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | law |
| random_lobby_member | Iterate through all interest group members of a lobby | random_lobby_member = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | political_lobby | interest_group |
| random_market | Iterate through all markets globally | random_market = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | market |
| random_market_goods | Iterate through all active (market) goods in a market | random_market_goods = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | market | market_goods |
| random_member | Iterate through all interest group members of a party | random_member = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | party | interest_group |
| random_military_formation | Iterate through all military formations currently present at input scope | random_military_formation = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, front, hq | military_formation |
| random_neighbouring_state | Iterate through all states neighbouring a state region | random_neighbouring_state = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, state, state_region, strategic_region | state |
| random_overlord_or_above | Any country above current in hierarchy | random_overlord_or_above = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | country |
| random_owned_country | Iterate through all countries owned by the scoped company | random_owned_country = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | company | country |
| random_participant | Any of two participants of the diplomatic pact in a scope | random_participant = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | diplomatic_pact | country |
| random_political_lobby | Iterate through all political lobbies in a country or interest group | random_political_lobby = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, interest_group | political_lobby |
| random_political_movement | Iterate through all political movements in a country | random_political_movement = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | political_movement |
| random_possible_amendment_type | Iterate through amendment types that could be added to the scoped law | random_possible_amendment_type = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | law | amendment_type |
| random_potential_party | Iterate through all potential political parties in a country | random_potential_party = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | party |
| random_power_bloc | Iterate through all power blocs | random_power_bloc = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | power_bloc |
| random_power_bloc_member | Iterate through all members of the scoped power bloc including the leader | random_power_bloc_member = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | power_bloc | country |
| random_preferred_law | Iterate through all active and possible laws in an interest group's country, ordered by how much they prefer that law | random_preferred_law = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | interest_group | law |
| random_primary_culture | Primary cultures of the scoped country or country definition | random_primary_culture = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, country_definition | culture |
| random_province | Iterate through all Provinces in the scoped State | random_province = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | state | province |
| random_province_in_<georegion_short_name> | Iterate through all Provinces in the specified geographic region | random_province_in_<georegion_short_name>' = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | province |
| random_rival_country | Any country that is being rivaled by the country in a scope | random_rival_country = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | country |
| random_rivaling_country | Any country that is rivaling the country in a scope | random_rivaling_country = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | country |
| random_scope_admiral | Iterate through all admirals in a: country, interest group, or military formation | random_scope_admiral = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, front, interest_group, military_formation | character |
| random_scope_ally | Iterate through all allies to a: country | random_scope_ally = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | country |
| random_scope_amendment | Iterate through amendments of the scoped law | random_scope_amendment = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | law | amendment |
| random_scope_army | Iterate through all armies currently present at input scope | random_scope_army = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, front, hq | military_formation |
| random_scope_article | Iterate through articles of the scoped treaty | random_scope_article = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | treaty | treaty_article |
| random_scope_article_option | Iterate through article_options of the scoped treaty or treaty_options | random_scope_article_option = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | treaty, treaty_options | treaty_article_options |
| random_scope_building | Iterate through all buildings in a: state, country | random_scope_building = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, state | building |
| random_scope_character | Iterate through all characters in a: country, interest group, or front | random_scope_character = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, front, interest_group, military_formation | character |
| random_scope_country | Iterate through all countries with a presence in the supported scope (currently: market, state_region, strategic region) | random_scope_country = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | market, state_region, strategic_region | country |
| random_scope_culture | Iterate through all cultures in the scope | random_scope_culture = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, state | culture |
| random_scope_diplomatic_pact | Any diplomatic pact of the country in a scope | random_scope_diplomatic_pact = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | diplomatic_pact |
| random_scope_fleet | Iterate through all fleets currently present at input scope | random_scope_fleet = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, hq | military_formation |
| random_scope_front | Iterate through all Fronts related to the scoped War | random_scope_front = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | war | front |
| random_scope_general | Iterate through all generals in a: country, interest group, front, or military formation | random_scope_general = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, front, interest_group, military_formation | character |
| random_scope_held_interest_marker | Iterate through all interest markers held by a country | random_scope_held_interest_marker = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | interest_marker |
| random_scope_homeland_state | Iterate through all states that are a homeland for the scoped culture, or a homeland of any primary culture of the scoped country | random_scope_homeland_state = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, culture | state |
| random_scope_initiator_ally | Iterate through all allies to an initiator in a: diplomatic play | random_scope_initiator_ally = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | diplomatic_play | country |
| random_scope_interest_marker | Iterate through all interest markers in a: country, state_region, strategic region | random_scope_interest_marker = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, state_region, strategic_region | interest_marker |
| random_scope_je_involved | Iterate through all involved in a journal entry | random_scope_je_involved = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | journal_entry | country |
| random_scope_play_involved | Iterate through all involved in a: diplomatic play | random_scope_play_involved = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | diplomatic_play | country |
| random_scope_politician | Iterate through all politicians in a: country or interest group | random_scope_politician = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, front, interest_group, military_formation | character |
| random_scope_pop | Iterate through all pops in a: country, state, interest group, culture | random_scope_pop = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, culture, interest_group, state | pop |
| random_scope_regional_hqs | Iterate through regional HQs of the scoped company | random_scope_regional_hqs = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | company | building |
| random_scope_ship | Iterate through all ships in a country or military formation | random_scope_ship = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, military_formation | ship |
| random_scope_state | Iterate through all states including provinces from a: country, state_region, theater, front, or strait | random_scope_state = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, front, state_region, strait, strategic_region, theater | state |
| random_scope_strait | Iterate through all straits with a land endpoint in the scoped state or country | random_scope_strait = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, state | strait |
| random_scope_target_ally | Iterate through all allies to a target in a: diplomatic play | random_scope_target_ally = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | diplomatic_play | country |
| random_scope_theater | Iterate through all theaters in a: country | random_scope_theater = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | theater |
| random_scope_treaty | Iterate through in force treaties binding the scoped country | random_scope_treaty = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | treaty |
| random_scope_violate_sovereignty_interested_parties | Iterate through all countries that would be interested if country in scope has their sovereignty violated | random_scope_violate_sovereignty_interested_parties = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | country |
| random_scope_violate_sovereignty_wars | Iterate through all relevant wars if target country had their sovereignty violated by scoped country | random_scope_violate_sovereignty_wars = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | war |
| random_scope_war | Iterate through all wars related to the scope | random_scope_war = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | war |
| random_sea_node_adjacent_state | Iterate through all states that share a sea node with a state | random_sea_node_adjacent_state = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | state | state |
| random_state | Iterate through all states globally | random_state = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | state |
| random_state_in_<georegion_short_name> | Iterate through all states in the specified geographic region | random_state_in_<georegion_short_name> = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | state |
| random_state_region | Iterate through all state regions | random_state_region = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | state_region |
| random_state_region_in_<georegion_short_name> | Iterate through all state regions in the specified geographic region | random_state_region_in_<georegion_short_name> = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | state_region |
| random_strategic_objective | Iterate through all Strategic Objective states from the scoped Country | random_strategic_objective = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | state |
| random_strategic_region | Iterate through all strategic regions globally | random_strategic_region = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | strategic_region |
| random_strategic_region_in_<georegion_short_name> | Iterate through all strategic regions in the specified geographic region | random_strategic_region_in_<georegion_short_name> = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | strategic_region |
| random_subject_or_below | Any country below current in hierarchy | random_subject_or_below = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | country |
| random_supporting_character | Iterate through all characters that support the scoped political movement | random_supporting_character = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | political_movement | character |
| random_treaty | Iterate through treaties (both in force and drafts) | random_treaty = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | treaty |
| random_valid_mass_migration_culture | Lists for cultures in the scoped country that are valid for mass migration | random_valid_mass_migration_culture = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | culture |
| random_war_participant | Iterate through all participants in a war | random_war_participant = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | war | country |

#### Multiple random scopes

Often it is useful to return multiple random or semi-random scopes. This can be implemented in a few different ways. The most straightforward is multiple uses of a `random_` iterator. To ensure that the same scope is not returned twice, set a variable on each scope as part of its effects and check that the variable has not been set in order to return the next scope.

```
random_country = {
    limit = {
        NOT = { has_variable = blocker_var }
        <other limit triggers>
    }
    set_variable = blocker_var
    <effects>
}
<repeat above as desired>
```

This style can be made more succinct by using a [scripted effect](Macro.md) or a [while](Effect.md) loop, so that the actual effect only needs to be defined once.

An alternative approach uses a single `ordered_` iterator with a semi-random ordering. This ensures each returned scope is unique without having to check for variables, as well as keeping the amount of script used to a minimum. It makes use of the [script value](Script value.md) function `modulo` to give a semi-random ordering.

```
ordered_country = {
    limit = { } # if desired
    order_by = {
        value = gdp
        modulo = { 1 10 }
    }
    max = 10
    <effects>
}
```

This example returns 10 countries which are ordered by a randomized modulo of GDP. The `modulo` range can be set to any values desired and can also used `fixed_range` or `integer_range` in order to make use of other scripted values, and other values can be used as the basis, such as total population, prestige, or any typically unique value set.

### Scripted lists

Scripted lists are customized reusable iterators. These are defined in `/common/scripted_lists`.

These have the following format:

```
<list_name> = { # This is used for the custom iterator
    base = # one of the provided lists (country, scope_state, interest_group, etc)
    conditions = {
        <triggers> # The filters for the custom list
    }
}
```

Example from the base game:

```
# Defined in /common/scripted_lists/victoria_scripted_lists.txt
princely_state = {
    base = country
    conditions = {
        is_princely_state = yes
    }
}

# Usage in je_federation_of_india
	complete = {
		custom_tooltip = {
			text = all_princely_states_have_acceded_to_the_federation_tt
			NOT = {
				any_princely_state = {
					exists = THIS
				}
			}
		}
	}
```

### Geographic regions

Main article:
Geographic Region
Geographic regions provide script-defined iterators using the geographic region short_key. A geographic region can be used to iterate through any included regions in a more performance friendly manner.

The supported iterators are as follows:

- `{any|every|ordered|random}_country_in_<geographic_region_short_key>`
- `{any|every|ordered|random}_province_in_<geographic_region_short_key>`
- `{any|every|ordered|random}_state_in_<geographic_region_short_key>`
- `{any|every|ordered|random}_state_region_in_<geographic_region_short_key>`
- `{any|every|ordered|random}_strategic_region_in_<geographic_region_short_key>`

Example, from `je_springtime_of_the_peoples`:

```
 	possible = {
 		any_country_in_europe = {
 			has_technology_researched = egalitarianism
         }
 		custom_tooltip = {
 			text = peoples_springtime_underway_tt
 			has_global_variable = peoples_springtime_happening
 		}
 	}
```

*This method is highly recommended by the game developers as the unbounded _country and _state iterators are inherently expensive.*

## Scope types

|  | Please help improve this article or section by [expanding it](https://vic3.paradoxwikis.com/index.php?title=Scope&action=edit) with: definitions and examples. |
|---|---|

- battle
- battle_side
- boolean
- building
- building_type
- character
- civil_war
- color
- combat_unit_type
- company
- company_type
- country
- country_definition
- culture
- decree
- diplomatic_catalyst
- diplomatic_catalyst_type
- diplomatic_catalyst
- diplomatic_pact
- diplomatic_play
- diplomatic_play_type
- diplomatic_relations
- flag
- front
- goods
- harvest_condition_area
- harvest_condition_type
- hq
- ideology
- institution
- institution_type
- interest_group
- interest_group_trait
- interest_group_type
- interest_marker
- invasion
- journal_entry
- law
- law_type
- market
- market_goods
- military_formation
- mobilization_option
- new_combat_unit
- none
- party
- political_lobby
- political_lobby_type
- political_movement
- political_movement_type
- pop
- pop_type
- power_bloc
- power_bloc_identity
- power_bloc_principle
- power_bloc_principle_group
- province
- religion
- shipping_lanes
- state
- state_goods
- state_region
- strategic_region
- technology
- theater
- treaty
- treaty_article
- treaty_article
- treaty_article_options
- treaty_options
- value
- war

## References

Modding
Return to top
| Documentation | [Defines](Defines.md) • [Effects](Effect.md) • [Event targets](Event target.md) • Scopes • [Triggers](Trigger.md) [Macros](Macro.md) • [Modifier types](Modifier types.md) • [On actions](https://vic3.paradoxwikis.com/On_actions) • [Script value](Script value.md) • [Variables](Variable.md) |
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
