---
title: Event target
source: https://vic3.paradoxwikis.com/Event_target
pageid: 3452
categories: [1.13, Modding]
fetched: 2026-10-27
---
This article has been verified for the current [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) (1.13) of the game.

This page discusses the game script element called "event targets". For pop-up narrative content events, see
Event modding
; for lists and details of events that exist in Victoria 3, see
Events
.
See also:
Effect
,
Trigger
**Event targets** are object, [scope](Scope.md), or value references used in Victoria 3's game script. Most event targets can be used as target of an [effect](Effect.md) or [trigger](Trigger.md) when it refers to an appropriate scope, object, or value. Similarly, event targets can be used as scopes or the left side of a value comparison.

Event targets that represent scopes can generally be used in dot chains as for example: `p:xF98DA3.state.owner.capital` which looks at the specified province, then chains to that province's state, that state's owning country, and finally to that country's capital state.

## Data event targets

These event targets require additional input, such as a scripted type or specified scope. This generally takes the form of `event_target:data`; some use the format `event_target(data)`, this type must be enclosed in quotation marks, including any dot scoped elements, e.g. `"scope:power_bloc.power_bloc_leader.market.market_number_goods_shortages_with(scope:with_country)"`.

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

## Value event targets

These event targets return a numerical or boolean value. This allows them to be used in comparisons or script values.

| Event target | Description | From scope |
|---|---|---|
| ai_army_comparison | Scope to comparative army strength between two countries (example: value = ai_army_comparison:root) | country |
| ai_colonization_value | Scope to target country AI desire to colonize a strategic region (example: value = ai_colonization_value:root) | strategic_region |
| ai_gdp_comparison | Scope to comparative GDP between two countries (example: value = ai_army_comparison:root) | country |
| ai_ideological_opinion | Scope to AI ideological opinion of scope country on target country (example: value = ai_ideological_opinion:root) | country |
| ai_navy_comparison | Scope to comparative navy strength between two countries (example: value = ai_navy_comparison:root) | country |
| ai_state_value | Scope to target country AI desire to own scope state (example: value = ai_state_value:root) | state |
| ai_subject_value | Scope to AI desire of target country to have scope country as a subject (example: value = ai_subject_value:root) | country |
| ai_transit_rights_value | Scope to AI desire of to have transit rights through target country (example: value = ai_transit_rights_value:root) | country |
| ai_treaty_export_value | Scope to target country AI desire to export scoped market good (example: value = ai_market_export_value:root) | market_goods |
| ai_treaty_fairness | Scope to AI evaluation of how fair (to both sides) it considers existing treaty articles with the target country to be (example: value = ai_treaty_fairness_score:root) | country |
| ai_treaty_import_value | Scope to target country AI desire to import scoped market good through treaties (example: value = ai_market_import_value:root) | market_goods |
| ai_treaty_port_value | Scope to target country AI desire to have a treaty port in scope state (example: value = ai_treaty_port_value:root) | state |
| ai_treaty_trade_value | Scope to target country AI desire to import and export scoped market good (example: value = ai_market_trade_value:root) | market_goods |
| ai_treaty_value | Scope to AI evaluation of how favorable to itself it considers existing treaty articles with the target country to be (example: value = ai_treaty_value:root) | country |
| army_size | Number of battalions of scope country, excluding currently raised conscripts. | country |
| army_size_including_conscripts | Number of battalions of scope country, including currently raised conscripts. | country |
| army_size_including_raised_conscripts | Number of battalions of scope country, including currently raised conscripts but excluding unraised conscripts. | country |
| array_define | Reference the value of a numeric value in an array define: array_define:Namespace\|Name\|Index. Index is 0-based. | none |
| average_defense | Returns the average defense of units on Front on the same side as Country | front |
| average_expected_sol | Get the average expected Standard of Living of the scope | country, state |
| average_offense | Returns the average offense of units on Front on the same side as Country | front |
| average_progressiveness | Get the average progressiveness of the scoped character or interest group | character, interest_group |
| average_sol | Get the average Standard of Living of the scope | country, state |
| base_price | Get the base price of the scoped good | goods |
| binding_period | Get the original binding period in days when the treaty was signed for the scoped treaty | treaty, treaty_options |
| building_levels | Get the total number of non-subsistence building levels of the scoped country | country |
| cached_ai_coastal_population | Scope to total coastal population recorded in AI spending variables (example: value = cached_ai_coastal_population) | country |
| cached_ai_incorporated_coastal_population | Scope to total incorporated coastal population recorded in AI spending variables (example: value = cached_ai_incorporated_coastal_population) | country |
| cached_ai_incorporated_population | Scope to total incorporated population recorded in AI spending variables (example: value = cached_ai_incorporated_population) | country |
| cached_ai_overseas_subject_population | Scope to total population in direct non-adjacent subjects recorded in AI spending variables (example: value = cached_ai_overseas_subject_population) | country |
| cached_ai_subject_population | Scope to total population in direct subjects recorded in AI spending variables (example: value = cached_ai_subject_population) | country |
| cached_ai_total_population | Scope to total population recorded in AI spending variables (example: value = cached_ai_total_population) | country |
| cached_ai_unincorporated_coastal_population | Scope to total unincorporated coastal population recorded in AI spending variables (example: value = cached_ai_unincorporated_coastal_population) | country |
| cached_ai_unincorporated_population | Scope to total unincorporated population recorded in AI spending variables (example: value = cached_ai_unincorporated_population) | country |
| colonial_growth_per_colony | Scope to the country's colonial growth per colony value (example: colonial_growth_per_colony > 0) | country |
| combat_width | Scope to combat width multiplier of scope province | province |
| command_limit_num_units | Get the baseline number of units from their military formation a commander would normally get, depending on their command limit | character |
| compare_complex_value | A comparison trigger that needs a parsable string parameter that will return its value in the context it is used eg: scope:root.number_of(armies) | varies |
| compare_value | A comparison trigger that will return its value in the context it is used eg: root.gold | varies |
| credit | Scope to the current amount of max credit the country can take | country |
| decree_cost | Scope to a state's cost for a certain decree authority > decree_cost:decree_road_maintaintenance | state |
| defense | Returns the unit's defense rating (including impact from their commander) | new_combat_unit |
| define | Reference the value of a numeric or color define: define:Namespace\|Name | none |
| demoralized | Returns the unit's number of demoralized manpower | new_combat_unit |
| detection | Links from a fleet scope to the total detection of the ships in the fleet | military_formation |
| diplomatic_pact_expense_ratio | Scope to the ratio of diplomatic pact expenses to income for this country, clamped 0-1 (example: value = diplomatic_pact_expense_ratio) | country |
| front_length | Returns the number of provinces in Front | front |
| gdp | Get the scoped country's yearly predicted GDP | country, state |
| global_gdp | Get the global yearly predicted GDP | none |
| global_productivity | Scope to global productivity values (example: global_productivity:high_threshold) | none |
| goal_value | Scope to the journal entry's goal value | journal_entry |
| government_size | Get the scoped country's current number of Parties & independent IGs in government | country |
| income | Get the current weekly income of the scoped country | country |
| income_transfer_expenses | Scope to the amount of money scope country is transferring to other countries via treaties & pacts (example:income_transfer_expenses >= 100) | country |
| income_transfer_relative_expenses | Scope to the fraction of their income country is transferring to other countries via treaties & pacts (example:income_transfer_relative_expenses >= 0.2) | country |
| infamy | Scope to infamy of scope country (example: infamy >= 2) | country |
| infamy_threshold | Scope to infamy level threshold for comparison purposes (infamy_threshold:infamous) | none |
| input_quantity | Scope to the quantity input in a treaty article | treaty_article, treaty_article_options |
| investment | Scope to current investment level in an institution (example: investment < investment_max) | institution |
| investment_max | Scope to the country's current maximum investment level in an institution (example: investment < investment_max) | institution |
| investment_pool_income | Get the current weekly investment pool income of the scoped country | country |
| legitimacy | Scope to the current amount of legitimacy in country | country |
| level | Scope to the level of a building | building |
| level_after_queued_constructions | Scope to the level of a building after all queued constructions finish | building |
| lobby_foreign_anti_clout | Scope to the total clout of all anti-country foreign policy lobbies targeting a specific country (lobby_foreign_anti_clout:root >= 0.2) | country |
| lobby_foreign_pro_clout | Scope to the total clout of all pro-country foreign policy lobbies targeting a specific country (lobby_foreign_pro_clout:root >= 0.2) | country |
| lobby_in_government_foreign_anti_clout | Scope to the total clout of all anti-country foreign policy lobbies in government targeting a specific country (lobby_in_government_foreign_anti_clout:root >= 0.2) | country |
| lobby_in_government_foreign_pro_clout | Scope to the total clout of all pro-country foreign policy lobbies in government targeting a specific country (lobby_in_government_foreign_pro_clout:root >= 0.2) | country |
| lobby_join_weight | Scope to the join weight of an interest group to a particular lobby (lobby_join_weight:root >= 5) | interest_group |
| lobby_war_opposition | Scope to the total clout of all lobbies that oppose the scoped war (lobby_war_opposition:root >= 0.2) | country |
| lobby_war_support | Scope to the total clout of all lobbies that support the scoped war (lobby_war_support:root >= 0.2) | country |
| manpower | Returns the unit's manpower | new_combat_unit |
| market_export_cap | Get the maximum amount of goods the market can export based on it's production of the scoped MarketGoods | market_goods |
| market_import_cap | Get the maximum amount of goods the market can import based on it's consumption of the scoped MarketGoods | market_goods |
| migration_pull | Get the migration pull for a state or the mass migration pull for a country. | country, state |
| military_expenses | Get the current military expenses (slaves, wages and goods) of the scoped country | country |
| military_expenses_share | Get the current share of military expenses (slaves, wages and goods) relative to the total expenses of the scoped country | country |
| mobilization | Returns the unit's mobilization value between 0 and 1 | new_combat_unit |
| modifier | Scope to the value of the modifier type of specified key belonging to the current object, example: modifier:country_influence_add | battle_side, building, character, country, interest_group, market, power_bloc, state |
| momentum | Get the scoped party's raw momentum | party |
| morale | Returns the unit's morale | new_combat_unit |
| mutual_trade_value_with_country | Scope to the total base value of goods traded in trade routes between the two markets (example: mutual_trade_value_with_country:root >= 1000) | country |
| named_script_value | A script value that will calculate and returns its value in the context it is used | none |
| naval_combat_power | Scope to the country's navy combat power (example: naval_combat_power > 100) | country |
| naval_hostility_average_damage_dealt | Scope to average damage dealt by this country in naval hostilities it initiated over the lookback period. Returns -1 if no hostilities found. | country |
| naval_hostility_damage | Scope to damage points inflicted by this country against another in active naval hostilities (example: naval_hostility_damage:root >= 50) | country |
| naval_vulnerability | Scope to a country's naval vulnerability score based on trade reliance and coastal GDP share, capped at a define maximum | country |
| navy_size | Number of flotillas of scope country. | country |
| num_active_interests | Scope to the number of active interests a country has num_active_interests > 5 | country |
| num_active_natural_interests | Scope to the number of active natural interests a country has num_active_natural_interests > 5 | country |
| num_active_plays | Get the current number of active Diplomatic Plays the scoped country started | country |
| num_active_ships | Get the number of active ships for a country, commander or military formation OR Get the number of active ships for military formations in the province that are allied to the specified country | character, country, military_formation, province |
| num_active_ships_in_battle | Get the number of active ships in battle for a country, commander or military formation OR Get the number of active ships in battle for military formations in the province that are allied to the specified country | character, country, military_formation, province |
| num_active_ships_not_in_battle | Get the number of active ships not in battle for a country, commander or military formation OR Get the number of active ships not in battle for military formations in the province that are allied to the specified country | character, country, military_formation, province |
| num_admirals | Scope to the country's number of admirals | country |
| num_alliances | Get the total number of alliances of the scoped country (example: num_alliances:root >= 2) | country |
| num_alliances_and_defensive_pacts_with_allies | Scope to the number of alliances target country has with allies of scope country (example: num_alliances_and_defensive_pacts_with_allies:root >= 2) | country |
| num_alliances_and_defensive_pacts_with_rivals | Scope to the number of alliances & defensive pacts target country has with rivals of scope country (example: num_alliances_and_defensive_pacts_with_rivals:root >= 2) | country |
| num_battalions | Returns the number of active battalions under a commander | character |
| num_characters | Scope to the country's number of characters | country |
| num_colony_projects | Get the scoped country's current number of incomplete / in progress colony projects | country |
| num_commanderless_units | Number of units in a MilitaryFormation which currently don't have a commander due to commanders Command Limit. Obs: defeated commanders do not command units, i.e., the more defeated commanders, the more commanderless units. | military_formation |
| num_commanders | Scope to the country's number of commanders | country |
| num_defending_battalions | Returns the total number of units in battle on Front on the same side as Country, example: num_defending_battalions(root) | front |
| num_defensive_pacts | Scope to the number of defensive pacts target country has in total (example: num_defensive_pacts >= 2) | country |
| num_garrison_units | Returns the number of units garrisoned in a HQ | hq |
| num_generals | Scope to the country's number of generals | country |
| num_income_transfer_pacts | Scope to the number of income-transferring (to others) pacts target country has in total (example: num_income_transfer_pacts >= 2) | country |
| num_income_transfer_treaty_articles | Scope to the number of income-transferring (to others) treaty articles target country has in total (example: num_income_transfer_treaty_articles >= 2) | country |
| num_income_transfers | Scope to the number of income-transferring (to others) pacts and treaty articles target country has in total (example: num_income_transfers >= 2) | country |
| num_incorporated_states | Get the scoped country's current number of incorporated states | country |
| num_interests | Scope to the number of interests a country has (including inactive) num_interests > 5 | country |
| num_mandates | Scope to the number of available mandates of the scoped power bloc (power_bloc.num_mandates > 0) | power_bloc |
| num_mobilized_battalions | Returns the number of fully mobilized units under a General | character |
| num_natural_interests | Scope to the number of natural interests a country has (including inactive) num_natural_interests > 5 | country |
| num_non_destroyed_ships | Get the number of non-destroyed ships for a country, commander or military formation OR Get the number of non-destroyed ships for military formations in the province that are allied to the specified country | character, country, military_formation, province |
| num_non_destroyed_ships_in_battle | Get the number of non-destroyed ships in battle for a country, commander or military formation OR Get the number of non-destroyed ships in battle for military formations in the province that are allied to the specified country | character, country, military_formation, province |
| num_non_destroyed_ships_not_in_battle | Get the number of non-destroyed ships not in battle for a country, commander or military formation OR Get the number of non-destroyed ships not in battle for military formations in the province that are allied to the specified country | character, country, military_formation, province |
| num_obligations_earned | Scope from a country to the number of obligations others owe them (=which they have earned) | country |
| num_pending_events | Scope to the number of pending events in scope country, generally or for a specified category num_pending_events > 0 num_pending_events:enactment > 0 | country |
| num_politicians | Scope to the country's number of politicians | country |
| num_positive_relations | Get the current number of countries with positive Relation with the scoped country | country |
| num_provinces | Get the scoped entity's current number of provinces | front, state, state_region |
| num_queued_constructions | Scope to the number of queued constructions target country has in total (example: num_queued_constructions >= 2) | country |
| num_queued_government_constructions | Scope to the number of queued government constructions target country has in total (example: num_queued_government_constructions >= 2) | country |
| num_queued_private_constructions | Scope to the number of queued private constructions target country has in total (example: num_queued_private_constructions >= 2) | country |
| num_rivals | Scope to the number of rivals target country has in total (example: num_rivals >= 2) | country |
| num_ruling_igs | Get the scoped country's current number of IGs in government | country |
| num_shared_rivals | Scope to the number of shared rivals scope country has with target country (example: num_shared_rivals:root >= 2) | country |
| num_ships | Get the number of ships for a country, commander or military formation OR Get the number of ships for military formations in the province that are allied to the specified country | character, country, military_formation, province |
| num_ships_in_battle | Get the number of ships in battle for a country, commander or military formation OR Get the number of ships in battle for military formations in the province that are allied to the specified country | character, country, military_formation, province |
| num_ships_not_in_battle | Get the number of ships not in battle for a country, commander or military formation OR Get the number of ships not in battle for military formations in the province that are allied to the specified country | character, country, military_formation, province |
| num_ships_of_group | Number of ships of the provided ship group in the scoped country or military formation | country, military_formation |
| num_states | Get the scoped country's current number of states | country |
| num_total_battalions | Returns the total number of units on Front on the same side as Country, example: num_total_battalions(root) | front |
| num_unincorporated_states | Get the scoped country's current number of unincorporated states | country |
| num_units | Get the number of active units for a commander or military formation Get the number of active units for military formations in the province that are allied to the specified country | character, military_formation, province |
| num_units_in_battle | Get the number of active units in battle for a commander or military formation Get the number of active units in battle for military formations in the province that are allied to the specified country | character, military_formation, province |
| num_units_not_in_battle | Get the number of active units not in battle for a commander or military formation Get the number of active units not in battle for military formations in the province that are allied to the specified country | character, military_formation, province |
| num_units_share | Share of units a commander has considering his command limit. Example: if the character has 30 Command Limit, the fleet has 60 total Command Limit, and the formation has 50 total flotillas, then the character should get 25 flotillas for their battle) | character |
| num_world_market_hub_trade_center_levels | Get the total number of trade center levels associated with scope world market hub state | state |
| offense | Returns the unit's offense rating (including impact from their commander) | new_combat_unit |
| participants | Get the total number of participating countries in the scoped market | market |
| pirated_trade_value_by | Scope to the average weekly base value of goods pilfered from this country by a target country (example: pirated_trade_value_by:root >= 50) | country |
| player_owed_obligation_days_left | Scope to number of days left on an obligation in diplomatic relations scope (example: obligation_days_left >= 2) | diplomatic_relations |
| pop_weight_modifier_scale | Get the Pop's weight modifier scale multiplier | pop |
| popularity | Get the scoped character's popularity, normally ranging between -100 and +100 | character |
| population_below_expected_sol | Scope to the current percentage of the state's population that are below their expected standard of living (0-1) | state |
| power_projection | Get the power projection value of the scoped formation, unit, or ship | military_formation, new_combat_unit, ship |
| principal | Get the current debt principal of the country | country |
| prosperity | Scope to the amount of prosperity for scope company (example: prosperity >= 2) | company |
| rank_value | Scope to rank value of a particular country rank (rank_value:great_power) | none |
| relations | Scope to relations between two countries (example: relations:root >= 2) | country |
| relations_change_rate | Scope to daily change in relations progress between two countries (example: relations_change_rate:root > 0) | country |
| relations_threshold | Scope to relations threshold level for comparison purposes (relations_threshold:warm) | none |
| remaining_binding_period | Get the current remaining binding period in days for the scoped treaty | treaty, treaty_options |
| required_construction | Get the required amount of construction for scope building type | building_type |
| scope_relations | Scope to relations value in diplomatic relations scope (example: scope_relations >= 2) | diplomatic_relations |
| scope_tension | Scope to tension value in diplomatic relations scope (example: scope_tension >= 2) | diplomatic_relations |
| screening | Links from a fleet scope to the total screening of the ships in the fleet | military_formation |
| strait_trade_importance_by | Scope to the trade importance of goods this country is trading through straits controlled by a target country. Accumulated value is multiplied by STRAIT_FULL_CONTROL_TRADE_IMPORTANCE_MULT for straits where the controller controls both sides (example: strait_trade_importance_by:root >= 100) | country |
| techs_researched | Scope to the current amount of techs researched of a country | country |
| tension | Scope to tension between two countries (example: tension:root >= 2) | country |
| tension_threshold | Scope to tension level threshold for comparison purposes (tension_threshold:warm) | none |
| total_crew_needed | Get the total crew needed by all ships of a country | country |
| total_export_value | Scope to the total value of scope country's exports to the world market (example: total_export_value >= 1000) | country |
| total_import_value | Scope to the total value of scope country's imports from the world market (example: total_import_value >= 1000) | country |
| total_marine_capacity | Get the total marine capacity across all fleets of a country | country |
| total_pirated_trade_value | Scope to the total average weekly base value of goods pilfered via piracy between two countries in a diplomatic relations scope (example: total_pirated_trade_value >= 100) | diplomatic_relations |
| total_trade_value | Scope to the total value of scope country's trade with the world market (example: total_trade_value >= 1000) | country |
| training_rate | Scope to the current maximum weekly training rate of a building | building |
| treaty_exports | Get the current number of treaty (NOT world market) exports of the good to the market of the scoped MarketGoods | market_goods |
| treaty_imports | Get the current number of treaty (NOT world market) imports of the good to the market of the scoped MarketGoods | market_goods |
| value | A numeric literal value eg: 1, 5.2, -6 | none |
| visibility | Links from a fleet scope to the total visibility of the ships in the fleet | military_formation |
| vulnerability | Links from a fleet scope to the total vulnerability of the ships in the fleet | military_formation |
| weekly_prosperity_change | Scope to the weekly prosperity change for scope company (example: weekly_prosperity_change >= 2) | company |

## Wild card event targets

These event targets refer to a type of event target, rather than a specifically named event target. For example, the event target `compare_value` refers to any simple, inline [trigger](Trigger.md) which checks a numerical value such as `free_arable_land`. Similarly, `named_script_value` refers to the calculated [script value](Script value.md) by its name.

| Event target | Description | From scope | To scope |
|---|---|---|---|
| compare_complex_value | A comparison trigger that needs a parsable string parameter that will return its value in the context it is used eg: scope:root.number_of(armies) | varies | value |
| compare_value | A comparison trigger that will return its value in the context it is used eg: root.gold | varies | value |
| named_script_value | A script value that will calculate and returns its value in the context it is used | none | color, value |
| value | A numeric literal value eg: 1, 5.2, -6 | none | value |

## Event targets by scope

The following tables list event targets by their required scope. Some event targets are repeated as they can be used in multiple scopes. Event targets that can be used in any scope are indicated with `none`.

### None scope/scopeless

| Event target | Description | To scope |
|---|---|---|
| amendment_type | Scope to an amendment type from its name (amendment_type:key) | amendment_type |
| array_define | Reference the value of a numeric value in an array define: array_define:Namespace\|Name\|Index. Index is 0-based. | value |
| bg | Scope to a building group from its name (bg:bg_logging) | building_group |
| bt | Scope to a building type, example: bt:building_tooling_workshops | building_type |
| c | Scope to the country with specified tag, example: c:GBR | country |
| catalyst_type | Scope to a diplomatic catalyst type from its name (catalyst_type:catalyst_relations_level_improved) | diplomatic_catalyst_type |
| cd | Scope to the country definition with specified tag, example: cd:FRA | country_definition |
| company_type | Scope to a company type from its name (company_type:company_rheinmetall) | company_type |
| cu | Scope to the culture with specified key, example: cu:welsh | culture |
| define | Reference the value of a numeric or color define: define:Namespace\|Name | value |
| flag | A localization key, ex. flag:the_boss | flag |
| g | Scope to the goods with specified key, example: g:iron | goods |
| global_gdp | Get the global yearly predicted GDP | value |
| global_productivity | Scope to global productivity values (example: global_productivity:high_threshold) | value |
| global_var | Reference a previous set global variable via its name eg: global_var:important_thing | varies |
| harvest_condition_type | Scope to a harvest condition type from its name (harvest_condition_type:drought) | harvest_condition_type |
| i | Scope to ideology specified by key, example: i:ideology_patriarchal | ideology |
| identity | Scope to the power bloc identity from its name (identity:key) | power_bloc_identity |
| ideology | Dual use Scope to a ideology from its name (ideology:ideology_anarchist) Scope to the ideology of the scoped character | ideology |
| ig_trait | Scope to the Interest Group trait with specified key, example: ig_trait:ig_trait_xenophobia | interest_group_trait |
| ig_type | Scope to an interest group type, example: ig_type:ig_landowners | interest_group_type |
| infamy_threshold | Scope to infamy level threshold for comparison purposes (infamy_threshold:infamous) | value |
| is_setup | Scope to true/false if gamestate is being initialized! | boolean |
| je_tutorial | Scope to the active tutorial lesson's journal entry (do not use this outside tutorial) | journal_entry |
| law_type | Scope to a law type from its name (law_type:law_protected_speech) or from a scoped law | law_type |
| lobby_type | Scope to a political lobby type from its name (lobby_type:lobby_pro_country) | political_lobby_type |
| local_var | Reference a previous set local variable via its name eg: local_var:person_of_interest | varies |
| mobilization_option | Scope to a mobilization option from its name (mobilization_option:key) | mobilization_option |
| movement_type | Scope to a political movement type from its name (movement_type:movement_religious_majority) | political_movement_type |
| named_script_value | A script value that will calculate and returns its value in the context it is used | color, value |
| no | Boolean literal for false values | boolean |
| p | Scope to province specified by hex key, example: p:x1A6E5B | province |
| play_type | Scope to a diplomatic play type from its name (play_type:dp_default_treaty_article) | diplomatic_play_type |
| player | Scope to the player (do not use this outside tutorial) | country |
| pop_type | Scope to a pop type from its name (pop_type:laborers) | pop_type |
| prev | The previous scope | varies |
| principle | Scope to the power bloc principle from its name (principle:key) | power_bloc_principle |
| principle_group | Scope to the power bloc principle group from its name (principle_group:key) | power_bloc_principle_group |
| rank_value | Scope to rank value of a particular country rank (rank_value:great_power) | value |
| rel | Scope to the religion with specified key, example: rel:catholic | religion |
| relations_threshold | Scope to relations threshold level for comparison purposes (relations_threshold:warm) | value |
| root | The head of the current top scope eg: receiver of an event, taker of a decision | varies |
| s | Scope to state region specified by key, example: s:STATE_UTAH | state_region |
| scope | Reference a previously saved scope via its name eg: scope:target | varies |
| ship_group | Scope from a ship to its group or Scope to a ship group from its name (ship_group:ship_group_capital_ships) | ship_group |
| ship_type | Scope to a ship type from its name (ship_type:ship_type_frigate) | ship_type |
| sr | Scope to the strategic region of specified key, example: sr:region_persia | strategic_region |
| strait_type | Scope to a strait type from its name (strait_type:key) | strait_type |
| tension_threshold | Scope to tension level threshold for comparison purposes (tension_threshold:warm) | value |
| this | The current scope | varies |
| unit_type | Scope to a combat unit type from its name (unit_type:key) | combat_unit_type |
| value | A numeric literal value eg: 1, 5.2, -6 | value |
| yes | Boolean literal for true values | boolean |

### Battle scope

| Event target | Description | To scope |
|---|---|---|
| attacker_side | Scope from a battle to the BattleSide corresponding to the attacker | battle_side |
| defender_side | Scope from a battle to the BattleSide corresponding to the defender | battle_side |
| front | Scope to a front from various scopes From a battle to the front where it takes place From a character to the front where they are at or travelling towards From a military formation to the front it is currently at From a province to the front that contains it From an invasion to the invasion front | front |

### Building scope

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

### Character scope

| Event target | Description | To scope |
|---|---|---|
| average_progressiveness | Get the average progressiveness of the scoped character or interest group | value |
| command_limit_num_units | Get the baseline number of units from their military formation a commander would normally get, depending on their command limit | value |
| commander_military_formation | Scope to the Military Formation of a Character. | military_formation |
| culture | Scope to pop's or character's culture | culture |
| front | Scope to a front from various scopes From a battle to the front where it takes place From a character to the front where they are at or travelling towards From a military formation to the front it is currently at From a province to the front that contains it From an invasion to the invasion front | front |
| home_country | Scopes to the home country of an exile | country |
| ideology | Dual use Scope to a ideology from its name (ideology:ideology_anarchist) Scope to the ideology of the scoped character | ideology |
| interest_group | Scope to the interest group of the character! | interest_group |
| interest_group_type | Scope to the type of the scoped character's interest group | interest_group_type |
| modifier | Scope to the value of the modifier type of specified key belonging to the current object, example: modifier:country_influence_add | boolean, value |
| num_active_ships | Get the number of active ships for a country, commander or military formation OR Get the number of active ships for military formations in the province that are allied to the specified country | value |
| num_active_ships_in_battle | Get the number of active ships in battle for a country, commander or military formation OR Get the number of active ships in battle for military formations in the province that are allied to the specified country | value |
| num_active_ships_not_in_battle | Get the number of active ships not in battle for a country, commander or military formation OR Get the number of active ships not in battle for military formations in the province that are allied to the specified country | value |
| num_battalions | Returns the number of active battalions under a commander | value |
| num_mobilized_battalions | Returns the number of fully mobilized units under a General | value |
| num_non_destroyed_ships | Get the number of non-destroyed ships for a country, commander or military formation OR Get the number of non-destroyed ships for military formations in the province that are allied to the specified country | value |
| num_non_destroyed_ships_in_battle | Get the number of non-destroyed ships in battle for a country, commander or military formation OR Get the number of non-destroyed ships in battle for military formations in the province that are allied to the specified country | value |
| num_non_destroyed_ships_not_in_battle | Get the number of non-destroyed ships not in battle for a country, commander or military formation OR Get the number of non-destroyed ships not in battle for military formations in the province that are allied to the specified country | value |
| num_ships | Get the number of ships for a country, commander or military formation OR Get the number of ships for military formations in the province that are allied to the specified country | value |
| num_ships_in_battle | Get the number of ships in battle for a country, commander or military formation OR Get the number of ships in battle for military formations in the province that are allied to the specified country | value |
| num_ships_not_in_battle | Get the number of ships not in battle for a country, commander or military formation OR Get the number of ships not in battle for military formations in the province that are allied to the specified country | value |
| num_units | Get the number of active units for a commander or military formation Get the number of active units for military formations in the province that are allied to the specified country | value |
| num_units_in_battle | Get the number of active units in battle for a commander or military formation Get the number of active units in battle for military formations in the province that are allied to the specified country | value |
| num_units_not_in_battle | Get the number of active units not in battle for a commander or military formation Get the number of active units not in battle for military formations in the province that are allied to the specified country | value |
| num_units_share | Share of units a commander has considering his command limit. Example: if the character has 30 Command Limit, the fleet has 60 total Command Limit, and the formation has 50 total flotillas, then the character should get 25 flotillas for their battle) | value |
| opposing_commander | Scope from a character in battle to the character on the other side of the battle | character |
| owner | Scope to the owner country of object | country |
| political_movement | If used in a character scope, scope to the political movement that character supports. If used in a revolution civil war scope, scope to the movement that started the revolution. If used in an interest group scope, scope to the group's dominant movement. | political_movement |
| popularity | Get the scoped character's popularity, normally ranging between -100 and +100 | value |
| religion | Scope to country or country definition's primary religion or pop religion | religion |

### Country scope

| Event target | Description | To scope |
|---|---|---|
| active_law | Scope to the scoped country's active law in the named law group (active_law:lawgroup_trade_policy) | law |
| ai_army_comparison | Scope to comparative army strength between two countries (example: value = ai_army_comparison:root) | value |
| ai_gdp_comparison | Scope to comparative GDP between two countries (example: value = ai_army_comparison:root) | value |
| ai_ideological_opinion | Scope to AI ideological opinion of scope country on target country (example: value = ai_ideological_opinion:root) | value |
| ai_navy_comparison | Scope to comparative navy strength between two countries (example: value = ai_navy_comparison:root) | value |
| ai_subject_value | Scope to AI desire of target country to have scope country as a subject (example: value = ai_subject_value:root) | value |
| ai_transit_rights_value | Scope to AI desire of to have transit rights through target country (example: value = ai_transit_rights_value:root) | value |
| ai_treaty_fairness | Scope to AI evaluation of how fair (to both sides) it considers existing treaty articles with the target country to be (example: value = ai_treaty_fairness_score:root) | value |
| ai_treaty_value | Scope to AI evaluation of how favorable to itself it considers existing treaty articles with the target country to be (example: value = ai_treaty_value:root) | value |
| army_size | Number of battalions of scope country, excluding currently raised conscripts. | value |
| army_size_including_conscripts | Number of battalions of scope country, including currently raised conscripts. | value |
| army_size_including_raised_conscripts | Number of battalions of scope country, including currently raised conscripts but excluding unraised conscripts. | value |
| average_expected_sol | Get the average expected Standard of Living of the scope | value |
| average_sol | Get the average Standard of Living of the scope | value |
| building_levels | Get the total number of non-subsistence building levels of the scoped country | value |
| cached_ai_coastal_population | Scope to total coastal population recorded in AI spending variables (example: value = cached_ai_coastal_population) | value |
| cached_ai_incorporated_coastal_population | Scope to total incorporated coastal population recorded in AI spending variables (example: value = cached_ai_incorporated_coastal_population) | value |
| cached_ai_incorporated_population | Scope to total incorporated population recorded in AI spending variables (example: value = cached_ai_incorporated_population) | value |
| cached_ai_overseas_subject_population | Scope to total population in direct non-adjacent subjects recorded in AI spending variables (example: value = cached_ai_overseas_subject_population) | value |
| cached_ai_subject_population | Scope to total population in direct subjects recorded in AI spending variables (example: value = cached_ai_subject_population) | value |
| cached_ai_total_population | Scope to total population recorded in AI spending variables (example: value = cached_ai_total_population) | value |
| cached_ai_unincorporated_coastal_population | Scope to total unincorporated coastal population recorded in AI spending variables (example: value = cached_ai_unincorporated_coastal_population) | value |
| cached_ai_unincorporated_population | Scope to total unincorporated population recorded in AI spending variables (example: value = cached_ai_unincorporated_population) | value |
| capital | Scope to the capital state of a country | state |
| civil_war_origin_country | Scope to the origin country of a civil war country | country |
| colonial_growth_per_colony | Scope to the country's colonial growth per colony value (example: colonial_growth_per_colony > 0) | value |
| company | Scope to the scoped country's company of the named company type (company:company_rheinmetall) | company |
| country_definition | Scope to country's definition | country_definition |
| credit | Scope to the current amount of max credit the country can take | value |
| currently_enacting_law | Scope from a country to the law that they're currently enacting | law |
| diplomatic_pact_expense_ratio | Scope to the ratio of diplomatic pact expenses to income for this country, clamped 0-1 (example: value = diplomatic_pact_expense_ratio) | value |
| flagship | Get the flagship of the scoped country | ship |
| gdp | Get the scoped country's yearly predicted GDP | value |
| get_ruler_for | Scopes from country to a character that would be ruler, under the given transfer of power type get_ruler_for:parliamentary_elective = { effects... } | character |
| government_size | Get the scoped country's current number of Parties & independent IGs in government | value |
| heir | Scope to the heir of a country | character |
| ig | Scope to the interest group of specified key belonging to the country, example: ig:ig_armed_forces | interest_group |
| imposed_law | Scope from a country to the law currently imposed on them (enacting or not) | law |
| imposer_of_law | Scope from a country to the country currently imposing a law on them | country |
| income | Get the current weekly income of the scoped country | value |
| income_transfer_expenses | Scope to the amount of money scope country is transferring to other countries via treaties & pacts (example:income_transfer_expenses >= 100) | value |
| income_transfer_relative_expenses | Scope to the fraction of their income country is transferring to other countries via treaties & pacts (example:income_transfer_relative_expenses >= 0.2) | value |
| infamy | Scope to infamy of scope country (example: infamy >= 2) | value |
| institution | Scope to a country's institution from its name (institution:institution_health_system) | institution |
| investment_pool_income | Get the current weekly investment pool income of the scoped country | value |
| je | Scope to the journal entry of specified key belonging to the country, example: je:je_antarctica | journal_entry |
| legitimacy | Scope to the current amount of legitimacy in country | value |
| lobby_foreign_anti_clout | Scope to the total clout of all anti-country foreign policy lobbies targeting a specific country (lobby_foreign_anti_clout:root >= 0.2) | value |
| lobby_foreign_pro_clout | Scope to the total clout of all pro-country foreign policy lobbies targeting a specific country (lobby_foreign_pro_clout:root >= 0.2) | value |
| lobby_in_government_foreign_anti_clout | Scope to the total clout of all anti-country foreign policy lobbies in government targeting a specific country (lobby_in_government_foreign_anti_clout:root >= 0.2) | value |
| lobby_in_government_foreign_pro_clout | Scope to the total clout of all pro-country foreign policy lobbies in government targeting a specific country (lobby_in_government_foreign_pro_clout:root >= 0.2) | value |
| lobby_war_opposition | Scope to the total clout of all lobbies that oppose the scoped war (lobby_war_opposition:root >= 0.2) | value |
| lobby_war_support | Scope to the total clout of all lobbies that support the scoped war (lobby_war_support:root >= 0.2) | value |
| market | Scope to the market of the object | market |
| market_capital | Scope to the market capital of a country | state |
| migration_pull | Get the migration pull for a state or the mass migration pull for a country. | value |
| military_expenses | Get the current military expenses (slaves, wages and goods) of the scoped country | value |
| military_expenses_share | Get the current share of military expenses (slaves, wages and goods) relative to the total expenses of the scoped country | value |
| modifier | Scope to the value of the modifier type of specified key belonging to the current object, example: modifier:country_influence_add | boolean, value |
| mutual_trade_value_with_country | Scope to the total base value of goods traded in trade routes between the two markets (example: mutual_trade_value_with_country:root >= 1000) | value |
| naval_combat_power | Scope to the country's navy combat power (example: naval_combat_power > 100) | value |
| naval_hostility_average_damage_dealt | Scope to average damage dealt by this country in naval hostilities it initiated over the lookback period. Returns -1 if no hostilities found. | value |
| naval_hostility_damage | Scope to damage points inflicted by this country against another in active naval hostilities (example: naval_hostility_damage:root >= 50) | value |
| naval_vulnerability | Scope to a country's naval vulnerability score based on trade reliance and coastal GDP share, capped at a define maximum | value |
| navy_size | Number of flotillas of scope country. | value |
| num_active_interests | Scope to the number of active interests a country has num_active_interests > 5 | value |
| num_active_natural_interests | Scope to the number of active natural interests a country has num_active_natural_interests > 5 | value |
| num_active_plays | Get the current number of active Diplomatic Plays the scoped country started | value |
| num_active_ships | Get the number of active ships for a country, commander or military formation OR Get the number of active ships for military formations in the province that are allied to the specified country | value |
| num_active_ships_in_battle | Get the number of active ships in battle for a country, commander or military formation OR Get the number of active ships in battle for military formations in the province that are allied to the specified country | value |
| num_active_ships_not_in_battle | Get the number of active ships not in battle for a country, commander or military formation OR Get the number of active ships not in battle for military formations in the province that are allied to the specified country | value |
| num_admirals | Scope to the country's number of admirals | value |
| num_alliances | Get the total number of alliances of the scoped country (example: num_alliances:root >= 2) | value |
| num_alliances_and_defensive_pacts_with_allies | Scope to the number of alliances target country has with allies of scope country (example: num_alliances_and_defensive_pacts_with_allies:root >= 2) | value |
| num_alliances_and_defensive_pacts_with_rivals | Scope to the number of alliances & defensive pacts target country has with rivals of scope country (example: num_alliances_and_defensive_pacts_with_rivals:root >= 2) | value |
| num_characters | Scope to the country's number of characters | value |
| num_colony_projects | Get the scoped country's current number of incomplete / in progress colony projects | value |
| num_commanders | Scope to the country's number of commanders | value |
| num_defensive_pacts | Scope to the number of defensive pacts target country has in total (example: num_defensive_pacts >= 2) | value |
| num_generals | Scope to the country's number of generals | value |
| num_income_transfer_pacts | Scope to the number of income-transferring (to others) pacts target country has in total (example: num_income_transfer_pacts >= 2) | value |
| num_income_transfer_treaty_articles | Scope to the number of income-transferring (to others) treaty articles target country has in total (example: num_income_transfer_treaty_articles >= 2) | value |
| num_income_transfers | Scope to the number of income-transferring (to others) pacts and treaty articles target country has in total (example: num_income_transfers >= 2) | value |
| num_incorporated_states | Get the scoped country's current number of incorporated states | value |
| num_interests | Scope to the number of interests a country has (including inactive) num_interests > 5 | value |
| num_natural_interests | Scope to the number of natural interests a country has (including inactive) num_natural_interests > 5 | value |
| num_non_destroyed_ships | Get the number of non-destroyed ships for a country, commander or military formation OR Get the number of non-destroyed ships for military formations in the province that are allied to the specified country | value |
| num_non_destroyed_ships_in_battle | Get the number of non-destroyed ships in battle for a country, commander or military formation OR Get the number of non-destroyed ships in battle for military formations in the province that are allied to the specified country | value |
| num_non_destroyed_ships_not_in_battle | Get the number of non-destroyed ships not in battle for a country, commander or military formation OR Get the number of non-destroyed ships not in battle for military formations in the province that are allied to the specified country | value |
| num_obligations_earned | Scope from a country to the number of obligations others owe them (=which they have earned) | value |
| num_pending_events | Scope to the number of pending events in scope country, generally or for a specified category num_pending_events > 0 num_pending_events:enactment > 0 | value |
| num_politicians | Scope to the country's number of politicians | value |
| num_positive_relations | Get the current number of countries with positive Relation with the scoped country | value |
| num_queued_constructions | Scope to the number of queued constructions target country has in total (example: num_queued_constructions >= 2) | value |
| num_queued_government_constructions | Scope to the number of queued government constructions target country has in total (example: num_queued_government_constructions >= 2) | value |
| num_queued_private_constructions | Scope to the number of queued private constructions target country has in total (example: num_queued_private_constructions >= 2) | value |
| num_rivals | Scope to the number of rivals target country has in total (example: num_rivals >= 2) | value |
| num_ruling_igs | Get the scoped country's current number of IGs in government | value |
| num_shared_rivals | Scope to the number of shared rivals scope country has with target country (example: num_shared_rivals:root >= 2) | value |
| num_ships | Get the number of ships for a country, commander or military formation OR Get the number of ships for military formations in the province that are allied to the specified country | value |
| num_ships_in_battle | Get the number of ships in battle for a country, commander or military formation OR Get the number of ships in battle for military formations in the province that are allied to the specified country | value |
| num_ships_not_in_battle | Get the number of ships not in battle for a country, commander or military formation OR Get the number of ships not in battle for military formations in the province that are allied to the specified country | value |
| num_ships_of_group | Number of ships of the provided ship group in the scoped country or military formation | value |
| num_states | Get the scoped country's current number of states | value |
| num_unincorporated_states | Get the scoped country's current number of unincorporated states | value |
| overlord | Scope to the direct overlord of the country in scope | country |
| owner | Scope to the owner country of object | country |
| owning_company | Scope to the company owning the scoped country | company |
| pirated_trade_value_by | Scope to the average weekly base value of goods pilfered from this country by a target country (example: pirated_trade_value_by:root >= 50) | value |
| power_bloc | Scope to the power bloc for the scoped country | power_bloc |
| principal | Get the current debt principal of the country | value |
| py | Scope to the active party of specified key belonging to the country, example: py:communist_party | party |
| relations | Scope to relations between two countries (example: relations:root >= 2) | value |
| relations_change_rate | Scope to daily change in relations progress between two countries (example: relations_change_rate:root > 0) | value |
| religion | Scope to country or country definition's primary religion or pop religion | religion |
| ruler | Scope to the ruler of a country | character |
| strait_trade_importance_by | Scope to the trade importance of goods this country is trading through straits controlled by a target country. Accumulated value is multiplied by STRAIT_FULL_CONTROL_TRADE_IMPORTANCE_MULT for straits where the controller controls both sides (example: strait_trade_importance_by:root >= 100) | value |
| technology_being_researched | Scope to the current technology a country is researching | technology |
| techs_researched | Scope to the current amount of techs researched of a country | value |
| tension | Scope to tension between two countries (example: tension:root >= 2) | value |
| top_overlord | Scope to the top overlord of the country in scope | country |
| total_crew_needed | Get the total crew needed by all ships of a country | value |
| total_export_value | Scope to the total value of scope country's exports to the world market (example: total_export_value >= 1000) | value |
| total_import_value | Scope to the total value of scope country's imports from the world market (example: total_import_value >= 1000) | value |
| total_marine_capacity | Get the total marine capacity across all fleets of a country | value |
| total_trade_value | Scope to the total value of scope country's trade with the world market (example: total_trade_value >= 1000) | value |

### Diplomacy scopes

| Event target | Description | To scope |
|---|---|---|
| initiator | Scope to the initiator of the object | country |
| region | Scope to the strategic region of the object! | strategic_region |
| target | Scope to the target of the object | varies |
| type | Scope from an object to its type | amendment_type, building_type, company_type, diplomatic_play_type, harvest_condition_type, institution_type, interest_group_type, law_type, political_movement_type, ship_type, strait_type |
| war | Scope from a diplomatic play to its war | war |

| Event target | Description | To scope |
|---|---|---|
| diplomatic_pact_other_country | Scope to the other country of the diplomatic pact in scope, example: diplomatic_pact_other_country(root) | country |
| first_country | Scope to the first_country of any of: diplomatic pact treaty treaty options treaty article's treaty treaty article options (for mutual article types only) | country |
| second_country | Scope to the second_country of any of: diplomatic pact treaty treaty options treaty article's treaty treaty article options (for mutual article types only) | country |

| Event target | Description | To scope |
|---|---|---|
| player_owed_obligation_days_left | Scope to number of days left on an obligation in diplomatic relations scope (example: obligation_days_left >= 2) | value |
| scope_relations | Scope to relations value in diplomatic relations scope (example: scope_relations >= 2) | value |
| scope_tension | Scope to tension value in diplomatic relations scope (example: scope_tension >= 2) | value |
| total_pirated_trade_value | Scope to the total average weekly base value of goods pilfered via piracy between two countries in a diplomatic relations scope (example: total_pirated_trade_value >= 100) | value |

### Goods scopes

| Event target | Description | To scope |
|---|---|---|
| base_price | Get the base price of the scoped good | value |

| Event target | Description | To scope |
|---|---|---|
| ai_treaty_export_value | Scope to target country AI desire to export scoped market good (example: value = ai_market_export_value:root) | value |
| ai_treaty_import_value | Scope to target country AI desire to import scoped market good through treaties (example: value = ai_market_import_value:root) | value |
| ai_treaty_trade_value | Scope to target country AI desire to import and export scoped market good (example: value = ai_market_trade_value:root) | value |
| goods | Scope to the goods traded by a trade route | goods |
| largest_exporting_market | Scope to the largest exporting market for the scope market good to the local market | market |
| largest_importing_market | Scope to the largest importing market for the scope market good from the local market | market |
| market | Scope to the market of the object | market |
| market_export_cap | Get the maximum amount of goods the market can export based on it's production of the scoped MarketGoods | value |
| market_import_cap | Get the maximum amount of goods the market can import based on it's consumption of the scoped MarketGoods | value |
| owner | Scope to the owner country of object | country |
| treaty_exports | Get the current number of treaty (NOT world market) exports of the good to the market of the scoped MarketGoods | value |
| treaty_imports | Get the current number of treaty (NOT world market) imports of the good to the market of the scoped MarketGoods | value |

| Event target | Description | To scope |
|---|---|---|
| goods | Scope to the goods traded by a trade route | goods |
| market | Scope to the market of the object | market |

### Law scope

| Event target | Description | To scope |
|---|---|---|
| currently_active_law_in_group | Scope from a law to the currently active law in that group | law |
| imposer_of_law | Scope from a country to the country currently imposing a law on them | country |
| law_type | Scope to a law type from its name (law_type:law_protected_speech) or from a scoped law | law_type |
| owner | Scope to the owner country of object | country |
| type | Scope from an object to its type | amendment_type, building_type, company_type, diplomatic_play_type, harvest_condition_type, institution_type, interest_group_type, law_type, political_movement_type, ship_type, strait_type |

### Market scope

| Event target | Description | To scope |
|---|---|---|
| market | Scope to the market of the object | market |
| mg | Scope from a market to the MarketGoods with the specified key, (example: mg:tools) | market_goods |
| modifier | Scope to the value of the modifier type of specified key belonging to the current object, example: modifier:country_influence_add | boolean, value |
| owner | Scope to the owner country of object | country |
| participants | Get the total number of participating countries in the scoped market | value |
| state | Scope to the state of the object | state |
| trade_center | Scope to the trade center state of the market! | state |

### Pop scope

| Event target | Description | To scope |
|---|---|---|
| culture | Scope to pop's or character's culture | culture |
| home_country | Scopes to the home country of an exile | country |
| owner | Scope to the owner country of object | country |
| pop_weight_modifier_scale | Get the Pop's weight modifier scale multiplier | value |
| religion | Scope to country or country definition's primary religion or pop religion | religion |
| state | Scope to the state of the object | state |
| workplace | Scope to the workplace of a pop | building |

### Power bloc scope

| Event target | Description | To scope |
|---|---|---|
| modifier | Scope to the value of the modifier type of specified key belonging to the current object, example: modifier:country_influence_add | boolean, value |
| num_mandates | Scope to the number of available mandates of the scoped power bloc (power_bloc.num_mandates > 0) | value |
| power_bloc_leader | Scope to the leader country of the scoped power bloc | country |
| power_struggle_contender | Scope to the contender country if there is a power struggle | country |

### State scope

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

### Treaty scopes

| Event target | Description | To scope |
|---|---|---|
| amended_treaty | Scope to the treaty the scoped treaty is amending | treaty |
| binding_period | Get the original binding period in days when the treaty was signed for the scoped treaty | value |
| enforced_on_country | Scope to the enforced_on_country of an enforced treaty | country |
| enforcer_country | Scope to the enforcer_country of an enforced treaty | country |
| first_country | Scope to the first_country of any of: diplomatic pact treaty treaty options treaty article's treaty treaty article options (for mutual article types only) | country |
| remaining_binding_period | Get the current remaining binding period in days for the scoped treaty | value |
| second_country | Scope to the second_country of any of: diplomatic pact treaty treaty options treaty article's treaty treaty article options (for mutual article types only) | country |

| Event target | Description | To scope |
|---|---|---|
| first_country | Scope to the first_country of any of: diplomatic pact treaty treaty options treaty article's treaty treaty article options (for mutual article types only) | country |
| input_building_type | Scope to the building type input in a treaty article | building_type |
| input_company | Scope to the company input in a treaty article | company |
| input_country | Scope to the country input in a treaty article | country |
| input_goods | Scope to the goods input in a treaty article | goods |
| input_law | Scope to the law input in a treaty article | law_type |
| input_market_goods | Scope to the market goods input in a treaty article (example: input_market_goods:root) | market_goods |
| input_quantity | Scope to the quantity input in a treaty article | value |
| input_ship | Scope to the ship input in a treaty article | ship |
| input_state | Scope to the state input in a treaty article | state |
| input_strategic_region | Scope to the strategic region input in a treaty article | strategic_region |
| second_country | Scope to the second_country of any of: diplomatic pact treaty treaty options treaty article's treaty treaty article options (for mutual article types only) | country |
| shipping_lane | Scope to the shipping lane for the military formation, or treaty article (goods transfer) | shipping_lanes |
| source_country | Scope to the source_country of any of: treaty article (for directed article types only) treaty article options (for directed article types only) | country |
| target_country | Scope to the target_country of any of: treaty article (for directed article types only) treaty article options (for directed article types only) | country |
| treaty | Scope to the treaty a treaty article belongs to | treaty |

| Event target | Description | To scope |
|---|---|---|
| first_country | Scope to the first_country of any of: diplomatic pact treaty treaty options treaty article's treaty treaty article options (for mutual article types only) | country |
| input_building_type | Scope to the building type input in a treaty article | building_type |
| input_company | Scope to the company input in a treaty article | company |
| input_country | Scope to the country input in a treaty article | country |
| input_goods | Scope to the goods input in a treaty article | goods |
| input_law | Scope to the law input in a treaty article | law_type |
| input_market_goods | Scope to the market goods input in a treaty article (example: input_market_goods:root) | market_goods |
| input_quantity | Scope to the quantity input in a treaty article | value |
| input_ship | Scope to the ship input in a treaty article | ship |
| input_state | Scope to the state input in a treaty article | state |
| input_strategic_region | Scope to the strategic region input in a treaty article | strategic_region |
| second_country | Scope to the second_country of any of: diplomatic pact treaty treaty options treaty article's treaty treaty article options (for mutual article types only) | country |
| source_country | Scope to the source_country of any of: treaty article (for directed article types only) treaty article options (for directed article types only) | country |
| target_country | Scope to the target_country of any of: treaty article (for directed article types only) treaty article options (for directed article types only) | country |

### War scope

| Event target | Description | To scope |
|---|---|---|
| attacker_warleader | Scope to the attacker warleader of a war | country |
| defender_warleader | Scope to the defender warleader of a war | country |
| diplomatic_play | Scope from a war to its diplomatic play | diplomatic_play |

## All event targets

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
| amendment_type | Scope to an amendment type from its name (amendment_type:key) | none | amendment_type |
| army_size | Number of battalions of scope country, excluding currently raised conscripts. | country | value |
| army_size_including_conscripts | Number of battalions of scope country, including currently raised conscripts. | country | value |
| army_size_including_raised_conscripts | Number of battalions of scope country, including currently raised conscripts but excluding unraised conscripts. | country | value |
| array_define | Reference the value of a numeric value in an array define: array_define:Namespace\|Name\|Index. Index is 0-based. | none | value |
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
| bg | Scope to a building group from its name (bg:bg_logging) | none | building_group |
| binding_period | Get the original binding period in days when the treaty was signed for the scoped treaty | treaty, treaty_options | value |
| bt | Scope to a building type, example: bt:building_tooling_workshops | none | building_type |
| building | Scope to the related building | new_combat_unit | building |
| building_levels | Get the total number of non-subsistence building levels of the scoped country | country | value |
| c | Scope to the country with specified tag, example: c:GBR | none | country |
| cached_ai_coastal_population | Scope to total coastal population recorded in AI spending variables (example: value = cached_ai_coastal_population) | country | value |
| cached_ai_incorporated_coastal_population | Scope to total incorporated coastal population recorded in AI spending variables (example: value = cached_ai_incorporated_coastal_population) | country | value |
| cached_ai_incorporated_population | Scope to total incorporated population recorded in AI spending variables (example: value = cached_ai_incorporated_population) | country | value |
| cached_ai_overseas_subject_population | Scope to total population in direct non-adjacent subjects recorded in AI spending variables (example: value = cached_ai_overseas_subject_population) | country | value |
| cached_ai_subject_population | Scope to total population in direct subjects recorded in AI spending variables (example: value = cached_ai_subject_population) | country | value |
| cached_ai_total_population | Scope to total population recorded in AI spending variables (example: value = cached_ai_total_population) | country | value |
| cached_ai_unincorporated_coastal_population | Scope to total unincorporated coastal population recorded in AI spending variables (example: value = cached_ai_unincorporated_coastal_population) | country | value |
| cached_ai_unincorporated_population | Scope to total unincorporated population recorded in AI spending variables (example: value = cached_ai_unincorporated_population) | country | value |
| capital | Scope to the capital state of a country | country | state |
| catalyst_type | Scope to a diplomatic catalyst type from its name (catalyst_type:catalyst_relations_level_improved) | none | diplomatic_catalyst_type |
| cd | Scope to the country definition with specified tag, example: cd:FRA | none | country_definition |
| civil_war | Scope to the civil war started by the scoped (revolutionary) political movement. | political_movement | civil_war |
| civil_war_origin_country | Scope to the origin country of a civil war country | country | country |
| colonial_growth_per_colony | Scope to the country's colonial growth per colony value (example: colonial_growth_per_colony > 0) | country | value |
| combat_width | Scope to combat width multiplier of scope province | province | value |
| command_limit_num_units | Get the baseline number of units from their military formation a commander would normally get, depending on their command limit | character | value |
| commander | Scope from a military formation to its commander character | military_formation | character |
| commander_military_formation | Scope to the Military Formation of a Character. | character | military_formation |
| company | Scope to the scoped country's company of the named company type (company:company_rheinmetall) | country | company |
| company_type | Scope to a company type from its name (company_type:company_rheinmetall) | none | company_type |
| compare_complex_value | A comparison trigger that needs a parsable string parameter that will return its value in the context it is used eg: scope:root.number_of(armies) | varies | value |
| compare_value | A comparison trigger that will return its value in the context it is used eg: root.gold | varies | value |
| controller | Scope to the controller of the object | province, state | country |
| country | Scope to the country of a military formation or ship | military_formation, ship | country |
| country_definition | Scope to country's definition | country | country_definition |
| credit | Scope to the current amount of max credit the country can take | country | value |
| cu | Scope to the culture with specified key, example: cu:welsh | none | culture |
| culture | Scope to pop's or character's culture | character, new_combat_unit, political_movement, pop | culture |
| current_hq | Returns the current HQ of the scoped military formation (may not be valid if the formation is not currently stationed in an HQ) | military_formation | hq |
| currently_active_law_in_group | Scope from a law to the currently active law in that group | law | law |
| currently_enacting_law | Scope from a country to the law that they're currently enacting | country | law |
| decree_cost | Scope to a state's cost for a certain decree authority > decree_cost:decree_road_maintaintenance | state | value |
| defender_side | Scope from a battle to the BattleSide corresponding to the defender | battle | battle_side |
| defender_warleader | Scope to the defender warleader of a war | war | country |
| defense | Returns the unit's defense rating (including impact from their commander) | new_combat_unit | value |
| define | Reference the value of a numeric or color define: define:Namespace\|Name | none | value |
| demoralized | Returns the unit's number of demoralized manpower | new_combat_unit | value |
| detection | Links from a fleet scope to the total detection of the ships in the fleet | military_formation | value |
| diplomatic_pact_expense_ratio | Scope to the ratio of diplomatic pact expenses to income for this country, clamped 0-1 (example: value = diplomatic_pact_expense_ratio) | country | value |
| diplomatic_pact_other_country | Scope to the other country of the diplomatic pact in scope, example: diplomatic_pact_other_country(root) | diplomatic_pact | country |
| diplomatic_play | Scope from a war to its diplomatic play | war | diplomatic_play |
| enforced_on_country | Scope to the enforced_on_country of an enforced treaty | treaty | country |
| enforcer_country | Scope to the enforcer_country of an enforced treaty | treaty | country |
| executive | Scope from a company to its executive character | company | character |
| first_country | Scope to the first_country of any of: diplomatic pact treaty treaty options treaty article's treaty treaty article options (for mutual article types only) | diplomatic_pact, treaty, treaty_article, treaty_article_options, treaty_options | country |
| flag | A localization key, ex. flag:the_boss | none | flag |
| flagship | Get the flagship of the scoped country | country | ship |
| front | Scope to a front from various scopes From a battle to the front where it takes place From a character to the front where they are at or travelling towards From a military formation to the front it is currently at From a province to the front that contains it From an invasion to the invasion front | battle, character, invasion, military_formation, province | front |
| front_length | Returns the number of provinces in Front | front | value |
| g | Scope to the goods with specified key, example: g:iron | none | goods |
| gdp | Get the scoped country's yearly predicted GDP | country, state | value |
| get_ruler_for | Scopes from country to a character that would be ruler, under the given transfer of power type get_ruler_for:parliamentary_elective = { effects... } | country | character |
| global_gdp | Get the global yearly predicted GDP | none | value |
| global_productivity | Scope to global productivity values (example: global_productivity:high_threshold) | none | value |
| global_var | Reference a previous set global variable via its name eg: global_var:important_thing | none | varies |
| goal_value | Scope to the journal entry's goal value | journal_entry | value |
| goods | Scope to the goods traded by a trade route | market_goods, state_goods | goods |
| government_size | Get the scoped country's current number of Parties & independent IGs in government | country | value |
| group | Scope from a building object or type to its group | building, building_type | building_group |
| harvest_condition_type | Scope to a harvest condition type from its name (harvest_condition_type:drought) | none | harvest_condition_type |
| heir | Scope to the heir of a country | country | character |
| home_country | Scopes to the home country of an exile | character, pop | country |
| home_hq | Returns the home HQ of the scoped military formation | military_formation | hq |
| i | Scope to ideology specified by key, example: i:ideology_patriarchal | none | ideology |
| identity | Scope to the power bloc identity from its name (identity:key) | none | power_bloc_identity |
| ideology | Dual use Scope to a ideology from its name (ideology:ideology_anarchist) Scope to the ideology of the scoped character | character, none | ideology |
| ig | Scope to the interest group of specified key belonging to the country, example: ig:ig_armed_forces | country, political_movement | interest_group |
| ig_trait | Scope to the Interest Group trait with specified key, example: ig_trait:ig_trait_xenophobia | none | interest_group_trait |
| ig_type | Scope to an interest group type, example: ig_type:ig_landowners | none | interest_group_type |
| imposed_law | Scope from a country to the law currently imposed on them (enacting or not) | country | law |
| imposer_of_law | Scope from a country to the country currently imposing a law on them | country, law | country |
| income | Get the current weekly income of the scoped country | country | value |
| income_transfer_expenses | Scope to the amount of money scope country is transferring to other countries via treaties & pacts (example:income_transfer_expenses >= 100) | country | value |
| income_transfer_relative_expenses | Scope to the fraction of their income country is transferring to other countries via treaties & pacts (example:income_transfer_relative_expenses >= 0.2) | country | value |
| infamy | Scope to infamy of scope country (example: infamy >= 2) | country | value |
| infamy_threshold | Scope to infamy level threshold for comparison purposes (infamy_threshold:infamous) | none | value |
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
| lobby_type | Scope to a political lobby type from its name (lobby_type:lobby_pro_country) | none | political_lobby_type |
| lobby_war_opposition | Scope to the total clout of all lobbies that oppose the scoped war (lobby_war_opposition:root >= 0.2) | country | value |
| lobby_war_support | Scope to the total clout of all lobbies that support the scoped war (lobby_war_support:root >= 0.2) | country | value |
| local_var | Reference a previous set local variable via its name eg: local_var:person_of_interest | none | varies |
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
| mobilization_option | Scope to a mobilization option from its name (mobilization_option:key) | none | mobilization_option |
| modifier | Scope to the value of the modifier type of specified key belonging to the current object, example: modifier:country_influence_add | battle_side, building, character, country, interest_group, market, power_bloc, state | boolean, value |
| momentum | Get the scoped party's raw momentum | party | value |
| morale | Returns the unit's morale | new_combat_unit | value |
| most_desired_law | Scope to the law type that political movement most desires to be enacted (if any). | political_movement | law_type |
| movement_type | Scope to a political movement type from its name (movement_type:movement_religious_majority) | none | political_movement_type |
| mutual_trade_value_with_country | Scope to the total base value of goods traded in trade routes between the two markets (example: mutual_trade_value_with_country:root >= 1000) | country | value |
| named_script_value | A script value that will calculate and returns its value in the context it is used | none | color, value |
| national_awakening_state_region | Links from a culture scope to the state region with an active national awakening for that culture | culture | state_region |
| naval_combat_power | Scope to the country's navy combat power (example: naval_combat_power > 100) | country | value |
| naval_controller_hq | Returns the province or state controller navy HQ | province | hq |
| naval_hostility_average_damage_dealt | Scope to average damage dealt by this country in naval hostilities it initiated over the lookback period. Returns -1 if no hostilities found. | country | value |
| naval_hostility_damage | Scope to damage points inflicted by this country against another in active naval hostilities (example: naval_hostility_damage:root >= 50) | country | value |
| naval_hq | Returns the province or state owner local navy HQ | province | hq |
| naval_vulnerability | Scope to a country's naval vulnerability score based on trade reliance and coastal GDP share, capped at a define maximum | country | value |
| navy_size | Number of flotillas of scope country. | country | value |
| nf | Scope to a Decree of specified key applied to the state, example: nf:decree_road_maintaintenance | state | decree |
| no | Boolean literal for false values | none | boolean |
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
| num_ships_of_group | Number of ships of the provided ship group in the scoped country or military formation | country, military_formation | value |
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
| p | Scope to province specified by hex key, example: p:x1A6E5B | none | province |
| parent_law_type | Links from an amendment scope to the law type that is considered the amendment's parent | amendment | law_type |
| participants | Get the total number of participating countries in the scoped market | market | value |
| party | Scope to the party that an IG is supporting | interest_group | party |
| pirated_trade_value_by | Scope to the average weekly base value of goods pilfered from this country by a target country (example: pirated_trade_value_by:root >= 50) | country | value |
| play_type | Scope to a diplomatic play type from its name (play_type:dp_default_treaty_article) | none | diplomatic_play_type |
| player | Scope to the player (do not use this outside tutorial) | none | country |
| player_owed_obligation_days_left | Scope to number of days left on an obligation in diplomatic relations scope (example: obligation_days_left >= 2) | diplomatic_relations | value |
| political_movement | If used in a character scope, scope to the political movement that character supports. If used in a revolution civil war scope, scope to the movement that started the revolution. If used in an interest group scope, scope to the group's dominant movement. | character, civil_war | political_movement |
| pop_type | Scope to a pop type from its name (pop_type:laborers) | none | pop_type |
| pop_weight_modifier_scale | Get the Pop's weight modifier scale multiplier | pop | value |
| popularity | Get the scoped character's popularity, normally ranging between -100 and +100 | character | value |
| population_below_expected_sol | Scope to the current percentage of the state's population that are below their expected standard of living (0-1) | state | value |
| power_bloc | Scope to the power bloc for the scoped country | country | power_bloc |
| power_bloc_leader | Scope to the leader country of the scoped power bloc | power_bloc | country |
| power_projection | Get the power projection value of the scoped formation, unit, or ship | military_formation, new_combat_unit, ship | value |
| power_struggle_contender | Scope to the contender country if there is a power struggle | power_bloc | country |
| prev | The previous scope | none | varies |
| principal | Get the current debt principal of the country | country | value |
| principle | Scope to the power bloc principle from its name (principle:key) | none | power_bloc_principle |
| principle_group | Scope to the power bloc principle group from its name (principle_group:key) | none | power_bloc_principle_group |
| prosperity | Scope to the amount of prosperity for scope company (example: prosperity >= 2) | company | value |
| province | Scope from a battle side to the province in which the battle is being fought | battle_side | province |
| py | Scope to the active party of specified key belonging to the country, example: py:communist_party | country | party |
| rank_value | Scope to rank value of a particular country rank (rank_value:great_power) | none | value |
| region | Scope to the strategic region of the object! | building, diplomatic_play, hq, interest_marker, province, state, state_region | strategic_region |
| region_state | Scope to the state owned by the target country, (example: region_state:BIC) | state_region | state |
| rel | Scope to the religion with specified key, example: rel:catholic | none | religion |
| relations | Scope to relations between two countries (example: relations:root >= 2) | country | value |
| relations_change_rate | Scope to daily change in relations progress between two countries (example: relations_change_rate:root > 0) | country | value |
| relations_threshold | Scope to relations threshold level for comparison purposes (relations_threshold:warm) | none | value |
| religion | Scope to country or country definition's primary religion or pop religion | character, country, country_definition, political_movement, pop | religion |
| remaining_binding_period | Get the current remaining binding period in days for the scoped treaty | treaty, treaty_options | value |
| required_construction | Get the required amount of construction for scope building type | building_type | value |
| root | The head of the current top scope eg: receiver of an event, taker of a decision | none | varies |
| ruler | Scope to the ruler of a country | country | character |
| s | Scope to state region specified by key, example: s:STATE_UTAH | none | state_region |
| scope | Reference a previously saved scope via its name eg: scope:target | none | varies |
| scope_relations | Scope to relations value in diplomatic relations scope (example: scope_relations >= 2) | diplomatic_relations | value |
| scope_tension | Scope to tension value in diplomatic relations scope (example: scope_tension >= 2) | diplomatic_relations | value |
| screening | Links from a fleet scope to the total screening of the ships in the fleet | military_formation | value |
| second_country | Scope to the second_country of any of: diplomatic pact treaty treaty options treaty article's treaty treaty article options (for mutual article types only) | diplomatic_pact, treaty, treaty_article, treaty_article_options, treaty_options | country |
| sg | Scope from a state to the StateGoods with the specified key, example: sg:wood | state | state_goods |
| ship_fleet | Links from a ship scope to the ship fleet | ship | military_formation |
| ship_group | Scope from a ship to its group or Scope to a ship group from its name (ship_group:ship_group_capital_ships) | none, ship | ship_group |
| ship_type | Scope to a ship type from its name (ship_type:ship_type_frigate) | none | ship_type |
| shipping_lane | Scope to the shipping lane for the military formation, or treaty article (goods transfer) | military_formation, treaty_article | shipping_lanes |
| slaves_role | Scope from building type to its slaves role pop type | building_type | pop_type |
| source_country | Scope to the source_country of any of: treaty article (for directed article types only) treaty article options (for directed article types only) | treaty_article, treaty_article_options | country |
| sponsor | Links from an amendment scope to the interest group that sponsored the amendment | amendment | interest_group |
| sr | Scope to the strategic region of specified key, example: sr:region_persia | none | strategic_region |
| state | Scope to the state of the object | building, market, pop, province | state |
| state_region | Scope to the state region of a state | state | state_region |
| strait_trade_importance_by | Scope to the trade importance of goods this country is trading through straits controlled by a target country. Accumulated value is multiplied by STRAIT_FULL_CONTROL_TRADE_IMPORTANCE_MULT for straits where the controller controls both sides (example: strait_trade_importance_by:root >= 100) | country | value |
| strait_type | Scope to a strait type from its name (strait_type:key) | none | strait_type |
| target | Scope to the target of the object | diplomatic_catalyst, diplomatic_play, journal_entry, political_lobby | varies |
| target_country | Scope to the target_country of any of: treaty article (for directed article types only) treaty article options (for directed article types only) | treaty_article, treaty_article_options | country |
| technology_being_researched | Scope to the current technology a country is researching | country | technology |
| techs_researched | Scope to the current amount of techs researched of a country | country | value |
| tension | Scope to tension between two countries (example: tension:root >= 2) | country | value |
| tension_threshold | Scope to tension level threshold for comparison purposes (tension_threshold:warm) | none | value |
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
| unit_type | Scope to a combat unit type from its name (unit_type:key) | none | combat_unit_type |
| value | A numeric literal value eg: 1, 5.2, -6 | none | value |
| var | Reference a previous set variable in scope via its name eg: var:mortal_enemy | varies | varies |
| visibility | Links from a fleet scope to the total visibility of the ships in the fleet | military_formation | value |
| vulnerability | Links from a fleet scope to the total vulnerability of the ships in the fleet | military_formation | value |
| war | Scope from a diplomatic play to its war | diplomatic_play | war |
| weekly_prosperity_change | Scope to the weekly prosperity change for scope company (example: weekly_prosperity_change >= 2) | company | value |
| workplace | Scope to the workplace of a pop | pop | building |
| world_market_hub | Scope to the world market hub state associated with the scoped state | state | state |
| yes | Boolean literal for true values | none | boolean |

## References

---

- To update these tables, see [Module:Script docs/Event targets](https://vic3.paradoxwikis.com/Module:Script_docs/Event_targets)

Modding
Return to top
| Documentation | [Defines](Defines.md) • [Effects](Effect.md) • Event targets • [Scopes](Scope.md) • [Triggers](Trigger.md) [Macros](Macro.md) • [Modifier types](Modifier types.md) • [On actions](https://vic3.paradoxwikis.com/On_actions) • [Script value](Script value.md) • [Variables](Variable.md) |
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
