---
title: Character modding
source: https://vic3.paradoxwikis.com/Character_modding
pageid: 6734
categories: [Potentially_outdated, 1.11, Modding]
fetched: 2026-10-27
---
Please help with verifying or updating older sections of this article. At least some were last verified for [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) 1.11.

Characters
**Game folder The folder where the files for this type are stored. :** `common/character_templates`

---

**Injectable Can INJECT database functions be used with this type? :** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) yes **Replaceable Can REPLACE database functions be used with this type? :** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) yes

---

**Related game objects:** Character traits, Character roles, Ideologies

[Characters](Character.md) are defined either with character templates in /common/character_templates/ or the `create_character` [effect](Effect.md). Starting characters are found in /common/history/characters/, and many characters are defined in events or other effects as well.

Character templates can be used with the `create_character` effect to generate characters, or they can appear semi-randomly if a usage block is defined.

## Character templates

Character templates are defined in /common/character_templates/, as an example:

```
usa_rockefeller_character_template = {
    first_name = John
    last_name = Rockefeller
    historical = yes
    dna = dna_john_d_rockefeller
    culture = cu:yankee
    female = no
    religion = rel:protestant
    ideology = ideology_moderate
    interest_group = ig_industrialists
    birth_date = 1839.6.8
    traits = {
        ambitious
        persistent
        basic_entrepreneur
    }
    executive_usage = {
      country_trigger = {
        exists = c:USA
        this = c:USA
      }
      company_trigger = {
        is_company_type = company_type:company_standard_oil
      }
      earliest_usage_date = 1875.1.1
      latest_usage_date = 1915.1.1
      chance = 100
    }
    commander_usage = {
      country_trigger = {
        exists = c:USA
        this = c:USA
      }
      role = general
      earliest_usage_date = 1836.1.1
      latest_usage_date = 1860.1.1
      chance = 75
    }
}
```

| Parameter | Function | Example | Required |
|---|---|---|---|
| template_key | Unique template identifier | usa_rockefeller_character_template | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |
| first_name | Character's first name, points to a localization key Set to culture for a random name from character's culture | first_name = John | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |
| last_name | Character's last name, points to a localization key Set to culture for a random name from character's culture | last_name = Rockefeller | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |
| historical | Indicates the character is historical | historical = yes | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| dna | Refers to a defined character appearance | dna = dna_string | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| female | Sets character as female, defaults to male | female = yes | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| culture | Sets character's culture Use primary_culture or ig_before_primary_culture if not using a specific culture | culture = cu:yankee | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |
| religion | Sets character's religion Defaults to religion of character's culture | religion = rel:protestant | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| age | Sets character's age at generation | age = 36 | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| birth_date | Sets character's birth date, calculating age at generation Overrides age | birth_date = 1812.1.1 | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| interest_group | Sets interest group affiliation | interest_group = ig_devout | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| ideology | Sets character's ideology | ideology = ideology_moderate | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| traits | Sets predefined traits | traits = { cautious } | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| trait_generation | Generates traits on character generation | trait_generation = { effects } | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| commander_rank | Sets a commanders rank on generation Use default or a scripted rank | commander_rank = commander_rank_2 | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| ruler | Sets character as ruler when generated | ruler = yes | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| heir | Sets character as heir when generated | heir = yes | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| ig_leader | Sets character as interest group leader when generated | ig_leader = yes | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| is_general | Sets character as a general when generated | is_general = yes | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| is_admiral | Sets character as an admiral when generated | is_admiral = yes | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| is_agitator | Sets character as an agitator when generated | is_agitator = yes | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| on_created | Runs effects on the character when generated | on_created = { effects } | ![No](/images/thumb/0/04/No.png/24px-No.png) |

Character templates can include one or more **usage** blocks, which allow the template to be used as a randomly generated character, rather than generating the character by effect. Once a template has been generated by a usage block or `create_character`, it cannot be generated by a usage block again.

| Main parameters | Function |  |  |
|---|---|---|---|
| interest_group_leader_usage | Sets character as a potential randomly generated interest group leader |  |  |
| agitator_usage | Sets character as a potential randomly generated agitator |  |  |
| commander_usage | Sets character as a potential randomly generated commander |  |  |
| executive_usage | Sets character as a potential randomly generated executive |  |  |
| Sub parameters | Sub-parameter of | Function | Required |
| country_trigger | any main parameter | Trigger in country scope to determine if usage is valid | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| interest_group_trigger | interest_group_leader_usage agitator_usage | Trigger in interest group scope to determine if usage is valid | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| company_trigger | executive_usage | Trigger in company scope to determine if usage is valid | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| role | commander_usage | Determines role type, `admiral` or `general` | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |
| earliest_usage_date | any main parameter | Sets earliest date usage block is valid | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |
| latest_usage_date | any main parameter | Sets earliest date usage block is valid | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |
| chance | any main parameter | Sets chance (from 0-100) of template being used on next valid generation | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |

### Character names

See also:
Localization
**NOTE:** All text presented to the player *must* be done through localization keys. Unlocalized character names default to a random name from the character's culture.

Base game character names are defined in /Victoria 3/game/localization/<language>/names_l_<language>.yml; new character names can be defined in any localization file. Character names can be assigned to [cultures](Culture modding.md), or used only for specific character templates.

### Ruler Selector

Adding characters to the ruler selector can be somewhat finicky. `is_for_ruler_selector = yes` is required. It seems to also be necessary that your characters be set to an IG leader with an `interest_group_leader_usage` block if you wish for them to appear in the selector.

## Character roles

TBA

## Create character effect

The [effect](Effect.md) `create_character` can use a defined character template, define a character using the same parameters as character templates, or use a template then modify it with additional parameters.

## Character history

Starting characters can be found at /common/history/characters/. They can be created from templates or direct definitions in `create_character`

## Character traits

Character traits
**Game folder The folder where the files for this type are stored. :** `common/character_traits`

---

**Icon folder The folder where base game icons for this type typically go. :** `gfx/interface/icons/character_trait_icons`

---

**Injectable Can INJECT database functions be used with this type? :** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) yes **Replaceable Can REPLACE database functions be used with this type? :** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) yes

---

**Related game objects:** Characters

Character traits are defined in /common/character_traits/

When adding modded traits instead of modifying existing vanilla traits, create a new file.

```
notorious = {
  type = condition                            # Can be one of personality, skill, or condition. Each category is limited by defines. Random traits can be applied based on a particular type.
  texture = "gfx/interface/icons/character_trait_icons/direct.dds"  # The trait's texture asset

  character_modifier = {                      # Applies to the Character regardless of role
    character_popularity_add = 25
  }

  command_modifier = {                        # Applies to the Character, their Military Formation, and any Combat Units under the Character's command, assuming the unit is fully Mobilized (or does not need to Mobilize)
    unit_kill_rate_mult = 0.1
  }
  
  country_modifier = {                        # Applies to the Character's Country if they are the Ruler of it
    state_turmoil_mult = 0.1
  }
  
  agitator_modifier = {
    political_movement_radicalism_add = 0.15  # Applies to the Character's Political Movement
  }
    
  interest_group_modifier = {                 # Applies to the Character's Interest Group if they are the Leader of it
    interest_group_pol_str_mult = -0.05
    interest_group_pop_attraction_mult = 0.1
  }

  executive_modifier = {                      # Applies to the Character's Company if they are the Executive of it
    building_cash_reserves_mult = -0.1
  }

  possible = {                                # Used to determine if this trait is a valid random choice
    popularity < 0                            # Does NOT impact the validity of the trait once it's acquired
  }

  weight = {                                  # Script value to determine how likely it is the character will randomly get this trait, compared to other traits in its category. Default 1
    value = popularity
    multiply = -1
  }

  replace = {                                 # When the character gains this trait, any traits they have in the following list are removed
    famous
    wicked
  }

  value = 2                                   # How much this trait is "worth" in experience levels traits. Default 1
                                              # Used to determine whether the character is owed more traits, and which trait category is overrepresented
}
```

### Trait localization

See also:
Localization
Traits generate two localization keys: `<trait_name>` and `<trait_name>_desc`, for the name and flavor description.

## Character script documentation

The following [effects](Effect.md), [event targets](Event target.md), and [triggers](Trigger.md) can be used in character scope.

| Effect | Description | Example | Targets |
|---|---|---|---|
| add_career_length | Adds to a character's current career length in a role. Role can be a specific database role or a role type (e.g. general). If no role is specified, applies to all roles with career end dates. | add_career_length = { role = role_key/role_type days/months/years = 5 random_range = { 0.8 1.2 } } |  |
| add_character_role | Adds a new role to a character, works with either archetype or database role | add_character_role = general/character_role_general |  |
| add_commander_rank | Promotes/demotes a character a given amount of military ranks | add_commander_rank = integer |  |
| add_experience | Adds an amount of experience to a commander | add_experience = 0.2 |  |
| add_modifier | Adds a timed modifier effect to object in scope | add_modifier = { name = static_modifier_name days/weeks/months/years = value (optional) #can use scripted values, negative values are permanent multiplier = value (optional) #multiplies the values of the static modifier is_decaying = yes (optional) #sets modifier to decay in strength over its duration } add_modifier = static_modifier_name #set as permanent modifier with no multiplier or decay |  |
| add_random_trait | Adds a random qualifying Trait of the specified category | add_random_trait = personality / skill / condition |  |
| add_trait | Add a trait to a Character | add_trait = trait |  |
| change_character_culture | Changes the culture of the scoped character | change_character_culture = cu:colombian | culture |
| change_character_religion | Changes the religion of the scoped character | change_character_religion = rel:protestant | religion |
| disinherit_character | Strips the scoped character of their heir status in whichever countries apply. | scope:larry = { disinherit_character = yes } |  |
| every_character_role | Iterate through all roles of the scoped character | every_character_role = { limit = { <triggers> } #optional <effects> } | character_role |
| exile_character | Exile a character to the exile pool | exile_character = yes |  |
| free_character_from_void | Frees a character from the void, if set to no character is deleted instead | free_character_from_void = yes |  |
| kill_character | Kill a character | kill_character = bool (yes - kill [by default], no - don't do anything) kill_character = { hidden = bool (yes - without notification; no - show notification [by default]) value = bool (yes - kill [by default], no - don't do anything) } |  |
| ordered_character_role | Iterate through all roles of the scoped character | ordered_character_role = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | character_role |
| place_character_in_void | Banishes a character to the void, duration is how long character is kept before being deleted | place_character_in_void = months |  |
| random_character_role | Iterate through all roles of the scoped character | random_character_role = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | character_role |
| remove_as_interest_group_leader | Removes a character from position as interest group leader | remove_as_interest_group_leader = yes |  |
| remove_character_role | Removes an existing role from a character, works with either archetype or database role | remove_character_role = general/character_role_general |  |
| remove_modifier | Removes a timed modifier effect to object in scope | remove_modifier = static_modifier_name |  |
| remove_trait | Remove a trait from a Character | remove_trait = trait |  |
| replace_character_roles | Replaces existing role(s) from a character with another, works with either archetype or database role | replace_character_role = { add = { roles } remove = { roles } remove_all = no/yes } |  |
| set_as_adult | Turns the scoped character into an adult if they are not one already. | set_as_adult = yes |  |
| set_as_interest_group_leader | Sets a character as interest group leader | set_as_interest_group_leader = yes |  |
| set_career_length | Sets the career length from now for a character in a role. Role can be a specific database role or a role type (e.g. general). If no role is specified, applies to all roles with career end dates. | set_career_length = { role = role_key/role_type days/months/years = 10 random_range = { 0.8 1.2 } } |  |
| set_character_as_ruler | Set scoped character as ruler in their country. | scope:larry = { set_character_as_ruler = yes } CAUTION: Do not use this effect with chartered companies, as the character's country will be affected |  |
| set_character_busy_and_immortal | Mark a character as busy and immortal or clear said mark | set_character_busy = bool |  |
| set_character_immortal | Set scoped character as immortal or not. | scope:larry = { set_character_immortal = yes/no } |  |
| set_commander_rank | Promotes/demotes a character to a given military rank value | set_commander_rank = 3 |  |
| set_first_name | Changes the first name of a character to a loc key | set_first_name = loc_key |  |
| set_home_country | Set a character's home country. This makes them start considering themselves as having been exiled, i.e. was_exiled starts evaluating to yes for them. | set_home_country = c:FRA | country |
| set_home_country_definition | Set a character's home country directly to a tag, you can use this to avoid making sure that the tag exists, this makes them an exile | set_home_country_definition = cd:FRA | country_definition |
| set_home_state | Changes the home state of the scoped character | set_home_state = <state scope> | state |
| set_ideology | Changes scoped character's ideology | set_ideology = ideology:<ideology key> | ideology |
| set_interest_group | Sets the interest group of the character | set_interest_group = ruler.interest_group | interest_group |
| set_is_noble | Sets the noble flag of the scoped character. | set_is_noble = yes/no |  |
| set_last_name | Changes the last name of a character to a loc key | set_last_name = loc_key |  |
| transfer_character | Transfers current scope character to target country | transfer_character = country | country |
| transfer_to_formation | Transfers scope character to target formation | transfer_to_formation = scope:formation | military_formation |

| Trigger | Description | Example | Targets |
|---|---|---|---|
| age | Compares the character age | age > 20 | value |
| any_character_role | Iterate through all roles of the scoped character | any_character_role = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | character_role |
| any_scope_homeland_state | Iterate through all states that are a homeland for the scoped culture, or a homeland of any primary culture of the scoped country | any_scope_homeland_state = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | state |
| can_agitate | Check if the scope character can agitate the target country | can_agitate = <scope/c:TAG> | country |
| character_acceptance | Compares the acceptance of the scoped character in the target country against an acceptance value | character_acceptance = { target = c:FRA value > 50 } | value |
| character_supports_political_movement | Checks whether the scoped character supports a political movement | character_supports_political_movement = yes/no | boolean |
| commander_is_available | Check if a commander is not busy | commander_is_available = bool | boolean |
| commander_rank | Compares the commanders rank | commander_rank > 2 | value |
| could_support_political_movement | Check if a character could potentially support a political movement | could_support_political_movement = <scope> |  |
| experience_level | Compares the character experience level | experience_level > 1 | value |
| has_commander_order | Checks whether the scoped character is following the given order | has_commander_order = order type key/order type scope |  |
| has_culture | Checks characters culture | has_culture = culture scope or character scope |  |
| has_ideology | Check if scoped character or interest group has ideology |  |  |
| has_military_formation | Checks if character has a Military Formation | has_military_formation = bool | boolean |
| has_modifier | Check if a supported scope has a certain timed modifier | has_modifier = <key> |  |
| has_religion | Checks characters religion | has_religion = religion/character scope |  |
| has_role | Checks if character has specific role | has_role = role |  |
| has_role_of_type | Checks if character has a role of the specified archetype | has_role_of_type = archetype |  |
| has_template | Checks if character was made from the specified template | has_template = template_key |  |
| has_trait | Checks if character has specific trait | has_trait = trait |  |
| is_adult | Check if character is an adult | is_adult = bool | boolean |
| is_advancing_on_front | Checks if a commander is advancing on a front | is_advancing_on_front = <front scope> | front |
| is_attacker_in_battle | Checks if a Commander or Ship is attacker in a battle | is_attacker_in_battle = bool | boolean |
| is_busy | Check if character is busy | is_busy = bool | boolean |
| is_character_alive | Checks if the scoped character is alive | is_character_alive = bool | boolean |
| is_defender_in_battle | Checks if a Commander or ship is defender in a battle | is_defender_in_battle = bool | boolean |
| is_female | Check if character is female | is_female = bool | boolean |
| is_heir_of_own_country | Checks whether the scoped character is the heir in the country they live in | is_heir_of_own_country = yes / no | boolean |
| is_historical | Check if character is historical | is_historical = yes/no | boolean |
| is_immortal | checks if the scoped character is immortal | scope:abbath = { is_immortal = yes } | boolean |
| is_in_battle | Checks if a Commander or ship is engaged in battle | is_in_battle = bool | boolean |
| is_in_exile_pool | Checks whether the scoped character is in the exile pool | is_in_exile_pool = yes/no | boolean |
| is_in_void | Check if character is in the void | is_in_void = bool | boolean |
| is_interest_group_leader | Checks if character is the leader of their interest group | is_interest_group_leader = yes/no | boolean |
| is_interest_group_type | Checks if Interest Group is of a certain type Can also be used on characters directly | is_interest_group_type = x |  |
| is_monarch | Checks if character is a monarch of a country with hereditary succession | is_monarch = bool | boolean |
| is_noble | Check if character is a noble | is_noble = bool | boolean |
| is_on_front | Checks if a character or military formation has been assigned to a Front and has arrived there | is_on_front = yes/no | boolean |
| is_ruler_of_any_country | Checks if character is a ruler/head of state of any country | is_ruler_of_any_country = bool | boolean |
| is_ruler_of_other_country | Checks if character is a ruler/head of state of any country they don't live in | is_ruler_of_other_country = bool | boolean |
| is_ruler_of_own_country | Checks if character is a ruler/head of state of the country they live in | is_ruler_of_own_country = bool | boolean |
| law_enactment_stance | Compares the stance of the scoped character, movement or interest group has about enactment of the specified law compared to the current active law in the same group |  |  |
| law_stance | Compares the base stance of the scoped character, movement or interest group has about the specified law, ignoring the current active law in the same group |  |  |
| lifetime_piracy_income | Compares the lifetime piracy income of a character | lifetime_piracy_income >= 1000000 | value |
| loyalty | Compares the character loyalty | loyalty > 1 | value |
| primary_role | Checks if the character's primary role is the specified role | primary_role = role |  |
| prominence | Compares the character prominence | prominence > 1 | value |
| remaining_career_length | Checks if the character's remaining career length meets a duration threshold. Role can be a specific database role, a role type, or omitted to use the role furthest from career end. | remaining_career_length = { role = general years = 5 } | value |
| role_priority | Compares the priority of the character role | role_priority >= 10 | value |
| trait_value | Compares the character's total trait value | trait_value < experience_level | value |
| was_exiled | Checks whether the scoped character was exiled | was_exiled = yes/no | boolean |
| years_of_service | Compares the commander's years of service | years_of_service > 1 | value |

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

### Character modifier types

`character_` [modifier types](Modifier types.md) apply their effects to characters.

| Modifier type | Localization | Type | Format | Notes |
|---|---|---|---|---|
| character_advancement_speed_add | General Advancement Speed | additive | good |  |
| character_advancement_speed_mult | General Advancement Speed | multiplicative | percent, good |  |
| character_battle_condition_aggressive_maneuver_mult | Aggressive Maneuver Chance | multiplicative | percent, neutral |  |
| character_battle_condition_blunder_mult | Blunder Chance | multiplicative | percent, bad |  |
| character_battle_condition_broken_supply_line_mult | Broken Supply Line Chance | multiplicative | percent, bad |  |
| character_battle_condition_camouflaged_mult | Camouflaged Chance | multiplicative | percent, good |  |
| character_battle_condition_careful_maneuver_mult | Careful Maneuver Chance | multiplicative | percent, good |  |
| character_battle_condition_charted_terrain_mult | Charted Terrain Chance | multiplicative | percent, good |  |
| character_battle_condition_death_from_below_mult | Death from Below Chance | multiplicative | percent, good |  |
| character_battle_condition_dug_in_mult | Dug In Chance | multiplicative | percent, good |  |
| character_battle_condition_exhausted_mult | Exhausted Chance | multiplicative | percent, bad |  |
| character_battle_condition_good_visibility_mult | Good Visibility Chance | multiplicative | percent, good |  |
| character_battle_condition_guerilla_ambush_mult | Ambush Chance | multiplicative | percent, good |  |
| character_battle_condition_logistics_secured_mult | Logistics Secured Chance | multiplicative | percent, good |  |
| character_battle_condition_lost_mult | Lost Chance | multiplicative | percent, bad |  |
| character_battle_condition_mud_mult | Mud Chance | multiplicative | percent, bad |  |
| character_battle_condition_poor_visibility_mult | Poor Visibility Chance | multiplicative | percent, bad |  |
| character_battle_condition_ramming_maneuver_mult | Ramming Maneuver Chance | multiplicative | percent, neutral |  |
| character_battle_condition_rapid_advance_mult | Rapid Advance Chance | multiplicative | percent, good |  |
| character_battle_condition_rough_waters_mult | Rough Waters Chance | multiplicative | percent, neutral |  |
| character_battle_condition_strong_winds_mult | Strong Winds Chance | multiplicative | percent, neutral |  |
| character_battle_condition_surprise_maneuver_mult | Surprise Maneuver Chance | multiplicative | percent, good |  |
| character_blockade_mult | Admiral Blockade Strength | multiplicative | percent, good |  |
| character_command_limit_add | Command Limit | additive | good |  |
| character_command_limit_mult | Command Limit | multiplicative | percent, good |  |
| character_commander_loyalty_add | Commander Loyalty | additive | good |  |
| character_convoy_protection_mult | Admiral Merchant Marine Protection | multiplicative | percent, good |  |
| character_convoy_raiding_mult | Admiral Merchant Marine Raiding Efficiency | multiplicative | percent, good |  |
| character_coup_strength_add | Coup Strength | additive | neutral |  |
| character_coup_strength_mult | Coup Strength | multiplicative | percent, neutral |  |
| character_expedition_events_explorer_mult | Expedition Opportunity | multiplicative | percent, good |  |
| character_health_add | Character Health | additive | percent, good |  |
| character_interception_add | Admiral Interception Chance | additive | good |  |
| character_loyalty_add | Loyalty | additive | good |  |
| character_loyalty_mult | Loyalty | multiplicative | percent, good |  |
| character_max_offensive_battles_add | Max Offensive Battles | additive | good |  |
| character_naval_mission_area_add | Naval Mission Area Size | additive | good |  |
| character_piracy_goods_capacity_mult | Pirating Capacity | multiplicative | percent, good |  |
| character_popularity_add | Popularity | additive | good |  |
| character_prominence_add | Prominence | additive | neutral |  |
| character_raid_supply_add | Admiral Raid Supply Chance | additive | good |  |

### Character GUI script

Main article:
GUI script
| Function | Arguments | Output | Description |
|---|---|---|---|
| AccessBattle |  | Battle | Category: const |
| AccessCulture |  | Culture | Category: const |
| AccessInterestGroup |  | InterestGroup | Category: const |
| AccessOrders |  | Unknown | Category: const |
| AccessPossibleSpecialOrders |  | Unknown | Category: const |
| AccessReligion |  | Religion | Category: const |
| AccessSelf |  | Character | Category: const |
| AccessTraits |  | Unknown | Category: const |
| AccessUnavailableOrders |  | Unknown | Category: const |
| GetAcceptanceStatus |  | AcceptanceStatus | Category: nonconst |
| GetAcceptanceStatusIn | Country | AcceptanceStatus | Category: nonconst |
| GetAcceptanceValue |  | int32 | Category: nonconst |
| GetAcceptanceValueDesc |  | CString | Category: nonconst |
| GetAcceptanceValueDescIn | Country | CString | Category: nonconst |
| GetAcceptanceValueIn | Country | int32 | Category: nonconst |
| GetAge |  | int32 | Category: nonconst |
| GetAgitatorSpawnedNotificationText |  | CString | Category: nonconst |
| GetAllRoleNames |  | CString | Category: nonconst |
| GetAnimatedPortrait | PortraitEnvironment PortraitCamera PortraitAnimation CVector2f | Unknown | Category: nonconst |
| GetAssignedState |  | State | Category: nonconst |
| GetBattle |  | Battle | Category: nonconst |
| GetBirthday |  | CString | Category: nonconst |
| GetCombatUnitsTypeIcon |  | CString | Category: nonconst |
| GetCommandLimit |  | CString | Category: nonconst |
| GetCommandLimitDesc |  | CString | Category: nonconst |
| GetCommandLimitRaw |  | int32 | Category: nonconst |
| GetCommanderDetails |  | CString | Category: nonconst |
| GetCommanderRank |  | CommanderRank | Category: nonconst |
| GetCountry |  | Country | Category: nonconst |
| GetCulture |  | Culture | Category: nonconst |
| GetCustom | CustomLocalization | CString | Category: nonconst |
| GetDebugDesc |  | CString | Category: nonconst |
| GetFirstName |  | CString | Category: nonconst |
| GetFirstNameNoFormatting |  | CString | Category: nonconst |
| GetFirstNamePossessive |  | CString | Category: nonconst |
| GetFront |  | Front | Category: nonconst |
| GetFullName |  | CString | Category: nonconst |
| GetFullNameNoFormatting |  | CString | Category: nonconst |
| GetFullNamePossessive |  | CString | Category: nonconst |
| GetFullNameWithTitle |  | CString | Category: nonconst |
| GetFullNameWithTitleNoFormatting |  | CString | Category: nonconst |
| GetFullNameWithTitlePossessive |  | CString | Category: nonconst |
| GetGender |  | CString | Category: nonconst |
| GetGenderOpposite |  | CString | Category: nonconst |
| GetHerHim |  | CString | Category: nonconst |
| GetHerHimOpposite |  | CString | Category: nonconst |
| GetHerHis |  | CString | Category: nonconst |
| GetHerHisOpposite |  | CString | Category: nonconst |
| GetHerselfHimself |  | CString | Category: nonconst |
| GetHerselfHimselfOpposite |  | CString | Category: nonconst |
| GetHistoricalUrl |  | CString | Category: nonconst |
| GetHomeCountry |  | Country | Category: nonconst |
| GetHomeCountryDefinition |  | CountryDefinition | Category: nonconst |
| GetID |  | int32 | Category: nonconst |
| GetIDString |  | CString | Category: nonconst |
| GetIdeology |  | Ideology | Category: nonconst |
| GetInfoTooltip |  | CString | Category: nonconst |
| GetInteraction | Unknown | CharacterInteraction | Category: nonconst |
| GetInteractions |  | Unknown | Category: nonconst |
| GetInterestGroup |  | InterestGroup | Category: nonconst |
| GetInvasion |  | Invasion | Category: nonconst |
| GetLastName |  | CString | Category: nonconst |
| GetLastNameNoFormatting |  | CString | Category: nonconst |
| GetLastNamePossessive |  | CString | Category: nonconst |
| GetMilitaryFormation |  | MilitaryFormation | Category: nonconst |
| GetNextCommanderRank |  | CommanderRank | Category: nonconst |
| GetNextCommanderRankBenefits |  | CString | Category: nonconst |
| GetNextOrderType |  | CommanderOrderType | Category: nonconst |
| GetNumUnitsThatWouldBeSplitOff |  | int32 | Category: nonconst |
| GetOrderType |  | CommanderOrderType | Category: nonconst |
| GetPoliticalMovement |  | PoliticalMovement | Category: nonconst |
| GetPopularity |  | CFixedPoint | Category: nonconst |
| GetPopularityDesc |  | CString | Category: nonconst |
| GetPortrait | PortraitEnvironment PortraitCamera PortraitAnimation CVector2f | Unknown | Category: nonconst |
| GetPrimaryRoleName |  | CString | Category: nonconst |
| GetPrimaryRoleTitle |  | CString | Category: nonconst |
| GetPromoteCommand |  | Command | Category: nonconst |
| GetRankName |  | CString | Category: nonconst |
| GetRankNameFor | CommanderRank | CString | Category: nonconst |
| GetRankTitle |  | CString | Category: nonconst |
| GetRankTitleFor | CommanderRank | CString | Category: nonconst |
| GetRecruitCommand | MilitaryFormation | Command | Category: nonconst |
| GetReligion |  | Religion | Category: nonconst |
| GetRepairingTexture |  | Unknown | Category: nonconst |
| GetSheHe |  | CString | Category: nonconst |
| GetSheHeOpposite |  | CString | Category: nonconst |
| GetStrengthPointsIcon |  | CString | Category: nonconst |
| GetTimedModifiers |  | Unknown | Category: nonconst |
| GetTooltipTag |  | CString | Category: nonconst |
| GetTraitsDesc |  | CString | Category: nonconst |
| GetWomanMan |  | CString | Category: nonconst |
| GetWomanManOpposite |  | CString | Category: nonconst |
| HasAdvancingOrder |  | bool |  |
| HasInvasionPlan |  | bool |  |
| HasMilitaryFormation |  | bool |  |
| HasOrder | Unknown | bool |  |
| HasUnavailableAdvanceOrders |  | bool |  |
| HasUnavailableDefendOrders |  | bool |  |
| IsAdmiral |  | bool |  |
| IsAgitator |  | bool |  |
| IsAtFront |  | bool |  |
| IsAttackingInBattle |  | bool |  |
| IsBeingHighlighted |  | bool |  |
| IsBeingTutorialHighlighted |  | bool |  |
| IsBusy |  | bool |  |
| IsCommander |  | bool |  |
| IsDefeated |  | bool |  |
| IsDefendingInBattle |  | bool |  |
| IsExecutive |  | bool |  |
| IsFemale |  | bool |  |
| IsGeneral |  | bool |  |
| IsHeir |  | bool |  |
| IsHistorical |  | bool |  |
| IsIGLeader |  | bool |  |
| IsInBattle |  | bool |  |
| IsInExilePool |  | bool |  |
| IsMaxRank |  | bool |  |
| IsOffer |  | bool |  |
| IsPinnedInOutliner |  | bool |  |
| IsPolitician |  | bool |  |
| IsRetired |  | bool |  |
| IsRuler |  | bool |  |
| IsValid |  | bool |  |
| IsZoomingToOrderTarget |  | bool |  |
| MakeScope |  | Scope |  |
| OpenHistoricalUrl |  | void |  |
| PredictMovementToJoin | Unknown | PoliticalMovement |  |
| PredictMovementTypeToStart | Unknown | PoliticalMovementType |  |
| RecruitCharacter | Unknown | void |  |
| SelectOrder | CommanderOrderType | Command |  |
| Self |  | Character |  |
| SplitIntoOwnFormation |  | Command |  |
| TogglePinInOutliner |  | void |  |
| WillJoinMovementIfInvited | Country | bool |  |
| WillStartMovementIfInvited | Country | bool |  |
| ZoomToLocation |  | void |  |
| ZoomToOrderTarget |  | void |  |

| Function | Arguments | Output | Description |
|---|---|---|---|
| AccessSelf |  | CharacterInteraction | Category: const |
| ExecuteCommand | Character | void |  |
| GetClickSound |  | Unknown | Category: nonconst |
| GetCommandDesc | Character | CString | Category: nonconst |
| GetCooldownDesc | Character | CString | Category: nonconst |
| GetCooldownDuration | Character | CString | Category: nonconst |
| GetCooldownRemaining | Character | CString | Category: nonconst |
| GetDesc |  | CString | Category: nonconst |
| GetEffects | Character | CString | Category: nonconst |
| GetIcon |  | Unknown | Category: nonconst |
| GetInfo |  | CString | Category: nonconst |
| GetName |  | CString | Category: nonconst |
| GetRequirements | Character | CString | Category: nonconst |
| GetTooltipTag |  | CString | Category: nonconst |
| HasCooldown | Unknown | bool |  |
| HasIcon |  | bool |  |
| IsCommandValid | Character | bool |  |
| IsOnCooldown | Character | bool |  |
| Self |  | CharacterInteraction |  |
| ShouldShowRequirements |  | bool |  |

| Function | Arguments | Output | Description |
|---|---|---|---|
| AccessSelf |  | CharacterTrait | Category: const |
| AccessUnlockedOrders |  | Unknown | Category: const |
| GetDesc |  | CString | Category: nonconst |
| GetModifiers |  | CString | Category: nonconst |
| GetName |  | CString | Category: nonconst |
| GetNameNoFormatting |  | CString | Category: nonconst |
| GetTexture |  | Unknown | Category: nonconst |
| GetTooltipTag |  | CString | Category: nonconst |
| Self |  | CharacterTrait |  |

| Promote | Arguments | Output | Description |
|---|---|---|---|
| AccessBattle |  | Battle | Category: const |
| AccessCountry |  | Country | Category: const |
| AccessCulture |  | Culture | Category: const |
| AccessInterestGroup |  | InterestGroup | Category: const |
| AccessReligion |  | Religion | Category: const |
| GetAcceptanceStatus |  | AcceptanceStatus | Category: nonconst |
| GetAcceptanceStatusIn | Country | AcceptanceStatus | Category: nonconst |
| GetAssignedState |  | State | Category: nonconst |
| GetBattle |  | Battle | Category: nonconst |
| GetCommanderRank |  | CommanderRank | Category: nonconst |
| GetCountry |  | Country | Category: nonconst |
| GetCulture |  | Culture | Category: nonconst |
| GetFront |  | Front | Category: nonconst |
| GetHomeCountry |  | Country | Category: nonconst |
| GetHomeCountryDefinition |  | CountryDefinition | Category: nonconst |
| GetIdeology |  | Ideology | Category: nonconst |
| GetInteraction | CharacterInteraction | CharacterInteraction | Category: nonconst |
| GetInterestGroup |  | InterestGroup | Category: nonconst |
| GetInvasion |  | Invasion | Category: nonconst |
| GetMilitaryFormation |  | MilitaryFormation | Category: nonconst |
| GetNextCommanderRank |  | CommanderRank | Category: nonconst |
| GetNextOrderType |  | CommanderOrderType | Category: nonconst |
| GetOrderType |  | CommanderOrderType | Category: nonconst |
| GetPoliticalMovement |  | PoliticalMovement | Category: nonconst |
| GetReligion |  | Religion | Category: nonconst |
| MakeScope |  | Scope |  |
| PredictMovementToJoin | Country | PoliticalMovement |  |
| PredictMovementTypeToStart | Country | PoliticalMovementType |  |

## References

Modding
Return to top
| Documentation | [Defines](Defines.md) • [Effects](Effect.md) • [Event targets](Event target.md) • [Scopes](Scope.md) • [Triggers](Trigger.md) [Macros](Macro.md) • [Modifier types](Modifier types.md) • [On actions](https://vic3.paradoxwikis.com/On_actions) • [Script value](Script value.md) • [Variables](Variable.md) |
|---|---|

| Scripted content | [Decisions](Decision modding.md) • [Events](Event modding.md) • [History](History modding.md) • [Journal](Journal modding.md) • [Modifiers](Modifier modding.md) • Objectives • [Scripted gui](Scripted gui.md) |
|---|---|

| Scripted types | [Buildings](Building modding.md) • Characters • Concepts • [Countries](Country modding.md) • [Culture](Culture modding.md) • [Decrees](Decree modding.md) • [Diplomacy](Diplomacy modding.md) • [Goods](Goods modding.md) • [Institutions](Institution modding.md) • [Interest groups](Interest group modding.md) • [Laws](Law modding.md) • Parties • [Pops](Pop modding.md) • [Power blocs](Power bloc modding.md) • [Religion](Religion modding.md) • Subject types • [Technology](Technology modding.md) • [Treaties](Treaty modding.md) • [War goals](War goal modding.md) |
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
