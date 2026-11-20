---
translated: 2026-10-27
translator: machine (glm-5.3)
title: History modding
source: https://vic3.paradoxwikis.com/History_modding
pageid: 7409
categories: [Potentially_outdated, 1.10, Expand, Modding]
fetched: 2026-10-27
---
请协助验证或更新本文中较旧的章节。至少有部分内容最后验证于 [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) 1.10。

|  | 请通过[扩充](https://vic3.paradoxwikis.com/index.php?title=History_modding&action=edit)以下内容来协助改进本条目：更多历史类别的信息。 |
|---|---|

历史 [effects](Effect.md)（游戏内效果脚本）位于 common/history/ 中，是《维多利亚3》为新游戏初始化起始状态的方式。这包括国家、政治、人口（Pops）、识字率、技术等内容。

history 文件夹包含若干子文件夹，用于组织这些设置效果。这些效果都会在玩家于主菜单选择沙盒选项或通过目标选择一个国家之后执行。注意，history 只涉及改变新游戏的起始游戏状态。修改 history 文件不会影响其他脚本文件中定义的机制，也不会影响任何已在进行中的游戏。

## 历史文件结构

《维多利亚3》按以下顺序执行其历史效果：[1]

| 顺序 | 键 |
|---|---|
| 1 | STATES |
| 2 | COUNTRIES |
| 3 | POPS |
| 4 | DIPLOMACY |
| 5 | POPULATION |
| 6 | POWER_BLOCS |
| 7 | INTERESTS |
| 8 | BUILDINGS |
| 9 | PRODUCTION_METHODS |
| 10 | MILITARY_FORMATIONS |
| 11 | AI |
| 12 | TREATIES |
| 13 | LOBBIES |
| 14 | DIPLOMATIC_PLAYS |
| 15 | TRADE |
| 16 | GLOBAL |
| 17 | POLITICAL_MOVEMENTS |
| 18 | CHARACTERS |
| 19 | GOVERNMENT |
| 20 | GOVERNMENT_SETUP |
| 21 | MILITARY_DEPLOYMENTS |

上述每个键都会创建一个 effect 块，执行其中包含的所有效果。所有 history 键都不提供 scope（作用域），因此所有效果都必须正确指定作用域。文件和子文件夹可以随意命名，只有其中包含的 history 键才重要。

### 修改历史文件

参见
Mod 文件加载顺序
以了解更多关于加载顺序规则的信息
Mod 作者一般应避免修改原版 history 文件，除非目的是抢在原版之前执行。修改原版文件，*尤其是各州（state）的 history*，是兼容性的一大杀手，因为它会以其他 mod 作者无法预料的方式改变起始游戏状态。`history` 文件夹中的文件遵循加载顺序规则，因此 mod 作者可以根据需要确保自己的历史效果在原版历史之前或之后执行。

### 使用历史效果

history 中使用的效果并非 history 文件独有，可以根据 mod 设置的需要在其他 history 文件中或游戏运行期间触发。如有需要，可以在效果原本所属的 history 文件之后更靠下游的位置使用这些效果。例如，你可以等到 `global` 历史阶段再移动或转换人口，以避免改动任何原版人口文件。大多数 mod 作者都会在 `global` 中执行其历史效果，因为它相对于其他 history 文件而言处于非常靠下游的位置。

*注意：在历史执行完毕后使用 create_state 或 create_pop 等历史专用效果不受 Paradox 支持，而且很可能出现各种 bug。*

## 历史文件示例

以下各节展示 history 文件的使用示例。注意，除了执行顺序之外，任何效果都可以在任何 history 键块中运行

### 州（States）历史

参见
地图 modding
以了解关于修改
省份地图
的更多信息；
州 modding
以了解关于修改
州区域（state regions）
和战略区域的更多信息；
覆盖州
以获取修改州设置的指南。
**州历史**用于创建起始的各州（*不包括它们的州区域*）以及拥有这些州的国家。故土（homeland）、宣称和建州地位也在此处指定。如果某个国家在 history 中没有被给予任何州，它在游戏开始时*将不会*存在。

此 history 文件涉及在**州区域**（`s:`）scope 中执行相关效果。以下来自爱达荷州原版历史的示例展示了所有这些效果的实际应用：

```
STATES = {
	s:STATE_IDAHO = {
		create_state = {
			country = c:ORG
			owned_provinces = { 
				x4B49F2 xE836AA xB94979 x2BCA5E x0667C7 x7B7595
			}
			state_type = unincorporated
		}
		create_state = {
			country = c:BNN
			owned_provinces = {
				x87941A xE65BC2 xFD9C12 xB8D005 x774CEA xD484FE xB20F44 x7355BF x017C34 x2C976D x73354E x3BC3DC x81EADA x156C47 x573B27 xA1A13A xA1C84D x40339D x4A7CD8 x744A86 x0B6D01 x3B157B x1F04CC x4690C2 xBC0AA9 x9888F6 x236126 xD00080 xEC9F6C x0FB2AA x4DBE4A x06E885 x44332A xB95EB2 x7B1E0A x233F47 x1E57E5 xC998B0
			}
		}
		create_state = {
			country = c:NZP
			owned_provinces = {
				x0682D7 x249E28 xED64F1 x9F2532 x83926D xC3178C xB5C710 x2CC6D7 x7D5812 xD06EF9 xE6E56D x9D7B0E xF11FC4 xCE1B4B x0062B6 x01C975 x073B66 x96529F x0456B2 xCC869C x402080
				xCFD016 xBFA9C4 xE6B7A4 x8C707D x25F860 x4DAA8A xD7B25C x9D92A7 x82AA18
			}
		}

		add_homeland = cu:nez_perce
		add_homeland = cu:paiute
		add_claim = c:ORG
	}
}
```

在此示例中，这个效果块做了以下事情：

- 在爱达荷**州区域**内创建**州**，同时创建拥有这些州的国家（此处为 ORG、BNN 和 NZP）。*州区域所包含的省份定义于 map_data/state_regions*
- 将 ORG 拥有的州指定为**未建州（unincorporated）**。如果未指定为 `unincorporated` 或 `treaty_port`，州默认为已建州
- 为爱达荷州区域添加 `nez_perce` 和 `paiute` 文化的故土
- 给予 ORG 对该州区域的宣称，以阻止其他国家殖民该州区域。

### 国家（Countries）历史

参见
国家 modding
以了解关于修改国家的更多信息
**国家历史**用于在创建人口和外交关系之前，设置一个国家的若干基础要素。游戏通常在此处设置初始政府、政治、税收政策、法律以及已研究的技术。

**注意：**在此阶段，游戏状态中只有国家和它们的空州。还没有人口、建筑或商品可供交互。

此示例展示了原版中大不列颠的国家历史：

```
COUNTRIES = {
	c:GBR ?= {
		set_next_election_date = 1836.2.1
		
		ig:ig_intelligentsia = {
			add_ruling_interest_group = yes
		}

		ig:ig_petty_bourgeoisie = {
			add_ruling_interest_group = yes
		}
		
		set_tariffs_export_priority = g:grain
		set_tariffs_import_priority = g:fabric
		set_tariffs_import_priority = g:wood
		set_tariffs_import_priority = g:hardwood
		
		effect_starting_technology_tier_1_tech = yes
		
		add_technology_researched = labor_movement # A relevant labour movement already existed prior to 1836

		set_tax_level = medium
		
		add_taxed_goods = g:liquor
		add_taxed_goods = g:luxury_clothes
		add_taxed_goods = g:luxury_furniture
		add_taxed_goods = g:tea

		# Laws 
		activate_law = law_type:law_monarchy
		activate_law = law_type:law_wealth_voting
		activate_law = law_type:law_freedom_of_conscience
		activate_law = law_type:law_women_own_property
		activate_law = law_type:law_per_capita_based_taxation
		activate_law = law_type:law_appointed_bureaucrats
		activate_law = law_type:law_right_of_assembly
		activate_law = law_type:law_national_supremacy
		activate_law = law_type:law_protectionism # Corn Laws, babyyy
		activate_law = law_type:law_interventionism
		activate_law = law_type:law_religious_schools
		activate_law = law_type:law_per_capita_based_taxation
		activate_law = law_type:law_colonial_resettlement
		activate_law = law_type:law_poor_laws
		activate_law = law_type:law_charitable_health_system
		activate_law = law_type:law_dedicated_police
		activate_law = law_type:law_professional_army
		activate_law = law_type:law_tenant_farmers # enclosure acts
		activate_law = law_type:law_migration_controls
		
		set_institution_investment_level = {
			institution = institution_colonial_affairs
			level = 2
		}
		
		set_institution_investment_level = {
			institution = institution_schools
			level = 3
		}

		set_institution_investment_level = {
			institution = institution_police
			level = 1
		}

		add_journal_entry = { type = je_victoria }
		if = {
			limit = {
				has_dlc_feature = rp1_content
			}
			add_journal_entry = { type = je_aberdeen_act }
		}

		add_modifier = {
			name = brazilian_slave_trade_modifier
			months = 600 # 50 Years
		}

		add_company = company_type:company_gwr
		company:company_gwr = {
			set_company_establishment_date = 1833.1.21
			set_company_state_region = s:STATE_HOME_COUNTIES
		}
	}
}
```

重要的一点是，`add_technology_researched` 是不可逆的。如果某个国家起始就已有某项技术被研究，你必须覆盖该国的原版历史文件才能阻止它以已研究状态开局。

### 人口（Pops）历史

参见
人口 modding
以了解关于修改职业的更多信息
**人口历史**是游戏为每个州创建人口的方式。这是在州（*而非州区域*）scope 中使用 `create_pop` 效果完成的。你可以通过以下方法指向某个州区域内的特定州：

```
# Using Brackets
s:STATE_MINSK = {
	region_state:RUS = {
	}
}

# Using Dot Linkage
s:STATE_MINSK.region_state:RUS = {
}
```

以下来自原版文件的示例展示了使用 `create_pops` 的多种方式：

```
This is an example of all the ways in which create_pop can now be used
POPS = {
	#s:STATE_MINSK = {
	#	region_state:RUS = {
	#		create_pop = {
	#			culture = byelorussian
	#			size = 176925
	#		}
	#
	#		create_pop = {
	#			culture = ukrainian
	#			size = 24700
	#		}
	#
	#		create_pop = {
	#			culture = ashkenazi
	#			religion = jewish
	#			size = 26100
	#		}
	#
	#		create_pop = {
	#			culture = polish
	#			size = 29783
	#		}
	#
	#		create_pop = {
	#			culture = lithuanian
	#			size = 1002
	#		}
	#
	#		create_pop = {
	#			culture = russian
	#			size = 2034
	#		}
	#
	#		create_pop = {
	#			pop_type = aristocrats
	#			culture = polish
	#			religion = catholic
	#			size = 5200
	#		}
	#	}
	#}
}
```

### 外交（Diplomacy）历史

参见
外交 modding
以了解关于外交的更多信息。
**外交历史**用于设置外交关系、附属国关系、关系值以及停战。以下是原版脚本的摘录：

```
DIPLOMACY = {
	c:SPA ?= {
		create_diplomatic_pact = {
			country = c:CUB
			type = colony
		}
		create_diplomatic_pact = {
			country = c:PHI
			type = colony
		}	
	}
}
```

```
DIPLOMACY = {
	c:NET ?= {
		create_bidirectional_truce = {
			country = c:BEL
			months = 40
		}
	}	
}
```

```
DIPLOMACY = {
	c:GRE ?= {
		set_owes_obligation_to = {
			country = c:RUS
			setting = yes
		}
		set_owes_obligation_to = {
			country = c:FRA
			setting = yes
		}
		set_owes_obligation_to = {
			country = c:GBR 
			setting = yes
		}
	}
}
```

```
DIPLOMACY = {
	c:AUS ?= { 
		set_relations = { country = c:KRA value = -30 }
		set_relations = { country = c:TUR value = -30 }
		set_relations = { country = c:BAV value = 30 }
		set_relations = { country = c:BAD value = 30 }
		set_relations = { country = c:WUR value = 30 }
		set_relations = { country = c:SAR value = 10 }
		set_relations = { country = c:SIC value = 30 }
		set_relations = { country = c:MOD value = 30 }
		set_relations = { country = c:PAR value = 30 }
		set_relations = { country = c:LUC value = 30 }
		set_relations = { country = c:PAP value = 30 }
	}
}
```

```
DIPLOMACY = {
	c:RUS ?= {
		create_diplomatic_pact = {
			country = c:TUR
			type = rivalry
		}
	}
	c:TUR ?= {
		create_diplomatic_pact = {
			country = c:RUS
			type = rivalry
		}
	}
}
```

### 人口总量（Population）历史

**人口总量历史**用于初始化一个国家起始的人口财富和识字率：

```
POPULATION = {
	c:MOD ?= {
		effect_starting_pop_wealth_high = yes
		effect_starting_pop_literacy_low = yes
	}
}
```

### 强权集团（Power bloc）历史

参见
强权集团 modding
以了解关于修改强权集团的更多信息。
**强权集团历史**用于为游戏创建起始的强权集团。请记住，附属国会自动纳入其宗主国的强权集团。目前没有任何效果或命令可以将一个国家移出强权集团或解散强权集团。

*重要：如果没有任何起始强权集团，将在历史执行期间导致 CTD（崩溃到桌面）。你必须定义至少一个起始强权集团！*

```
POWER_BLOCS = {
	c:GBR = {
		create_power_bloc = {
			name = BRITISH_EMPIRE
			map_color = hsv{ 0.99  0.7  0.9 }

			founding_date = 1784.5.12 # Treaty of Paris (1783) comes into effect
			identity = identity_sovereign_empire
			principle = principle_vassalization_1

			# subjects are automatically part of the bloc
		}
		if = {
			limit = {
				has_dlc_feature = power_bloc_features
			}
			power_bloc = {
				add_principle = principle_colonial_offices_2
			}
		}
	}

	c:AUS = {
		create_power_bloc = {
			name = METTERNICH_SYSTEM

			map_color = { 219 211 157 }

			founding_date = 1815.6.9 # Final agreement of the 1814 Congress of Vienna
			identity = identity_ideological_union
			principle = principle_creative_legislature_1

			# Habsburg leaders in Italy and Italian states held up by direct Austrian intervention
			member = c:MOD
			member = c:TUS
			member = c:PAR
			member = c:SIC
		}
		if = {
			limit = {
				has_dlc_feature = power_bloc_features
			}
			power_bloc = {
				add_principle = principle_defensive_cooperation_1
			}
		}
	}
}
```

*注意：强权集团是与"势力范围"（Sphere of Influence）DLC 相连的功能。按照 Paradox 的政策，不要让玩家访问他们未拥有的 DLC 功能。*使用 `has_dlc_feature = power_bloc_features` 来为第一条之外的原则设置条件

### 利益（Interest）历史

**利益历史**用于设置一个国家在游戏开始时的外交利益，从而决定其外交接触。这也会影响一个国家在游戏开始时能够访问哪些市场。

```
INTERESTS = {
	c:GBR ?= {
		add_declared_interest = region_baltic
		add_declared_interest = region_brazil
		add_declared_interest = region_rhine
		add_declared_interest = region_france
		add_declared_interest = region_south_china
		add_declared_interest = region_north_china
		add_declared_interest = region_nile_basin
		add_declared_interest = region_north_africa
		add_declared_interest = region_occitania
		add_declared_interest = region_poland
		add_declared_interest = region_russia
		add_declared_interest = region_anatolia
		add_declared_interest = region_indonesia
		add_declared_interest = region_japan
		add_declared_interest = region_andes
		add_declared_interest = region_manchuria
		add_declared_interest = region_caucasus
	}
}
```

### 建筑（Building）历史

参见
建筑 modding
以了解关于修改建筑的更多信息。
```
BUILDINGS={
	s:STATE_DISTRICT_OF_COLUMBIA={
		region_state:USA={
			create_building={
				building="building_government_administration"
				add_ownership={
					country={
						country="c:USA"
						levels=6
					}
				}
				reserves=1
				activate_production_methods={ "pm_secular_bureaucrats" "pm_professional_bureaucrats" "pm_horizontal_drawer_cabinets" }
			}
			create_building={
				building="building_white_house"
				level=1
			}
		}
	}
	if = {
		limit = {
			has_american_buildings_dlc_trigger = yes
		}
		s:STATE_DISTRICT_OF_COLUMBIA={
			region_state:USA={
				create_building={
					building="building_capitol_hill"
					level=1
				}
			}
		}
	}
}
```

### 生产方式（Production method）历史

**生产方式历史**用于更改特定国家中建筑的生产方式。虽然可以在创建建筑时指定生产方式，但对于自动调整规模的建筑（如城市中心或所有权建筑），必须使用此块。在此历史组中更改生产方式可确保所有建筑在批量切换生产方式之前都已创建完毕。

```
PRODUCTION_METHODS = {
	c:USA ?= {
		activate_production_method = {
			building_type = building_urban_center
			production_method = pm_market_squares
		}
		activate_production_method = {
			building_type = building_urban_center
			production_method = pm_gas_streetlights
		}
	}
}
```

### 军事编制（Military formation）历史
**军事编队历史**（Military Formation History）是游戏通常用来创建初始军事编队的地方。

兵营会自动缩放到陆军所需的相应等级。海军管理部门不会自动扩张，必须在建筑历史中手动创建，以避免人力短缺。

```
# Example Army Formation
c:PRU ?= {
	create_military_formation = {
		type = army
		hq_region = sr:region_central_europe
		name = 1_Armee
		
		combat_unit = {
			type = unit_type:combat_unit_type_skirmish_infantry
			state_region = s:STATE_POMERANIA
			count = 9
		}
		combat_unit = {
			type = unit_type:combat_unit_type_cuirassiers
			state_region = s:STATE_POMERANIA
			count = 1
		}
	}
}

# Example Naval Formation
c:PRU = {
	create_military_formation = {
		type = fleet
		hq_region = sr:region_central_europe
		name = Kniglich_Preuische_Marine
		save_scope_as = fleet_scope_prussian_navy
		
	}
	create_ship = {
		type = ship_type:ship_type_frigate
		fleet = scope:fleet_scope_prussian_navy
		name = sn_princess_louise
	}
}
```

### AI 历史

**AI 历史**（AI History）是调整若干面向脚本的设置与变量以改变 AI 行为的地方。

```
AI = {
	c:SER ?= {
		set_strategy = ai_strategy_agricultural_expansion
		set_strategy = ai_strategy_subject_break_free
		set_strategy = ai_strategy_conservative_agenda
	}
}
```

### 条约历史

**条约历史**（Treaty History）用于在游戏开始时创建已生效的条约。请注意，将 `entered_into_force_on` 日期设为游戏开始日期之前，仍会计入条约的 `binding_period`。

```
TREATIES = {
	create_treaty = {
		name = treaty_name_us_military_mission_to_texas
		first_country = c:USA
		second_country = c:TEX

		is_draft = no
		entered_into_force_on = 1835.10.2 # Start of Texas Revolt
		binding_period = { years = 5 } # about 5 years

		articles_to_create = {
			{
				article = military_assistance
				source_country = c:USA
				target_country = c:TEX
			}
			{ # Small arms aid
				article = goods_transfer
				source_country = c:USA
				target_country = c:TEX
				inputs = {
					{ goods = g:small_arms }
					{ quantity = 10 }
				}
			}
		}
	}
}
```

### 游说集团历史

**游说集团历史**（Lobby history）是游戏创建各国初始游说集团的地方：

```
LOBBIES = {
	c:GRE = {
		create_political_lobby = {  
			type = lobby_pro_country  
			target = c:GBR
			add_interest_group = ig:ig_petty_bourgeoisie
		}
		create_political_lobby = {
			type = lobby_pro_country  
			target = c:RUS
			add_interest_group = ig:ig_landowners
			add_interest_group = ig:ig_devout
		}
		create_political_lobby = {  
			type = lobby_pro_country  
			target = c:FRA
			add_interest_group = ig:ig_intelligentsia
		}	
	}
}
```

### 外交博弈历史

### 贸易历史

**贸易历史**（Trade History）用于创建通往或来自世界市场的贸易路线。

```
TRADE = {
	s:STATE_FLANDERS={
		region_state:BEL={
			sg:dye = {
				add_imports = 10
			}
			sg:clothes = {
				add_exports = 8
			}
		}
	}
}
```

### 全球历史

### 政治运动历史

### 人物历史

### 政府历史

### 政府设置历史

### 军事部署历史

## 参考资料

1. ↑ 由 [Tiger validator](https://github.com/amtep/tiger) 的 Amtep 所确定

Modding
返回顶部
| 文档 | [Defines](Defines.md) • [Effects](Effect.md) • [Event targets](Event target.md) • [Scopes](Scope.md) • [Triggers](Trigger.md) [Macros](Macro.md) • [Modifier types](Modifier types.md) • [On actions](https://vic3.paradoxwikis.com/On_actions) • [Script value](Script value.md) • [Variables](Variable.md) |
|---|---|

| 脚本内容 | [Decisions](Decision modding.md) • [Events](Event modding.md) • History • [Journal](Journal modding.md) • [Modifiers](Modifier modding.md) • Objectives • [Scripted gui](Scripted gui.md) |
|---|---|

| 脚本类型 | [Buildings](Building modding.md) • [Characters](Character modding.md) • Concepts • [Countries](Country modding.md) • [Culture](Culture modding.md) • [Decrees](Decree modding.md) • [Diplomacy](Diplomacy modding.md) • [Goods](Goods modding.md) • [Institutions](Institution modding.md) • [Interest groups](Interest group modding.md) • [Laws](Law modding.md) • Parties • [Pops](Pop modding.md) • [Power blocs](Power bloc modding.md) • [Religion](Religion modding.md) • Subject types • [Technology](Technology modding.md) • [Treaties](Treaty modding.md) • [War goals](War goal modding.md) |
|---|---|

| 地图 | [Map](Map modding.md) • [Geographic regions](Geographic region modding.md) • [States](State modding.md) |
|---|---|

| 界面 | [Interface](Interface modding.md) • [GUI script](GUI script.md) • [Localization](Localization.md) • [Customizable localization](Localization.md) • [Script localization](Script localization.md) |
|---|---|

| 图形 | [3D Models](Model modding.md) • [Event images](Event images.md) • [Graphical Assets](Graphical asset modding.md) • Fonts • [Flags](Flag modding.md) |
|---|---|

| 音频 | Music • [Sound](Sound modding.md) |
|---|---|

| 其他 | [AI](AI modding.md) • [Console commands](Console commands.md) • [Checksum](https://vic3.paradoxwikis.com/Checksum) • [Mods](Mod.md) • [Mod compatibility](Mod compatibility.md) • [Mod structure](Mod structure.md) • [Scripted tests](Scripted test.md) • [Troubleshooting](Troubleshooting.md) |
|---|---|

| 指南 | [Mod translation](Mod translation.md) • [New country modding](New country modding.md) • [Save-game editing](Save-game editing.md) • [State modding guide](State modding guide.md) |
|---|---|