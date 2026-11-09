---
title: List of flags
source: https://vic3.paradoxwikis.com/List_of_flags
pageid: 2599
categories: [Potentially_outdated, 1.12, Articles_with_potentially_outdated_tables, Flags, Lists]
fetched: 2026-10-27
---
Please help with verifying or updating older sections of this article. At least some were last verified for [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) 1.12.

See also:
Category:Flags
Many countries in the game can have different flags depending on the circumstances. The most important factor is usually the laws of the country. If the conditions for multiple flags are met, the flag with the highest priority is used. This list shows the flags without the flag of the overlord which is often included in a corner if the [game rule](Game rule.md) *“Flags for subjects”* is active. Flags which are listed multiple time have multiple entries in /Victoria 3/game/common/flag_definitions/ (usually with different conditions or different rules about where to show the flag of the overlord). Countries which have only one flag are not included in this list, because they can be found in the [list of countries](Countries.md). Generated flags are similarly not included.

The overlord canton`subject_canton` in the game script is the flag applied to this country's subjects' flags, when allowed by the subject's current flag and the game rules. The subject flag`coa_with_overlord_canton` in the game script is the flag used when this country is a subject. Most often, one or both of these are identical to the country's main flag. Some countries have special subject flags for use when the subject of certain countries such as Great Britain or France. The subject of a subject uses its top overlord's canton when allowed. Protectorates and tributaries never change their flag or allow a canton.

The conditions of flag variations often align with those for a country's [name](Dynamic country names.md) or [map color](Dynamic map colors.md), though not always.

All countries without a flag of priority 1000 or higher receive a random communist themed flag if they have the law Council Republic. Similarly, all countries without a flag of priority 2000 or higher receive a random anarchist themed flag if they have the law Anarchy.

| Jump to section |
|---|
| A • B • C • D • E • F • G • H • I • J • K • L • M • N • O • P • Q-R • S • T • U • V-Z |

## List

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this table. It was last verified for version 1.12. |
|---|---|

The [United States of America](America.md) has a large number of flags that represent the number of incorporated states – never counting District of Columbia or West Virginia. These flags all have priority 5 and so are not used if one of the higher priority flags for America is used instead. They all use the same overlord canton `sub_USA_canton_star` and allow for an overlord canton to be applied.

| American flags |
|---|
| USA_25 USA_26 USA_27 USA_28 USA_29 USA_30 USA_31 USA_32 USA_33 USA_34 USA_35 USA_36 USA_37 USA_38 USA_39 USA_40 USA_41 USA_42 USA_43 USA_44 USA_45 USA_46 USA_47 USA_48 USA_49 USA_50 USA_51 USA_52 USA_53 USA_54 USA_55 USA_56 USA_57 USA_58 USA_59 USA_60 USA_61 USA_62 USA_63 USA_64 USA_65 USA_66 USA_67 USA_68 USA_69 USA_70 USA_71 USA_72 USA_73 USA_74 USA_75 USA_76 USA_77 USA_78 USA_79 USA_80 USA_81 USA_82 USA_83 USA_84 USA_85 USA_86 USA_87 USA_88 USA_89 USA_90 USA_91 USA_92 USA_93 USA_94 USA_95 USA_96 USA_97 USA_98 USA_99 USA_100 |

## References

1. ↑ Technically, has the variable `algeria_deylik_restored`
2. ↑ Technically, has the variable `algeria_barbary_restored`
3. ↑ 3.0 3.1 Possibly a bug, two `subject_canton` lines exist; this is the second one which appears in game
4. ↑ 4.0 4.1 4.2 Used even if game rule for changing subject flags is off
5. ↑ 5.0 5.1 5.2 5.3 5.4 5.5 If the USA exists and has the journal entry *The American Civil War* active, this flag cannot use the revolutionary "tear" graphic
6. ↑ Technically, has the variable `legitimist_restoration_var`
7. ↑ Technically, has the variable `bonapartist_restoration_var`
8. ↑ 8.0 8.1 Technically, has the variable `ROM_united_principality`
9. ↑ 9.0 9.1 Technically, has the variable `king_sounds_better`

To update this table, see the 'sublist' pages:

- [List of flags/a-d](List of flags_a-d.md)
- [List of flags/e-l](List of flags_e-l.md)
- [List of flags/m-r](List of flags_m-r.md)
- [List of flags/s-z](List of flags_s-z.md)
