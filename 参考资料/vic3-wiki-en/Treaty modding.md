---
title: Treaty modding
source: https://vic3.paradoxwikis.com/Treaty_modding
pageid: 7705
categories: [Potentially_outdated, 1.11, Modding]
fetched: 2026-10-27
---
Please help with verifying or updating older sections of this article. At least some were last verified for [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) 1.11.

See also:
Treaty
**Treaties** are diplomatic agreements between two countries. They can be negotiated diplomatically, or imposed by war. Each treaty is made up of one or more articles.

## Treaty defines

| Define | Default Value | Dev Comment |
|---|---|---|
| LAW_ENACTMENT_LAW_COMMITMENT_EFFECT | 0.05 | # Committing to enacting a law via treaty adds this much to pass chance, scaled by the number of ranks the country the comittee has on the committer |

| Define | Default Value | Dev Comment |
|---|---|---|
| TREATY_PROPOSAL_PENDING_APPROVAL_DAYS | 30 | # Number of days before a pending treaty proposal is auto-declined |
| TREATY_ARTICLE_COST_LOBBY_CLOUT_MULT | 0.01 | # Each point of clout from pro/anti-country lobbies reduces or increases the influence cost multiplier of maintaining treaty articles with them by this amount |
| TREATY_ARTICLE_COST_LOBBY_CLOUT_MAX | 0.5 | # Cost multiplier impact of pro/anti-country lobbies cannot be greater than this |
| MAX_TREATY_OBLIGATIONS_DELAY_DAYS | 3650 | # obligations promised as part of treaties take effect on binding period end, or once this amount of days has passed since the treaty was originally signed, whichever comes first [>= 0] |
| BINDING_PERIOD_THRESHOLD_TO_EFFECTUATE_TREATY_OBLIGATIONS_DAYS | 30 | # When binding period is this many days or less, obligations are effectuated |
| TREATY_ARTICLE_MONEY_TRANSFER_ARTICLE_TYPE | "money_transfer" |  |
| TREATY_ARTICLE_TREATY_PORT_ARTICLE_TYPE | "treaty_port" |  |
| TREATY_ARTICLE_INVESTMENT_RIGHTS_ARTICLE_TYPE | "foreign_investment_rights" |  |
| TREATY_ARTICLE_LAW_COMMITMENT_ARTICLE_TYPE | "law_commitment" |  |
| DEFAULT_WAR_REPARATIONS_MONEY_TRANSFER | 0.1 |  |
| TREATY_PROPOSAL_COOLDOWN_DAYS | 7 | # The number of days before you can send another treaty proposal after having one rejected |
| TREATY_DEFAULT_BINDING_DURATION_YEARS | 5 |  |
| TREATY_THREATEN_HOSTILITIES_DURATION_DAYS | 365 |  |
| THREATEN_NAVAL_HOSTILITIES_COOLDOWN_DAYS | 1825 | # 5 years before you can threaten naval hostilities against the same country again |
| NAVAL_HOSTILITIES_POINTS_MAX | 100 | # Maximum damage points that can be inflicted in a single instance of naval hostilities |
| NAVAL_VULNERABILITY_MAX | 1.0 | # Maximum naval vulnerability score. This is used to determine how afraid a country should be of naval hostilities. |
| NAVAL_VULNERABILITY_TRADE_MULTIPLIER | 0.75 | # Vulnerability from trade: this value * (trade base cost / GDP) = vulnerability points |
| NAVAL_VULNERABILITY_COASTAL_GDP_MULTIPLIER | 0.5 | # Vulnerability from coastal GDP: this value * (coastal GDP / GDP) = vulnerability points |
| NAVAL_VULNERABILITY_PRESTIGE_MULTIPLIER | 1.0 | # Vulnerability from naval prestige: this value * (navy prestige / total prestige) = vulnerability points |
| NAVAL_HOSTILITIES_POINTS_SHIPS_SUNK_AT_FULL_FLEET | 500 | # Damage points awarded when 100% of a country's fleet construction cost is sunk |
| NAVAL_HOSTILITIES_POINTS_BLOCKADE_GDP_WEEKLY | 20 | # Damage points per week when 100% of a country's GDP is blockaded |
| NAVAL_HOSTILITIES_POINTS_PIRACY_GDP_WEEKLY | 20 | # Damage points per week when 100% of a country's GDP in goods is seized via piracy |
| NAVAL_HOSTILITIES_POINTS_BOMBARDMENT_DEVASTATION | 20 | # Damage points per unit of devastation added, scaled by state GDP / victim GDP |
| NAVAL_HOSTILITIES_POINTS_BOMBARDMENT_BUILDING_DESTROYED | 10 | # Fixed damage points per building level destroyed by bombardment |
| PAST_TEMPORARY_HOSTILITIES_KEEP_YEARS | 20 | # Number of years to keep temporary hostilities data after expiry |
| PIRACY_DAMAGE_TRACKING_WEEKS | 26 | # Number of weeks of piracy damage history to keep for averaging |

| Define | Default Value | Dev Comment |
|---|---|---|
| DIPLO_PROPOSAL_DAYS_LEFT_MAX | 28 | # AI will not answer a proposal when it has more than this amount of days left (should map to DIPLOMATIC_ACTION_PENDING_APPROVAL_DAYS) |
| DIPLO_PROPOSAL_DAYS_LEFT_MIN | 20 | # AI will always answer a proposal when it has this or less amount of days left (should map to DIPLOMATIC_ACTION_PENDING_APPROVAL_DAYS) |
| DIPLO_PROPOSAL_ANSWER_CHANCE | 5 | # Chance per tick of AI answering a proposal (1 = 1%) |
| DIPLO_PROPOSAL_TO_PLAYER_COOLDOWN_MONTHS | 120 | # Do not make the same exact proposal to the player for this amount of months |
| DIPLO_PROPOSAL_LIKELY_NON_ACCEPTED_COOLDOWN_MONTHS | 120 | # When AI rolls the dice on whether or not to attempt a proposal it thinks will be rejected, don't try again for this time |
| DIPLO_PROPOSAL_LIKELY_NON_ACCEPTED_TREATY_COOLDOWN_MONTHS | 12 | # When AI fails to propose a treaty to another AI, wait this long before trying again with the same country |
| DIPLO_PROPOSAL_NO_OBLIGATION_COOLDOWN_MONTHS | 120 | # If the AI decides not to offer an obligation for a proposal, remember that decision for this many months |
| DIPLO_PROPOSAL_ACCEPT_THRESHOLD | 1 | # At this or more acceptance on a diplomatic action without uses_random_approval flag, AI says yes to a proposal. Each point above it increases chance to accept a uses_random_approval or treaty proposal |
| DIPLO_PROPOSAL_HALFWAY_RANDOM_ACCEPTANCE_THRESHOLD | 10 | # At this or more acceptance on a diplomatic action with uses_random_approval flag or treaty proposal, the AI has 50% chance to accept it and considers it to be accepted for the purpose of proposing it |
| DIPLO_PROPOSAL_GUARANTEED_RANDOM_ACCEPTANCE_THRESHOLD | 30 | # At this or more acceptance on a diplomatic action or treaty proposal with uses_random_approval flag, the AI will always accept it |
| DIPLO_PROPOSAL_BREAK_THRESHOLD | -100 | # At this or less acceptance, AI breaks off an existing pact |
| DIPLO_PROPOSAL_TRANSFER_PACT_RELUCTANCE | 25 | # Add this to acceptance value for existing pact in transfer-pact proposals |
| INFLUENCE_DEFICIT_RECOVER_INFLUENCE_BASE_VALUE | 50 | # Added to score for the treaty or pact we're breaking to recover influence |
| INFLUENCE_DEFICIT_RECOVER_INFLUENCE_RANDOM_FACTOR | 1.0 | # The higher this is, the more random AI pact/treaty breaking due to influence deficit will be |
| TRADE_VALUE_DELTA_FACTOR | 3.0 | # When calculating treaty trade value, the delta between production/consumption counts for this much more than base production/consumption values |
| TRADE_VALUE_BASE_MULTIPLIER | 0.001 | # Base multiplier applied to the value for treaty trade based purely on production & consumption |
| TRADE_VALUE_RELATIVE_MULTIPLIER | 100 | # Relative multiplier applied to the value for treaty trade and divided by the total value in the market |
| TREATY_FAIRNESS_BASE_SCORE | 10 | # The base score for treaty fairness before country acceptances are considered, treaties with an acceptance delta smaller than this will be considered fair to both parts |
| REJECTED_TREATY_MEMORY_DURATION_DAYS | 365 | # For how many days does the AI remember a rejected treaty and refuse any treaties that aren't a significant enough improvement on it |
| REJECTED_TREATY_MIN_ACCEPTANCE_IMPROVEMENT_FOR_NEW_PROPOSAL | 10 | # For the AI to have a chance to accept a treaty proposal after recently having rejected a treaty, the new proposal must be this much better than the old one |
| REJECTED_TREATY_UNDER_MIN_ACCEPTANCE_IMPROVEMENT_PENALTY | -1000 | # Added to accepance when a treaty proposal isn't sufficiently improved upon within the rejected treaty memory duration |
| # Treaties |  |  |
| TREATIES_RANDOM_FACTOR | 1.0 | # How random should the AI be regarding article selection when composing treaties? |
| TREATIES_CHECK_CATEGORIES_WHEN_COMPOSING_TREATY | no | # Does the AI care about categories when composing a treaty after gathering the initial article? |
| TREATIES_NUMBER_CHECKED_CATEGORIES_TREATY_COMPOSER | 3 | # How many categories does the AI try to gather to check against when composing a treaty |
| TREATIES_MINIMUM_ACCEPTANCE_TO_PROPOSE | 15 | # How much acceptance does the AI require the other side to have for it to try sending a proposal? 0 = never accept, 30 = always accept, in between = random chance |
| TREATIES_MINIMUM_OWN_ACCEPTANCE_TO_PROPOSE | 10 | # How much own acceptance does the AI require to have itself for it to send a proposal? |
| TREATIES_MAX_NUMBER_ARTICLES | 6 | # How many articles in a treaty the AI will consider at most |
| TREATIES_ACCEPTANCE_BASE | 0 | # Base Acceptance for Treaties |
| TREATIES_ACCEPTANCE_WITHDRAW_THRESHOLD | -50 | # Threshold at or under which AI will withdraw from treaties outside of their binding period |
| TREATIES_ACCEPTANCE_WITHDRAW_BINDING_PERIOD_THRESHOLD | -10000 | # Threshold at or under which AI will withdraw from treaties while they are still binding |
| TREATIES_DEFAULT_LENGTH_YEARS | 5 | # How long treaties the AI will propose |
| TREATY_OBLIGATION_WE_OWE_THEM_ACCEPTANCE | -40 | # How country A's acceptance of a treaty changes if A would owe B an obligation as part of the treaty. Note: "WE" is the country doing the evaluation, not the player |
| TREATY_OBLIGATION_THEY_OWE_US_ACCEPTANCE | 30 | # How country A's acceptance of a treaty changes if A would be owed an obligation by B as part of the treaty. Note: "US" is the country doing the evaluation, not the player |
| TREATY_OBLIGATION_THEY_OWE_US_RECENTLY_REPUDIATED_ACCEPTANCE | 15 | # Same as above, but use this if B has recently repudiated an obligation (A values it less because B's word is not worth as much) |
| TREATY_OBLIGATION_THEY_CALL_US_IN_ACCEPTANCE | 30 | # How country A's acceptance of a treaty changes if B is calling in an obligation that A owes B. Note: "US" is the country doing the evaluation, not the player |
| TREATY_OBLIGATION_THEY_CALL_US_IN_RECENTLY_REPUDIATED_ACCEPTANCE | 15 | # Same as above, but use this if B has recently repudiated an obligation (A values it less because they're less inclined to follow honor agreements that B is willing to ignore) |

| Define | Default Value | Dev Comment |
|---|---|---|
| # selection for the signing location of a treaty happens in two steps # 1. a state is randomly selected among up to 6, those 6 being: # - the capital (1) # - the state with higest gdp (1) # - the state with the second highest gdp (0 or 1) # - for both treaty participants # - single-state countries don't have a second highest gdp state # 2. once a state is randomly selected, a hub is randomly selected in the # state region that the state belongs to (if it applies, e.g. no ports # in landlocked state regions) # every random selection is weighted via the following weights |  |  |
| TREATY_SIGNING_STATE_WEIGHT_CAPITAL | 1 | # weight that states have when randomly chosing a signing place for a treaty [>= 1] |
| TREATY_SIGNING_STATE_WEIGHT_HIGHEST_GDP | 1 | # as above, for the state with the highest gdp [>=1] |
| TREATY_SIGNING_STATE_WEIGHT_SECOND_HIGHEST_GDP | 1 | # as above, for the state with the second highest gdp [>=1] |
| TREATY_SIGNING_HUB_WEIGHT_CITY | 5 | # weight that city hubs have when randomly chosing a signing place for a treaty [>= 1] |
| TREATY_SIGNING_HUB_WEIGHT_PORT | 3 | # as above, for port hubs [>= 1] |
| TREATY_SIGNING_HUB_WEIGHT_FARM | 2 | # as above, for farm hubs [>= 1] |
| TREATY_SIGNING_HUB_WEIGHT_MINE | 1 | # as above, for mine hubs [>= 1] |
| TREATY_SIGNING_HUB_WEIGHT_WOOD | 1 | # as above, for wood hubs [>= 1] |

## Treaty article definition

Treaty articles allow for deeper diplomatic interaction, and more importantly, allows modders to add wargoals. Each treaty article is defined in common/treaty_articles.

The basic elements in this definition are:

| Element | Options | Example | Description |
|---|---|---|---|
| kind | directed mutual | `kind = directed` | Kind of treaty article |
| cost | `value` | `cost = 100` | Influence cost to maintain (must be non-negative) |
| relations_progress_per_day | `value` | `relations_progress_per_day = 1` | Relations progress between the two countries (can be negative) |
| relations_improvement_max | `value` | `relations_improvement_max = 100` | Max value relations can reach from this article alone (must be non-negative) |
| relations_improvement_min | `value` | `relations_improvement_min = 100` | Min value relations can reach from this article alone (must be non-negative) |
| icon | `path` | `icon = "gfx/interface/icons/diplomatic_treaties_articles_icons/alliance_treaties.dds"` | Path to the treaty article icon |
| maintenance_paid_by | source_country target_country | `maintenance_paid_by = target_country` | Who spends the influence to maintain this treaty article (ignore if mutual) |
| usage_limit | once_per_side once_per_treaty once_per_side_with_same_inputs | `usage_limit = once_per_side` | Restrictions on how many times this article can be used. `once_per_side` is once per country, although keep in mind there can be other restrictions |
| flags | is_alliance is_defensive_pact is_gurantee_independence is_support_independence is_investment_rights is_trade_privilege is_military_access is_transit_rights is_non_colonization_agreement is_goods_transfer is_money_transfer is_monopoly_for_company is_prohibit_goods_trade_with_world_market is_no_tariffs is_no_subventions is_treaty_port is_law_commitment can_be_renegotiated can_be_enforced causes_state_transfer friendly hostile giftable | flags = { is_transit_rights can_be_enforced can_be_renegotiated giftable friendly } | These are code flags that can be applied to treaty articles, and will likely result in the respective behaviour being applied for most of the `is` flags |
| mutual_exclusions | `article type` | mutual_exclusions = { alliance defensive_pact guarantee_independence } | This treaty article cannot be used with the ones included |
| unlocked_by_technologies | `technology` | unlocked_by_technologies = { international_trade } | What technology should unlock the use of this treaty article. [1] |
| automatically_support | `diplomatic play types` | automatically_support = { dp_independence dp_increase_autonomy dp_annex_subject } | What diplomatic plays the source country will automatically support the target country in |
| source_modifier | `modifier types` | source_modifier = { country_treaty_leverage_generation_add = 300 } | Modifiers applied to the source country (must be empty for mutual articles) |
| target_modifier | `modifier types` | target_modifier = { unit_experience_gain_mult = 0.5 building_training_rate_mult = 0.2 country_military_goods_cost_mult = -0.1 country_military_tech_spread_mult = 0.1 } | Modifiers applied to the target country (must be empty for mutual articles) |
| mutual_modifier | `modifier types` | mutual_modifier = { country_treaty_leverage_generation_add = 400 } | Modifiers applied to both countries |

### Validation

These parameters determine when an article can be used.

#### Visible

The `visible` trigger block controls whether the article should be visible to the country at all. It is checked for both countries.

It has the following scopes:

- `root`

#### Possible

The `possible` trigger block controls whether it is possible to consider between two countries. It also automatically runs the `visible` trigger.

It has the following scopes:

- `root`
- `other_country`

#### Maintain

The `requirement_to_maintain` trigger block is a repeatable block that determines if an article is possible as well as to be maintained.

It has the following scopes:

- `root`
- `article`
- `treaty`

Only for mutual articles:

- `first_country`
- `second_country`

Only for directed articles:

- `source_country`
- `target_country`

#### Can ratify

The `can_ratify` trigger block controls whether the two countries are able to ratify a treaty that contains this article type. It runs the `visible` and `possible` triggers automatically.

It has the following scopes:

- `root`
- `article`
- `treaty`

Only for mutual articles:

- `first_country`
- `second_country`

Only for directed articles:

- `source_country`
- `target_country`

### On entry into force

This effect block happens as soon as the treaty with this article is ratified, either diplomatically or by war.

It has the scope `article_options` which contains the parameters of the article, such as `source_country`, `target_country` and `input_state`

### On enforced

This effect block happens as soon as the treaty with this article is enforced by war.

It has the scope `article_options` which contains the parameters of the article, such as `source_country`, `target_country` and `input_state`

### Non-fulfillment

The non-fulfillment block describes how a country can fail their end of the treaty and what should happen when the source country of an article is not fulfilling their end of the agreement.

#### Conditions

The conditions block checks when a country is in contravention with the following time intervals available:

- `weekly`
- `monthly`
- `yearly`

And has the following scopes available:

- `root`
- `article`

For example:

```
conditions = {
weekly = {
    scope:article = { source_country = { in_default = yes } }
}
}
```

#### Consequences

The consequences parameter can be the following:

| Consequence | Description |
|---|---|
| none | nothing |
| withdraw | The contravening party automatically unilaterally withdraws from the treaty, becoming subject to any penalty that might apply |
| freeze | Causes the contravening party to have to keep up their end of the agreement, while the other party sees their obligations lifted, turning the treaty into a one-sided deal until the contravening party is able to fulfill their end of the agreement again |

#### Contraventions

An option for the maximum number of contraventions allowed before consequences applied is also provided:

- `max_consecutive_contraventions`

This limits how many times the country can meet the non-fulfillment conditions in a row before being in non-fulfillment.

### Article inputs

Articles can take inputs of the following kind:

- `quantity`
- `goods`
- `state`
- `strategic_region`
- `company`
- `building_type`
- `law_type`
- `country`

However, the implementation of these is not clearly documented in game files and some don't work without specific article flags. For example, the localization of choosing a strategic_region is only for non-colonization agreements, despite the treaty article not being that. If they are in unmodified Victoria 3, they probably work.

#### Article input triggers

Each input type has a `valid_trigger` block:

- `goods_valid_trigger = {}`
- `state_valid_trigger = {}`
- `strategic_region_valid_trigger = {}`
- `company_valid_trigger = {}`
- `building_type_valid_trigger = {}`
- `law_type_valid_trigger = {}`
- `country_valid_trigger = {}`

The valid triggers have the following scopes available:

| Scope | Description |
|---|---|
| `root` | Source country for the article |
| `article` | The article itself. (Note that not all inputs have been set at this point) |
| `input` | The specific input being checked |
| `other_country` | The other country |

And specifically for the goods valid trigger:

| Scope | Description |
|---|---|
| `goods` | The goods input being checked |
| `market_goods` | The same goods but as market goods for the source country market |

#### Quantity min and max

To set the minimum and maximum of an input, use:

- `quantity_min_value = {}`
- `quantity_max_value = {}`

Each one should include a [script value](Script value.md) block.

### Withdrawal

#### Can withdraw

The `can_withdraw` trigger block determines if a country is allowed to withdraw from a treaty. It has the following scopes:

- `withdrawing_country`
- `non_withdrawing_country`

For mutual articles, also:

- `first_country`
- `second_country`

For directed articles, also:

- `source_country`
- `target_country`

#### On withdrawal

The `on_withdrawal` effect block applies when a party withdraws from a treaty, immediately before the withdrawal takes effect.

It has the following scopes:

- `treaty_options`
- `article`
- `withdrawing_country`
- `non_withdrawing_country`

#### On break

The `on_break` effect block additionally applies when a party withdraws from a treaty before the binding period has ended, immediately before the withdrawal takes effect.

It has the following scopes:

- `treaty_options`
- `article`
- `withdrawing_country`
- `non_withdrawing_country`

### AI

The AI block contains information on how the AI should use and value this article.

#### Treaty categories

Here you can set the categories of the treaty article. The following are provided:

- `economy`
- `trade`
- `military`
- `military_defense`
- `ideology`
- `expansion`
- `power_bloc`
- `other`
- `none`

#### Article usage

How the AI will use the article. Can be multiple. The following are provided:

- `none`
- `will_offer`
- `will_request`

#### Acceptance

The following are provided to limit acceptance gained. These take integers:

- `combined_acceptance_cap_max`
- `combined_acceptance_cap_min`

`inherent_accept_score` and `contextual_accept_score` are added together to create the final acceptance value but maths conducted in one script value does not apply to the other and vice versa.

##### Inherent acceptance

The `inherent_accept_score` block is a script value that does **not** get re-evaluated every time the AI tries to add an article. It has the following scopes:

- `root`
- `article`

Only for mutual articles:

- `first_country`
- `second_country`

Only for directed articles:

- `source_country`
- `target_country`

##### Contextual acceptance

The `contextual_accept_score` block is a script value that has access to the treaty itself and so can check for other articles. It has the following scopes:

- `root`
- `article`
- `treaty`

Only for mutual articles:

- `first_country`
- `second_country`

Only for directed articles:

- `source_country`
- `target_country`

##### Wargoal multiplier

The `wargoal_score_multiplier` is a script value. A multiplier added to the AI acceptance determining how likely it is to pursue this article as a wargoal. It has the following scopes:

- `root`
- `article`

Only for mutual articles:

- `first_country`
- `second_country`

Only for directed articles:

- `source_country`
- `target_country`

### Wargoal data

#### Execution priority

An integer. Higher priority wargoals are executed first.

#### Contestion type

How the wargoal can be 'controlled'. The following are available:

- `control_target_state`
- `control_target_country_capital`
- `control_any_target_country_state`
- `control_own_state`
- `control_own_capital`
- `control_all_own_states`
- `control_all_target_country_claims`

#### Maneuvers and infamy

Both the `maneuvers` and `infamy` blocks are script values. These determine the maneuver cost and infamy gain from using this article as a war goal.

They have the following scopes:

- `root`
- `target_country`

And the following scopes depending on relevant inputs:

- `quantity`
- `country`
- `company`
- `state`
- `region`
- `building`
- `law`
- `goods`
- `market_goods`

## Treaty script documentation

The following [effects](Effect.md), [event targets](Event target.md), and [triggers](Trigger.md) can be used in treaty scopes.

### Treaty scope

| Effect | Description | Example | Targets |
|---|---|---|---|
| every_scope_article | Iterate through articles of the scoped treaty | every_scope_article = { limit = { <triggers> } #optional <effects> } | treaty_article |
| every_scope_article_option | Iterate through article_options of the scoped treaty or treaty_options | every_scope_article_option = { limit = { <triggers> } #optional <effects> } | treaty_article_options |
| ordered_scope_article | Iterate through articles of the scoped treaty | ordered_scope_article = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | treaty_article |
| ordered_scope_article_option | Iterate through article_options of the scoped treaty or treaty_options | ordered_scope_article_option = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | treaty_article_options |
| random_scope_article | Iterate through articles of the scoped treaty | random_scope_article = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | treaty_article |
| random_scope_article_option | Iterate through article_options of the scoped treaty or treaty_options | random_scope_article_option = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | treaty_article_options |
| withdraw | Withdraws a country from a treaty | scope:treaty = { withdraw = { country = <country scope> # must be valid and must be bound by the treaty apply_break_penalties = yes/no # optional, default no. If yes, break effects and on-actions apply when treaty is in binding time } } |  |

| Trigger | Description | Example | Targets |
|---|---|---|---|
| any_scope_article | Iterate through articles of the scoped treaty | any_scope_article = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | treaty_article |
| any_scope_article_option | Iterate through article_options of the scoped treaty or treaty_options | any_scope_article_option = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | treaty_article_options |
| binds | Checks if the scoped treaty or treaty_options binds the given country | scope:some_treaty = { if = { limit = { binds = c:FRA binds = c:BEL } } } | country |
| is_enforced | Checks if the scoped treaty is enforced on either party | scope:some_treaty = { if = { limit = { is_enforced = yes } } } | boolean |
| is_equal_exchange | Checks if the scoped treaty has the same articles on both sides | scope:some_treaty = { if = { limit = { is_equal_exchange = yes } } } | boolean |
| is_fulfilled_by | Check if the scoped treaty is fulfilled by the given country | scope:treaty = { is_fulfilled_by = c:FRA } | country |
| is_historical_treaty | Checks if the scoped treaty was signed before the game start date | is_historical_treaty = yes/no | boolean |
| is_renegotiation | Checks if the scoped treaty is amending an existing treaty | scope:some_treaty = { if = { limit = { is_renegotiation = yes } } } | boolean |
| was_coerced_with_naval_threat | Check if the scoped treaty was accepted through threatening naval hostilities | was_coerced_with_naval_threat = yes/no | boolean |

| Event target | Description | To scope |
|---|---|---|
| amended_treaty | Scope to the treaty the scoped treaty is amending | treaty |
| binding_period | Get the original binding period in days when the treaty was signed for the scoped treaty | value |
| enforced_on_country | Scope to the enforced_on_country of an enforced treaty | country |
| enforcer_country | Scope to the enforcer_country of an enforced treaty | country |
| first_country | Scope to the first_country of any of: diplomatic pact treaty treaty options treaty article's treaty treaty article options (for mutual article types only) | country |
| remaining_binding_period | Get the current remaining binding period in days for the scoped treaty | value |
| second_country | Scope to the second_country of any of: diplomatic pact treaty treaty options treaty article's treaty treaty article options (for mutual article types only) | country |

### Treaty article scope

| Effect | Description | Example | Targets |
|---|---|---|---|

| Trigger | Description | Example | Targets |
|---|---|---|---|
| has_type | Checks if the scoped object has the type identified by the given string | scope:some_object = { has_type = defensive_pact } |  |
| is_treaty_article_in_danger | Checks if treaty article is in danger of breaking | is_treaty_article_in_danger = yes | boolean |
| max_contraventions | Check the maximum contraventions for the article type of the scoped article or article_options | scope:treaty_article = { max_contraventions >= 1 } | value |
| num_contraventions | Check if the scoped article has the given number of contravention from the given country | scope:treaty_article = { num_contraventions = { target = c:FRA value > 0 } } | value |

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

### Treaty options scope

| Effect | Description | Example | Targets |
|---|---|---|---|
| every_scope_article_option | Iterate through article_options of the scoped treaty or treaty_options | every_scope_article_option = { limit = { <triggers> } #optional <effects> } | treaty_article_options |
| ordered_scope_article_option | Iterate through article_options of the scoped treaty or treaty_options | ordered_scope_article_option = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | treaty_article_options |
| random_scope_article_option | Iterate through article_options of the scoped treaty or treaty_options | random_scope_article_option = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | treaty_article_options |

| Trigger | Description | Example | Targets |
|---|---|---|---|
| any_scope_article_option | Iterate through article_options of the scoped treaty or treaty_options | any_scope_article_option = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | treaty_article_options |
| binds | Checks if the scoped treaty or treaty_options binds the given country | scope:some_treaty = { if = { limit = { binds = c:FRA binds = c:BEL } } } | country |
| is_equal_exchange | Checks if the scoped treaty has the same articles on both sides | scope:some_treaty = { if = { limit = { is_equal_exchange = yes } } } | boolean |
| is_historical_treaty | Checks if the scoped treaty was signed before the game start date | is_historical_treaty = yes/no | boolean |
| is_renegotiation | Checks if the scoped treaty is amending an existing treaty | scope:some_treaty = { if = { limit = { is_renegotiation = yes } } } | boolean |

| Event target | Description | To scope |
|---|---|---|
| amended_treaty | Scope to the treaty the scoped treaty is amending | treaty |
| binding_period | Get the original binding period in days when the treaty was signed for the scoped treaty | value |
| first_country | Scope to the first_country of any of: diplomatic pact treaty treaty options treaty article's treaty treaty article options (for mutual article types only) | country |
| remaining_binding_period | Get the current remaining binding period in days for the scoped treaty | value |
| second_country | Scope to the second_country of any of: diplomatic pact treaty treaty options treaty article's treaty treaty article options (for mutual article types only) | country |

### Treaty article options scope

| Effect | Description | Example | Targets |
|---|---|---|---|

| Trigger | Description | Example | Targets |
|---|---|---|---|
| has_type | Checks if the scoped object has the type identified by the given string | scope:some_object = { has_type = defensive_pact } |  |
| max_contraventions | Check the maximum contraventions for the article type of the scoped article or article_options | scope:treaty_article = { max_contraventions >= 1 } | value |

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

## References

1. ↑ May be bugged and does not block articles

Modding
Return to top
| Documentation | [Defines](Defines.md) • [Effects](Effect.md) • [Event targets](Event target.md) • [Scopes](Scope.md) • [Triggers](Trigger.md) [Macros](Macro.md) • [Modifier types](Modifier types.md) • [On actions](https://vic3.paradoxwikis.com/On_actions) • [Script value](Script value.md) • [Variables](Variable.md) |
|---|---|

| Scripted content | [Decisions](Decision modding.md) • [Events](Event modding.md) • [History](History modding.md) • [Journal](Journal modding.md) • [Modifiers](Modifier modding.md) • Objectives • [Scripted gui](Scripted gui.md) |
|---|---|

| Scripted types | [Buildings](Building modding.md) • [Characters](Character modding.md) • Concepts • [Countries](Country modding.md) • [Culture](Culture modding.md) • [Decrees](Decree modding.md) • [Diplomacy](Diplomacy modding.md) • [Goods](Goods modding.md) • [Institutions](Institution modding.md) • [Interest groups](Interest group modding.md) • [Laws](Law modding.md) • Parties • [Pops](Pop modding.md) • [Power blocs](Power bloc modding.md) • [Religion](Religion modding.md) • Subject types • [Technology](Technology modding.md) • Treaties • [War goals](War goal modding.md) |
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
