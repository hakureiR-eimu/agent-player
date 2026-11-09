---
translated: 2026-10-27
translator: machine (glm-5.3)
title: List of GUI script functions
source: https://vic3.paradoxwikis.com/List_of_GUI_script_functions
pageid: 8366
categories: [Modding, Lists]
fetched: 2026-10-27
---
主条目：
GUI 脚本
本页面列出所有 GUI 脚本 function，由于列表过长，无法直接包含在 GUI 脚本主页面中。

| 类型 | Function | 参数 | 输出 | 描述 |
|---|---|---|---|---|
| AIAttitude | AccessSelf |  | AIAttitude | 类别：const |
| AIAttitude | CalcScore |  | CFixedPoint |  |
| AIAttitude | GetColor |  | CString | 类别：nonconst |
| AIAttitude | GetDesc |  | CString | 类别：nonconst |
| AIAttitude | GetFirstCountry |  | Country | 类别：nonconst |
| AIAttitude | GetName |  | CString | 类别：nonconst |
| AIAttitude | GetReasonsDesc |  | CString | 类别：nonconst |
| AIAttitude | GetSecondCountry |  | Country | 类别：nonconst |
| AIAttitude | GetStrategicDesireCatalystDesc |  | CString | 类别：nonconst |
| AIAttitude | GetStrategicDesireDesc |  | CString | 类别：nonconst |
| AIAttitude | GetTexture |  | Unknown | 类别：nonconst |
| AIAttitude | GetTooltip |  | CString | 类别：nonconst |
| AIAttitude | GetTooltipTag |  | CString | 类别：nonconst |
| AIAttitude | Self |  | AIAttitude |  |
| AIStrategy | AccessSelf |  | AIStrategy | 类别：const |
| AIStrategy | GetDesc | Country | CString | 类别：nonconst |
| AIStrategy | GetName |  | CString | 类别：nonconst |
| AIStrategy | GetTexture |  | Unknown | 类别：nonconst |
| AIStrategy | GetTooltip | Country | CString | 类别：nonconst |
| AIStrategy | GetTooltipTag |  | CString | 类别：nonconst |
| AIStrategy | Self |  | AIStrategy |  |
| AcceptanceStatus | AccessSelf |  | AcceptanceStatus | 类别：const |
| AcceptanceStatus | GetBackground |  | Unknown | 类别：nonconst |
| AcceptanceStatus | GetColor |  | CVector4f | 类别：nonconst |
| AcceptanceStatus | GetDesc |  | CString | 类别：nonconst |
| AcceptanceStatus | GetEffectsDescIn | Country | CString | 类别：nonconst |
| AcceptanceStatus | GetHigherStatus |  | AcceptanceStatus | 类别：nonconst |
| AcceptanceStatus | GetLargeIcon |  | Unknown | 类别：nonconst |
| AcceptanceStatus | GetLowerBound |  | int32 | 类别：nonconst |
| AcceptanceStatus | GetLowerStatus |  | AcceptanceStatus | 类别：nonconst |
| AcceptanceStatus | GetName |  | CString | 类别：nonconst |
| AcceptanceStatus | GetNameNoFormatting |  | CString | 类别：nonconst |
| AcceptanceStatus | GetNameNoIcon |  | CString | 类别：nonconst |
| AcceptanceStatus | GetOrdinal |  | int32 | 类别：nonconst |
| AcceptanceStatus | GetSmallIcon |  | Unknown | 类别：nonconst |
| AcceptanceStatus | GetTextIcon |  | CString | 类别：nonconst |
| AcceptanceStatus | GetTooltipTag |  | CString | 类别：nonconst |
| AcceptanceStatus | GetUpperBound |  | int32 | 类别：nonconst |
| AcceptanceStatus | HasHigherStatus |  | bool |  |
| AcceptanceStatus | HasLowerStatus |  | bool |  |
| AcceptanceStatus | Self |  | AcceptanceStatus |  |
| AcceptanceStatusSegment | AccessSelf |  | AcceptanceStatusSegment | 类别：const |
| AcceptanceStatusSegment | GetColor |  | CVector4f | 类别：nonconst |
| AcceptanceStatusSegment | GetPopulationDesc |  | CString | 类别：nonconst |
| AcceptanceStatusSegment | GetStatus |  | AcceptanceStatus | 类别：nonconst |
| AcceptanceStatusSegment | GetTotalPopulation |  | int64 | 类别：nonconst |
| AcceptanceStatusSegment | GetTotalPopulationIncreasingInAcceptance |  | int64 | 类别：nonconst |
| AcceptanceStatusSegment | Self |  | AcceptanceStatusSegment |  |
| AccountInventory | AccessSelf |  | AccountInventory | 类别：const |
| AccountInventory | HasItem | Unknown | bool |  |
| AccountInventory | HasRetrievedInventory |  | bool |  |
| AccountInventory | Self |  | AccountInventory |  |
| Achievement | AccessSelf |  | Achievement | 类别：const |
| Achievement | IsUnlocked |  | bool |  |
| Achievement | Self |  | Achievement |  |
| AchievementPopup | AccessJustUnlockedAchievements |  | Unknown | 类别：const |
| AchievementPopup | AccessSelf |  | AchievementPopup | 类别：const |
| AchievementPopup | Self |  | AchievementPopup |  |
| AchievementPopup | ShowWindow |  | void |  |
| AchievementWindow | AccessGroups |  | Unknown | 类别：const |
| AchievementWindow | AccessSelf |  | AchievementWindow | 类别：const |
| AchievementWindow | HasGameStarted |  | bool |  |
| AchievementWindow | Hide |  | void |  |
| AchievementWindow | Self |  | AchievementWindow |  |
| AchievementWindow | ShouldShowAll |  | bool |  |
| AchievementWindow | ShouldShowLocked |  | bool |  |
| AchievementWindow | ShouldShowPossible |  | bool |  |
| AchievementWindow | ShouldShowUnlocked |  | bool |  |
| AchievementWindow | Show |  | void |  |
| AchievementWindow | ShowAll |  | void |  |
| AchievementWindow | ShowLocked |  | void |  |
| AchievementWindow | ShowPossible |  | void |  |
| AchievementWindow | ShowUnlocked |  | void |  |
| AddFriendWindow | AccessSelf |  | AddFriendWindow | 类别：const |
| AddFriendWindow | Hide |  | void |  |
| AddFriendWindow | Self |  | AddFriendWindow |  |
| AddFriendWindow | ShouldBeShown |  | bool |  |
| AddFriendWindow | Show |  | void |  |
| AddWarGoalPanel | AccessCountry |  | Country | 类别：const |
| AddWarGoalPanel | AccessDiplomaticPlay |  | DiplomaticPlay | 类别：const |
| AddWarGoalPanel | AccessSelf |  | AddWarGoalPanel | 类别：const |
| AddWarGoalPanel | AccessShownWarGoalTypes |  | Unknown | 类别：const |
| AddWarGoalPanel | AccessShownWarGoals |  | Unknown | 类别：const |
| AddWarGoalPanel | ClearSelectedWarGoalType |  | void |  |
| AddWarGoalPanel | GetCountry |  | Country | 类别：nonconst |
| AddWarGoalPanel | GetDiplomaticPlay |  | DiplomaticPlay | 类别：nonconst |
| AddWarGoalPanel | HasSelectedWarGoalType |  | bool |  |
| AddWarGoalPanel | Self |  | AddWarGoalPanel |  |
| AddWarGoalPanel | SetSelectedWarGoalType | WarGoalType | void |  |
| AgitatorSlot | AccessSelf |  | AgitatorSlot | 类别：const |
| AgitatorSlot | EnableInvite |  | void |  |
| AgitatorSlot | GetAgitator |  | Character | 类别：nonconst |
| AgitatorSlot | Self |  | AgitatorSlot |  |
| Alert | AccessSelf |  | Alert | 类别：const |
| Alert | AddingFinished |  | void |  |
| Alert | BeginIdleAnimation |  | void |  |
| Alert | GetAction |  | CString | 类别：nonconst |
| Alert | GetAlertGroup |  | Unknown | 类别：nonconst |
| Alert | GetColor |  | CVector4f | 类别：nonconst |
| Alert | GetDescription |  | CString | 类别：nonconst |
| Alert | GetHint |  | CString | 类别：nonconst |
| Alert | GetName |  | CString | 类别：nonconst |
| Alert | GetScopeTexture |  | Unknown | 类别：nonconst |
| Alert | GetTexture |  | Unknown | 类别：nonconst |
| Alert | GetToolTip |  | CString | 类别：nonconst |
| Alert | GetTooltipTag |  | CString | 类别：nonconst |
| Alert | HasScopeTexture |  | bool |  |
| Alert | IdleAnimationFinished |  | void |  |
| Alert | IsAdded |  | bool |  |
| Alert | IsAdding |  | bool |  |
| Alert | IsAngryImportantAction |  | bool |  |
| Alert | IsHidden |  | bool |  |
| Alert | IsRead |  | bool |  |
| Alert | IsRemovalRequested |  | bool |  |
| Alert | MarkAsHidden |  | void |  |
| Alert | MarkAsRead |  | void |  |
| Alert | RemovingFinished |  | void |  |
| Alert | Self |  | Alert |  |
| Alert | StartRemoving |  | void |  |
| Alert | Unhide |  | void |  |
| AlertGroup | AccessSelf |  | AlertGroup | 类别：const |
| AlertGroup | GetTooltipTag |  | CString | 类别：nonconst |
| AlertGroup | Self |  | AlertGroup |  |
| AlertOptionItem | AccessSelf |  | AlertOptionItem | 类别：const |
| AlertOptionItem | GetName |  | CString | 类别：nonconst |
| AlertOptionItem | GetNameWithConcept |  | CString | 类别：nonconst |
| AlertOptionItem | IsDefault |  | bool |  |
| AlertOptionItem | Self |  | AlertOptionItem |  |
| AlertSettingsItem | AccessSelf |  | AlertSettingsItem | 类别：const |
| AlertSettingsItem | GetCurrentOption |  | AlertOptionItem | 类别：nonconst |
| AlertSettingsItem | GetSettingName |  | CString | 类别：nonconst |
| AlertSettingsItem | GetValidOptions |  | Unknown | 类别：nonconst |
| AlertSettingsItem | OnSelectOption |  | void |  |
| AlertSettingsItem | Self |  | AlertSettingsItem |  |
| Amendment | AccessSelf |  | Amendment | 类别：const |
| Amendment | GetAttachedLaw |  | Law | 类别：nonconst |
| Amendment | GetCooldownEndDate |  | CString | 类别：nonconst |
| Amendment | GetCustom | CustomLocalization | CString | 类别：nonconst |
| Amendment | GetEndorsingInterestGroups |  | Unknown | 类别：nonconst |
| Amendment | GetEndorsingInterestGroupsBreakdown |  | CString | 类别：nonconst |
| Amendment | GetEndorsingInterestGroupsSummary |  | CString | 类别：nonconst |
| Amendment | GetIndifferentInterestGroups |  | Unknown | 类别：nonconst |
| Amendment | GetIndifferentInterestGroupsBreakdown |  | CString | 类别：nonconst |
| Amendment | GetIndifferentInterestGroupsSummary |  | CString | 类别：nonconst |
| Amendment | GetName |  | CString | 类别：nonconst |
| Amendment | GetNameNoFormatting |  | CString | 类别：nonconst |
| Amendment | GetNumEndorsingInterestGroups |  | int32 | 类别：nonconst |
| Amendment | GetNumIndifferentInterestGroups |  | int32 | 类别：nonconst |
| Amendment | GetNumOpposingInterestGroups |  | int32 | 类别：nonconst |
| Amendment | GetOnAmendedEffectsDesc |  | CString | 类别：nonconst |
| Amendment | GetOnRepealEffectsDesc |  | CString | 类别：nonconst |
| Amendment | GetOpposingInterestGroups |  | Unknown | 类别：nonconst |
| Amendment | GetOpposingInterestGroupsBreakdown |  | CString | 类别：nonconst |
| Amendment | GetOpposingInterestGroupsSummary |  | CString | 类别：nonconst |
| Amendment | GetParentLawType |  | LawType | 类别：nonconst |
| Amendment | GetSponsor |  | InterestGroup | 类别：nonconst |
| Amendment | GetTimeoutDate |  | CString | 类别：nonconst |
| Amendment | GetTooltipTag |  | CString | 类别：nonconst |
| Amendment | GetType |  | AmendmentType | 类别：nonconst |
| Amendment | HasCooldown |  | bool |  |
| Amendment | HasCooledDown |  | bool |  |
| Amendment | HasTimedOut |  | bool |  |
| Amendment | HasTimeout |  | bool |  |
| Amendment | IsActive |  | bool |  |
| Amendment | MakeScope |  | Scope |  |
| Amendment | Repeal |  | Command |  |
| Amendment | Self |  | Amendment |  |
| AmendmentType | AccessSelf |  | AmendmentType | 类别：const |
| AmendmentType | GetCustom | CustomLocalization | CString | 类别：nonconst |
| AmendmentType | GetDesc |  | CString | 类别：nonconst |
| AmendmentType | GetInstitutionModifierDesc |  | CString | 类别：nonconst |
| AmendmentType | GetIsPossibleDesc | Unknown Unknown | CString | 类别：nonconst |
| AmendmentType | GetModifier |  | Modifier | 类别：nonconst |
| AmendmentType | GetName |  | CString | 类别：nonconst |
| AmendmentType | GetNameNoFormatting |  | CString | 类别：nonconst |
| AmendmentType | GetNameWithLaw | Law | CString | 类别：nonconst |
| AmendmentType | GetOnAmendedEffectsDesc | Unknown | CString | 类别：nonconst |
| AmendmentType | GetOnRepealEffectsDesc | Unknown | CString | 类别：nonconst |
| AmendmentType | GetParentLawType |  | LawType | 类别：nonconst |
| AmendmentType | GetSponsorModifier |  | Modifier | 类别：nonconst |
| AmendmentType | GetTaxModifierDesc | Country | CString | 类别：nonconst |
| AmendmentType | GetTooltipTag |  | CString | 类别：nonconst |
| AmendmentType | GetUnlocks |  | CString | 类别：nonconst |
| AmendmentType | HasParentLaw |  | bool |  |
| AmendmentType | IsPossible | Unknown Unknown | bool |  |
| AmendmentType | MakeScope |  | Scope |  |
| AmendmentType | Self |  | AmendmentType |  |
| AnchorItem | AccessSelf |  | AnchorItem | 类别：const |
| AnchorItem | GetAnchorIndexAsString |  | CString | 类别：nonconst |
| AnchorItem | GetDisplayString |  | CString | 类别：nonconst |
| AnchorItem | GetIndexValidator |  | Unknown | 类别：nonconst |
| AnchorItem | GetTooltip |  | CString | 类别：nonconst |
| AnchorItem | IsExpanded |  | bool |  |
| AnchorItem | IsLocked |  | bool |  |
| AnchorItem | Self |  | AnchorItem |  |
| AnchorItem | SetAnchorIndexCallback |  | void |  |
| AnchorItem | ToggleExpanded |  | void |  |
| AnchorItem | ToggleLock |  | void |  |
| Application | AccessSelf |  | Application | 类别：const |
| Application | Quit |  | void |  |
| Application | Self |  | Application |  |
| Article | AccessSelf |  | Article | 类别：const |
| Article | CanWithdraw | Unknown | bool |  |
| Article | ExceedsMaxContraventions | Country | bool |  |
| Article | GetAboutToBreakReasonDesc |  | CString | 类别：nonconst |
| Article | GetArticleNumber |  | int32 | 类别：nonconst |
| Article | GetArticleType |  | ArticleType | 类别：nonconst |
| Article | GetAutoBreakReasonDesc |  | CString | 类别：nonconst |
| Article | GetBaseCost |  | CFixedPoint | 类别：nonconst |
| Article | GetBuildingType |  | BuildingType | 类别：nonconst |
| Article | GetCompany |  | Company | 类别：nonconst |
| Article | GetCostFor | Country | CFixedPoint | 类别：nonconst |
| Article | GetCostForDesc | Unknown | CString | 类别：nonconst |
| Article | GetCostWithTooltipFor | Country | CString | 类别：nonconst |
| Article | GetCountry |  | Country | 类别：nonconst |
| Article | GetCustom | CustomLocalization | CString | 类别：nonconst |
| Article | GetEffectsDesc |  | CString | 类别：nonconst |
| Article | GetFirstOrSourceCountry |  | Country | 类别：nonconst |
| Article | GetGoods |  | Goods | 类别：nonconst |
| Article | GetIcon |  | Unknown | 类别：nonconst |
| Article | GetImmediateEffectsDesc |  | CString | 类别：nonconst |
| Article | GetLaw |  | LawType | 类别：nonconst |
| Article | GetMaintenancePayer |  | Country | 类别：nonconst |
| Article | GetMutualModifierDesc |  | CString | 类别：nonconst |
| Article | GetName |  | CString | 类别：nonconst |
| Article | GetNameNoFormatting |  | CString | 类别：nonconst |
| Article | GetNameNoIcon |  | CString | 类别：nonconst |
| Article | GetNonFulfillmentDesc |  | CString | 类别：nonconst |
| Article | GetNonFulfillmentDescFor | Country | CString | 类别：nonconst |
| Article | GetQuantity |  | CFixedPoint | 类别：nonconst |
| Article | GetRelationsEffectDesc |  | CString | 类别：nonconst |
| Article | GetSecondOrTargetCountry |  | Country | 类别：nonconst |
| Article | GetShippingLane |  | ShippingLane | 类别：nonconst |
| Article | GetShortDesc |  | CString | 类别：nonconst |
| Article | GetSourceCountry |  | Country | 类别：nonconst |
| Article | GetSourceModifierDesc |  | CString | 类别：nonconst |
| Article | GetState |  | State | 类别：nonconst |
| Article | GetStrategicRegion |  | StrategicRegion | 类别：nonconst |
| Article | GetTargetCountry |  | Country | 类别：nonconst |
| Article | GetTargetModifierDesc |  | CString | 类别：nonconst |
| Article | GetText |  | CString | 类别：nonconst |
| Article | GetTooltipTag |  | CString | 类别：nonconst |
| Article | GetTreaty |  | Treaty | 类别：nonconst |
| Article | HasContraventions | Unknown | bool |  |
| Article | HasFlag | Unknown | bool |  |
| Article | HasKind | CString | bool |  |
| Article | HasType | CString | bool |  |
| Article | MakeScope |  | Scope |  |
| Article | RequiresInput | CString | bool |  |
| Article | Self |  | Article |  |
| ArticleDraft | AccessSelf |  | ArticleDraft | 类别：const |
| ArticleDraft | CanAddWarGoal | Country DiplomaticPlay | bool |  |
| ArticleDraft | CanBeModified |  | bool |  |
| ArticleDraft | CanBeModifiedDesc |  | CString |  |
| ArticleDraft | FilterGoods | CString | void |  |
| ArticleDraft | GetAcceptance | Country | int32 | 类别：nonconst |
| ArticleDraft | GetAcceptanceBreakdown | Country | CString | 类别：nonconst |
| ArticleDraft | GetArticleNumber |  | int32 | 类别：nonconst |
| ArticleDraft | GetArticleType |  | ArticleType | 类别：nonconst |
| ArticleDraft | GetBaseCost |  | CFixedPoint | 类别：nonconst |
| ArticleDraft | GetBuildingType |  | BuildingType | 类别：nonconst |
| ArticleDraft | GetCompany |  | Company | 类别：nonconst |
| ArticleDraft | GetCostFor | Country | CFixedPoint | 类别：nonconst |
| ArticleDraft | GetCostForDesc | Unknown | CString | 类别：nonconst |
| ArticleDraft | GetCostWithTooltipFor | Country | CString | 类别：nonconst |
| ArticleDraft | GetCountry |  | Country | 类别：nonconst |
| ArticleDraft | GetEffectsDesc |  | CString | 类别：nonconst |
| ArticleDraft | GetFirstOrSource |  | Country | 类别：nonconst |
| ArticleDraft | GetGoods |  | Goods | 类别：nonconst |
| ArticleDraft | GetIcon |  | Unknown | 类别：nonconst |
| ArticleDraft | GetImmediateEffectsDesc |  | CString | 类别：nonconst |
| ArticleDraft | GetLawType |  | LawType | 类别：nonconst |
| ArticleDraft | GetMaintenancePayer |  | Country | 类别：nonconst |
| ArticleDraft | GetMaxValidQuantity |  | int32 | 类别：nonconst |
| ArticleDraft | GetMinValidQuantity |  | int32 | 类别：nonconst |
| ArticleDraft | GetMutualModifierDesc |  | CString | 类别：nonconst |
| ArticleDraft | GetName |  | CString | 类别：nonconst |
| ArticleDraft | GetNameNoFormatting |  | CString | 类别：nonconst |
| ArticleDraft | GetNameNoIcon |  | CString | 类别：nonconst |
| ArticleDraft | GetNumInputs |  | int32 | 类别：nonconst |
| ArticleDraft | GetQuantity |  | CFixedPoint | 类别：nonconst |
| ArticleDraft | GetQuantityPercentage |  | float | 类别：nonconst |
| ArticleDraft | GetQuantityValidator |  | Unknown | 类别：nonconst |
| ArticleDraft | GetRelationsEffectDesc |  | CString | 类别：nonconst |
| ArticleDraft | GetRequiredInputsDesc |  | CString | 类别：nonconst |
| ArticleDraft | GetSecondOrTarget |  | Country | 类别：nonconst |
| ArticleDraft | GetShortDesc |  | CString | 类别：nonconst |
| ArticleDraft | GetSourceModifierDesc |  | CString | 类别：nonconst |
| ArticleDraft | GetState |  | State | 类别：nonconst |
| ArticleDraft | GetStrategicRegion |  | StrategicRegion | 类别：nonconst |
| ArticleDraft | GetTargetModifierDesc |  | CString | 类别：nonconst |
| ArticleDraft | GetText |  | CString | 类别：nonconst |
| ArticleDraft | GetValidBuildingTypes |  | Unknown | 类别：nonconst |
| ArticleDraft | GetValidCompanies |  | Unknown | 类别：nonconst |
| ArticleDraft | GetValidCountries |  | Unknown | 类别：nonconst |
| ArticleDraft | GetValidGoods |  | Unknown | 类别：nonconst |
| ArticleDraft | GetValidLaws | LawType | Unknown | 类别：nonconst |
| ArticleDraft | GetValidStates |  | Unknown | 类别：nonconst |
| ArticleDraft | GetValidStrategicRegions |  | Unknown | 类别：nonconst |
| ArticleDraft | GetWarGoalInfamyValue | Country | CFixedPoint | 类别：nonconst |
| ArticleDraft | GetWarGoalInfamyValueDesc | Unknown | CString | 类别：nonconst |
| ArticleDraft | GetWarGoalManeuversCost | Unknown Unknown | int32 | 类别：nonconst |
| ArticleDraft | GetWarGoalManeuversCostDesc | Unknown Unknown | CString | 类别：nonconst |
| ArticleDraft | HasAllRequiredInputsSet |  | bool |  |
| ArticleDraft | HasFlag | Unknown | bool |  |
| ArticleDraft | HasInputValue | CString | bool |  |
| ArticleDraft | HasKind | CString | bool |  |
| ArticleDraft | HasType | CString | bool |  |
| ArticleDraft | IsLawTypeValidInput | LawType | bool |  |
| ArticleDraft | IsPossible |  | bool |  |
| ArticleDraft | IsSelectedGoods | CString | bool |  |
| ArticleDraft | IsVisible |  | bool |  |
| ArticleDraft | OnInputTextChanged |  | void |  |
| ArticleDraft | OnQuantityChanged |  | void |  |
| ArticleDraft | OnQuantityChangedSlider |  | void |  |
| ArticleDraft | OnTextChanged |  | void |  |
| ArticleDraft | RequiresAnyInput |  | bool |  |
| ArticleDraft | RequiresInput | CString | bool |  |
| ArticleDraft | Self |  | ArticleDraft |  |
| ArticleDraft | SetBuildingType | BuildingType | void |  |
| ArticleDraft | SetCompany | Company | void |  |
| ArticleDraft | SetCountry | Country | void |  |
| ArticleDraft | SetGood | Goods | void |  |
| ArticleDraft | SetLaw | LawType | void |  |
| ArticleDraft | SetQuantity | Unknown | void |  |
| ArticleDraft | SetState | State | void |  |
| ArticleDraft | SetStrategicRegion | StrategicRegion | void |  |
| ArticleDraft | SetText | Unknown | void |  |
| ArticleDraft | SortGoods | CString | void |  |
| ArticleType | AccessSelf |  | ArticleType | 类别：const |
| ArticleType | GetCost |  | CFixedPoint | 类别：nonconst |
| ArticleType | GetCostFor | Unknown Unknown Unknown | CFixedPoint | 类别：nonconst |
| ArticleType | GetCostForDesc | Unknown Unknown Unknown | CString | 类别：nonconst |
| ArticleType | GetDailyRelationsProgress |  | CFixedPoint | 类别：nonconst |
| ArticleType | GetDesc |  | CString | 类别：nonconst |
| ArticleType | GetEffectsDesc |  | CString | 类别：nonconst |
| ArticleType | GetIcon |  | Unknown | 类别：nonconst |
| ArticleType | GetIsAvailableDesc | Unknown Unknown | CString | 类别：nonconst |
| ArticleType | GetIsPossibleDesc | Unknown Unknown | CString | 类别：nonconst |
| ArticleType | GetIsVisibleDesc | Unknown Unknown | CString | 类别：nonconst |
| ArticleType | GetName |  | CString | 类别：nonconst |
| ArticleType | GetNameNoFormatting |  | CString | 类别：nonconst |
| ArticleType | GetNameNoIcon |  | CString | 类别：nonconst |
| ArticleType | GetNumInputs |  | int32 | 类别：nonconst |
| ArticleType | GetRelationsEffectDesc |  | CString | 类别：nonconst |
| ArticleType | GetRelationsImprovementMax |  | int32 | 类别：nonconst |
| ArticleType | GetRelationsImprovementMin |  | int32 | 类别：nonconst |
| ArticleType | GetTooltipTag |  | CString | 类别：nonconst |
| ArticleType | HasFlag | CString | bool |  |
| ArticleType | HasKind | Unknown | bool |  |
| ArticleType | HasType | CString | bool |  |
| ArticleType | IsAvailable | Country Country | bool |  |
| ArticleType | IsPossible | Unknown Unknown | bool |  |
| ArticleType | IsVisible | Country Country | bool |  |
| ArticleType | RequiresAnyInput |  | bool |  |
| ArticleType | Self |  | ArticleType |  |
| Attribute | AccessSelf |  | Attribute | 类别：const |
| Attribute | GetName |  | CString | 类别：nonconst |
| Attribute | GetValue |  | float | 类别：nonconst |
| Attribute | OnValueChanged |  | void |  |
| Attribute | Self |  | Attribute |  |
| AvailabilityEntry | AccessSelf |  | AvailabilityEntry | 类别：const |
| AvailabilityEntry | GetAvailabilityString |  | CUTF8String | 类别：nonconst |
| AvailabilityEntry | Self |  | AvailabilityEntry |  |
| Battle | AccessAttackerBattleParticipant |  | BattleParticipant | 类别：const |
| Battle | AccessAttackerModifier |  | Modifier | 类别：const |
| Battle | AccessBorrowedAttackerBuildingEntries |  | Unknown | 类别：const |
| Battle | AccessBorrowedDefenderBuildingEntries |  | Unknown | 类别：const |
| Battle | AccessCommandedAttackerBuildingEntries |  | Unknown | 类别：const |
| Battle | AccessCommandedDefenderBuildingEntries |  | Unknown | 类别：const |
| Battle | AccessCountryTrendPairs |  | Unknown | 类别：const |
| Battle | AccessDefenderBattleParticipant |  | BattleParticipant | 类别：const |
| Battle | AccessDefenderModifier |  | Modifier | 类别：const |
| Battle | AccessManpowerTrendPairs |  | Unknown | 类别：const |
| Battle | AccessSelf |  | Battle | 类别：const |
| Battle | CalcCurrentAttackerManpower |  | int64 |  |
| Battle | CalcCurrentAttackerMorale |  | CFixedPoint |  |
| Battle | CalcCurrentDefenderManpower |  | int64 |  |
| Battle | CalcCurrentDefenderMorale |  | CFixedPoint |  |
| Battle | CalcPushOfWar |  | CFixedPoint |  |
| Battle | EndedInconclusively |  | bool |  |
| Battle | GetAttacker |  | Country | 类别：非常量 |
| Battle | GetAttackerBorrowedFormations |  | Unknown | 类别：非常量 |
| Battle | GetAttackerCondition |  | BattleCondition | 类别：非常量 |
| Battle | GetAttackerConditionUpdateDesc |  | CString | 类别：非常量 |
| Battle | GetAttackerEndCE |  | CFixedPoint | 类别：非常量 |
| Battle | GetAttackerLostUnits |  | int32 | 类别：非常量 |
| Battle | GetAttackerModifier |  | Modifier | 类别：非常量 |
| Battle | GetAttackerNumWantedUnitsDesc |  | CString | 类别：非常量 |
| Battle | GetAttackerStartCE |  | CFixedPoint | 类别：非常量 |
| Battle | GetAttackerStatistics |  | Unknown | 类别：非常量 |
| Battle | GetAttackerStillFightingTrend |  | DataTrend | 类别：非常量 |
| Battle | GetAttackerTotalDead |  | CFixedPoint | 类别：非常量 |
| Battle | GetAttackerTotalDemoralized |  | CFixedPoint | 类别：非常量 |
| Battle | GetAttackerTotalWounded |  | CFixedPoint | 类别：非常量 |
| Battle | GetAttackerTrend |  | DataTrend | 类别：非常量 |
| Battle | GetAttackerUnderCommandBreakdown |  | CString | 类别：非常量 |
| Battle | GetBattleIcon |  | Unknown | 类别：非常量 |
| Battle | GetBattleUnitFormation | MilitaryFormation | BattleMilitaryFormation | 类别：非常量 |
| Battle | GetBattleUnitTypeList | MilitaryFormation | Unknown | 类别：非常量 |
| Battle | GetCapturingCountry |  | Country | 类别：非常量 |
| Battle | GetCustom | CustomLocalization | CString | 类别：非常量 |
| Battle | GetDateDesc |  | CString | 类别：非常量 |
| Battle | GetDefender |  | Country | 类别：非常量 |
| Battle | GetDefenderBorrowedFormations |  | Unknown | 类别：非常量 |
| Battle | GetDefenderCondition |  | BattleCondition | 类别：非常量 |
| Battle | GetDefenderConditionUpdateDesc |  | CString | 类别：非常量 |
| Battle | GetDefenderEndCE |  | CFixedPoint | 类别：非常量 |
| Battle | GetDefenderLostUnits |  | int32 | 类别：非常量 |
| Battle | GetDefenderModifier |  | Modifier | 类别：非常量 |
| Battle | GetDefenderNumWantedUnitsDesc |  | CString | 类别：非常量 |
| Battle | GetDefenderStartCE |  | CFixedPoint | 类别：非常量 |
| Battle | GetDefenderStatistics |  | Unknown | 类别：非常量 |
| Battle | GetDefenderStillFightingTrend |  | DataTrend | 类别：非常量 |
| Battle | GetDefenderTotalDead |  | CFixedPoint | 类别：非常量 |
| Battle | GetDefenderTotalDemoralized |  | CFixedPoint | 类别：非常量 |
| Battle | GetDefenderTotalWounded |  | CFixedPoint | 类别：非常量 |
| Battle | GetDefenderTrend |  | DataTrend | 类别：非常量 |
| Battle | GetDefenderUnderCommandBreakdown |  | CString | 类别：非常量 |
| Battle | GetDefenseRaw |  | CFixedPoint | 类别：非常量 |
| Battle | GetDurationInDaysRaw |  | int32 | 类别：非常量 |
| Battle | GetEndDate |  | CString | 类别：非常量 |
| Battle | GetEndingAttackerMorale |  | CFixedPoint | 类别：非常量 |
| Battle | GetEndingDefenderMorale |  | CFixedPoint | 类别：非常量 |
| Battle | GetFinalAttackerManpower |  | int64 | 类别：非常量 |
| Battle | GetFinalAttackerUnits |  | int32 | 类别：非常量 |
| Battle | GetFinalDefenderManpower |  | int64 | 类别：非常量 |
| Battle | GetFinalDefenderUnits |  | int32 | 类别：非常量 |
| Battle | GetInitialAttackerMorale |  | CFixedPoint | 类别：非常量 |
| Battle | GetInitialDefenderMorale |  | CFixedPoint | 类别：非常量 |
| Battle | GetLocationName |  | CString | 类别：非常量 |
| Battle | GetLoosingProvincesCountry |  | Country | 类别：非常量 |
| Battle | GetLoser |  | Country | 类别：非常量 |
| Battle | GetMaxNumberInBattleTrends |  | CFixedPoint | 类别：非常量 |
| Battle | GetMaxNumberInManpowerTrends |  | CFixedPoint | 类别：非常量 |
| Battle | GetName |  | CString | 类别：非常量 |
| Battle | GetNumCapturedProvinces |  | int32 | 类别：非常量 |
| Battle | GetOccupationWon |  | CString | 类别：非常量 |
| Battle | GetOccupationWonRaw |  | CFixedPoint | 类别：非常量 |
| Battle | GetOffenseRaw |  | CFixedPoint | 类别：非常量 |
| Battle | GetProvince |  | Province | 类别：非常量 |
| Battle | GetStartDate |  | CString | 类别：非常量 |
| Battle | GetStartingAttackerManpower |  | int64 | 类别：非常量 |
| Battle | GetStartingAttackerUnits |  | int32 | 类别：非常量 |
| Battle | GetStartingDefenderManpower |  | int64 | 类别：非常量 |
| Battle | GetStartingDefenderUnits |  | int32 | 类别：非常量 |
| Battle | GetState |  | State | 类别：非常量 |
| Battle | GetStatusString |  | CString | 类别：非常量 |
| Battle | GetTerrain |  | CString | 类别：非常量 |
| Battle | GetTerrainDesc |  | CString | 类别：非常量 |
| Battle | GetTooltipTag |  | CString | 类别：非常量 |
| Battle | GetUnitIcon |  | CString | 类别：非常量 |
| Battle | GetVictoryScore |  | CString | 类别：非常量 |
| Battle | GetVictoryScoreRaw |  | CFixedPoint | 类别：非常量 |
| Battle | GetWinner |  | Country | 类别：非常量 |
| Battle | HasEnded |  | bool |  |
| Battle | HasInvasion |  | bool |  |
| Battle | IsActive |  | bool |  |
| Battle | IsBeingHighlighted |  | bool |  |
| Battle | IsBeingTutorialHighlighted |  | bool |  |
| Battle | IsLandBattle |  | bool |  |
| Battle | IsLeadCountry | Country | bool |  |
| Battle | IsLoser | Country | bool |  |
| Battle | IsManpowerTrendsEmpty |  | bool |  |
| Battle | IsNavalBattle |  | bool |  |
| Battle | IsNavalInvasionLandingBattle |  | bool |  |
| Battle | IsOnLoserSide | Country | bool |  |
| Battle | IsOnWinnerSide | Country | bool |  |
| Battle | IsRelevantForCountry | Country | bool |  |
| Battle | IsValid |  | bool |  |
| Battle | IsWinner | Country | bool |  |
| Battle | IsZoomingToMapMarkerPosition |  | bool |  |
| Battle | LostOrCapturedProvinces | Unknown | bool |  |
| Battle | MakeScope |  | Scope |  |
| Battle | Self |  | Battle |  |
| Battle | ZoomToMapMarkerPosition |  | void |  |
| BattleBuildingEntry | AccessSelf |  | BattleBuildingEntry | 类别：常量 |
| BattleBuildingEntry | GetAverageMorale |  | CFixedPoint | 类别：非常量 |
| BattleBuildingEntry | GetBuilding |  | Building | 类别：非常量 |
| BattleBuildingEntry | GetUnits |  | Unknown | 类别：非常量 |
| BattleBuildingEntry | IsExpanded |  | bool |  |
| BattleBuildingEntry | IsUnderDirectCommand |  | bool |  |
| BattleBuildingEntry | Self |  | BattleBuildingEntry |  |
| BattleBuildingEntry | ToggleExpand |  | void |  |
| BattleCondition | AccessSelf |  | BattleCondition | 类别：常量 |
| BattleCondition | GetDesc |  | CString | 类别：非常量 |
| BattleCondition | GetModifierDesc |  | CString | 类别：非常量 |
| BattleCondition | GetName |  | CString | 类别：非常量 |
| BattleCondition | GetNameNoFormatting |  | CString | 类别：非常量 |
| BattleCondition | GetTexture |  | Unknown | 类别：非常量 |
| BattleCondition | GetTooltipTag |  | CString | 类别：非常量 |
| BattleCondition | IsValid |  | bool |  |
| BattleCondition | Self |  | BattleCondition |  |
| BattleMarker | AccessSelf |  | BattleMarker | 类别：常量 |
| BattleMarker | GetBattle |  | Battle | 类别：非常量 |
| BattleMarker | GetPosition |  | CVector2f | 类别：非常量 |
| BattleMarker | Self |  | BattleMarker |  |
| BattleMilitaryFormation | AccessSelf |  | BattleMilitaryFormation | 类别：常量 |
| BattleMilitaryFormation | GetAverageDefense |  | CFixedPoint | 类别：非常量 |
| BattleMilitaryFormation | GetAverageOffense |  | CFixedPoint | 类别：非常量 |
| BattleMilitaryFormation | GetCurrentManpowerFromFormation |  | int64 | 类别：非常量 |
| BattleMilitaryFormation | GetCurrentMorale |  | CFixedPoint | 类别：非常量 |
| BattleMilitaryFormation | GetMaxManpowerFromFormation |  | int64 | 类别：非常量 |
| BattleMilitaryFormation | GetTotalUnitsFromFormation |  | int32 | 类别：非常量 |
| BattleMilitaryFormation | Self |  | BattleMilitaryFormation |  |
| BattlePanel | AccessSelf |  | BattlePanel | 类别：常量 |
| BattlePanel | GetBattle |  | Battle | 类别：非常量 |
| BattlePanel | Self |  | BattlePanel |  |
| BattleParticipant | AccessCountry |  | Country | 类别：常量 |
| BattleParticipant | AccessSelf |  | BattleParticipant | 类别：常量 |
| BattleParticipant | GetCountry |  | Country | 类别：非常量 |
| BattleParticipant | GetMorale |  | CFixedPoint | 类别：非常量 |
| BattleParticipant | GetNumCombatUnits |  | int32 | 类别：非常量 |
| BattleParticipant | Self |  | BattleParticipant |  |
| BattleParticipantsPanel | AccessCombatUnits |  | Unknown | 类别：常量 |
| BattleParticipantsPanel | AccessSelf |  | BattleParticipantsPanel | 类别：常量 |
| BattleParticipantsPanel | GetBattle |  | Battle | 类别：非常量 |
| BattleParticipantsPanel | GetHeaderText |  | CString | 类别：非常量 |
| BattleParticipantsPanel | Self |  | BattleParticipantsPanel |  |
| BattleSide | AccessSelf |  | BattleSide | 类别：常量 |
| BattleSide | GetIconFrame |  | int32 | 类别：非常量 |
| BattleSide | GetNumUnits |  | int32 | 类别：非常量 |
| BattleSide | GetNumUnitsAtEndOfBattleDesc |  | CString | 类别：非常量 |
| BattleSide | GetNumUnitsAtStartOfBattleDesc |  | CString | 类别：非常量 |
| BattleSide | GetNumUnitsDesc |  | CString | 类别：非常量 |
| BattleSide | GetOutcome |  | CString | 类别：非常量 |
| BattleSide | GetStatus |  | CString | 类别：非常量 |
| BattleSide | GetStatusDesc |  | CString | 类别：非常量 |
| BattleSide | HasEscaped |  | bool |  |
| BattleSide | HasLost |  | bool |  |
| BattleSide | HasWon |  | bool |  |
| BattleSide | IsAttacker |  | bool |  |
| BattleSide | IsDefender |  | bool |  |
| BattleSide | Self |  | BattleSide |  |
| BattleUnitType | AccessSelf |  | BattleUnitType | 类别：常量 |
| BattleUnitType | GetAverageMorale |  | CFixedPoint | 类别：非常量 |
| BattleUnitType | GetCombatUnitType |  | CombatUnitType | 类别：非常量 |
| BattleUnitType | GetIDString | Battle MilitaryFormation | CString | 类别：非常量 |
| BattleUnitType | GetNumberOfConscriptUnits |  | int32 | 类别：非常量 |
| BattleUnitType | GetNumberOfRegularUnits |  | int32 | 类别：非常量 |
| BattleUnitType | GetUnits |  | Unknown | 类别：非常量 |
| BattleUnitType | Self |  | BattleUnitType |  |
| BlurThreshold | AccessSelf |  | BlurThreshold | 类别：常量 |
| BlurThreshold | GetValue |  | float | 类别：非常量 |
| BlurThreshold | Self |  | BlurThreshold |  |
| BlurThreshold | SetValue |  | void |  |
| BlurThreshold | SetValueStr |  | void |  |
| BrushBool | AccessSelf |  | BrushBool | 类别：常量 |
| BrushBool | Get |  | bool |  |
| BrushBool | Self |  | BrushBool |  |
| BrushBool | Set |  | void |  |
| BrushBool | Toggle |  | void |  |
| BrushFloat | AccessSelf |  | BrushFloat | 类别：常量 |
| BrushFloat | DecreaseBySmallStep |  | void |  |
| BrushFloat | DecreaseByStep |  | void |  |
| BrushFloat | IncreaseBySmallStep |  | void |  |
| BrushFloat | IncreaseByStep |  | void |  |
| BrushFloat | Max |  | float |  |
| BrushFloat | Min |  | float |  |
| BrushFloat | ScaledValue | Unknown | float |  |
| BrushFloat | Self |  | BrushFloat |  |
| BrushFloat | SetMax |  | void |  |
| BrushFloat | SetMin |  | void |  |
| BrushFloat | SetScaledValue | Unknown | void |  |
| BrushFloat | SetStepSize |  | void |  |
| BrushFloat | SetValue |  | void |  |
| BrushFloat | SetValueArg | Unknown | void |  |
| BrushFloat | SetValueFromWidget | PdxGuiWidget | void |  |
| BrushFloat | SmallStepSize |  | float |  |
| BrushFloat | StepSize |  | float |  |
| BrushFloat | Value |  | float |  |
| BrushSettings | AccessSelf |  | BrushSettings | 类别：常量 |
| BrushSettings | Amount |  | BrushFloat |  |
| BrushSettings | Diameter |  | float |  |
| BrushSettings | Hardness |  | BrushFloat |  |
| BrushSettings | PixelSnap |  | BrushBool |  |
| BrushSettings | Radius |  | BrushFloat |  |
| BrushSettings | Self |  | BrushSettings |  |
| BrushSettings | SetAmount |  | void |  |
| BrushSettings | SetDiameter |  | void |  |
| BrushSettings | SetHardness |  | void |  |
| BrushSettingsDropdown | AccessSelf |  | BrushSettingsDropdown | 类别：常量 |
| BrushSettingsDropdown | GetBrushDiameter |  | float | 类别：非常量 |
| BrushSettingsDropdown | Self |  | BrushSettingsDropdown |  |
| BrushSettingsDropdown | Settings |  | BrushSettings |  |
| BrushSettingsDropdown | Thumbnail |  | Unknown |  |
| BrushSettingsDropdown | Toggle |  | void |  |
| BrushSettingsGlobal | AccessSelf |  | BrushSettingsGlobal | 类别：常量 |
| BrushSettingsGlobal | GetDisplayAmountNames |  | Unknown | 类别：非常量 |
| BrushSettingsGlobal | IsDisplayAmountActive | Unknown | bool |  |
| BrushSettingsGlobal | Self |  | BrushSettingsGlobal |  |
| BrushSettingsGlobal | SetIsDisplayAmountFromString | Unknown | void |  |
| BudgetPanel | AccessSelf |  | BudgetPanel | 类别：常量 |
| BudgetPanel | AccessTaxableGoods |  | Unknown | 类别：常量 |
| BudgetPanel | AccessTaxedGoods |  | Unknown | 类别：常量 |
| BudgetPanel | CanTaxGoods |  | bool |  |
| BudgetPanel | Filter | Unknown | void |  |
| BudgetPanel | GetFilters |  | Unknown | 类别：非常量 |
| BudgetPanel | IsAddConsumptionTaxMenuOpen |  | bool |  |
| BudgetPanel | IsSelected | Unknown | bool |  |
| BudgetPanel | Self |  | BudgetPanel |  |
| BudgetPanel | ToggleAddConsumptionTaxMenu | Unknown | void |  |
| Building | AccessConsumedGoods |  | Unknown | 类别：常量 |
| Building | AccessModifier |  | Modifier | 类别：常量 |
| Building | AccessOwnerPopsList |  | PopList | 类别：常量 |
| Building | AccessPopsList |  | PopList | 类别：常量 |
| Building | AccessProducedGoods |  | Unknown | 类别：常量 |
| Building | AccessProductionMethod | ProductionMethodGroup | ProductionMethod | 类别：常量 |
| Building | AccessProductionMethodGroups |  | Unknown | 类别：常量 |
| Building | AccessSelf |  | Building | 类别：常量 |
| Building | AccessShortageGoods |  | Unknown | 类别：常量 |
| Building | AccessState |  | State | 类别：常量 |
| Building | AccessStateRegion |  | StateRegion | 类别：常量 |
| Building | CalcInfrastructureUsage |  | CFixedPoint |  |
| Building | CalcInputAvailabilityOutputMult |  | CFixedPoint |  |
| Building | CalcInputGoodsShortageTargetPenalty |  | CFixedPoint |  |
| Building | CalcInputGoodsShortageTargetPenaltyFromGoods | Unknown | CFixedPoint |  |
| Building | CalcUrbanizationProvided |  | int32 |  |
| Building | CanBeAffectedByInputShortage | ModifierEntry | bool |  |
| Building | CanBePrivatized |  | bool |  |
| Building | CancelConstruction |  | Command |  |
| Building | Downsize |  | Command |  |
| Building | GetAdjustHiringTargetDesc |  | CString | 类别：非常量 |
| Building | GetAllEmployeesTransferDesc |  | CString | 类别：非常量 |
| Building | GetAllFailedHiresDesc |  | CString | 类别：非常量 |
| Building | GetArmyManpower |  | int64 | 类别：非常量 |
| Building | GetArmyReadinessStatusDesc |  | CString | 类别：非常量 |
| Building | GetAutoDownsizeTooltip |  | CString | 类别：非常量 |
| Building | GetAutoExpandTooltip |  | CString | 类别：非常量 |
| Building | GetAutoExpandTriggers |  | CString | 类别：非常量 |
| Building | GetAverageAnnualEarningsPerEmployee |  | CFixedPoint | 类别：非常量 |
| Building | GetAverageAnnualEarningsPerEmployeeFormatted |  | CString | 类别：非常量 |
| Building | GetAverageAnnualWage |  | CFixedPoint | 类别：非常量 |
| Building | GetAverageAnnualWageBreakdown |  | CString | 类别：非常量 |
| Building | GetAverageAnnualWageBreakdownForPopType | PopType | CString | 类别：非常量 |
| Building | GetAverageAnnualWageForPopType | PopType | CFixedPoint | 类别：非常量 |
| Building | GetAverageAnnualWageForPopTypeDesc | Unknown | CString | 类别：非常量 |
| Building | GetAverageAnnualWageSubsidies |  | CFixedPoint | 类别：非常量 |
| Building | GetAverageStandardOfLiving |  | CFixedPoint | 类别：非常量 |
| Building | GetBalance |  | CFixedPoint | 类别：非常量 |
| Building | GetBalanceDesc |  | CString | 类别：非常量 |
| Building | GetBuildingAssets |  | Unknown | 类别：非常量 |
| Building | GetBuildingGroupName |  | CString | 类别：非常量 |
| Building | GetBuildingOwnerships |  | Unknown | 类别：非常量 |
| Building | GetBuildingType |  | BuildingType | 类别：非常量 |
| Building | GetCancelConstructionTooltip |  | CString | 类别：非常量 |
| Building | GetCappedAssetsLong |  | Unknown | 类别：非常量 |
| Building | GetCappedAssetsLongRest |  | Unknown | 类别：非常量 |
| Building | GetCappedAssetsShort |  | Unknown | 类别：非常量 |
| Building | GetCappedAssetsShortRest |  | Unknown | 类别：非常量 |
| Building | GetCappedOwnersLong |  | Unknown | 类别：非常量 |
| Building | GetCappedOwnersLongRest |  | Unknown | 类别：非常量 |
| Building | GetCappedOwnersShort |  | Unknown | 类别：非常量 |
| Building | GetCappedOwnersShortRest |  | Unknown | 类别：非常量 |
| Building | GetCashReservesTrend |  | DataTrend | 类别：非常量 |
| Building | GetCasualtiesDesc |  | CString | 类别：非常量 |
| Building | GetChangeProductionMethodPopQualificationsWarningBreakdown | ProductionMethod | CString | 类别：非常量 |
| Building | GetCombatUnitCapacity |  | int32 | 类别：非常量 |
| Building | GetCombatUnitCapacityDesc |  | CString | 类别：非常量 |
| Building | GetCombatUnitProduction |  | CString | 类别：非常量 |
| Building | GetCombatUnitProductionBreakdown |  | CString | 类别：非常量 |
| Building | GetCombatUnitTypes |  | Unknown | 类别：非常量 |
| Building | GetCombatUnits |  | Unknown | 类别：非常量 |
| Building | GetCombatUnitsIcon |  | CString | 类别：非常量 |
| Building | GetCombatUnitsInFormation | MilitaryFormation | Unknown | 类别：非常量 |
| Building | GetCompany |  | Company | 类别：非常量 |
| Building | GetConstructionProgressPercentage |  | float | 类别：非常量 |
| Building | GetConstructionRemainingWeeksDesc |  | CString | 类别：非常量 |
| Building | GetConstructionSpeedPerWeek |  | CFixedPoint | 类别：非常量 |
| Building | GetConstructionSpeedPerWeekDesc |  | CString | 类别：非常量 |
| Building | GetConsumption | Goods | CFixedPoint | 类别：非常量 |
| Building | GetConsumptionDesc | Goods | CString | 类别：非常量 |
| Building | GetConsumptionValue | Goods | CFixedPoint | 类别：非常量 |
| Building | GetCurrentCashReserves |  | CFixedPoint | 类别：非常量 |
| Building | GetCustom | CustomLocalization | CString | 类别：非常量 |
| Building | GetDebugTooltip |  | CString | 类别：非常量 |
| Building | GetDefaultOutputGoods |  | Goods | 类别：非常量 |
| Building | GetDownsizeTooltip |  | CString | 类别：非常量 |
| Building | GetEarnings |  | CFixedPoint | 类别：非常量 |
| Building | GetEarningsPerEmployeeTrend |  | DataTrend | 类别：非常量 |
| Building | GetEmployeeCap |  | int64 | 类别：非常量 |
| Building | GetEmployeesBreakdown |  | CString | 类别：非常量 |
| Building | GetEmployeesTransferDesc | PopType | CString | 类别：非常量 |
| Building | GetEmploymentPercentage |  | CFixedPoint | 类别：非常量 |
| Building | GetEmploymentTooltip |  | CString | 类别：非常量 |
| Building | GetEstablishmentDate |  | CString | 类别：非常量 |
| Building | GetExpansionLevel |  | int32 | 类别：非常量 |
| Building | GetExpansionLevelBreakdown |  | CString | 类别：非常量 |
| Building | GetExpansionLevelBreakdownDesc |  | CString | 类别：非常量 |
| Building | GetExpansionLevelDesc |  | CString | 类别：非常量 |
| Building | GetExpansionLevelsInQueue |  | int32 | 类别：非常量 |
| Building | GetFailedHiresDesc | PopType | CString | 类别：非常量 |
| Building | GetGoodsShortageListDesc |  | CString | 类别：非常量 |
| Building | GetGovernmentExpenses |  | CFixedPoint | 类别：非常量 |
| Building | GetGovernmentExpensesDesc |  | CString | 类别：非常量 |
| Building | GetHQ |  | Hq | 类别：非常量 |
| Building | GetID |  | int32 | 类别：非常量 |
| Building | GetIDString |  | CString | 类别：非常量 |
| Building | GetIcon |  | Unknown | 类别：非常量 |
| Building | GetInfrastructureUsageBreakdown |  | CString | 类别：非常量 |
| Building | GetInputMult |  | CFixedPoint | 类别：非常量 |
| Building | GetInputMultDesc |  | CString | 类别：非常量 |
| Building | GetInputOutputTooltip |  | CString | 类别：非常量 |
| Building | GetInputShortagePenalty |  | CFixedPoint | 类别：非常量 |
| Building | GetLastIncome |  | CFixedPoint | 类别：非常量 |
| Building | GetLastMaterialExpenses |  | CFixedPoint | 类别：非常量 |
| Building | GetLastMaterialExpensesDesc |  | CString | 类别：非常量 |
| Building | GetLastRevenue |  | CFixedPoint | 类别：非常量 |
| Building | GetLastRevenueBalancedSI | CFixedPoint int32 | CString | 类别：非常量 |
| Building | GetLastSlaveBasket |  | int32 | 类别：非常量 |
| Building | GetLastSlaveBasketDesc |  | CString | 类别：非常量 |
| Building | GetLastSlaveUpkeep |  | CFixedPoint | 类别：非常量 |
| Building | GetLastSlaveUpkeepDesc |  | CString | 类别：非常量 |
| Building | GetLastWagesExpenses |  | CFixedPoint | 类别：非常量 |
| Building | GetLastWagesExpensesDesc |  | CString | 类别：非常量 |
| Building | GetManpowerCapacity |  | int64 | 类别：非常量 |
| Building | GetMaxCashReserves |  | CFixedPoint | 类别：非常量 |
| Building | GetMaxPopSize | PopType | int64 | 类别：非常量 |
| Building | GetMaxPopSizeDesc | PopType | CString | 类别：非常量 |
| Building | GetMilitaryFormations |  | Unknown | 类别：非常量 |
| Building | GetMobilizationRatio |  | CFixedPoint | 类别：非常量 |
| Building | GetModifier |  | Modifier | 类别：非常量 |
| Building | GetName |  | CString | 类别：非常量 |
| Building | GetNameNoFormatting |  | CString | 类别：非常量 |
| Building | GetNationalizeBuildingNoCompensationDesc | Unknown | CString | 类别：非常量 |
| Building | GetNationalizeBuildingWithCompensationDesc | Unknown | CString | 类别：非常量 |
| Building | GetNavyManpower |  | int64 | 类别：非常量 |
| Building | GetNoLevelsCanBeNationalizedDesc |  | CString | 类别：非常量 |
| Building | GetNoOfEmployed |  | int64 | 类别：非常量 |
| Building | GetNotHiringReasonDesc |  | CString | 类别：非常量 |
| Building | GetNumActiveUnitsProvidedToFormation | MilitaryFormation | int32 | 类别：非常量 |
| Building | GetNumEmployeesOfType | PopType | int64 | 类别：非常量 |
| Building | GetNumLevelsCanBeNationalized |  | int32 | 类别：非常量 |
| Building | GetNumOwnedLevels |  | int32 | 类别：非常量 |
| Building | GetNumUnitsOfCombatUnitType | CombatUnitType | int32 | 类别：非常量 |
| Building | GetNumUnitsOfCombatUnitTypeProvidedToFormation | Unknown Unknown | int32 | 类别：非常量 |
| Building | GetNumberOfCombatUnits |  | int32 | 类别：非常量 |
| Building | GetNumberOfFullyMobilizedBattalions |  | int32 | 类别：非常量 |
| Building | GetOutputPercentage | Goods | CFixedPoint | 类别：非常量 |
| Building | GetOutputRatio |  | CFixedPoint | 类别：非常量 |
| Building | GetOwner |  | Country | 类别：非常量 |
| Building | GetPopTypeFullyReplacedDesc | PopType | CString | 类别：非常量 |
| Building | GetPopTypeReplacementDesc | PopType | CString | 类别：非常量 |
| Building | GetPrivatizationTooltip |  | CString | 类别：非常量 |
| Building | GetProducedModifiers |  | Modifier | 类别：非常量 |
| Building | GetProduction | Goods | CFixedPoint | 类别：非常量 |
| Building | GetProductionDesc | Goods | CString | 类别：非常量 |
| Building | GetProductionMethodGroup | Unknown | ProductionMethodGroup | 类别：非常量 |
| Building | GetProductionValue | Goods | CFixedPoint | 类别：非常量 |
| Building | GetProfitability |  | CString | 类别：非常量 |
| Building | GetProfitabilityCompareIcon |  | CString | 类别：非常量 |
| Building | GetProfitabilityCompareIconInType |  | CString | 类别：非常量 |
| Building | GetProfitabilityInType |  | CString | 类别：非常量 |
| Building | GetProfitabilityInTypeTrend |  | DataTrend | 类别：非常量 |
| Building | GetProfitabilityRank |  | int32 | 类别：非常量 |
| Building | GetProfitabilityRankInType |  | int32 | 类别：非常量 |
| Building | GetProfitabilityTrend |  | DataTrend | 类别：非常量 |
| Building | GetQueueConstructionPopQualificationsWarningBreakdown |  | CString | 类别：非常量 |
| Building | GetQueueConstructionTooltip |  | CString | 类别：非常量 |
| Building | GetQueueMilitaryConstructionTooltip | MilitaryFormation CombatUnitType | CString | 类别：非常量 |
| Building | GetResetProductionMethodsToStandardTooltip |  | CString | 类别：非常量 |
| Building | GetSamplePops |  | Unknown | 类别：非常量 |
| Building | GetSizeTooltip |  | CString | 类别：非常量 |
| Building | GetState |  | State | 类别：非常量 |
| Building | GetStateRegion |  | StateRegion | 类别：非常量 |
| Building | GetStatusDesc |  | CString | 类别：非常量 |
| Building | GetSubsidies |  | CFixedPoint | 类别：非常量 |
| Building | GetSubsidiesDesc |  | CString | 类别：非常量 |
| Building | GetSubsidizeTooltip |  | CString | 类别：非常量 |
| Building | GetSubsistenceOutput |  | CFixedPoint | 类别：非常量 |
| Building | GetSubsistenceOutputDesc |  | CString | 类别：非常量 |
| Building | GetSubventions |  | CFixedPoint | 类别：非常量 |
| Building | GetTariffsPaid |  | CFixedPoint | 类别：非常量 |
| Building | GetTaxationRevenue |  | CFixedPoint | 类别：非常量 |
| Building | GetTaxationRevenueTooltip |  | CString | 类别：非常量 |
| Building | GetThroughputBonusCurrent |  | CFixedPoint | 类别：非常量 |
| Building | GetThroughputBonusTarget |  | CFixedPoint | 类别：非常量 |
| Building | GetThroughputDesc |  | CString | 类别：非常量 |
| Building | GetTimedModifiers |  | Unknown | 类别：非常量 |
| Building | GetTogglePrivatizationTooltip |  | CString | 类别：非常量 |
| Building | GetTooltip |  | CString | 类别：非常量 |
| Building | GetTooltipTag |  | CString | 类别：非常量 |
| Building | GetTotalConsumptionValue |  | CFixedPoint | 类别：非常量 |
| Building | GetTotalExpenses |  | CFixedPoint | 类别：非常量 |
| Building | GetTotalExpensesBalancedSI | CFixedPoint int32 | CString | 类别：非常量 |
| Building | GetTotalProductionValue |  | CFixedPoint | 类别：非常量 |
| Building | GetTradeRevenue |  | CFixedPoint | 类别：非常量 |
| Building | GetTrainingRate |  | int64 | 类别：非常量 |
| Building | GetTrainingRateDesc |  | CString | 类别：非常量 |
| Building | GetUnitsProvidedToFormationBreakdown | MilitaryFormation | CString | 类别：非常量 |
| Building | GetUrbanizationProvidedBreakdown |  | CString | 类别：非常量 |
| Building | GetWageRate |  | CFixedPoint | 类别：非常量 |
| Building | GetWorstGoodsShortage |  | Goods | 类别：非常量 |
| Building | HasAnyInputShortage |  | bool |  |
| Building | HasConstructionQueued |  | bool |  |
| Building | HasFailedHires |  | bool |  |
| Building | HasGovernmentConstructionQueued |  | bool |  |
| Building | HasInputGoods |  | bool |  |
| Building | HasInputShortage | Goods | bool |  |
| Building | HasMaximumInputShortage | Goods | bool |  |
| Building | HasOutputGoods |  | bool |  |
| Building | HasPrivateConstructionQueued |  | bool |  |
| Building | HasReachedLevelCap |  | bool |  |
| Building | HasSlaves |  | bool |  |
| Building | HasTradeRevenue |  | bool |  |
| Building | IsActive |  | bool |  |
| Building | IsActiveStr |  | CString |  |
| Building | IsAutoDownsizing |  | bool |  |
| Building | IsAutoExpanding |  | bool |  |
| Building | IsBeingHighlighted |  | bool |  |
| Building | IsBeingTutorialHighlighted |  | bool |  |
| Building | IsBuildingType | BuildingType | bool |  |
| Building | IsCappedBuilding |  | bool |  |
| Building | IsCurrentlyUnderConstruction |  | bool |  |
| Building | IsDownsizeable |  | bool |  |
| Building | IsExpandable |  | bool |  |
| Building | IsGovernmentFunded |  | bool |  |
| Building | IsMilitaryBuilding |  | bool |  |
| Building | IsOwner | Country | bool |  |
| Building | IsPinnedInOutliner |  | bool |  |
| Building | IsPotentialQueueConstruction |  | bool |  |
| Building | IsRoleFullyReplacedByAnotherPopType | PopType | bool |  |
| Building | IsSelfFunded |  | bool |  |
| Building | IsSubsidized |  | bool |  |
| Building | IsSubsistenceBuilding |  | bool |  |
| Building | IsUrbanCenter |  | bool |  |
| Building | IsValid |  | bool |  |
| Building | MakeScope |  | Scope |  |
| Building | NationalizeBuildingLevels | int32 | Command |  |
| Building | ProvidesUrbanization |  | bool |  |
| Building | QueueConstruction |  | Command |  |
| Building | QueueMilitaryConstruction | MilitaryFormation CombatUnitType | Command |  |
| Building | ResetProductionMethodsToStandard |  | Command |  |
| Building | Self |  | Building |  |
| Building | ShouldShowAsHiring |  | bool |  |
| Building | ShouldShowAsUnableToHire |  | bool |  |
| Building | ShouldShowAsUnwillingToHire |  | bool |  |
| Building | ShowLevelAndMaxLevel |  | bool |  |
| Building | SortBuildings | CString | void |  |
| Building | ToggleAutoExpand |  | Command |  |
| Building | ToggleAutoExpandOff |  | Command |  |
| Building | ToggleAutoExpandOn |  | Command |  |
| Building | TogglePinInOutliner |  | void |  |
| Building | TogglePrivatization |  | Command |  |
| Building | ToggleSubsidies |  | Command |  |
| Building | ToggleSubsidiesOff |  | Command |  |
| Building | ToggleSubsidiesOn |  | Command |  |
| Building | UsesInfrastructure |  | bool |  |
| BuildingBrowserBuildingTypeItem | AccessSelf |  | BuildingBrowserBuildingTypeItem | 类别：常量 |
| BuildingBrowserBuildingTypeItem | CanShowNationalizeBuildingsWindow |  | bool |  |
| BuildingBrowserBuildingTypeItem | GetAllSameProductionMethodTexture | ProductionMethodGroup | Unknown | 类别：非常量 |
| BuildingBrowserBuildingTypeItem | GetBuildingType |  | BuildingType | 类别：非常量 |
| BuildingBrowserBuildingTypeItem | GetBuildings |  | Unknown | 类别：非常量 |
| BuildingBrowserBuildingTypeItem | GetBuildingsInCountry |  | Unknown | 类别：非常量 |
| BuildingBrowserBuildingTypeItem | GetBulkChangeTooltip | ProductionMethodGroup | CString | 类别：非常量 |
| BuildingBrowserBuildingTypeItem | GetFilteredAverageProductivity |  | CFixedPoint | 类别：非常量 |
| BuildingBrowserBuildingTypeItem | GetNationalizeBuildingsButtonTooltip |  | CString | 类别：非常量 |
| BuildingBrowserBuildingTypeItem | GetTotalFilteredCashReserves |  | CFixedPoint | 类别：非常量 |
| BuildingBrowserBuildingTypeItem | GetTotalFilteredEmployed |  | int64 | 类别：非常量 |
| BuildingBrowserBuildingTypeItem | GetTotalFilteredEmployeeCap |  | int64 | 类别：非常量 |
| BuildingBrowserBuildingTypeItem | GetTotalFilteredMaxCashReserves |  | CFixedPoint | 类别：非常量 |
| BuildingBrowserBuildingTypeItem | GetTotalFilteredSizeDesc |  | CString | 类别：非常量 |
| BuildingBrowserBuildingTypeItem | HasAllAutoExpand |  | bool |  |
| BuildingBrowserBuildingTypeItem | HasAllDisallowedPrivatization |  | bool |  |
| BuildingBrowserBuildingTypeItem | HasAllForcedPrivatization |  | bool |  |
| BuildingBrowserBuildingTypeItem | HasAllNoAutoExpand |  | bool |  |
| BuildingBrowserBuildingTypeItem | HasAllNoPrivatization |  | bool |  |
| BuildingBrowserBuildingTypeItem | HasAllNoSubsidies |  | bool |  |
| BuildingBrowserBuildingTypeItem | HasAllPrivatization |  | bool |  |
| BuildingBrowserBuildingTypeItem | HasAllSameProductionMethod | ProductionMethodGroup | bool |  |
| BuildingBrowserBuildingTypeItem | HasAllSubsidies |  | bool |  |
| BuildingBrowserBuildingTypeItem | HasMixedAutoExpand |  | bool |  |
| BuildingBrowserBuildingTypeItem | HasMixedPrivatization |  | bool |  |
| BuildingBrowserBuildingTypeItem | HasMixedSubsidies |  | bool |  |
| BuildingBrowserBuildingTypeItem | RemoveAllPrivatization |  | Command |  |
| BuildingBrowserBuildingTypeItem | Self |  | BuildingBrowserBuildingTypeItem |  |
| BuildingBrowserBuildingTypeItem | ShowNationalizeBuildingsWindow |  | void |  |
| BuildingBrowserBuildingTypeItem | ToggleAllAutoExpand |  | Command |  |
| BuildingBrowserBuildingTypeItem | ToggleAllPrivatization |  | Command |  |
| BuildingBrowserBuildingTypeItem | ToggleAllSubsidies |  | Command |  |
| BuildingBrowserBuildingTypeItem | ToggleSwitchProductionMethodMenu | ProductionMethodGroup PdxGuiWidget | void |  |
| BuildingBrowserPanel | AccessSelf |  | BuildingBrowserPanel | 类别：常量 |
| BuildingBrowserPanel | BuildingTypeFilterAreAllTypesShown |  | bool |  |
| BuildingBrowserPanel | BuildingTypeFilterAreNoTypesShown |  | bool |  |
| BuildingBrowserPanel | BuildingTypeFilterHideAllTypes |  | void |  |
| BuildingBrowserPanel | BuildingTypeFilterIsTypeShown | BuildingType | bool |  |
| BuildingBrowserPanel | BuildingTypeFilterShowAllTypes |  | void |  |
| BuildingBrowserPanel | BuildingTypeFilterToggleShown | BuildingType | void |  |
| BuildingBrowserPanel | CanShowNationalizeBuildingsWindow |  | bool |  |
| BuildingBrowserPanel | Filter | Unknown | void |  |
| BuildingBrowserPanel | GetAllBuildingTypes |  | Unknown | 类别：非常量 |
| BuildingBrowserPanel | GetAllStates |  | Unknown | 类别：非常量 |
| BuildingBrowserPanel | GetBuildingBrowserBuildingTypeItems |  | Unknown | 类别：非常量 |
| BuildingBrowserPanel | GetCountry |  | Country | 类别：非常量 |
| BuildingBrowserPanel | GetFilteredBuildingTypes |  | Unknown | 类别：非常量 |
| BuildingBrowserPanel | GetNationalizeBuildingsButtonTooltip |  | CString | 类别：非常量 |
| BuildingBrowserPanel | GetPotentialDevelopmentBuildingTypes |  | Unknown | 类别：非常量 |
| BuildingBrowserPanel | GetPotentialRuralBuildingTypes |  | Unknown | 类别：非常量 |
| BuildingBrowserPanel | GetPotentialUrbanBuildingTypes |  | Unknown | 类别：非常量 |
| BuildingBrowserPanel | GetSortedAndFilteredBuildings |  | Unknown | 类别：非常量 |
| BuildingBrowserPanel | IsAnyFilterActive |  | bool |  |
| BuildingBrowserPanel | IsBuildingTypeExpanded | BuildingType | bool |  |
| BuildingBrowserPanel | IsFilterNo | CString | bool |  |
| BuildingBrowserPanel | IsFilterYes | CString | bool |  |
| BuildingBrowserPanel | IsFiltered | CString | bool |  |
| BuildingBrowserPanel | IsGroupedByBuildingType |  | bool |  |
| BuildingBrowserPanel | ResetAllFilters |  | void |  |
| BuildingBrowserPanel | Self |  | BuildingBrowserPanel |  |
| BuildingBrowserPanel | SetFilterMode | CString CString | void |  |
| BuildingBrowserPanel | ShowNationalizeBuildingsWindow |  | void |  |
| BuildingBrowserPanel | Sort | CString | void |  |
| BuildingBrowserPanel | StateFilterAreNoStatesShown |  | bool |  |
| BuildingBrowserPanel | StateFilterHideAllStates |  | void |  |
| BuildingBrowserPanel | StateFilterIsStateShown | Unknown | bool |  |
| BuildingBrowserPanel | StateFilterShowAllStates |  | void |  |
| BuildingBrowserPanel | StateFilterToggleShown | Unknown | void |  |
| BuildingBrowserPanel | StateFiltersAreAllStatesShown |  | bool |  |
| BuildingBrowserPanel | ToggleExpandBuildingType | BuildingType | void |  |
| BuildingBrowserPanel | ToggleGroupedByBuildingType |  | void |  |
| BuildingDetailsPanel | AccessBuilding |  | Building | 类别：常量 |
| BuildingDetailsPanel | AccessSelf |  | BuildingDetailsPanel | 类别：常量 |
| BuildingDetailsPanel | AccessState |  | State | 类别：常量 |
| BuildingDetailsPanel | GetBuilding |  | Building | 类别：非常量 |
| BuildingDetailsPanel | GetState |  | State | 类别：非常量 |
| BuildingDetailsPanel | Self |  | BuildingDetailsPanel |  |
| BuildingGroup | AccessSelf |  | BuildingGroup | 类别：常量 |
| BuildingGroup | GetCustom | CustomLocalization | CString | 类别：非常量 |
| BuildingGroup | GetName |  | CString | 类别：非常量 |
| BuildingGroup | GetNameNoFormatting |  | CString | 类别：非常量 |
| BuildingGroup | GetTooltipTag |  | CString | 类别：非常量 |
| BuildingGroup | IsBuildingGroup | BuildingGroup | bool |  |
| BuildingGroup | MakeScope |  | Scope |  |
| BuildingGroup | Self |  | BuildingGroup |  |
| BuildingMarker | AccessBuilding |  | Building | 类别：常量 |
| BuildingMarker | AccessSelf |  | BuildingMarker | 类别：常量 |
| BuildingMarker | GetBuilding |  | Building | 类别：非常量 |
| BuildingMarker | IsOpenInBuildingPanel |  | bool |  |
| BuildingMarker | Self |  | BuildingMarker |  |
| BuildingOwnership | AccessSelf |  | BuildingOwnership | 类别：常量 |
| BuildingOwnership | GetDividendToOwner |  | CFixedPoint | 类别：非常量 |
| BuildingOwnership | GetLevel |  | int32 | 类别：非常量 |
| BuildingOwnership | GetOwnedBuilding |  | Building | 类别：非常量 |
| BuildingOwnership | GetOwnerBuilding |  | Building | 类别：非常量 |
| BuildingOwnership | GetOwnerCountry |  | Country | 类别：非常量 |
| BuildingOwnership | GetOwnershipRatio |  | CFixedPoint | 类别：非常量 |
| BuildingOwnership | GetOwnershipTypeColor |  | CVector4f | 类别：非常量 |
| BuildingOwnership | GetPropertyRatio |  | CFixedPoint | 类别：非常量 |
| BuildingOwnership | GetTooltipTag |  | CString | 类别：非常量 |
| BuildingOwnership | IsCountryOwned |  | bool |  |
| BuildingOwnership | Self |  | BuildingOwnership |  |
| BuildingPotentialMarker | AccessSelf |  | BuildingPotentialMarker | 类别：常量 |
| BuildingPotentialMarker | AccessState |  | State | 类别：常量 |
| BuildingPotentialMarker | GetBuildingType |  | BuildingType | 类别：非常量 |
| BuildingPotentialMarker | GetPosition |  | CVector2f | 类别：非常量 |
| BuildingPotentialMarker | GetState |  | State | 类别：非常量 |
| BuildingPotentialMarker | Self |  | BuildingPotentialMarker |  |
| BuildingProductionMethodsEntry | AccessSelf |  | BuildingProductionMethodsEntry | 类别：常量 |
| BuildingProductionMethodsEntry | GetAllSameProductionMethod | Unknown | ProductionMethod | 类别：非常量 |
| BuildingProductionMethodsEntry | GetAllSameProductionMethodTexture | ProductionMethodGroup | Unknown | 类别：非常量 |
| BuildingProductionMethodsEntry | GetBuildingType |  | BuildingType | 类别：非常量 |
| BuildingProductionMethodsEntry | GetBuildings |  | Unknown | 类别：非常量 |
| BuildingProductionMethodsEntry | GetBulkChangeTooltip | ProductionMethodGroup | CString | 类别：非常量 |
| BuildingProductionMethodsEntry | HasAllAutoExpand |  | bool |  |
| BuildingProductionMethodsEntry | HasAllNoAutoExpand |  | bool |  |
| BuildingProductionMethodsEntry | HasAllNoSubsidies |  | bool |  |
| BuildingProductionMethodsEntry | HasAllSameProductionMethod | ProductionMethodGroup | bool |  |
| BuildingProductionMethodsEntry | HasAllSubsidies |  | bool |  |
| BuildingProductionMethodsEntry | HasMixedAutoExpand |  | bool |  |
| BuildingProductionMethodsEntry | HasMixedSubsidies |  | bool |  |
| BuildingProductionMethodsEntry | IsExpanded |  | bool |  |
| BuildingProductionMethodsEntry | Self |  | BuildingProductionMethodsEntry |  |
| BuildingProductionMethodsEntry | ToggleAllAutoExpand |  | Command |  |
| BuildingProductionMethodsEntry | ToggleAllSubsidies |  | Command |  |
| BuildingProductionMethodsEntry | ToggleExpand |  | void |  |
| BuildingType | AccessProductionMethodGroups |  | Unknown | 类别：常量 |
| BuildingType | AccessSelf |  | BuildingType | 类别：常量 |
| BuildingType | ActivateExpansionLens |  | void |  |
| BuildingType | CanBeAutoExpanded |  | bool |  |
| BuildingType | CanBeSubsidized |  | bool |  |
| BuildingType | CanSwitchOwner |  | bool |  |
| BuildingType | CreatedByUrbanization |  | bool |  |
| BuildingType | FiredPopsBecomeRadical |  | bool |  |
| BuildingType | GetBackground |  | Unknown | 类别：非常量 |
| BuildingType | GetBuildingGroup |  | BuildingGroup | 类别：非常量 |
| BuildingType | GetBuildingGroupName |  | CString | 类别：非常量 |
| BuildingType | GetBuildingKindDesc | Country | CString | 类别：非常量 |
| BuildingType | GetBuildingModifier |  | Modifier | 类别：非常量 |
| BuildingType | GetConstructionCosts |  | CString | 类别：非常量 |
| BuildingType | GetCountryModifier |  | Modifier | 类别：非常量 |
| BuildingType | GetCustom | CustomLocalization | CString | 类别：非常量 |
| BuildingType | GetDiscoveredResourceName |  | CString | 类别：非常量 |
| BuildingType | GetExpansionMissingQualificationsDesc | Unknown Unknown | CString | 类别：非常量 |
| BuildingType | GetExpansionProductivityDesc | Unknown Unknown | CString | 类别：非常量 |
| BuildingType | GetExpansionProductivityImpact | Building State | CFixedPoint | 类别：非常量 |
| BuildingType | GetExpansionProductivityImpactDesc | Building State | CString | 类别：非常量 |
| BuildingType | GetExpansionRevenueImpact | Building State | CFixedPoint | 类别：非常量 |
| BuildingType | GetExpansionRevenueImpactDesc | Building State | CString | 类别：非常量 |
| BuildingType | GetID |  | int32 | 类别：非常量 |
| BuildingType | GetIDString |  | CString | 类别：非常量 |
| BuildingType | GetIcon |  | Unknown | 类别：非常量 |
| BuildingType | GetKey |  | CString | 类别：非常量 |
| BuildingType | GetModifierEffectsAsString |  | CString | 类别：非常量 |
| BuildingType | GetMonopolyCompanyIn | Unknown | Company | 类别：非常量 |
| BuildingType | GetMonopolyCountryIn | Unknown | Country | 类别：非常量 |
| BuildingType | GetName |  | CString | 类别：非常量 |
| BuildingType | GetNameNoFormatting |  | CString | 类别：非常量 |
| BuildingType | GetNumAvailableStatesForBuilding |  | int32 | 类别：非常量 |
| BuildingType | GetNumLevelsInCountryFormatted | Country | CString | 类别：非常量 |
| BuildingType | GetNumLevelsInCountryRaw | Country | int32 | 类别：非常量 |
| BuildingType | GetNumLevelsOwnedByCompanyFormatted | Company | CString | 类别：非常量 |
| BuildingType | GetNumLevelsOwnedByCompanyRaw | Company | int32 | 类别：非常量 |
| BuildingType | GetProductivitySpanDesc | Country | CString | 类别：非常量 |
| BuildingType | GetRequiredConstruction |  | CFixedPoint | 类别：非常量 |
| BuildingType | GetResetProductionMethodsToStandardTooltip |  | CString | 类别：非常量 |
| BuildingType | GetStandardProductionMethodDesc | Unknown | CString | 类别：非常量 |
| BuildingType | GetStateModifier |  | Modifier | 类别：非常量 |
| BuildingType | GetTabName |  | CString | 类别：非常量 |
| BuildingType | GetToggleMonopolyEffectDesc |  | CString | 类别：非常量 |
| BuildingType | GetTooltip |  | CString | 类别：非常量 |
| BuildingType | GetTooltipForBuilding | Building | CString | 类别：非常量 |
| BuildingType | GetTooltipForState | Unknown | CString | 类别：非常量 |
| BuildingType | GetTooltipTag |  | CString | 类别：非常量 |
| BuildingType | GetUrbanizationProvidedBreakdown |  | CString | 类别：非常量 |
| BuildingType | HasCompanyMonopoly | Unknown | bool |  |
| BuildingType | HasCountryMonopoly |  | bool |  |
| BuildingType | HasInputGoods |  | bool |  |
| BuildingType | HasMonopoly |  | bool |  |
| BuildingType | HasOutputGoods |  | bool |  |
| BuildingType | HasRequiredPrinciplesInCountry | Country | bool |  |
| BuildingType | HasRequiredTechnologiesInCountry | Country | bool |  |
| BuildingType | IsAlwaysSelfOwning |  | bool |  |
| BuildingType | IsBeingHighlighted |  | bool |  |
| BuildingType | IsBeingTutorialHighlighted |  | bool |  |
| BuildingType | IsBuildable |  | bool |  |
| BuildingType | IsBuildableInAnyState | Country | bool |  |
| BuildingType | IsCappedBuilding |  | bool |  |
| BuildingType | IsDownsizeable |  | bool |  |
| BuildingType | IsExpandable |  | bool |  |
| BuildingType | IsGovernmentFunded |  | bool |  |
| BuildingType | IsMilitaryBuilding |  | bool |  |
| BuildingType | IsRural |  | bool |  |
| BuildingType | IsSelfFunded |  | bool |  |
| BuildingType | IsSubsistenceBuilding |  | bool |  |
| BuildingType | IsUnique |  | bool |  |
| BuildingType | IsUrban |  | bool |  |
| BuildingType | IsUsingArableLand |  | bool |  |
| BuildingType | IssDevelopment |  | bool |  |
| BuildingType | MakeScope |  | Scope |  |
| BuildingType | ProvidesUrbanization |  | bool |  |
| BuildingType | RecruitsCombatUnits |  | bool |  |
| BuildingType | ResetProductionMethodsToStandard |  | Command |  |
| BuildingType | Self |  | BuildingType |  |
| BuildingType | ToggleMonopoly |  | Command |  |
| BuildingType | UsesInfrastructure |  | bool |  |
| CFixedPoint | AccessSelf |  | CFixedPoint | 类别：常量 |
| CFixedPoint | GetFixedPoint |  | Unknown | 类别：非常量 |
| CFixedPoint | Self |  | CFixedPoint |  |
| CPdxEnumValue | AccessSelf |  | CPdxEnumValue | 类别：常量 |
| CPdxEnumValue | AreBundleValuesMixed |  | bool |  |
| CPdxEnumValue | GetDropdownEntries |  | Unknown | 类别：非常量 |
| CPdxEnumValue | GetDropdownValueIndex |  | CVector2i | 类别：非常量 |
| CPdxEnumValue | GetValueString |  | CString | 类别：非常量 |
| CPdxEnumValue | Self |  | CPdxEnumValue |  |
| CPdxEnumValue | SetDropdownValueIndex |  | void |  |
| CPdxFloatRect | AccessSelf |  | CPdxFloatRect | 类别：常量 |
| CPdxFloatRect | GetRect |  | Unknown | 类别：非常量 |
| CPdxFloatRect | Self |  | CPdxFloatRect |  |
| CPdxInputBindingSetting | AccessSelf |  | CPdxInputBindingSetting | 类别：常量 |
| CPdxInputBindingSetting | Self |  | CPdxInputBindingSetting |  |
| CPdxIntRect | AccessSelf |  | CPdxIntRect | 类别：常量 |
| CPdxIntRect | GetRect |  | Unknown | 类别：非常量 |
| CPdxIntRect | Self |  | CPdxIntRect |  |
| CString | AccessSelf |  | CString | 类别：常量 |
| CString | GetString |  | Unknown | 类别：非常量 |
| CString | Self |  | CString |  |
| CUTF8String | AccessSelf |  | CUTF8String | 类别：常量 |
| CUTF8String | GetString |  | Unknown | 类别：非常量 |
| CUTF8String | Self |  | CUTF8String |  |
| CVector2f | AccessSelf |  | CVector2f | 类别：常量 |
| CVector2f | GetVector |  | Unknown | 类别：非常量 |
| CVector2f | Self |  | CVector2f |  |
| CVector2i | AccessSelf |  | CVector2i | 类别：常量 |
| CVector2i | GetVector |  | Unknown | 类别：非常量 |
| CVector2i | Self |  | CVector2i |  |
| CVector3f | AccessSelf |  | CVector3f | 类别：常量 |
| CVector3f | GetVector |  | Unknown | 类别：非常量 |
| CVector3f | Self |  | CVector3f |  |
| CVector3i | AccessSelf |  | CVector3i | 类别：常量 |
| CVector3i | GetVector |  | Unknown | 类别：非常量 |
| CVector3i | Self |  | CVector3i |  |
| CVector4f | AccessSelf |  | CVector4f | 类别：常量 |
| CVector4f | GetVector |  | Unknown | 类别：非常量 |
| CVector4f | Self |  | CVector4f |  |
| CVector4i | AccessSelf |  | CVector4i | 类别：常量 |
| CVector4i | GetVector |  | Unknown | 类别：非常量 |
| CVector4i | Self |  | CVector4i |  |
| CanalType | AccessSelf |  | CanalType | 类别：常量 |
| CanalType | GetBuildingType |  | BuildingType | 类别：非常量 |
| CanalType | GetCustom | CustomLocalization | CString | 类别：非常量 |
| CanalType | GetName |  | CString | 类别：非常量 |
| CanalType | GetNameNoFormatting |  | CString | 类别：非常量 |
| CanalType | GetStateRegion |  | StateRegion | 类别：非 const |
| CanalType | GetTexture |  | Unknown | 类别：非 const |
| CanalType | GetTooltipTag |  | CString | 类别：非 const |
| CanalType | MakeScope |  | Scope |  |
| CanalType | Self |  | CanalType |  |
| ChangeLawPanel | AccessSelf |  | ChangeLawPanel | 类别：const |
| ChangeLawPanel | GetLawAlternatives |  | Unknown | 类别：非 const |
| ChangeLawPanel | GetLawGroup |  | LawGroup | 类别：非 const |
| ChangeLawPanel | GetSelectedLaw |  | Law | 类别：非 const |
| ChangeLawPanel | Self |  | ChangeLawPanel |  |
| ChangeProductionMethodMenuItem | AccessMethod |  | ProductionMethod | 类别：const |
| ChangeProductionMethodMenuItem | AccessSelf |  | ChangeProductionMethodMenuItem | 类别：const |
| ChangeProductionMethodMenuItem | Execute |  | void |  |
| ChangeProductionMethodMenuItem | GetProductionMethodGroup |  | ProductionMethodGroup | 类别：非 const |
| ChangeProductionMethodMenuItem | GetTooltip | Country | CString | 类别：非 const |
| ChangeProductionMethodMenuItem | IsActive |  | bool |  |
| ChangeProductionMethodMenuItem | IsValid |  | bool |  |
| ChangeProductionMethodMenuItem | OnMenuItemHovered |  | void |  |
| ChangeProductionMethodMenuItem | Self |  | ChangeProductionMethodMenuItem |  |
| ChangeProductionMethodsMenuItems | AccessItems |  | Unknown | 类别：const |
| ChangeProductionMethodsMenuItems | AccessSelf |  | ChangeProductionMethodsMenuItems | 类别：const |
| ChangeProductionMethodsMenuItems | Self |  | ChangeProductionMethodsMenuItems |  |
| Character | AccessBattle |  | Battle | 类别：const |
| Character | AccessCulture |  | Culture | 类别：const |
| Character | AccessInterestGroup |  | InterestGroup | 类别：const |
| Character | AccessOrders |  | Unknown | 类别：const |
| Character | AccessPossibleSpecialOrders |  | Unknown | 类别：const |
| Character | AccessReligion |  | Religion | 类别：const |
| Character | AccessSelf |  | Character | 类别：const |
| Character | AccessTraits |  | Unknown | 类别：const |
| Character | AccessUnavailableOrders |  | Unknown | 类别：const |
| Character | GetAcceptanceStatus |  | AcceptanceStatus | 类别：非 const |
| Character | GetAcceptanceStatusIn | Country | AcceptanceStatus | 类别：非 const |
| Character | GetAcceptanceValue |  | int32 | 类别：非 const |
| Character | GetAcceptanceValueDesc |  | CString | 类别：非 const |
| Character | GetAcceptanceValueDescIn | Country | CString | 类别：非 const |
| Character | GetAcceptanceValueIn | Country | int32 | 类别：非 const |
| Character | GetAge |  | int32 | 类别：非 const |
| Character | GetAgitatorSpawnedNotificationText |  | CString | 类别：非 const |
| Character | GetAllRoleNames |  | CString | 类别：非 const |
| Character | GetAnimatedPortrait | PortraitEnvironment PortraitCamera PortraitAnimation CVector2f | Unknown | 类别：非 const |
| Character | GetAssignedState |  | State | 类别：非 const |
| Character | GetBattle |  | Battle | 类别：非 const |
| Character | GetBirthday |  | CString | 类别：非 const |
| Character | GetCombatUnitsTypeIcon |  | CString | 类别：非 const |
| Character | GetCommandLimit |  | CString | 类别：非 const |
| Character | GetCommandLimitDesc |  | CString | 类别：非 const |
| Character | GetCommandLimitRaw |  | int32 | 类别：非 const |
| Character | GetCommanderDetails |  | CString | 类别：非 const |
| Character | GetCommanderRank |  | CommanderRank | 类别：非 const |
| Character | GetCountry |  | Country | 类别：非 const |
| Character | GetCulture |  | Culture | 类别：非 const |
| Character | GetCustom | CustomLocalization | CString | 类别：非 const |
| Character | GetDebugDesc |  | CString | 类别：非 const |
| Character | GetFirstName |  | CString | 类别：非 const |
| Character | GetFirstNameNoFormatting |  | CString | 类别：非 const |
| Character | GetFirstNamePossessive |  | CString | 类别：非 const |
| Character | GetFront |  | Front | 类别：非 const |
| Character | GetFullName |  | CString | 类别：非 const |
| Character | GetFullNameNoFormatting |  | CString | 类别：非 const |
| Character | GetFullNamePossessive |  | CString | 类别：非 const |
| Character | GetFullNameWithTitle |  | CString | 类别：非 const |
| Character | GetFullNameWithTitleNoFormatting |  | CString | 类别：非 const |
| Character | GetFullNameWithTitlePossessive |  | CString | 类别：非 const |
| Character | GetGender |  | CString | 类别：非 const |
| Character | GetGenderOpposite |  | CString | 类别：非 const |
| Character | GetHerHim |  | CString | 类别：非 const |
| Character | GetHerHimOpposite |  | CString | 类别：非 const |
| Character | GetHerHis |  | CString | 类别：非 const |
| Character | GetHerHisOpposite |  | CString | 类别：非 const |
| Character | GetHerselfHimself |  | CString | 类别：非 const |
| Character | GetHerselfHimselfOpposite |  | CString | 类别：非 const |
| Character | GetHistoricalUrl |  | CString | 类别：非 const |
| Character | GetHomeCountry |  | Country | 类别：非 const |
| Character | GetHomeCountryDefinition |  | CountryDefinition | 类别：非 const |
| Character | GetID |  | int32 | 类别：非 const |
| Character | GetIDString |  | CString | 类别：非 const |
| Character | GetIdeology |  | Ideology | 类别：非 const |
| Character | GetInfoTooltip |  | CString | 类别：非 const |
| Character | GetInteraction | Unknown | CharacterInteraction | 类别：非 const |
| Character | GetInteractions |  | Unknown | 类别：非 const |
| Character | GetInterestGroup |  | InterestGroup | 类别：非 const |
| Character | GetInvasion |  | Invasion | 类别：非 const |
| Character | GetLastName |  | CString | 类别：非 const |
| Character | GetLastNameNoFormatting |  | CString | 类别：非 const |
| Character | GetLastNamePossessive |  | CString | 类别：非 const |
| Character | GetMilitaryFormation |  | MilitaryFormation | 类别：非 const |
| Character | GetNextCommanderRank |  | CommanderRank | 类别：非 const |
| Character | GetNextCommanderRankBenefits |  | CString | 类别：非 const |
| Character | GetNextOrderType |  | CommanderOrderType | 类别：非 const |
| Character | GetNumUnitsThatWouldBeSplitOff |  | int32 | 类别：非 const |
| Character | GetOrderType |  | CommanderOrderType | 类别：非 const |
| Character | GetPoliticalMovement |  | PoliticalMovement | 类别：非 const |
| Character | GetPopularity |  | CFixedPoint | 类别：非 const |
| Character | GetPopularityDesc |  | CString | 类别：非 const |
| Character | GetPortrait | PortraitEnvironment PortraitCamera PortraitAnimation CVector2f | Unknown | 类别：非 const |
| Character | GetPrimaryRoleName |  | CString | 类别：非 const |
| Character | GetPrimaryRoleTitle |  | CString | 类别：非 const |
| Character | GetPromoteCommand |  | Command | 类别：非 const |
| Character | GetRankName |  | CString | 类别：非 const |
| Character | GetRankNameFor | CommanderRank | CString | 类别：非 const |
| Character | GetRankTitle |  | CString | 类别：非 const |
| Character | GetRankTitleFor | CommanderRank | CString | 类别：非 const |
| Character | GetRecruitCommand | MilitaryFormation | Command | 类别：非 const |
| Character | GetReligion |  | Religion | 类别：非 const |
| Character | GetRepairingTexture |  | Unknown | 类别：非 const |
| Character | GetSheHe |  | CString | 类别：非 const |
| Character | GetSheHeOpposite |  | CString | 类别：非 const |
| Character | GetStrengthPointsIcon |  | CString | 类别：非 const |
| Character | GetTimedModifiers |  | Unknown | 类别：非 const |
| Character | GetTooltipTag |  | CString | 类别：非 const |
| Character | GetTraitsDesc |  | CString | 类别：非 const |
| Character | GetWomanMan |  | CString | 类别：非 const |
| Character | GetWomanManOpposite |  | CString | 类别：非 const |
| Character | HasAdvancingOrder |  | bool |  |
| Character | HasInvasionPlan |  | bool |  |
| Character | HasMilitaryFormation |  | bool |  |
| Character | HasOrder | Unknown | bool |  |
| Character | HasUnavailableAdvanceOrders |  | bool |  |
| Character | HasUnavailableDefendOrders |  | bool |  |
| Character | IsAdmiral |  | bool |  |
| Character | IsAgitator |  | bool |  |
| Character | IsAtFront |  | bool |  |
| Character | IsAttackingInBattle |  | bool |  |
| Character | IsBeingHighlighted |  | bool |  |
| Character | IsBeingTutorialHighlighted |  | bool |  |
| Character | IsBusy |  | bool |  |
| Character | IsCommander |  | bool |  |
| Character | IsDefeated |  | bool |  |
| Character | IsDefendingInBattle |  | bool |  |
| Character | IsExecutive |  | bool |  |
| Character | IsFemale |  | bool |  |
| Character | IsGeneral |  | bool |  |
| Character | IsHeir |  | bool |  |
| Character | IsHistorical |  | bool |  |
| Character | IsIGLeader |  | bool |  |
| Character | IsInBattle |  | bool |  |
| Character | IsInExilePool |  | bool |  |
| Character | IsMaxRank |  | bool |  |
| Character | IsOffer |  | bool |  |
| Character | IsPinnedInOutliner |  | bool |  |
| Character | IsPolitician |  | bool |  |
| Character | IsRetired |  | bool |  |
| Character | IsRuler |  | bool |  |
| Character | IsValid |  | bool |  |
| Character | IsZoomingToOrderTarget |  | bool |  |
| Character | MakeScope |  | Scope |  |
| Character | OpenHistoricalUrl |  | void |  |
| Character | PredictMovementToJoin | Unknown | PoliticalMovement |  |
| Character | PredictMovementTypeToStart | Unknown | PoliticalMovementType |  |
| Character | RecruitCharacter | Unknown | void |  |
| Character | SelectOrder | CommanderOrderType | Command |  |
| Character | Self |  | Character |  |
| Character | SplitIntoOwnFormation |  | Command |  |
| Character | TogglePinInOutliner |  | void |  |
| Character | WillJoinMovementIfInvited | Country | bool |  |
| Character | WillStartMovementIfInvited | Country | bool |  |
| Character | ZoomToLocation |  | void |  |
| Character | ZoomToOrderTarget |  | void |  |
| CharacterInteraction | AccessSelf |  | CharacterInteraction | 类别：const |
| CharacterInteraction | ExecuteCommand | Character | void |  |
| CharacterInteraction | GetClickSound |  | Unknown | 类别：非 const |
| CharacterInteraction | GetCommandDesc | Character | CString | 类别：非 const |
| CharacterInteraction | GetCooldownDesc | Character | CString | 类别：非 const |
| CharacterInteraction | GetCooldownDuration | Character | CString | 类别：非 const |
| CharacterInteraction | GetCooldownRemaining | Character | CString | 类别：非 const |
| CharacterInteraction | GetDesc |  | CString | 类别：非 const |
| CharacterInteraction | GetEffects | Character | CString | 类别：非 const |
| CharacterInteraction | GetIcon |  | Unknown | 类别：非 const |
| CharacterInteraction | GetInfo |  | CString | 类别：非 const |
| CharacterInteraction | GetName |  | CString | 类别：非 const |
| CharacterInteraction | GetRequirements | Character | CString | 类别：非 const |
| CharacterInteraction | GetTooltipTag |  | CString | 类别：非 const |
| CharacterInteraction | HasCooldown | Unknown | bool |  |
| CharacterInteraction | HasIcon |  | bool |  |
| CharacterInteraction | IsCommandValid | Character | bool |  |
| CharacterInteraction | IsOnCooldown | Character | bool |  |
| CharacterInteraction | Self |  | CharacterInteraction |  |
| CharacterInteraction | ShouldShowRequirements |  | bool |  |
| CharacterTrait | AccessSelf |  | CharacterTrait | 类别：const |
| CharacterTrait | AccessUnlockedOrders |  | Unknown | 类别：const |
| CharacterTrait | GetDesc |  | CString | 类别：非 const |
| CharacterTrait | GetModifiers |  | CString | 类别：非 const |
| CharacterTrait | GetName |  | CString | 类别：非 const |
| CharacterTrait | GetNameNoFormatting |  | CString | 类别：非 const |
| CharacterTrait | GetTexture |  | Unknown | 类别：非 const |
| CharacterTrait | GetTooltipTag |  | CString | 类别：非 const |
| CharacterTrait | Self |  | CharacterTrait |  |
| Chat | AccessChatMessages |  | Unknown | 类别：const |
| Chat | AccessSelf |  | Chat | 类别：const |
| Chat | GetReceiver |  | Friend | 类别：非 const |
| Chat | GetReceiverName |  | CUTF8String | 类别：非 const |
| Chat | GetUnreadMessageCount |  | int32 | 类别：非 const |
| Chat | HasUnreadMessages |  | bool |  |
| Chat | IsRoomChat |  | bool |  |
| Chat | Self |  | Chat |  |
| ChatMessage | AccessSelf |  | ChatMessage | 类别：const |
| ChatMessage | GetMessage |  | CUTF8String | 类别：非 const |
| ChatMessage | GetName |  | CUTF8String | 类别：非 const |
| ChatMessage | Self |  | ChatMessage |  |
| ChatNotificationMessage | AccessSelf |  | ChatNotificationMessage | 类别：const |
| ChatNotificationMessage | ChatMessage |  | ChatMessage |  |
| ChatNotificationMessage | Kill |  | void |  |
| ChatNotificationMessage | Self |  | ChatNotificationMessage |  |
| ChatNotificationMessage | StartChat |  | void |  |
| ChatTab | AccessSelf |  | ChatTab | 类别：const |
| ChatTab | Activate |  | void |  |
| ChatTab | Close |  | void |  |
| ChatTab | GetChat |  | Chat | 类别：非 const |
| ChatTab | GetChatTitle |  | CUTF8String | 类别：非 const |
| ChatTab | IsActive |  | bool |  |
| ChatTab | Self |  | ChatTab |  |
| ChatWindow | AccessChatTabs |  | Unknown | 类别：const |
| ChatWindow | AccessSelf |  | ChatWindow | 类别：const |
| ChatWindow | CanSendMessage |  | bool |  |
| ChatWindow | Hide |  | void |  |
| ChatWindow | Self |  | ChatWindow |  |
| ChatWindow | SendMessage |  | void |  |
| ChatWindow | ShouldBeShown |  | bool |  |
| ChatWindow | Show |  | void |  |
| ChildGenerator | AccessSelf |  | ChildGenerator | 类别：const |
| ChildGenerator | GetGenerationItems |  | Unknown | 类别：非 const |
| ChildGenerator | GetRandomChildrenRatio |  | float | 类别：非 const |
| ChildGenerator | OnRandomizedRatioChanged |  | void |  |
| ChildGenerator | Regenerate |  | void |  |
| ChildGenerator | Self |  | ChildGenerator |  |
| ChildItem | AccessSelf |  | ChildItem | 类别：const |
| ChildItem | CopyDnaToClipboard |  | void |  |
| ChildItem | GetDna |  | CString | 类别：非 const |
| ChildItem | GetDnaForTexture | CString | CString | 类别：非 const |
| ChildItem | IsRandomized |  | bool |  |
| ChildItem | PasteDna |  | void |  |
| ChildItem | Self |  | ChildItem |  |
| Cities | AccessSelf |  | Cities | 类别：const |
| Cities | ClearAll |  | void |  |
| Cities | GetCurrentBuildingCityTypeName |  | CString | 类别：非 const |
| Cities | GetCurrentBuildingLevel |  | int32 | 类别：非 const |
| Cities | GetCurrentBuildingTypeName |  | CString | 类别：非 const |
| Cities | GetMidRatio |  | float | 类别：非 const |
| Cities | GetMonumentsMode |  | CString | 类别：非 const |
| Cities | GetPoorRatio |  | float | 类别：非 const |
| Cities | GetRichRatio |  | float | 类别：非 const |
| Cities | IsAutoRefresh |  | bool |  |
| Cities | IsCurrentBuildingTypeValid |  | bool |  |
| Cities | IsCurrentBuildingUnderConstruction |  | bool |  |
| Cities | Random |  | void |  |
| Cities | Refresh |  | void |  |
| Cities | Self |  | Cities |  |
| Cities | SetAutoRefresh | bool | void |  |
| Cities | SetCurrentBuildingLevel |  | void |  |
| Cities | SetCurrentBuildingLevelStr |  | void |  |
| Cities | SetCurrentBuildingUnderConstruction | bool | void |  |
| Cities | SetMidRatio |  | void |  |
| Cities | SetMidRatioStr |  | void |  |
| Cities | SetPoorRatio |  | void |  |
| Cities | SetPoorRatioStr |  | void |  |
| Cities | SetRichRatio |  | void |  |
| Cities | SetRichRatioStr |  | void |  |
| CityMarker | AccessSelf |  | CityMarker | 类别：const |
| CityMarker | GetCityName |  | CString | 类别：非 const |
| CityMarker | GetCountry |  | Country | 类别：非 const |
| CityMarker | GetState |  | State | 类别：非 const |
| CityMarker | IsCountryCapital |  | bool |  |
| CityMarker | IsRegionCapital |  | bool |  |
| CityMarker | Self |  | CityMarker |  |
| CivilWar | AccessInsurrectionaryIGs | Country | Unknown | 类别：const |
| CivilWar | AccessOriginCountry |  | Country | 类别：const |
| CivilWar | AccessPoliticalMovement |  | PoliticalMovement | 类别：const |
| CivilWar | AccessSelf |  | CivilWar | 类别：const |
| CivilWar | AccessUprisingCountry |  | Country | 类别：const |
| CivilWar | GetClockCheckpointDateString |  | CString | 类别：非 const |
| CivilWar | GetClockCheckpointRemainingWeeks |  | int32 | 类别：非 const |
| CivilWar | GetClockTime |  | CFixedPoint | 类别：非 const |
| CivilWar | GetCustom | CustomLocalization | CString | 类别：非 const |
| CivilWar | GetLeadingInsurrectionaryIG |  | InterestGroup | 类别：非 const |
| CivilWar | GetMaxProgress |  | CFixedPoint | 类别：非 const |
| CivilWar | GetMaxProgressDesc |  | CString | 类别：非 const |
| CivilWar | GetName |  | CString | 类别：非 const |
| CivilWar | GetNumUprisingBattalions |  | int32 | 类别：非 const |
| CivilWar | GetNumUprisingFlotillas |  | int32 | 类别：非 const |
| CivilWar | GetNumUprisingPotentialConscripts |  | int32 | 类别：非 const |
| CivilWar | GetNumUprisingStates |  | int32 | 类别：非 const |
| CivilWar | GetOriginCountry |  | Country | 类别：非 const |
| CivilWar | GetPoliticalMovement |  | PoliticalMovement | 类别：非 const |
| CivilWar | GetProgress |  | CFixedPoint | 类别：非 const |
| CivilWar | GetProgressAtCheckpoint |  | CFixedPoint | 类别：非 const |
| CivilWar | GetProgressAtCheckpointDesc |  | CString | 类别：非 const |
| CivilWar | GetTooltipTag |  | CString | 类别：非 const |
| CivilWar | GetUprisingConscriptionRateDesc |  | CString | 类别：非 const |
| CivilWar | GetUprisingCountry |  | Country | 类别：非 const |
| CivilWar | GetUprisingNumUnitsDesc |  | CString | 类别：非 const |
| CivilWar | GetUprisingStatesString |  | CString | 类别：非 const |
| CivilWar | HasBrokenOut |  | bool |  |
| CivilWar | HasPoliticalMovement |  | bool |  |
| CivilWar | IsOriginCountry | Unknown | bool |  |
| CivilWar | IsRevolution |  | bool |  |
| CivilWar | IsSecession |  | bool |  |
| CivilWar | IsUprisingCountry | Unknown | bool |  |
| CivilWar | IsValid |  | bool |  |
| CivilWar | MakeScope |  | Scope |  |
| CivilWar | Self |  | CivilWar |  |
| CloudSaveData | AccessSelf |  | CloudSaveData | 类别：const |
| CloudSaveData | AreCloudSavesAvailable |  | bool |  |
| CloudSaveData | GetCloudSaveTooltip |  | CString | 类别：非 const |
| CloudSaveData | OnCloudSaveClick |  | void |  |
| CloudSaveData | Self |  | CloudSaveData |  |
| CloudSaveData | ShouldSaveToCloud |  | bool |  |
| CoatOfArms | AccessSelf |  | CoatOfArms | 类别：const |
| CoatOfArms | GetColor | Unknown | CVector4f | 类别：非 const |
| CoatOfArms | GetFrame | Unknown Unknown | int32 | 类别：非 const |
| CoatOfArms | GetLargeFlagFrame |  | int32 | 类别：非 const |
| CoatOfArms | GetLargeFlagSlot |  | CVector4f | 类别：非 const |
| CoatOfArms | GetLargeFlagTexture |  | Unknown | 类别：非 const |
| CoatOfArms | GetLargePowerBlocCoaFrame |  | int32 | 类别：非 const |
| CoatOfArms | GetLargePowerBlocCoaSlot |  | CVector4f | 类别：非 const |
| CoatOfArms | GetLargePowerBlocCoaTexture |  | Unknown | 类别：非 const |
| CoatOfArms | GetMediumFlagFrame |  | int32 | 类别：非 const |
| CoatOfArms | GetMediumFlagSlot |  | CVector4f | 类别：非 const |
| CoatOfArms | GetMediumFlagTexture |  | Unknown | 类别：非 const |
| CoatOfArms | GetMediumPowerBlocCoaFrame |  | int32 | 类别：非 const |
| CoatOfArms | GetMediumPowerBlocCoaSlot |  | CVector4f | 类别：非 const |
| CoatOfArms | GetMediumPowerBlocCoaTexture |  | Unknown | 类别：非 const |
| CoatOfArms | GetSlot | Unknown Unknown | CVector4f | 类别：非 const |
| CoatOfArms | GetSmallFlagFrame |  | int32 | 类别：非 const |
| CoatOfArms | GetSmallFlagSlot |  | CVector4f | 类别：非 const |
| CoatOfArms | GetSmallFlagTexture |  | Unknown | 类别：非 const |
| CoatOfArms | GetSmallPowerBlocCoaFrame |  | int32 | 类别：非 const |
| CoatOfArms | GetSmallPowerBlocCoaSlot |  | CVector4f | 类别：非 const |
| CoatOfArms | GetSmallPowerBlocCoaTexture |  | Unknown | 类别：非 const |
| CoatOfArms | GetTexture | Unknown Unknown | Unknown | 类别：非 const |
| CoatOfArms | GetVeryLargePowerBlocCoaFrame |  | int32 | 类别：非 const |
| CoatOfArms | GetVeryLargePowerBlocCoaSlot |  | CVector4f | 类别：非 const |
| CoatOfArms | GetVeryLargePowerBlocCoaTexture |  | Unknown | 类别：非 const |
| CoatOfArms | GetVerySmallPowerBlocCoaFrame |  | int32 | 类别：非 const |
| CoatOfArms | GetVerySmallPowerBlocCoaSlot |  | CVector4f | 类别：非 const |
| CoatOfArms | GetVerySmallPowerBlocCoaTexture |  | Unknown | 类别：非 const |
| CoatOfArms | Self |  | CoatOfArms |  |
| CoatOfArmsPreviewWindow | AccessSelf |  | CoatOfArmsPreviewWindow | 类别：const |
| CoatOfArmsPreviewWindow | Close |  | void |  |
| CoatOfArmsPreviewWindow | GetRandomFlagFrame | uint32 | int32 | 类别：非 const |
| CoatOfArmsPreviewWindow | GetRandomFlagTexture | uint32 | Unknown | 类别：非 const |
| CoatOfArmsPreviewWindow | RandomSeed |  | void |  |
| CoatOfArmsPreviewWindow | Self |  | CoatOfArmsPreviewWindow |  |
| CohesionLevel | AccessSelf |  | CohesionLevel | 类别：const |
| CohesionLevel | GetBackground |  | Unknown | 类别：非 const |
| CohesionLevel | GetEffects |  | CString | 类别：非 const |
| CohesionLevel | GetLowerBound |  | CFixedPoint | 类别：非 const |
| CohesionLevel | GetName |  | CString | 类别：非 const |
| CohesionLevel | GetNameNoFormatting |  | CString | 类别：非 const |
| CohesionLevel | GetProgress | Unknown | float | 类别：非 const |
| CohesionLevel | GetTooltipTag |  | CString | 类别：非 const |
| CohesionLevel | GetUpperBound |  | CFixedPoint | 类别：非 const |
| CohesionLevel | GetWidth |  | CFixedPoint | 类别：非 const |
| CohesionLevel | IsActive | Unknown | bool |  |
| CohesionLevel | Self |  | CohesionLevel |  |
| ColonyMarker | AccessSelf |  | ColonyMarker | 类别：const |
| ColonyMarker | AccessState |  | State | 类别：const |
| ColonyMarker | GetPosition |  | CVector2f | 类别：非 const |
| ColonyMarker | GetState |  | State | 类别：非 const |
| ColonyMarker | Self |  | ColonyMarker |  |
| ColorPicker | AccessSelf |  | ColorPicker | 类别：const |
| ColorPicker | GetColor |  | CVector4f | 类别：非 const |
| ColorPicker | GetColorSpace |  | Unknown | 类别：非 const |
| ColorPicker | Self |  | ColorPicker |  |
| CombatUnit | AccessSelf |  | CombatUnit | 类别：const |
| CombatUnit | GetBattle |  | Battle | 类别：非 const |
| CombatUnit | GetBuilding |  | Building | 类别：非 const |
| CombatUnit | GetCasualtiesDesc |  | CString | 类别：非 const |
| CombatUnit | GetCountry |  | Country | 类别：非 const |
| CombatUnit | GetCulture |  | Culture | 类别：非 const |
| CombatUnit | GetCurrentExperienceTowardsNextLevel |  | CFixedPoint | 类别：非 const |
| CombatUnit | GetCurrentVeterancyLevel |  | int32 | 类别：非 const |
| CombatUnit | GetCurrentVeterancyLevelEffect |  | CString | 类别：非 const |
| CombatUnit | GetCurrentVeterancyLevelIcon |  | Unknown | 类别：非 const |
| CombatUnit | GetCurrentVeterancyLevelName |  | CString | 类别：非 const |
| CombatUnit | GetCustom | CustomLocalization | CString | 类别：非 const |
| CombatUnit | GetDefenseBreakdown |  | CString | 类别：非 const |
| CombatUnit | GetDefenseFormatted |  | CString | 类别：非 const |
| CombatUnit | GetDefenseRaw |  | CFixedPoint | 类别：非 const |
| CombatUnit | GetDemoralized |  | int64 | 类别：非 const |
| CombatUnit | GetExperienceGainDescription |  | CString | 类别：非常量 |
| CombatUnit | GetFront |  | Front | 类别：非常量 |
| CombatUnit | GetIconString |  | CString | 类别：非常量 |
| CombatUnit | GetIconTexture |  | Unknown | 类别：非常量 |
| CombatUnit | GetManpowerFormatted |  | CString | 类别：非常量 |
| CombatUnit | GetManpowerRaw |  | int64 | 类别：非常量 |
| CombatUnit | GetManpowerTooltip |  | CString | 类别：非常量 |
| CombatUnit | GetMaxManpower |  | int64 | 类别：非常量 |
| CombatUnit | GetMilitaryFormation |  | MilitaryFormation | 类别：非常量 |
| CombatUnit | GetMobilization |  | CFixedPoint | 类别：非常量 |
| CombatUnit | GetMorale |  | CString | 类别：非常量 |
| CombatUnit | GetMoraleGainDesc |  | CString | 类别：非常量 |
| CombatUnit | GetMoraleModifierBreakdown |  | CString | 类别：非常量 |
| CombatUnit | GetMoraleRaw |  | CFixedPoint | 类别：非常量 |
| CombatUnit | GetMoraleTooltip |  | CString | 类别：非常量 |
| CombatUnit | GetName |  | CString | 类别：非常量 |
| CombatUnit | GetNeededExperienceForNextLevel |  | CFixedPoint | 类别：非常量 |
| CombatUnit | GetOffenseBreakdown |  | CString | 类别：非常量 |
| CombatUnit | GetOffenseFormatted |  | CString | 类别：非常量 |
| CombatUnit | GetOffenseRaw |  | CFixedPoint | 类别：非常量 |
| CombatUnit | GetPowerProjection |  | CFixedPoint | 类别：非常量 |
| CombatUnit | GetTooltipTag |  | CString | 类别：非常量 |
| CombatUnit | GetType |  | CString | 类别：非常量 |
| CombatUnit | GetUnitType |  | CombatUnitType | 类别：非常量 |
| CombatUnit | HasBattle |  | bool |  |
| CombatUnit | HasFront |  | bool |  |
| CombatUnit | IsArmyUnit |  | bool |  |
| CombatUnit | IsConscript |  | bool |  |
| CombatUnit | IsFullyMobilized |  | bool |  |
| CombatUnit | IsMobilizing |  | bool |  |
| CombatUnit | IsNavyUnit |  | bool |  |
| CombatUnit | IsValid |  | bool |  |
| CombatUnit | MakeScope |  | Scope |  |
| CombatUnit | Self |  | CombatUnit |  |
| CombatUnitGroup | AccessSelf |  | CombatUnitGroup | 类别：常量 |
| CombatUnitGroup | GetDesc |  | CString | 类别：非常量 |
| CombatUnitGroup | GetIDString |  | CString | 类别：非常量 |
| CombatUnitGroup | GetName |  | CString | 类别：非常量 |
| CombatUnitGroup | GetTooltipTag |  | CString | 类别：非常量 |
| CombatUnitGroup | GetUIColor |  | CVector4f | 类别：非常量 |
| CombatUnitGroup | Self |  | CombatUnitGroup |  |
| CombatUnitType | AccessSelf |  | CombatUnitType | 类别：常量 |
| CombatUnitType | GetBasePowerProjection |  | CFixedPoint | 类别：非常量 |
| CombatUnitType | GetBattleModifier |  | Modifier | 类别：非常量 |
| CombatUnitType | GetCustom | CustomLocalization | CString | 类别：非常量 |
| CombatUnitType | GetDefaultTexture |  | Unknown | 类别：非常量 |
| CombatUnitType | GetDesc |  | CString | 类别：非常量 |
| CombatUnitType | GetFormationModifier |  | Modifier | 类别：非常量 |
| CombatUnitType | GetGroup |  | CombatUnitGroup | 类别：非常量 |
| CombatUnitType | GetIconString |  | CString | 类别：非常量 |
| CombatUnitType | GetName |  | CString | 类别：非常量 |
| CombatUnitType | GetNameNoFormatting |  | CString | 类别：非常量 |
| CombatUnitType | GetNameWithCulture | Culture | CString | 类别：非常量 |
| CombatUnitType | GetRequirements |  | CString | 类别：非常量 |
| CombatUnitType | GetTextureForCulture | Culture | Unknown | 类别：非常量 |
| CombatUnitType | GetTooltipTag |  | CString | 类别：非常量 |
| CombatUnitType | GetUpkeepModifier |  | Modifier | 类别：非常量 |
| CombatUnitType | IsValid |  | bool |  |
| CombatUnitType | MakeScope |  | Scope |  |
| CombatUnitType | Self |  | CombatUnitType |  |
| Command | AccessSelf |  | Command | 类别：常量 |
| Command | Execute |  | void |  |
| Command | GetConfirmationDesc |  | CString | 类别：非常量 |
| Command | GetDesc |  | CString | 类别：非常量 |
| Command | IsPotential |  | bool |  |
| Command | IsRedundant |  | bool |  |
| Command | IsValid |  | bool |  |
| Command | Self |  | Command |  |
| Command | ShouldAskConfirmation |  | bool |  |
| CommanderOrderType | AccessSelf |  | CommanderOrderType | 类别：常量 |
| CommanderOrderType | CanEscapeFromBattle |  | bool |  |
| CommanderOrderType | GetAltName | CString | CString | 类别：非常量 |
| CommanderOrderType | GetClickSound |  | Unknown | 类别：非常量 |
| CommanderOrderType | GetCustom | CustomLocalization | CString | 类别：非常量 |
| CommanderOrderType | GetDesc |  | CString | 类别：非常量 |
| CommanderOrderType | GetEscapePowerRatio |  | CFixedPoint | 类别：非常量 |
| CommanderOrderType | GetModifier |  | Modifier | 类别：非常量 |
| CommanderOrderType | GetName |  | CString | 类别：非常量 |
| CommanderOrderType | GetNameNoFormatting |  | CString | 类别：非常量 |
| CommanderOrderType | GetTexture |  | Unknown | 类别：非常量 |
| CommanderOrderType | GetTooltipTag |  | CString | 类别：非常量 |
| CommanderOrderType | HasAdvanceBehavior |  | bool |  |
| CommanderOrderType | IsBasicOrderType |  | bool |  |
| CommanderOrderType | IsRaidConvoys |  | bool |  |
| CommanderOrderType | IsStandBy |  | bool |  |
| CommanderOrderType | IsValid |  | bool |  |
| CommanderOrderType | MakeScope |  | Scope |  |
| CommanderOrderType | Self |  | CommanderOrderType |  |
| CommanderPanel | AccessCharacter |  | Character | 类别：常量 |
| CommanderPanel | AccessSelf |  | CommanderPanel | 类别：常量 |
| CommanderPanel | GetCharacter |  | Character | 类别：非常量 |
| CommanderPanel | Self |  | CommanderPanel |  |
| CommanderRank | AccessSelf |  | CommanderRank | 类别：常量 |
| CommanderRank | GetModifiers | Character | CString | 类别：非常量 |
| CommanderRank | GetName | Character | CString | 类别：非常量 |
| CommanderRank | GetTexture |  | Unknown | 类别：非常量 |
| CommanderRank | GetTitle | Unknown | CString | 类别：非常量 |
| CommanderRank | GetTooltipTag |  | CString | 类别：非常量 |
| CommanderRank | Self |  | CommanderRank |  |
| CompaniesPanel | AccessSelf |  | CompaniesPanel | 类别：常量 |
| CompaniesPanel | GetCompanies |  | Unknown | 类别：非常量 |
| CompaniesPanel | IsSorted | Unknown | bool |  |
| CompaniesPanel | Self |  | CompaniesPanel |  |
| CompaniesPanel | Sort | CString | void |  |
| Company | AccessCompanyType |  | CompanyType | 类别：常量 |
| Company | AccessExecutive |  | Character | 类别：常量 |
| Company | AccessSelf |  | Company | 类别：常量 |
| Company | GetActiveCharters | CompanyCharterType | Unknown | 类别：非常量 |
| Company | GetAdditionalIndustryTypes |  | Unknown | 类别：非常量 |
| Company | GetBuilding |  | Building | 类别：非常量 |
| Company | GetBuildingTypeLevels | BuildingType | int32 | 类别：非常量 |
| Company | GetBuildingTypeSizeDescription | BuildingType | CString | 类别：非常量 |
| Company | GetBuildingTypes |  | Unknown | 类别：非常量 |
| Company | GetBuildingTypesForTrends |  | Unknown | 类别：非常量 |
| Company | GetBuildingTypesSizeDescription |  | CString | 类别：非常量 |
| Company | GetColonies |  | Unknown | 类别：非常量 |
| Company | GetCompanyType |  | CompanyType | 类别：非常量 |
| Company | GetCountry |  | Country | 类别：非常量 |
| Company | GetCustom | CustomLocalization | CString | 类别：非常量 |
| Company | GetEstablishmentDate |  | Date | 类别：非常量 |
| Company | GetExecutive |  | Character | 类别：非常量 |
| Company | GetFormattedProductivity |  | CString | 类别：非常量 |
| Company | GetGlobalProductivityComparison |  | CFixedPoint | 类别：非常量 |
| Company | GetHQProfitDescription |  | CString | 类别：非常量 |
| Company | GetIsProducingPrestigeGoodsDesc |  | CString | 类别：非常量 |
| Company | GetMonopoliesDesc |  | CString | 类别：非常量 |
| Company | GetMonopolyBuildingTypes |  | Unknown | 类别：非常量 |
| Company | GetName |  | CString | 类别：非常量 |
| Company | GetNameFromPerspective | Unknown | CString | 类别：非常量 |
| Company | GetNameNoFormatting |  | CString | 类别：非常量 |
| Company | GetNameNoIcon |  | CString | 类别：非常量 |
| Company | GetNumEmployedBuildingLevels |  | int32 | 类别：非常量 |
| Company | GetNumOwnedBuildingLevels |  | int32 | 类别：非常量 |
| Company | GetOwnedCountries |  | Unknown | 类别：非常量 |
| Company | GetOwnedTradeCenters |  | Unknown | 类别：非常量 |
| Company | GetPrestigeGoods |  | Unknown | 类别：非常量 |
| Company | GetProducedPrestigeGoodsDesc |  | CString | 类别：非常量 |
| Company | GetProductivity |  | CFixedPoint | 类别：非常量 |
| Company | GetProductivityTrend |  | DataTrend | 类别：非常量 |
| Company | GetProfit |  | CFixedPoint | 类别：非常量 |
| Company | GetProfitTrend |  | DataTrend | 类别：非常量 |
| Company | GetProsperity |  | CFixedPoint | 类别：非常量 |
| Company | GetProsperityChange |  | CFixedPoint | 类别：非常量 |
| Company | GetProsperityChangeDesc |  | CString | 类别：非常量 |
| Company | GetProsperityTrend |  | DataTrend | 类别：非常量 |
| Company | GetRegionalHQs |  | Unknown | 类别：非常量 |
| Company | GetRevenueTrend |  | DataTrend | 类别：非常量 |
| Company | GetSizeTrend |  | DataTrend | 类别：非常量 |
| Company | GetState |  | State | 类别：非常量 |
| Company | GetTargetProsperity |  | CFixedPoint | 类别：非常量 |
| Company | GetTargetProsperityBreakdown |  | CString | 类别：非常量 |
| Company | GetTargetProsperityDesc |  | CString | 类别：非常量 |
| Company | GetTooltipTag |  | CString | 类别：非常量 |
| Company | GetTrendForBuildingType | BuildingType | DataTrend | 类别：非常量 |
| Company | HasAdditionalIndustry | BuildingType | bool |  |
| Company | HasAnyColonizationCharterActive |  | bool |  |
| Company | HasAnyIndustryCharterActive |  | bool |  |
| Company | HasAnyInvestmentCharterActive |  | bool |  |
| Company | HasAnyMonopolyCharterActive |  | bool |  |
| Company | HasAnyTradeCharterActive |  | bool |  |
| Company | HasHighProductivity |  | bool |  |
| Company | HasLowProductivity |  | bool |  |
| Company | HasMonopoly | Unknown | bool |  |
| Company | IsPinnedInOutliner |  | bool |  |
| Company | IsProducingPrestigeGoods |  | bool |  |
| Company | IsProsperous |  | bool |  |
| Company | IsValid |  | bool |  |
| Company | MakeScope |  | Scope |  |
| Company | Self |  | Company |  |
| Company | ToggleBuildingCharter | CompanyCharterType BuildingType | Command |  |
| Company | ToggleCharter | CompanyCharterType | Command |  |
| Company | TogglePinInOutliner |  | void |  |
| Company | ToggleRegionCharter | CompanyCharterType StateRegion | Command |  |
| CompanyChangeNamePopup | AccessSelf |  | CompanyChangeNamePopup | 类别：常量 |
| CompanyChangeNamePopup | Confirm |  | Command |  |
| CompanyChangeNamePopup | GetCompany |  | Company | 类别：非常量 |
| CompanyChangeNamePopup | OnEditName |  | void |  |
| CompanyChangeNamePopup | Self |  | CompanyChangeNamePopup |  |
| CompanyCharter | AccessSelf |  | CompanyCharter | 类别：常量 |
| CompanyCharter | GetBuildingType |  | BuildingType | 类别：非常量 |
| CompanyCharter | GetDesc |  | CString | 类别：非常量 |
| CompanyCharter | GetEffects |  | CString | 类别：非常量 |
| CompanyCharter | GetName |  | CString | 类别：非常量 |
| CompanyCharter | GetNameNoFormatting |  | CString | 类别：非常量 |
| CompanyCharter | GetNameNoIcon |  | CString | 类别：非常量 |
| CompanyCharter | GetStateRegion |  | StateRegion | 类别：非常量 |
| CompanyCharter | GetToggleCommand |  | Command | 类别：非常量 |
| CompanyCharter | GetTooltipTag |  | CString | 类别：非常量 |
| CompanyCharter | GetType |  | CompanyCharterType | 类别：非常量 |
| CompanyCharter | Self |  | CompanyCharter |  |
| CompanyCharterType | AccessSelf |  | CompanyCharterType | 类别：常量 |
| CompanyCharterType | GetAuthorityCost | Company | CFixedPoint | 类别：非常量 |
| CompanyCharterType | GetDesc |  | CString | 类别：非常量 |
| CompanyCharterType | GetEffects |  | CString | 类别：非常量 |
| CompanyCharterType | GetIcon |  | Unknown | 类别：非常量 |
| CompanyCharterType | GetName |  | CString | 类别：非常量 |
| CompanyCharterType | GetNameNoFormatting |  | CString | 类别：非常量 |
| CompanyCharterType | GetNameNoIcon |  | CString | 类别：非常量 |
| CompanyCharterType | GetPotentialBuildings | Company | Unknown | 类别：非常量 |
| CompanyCharterType | GetPotentialRegions | Company | Unknown | 类别：非常量 |
| CompanyCharterType | GetTooltipTag |  | CString | 类别：非常量 |
| CompanyCharterType | IsColonizationCharter |  | bool |  |
| CompanyCharterType | IsIndustryCharter |  | bool |  |
| CompanyCharterType | IsInvestmentCharter |  | bool |  |
| CompanyCharterType | IsMonopolyCharter |  | bool |  |
| CompanyCharterType | IsTargettingBuildings |  | bool |  |
| CompanyCharterType | IsTargettingRegions |  | bool |  |
| CompanyCharterType | IsTradeCharter |  | bool |  |
| CompanyCharterType | Self |  | CompanyCharterType |  |
| CompanyPanel | AccessSelf |  | CompanyPanel | 类别：常量 |
| CompanyPanel | GetCompany |  | Company | 类别：非常量 |
| CompanyPanel | Self |  | CompanyPanel |  |
| CompanyType | AccessBuildingTypes | Country | Unknown | 类别：常量 |
| CompanyType | AccessSelf |  | CompanyType | 类别：常量 |
| CompanyType | CanProducePrestigeGoods |  | bool |  |
| CompanyType | GetAverageProductivity |  | CFixedPoint | 类别：非常量 |
| CompanyType | GetBackground |  | Unknown | 类别：非常量 |
| CompanyType | GetCategory |  | CString | 类别：非常量 |
| CompanyType | GetCustom | CustomLocalization | CString | 类别：非常量 |
| CompanyType | GetIcon |  | Unknown | 类别：非常量 |
| CompanyType | GetKey |  | CString | 类别：非常量 |
| CompanyType | GetName |  | CString | 类别：非常量 |
| CompanyType | GetNameNoFormatting |  | CString | 类别：非常量 |
| CompanyType | GetNumBuildingLevels |  | int32 | 类别：非常量 |
| CompanyType | GetPotentialBuildingTypes | Unknown | Unknown | 类别：非常量 |
| CompanyType | GetPotentialState |  | State | 类别：非常量 |
| CompanyType | GetPrestigeGoods |  | Unknown | 类别：非常量 |
| CompanyType | GetProducedPrestigeGoodsDesc |  | CString | 类别：非常量 |
| CompanyType | GetProductivity |  | CFixedPoint | 类别：非常量 |
| CompanyType | GetProsperityModifier |  | Modifier | 类别：非常量 |
| CompanyType | GetTooltipTag |  | CString | 类别：非常量 |
| CompanyType | IsFlavoredCompany |  | bool |  |
| CompanyType | MakeScope |  | Scope |  |
| CompanyType | Self |  | CompanyType |  |
| CompanyType | UsesDynamicNaming |  | bool |  |
| ConfirmationWindow | AccessSelf |  | ConfirmationWindow | 类别：常量 |
| ConfirmationWindow | GetDesc |  | CString | 类别：非常量 |
| ConfirmationWindow | Self |  | ConfirmationWindow |  |
| ConsoleMenuItem | AccessSelf |  | ConsoleMenuItem | 类别：常量 |
| ConsoleMenuItem | GetHelp |  | CString | 类别：非常量 |
| ConsoleMenuItem | GetName |  | CString | 类别：非常量 |
| ConsoleMenuItem | IsCurrentGroup |  | bool |  |
| ConsoleMenuItem | Select |  | void |  |
| ConsoleMenuItem | Self |  | ConsoleMenuItem |  |
| ConsoleWindow | AccessSelf |  | ConsoleWindow | 类别：常量 |
| ConsoleWindow | IsMenuShown |  | bool |  |
| ConsoleWindow | Self |  | ConsoleWindow |  |
| ConsoleWindow | ToggleMenu |  | void |  |
| ConstructionPanel | AccessCurrentGovernmentConstructionQueuePage | Country | int32 | 类别：常量 |
| ConstructionPanel | AccessCurrentPrivateConstructionQueuePage | Country | int32 | 类别：常量 |
| ConstructionPanel | AccessSelf |  | ConstructionPanel | 类别：常量 |
| ConstructionPanel | GetConstructionEntries |  | Unknown | 类别：非常量 |
| ConstructionPanel | GetCountry |  | Country | 类别：非常量 |
| ConstructionPanel | GetFilter |  | Unknown | 类别：非常量 |
| ConstructionPanel | GetNumGovernmentConstructionQueueElements | Country | int32 | 类别：非常量 |
| ConstructionPanel | GetNumGovernmentConstructionQueuePages | Country | int32 | 类别：非常量 |
| ConstructionPanel | GetNumPrivateConstructionQueueElements | Country | int32 | 类别：非常量 |
| ConstructionPanel | GetNumPrivateConstructionQueuePages | Country | int32 | 类别：非常量 |
| ConstructionPanel | IsFilterNo | CString | bool |  |
| ConstructionPanel | IsFilterYes | CString | bool |  |
| ConstructionPanel | IsFiltered | CString | bool |  |
| ConstructionPanel | IsShowingGovernmentConstructions |  | bool |  |
| ConstructionPanel | IsShowingPrivateConstructions |  | bool |  |
| ConstructionPanel | NextGovernmentConstructionQueuePage | Country | void |  |
| ConstructionPanel | NextPrivateConstructionQueuePage | Country | void |  |
| ConstructionPanel | PrevGovernmentConstructionQueuePage | Country | void |  |
| ConstructionPanel | PrevPrivateConstructionQueuePage | Country | void |  |
| ConstructionPanel | Self |  | ConstructionPanel |  |
| ConstructionPanel | SetFilterMode | CString CString | void |  |
| ConstructionPanel | ShowGovernmentConstructions |  | void |  |
| ConstructionPanel | ShowPrivateConstructions |  | void |  |
| ConstructionQueueElement | AccessBuilding |  | Building | 类别：常量 |
| ConstructionQueueElement | AccessSelf |  | ConstructionQueueElement | 类别：常量 |
| ConstructionQueueElement | AccessState |  | State | 类别：常量 |
| ConstructionQueueElement | CalcPercentComplete |  | CFixedPoint |  |
| ConstructionQueueElement | CancelConstruction |  | Command |  |
| ConstructionQueueElement | GetBaseConstructionSpeed |  | CFixedPoint | 类别：非常量 |
| ConstructionQueueElement | GetBuilding |  | Building | 类别：非常量 |
| ConstructionQueueElement | GetCompanyConstructionBonusDesc |  | CString | 类别：非常量 |
| ConstructionQueueElement | GetConstructionSpeed |  | CFixedPoint | 类别：非常量 |
| ConstructionQueueElement | GetConstructionSpeedPerWeekDesc |  | CString | 类别：非常量 |
| ConstructionQueueElement | GetInvestorBuilding |  | Building | 类别：非常量 |
| ConstructionQueueElement | GetInvestorBuildingType |  | BuildingType | 类别：非常量 |
| ConstructionQueueElement | GetInvestorCountry |  | Country | 类别：非常量 |
| ConstructionQueueElement | GetInvestorState |  | State | 类别：非常量 |
| ConstructionQueueElement | GetQueueNumber |  | int32 | 类别：非常量 |
| ConstructionQueueElement | GetState |  | State | 类别：非常量 |
| ConstructionQueueElement | GetTooltip |  | CString | 类别：非常量 |
| ConstructionQueueElement | GetTooltipTag |  | CString | 类别：非常量 |
| ConstructionQueueElement | GetTotalProgress |  | CFixedPoint | 类别：非常量 |
| ConstructionQueueElement | GetWeeksLeft |  | int32 | 类别：非常量 |
| ConstructionQueueElement | IsCurrentlyUnderConstruction |  | bool |  |
| ConstructionQueueElement | IsPrivatelyFundedConstruction |  | bool |  |
| ConstructionQueueElement | IsValidConstruction |  | bool |  |
| ConstructionQueueElement | MoveDown |  | Command |  |
| ConstructionQueueElement | MoveToBottom |  | Command |  |
| ConstructionQueueElement | MoveToTop |  | Command |  |
| ConstructionQueueElement | MoveUp |  | Command |  |
| ConstructionQueueElement | Self |  | ConstructionQueueElement |  |
| Container | AccessSelf |  | Container | 类别：常量 |
| Container | Self |  | Container |  |
| ContextMenuItem | AccessSelf |  | ContextMenuItem | 类别：常量 |
| ContextMenuItem | Enabled |  | bool |  |
| ContextMenuItem | GetIcon |  | Unknown | 类别：非常量 |
| ContextMenuItem | GetLabel |  | CString | 类别：非常量 |
| ContextMenuItem | Self |  | ContextMenuItem |  |
| ContextualDiplomaticActionType | AccessCountry |  | Country | 类别：常量 |
| ContextualDiplomaticActionType | AccessSelf |  | ContextualDiplomaticActionType | 类别：常量 |
| ContextualDiplomaticActionType | GetCountry |  | Country | 类别：非常量 |
| ContextualDiplomaticActionType | GetDiplomaticActionType |  | DiplomaticActionType | 类别：非常量 |
| ContextualDiplomaticActionType | GetTooltipTag |  | CString | 类别：非常量 |
| ContextualDiplomaticActionType | Self |  | ContextualDiplomaticActionType |  |
| ContextualDiplomaticPact | AccessDiplomaticPact |  | DiplomaticPact | 类别：常量 |
| ContextualDiplomaticPact | AccessSelf |  | ContextualDiplomaticPact | 类别：常量 |
| ContextualDiplomaticPact | GetContextCountry |  | Country | 类别：非常量 |
| ContextualDiplomaticPact | GetDiplomaticActionType |  | DiplomaticActionType | 类别：非常量 |
| ContextualDiplomaticPact | GetDiplomaticPact |  | DiplomaticPact | 类别：非常量 |
| ContextualDiplomaticPact | GetOtherCountry |  | Country | 类别：非常量 |
| ContextualDiplomaticPact | GetTooltip |  | CString | 类别：非常量 |
| ContextualDiplomaticPact | GetTooltipTag |  | CString | 类别：非常量 |
| ContextualDiplomaticPact | IsOngoingForContextCountry |  | bool |  |
| ContextualDiplomaticPact | IsOngoingForOtherCountry |  | bool |  |
| ContextualDiplomaticPact | Self |  | ContextualDiplomaticPact |  |
| CountriesPanel | AccessSelf |  | CountriesPanel | 类别：常量 |
| CountriesPanel | GetCountries |  | Unknown | 类别：非常量 |
| CountriesPanel | IsSorted | Unknown | bool |  |
| CountriesPanel | Self |  | CountriesPanel |  |
| CountriesPanel | Sort | CString | void |  |
| Country | AccessActiveDiplomaticPactTypes |  | Unknown | 类别：常量 |
| Country | AccessActiveDiplomaticPacts | ContextualDiplomaticActionType | Unknown | 类别：常量 |
| Country | AccessActiveDiplomaticPlays |  | Unknown | 类别：常量 |
| Country | AccessActiveEconomyLaws |  | Unknown | 类别：常量 |
| Country | AccessActiveHumanRightsLaws |  | Unknown | 类别：常量 |
| Country | AccessActiveInterestGroups |  | Unknown | 类别：常量 |
| Country | AccessActiveJournalEntries |  | Unknown | 类别：常量 |
| Country | AccessActiveLawFromGroup | LawGroup | Law | 类别：常量 |
| Country | AccessActiveNonPlayerObjectiveJournalEntries |  | Unknown | 类别：常量 |
| Country | AccessActiveOtherLaws |  | Unknown | 类别：常量 |
| Country | AccessActiveParties |  | Unknown | 类别：常量 |
| Country | AccessActivePinnedNonPlayerObjectiveJournalEntries |  | Unknown | 类别：常量 |
| Country | AccessActivePinnedPlayerObjectiveJournalEntries |  | Unknown | 类别：常量 |
| Country | AccessActivePlayerObjectiveJournalEntries |  | Unknown | 类别：常量 |
| Country | AccessActivePowerStructureLaws |  | Unknown | 类别：常量 |
| Country | AccessAdmirals |  | Unknown | 类别：常量 |
| Country | AccessAdmiralsOffer |  | Unknown | 类别：常量 |
| Country | AccessAllInterestGroups |  | Unknown | 类别：常量 |
| Country | AccessCapital |  | State | 类别：常量 |
| Country | AccessCivilWars |  | Unknown | 类别：常量 |
| Country | AccessConstructionQueue |  | Unknown | 类别：常量 |
| Country | AccessCurrentlyResearchedTechnology |  | Technology | 类别：常量 |
| Country | AccessDefinition |  | CountryDefinition | 类别：常量 |
| Country | AccessFirstMarket |  | Market | 类别：常量 |
| Country | AccessFormableCountries |  | Unknown | 类别：常量 |
| Country | AccessGenerals |  | Unknown | 类别：常量 |
| Country | AccessGeneralsOffer |  | Unknown | 类别：常量 |
| Country | AccessGovernment |  | GovernmentType | 类别：常量 |
| Country | AccessGovernmentConstructionQueue |  | Unknown | 类别：常量 |
| 国家 | AccessHeaviestJournalEntry |  | JournalEntry | 类别：const |
| 国家 | AccessHeir |  | Character | 类别：const |
| 国家 | AccessInactiveJournalEntries |  | Unknown | 类别：const |
| 国家 | AccessInstitutions |  | Unknown | 类别：const |
| 国家 | AccessInterestGroupsInGovernment |  | Unknown | 类别：const |
| 国家 | AccessInterestGroupsInOpposition |  | Unknown | 类别：const |
| 国家 | AccessInterests |  | Unknown | 类别：const |
| 国家 | AccessLandHQs |  | Unknown | 类别：const |
| 国家 | AccessLastElectionParties |  | Unknown | 类别：const |
| 国家 | AccessLawBeingEnacted |  | Law | 类别：const |
| 国家 | AccessLawsWithGovernmentOrMovementSupport |  | Unknown | 类别：const |
| 国家 | AccessLawsWithoutGovernmentOrMovementSupport |  | Unknown | 类别：const |
| 国家 | AccessMarginalInterestGroups |  | Unknown | 类别：const |
| 国家 | AccessModifier |  | Modifier | 类别：const |
| 国家 | AccessNavalHQs |  | Unknown | 类别：const |
| 国家 | AccessNonRevolutionaryPoliticalMovements |  | Unknown | 类别：const |
| 国家 | AccessNumResearchableTechnologies |  | int32 | 类别：const |
| 国家 | AccessOverlord |  | Country | 类别：const |
| 国家 | AccessPagedGovernmentConstructionQueue | int32 Unknown | Unknown | 类别：const |
| 国家 | AccessPagedPrivateConstructionQueue | int32 Unknown | Unknown | 类别：const |
| 国家 | AccessPoliticalMovements |  | Unknown | 类别：const |
| 国家 | AccessPopCultures |  | Unknown | 类别：const |
| 国家 | AccessPopCulturesSortedByPolStr |  | Unknown | 类别：const |
| 国家 | AccessPopCulturesSortedByPopulation |  | Unknown | 类别：const |
| 国家 | AccessPopReligionsSortedByPolStr |  | Unknown | 类别：const |
| 国家 | AccessPopReligionsSortedByPopulation |  | Unknown | 类别：const |
| 国家 | AccessPopTypes |  | Unknown | 类别：const |
| 国家 | AccessPopTypesSortedOnPolStr |  | Unknown | 类别：const |
| 国家 | AccessPopTypesSortedOnPopulation |  | Unknown | 类别：const |
| 国家 | AccessPowerBloc |  | PowerBloc | 类别：const |
| 国家 | AccessPrivateConstructionQueue |  | Unknown | 类别：const |
| 国家 | AccessReleasableCountries |  | Unknown | 类别：const |
| 国家 | AccessResearchableTechnologiesMilitary |  | Unknown | 类别：const |
| 国家 | AccessResearchableTechnologiesOther |  | Unknown | 类别：const |
| 国家 | AccessResearchableTechnologiesProduction |  | Unknown | 类别：const |
| 国家 | AccessResearchableTechnologiesSociety |  | Unknown | 类别：const |
| 国家 | AccessRuler |  | Character | 类别：const |
| 国家 | AccessSecessions |  | Unknown | 类别：const |
| 国家 | AccessSelf |  | Country | 类别：const |
| 国家 | AccessShippingLanes |  | Unknown | 类别：const |
| 国家 | AccessShippingOriginStates | Province | Unknown | 类别：const |
| 国家 | AccessShownCurrentlyConstructingGovernmentQueue |  | Unknown | 类别：const |
| 国家 | AccessShownCurrentlyConstructingPrivateQueue |  | Unknown | 类别：const |
| 国家 | AccessShownCurrentlyConstructingQueue |  | Unknown | 类别：const |
| 国家 | AccessStateReligion |  | Religion | 类别：const |
| 国家 | AccessStates |  | Unknown | 类别：const |
| 国家 | AccessStrategies |  | Unknown | 类别：const |
| 国家 | AccessTopOverlord |  | Country | 类别：const |
| 国家 | AccessTruces |  | Unknown | 类别：const |
| 国家 | AccessVioSovInterestedCountries | Country | Unknown | 类别：const |
| 国家 | AccessVioSovWars | Country | Unknown | 类别：const |
| 国家 | AccessVisibleJournalEntries |  | Unknown | 类别：const |
| 国家 | AccessWars |  | Unknown | 类别：const |
| 国家 | CalcBaseConstructionSpeed |  | CFixedPoint |  |
| 国家 | CalcConscriptableBattalions |  | int32 |  |
| 国家 | CalcCulturalTurmoil | Culture | CFixedPoint |  |
| 国家 | CalcLibertyDesireLevel |  | LibertyDesireLevel |  |
| 国家 | CalcMaxNumDeclaredInterests |  | int32 |  |
| 国家 | CalcNumStatesInTurmoil |  | int32 |  |
| 国家 | CalcRelativeUsedGovernmentConstruction |  | CFixedPoint |  |
| 国家 | CalcRelativeUsedPrivateConstruction |  | CFixedPoint |  |
| 国家 | CalcTurmoil |  | CFixedPoint |  |
| 国家 | CalcUnusedConstruction |  | CFixedPoint |  |
| 国家 | CalcUsedConstruction |  | CFixedPoint |  |
| 国家 | CalcUsedGovernmentConstruction |  | CFixedPoint |  |
| 国家 | CalcUsedPrivateConstruction |  | CFixedPoint |  |
| 国家 | CanBuildingTypeBeMonopolized | BuildingType | bool |  |
| 国家 | CanSignTreatyWith | Country | bool |  |
| 国家 | CanTradeGoods | Unknown | bool |  |
| 国家 | CreateCompany | CompanyType | Command |  |
| 国家 | DeclareBankruptcy |  | Command |  |
| 国家 | DeclareInterest | StrategicRegion | Command |  |
| 国家 | DemobilizeAllArmies |  | Command |  |
| 国家 | EstimatedConstructionQueueDuration |  | int32 |  |
| 国家 | EstimatedGovernmentConstructionQueueDuration |  | int32 |  |
| 国家 | EstimatedPrivateConstructionQueueDuration |  | int32 |  |
| 国家 | Exists |  | bool |  |
| 国家 | GetAIStrategiesDesc |  | CString | 类别：nonconst |
| 国家 | GetActiveConstructionProjectsDesc |  | CString | 类别：nonconst |
| 国家 | GetActiveLawFrom | Unknown | Law | 类别：nonconst |
| 国家 | GetActiveLawFromGroup | CString | Law | 类别：nonconst |
| 国家 | GetActivePeaceDealDesc |  | CString | 类别：nonconst |
| 国家 | GetAdditionalExpensesTrend |  | DataTrend | 类别：nonconst |
| 国家 | GetAdditionalIncomeTrend |  | DataTrend | 类别：nonconst |
| 国家 | GetAdditionalSOLFactorsDescAll |  | CString | 类别：nonconst |
| 国家 | GetAdditionalSOLFactorsDescMiddle |  | CString | 类别：nonconst |
| 国家 | GetAdditionalSOLFactorsDescPoor |  | CString | 类别：nonconst |
| 国家 | GetAdditionalSOLFactorsDescRich |  | CString | 类别：nonconst |
| 国家 | GetAdditionalSOLFactorsDescWithCulture | Culture | CString | 类别：nonconst |
| 国家 | GetAdditionalSOLFactorsDescWithCultureMiddle | Culture | CString | 类别：nonconst |
| 国家 | GetAdditionalSOLFactorsDescWithCulturePoor | Culture | CString | 类别：nonconst |
| 国家 | GetAdditionalSOLFactorsDescWithCultureRich | Culture | CString | 类别：nonconst |
| 国家 | GetAdjective |  | CString | 类别：nonconst |
| 国家 | GetAdjectiveNoFlag |  | CString | 类别：nonconst |
| 国家 | GetAdjectiveNoFormatting |  | CString | 类别：nonconst |
| 国家 | GetAllAcceptanceStatusSegments |  | Unknown | 类别：nonconst |
| 国家 | GetAllGeneralDiploActions |  | Unknown | 类别：nonconst |
| 国家 | GetAllOverlordDiploActions |  | Unknown | 类别：nonconst |
| 国家 | GetAllPowerBlocLeaderDiploActions |  | Unknown | 类别：nonconst |
| 国家 | GetAllPowerBlocMemberDiploActions |  | Unknown | 类别：nonconst |
| 国家 | GetAllSubjectDiploActions |  | Unknown | 类别：nonconst |
| 国家 | GetAllianceLikeTreatiesBrokenDesc | Country | CString | 类别：nonconst |
| 国家 | GetAllianceLikeTreatiesBrokenFromPlayDesc | DiplomaticPlay | CString | 类别：nonconst |
| 国家 | GetAllianceLikeTreatiesBrokenOnWarDesc | Country | CString | 类别：nonconst |
| 国家 | GetAllianceLikeTreatiesList | Unknown | CString | 类别：nonconst |
| 国家 | GetAltAdjective | CString | CString | 类别：nonconst |
| 国家 | GetAltAdjectiveNoFlag | CString | CString | 类别：nonconst |
| 国家 | GetAltAdjectiveNoFormatting | CString | CString | 类别：nonconst |
| 国家 | GetAltName | CString | CString | 类别：nonconst |
| 国家 | GetAltNameNoFlag | CString | CString | 类别：nonconst |
| 国家 | GetAltNameNoFormatting | CString | CString | 类别：nonconst |
| 国家 | GetArableLand |  | int32 | 类别：nonconst |
| 国家 | GetArableLandDesc |  | CString | 类别：nonconst |
| 国家 | GetArmiesBreakdown |  | CString | 类别：nonconst |
| 国家 | GetArmyPowerProjection |  | CFixedPoint | 类别：nonconst |
| 国家 | GetArmyPowerProjectionDesc |  | CString | 类别：nonconst |
| 国家 | GetArmyReadinessStatusDesc |  | CString | 类别：nonconst |
| 国家 | GetAttainableCompanies |  | Unknown | 类别：nonconst |
| 国家 | GetAttitudeColor | Unknown | CVector4f | 类别：nonconst |
| 国家 | GetAttitudeTowards | Country | AIAttitude | 类别：nonconst |
| 国家 | GetAvailableCompanies |  | Unknown | 类别：nonconst |
| 国家 | GetAvailableGeneralDiploActions |  | Unknown | 类别：nonconst |
| 国家 | GetAvailableOverlordDiploActions |  | Unknown | 类别：nonconst |
| 国家 | GetAvailablePowerBlocLeaderDiploActions |  | Unknown | 类别：nonconst |
| 国家 | GetAvailablePowerBlocMemberDiploActions |  | Unknown | 类别：nonconst |
| 国家 | GetAvailableSubjectDiploActions |  | Unknown | 类别：nonconst |
| 国家 | GetAverageExpectedStandardOfLivingWithCultureMiddle | Unknown | CFixedPoint | 类别：nonconst |
| 国家 | GetAverageExpectedStandardOfLivingWithCulturePoor | Unknown | CFixedPoint | 类别：nonconst |
| 国家 | GetAverageExpectedStandardOfLivingWithCultureRich | Unknown | CFixedPoint | 类别：nonconst |
| 国家 | GetAverageSoLByPoliticalStrength |  | CFixedPoint | 类别：nonconst |
| 国家 | GetAverageSoLByPopulation |  | CFixedPoint | 类别：nonconst |
| 国家 | GetAverageSoLByPopulationTrend |  | DataTrend | 类别：nonconst |
| 国家 | GetAverageSoLByPopulationWithCulture | Unknown | CFixedPoint | 类别：nonconst |
| 国家 | GetAverageSoLLowerTrend |  | DataTrend | 类别：nonconst |
| 国家 | GetAverageSoLMiddleTrend |  | DataTrend | 类别：nonconst |
| 国家 | GetAverageSoLUpperTrend |  | DataTrend | 类别：nonconst |
| 国家 | GetAverageStandardOfLivingMiddle |  | CFixedPoint | 类别：nonconst |
| 国家 | GetAverageStandardOfLivingPoor |  | CFixedPoint | 类别：nonconst |
| 国家 | GetAverageStandardOfLivingRich |  | CFixedPoint | 类别：nonconst |
| 国家 | GetAverageStandardOfLivingWithCultureMiddle | Unknown | CFixedPoint | 类别：nonconst |
| 国家 | GetAverageStandardOfLivingWithCulturePoor | Unknown | CFixedPoint | 类别：nonconst |
| 国家 | GetAverageStandardOfLivingWithCultureRich | Unknown | CFixedPoint | 类别：nonconst |
| 国家 | GetAverageStateTaxCollectionMult |  | CFixedPoint | 类别：nonconst |
| 国家 | GetAverageStateTaxCollectionMultBreakdown |  | CString | 类别：nonconst |
| 国家 | GetAverageTaxWaste |  | CFixedPoint | 类别：nonconst |
| 国家 | GetAverageTaxWasteBreakdown |  | CString | 类别：nonconst |
| 国家 | GetBalanceTrend |  | DataDynamicTrend | 类别：nonconst |
| 国家 | GetBaseConstructionSpeedDesc |  | CString | 类别：nonconst |
| 国家 | GetBaseWeeklyTechnologySpread |  | CFixedPoint | 类别：nonconst |
| 国家 | GetBaseWeeklyTechnologySpreadForTech | Unknown | CFixedPoint | 类别：nonconst |
| 国家 | GetBattalions |  | int32 | 类别：nonconst |
| 国家 | GetBattalionsDesc |  | CString | 类别：nonconst |
| 国家 | GetBattalionsMobilizing |  | int32 | 类别：nonconst |
| 国家 | GetBattalionsRanking |  | CString | 类别：nonconst |
| 国家 | GetBolsterDesc |  | CString | 类别：nonconst |
| 国家 | GetBolsteringCostDesc |  | CString | 类别：nonconst |
| 国家 | GetCanBuildingTypeBeMonopolizedDesc | BuildingType | CString | 类别：nonconst |
| 国家 | GetCanSignTreatyWithDesc | Country | CString | 类别：nonconst |
| 国家 | GetCapital |  | State | 类别：nonconst |
| 国家 | GetColonialGrowthDetails |  | CString | 类别：nonconst |
| 国家 | GetCompanies |  | Unknown | 类别：nonconst |
| 国家 | GetCompanyConstructionEfficiencyBonusFormatted |  | CString | 类别：nonconst |
| 国家 | GetCompanyThroughputBonusFormatted |  | CString | 类别：nonconst |
| 国家 | GetConscriptedBattalions |  | int32 | 类别：nonconst |
| 国家 | GetConscriptionRatio |  | CFixedPoint | 类别：nonconst |
| 国家 | GetConstructionGoodsExpenseTrend |  | DataTrend | 类别：nonconst |
| 国家 | GetConstructionGoodsExpenses |  | CFixedPoint | 类别：nonconst |
| 国家 | GetConstructionGoodsExpensesByGoodsDesc | Unknown | CString | 类别：nonconst |
| 国家 | GetConstructionGoodsExpensesDesc |  | CString | 类别：nonconst |
| 国家 | GetConstructionQueueDesc |  | CString | 类别：nonconst |
| 国家 | GetConstructionsInCountry | Country | Unknown | 类别：nonconst |
| 国家 | GetConsumptionTaxIncome |  | CFixedPoint | 类别：nonconst |
| 国家 | GetConsumptionTaxTrend |  | DataTrend | 类别：nonconst |
| 国家 | GetConsumptionTaxesDesc |  | CString | 类别：nonconst |
| 国家 | GetConvoyEffectDesc |  | CString | 类别：nonconst |
| 国家 | GetCountriesWithTreaties |  | Unknown | 类别：nonconst |
| 国家 | GetCountryScorePosition |  | int32 | 类别：nonconst |
| 国家 | GetCountryScorePositionDesc |  | CString | 类别：nonconst |
| 国家 | GetCreditRatio |  | CFixedPoint | 类别：nonconst |
| 国家 | GetCreditTooltip |  | CString | 类别：nonconst |
| 国家 | GetCulturePolStrAsPercentage | Culture | CFixedPoint | 类别：nonconst |
| 国家 | GetCulturePopulation | Culture | int64 | 类别：nonconst |
| 国家 | GetCurrentLeverage | Unknown | CFixedPoint | 类别：nonconst |
| 国家 | GetCurrentLeverageShare | PowerBloc | CFixedPoint | 类别：nonconst |
| 国家 | GetCurrentPowerStruggleMonth |  | int32 | 类别：nonconst |
| 国家 | GetCurrentlyResearchedTechnology |  | Technology | 类别：nonconst |
| 国家 | GetCurrentlySpreadingTechsDesc |  | CString | 类别：nonconst |
| 国家 | GetCustom | CustomLocalization | CString | 类别：nonconst |
| 国家 | GetDailyRelationsProgress | Country | CFixedPoint | 类别：nonconst |
| 国家 | GetDaysUntilElection |  | int32 | 类别：nonconst |
| 国家 | GetDaysUntilRankLoss |  | int32 | 类别：nonconst |
| 国家 | GetDecisions |  | Unknown | 类别：nonconst |
| 国家 | GetDeclareBankruptcyDesc |  | CString | 类别：nonconst |
| 国家 | GetDecreasingInterestsDesc |  | CString | 类别：nonconst |
| 国家 | GetDeficitConvoyRatio |  | CFixedPoint | 类别：nonconst |
| 国家 | GetDeficitConvoyRatioForProgressBar |  | CFixedPoint | 类别：nonconst |
| 国家 | GetDeficitPowerRatio | Unknown | CFixedPoint | 类别：nonconst |
| 国家 | GetDeficitPowerRatioForProgressBar | CString | CFixedPoint | 类别：nonconst |
| 国家 | GetDefinition |  | CountryDefinition | 类别：nonconst |
| 国家 | GetDependents |  | int64 | 类别：nonconst |
| 国家 | GetDiplomaticAction | Unknown Unknown | DiplomaticAction | 类别：nonconst |
| 国家 | GetDiplomaticActionWithStates | Unknown Unknown Unknown Unknown | DiplomaticAction | 类别：nonconst |
| 国家 | GetDiplomaticPactsExpenseTrend |  | DataTrend | 类别：nonconst |
| 国家 | GetDiplomaticPactsIncomeTrend |  | DataTrend | 类别：nonconst |
| 国家 | GetDiplomaticStatusColor | Country | CVector4f | 类别：nonconst |
| 国家 | GetDividendsTaxTrend |  | DataTrend | 类别：nonconst |
| 国家 | GetDomesticallyOwnedGDP |  | CFixedPoint | 类别：nonconst |
| 国家 | GetDomesticallyOwnedGDPFraction |  | CFixedPoint | 类别：nonconst |
| 国家 | GetDraftTreaties |  | Unknown | 类别：nonconst |
| 国家 | GetDraftTreatiesWith | Unknown | Unknown | 类别：nonconst |
| 国家 | GetEconomicDependenceOn | Country | CString | 类别：nonconst |
| 国家 | GetEconomicDependenceOnDesc | Unknown | CString | 类别：nonconst |
| 国家 | GetEconomicDependenceOnRaw | Unknown | CFixedPoint | 类别：nonconst |
| 国家 | GetElection |  | Election | 类别：nonconst |
| 国家 | GetElectionPollTooltip |  | CString | 类别：nonconst |
| 国家 | GetElectoralConfidence |  | CFixedPoint | 类别：nonconst |
| 国家 | GetElectoralConfidenceEffectDesc |  | CString | 类别：nonconst |
| 国家 | GetEmployedWorkingAdults |  | int64 | 类别：nonconst |
| 国家 | GetEmptyAgitatorSlots |  | int32 | 类别：nonconst |
| 国家 | GetEnemyOccupation |  | CFixedPoint | 类别：nonconst |
| 国家 | GetEnforcedTreaties |  | Unknown | 类别：nonconst |
| 国家 | GetEnforcedTreatiesWith | Country | Unknown | 类别：nonconst |
| 国家 | GetEnforcedTreatiesWithDesc | Unknown | CString | 类别：nonconst |
| 国家 | GetEventsByCategory | CString | Unknown | 类别：nonconst |
| 国家 | GetExcessConvoyRatio |  | CFixedPoint | 类别：nonconst |
| 国家 | GetExcessConvoyRatioForProgressBar |  | CFixedPoint | 类别：nonconst |
| 国家 | GetExcessPowerRatio | Unknown | CFixedPoint | 类别：nonconst |
| 国家 | GetExcessPowerRatioForProgressBar | CString | CFixedPoint | 类别：nonconst |
| 国家 | GetExpectedSOLFactorsDescAll |  | CString | 类别：nonconst |
| 国家 | GetExpectedSOLFactorsDescMiddle |  | CString | 类别：nonconst |
| 国家 | GetExpectedSOLFactorsDescPoor |  | CString | 类别：nonconst |
| 国家 | GetExpectedSOLFactorsDescRich |  | CString | 类别：nonconst |
| 国家 | GetExpectedSOLFactorsDescWithCulture | Unknown | CString | 类别：nonconst |
| 国家 | GetExpectedSoLByPopulation |  | CFixedPoint | 类别：nonconst |
| 国家 | GetExpectedStandardOfLivingMiddle |  | CFixedPoint | 类别：nonconst |
| 国家 | GetExpectedStandardOfLivingPoor |  | CFixedPoint | 类别：nonconst |
| 国家 | GetExpectedStandardOfLivingRich |  | CFixedPoint | 类别：nonconst |
| 国家 | GetExpensesBreakdown |  | CString | 类别：nonconst |
| 国家 | GetExportSubventionsDescHigh | Goods | CString | 类别：nonconst |
| 国家 | GetExportSubventionsDescLow | Goods | CString | 类别：nonconst |
| 国家 | GetExportSubventionsDescMax | Goods | CString | 类别：nonconst |
| 国家 | GetExportTariffsDescHigh | Goods | CString | 类别：nonconst |
| 国家 | GetExportTariffsDescLow | Goods | CString | 类别：nonconst |
| 国家 | GetExportTariffsDescMax | Goods | CString | 类别：nonconst |
| 国家 | GetExportTariffsDescNone | Goods | CString | 类别：nonconst |
| 国家 | GetExportedAmount | Unknown | CFixedPoint | 类别：nonconst |
| 国家 | GetExports |  | Unknown | 类别：nonconst |
| 国家 | GetFirstPrimaryCulture |  | Culture | 类别：nonconst |
| 国家 | GetFlag |  | CoatOfArms | 类别：nonconst |
| 国家 | GetFlagTextIcon |  | CString | 类别：nonconst |
| 国家 | GetFlavorText |  | CString | 类别：nonconst |
| 国家 | GetFleetsBreakdown |  | CString | 类别：nonconst |
| 国家 | GetFlotillasRanking |  | CString | 类别：nonconst |
| 国家 | GetForeignOwnedGDP |  | CFixedPoint | 类别：nonconst |
| 国家 | GetForeignOwnedGDPDesc |  | CString | 类别：nonconst |
| 国家 | GetForeignOwnedGDPFraction |  | CFixedPoint | 类别：nonconst |
| 国家 | GetFormattedStandardOfLivingAll |  | CString | 类别：nonconst |
| 国家 | GetFormattedStandardOfLivingAllWithCulture | Culture | CString | 类别：nonconst |
| 国家 | GetFormattedStandardOfLivingLabelAll |  | CString | 类别：nonconst |
| 国家 | GetFormattedStandardOfLivingLabelAllWithCulture | Culture | CString | 类别：nonconst |
| 国家 | GetFormattedStandardOfLivingLabelMiddle |  | CString | 类别：nonconst |
| 国家 | GetFormattedStandardOfLivingLabelMiddleWithCulture | Culture | CString | 类别：nonconst |
| 国家 | GetFormattedStandardOfLivingLabelPoor |  | CString | 类别：nonconst |
| 国家 | GetFormattedStandardOfLivingLabelPoorWithCulture | Culture | CString | 类别：nonconst |
| 国家 | GetFormattedStandardOfLivingLabelRich |  | CString | 类别：nonconst |
| 国家 | GetFormattedStandardOfLivingLabelRichWithCulture | Culture | CString | 类别：nonconst |
| 国家 | GetFormattedStandardOfLivingMiddle |  | CString | 类别：nonconst |
| 国家 | GetFormattedStandardOfLivingMiddleWithCulture | Culture | CString | 类别：nonconst |
| 国家 | GetFormattedStandardOfLivingPoor |  | CString | 类别：nonconst |
| 国家 | GetFormattedStandardOfLivingPoorWithCulture | Culture | CString | 类别：nonconst |
| 国家 | GetFormattedStandardOfLivingRich |  | CString | 类别：nonconst |
| 国家 | GetFormattedStandardOfLivingRichWithCulture | Culture | CString | 类别：nonconst |
| 国家 | GetFreeArableLand |  | int32 | 类别：nonconst |
| 国家 | GetGDP |  | CFixedPoint | 类别：nonconst |
| 国家 | GetGDPOwnedInForeignCountries |  | CFixedPoint | 类别：nonconst |
| 国家 | GetGDPOwnedInForeignCountriesDesc |  | CString | 类别：nonconst |
| 国家 | GetGDPPerCapita |  | CFixedPoint | 类别：nonconst |
| 国家 | GetGDPPerCapitaRanking |  | CString | 类别：nonconst |
| 国家 | GetGDPRanking |  | CString | 类别：nonconst |
| 国家 | GetGDPTrend |  | DataTrend | 类别：nonconst |
| 国家 | GetGDPWithOwnershipsInForeignCountries |  | CFixedPoint | 类别：nonconst |
| 国家 | GetGameOverDateString |  | CString | 类别：nonconst |
| 国家 | GetGdpRatioOwnedBy | Unknown | CString | 类别：nonconst |
| 国家 | GetGdpRatioOwnedByDesc | Unknown | CString | 类别：nonconst |
| 国家 | GetGdpRatioOwnedByRaw | Unknown | CFixedPoint | 类别：nonconst |
| 国家 | GetGoldProgressDesc |  | CString | 类别：nonconst |
| 国家 | GetGoldReserveLimit |  | CFixedPoint | 类别：nonconst |
| 国家 | GetGoldReserveLimitDesc |  | CString | 类别：nonconst |
| 国家 | GetGoldReserveRatio |  | CFixedPoint | 类别：nonconst |
| 国家 | GetGoldReserves |  | CFixedPoint | 类别：nonconst |
| 国家 | GetGoldReservesTrend |  | DataDynamicTrend | 类别：nonconst |
| 国家 | GetGoodsLeaderboardDesc |  | CString | 类别：nonconst |
| 国家 | GetGovernment |  | GovernmentType | 类别：nonconst |
| 国家 | GetGovernmentConstructionGoodsExpenses |  | CFixedPoint | 类别：nonconst |
| 国家 | GetGovernmentConstructionGoodsExpensesByGoodsDesc |  | CString | 类别：nonconst |
| 国家 | GetGovernmentGoodsExpenseTrend |  | DataTrend | 类别：nonconst |
| 国家 | GetGovernmentGoodsExpenses |  | CFixedPoint | 类别：nonconst |
| 国家 | GetGovernmentGoodsExpensesByGoodsDesc |  | CString | 类别：nonconst |
| 国家 | GetGovernmentGoodsExpensesDesc |  | CString | 类别：nonconst |
| 国家 | GetGovernmentIGsDesc |  | CString | 类别：nonconst |
| 国家 | GetGovernmentInterestGroupsDesc |  | CString | 类别：nonconst |
| 国家 | GetGovernmentInterestGroupsPopulationDesc |  | CString | 类别：nonconst |
| 国家 | GetGovernmentLegitimacy |  | int32 | 类别：nonconst |
| 国家 | GetGovernmentLegitimacyDesc |  | CString | 类别：nonconst |
| 国家 | GetGovernmentLegitimacyLevel |  | LegitimacyLevel | 类别：nonconst |
| 国家 | GetGovernmentSelfDebt |  | CFixedPoint | 类别：nonconst |
| 国家 | GetGovernmentSelfDebtFraction |  | CFixedPoint | 类别：nonconst |
| 国家 | GetGovernmentShareDividendsTrend |  | DataTrend | 类别：nonconst |
| 国家 | GetGovernmentShareLossesTrend |  | DataTrend | 类别：nonconst |
| 国家 | GetGovernmentSlavesExpenseTrend |  | DataTrend | 类别：nonconst |
| 国家 | GetGovernmentSlavesExpenses |  | CFixedPoint | 类别：nonconst |
| 国家 | GetGovernmentSlavesExpensesDesc |  | CString | 类别：nonconst |
| 国家 | GetGovernmentWageLevelDescHigh |  | CString | 类别：nonconst |
| 国家 | GetGovernmentWageLevelDescLow |  | CString | 类别：nonconst |
| 国家 | GetGovernmentWageLevelDescMedium |  | CString | 类别：nonconst |
| 国家 | GetGovernmentWageLevelDescVeryHigh |  | CString | Category: nonconst |
| 国家 | GetGovernmentWageLevelDescVeryLow |  | CString | Category: nonconst |
| 国家 | GetGovernmentWagesExpenseTrend |  | DataTrend | Category: nonconst |
| 国家 | GetGovernmentWagesExpenses |  | CFixedPoint | Category: nonconst |
| 国家 | GetGovernmentWagesExpensesDesc |  | CString | Category: nonconst |
| 国家 | GetGroupsForActiveJournalEntries |  | Unknown | Category: nonconst |
| 国家 | GetGroupsForInActiveJournalEntries |  | Unknown | Category: nonconst |
| 国家 | GetGrowingCivilWars |  | Unknown | Category: nonconst |
| 国家 | GetHeir |  | Character | Category: nonconst |
| 国家 | GetHighestPossibleRank |  | CString | Category: nonconst |
| 国家 | GetID |  | int32 | Category: nonconst |
| 国家 | GetIDString |  | CString | Category: nonconst |
| 国家 | GetIGApprovalFromLoyalistsBreakdown |  | CString | Category: nonconst |
| 国家 | GetIGApprovalFromRadicalsBreakdown |  | CString | Category: nonconst |
| 国家 | GetImportSubventionsDescHigh | Goods | CString | Category: nonconst |
| 国家 | GetImportSubventionsDescLow | Goods | CString | Category: nonconst |
| 国家 | GetImportSubventionsDescMax | Goods | CString | Category: nonconst |
| 国家 | GetImportTariffsDescHigh | Goods | CString | Category: nonconst |
| 国家 | GetImportTariffsDescLow | Goods | CString | Category: nonconst |
| 国家 | GetImportTariffsDescMax | Goods | CString | Category: nonconst |
| 国家 | GetImportTariffsDescNone | Goods | CString | Category: nonconst |
| 国家 | GetImportedAmount | Unknown | CFixedPoint | Category: nonconst |
| 国家 | GetImports |  | Unknown | Category: nonconst |
| 国家 | GetInDefaultEffectsDesc |  | CString | Category: nonconst |
| 国家 | GetInForceTreaties |  | Unknown | Category: nonconst |
| 国家 | GetInactiveConstructionProjectsDesc |  | CString | Category: nonconst |
| 国家 | GetInactivePopulation |  | int64 | Category: nonconst |
| 国家 | GetInactivePopulationDesc |  | CString | Category: nonconst |
| 国家 | GetIncomeBreakdown |  | CString | Category: nonconst |
| 国家 | GetIncomeTaxIncome |  | CFixedPoint | Category: nonconst |
| 国家 | GetIncorporatedLiteracyRanking |  | CString | Category: nonconst |
| 国家 | GetIncorporatedLiteracyRate |  | CFixedPoint | Category: nonconst |
| 国家 | GetIncorporatedLiteracyTrend |  | DataTrend | Category: nonconst |
| 国家 | GetIncorporatedPopulation |  | int64 | Category: nonconst |
| 国家 | GetIncorporatedStatesLawCostDesc |  | CString | Category: nonconst |
| 国家 | GetIndependentInterestGroupsInGovernment |  | Unknown | Category: nonconst |
| 国家 | GetIndependentInterestGroupsInOpposition |  | Unknown | Category: nonconst |
| 国家 | GetInfamy |  | CFixedPoint | Category: nonconst |
| 国家 | GetInfamyColor |  | CVector4f | Category: nonconst |
| 国家 | GetInfamyDesc |  | CString | Category: nonconst |
| 国家 | GetInfamyIconTexture |  | Unknown | Category: nonconst |
| 国家 | GetInfamyLabel |  | CString | Category: nonconst |
| 国家 | GetInstitutionInvestment |  | CFixedPoint | Category: nonconst |
| 国家 | GetInstitutionInvestmentBureaucracyCost |  | CFixedPoint | Category: nonconst |
| 国家 | GetInstitutionInvestmentBureaucracyCostDesc |  | CString | Category: nonconst |
| 国家 | GetInstitutionInvestmentBureaucracyFactor |  | CFixedPoint | Category: nonconst |
| 国家 | GetInstitutionInvestmentBureaucracyFactorDesc |  | CString | Category: nonconst |
| 国家 | GetInstitutionInvestmentDesc |  | CString | Category: nonconst |
| 国家 | GetInstitutionsSummary |  | CString | Category: nonconst |
| 国家 | GetInsurrectionaryIGsDesc |  | CString | Category: nonconst |
| 国家 | GetInterestExpenseTrend |  | DataTrend | Category: nonconst |
| 国家 | GetInterestGroupOfType | Unknown | InterestGroup | Category: nonconst |
| 国家 | GetInterestPayment |  | CFixedPoint | Category: nonconst |
| 国家 | GetInterestRateTooltip |  | CString | Category: nonconst |
| 国家 | GetInvestmentFundTrend |  | DataTrend | Category: nonconst |
| 国家 | GetInvestmentGdpFractionInCountry | 国家 | CFixedPoint | Category: nonconst |
| 国家 | GetInvestmentIncome |  | CFixedPoint | Category: nonconst |
| 国家 | GetInvestmentIncomeTrend |  | DataTrend | Category: nonconst |
| 国家 | GetInvestmentLevelsInCountry | 国家 | int32 | Category: nonconst |
| 国家 | GetInvestmentPool |  | CFixedPoint | Category: nonconst |
| 国家 | GetInvestmentPoolChange |  | CFixedPoint | Category: nonconst |
| 国家 | GetInvestmentPoolChangeFromConstructionDesc |  | CString | Category: nonconst |
| 国家 | GetInvestmentPoolChangeFromInvestmentBreakdown |  | CString | Category: nonconst |
| 国家 | GetInvestmentPoolChangeFromInvestmentDesc |  | CString | Category: nonconst |
| 国家 | GetInvestmentPoolPredictedNextBuildingDesc |  | CString | Category: nonconst |
| 国家 | GetJournalEntry | Unknown | JournalEntry | Category: nonconst |
| 国家 | GetKillRateNavy |  | CFixedPoint | Category: nonconst |
| 国家 | GetLabel | 国家 | CString | Category: nonconst |
| 国家 | GetLackOfAutonomousInvestmentReasonDesc |  | CString | Category: nonconst |
| 国家 | GetLastCatalystExpiryDate | 国家 DiplomaticCatalyst | CString | Category: nonconst |
| 国家 | GetLastElectionResultsTooltip |  | CString | Category: nonconst |
| 国家 | GetLawBeingEnacted |  | Law | Category: nonconst |
| 国家 | GetLawBeingEnactedFromGroup | Unknown | Law | Category: nonconst |
| 国家 | GetLawEnactmentProgress |  | CFixedPoint | Category: nonconst |
| 国家 | GetLawEnactmentProgressDesc |  | CString | Category: nonconst |
| 国家 | GetLeaderReligionPercentage |  | CFixedPoint | Category: nonconst |
| 国家 | GetLeverageAdvantage | PowerBloc | CFixedPoint | Category: nonconst |
| 国家 | GetLeverageAdvantageTarget | PowerBloc | CFixedPoint | Category: nonconst |
| 国家 | GetLeverageBreakdown |  | CString | Category: nonconst |
| 国家 | GetLeverageComparisonDesc | PowerBloc | CString | Category: nonconst |
| 国家 | GetLeverageGain | PowerBloc | CFixedPoint | Category: nonconst |
| 国家 | GetLeverageGainBreakdown | PowerBloc | CString | Category: nonconst |
| 国家 | GetLeverageResistance |  | CFixedPoint | Category: nonconst |
| 国家 | GetLeverageTarget | PowerBloc | CFixedPoint | Category: nonconst |
| 国家 | GetLeverageTooltip |  | CString | Category: nonconst |
| 国家 | GetLibertyDesireLevelLabel |  | CString | Category: nonconst |
| 国家 | GetLibertyDesireRaw |  | CFixedPoint | Category: nonconst |
| 国家 | GetLimitedMassMigrationCountryAttraction |  | CFixedPoint | Category: nonconst |
| 国家 | GetLobbyJournalEntries |  | Unknown | Category: nonconst |
| 国家 | GetLowerStrataPopulationTrend |  | DataTrend | Category: nonconst |
| 国家 | GetLoyalistsChangeSummary |  | CString | Category: nonconst |
| 国家 | GetLoyalistsDecreaseBreakdown |  | CString | Category: nonconst |
| 国家 | GetLoyalistsIncreaseBreakdown |  | CString | Category: nonconst |
| 国家 | GetLoyalistsOrRadicalsGainedFromLegitimacy |  | int64 | Category: nonconst |
| 国家 | GetLoyalistsOrRadicalsGainedFromLegitimacyModifierDescription | Unknown | CString | Category: nonconst |
| 国家 | GetLoyalistsSummaryDesc |  | CString | Category: nonconst |
| 国家 | GetLoyalistsTrend |  | DataTrend | Category: nonconst |
| 国家 | GetLoyaltiesGain |  | CFixedPoint | Category: nonconst |
| 国家 | GetMapColor |  | CVector4f | Category: nonconst |
| 国家 | GetMarginalAndInactivePopulationInCountryAsPercentage |  | float | Category: nonconst |
| 国家 | GetMarginalCloutInCountryAsPercentage |  | float | Category: nonconst |
| 国家 | GetMarginalInterestGroupsDesc |  | CString | Category: nonconst |
| 国家 | GetMarginalInterestGroupsPopulationDesc |  | CString | Category: nonconst |
| 国家 | GetMarket |  | Market | Category: nonconst |
| 国家 | GetMarketOwnerName |  | CString | Category: nonconst |
| 国家 | GetMassMigrationAttractionBreakdown |  | CString | Category: nonconst |
| 国家 | GetMassMigrationAttractionDesc |  | CString | Category: nonconst |
| 国家 | GetMaxCloutOrPopulationPercentage |  | float | Category: nonconst |
| 国家 | GetMaxCredit |  | CFixedPoint | Category: nonconst |
| 国家 | GetMaxFreeCharters |  | int32 | Category: nonconst |
| 国家 | GetMaxLawEnactmentSetbacks |  | int32 | Category: nonconst |
| 国家 | GetMaxNumCompanies |  | int32 | Category: nonconst |
| 国家 | GetMaxNumCompaniesDesc |  | CString | Category: nonconst |
| 国家 | GetMaxNumDeclaredInterestsBreakdown |  | CString | Category: nonconst |
| 国家 | GetMaxPowerStruggleMonth |  | int32 | Category: nonconst |
| 国家 | GetMaxWeeklyTechnologyProgressForTech | Unknown | CFixedPoint | Category: nonconst |
| 国家 | GetMaxWeeklyTechnologySpread |  | CFixedPoint | Category: nonconst |
| 国家 | GetMaxWeeklyTechnologySpreadForTech | Unknown | CFixedPoint | Category: nonconst |
| 国家 | GetMiddleStrataPopulationTrend |  | DataTrend | Category: nonconst |
| 国家 | GetMilitaryFormationsArmy |  | Unknown | Category: nonconst |
| 国家 | GetMilitaryFormationsFleet |  | Unknown | Category: nonconst |
| 国家 | GetMilitaryGoodsExpenseTrend |  | DataTrend | Category: nonconst |
| 国家 | GetMilitaryGoodsExpenses |  | CFixedPoint | Category: nonconst |
| 国家 | GetMilitaryGoodsExpensesByGoodsDesc |  | CString | Category: nonconst |
| 国家 | GetMilitaryGoodsExpensesDesc |  | CString | Category: nonconst |
| 国家 | GetMilitaryInterfaceColor |  | CVector4f | Category: nonconst |
| 国家 | GetMilitarySlavesExpenseTrend |  | DataTrend | Category: nonconst |
| 国家 | GetMilitarySlavesExpenses |  | CFixedPoint | Category: nonconst |
| 国家 | GetMilitarySlavesExpensesDesc |  | CString | Category: nonconst |
| 国家 | GetMilitaryWageLevelDescHigh |  | CString | Category: nonconst |
| 国家 | GetMilitaryWageLevelDescLow |  | CString | Category: nonconst |
| 国家 | GetMilitaryWageLevelDescMedium |  | CString | Category: nonconst |
| 国家 | GetMilitaryWageLevelDescVeryHigh |  | CString | Category: nonconst |
| 国家 | GetMilitaryWageLevelDescVeryLow |  | CString | Category: nonconst |
| 国家 | GetMilitaryWagesExpenseTrend |  | DataTrend | Category: nonconst |
| 国家 | GetMilitaryWagesExpenses |  | CFixedPoint | Category: nonconst |
| 国家 | GetMilitaryWagesExpensesDesc |  | CString | Category: nonconst |
| 国家 | GetMinWeeklyTechnologyProgressForTech | Technology | CFixedPoint | Category: nonconst |
| 国家 | GetMinWeeklyTechnologySpread |  | CFixedPoint | Category: nonconst |
| 国家 | GetMinWeeklyTechnologySpreadForTech | Unknown | CFixedPoint | Category: nonconst |
| 国家 | GetMintingTrend |  | DataTrend | Category: nonconst |
| 国家 | GetMobilizationRatio |  | CFixedPoint | Category: nonconst |
| 国家 | GetModifier |  | Modifier | Category: nonconst |
| 国家 | GetMoveCapitalEffectsDesc |  | CString | Category: nonconst |
| 国家 | GetMoveMarketCapitalEffectsDesc |  | CString | Category: nonconst |
| 国家 | GetName |  | CString | Category: nonconst |
| 国家 | GetNameNoFlag |  | CString | Category: nonconst |
| 国家 | GetNameNoFormatting |  | CString | Category: nonconst |
| 国家 | GetNavyPowerProjection |  | CFixedPoint | Category: nonconst |
| 国家 | GetNavyPowerProjectionDesc |  | CString | Category: nonconst |
| 国家 | GetNegotiatingInterestGroup |  | InterestGroup | Category: nonconst |
| 国家 | GetNextElectionDate |  | CString | Category: nonconst |
| 国家 | GetNextRank |  | CString | Category: nonconst |
| 国家 | GetNextRankDesc |  | CString | Category: nonconst |
| 国家 | GetNextRankNumber |  | int32 | Category: nonconst |
| 国家 | GetNextStartOfCampaignDate |  | CString | Category: nonconst |
| 国家 | GetNonPotentialDiploPlays |  | Unknown | Category: nonconst |
| 国家 | GetNonSubjectDiplomaticPactsWith | 国家 | Unknown | Category: nonconst |
| 国家 | GetNumActiveConstructionQueueElements |  | int32 | Category: nonconst |
| 国家 | GetNumActiveGovernmentConstructionQueueElements |  | int32 | Category: nonconst |
| 国家 | GetNumActivePrivateConstructionQueueElements |  | int32 | Category: nonconst |
| 国家 | GetNumActiveShownConstructionQueueElements |  | int32 | Category: nonconst |
| 国家 | GetNumActiveShownGovernmentConstructionQueueElements |  | int32 | Category: nonconst |
| 国家 | GetNumActiveShownPrivateConstructionQueueElements |  | int32 | Category: nonconst |
| 国家 | GetNumAvailableCompanies |  | int32 | Category: nonconst |
| 国家 | GetNumAvailableConvoys |  | int32 | Category: nonconst |
| 国家 | GetNumAvailableNegotiations |  | int32 | Category: nonconst |
| 国家 | GetNumBattalions |  | int32 | Category: nonconst |
| 国家 | GetNumBuildingsInConstructionQueueInState | State | int32 | Category: nonconst |
| 国家 | GetNumBuildingsUnderConstructionInState | State | int32 | Category: nonconst |
| 国家 | GetNumCombatUnits |  | int32 | Category: nonconst |
| 国家 | GetNumCompanies |  | int32 | Category: nonconst |
| 国家 | GetNumConvoys |  | int32 | Category: nonconst |
| 国家 | GetNumConvoysDamagedDesc |  | CString | Category: nonconst |
| 国家 | GetNumConvoysDesc |  | CString | Category: nonconst |
| 国家 | GetNumDamagedConvoys |  | int32 | Category: nonconst |
| 国家 | GetNumDeclaredInterests |  | int32 | Category: nonconst |
| 国家 | GetNumFlotillas |  | int32 | Category: nonconst |
| 国家 | GetNumGovernmentConstructionsInQueue |  | int32 | Category: nonconst |
| 国家 | GetNumInactiveAndNonShownGovernmentConstructionQueueElements |  | int32 | Category: nonconst |
| 国家 | GetNumInactiveAndNonShownPrivateConstructionQueueElements |  | int32 | Category: nonconst |
| 国家 | GetNumInactiveConstructionQueueElements |  | int32 | Category: nonconst |
| 国家 | GetNumInactiveGovernmentConstructionQueueElements |  | int32 | Category: nonconst |
| 国家 | GetNumInactivePrivateConstructionQueueElements |  | int32 | Category: nonconst |
| 国家 | GetNumIncorporatedLiteratePops |  | int64 | Category: nonconst |
| 国家 | GetNumIncorporatedStates |  | int32 | Category: nonconst |
| 国家 | GetNumIncorporatedStatesDesc |  | CString | Category: nonconst |
| 国家 | GetNumInsufficientTaxCapacityStates |  | int32 | Category: nonconst |
| 国家 | GetNumInterestGroupMembers |  | int64 | Category: nonconst |
| 国家 | GetNumIsolatedStates |  | int32 | Category: nonconst |
| 国家 | GetNumLowMarketAccessStates |  | int32 | Category: nonconst |
| 国家 | GetNumLoyalists |  | int64 | Category: nonconst |
| 国家 | GetNumNeutrals |  | int64 | Category: nonconst |
| 国家 | GetNumPoliticallyInactiveLoyalists |  | int64 | Category: nonconst |
| 国家 | GetNumPoliticallyInactiveNeutrals |  | int64 | Category: nonconst |
| 国家 | GetNumPoliticallyInactiveRadicals |  | int64 | Category: nonconst |
| 国家 | GetNumPrivateConstructionsInQueue |  | int32 | Category: nonconst |
| 国家 | GetNumRadicals |  | int64 | Category: nonconst |
| 国家 | GetNumStatesThatCanBeIncorporated |  | int32 | Category: nonconst |
| 国家 | GetNumStatesWithConstruction |  | int32 | Category: nonconst |
| 国家 | GetNumStatesWithoutConstruction |  | int32 | Category: nonconst |
| 国家 | GetNumTotalLiteratePops |  | int64 | Category: nonconst |
| 国家 | GetNumTurmoilStates |  | int32 | Category: nonconst |
| 国家 | GetNumUnincorporatedStates |  | int32 | Category: nonconst |
| 国家 | GetNumUnincorporatedStatesDesc |  | CString | Category: nonconst |
| 国家 | GetNumUsableConvoys |  | int32 | Category: nonconst |
| 国家 | GetNumberOfActiveConscriptionCenters |  | int32 | Category: nonconst |
| 国家 | GetNumberOfInactiveConscriptionCenters |  | int32 | Category: nonconst |
| 国家 | GetObjective |  | Objective | Category: nonconst |
| 国家 | GetObligationFromExpirationDate | 国家 | CString | Category: nonconst |
| 国家 | GetObligationFromExpirationDesc | 国家 | CString | Category: nonconst |
| 国家 | GetObligationToExpirationDate | 国家 | CString | Category: nonconst |
| 国家 | GetObligationToExpirationDesc | 国家 | CString | Category: nonconst |
| 国家 | GetObligationsOwedFrom |  | Unknown | Category: nonconst |
| 国家 | GetObligationsOwedTo |  | Unknown | Category: nonconst |
| 国家 | GetOppositionInterestGroupsDesc |  | CString | Category: nonconst |
| 国家 | GetOppositionInterestGroupsPopulationDesc |  | CString | Category: nonconst |
| 国家 | GetOtherPowerBlocWithHighestLeverage | Unknown | PowerBloc | Category: nonconst |
| 国家 | GetOverlord |  | Country | Category: nonconst |
| 国家 | GetOwningCompany |  | Company | Category: nonconst |
| 国家 | GetPartiesInGovernment |  | Unknown | Category: nonconst |
| 国家 | GetPartiesInOpposition |  | Unknown | Category: nonconst |
| 国家 | GetPeopleAbroad |  | int64 | Category: nonconst |
| 国家 | GetPlayedByDesc |  | CString | Category: nonconst |
| 国家 | GetPlayer |  | Player | Category: nonconst |
| 国家 | GetPoliticalLobbies |  | Unknown | Category: nonconst |
| 国家 | GetPoliticallyInvolvedPercentage |  | CFixedPoint | Category: nonconst |
| 国家 | GetPoliticallyInvolvedPopulation |  | int64 | Category: nonconst |
| 国家 | GetPoliticallyInvolvedPopulationDesc |  | CString | Category: nonconst |
| 国家 | GetPollTaxIncome |  | CFixedPoint | Category: nonconst |
| 国家 | GetPollTaxTrend |  | DataTrend | Category: nonconst |
| 国家 | GetPopConsumptionDependenceOn | Unknown | CString | Category: nonconst |
| 国家 | GetPopConsumptionDependenceOnDesc | Unknown | CString | Category: nonconst |
| 国家 | GetPopConsumptionDependenceOnRaw | Unknown | CFixedPoint | Category: nonconst |
| 国家 | GetPopGrowthDesc |  | CString | Category: nonconst |
| 国家 | GetPopReligions |  | Unknown | Category: nonconst |
| 国家 | GetPopulationRanking |  | CString | Category: nonconst |
| 国家 | GetPopulationTrend |  | DataTrend | Category: nonconst |
| 国家 | GetPotentialCompanies |  | Unknown | Category: nonconst |
| 国家 | GetPotentialDiploPlays |  | Unknown | Category: nonconst |
| 国家 | GetPotentialGeneralDiploActions |  | Unknown | Category: nonconst |
| 国家 | GetPotentialInvestors |  | Unknown | Category: nonconst |
| 国家 | GetPotentialLabor |  | int64 | Category: nonconst |
| 国家 | GetPotentialOverlordDiploActions |  | Unknown | Category: nonconst |
| 国家 | GetPotentialPowerBlocLeaderDiploActions |  | Unknown | Category: nonconst |
| 国家 | GetPotentialPowerBlocMemberDiploActions |  | Unknown | Category: nonconst |
| 国家 | GetPotentialSubjectDiploActions |  | Unknown | Category: nonconst |
| 国家 | GetPowerBloc |  | PowerBloc | Category: nonconst |
| 国家 | GetPowerBlocExpenseDesc |  | CString | Category: nonconst |
| 国家 | GetPowerBlocExpenseRaw |  | CFixedPoint | Category: nonconst |
| 国家 | GetPowerBlocExpenseTrend |  | DataTrend | Category: nonconst |
| 国家 | GetPowerBlocIncomeDesc |  | CString | Category: nonconst |
| 国家 | GetPowerBlocIncomeRaw |  | CFixedPoint | Category: nonconst |
| 国家 | GetPowerBlocIncomeTrend |  | DataTrend | Category: nonconst |
| 国家 | GetPowerBlocNonMemberCountryTooltip |  | CString | Category: nonconst |
| 国家 | GetPowerBlocWithHighestLeverage |  | PowerBloc | Category: nonconst |
| 国家 | GetPowerBlocsTotalLeverageShare |  | CFixedPoint | Category: nonconst |
| 国家 | GetPowerBlocsWithLeverage |  | Unknown | Category: nonconst |
| 国家 | GetPowerDelta | CString | CFixedPoint | Category: nonconst |
| 国家 | GetPowerDeltaIcon | CString | CString | Category: nonconst |
| 国家 | GetPowerExpensesString | CString | CString | Category: nonconst |
| 国家 | GetPowerIncome | CString | CFixedPoint | Category: nonconst |
| 国家 | GetPowerIncomeString | CString | CString | Category: nonconst |
| 国家 | GetPowerTooltip | CString | CString | Category: nonconst |
| 国家 | GetPredictedBalanceFromBankruptcy |  | CFixedPoint | Category: nonconst |
| 国家 | GetPrestige |  | int32 | Category: nonconst |
| 国家 | GetPrestigeDesc |  | CString | Category: nonconst |
| 国家 | GetPrestigeForCurrentRank |  | int32 | Category: nonconst |
| 国家 | GetPrestigeForNextRank |  | int32 | Category: nonconst |
| 国家 | GetPrestigeGoodsLeaderboardDesc |  | CString | Category: nonconst |
| 国家 | GetPrestigeToMaintainRank |  | int32 | Category: nonconst |
| 国家 | GetPrestigeTrend |  | DataTrend | Category: nonconst |
| 国家 | GetPreviousAttitudeTowards | Unknown | AIAttitude | Category: nonconst |
| 国家 | GetPreviousAutonomousInvestmentsDesc |  | CString | Category: nonconst |
| 国家 | GetPreviousRank |  | CString | Category: nonconst |
| 国家 | GetPriceReportDesc |  | CString | Category: nonconst |
| 国家 | GetPrimaryCulturesDesc |  | CString | Category: nonconst |
| 国家 | GetPrincipal |  | CFixedPoint | Category: nonconst |
| 国家 | GetPrivateConstructionGoodsExpenses |  | CFixedPoint | Category: nonconst |
| 国家 | GetPrivateConstructionGoodsExpensesByGoodsDesc |  | CString | Category: nonconst |
| 国家 | GetPrivateConstructionQueueDesc |  | CString | Category: nonconst |
| 国家 | GetRadicalizationFromBankruptcy |  | int64 | Category: nonconst |
| 国家 | GetRadicalsChangeSummary |  | CString | Category: nonconst |
| 国家 | GetRadicalsDecreaseBreakdown |  | CString | Category: nonconst |
| 国家 | GetRadicalsIncreaseBreakdown |  | CString | Category: nonconst |
| 国家 | GetRadicalsLoyalistsChangeStartDate |  | CString | Category: nonconst |
| 国家 | GetRadicalsSummaryDesc |  | CString | Category: nonconst |
| 国家 | GetRadicalsTrend |  | DataTrend | Category: nonconst |
| 国家 | GetRank |  | CString | Category: nonconst |
| 国家 | GetRankDesc |  | CString | Category: nonconst |
| 国家 | GetRankIconIndex |  | int32 | Category: nonconst |
| 国家 | GetRankModifier |  | Modifier | Category: nonconst |
| 国家 | GetRankNumber |  | int32 | Category: nonconst |
| 国家 | GetRankProgress |  | float | Category: nonconst |
| 国家 | GetRankTooltip |  | CString | Category: nonconst |
| 国家 | GetRecentPartiesDesc |  | CString | Category: nonconst |
| 国家 | GetRegularBattalions |  | int32 | Category: nonconst |
| 国家 | GetReinforcementRateArmy |  | CFixedPoint | Category: nonconst |
| 国家 | GetReinforcementRateNavy |  | CFixedPoint | Category: nonconst |
| 国家 | GetRelationsColor | Unknown | CVector4f | Category: nonconst |
| 国家 | GetRelationsIconTexture | 国家 | Unknown | Category: nonconst |
| 国家 | GetRelationsProgress | Unknown | CFixedPoint | Category: nonconst |
| 国家 | GetRelationsProgressDesc | Unknown | CString | Category: nonconst |
| 国家 | GetRelationsTooltip | 国家 | CString | Category: nonconst |
| 国家 | GetRelationsWith | 国家 | int32 | Category: nonconst |
| 国家 | GetRelationsWithDesc | 国家 | CString | Category: nonconst |
| 国家 | GetRelativePrestige | 国家 | CFixedPoint | Category: nonconst |
| 国家 | GetRemainingCredit |  | CFixedPoint | Category: nonconst |
| 国家 | GetRemainingDaysForFreeGovernmentReformRaw |  | int32 | Category: nonconst |
| 国家 | GetRequiredConvoys |  | int32 | Category: nonconst |
| 国家 | GetRequiredConvoysBreakdown |  | CString | Category: nonconst |
| 国家 | GetResearchQueueBottom |  | Unknown | Category: nonconst |
| 国家 | GetResearchQueueTop |  | Unknown | Category: nonconst |
| 国家 | GetRuler |  | Character | Category: nonconst |
| 国家 | GetRulingIGsDesc |  | CString | Category: nonconst |
| 国家 | GetSOLDescForAllStratas |  | CString | Category: nonconst |
| Country | GetSalariedWorkingAdults |  | int64 | 类别：nonconst |
| Country | GetSeaNodesMightBeConvoyRaidedInDesc |  | CString | 类别：nonconst |
| Country | GetSelectedLaw |  | Law | 类别：nonconst |
| Country | GetSocialHierarchy |  | SocialHierarchy | 类别：nonconst |
| Country | GetSpecialSocialHierarchy |  | SocialHierarchy | 类别：nonconst |
| Country | GetStandardOfLivingRanking |  | CString | 类别：nonconst |
| Country | GetStateOwnedBuildingsBureaucracyCostForLevels | int32 | CFixedPoint | 类别：nonconst |
| Country | GetStateReligion |  | Religion | 类别：nonconst |
| Country | GetStatesInTurmoilBreakdown |  | CString | 类别：nonconst |
| Country | GetStatus | Country | CString | 类别：nonconst |
| Country | GetStrategicObjectives |  | Unknown | 类别：nonconst |
| Country | GetStrategicRegions |  | Unknown | 类别：nonconst |
| Country | GetSubjectOrPowerBlocHierarchyLabel | Country | CString | 类别：nonconst |
| Country | GetSubjectPact |  | DiplomaticPact | 类别：nonconst |
| Country | GetSubjectType |  | SubjectType | 类别：nonconst |
| Country | GetSubjectTypeName |  | CString | 类别：nonconst |
| Country | GetSubjects |  | Unknown | 类别：nonconst |
| Country | GetSubjectsOfType | SubjectType | Unknown | 类别：nonconst |
| Country | GetSubsidiesExpenseTrend |  | DataTrend | 类别：nonconst |
| Country | GetSubsidiesExpenses |  | CFixedPoint | 类别：nonconst |
| Country | GetSubsidiesExpensesDesc |  | CString | 类别：nonconst |
| Country | GetSubsistingWorkingAdults |  | int64 | 类别：nonconst |
| Country | GetSubventionsExpenseTrend |  | DataTrend | 类别：nonconst |
| Country | GetSubventionsExpenses |  | CFixedPoint | 类别：nonconst |
| Country | GetSubventionsExpensesDesc |  | CString | 类别：nonconst |
| Country | GetSupplyNetworkNumSeaNodes |  | int32 | 类别：nonconst |
| Country | GetSupplyNetworkNumSeaNodesDesc |  | CString | 类别：nonconst |
| Country | GetSupplyNetworkStrength |  | CFixedPoint | 类别：nonconst |
| Country | GetSuppressionCostDesc |  | CString | 类别：nonconst |
| Country | GetSuppressionDesc |  | CString | 类别：nonconst |
| Country | GetTagName |  | CString | 类别：nonconst |
| Country | GetTargetLeverage | Unknown | CFixedPoint | 类别：nonconst |
| Country | GetTargetLeverageShare | PowerBloc | CFixedPoint | 类别：nonconst |
| Country | GetTargetRank |  | CString | 类别：nonconst |
| Country | GetTariffTrend |  | DataTrend | 类别：nonconst |
| Country | GetTaxIncomeFor | Unknown | CFixedPoint | 类别：nonconst |
| Country | GetTaxIncomeTrend |  | DataTrend | 类别：nonconst |
| Country | GetTaxLevelDescHigh |  | CString | 类别：nonconst |
| Country | GetTaxLevelDescLow |  | CString | 类别：nonconst |
| Country | GetTaxLevelDescMedium |  | CString | 类别：nonconst |
| Country | GetTaxLevelDescVeryHigh |  | CString | 类别：nonconst |
| Country | GetTaxLevelDescVeryLow |  | CString | 类别：nonconst |
| Country | GetTensionIconTexture | Country | Unknown | 类别：nonconst |
| Country | GetTensionTooltip | Country | CString | 类别：nonconst |
| Country | GetTensionWith | Country | int32 | 类别：nonconst |
| Country | GetTensionWithDesc | Country | CString | 类别：nonconst |
| Country | GetTimeUntilTargetReachedArmy |  | CString | 类别：nonconst |
| Country | GetTimeUntilTargetReachedNavy |  | CString | 类别：nonconst |
| Country | GetTimedModifierDurationRemaining | Modifier | CString | 类别：nonconst |
| Country | GetTimedModifiers |  | Unknown | 类别：nonconst |
| Country | GetTooltipTag |  | CString | 类别：nonconst |
| Country | GetTopOverlord |  | Country | 类别：nonconst |
| Country | GetTotalAgitatorSlots |  | int32 | 类别：nonconst |
| Country | GetTotalExpensesTrend |  | DataTrend | 类别：nonconst |
| Country | GetTotalExportedAmount |  | CFixedPoint | 类别：nonconst |
| Country | GetTotalForeignConstructions |  | int32 | 类别：nonconst |
| Country | GetTotalGovernmentClout |  | CFixedPoint | 类别：nonconst |
| Country | GetTotalImportedAmount |  | CFixedPoint | 类别：nonconst |
| Country | GetTotalIncomeTrend |  | DataTrend | 类别：nonconst |
| Country | GetTotalLeverageFactors |  | CFixedPoint | 类别：nonconst |
| Country | GetTotalLeverageFactorsBreakdown |  | CString | 类别：nonconst |
| Country | GetTotalLeverageFactorsWithResistance |  | CFixedPoint | 类别：nonconst |
| Country | GetTotalLeverageFactorsWithResistanceBreakdown |  | CString | 类别：nonconst |
| Country | GetTotalLiteracyRanking |  | CString | 类别：nonconst |
| Country | GetTotalLiteracyRate |  | CFixedPoint | 类别：nonconst |
| Country | GetTotalMarginalClout |  | CFixedPoint | 类别：nonconst |
| Country | GetTotalNumLoyalistsChange |  | int64 | 类别：nonconst |
| Country | GetTotalNumLoyalistsDecrease |  | int64 | 类别：nonconst |
| Country | GetTotalNumLoyalistsIncrease |  | int64 | 类别：nonconst |
| Country | GetTotalNumRadicalsChange |  | int64 | 类别：nonconst |
| Country | GetTotalNumRadicalsDecrease |  | int64 | 类别：nonconst |
| Country | GetTotalNumRadicalsIncrease |  | int64 | 类别：nonconst |
| Country | GetTotalOppositionClout |  | CFixedPoint | 类别：nonconst |
| Country | GetTotalPopulation |  | int64 | 类别：nonconst |
| Country | GetTotalUrbanization |  | int32 | 类别：nonconst |
| Country | GetTreatiesBrokenFromNeutralityDesc | DiplomaticPlay | CString | 类别：nonconst |
| Country | GetTreatiesExpenseTrend |  | DataTrend | 类别：nonconst |
| Country | GetTreatiesIncomeTrend |  | DataTrend | 类别：nonconst |
| Country | GetTreatiesWith | Country | Unknown | 类别：nonconst |
| Country | GetTreatiesWithDesc | Country | CString | 类别：nonconst |
| Country | GetTruceDate | Country | CString | 类别：nonconst |
| Country | GetUnclaimedLeverage |  | CFixedPoint | 类别：nonconst |
| Country | GetUnclaimedLeverageFormatted |  | CString | 类别：nonconst |
| Country | GetUnclaimedLeverageShare |  | CFixedPoint | 类别：nonconst |
| Country | GetUnclaimedLeverageShareTarget |  | CFixedPoint | 类别：nonconst |
| Country | GetUnclaimedLeverageTarget |  | CFixedPoint | 类别：nonconst |
| Country | GetUnemployedWorkingAdults |  | int64 | 类别：nonconst |
| Country | GetUnenforcedTreaties |  | Unknown | 类别：nonconst |
| Country | GetUnenforcedTreatiesWith | Country | Unknown | 类别：nonconst |
| Country | GetUnenforcedTreatiesWithDesc | Unknown | CString | 类别：nonconst |
| Country | GetUnrealizedTaxes |  | CFixedPoint | 类别：nonconst |
| Country | GetUpperStrataPopulationTrend |  | DataTrend | 类别：nonconst |
| Country | GetUsedAgitatorSlots |  | int32 | 类别：nonconst |
| Country | GetUsedFreeCharters |  | int32 | 类别：nonconst |
| Country | GetWarships |  | int32 | 类别：nonconst |
| Country | GetWeeklyBalance |  | CFixedPoint | 类别：nonconst |
| Country | GetWeeklyCostArmy |  | CFixedPoint | 类别：nonconst |
| Country | GetWeeklyCostNavy |  | CFixedPoint | 类别：nonconst |
| Country | GetWeeklyExpenses |  | CFixedPoint | 类别：nonconst |
| Country | GetWeeklyFixedExpenses |  | CFixedPoint | 类别：nonconst |
| Country | GetWeeklyGDP |  | CFixedPoint | 类别：nonconst |
| Country | GetWeeklyIncome |  | CFixedPoint | 类别：nonconst |
| Country | GetWeeklyInnovation |  | CFixedPoint | 类别：nonconst |
| Country | GetWeeklyInnovationDesc |  | CString | 类别：nonconst |
| Country | GetWeeklyInterestRate |  | CFixedPoint | 类别：nonconst |
| Country | GetWeeklyLeverageGain | PowerBloc | CFixedPoint | 类别：nonconst |
| Country | GetWeeklyLibertyDesireChange |  | CFixedPoint | 类别：nonconst |
| Country | GetWeeklyLibertyDesireChangeDesc |  | CString | 类别：nonconst |
| Country | GetWeeklyLibertyDesireChangeFromSupportIndependence |  | CFixedPoint | 类别：nonconst |
| Country | GetWeeklyLibertyDesireChangeFromSupportIndependenceDesc |  | CString | 类别：nonconst |
| Country | GetWeeklyMaxInnovation |  | CFixedPoint | 类别：nonconst |
| Country | GetWeeklyMaxInnovationDesc |  | CString | 类别：nonconst |
| Country | GetWeeklyRawInnovation |  | CFixedPoint | 类别：nonconst |
| Country | GetWeeklyResearchSpeed |  | CFixedPoint | 类别：nonconst |
| Country | GetWeeklyResearchSpeedDesc |  | CString | 类别：nonconst |
| Country | GetWeeklyTechnologyProgressDescForTech | Technology | CString | 类别：nonconst |
| Country | GetWeeklyTechnologySpreadBreakdown |  | CString | 类别：nonconst |
| Country | GetWeeklyTechnologySpreadDesc |  | CString | 类别：nonconst |
| Country | GetWeeklyTechnologySpreadForTechDesc | Technology | CString | 类别：nonconst |
| Country | GetWeeklyTemporaryExpenses |  | CFixedPoint | 类别：nonconst |
| Country | GetWeeklyTemporaryIncome |  | CFixedPoint | 类别：nonconst |
| Country | GetWelfarePaymentsExpenses |  | CFixedPoint | 类别：nonconst |
| Country | GetWelfarePaymentsTrend |  | DataTrend | 类别：nonconst |
| Country | GetWorkingAdults |  | int64 | 类别：nonconst |
| Country | GetYearlyInterestRate |  | CFixedPoint | 类别：nonconst |
| Country | GetYouOrCountryName |  | CString | 类别：nonconst |
| Country | GetZeroBalancePlotPoints |  | Unknown | 类别：nonconst |
| Country | GetZeroMoneyPlotPoints |  | Unknown | 类别：nonconst |
| Country | HasActiveDiplomacy |  | bool |  |
| Country | HasAnyAllianceLikeTreatiesWith | Unknown | bool |  |
| Country | HasAnySlavery |  | bool |  |
| Country | HasAnyTaxes |  | bool |  |
| Country | HasConstructionQueued |  | bool |  |
| Country | HasCurrentlyResearchedTechnology |  | bool |  |
| Country | HasDamagedConvoys |  | bool |  |
| Country | HasDeclaredInterest | Unknown | bool |  |
| Country | HasDecreasingInterests |  | bool |  |
| Country | HasDiplomaticPactWith | Unknown Unknown | bool |  |
| Country | HasElectionTrendData |  | bool |  |
| Country | HasElections |  | bool |  |
| Country | HasExportSubventionsHigh | Goods | bool |  |
| Country | HasExportSubventionsLow | Goods | bool |  |
| Country | HasExportSubventionsMax | Goods | bool |  |
| Country | HasExportTariffsHigh | Goods | bool |  |
| Country | HasExportTariffsLow | Goods | bool |  |
| Country | HasExportTariffsMax | Goods | bool |  |
| Country | HasExportTariffsNone | Goods | bool |  |
| Country | HasForeignInvestmentRights | Country | bool |  |
| Country | HasGovernmentWages |  | bool |  |
| Country | HasHeir |  | bool |  |
| Country | HasHigherUnclaimedLeverage |  | bool |  |
| Country | HasHigherUnclaimedLeverageTarget |  | bool |  |
| Country | HasIGApprovalFromLoyalists |  | bool |  |
| Country | HasIGApprovalFromRadicals |  | bool |  |
| Country | HasImportSubventionsHigh | Goods | bool |  |
| Country | HasImportSubventionsLow | Goods | bool |  |
| Country | HasImportSubventionsMax | Goods | bool |  |
| Country | HasImportTariffsHigh | Goods | bool |  |
| Country | HasImportTariffsLow | Goods | bool |  |
| Country | HasImportTariffsMax | Goods | bool |  |
| Country | HasImportTariffsNone | Goods | bool |  |
| Country | HasInterestIn | StrategicRegion | bool |  |
| Country | HasMilitaryWages |  | bool |  |
| Country | HasNewProductionMethodInGroup | ProductionMethodGroup | bool |  |
| Country | HasNewProductionMethodInSameGroup | BuildingType ProductionMethod | bool |  |
| Country | HasObjective |  | bool |  |
| Country | HasOverlappingInterestsWith | Unknown | bool |  |
| Country | HasOwningCompany |  | bool |  |
| Country | HasProgressingLawEnactment |  | bool |  |
| Country | HasRuler |  | bool |  |
| Country | HasSelectedLaw |  | bool |  |
| Country | HasSpecialSocialHierarchy |  | bool |  |
| Country | InDefault |  | bool |  |
| Country | IsAI |  | bool |  |
| Country | IsAIOrOtherPlayer |  | bool |  |
| Country | IsAlliedInDiploPlayWith | Country | bool |  |
| Country | IsAnySubjectOf | Unknown | bool |  |
| Country | IsAtWar |  | bool |  |
| Country | IsAtWarWith | Country | bool |  |
| Country | IsBeingHighlighted |  | bool |  |
| Country | IsBeingTutorialHighlighted |  | bool |  |
| Country | IsColonizable |  | bool |  |
| Country | IsCommittedInDiplomaticPlay |  | bool |  |
| Country | IsConscripting |  | bool |  |
| Country | IsConstructionPaused |  | bool |  |
| Country | IsDead |  | bool |  |
| Country | IsDiplomaticallyRelevantCountry | Unknown | bool |  |
| Country | IsEconomyHealthy |  | bool |  |
| Country | IsEconomyHealthyDesc |  | CString |  |
| Country | IsEnactingLaw |  | bool |  |
| Country | IsHighestRank |  | bool |  |
| Country | IsIgnoringCountryFormation | CountryFormation | bool |  |
| Country | IsIgnoringDecision | Decision | bool |  |
| Country | IsInElectionCampaignPeriod |  | bool |  |
| Country | IsInPowerBloc |  | bool |  |
| Country | IsInsurrectionary |  | bool |  |
| Country | IsInvolvedInActiveConflict |  | bool |  |
| Country | IsLocalPlayer |  | bool |  |
| Country | IsLowestRank |  | bool |  |
| Country | IsMobilized |  | bool |  |
| Country | IsNegotiating |  | bool |  |
| Country | IsNeighborsWith | Unknown | bool |  |
| Country | IsNewProductionMethod | ProductionMethod | bool |  |
| Country | IsObjectiveIdle |  | bool |  |
| Country | IsOtherPlayer |  | bool |  |
| Country | IsPinnedInOutliner |  | bool |  |
| Country | IsPlayer |  | bool |  |
| Country | IsPowerBlocLeader |  | bool |  |
| Country | IsPowerStruggling |  | bool |  |
| Country | IsRank | Unknown | bool |  |
| Country | IsRevolutionary |  | bool |  |
| Country | IsSecessionist |  | bool |  |
| Country | IsSubject |  | bool |  |
| Country | IsSubjectOf | Country | bool |  |
| Country | IsTaxingAnyGood |  | bool |  |
| Country | IsValid |  | bool |  |
| Country | LeavePowerBloc |  | Command |  |
| Country | MakeScope |  | Scope |  |
| Country | MobilizeAllArmies |  | Command |  |
| Country | OwesObligationTo | Unknown | bool |  |
| Country | PauseConstruction |  | Command |  |
| Country | PauseConstructionTooltip |  | CString |  |
| Country | PredictBalanceWithoutTemporaryIncomeAndExpenses |  | CFixedPoint |  |
| Country | PredictConsumptionTaxes |  | CFixedPoint |  |
| Country | PredictDiplomaticPactsExpenses |  | CFixedPoint |  |
| Country | PredictDiplomaticPactsExpensesDesc |  | CString |  |
| Country | PredictDiplomaticPactsIncome |  | CFixedPoint |  |
| Country | PredictDiplomaticPactsIncomeDesc |  | CString |  |
| Country | PredictDividendsTaxes |  | CFixedPoint |  |
| Country | PredictDividendsTaxesDesc |  | CString |  |
| Country | PredictEconomyHealthDesc |  | CString |  |
| Country | PredictGovernmentShareDividends |  | CFixedPoint |  |
| Country | PredictGovernmentShareDividendsDesc |  | CString |  |
| Country | PredictGovernmentShareLosses |  | CFixedPoint |  |
| Country | PredictGovernmentShareLossesDesc |  | CString |  |
| Country | PredictGovernmentWagesExpenses |  | CFixedPoint |  |
| Country | PredictMaxWeeklyTechnologyProgressForTech | Unknown | CFixedPoint |  |
| Country | PredictMilitaryWagesExpenses |  | CFixedPoint |  |
| Country | PredictMinWeeklyTechnologyProgressForTech | Unknown | CFixedPoint |  |
| Country | PredictMinting |  | CFixedPoint |  |
| Country | PredictMintingDesc |  | CString |  |
| Country | PredictTariffs |  | CFixedPoint |  |
| Country | PredictTariffsDesc |  | CString |  |
| Country | PredictTotalMilitaryExpenses |  | CFixedPoint |  |
| Country | PredictTreatyExpenses |  | CFixedPoint |  |
| Country | PredictTreatyExpensesDesc |  | CString |  |
| Country | PredictTreatyIncome |  | CFixedPoint |  |
| Country | PredictTreatyIncomeDesc |  | CString |  |
| Country | PredictWeeklyBalance |  | CFixedPoint |  |
| Country | PredictWeeklyBalanceWithEconomyHealthHint |  | CString |  |
| Country | PredictWeeklyFixedIncome |  | CFixedPoint |  |
| Country | PredictWeeklyIncome |  | CFixedPoint |  |
| Country | RemoveCompany | CompanyType | Command |  |
| Country | ResumeConstruction |  | Command |  |
| Country | ResumeConstructionTooltip |  | CString |  |
| Country | Self |  | Country |  |
| Country | SetExportSubventionsHigh | Goods | Command |  |
| Country | SetExportSubventionsLow | Goods | Command |  |
| Country | SetExportSubventionsMax | Goods | Command |  |
| Country | SetExportTariffsHigh | Goods | Command |  |
| Country | SetExportTariffsLow | Goods | Command |  |
| Country | SetExportTariffsMax | Goods | Command |  |
| Country | SetExportTariffsNone | Goods | Command |  |
| Country | SetGovernmentWageLevelHigh |  | Command |  |
| Country | SetGovernmentWageLevelLow |  | Command |  |
| Country | SetGovernmentWageLevelMedium |  | Command |  |
| Country | SetGovernmentWageLevelVeryHigh |  | Command |  |
| Country | SetGovernmentWageLevelVeryLow |  | Command |  |
| Country | SetImportSubventionsHigh | Goods | Command |  |
| Country | SetImportSubventionsLow | Goods | Command |  |
| Country | SetImportSubventionsMax | Goods | Command |  |
| Country | SetImportTariffsHigh | Goods | Command |  |
| Country | SetImportTariffsLow | Goods | Command |  |
| Country | SetImportTariffsMax | Goods | Command |  |
| Country | SetImportTariffsNone | Goods | Command |  |
| Country | SetMilitaryWageLevelHigh |  | Command |  |
| Country | SetMilitaryWageLevelLow |  | Command |  |
| Country | SetMilitaryWageLevelMedium |  | Command |  |
| Country | SetMilitaryWageLevelVeryHigh |  | Command |  |
| Country | SetMilitaryWageLevelVeryLow |  | Command |  |
| Country | SetTaxLevelHigh |  | Command |  |
| Country | SetTaxLevelLow |  | Command |  |
| Country | SetTaxLevelMedium |  | Command |  |
| Country | SetTaxLevelVeryHigh |  | Command |  |
| Country | SetTaxLevelVeryLow |  | Command |  |
| Country | ShowInvestmentPoolPredictedNextBuilding |  | bool |  |
| Country | SortCompanies | Unknown | void |  |
| Country | SortCultures | CString | void |  |
| Country | SortReligions | CString | void |  |
| Country | SortStates | Unknown | void |  |
| Country | SortSubjects | CString | void |  |
| Country | StartNegotiationWith | InterestGroup | Command |  |
| Country | ToggleIgnoreCountryFormation | CountryFormation | Command |  |
| Country | ToggleIgnoreDecision | Decision | Command |  |
| Country | TogglePinInOutliner |  | void |  |
| Country | TryGetOverlordTooltipEntry |  | CString |  |
| Country | TryGetSubjectsTooltipEntry |  | CString |  |
| CountryCreation | AccessSelf |  | CountryCreation | 类别：const |
| CountryCreation | CanReleaseCountry | Country | bool |  |
| CountryCreation | CanReleaseCountryAs | Unknown Unknown | bool |  |
| CountryCreation | GetAdjective |  | CString | 类别：nonconst |
| CountryCreation | GetCapital |  | StateRegion | 类别：nonconst |
| CountryCreation | GetCustom | CustomLocalization | CString | 类别：nonconst |
| CountryCreation | GetDefinition |  | CountryDefinition | 类别：nonconst |
| CountryCreation | GetName |  | CString | 类别：nonconst |
| CountryCreation | GetNumControlledStates | Unknown | int32 | 类别：nonconst |
| CountryCreation | GetNumProvincesToRelease |  | int32 | 类别：nonconst |
| CountryCreation | GetNumReleasableStates | Country | int32 | 类别：nonconst |
| CountryCreation | GetNumRequiredStates |  | int32 | 类别：nonconst |
| CountryCreation | GetReleaseDesc | Country | CString | 类别：nonconst |
| CountryCreation | GetTooltipTag |  | CString | 类别：nonconst |
| CountryCreation | GetTotalNumStates |  | int32 | 类别：nonconst |
| CountryCreation | IsReleasedInSpecificProvinces |  | bool |  |
| CountryCreation | IsValid |  | bool |  |
| CountryCreation | ListCultures |  | CString |  |
| CountryCreation | ListPotentialReleasableStates | Country | CString |  |
| CountryCreation | ListPotentialStates | Country | CString |  |
| CountryCreation | ListReleasableStates | Country | CString |  |
| CountryCreation | ListReleasableStatesWithoutHomeland | Country | CString |  |
| CountryCreation | MakeScope |  | Scope |  |
| CountryCreation | Self |  | CountryCreation |  |
| CountryCreation | ShowRequiredNumStates | Country | bool |  |
| CountryDefinition | AccessSelf |  | CountryDefinition | 类别：const |
| CountryDefinition | GetAdjective |  | CString | 类别：nonconst |
| CountryDefinition | GetBaseFlag |  | CoatOfArms | 类别：nonconst |
| CountryDefinition | GetColor |  | CVector4f | 类别：nonconst |
| CountryDefinition | GetCustom | CustomLocalization | CString | 类别：nonconst |
| CountryDefinition | GetFlag | CString | CoatOfArms | 类别：nonconst |
| CountryDefinition | GetName |  | CString | 类别：nonconst |
| CountryDefinition | GetPrimaryCulture |  | Culture | 类别：nonconst |
| CountryDefinition | GetPrimaryCultureName |  | CString | 类别：nonconst |
| CountryDefinition | GetTier |  | CString | 类别：nonconst |
| CountryDefinition | GetTooltipTag |  | CString | 类别：nonconst |
| CountryDefinition | IsValid |  | bool |  |
| CountryDefinition | MakeScope |  | Scope |  |
| CountryDefinition | Self |  | CountryDefinition |  |
| CountryEntry | AccessSelf |  | CountryEntry | 类别：const |
| CountryEntry | GetCountry |  | CUTF8String | 类别：nonconst |
| CountryEntry | Self |  | CountryEntry |  |
| CountryFormation | AccessFormationCandidates |  | Unknown | 类别：const |
| CountryFormation | AccessFormationCultureCountries |  | Unknown | 类别：const |
| CountryFormation | AccessFormationStateRegions |  | Unknown | 类别：const |
| CountryFormation | AccessSelf |  | CountryFormation | 类别：const |
| CountryFormation | CanFormCountry | Unknown | bool |  |
| CountryFormation | CanLaunchLeadershipPlay | Country | bool |  |
| CountryFormation | CanLaunchUnificationPlay |  | bool |  |
| CountryFormation | ControlsStateRegion | Country StateRegion | bool |  |
| CountryFormation | FormCountry | Country | Command |  |
| CountryFormation | GetAdjective |  | CString | 类别：nonconst |
| CountryFormation | GetControlsStateRegionDesc | Country StateRegion | CString | 类别：nonconst |
| CountryFormation | GetCustom | CustomLocalization | CString | 类别：nonconst |
| CountryFormation | GetDefinition |  | CountryDefinition | 类别：nonconst |
| CountryFormation | GetFormDesc | Country | CString | 类别：nonconst |
| CountryFormation | GetName |  | CString | 类别：nonconst |
| CountryFormation | GetNumControlledStates | Country | int32 | 类别：nonconst |
| CountryFormation | GetNumRequiredStates |  | int32 | 类别：nonconst |
| CountryFormation | GetNumSupportingCountries | Country | int32 | 类别：nonconst |
| CountryFormation | GetSupportCandidateDesc | Country Country | CString | 类别：nonconst |
| CountryFormation | GetSupportForAllCandidatesDesc | Country | CString | 类别：nonconst |
| CountryFormation | GetSupportForCandidateBreakdown | Unknown Unknown | CString | 类别：nonconst |
| CountryFormation | GetSupportedCandidateCountry | Unknown | Country | 类别：nonconst |
| CountryFormation | GetSupportingCountriesDesc | Country | CString | 类别：nonconst |
| CountryFormation | GetTooltipTag |  | CString | 类别：nonconst |
| CountryFormation | GetTotalNumStates |  | int32 | 类别：nonconst |
| CountryFormation | GetTriggerLeadershipPlayDesc | Country Country | CString | 类别：nonconst |
| CountryFormation | GetTriggerUnificationPlayDesc | Country | CString | 类别：nonconst |
| CountryFormation | IsCandidateForFormation | Unknown | bool |  |
| CountryFormation | IsMajorFormation |  | bool |  |
| CountryFormation | IsSupportingAnyCandidate | Unknown | bool |  |
| CountryFormation | IsSupportingCandidate | Unknown Unknown | bool |  |
| CountryFormation | ListCultures |  | CString |  |
| CountryFormation | ListRequiredStates | Country | CString |  |
| CountryFormation | MakeScope |  | Scope |  |
| CountryFormation | Self |  | CountryFormation |  |
| CountryFormation | ShowLeadershipPlayConfirmation | Unknown | void |  |
| CountryFormation | ShowUnificationPlayConfirmation |  | void |  |
| CountryFormation | SupportCandidate | Unknown Unknown | Command |  |
| CountryFormationPanel | AccessCountryFormation |  | CountryFormation | 类别：const |
| CountryFormationPanel | AccessSelf |  | CountryFormationPanel | 类别：const |
| CountryFormationPanel | GetCountryFormation |  | CountryFormation | 类别：nonconst |
| CountryFormationPanel | Self |  | CountryFormationPanel |  |
| CountryMarker | AccessSelf |  | CountryMarker | 类别：const |
| CountryMarker | Self |  | CountryMarker |  |
| CountryPanel | AccessSelf |  | CountryPanel | 类别：const |
| CountryPanel | Self |  | CountryPanel |  |
| CountryTrendPair | AccessSelf |  | CountryTrendPair | 类别：const |
| CountryTrendPair | GetCountry |  | Country | 类别：nonconst |
| CountryTrendPair | GetTrend |  | DataTrend | 类别：nonconst |
| CountryTrendPair | Self |  | CountryTrendPair |  |
| CreateAccount | AccessSelf |  | CreateAccount | 类别：const |
| CreateAccount | CanCreateAccount |  | bool |  |
| CreateAccount | CreateAccount |  | void |  |
| CreateAccount | GetCountries |  | Unknown | 类别：nonconst |
| CreateAccount | GetDays |  | Unknown | 类别：nonconst |
| CreateAccount | GetEmail |  | CUTF8String | 类别：nonconst |
| CreateAccount | GetErrorMessage |  | CUTF8String | 类别：nonconst |
| CreateAccount | GetMonths |  | Unknown | 类别：nonconst |
| CreateAccount | GetOptedIntoMarketingChecked |  | bool | 类别：nonconst |
| CreateAccount | GetPassword |  | CUTF8String | 类别：nonconst |
| CreateAccount | GetSelectedCountryIndex |  | CVector2i | 类别：nonconst |
| CreateAccount | GetSelectedDayIndex |  | CVector2i | 类别：nonconst |
| CreateAccount | GetSelectedMonthIndex |  | CVector2i | 类别：nonconst |
| CreateAccount | GetSelectedYearIndex |  | CVector2i | 类别：nonconst |
| CreateAccount | GetYears |  | Unknown | 类别：nonconst |
| CreateAccount | Hide |  | void |  |
| CreateAccount | IsCreatingAccount |  | bool |  |
| CreateAccount | OnCountryChanged |  | void |  |
| CreateAccount | OnDayChanged |  | void |  |
| CreateAccount | OnMonthChanged |  | void |  |
| CreateAccount | OnOptedIntoMarketingToggled |  | void |  |
| CreateAccount | OnYearChanged |  | void |  |
| CreateAccount | Self |  | CreateAccount |  |
| CreateAccount | SetEmail |  | void |  |
| CreateAccount | SetPassword |  | void |  |
| CreateAccount | Show |  | void |  |
| CreateSocialProfileWindow | AccessSelf |  | CreateSocialProfileWindow | 类别：const |
| CreateSocialProfileWindow | Create |  | void |  |
| CreateSocialProfileWindow | GetErrorMessage |  | CString | 类别：nonconst |
| CreateSocialProfileWindow | GetName |  | CString | 类别：nonconst |
| CreateSocialProfileWindow | Hide |  | void |  |
| CreateSocialProfileWindow | IsCreatingProfile |  | bool |  |
| CreateSocialProfileWindow | IsValidName |  | bool |  |
| CreateSocialProfileWindow | Self |  | CreateSocialProfileWindow |  |
| CreateSocialProfileWindow | SetName |  | void |  |
| CreateSocialProfileWindow | ShouldBeShown |  | bool |  |
| CreateSocialProfileWindow | Show |  | void |  |
| CreditsWindow | AccessSelf |  | CreditsWindow | 类别：const |
| CreditsWindow | GetCredits |  | CUTF8String | 类别：nonconst |
| CreditsWindow | HasReachedEnd |  | bool |  |
| CreditsWindow | IsFastest |  | bool |  |
| CreditsWindow | IsPaused |  | bool |  |
| CreditsWindow | IsSlowest |  | bool |  |
| CreditsWindow | OnClose |  | void |  |
| CreditsWindow | OnFaster |  | void |  |
| CreditsWindow | OnSlower |  | void |  |
| CreditsWindow | OnTogglePause |  | void |  |
| CreditsWindow | Self |  | CreditsWindow |  |
| CulturalCommunity | AccessSelf |  | CulturalCommunity | 类别：const |
| CulturalCommunity | GetCulture |  | Culture | 类别：nonconst |
| CulturalCommunity | GetCustom | CustomLocalization | CString | 类别：nonconst |
| CulturalCommunity | GetID |  | uint32 | 类别：nonconst |
| CulturalCommunity | GetLocalAcceptanceDifference |  | CFixedPoint | 类别：nonconst |
| CulturalCommunity | GetLocalAcceptanceDifferenceDesc |  | CString | 类别：nonconst |
| CulturalCommunity | GetName |  | CString | 类别：nonconst |
| CulturalCommunity | GetState |  | State | 类别：nonconst |
| CulturalCommunity | GetTooltipTag |  | CString | 类别：nonconst |
| CulturalCommunity | IsValid |  | bool |  |
| CulturalCommunity | MakeScope |  | Scope |  |
| CulturalCommunity | Self |  | CulturalCommunity |  |
| Culture | AccessHomelands |  | Unknown | 类别：const |
| Culture | AccessReligion |  | Religion | 类别：const |
| Culture | AccessSameHeritageCultures |  | Unknown | 类别：const |
| Culture | AccessSelf |  | Culture | 类别：const |
| Culture | CalcAvgSoL |  | CFixedPoint |  |
| Culture | CalcAvgSoLForMiddle |  | CFixedPoint |  |
| Culture | CalcAvgSoLForPoor |  | CFixedPoint |  |
| Culture | CalcAvgSoLForRich |  | CFixedPoint |  |
| Culture | CalcTurmoilInCountry | Unknown | CFixedPoint |  |
| Culture | GetAcceptanceDescIn | Country | CString | 类别：nonconst |
| Culture | GetAcceptanceIn | Country | int32 | 类别：nonconst |
| Culture | GetAllAcceptanceStatusSegments | Country | Unknown | 类别：nonconst |
| Culture | GetCasualtiesFromWars |  | int64 | 类别：nonconst |
| Culture | GetColor |  | CVector4f | 类别：nonconst |
| Culture | GetCulturalTraitsDesc |  | CString | 类别：nonconst |
| Culture | GetCurrentFervor |  | CFixedPoint | 类别：nonconst |
| Culture | GetCustom | CustomLocalization | CString | 类别：nonconst |
| Culture | GetDependents | Country | int64 | 类别：nonconst |
| Culture | GetDependentsAsPercentage | Country | CFixedPoint | 类别：nonconst |
| Culture | GetHeritageTrait |  | DiscriminationTrait | 类别：nonconst |
| Culture | GetID |  | uint32 | 类别：nonconst |
| Culture | GetLanguageTrait |  | DiscriminationTrait | 类别：nonconst |
| Culture | GetMigrationTargetsDesc |  | CString | 类别：nonconst |
| Culture | GetMonthlyChangeFervor |  | CFixedPoint | 类别：nonconst |
| Culture | GetName |  | CString | 类别：nonconst |
| Culture | GetNameNoFormatting |  | CString | 类别：nonconst |
| Culture | GetObsessionsDesc |  | CString | 类别：nonconst |
| Culture | GetPolStr | Country | int64 | 类别：nonconst |
| Culture | GetPolStrAsFloat | Unknown | float | 类别：nonconst |
| Culture | GetPolStrAsPercentage | Country | CFixedPoint | 类别：nonconst |
| Culture | GetPopulation | Country | int64 | 类别：nonconst |
| Culture | GetPopulationAsFloat | Unknown | float | 类别：nonconst |
| Culture | GetPopulationAsPercentage | Country | CFixedPoint | 类别：nonconst |
| Culture | GetPopulationChange | Country | int64 | 类别：nonconst |
| Culture | GetPopulationChangeDesc | Country | CString | 类别：nonconst |
| Culture | GetPopulationInCountryAsPercentage | Unknown | CFixedPoint | 类别：nonconst |
| Culture | GetReligion |  | Religion | 类别：nonconst |
| Culture | GetReligionsDesc |  | CString | 类别：nonconst |
| Culture | GetStateDependents | State | int64 | 类别：nonconst |
| Culture | GetStateDependentsAsPercentage | State | CFixedPoint | 类别：nonconst |
| Culture | GetStatePolStr | State | int64 | 类别：nonconst |
| Culture | GetStatePolStrAsFloat | Unknown | float | 类别：nonconst |
| Culture | GetStatePolStrAsPercentage | State | CFixedPoint | 类别：nonconst |
| Culture | GetStatePopulation | State | int64 | 类别：nonconst |
| Culture | GetStatePopulationAsFloat | Unknown | float | 类别：nonconst |
| Culture | GetStatePopulationAsPercentage | State | CFixedPoint | 类别：nonconst |
| Culture | GetStateWorkforce | State | int64 | 类别：nonconst |
| Culture | GetStateWorkforceAsPercentage | State | CFixedPoint | 类别：nonconst |
| Culture | GetTaboosDesc |  | CString | 类别：nonconst |
| Culture | GetTargetFervor |  | CFixedPoint | 类别：nonconst |
| Culture | GetTargetFervorBreakdown |  | CString | 类别：nonconst |
| Culture | GetTargetFervorFromCountryModifiers |  | CFixedPoint | 类别：nonconst |
| Culture | GetTargetFervorFromCountryModifiersBreakdown |  | CString | 类别：nonconst |
| Culture | GetTooltipTag |  | CString | 类别：nonconst |
| Culture | GetTraditionTraits |  | Unknown | 类别：nonconst |
| Culture | GetTurmoil |  | CFixedPoint | 类别：nonconst |
| Culture | GetWorkforce | Country | int64 | 类别：nonconst |
| Culture | GetWorkforceAsPercentage | Country | CFixedPoint | 类别：nonconst |
| Culture | HasNationalAwakening |  | bool |  |
| Culture | HasSecessionMovement | Country | bool |  |
| Culture | IsPrimaryCultureIn | Country | bool |  |
| Culture | IsPrimaryCultureInYesNo | Unknown | CString |  |
| Culture | IsValid |  | bool |  |
| Culture | MakeScope |  | Scope |  |
| Culture | Self |  | Culture |  |
| CultureCasualtyStatistics | AccessSelf |  | CultureCasualtyStatistics | 类别：const |
| CultureCasualtyStatistics | GetDead |  | int64 | 类别：nonconst |
| CultureCasualtyStatistics | GetDemoralized |  | int64 | 类别：nonconst |
| CultureCasualtyStatistics | GetWounded |  | int64 | 类别：nonconst |
| CultureCasualtyStatistics | Self |  | CultureCasualtyStatistics |  |
| CultureInfoPanel | AccessCulture |  | Culture | 类别：const |
| CultureInfoPanel | AccessPops |  | Unknown | 类别：const |
| CultureInfoPanel | AccessPopsList |  | PopList | 类别：const |
| CultureInfoPanel | AccessSelf |  | CultureInfoPanel | 类别：const |
| CultureInfoPanel | GetCulture |  | Culture | 类别：nonconst |
| CultureInfoPanel | IsShowingNationalOnly |  | bool |  |
| CultureInfoPanel | Self |  | CultureInfoPanel |  |
| CultureInfoPanel | ToggleShowNationalOnly |  | void |  |
| CurveEditor | AccessSelf |  | CurveEditor | 类别：const |
| CurveEditor | Configure |  | void |  |
| CurveEditor | Delete |  | void |  |
| CurveEditor | Self |  | CurveEditor |  |
| CurvePoint | AccessSelf |  | CurvePoint | 类别：const |
| CurvePoint | Position |  | CVector2f |  |
| CurvePoint | Self |  | CurvePoint |  |
| DataColorPicker | AccessSelf |  | DataColorPicker | 类别：const |
| DataColorPicker | GetColor |  | CVector4f | 类别：nonconst |
| DataColorPicker | GetName |  | CString | 类别：nonconst |
| DataColorPicker | OnColorEdited |  | void |  |
| DataColorPicker | Self |  | DataColorPicker |  |
| DataDynamicTrend | AccessSelf |  | DataDynamicTrend | 类别：const |
| DataDynamicTrend | Self |  | DataDynamicTrend |  |
| DataTrend | AccessSelf |  | DataTrend | 类别：const |
| DataTrend | Self |  | DataTrend |  |
| DatatypesExplorer | AccessSelf |  | DatatypesExplorer | 类别：const |
| DatatypesExplorer | DumpDataTypes |  | bool |  |
| DatatypesExplorer | IsEnableFilterFunctions |  | bool |  |
| DatatypesExplorer | IsEnableFilterMacros |  | bool |  |
| DatatypesExplorer | IsEnableFilterOrphanTypes |  | bool |  |
| DatatypesExplorer | IsEnableFilterPromotes |  | bool |  |
| DatatypesExplorer | IsEnableFilterTypes |  | bool |  |
| DatatypesExplorer | Self |  | DatatypesExplorer |  |
| DatatypesExplorer | SetDataTypeFilter |  | void |  |
| DatatypesExplorer | SetNameFilter |  | void |  |
| DatatypesExplorer | ToggleFilterFunctions |  | void |  |
| DatatypesExplorer | ToggleFilterMacros |  | void |  |
| DatatypesExplorer | ToggleFilterOrphanTypes |  | void |  |
| DatatypesExplorer | ToggleFilterPromotes |  | void |  |
| DatatypesExplorer | ToggleFilterTypes |  | void |  |
| Date | AccessSelf |  | Date | 类别：const |
| Date | Format | CString | CString |  |
| Date | GetString |  | CString | 类别：nonconst |
| Date | Self |  | Date |  |
| Decision | AccessSelf |  | Decision | 类别：const |
| Decision | GetCustom | CustomLocalization | CString | 类别：nonconst |
| Decision | GetDesc |  | CString | 类别：nonconst |
| Decision | GetName |  | CString | 类别：nonconst |
| Decision | GetTooltip | Country | CString | 类别：nonconst |
| Decision | GetTooltipTag |  | CString | 类别：nonconst |
| Decision | MakeScope |  | Scope |  |
| Decision | Self |  | Decision |  |
| Decision | TakeDecision | Country | Command |  |
| Decree | AccessSelf |  | Decree | 类别：const |
| Decree | GetCost |  | CFixedPoint | 类别：nonconst |
| Decree | GetCountry |  | Country | 类别：nonconst |
| Decree | GetCustom | CustomLocalization | CString | 类别：nonconst |
| Decree | GetModifier |  | Modifier | 类别：nonconst |
| Decree | GetName |  | CString | 类别：nonconst |
| Decree | GetRemoveCommand |  | Command | 类别：nonconst |
| Decree | GetState |  | State | 类别：nonconst |
| Decree | GetTexture |  | Unknown | 类别：nonconst |
| Decree | GetTooltip |  | CString | 类别：nonconst |
| Decree | GetTooltipTag |  | CString | 类别：nonconst |
| Decree | GetType |  | DecreeType | 类别：nonconst |
| Decree | MakeScope |  | Scope |  |
| Decree | Self |  | Decree |  |
| DecreeMarker | AccessDecree |  | Decree | 类别：const |
| DecreeMarker | AccessSelf |  | DecreeMarker | 类别：const |
| DecreeMarker | GetDecree |  | Decree | 类别：nonconst |
| DecreeMarker | GetPosition |  | CVector2f | 类别：nonconst |
| DecreeMarker | Self |  | DecreeMarker |  |
| DecreeType | AccessSelf |  | DecreeType | 类别：const |
| DecreeType | GetCostFormatted | Country | CString | 类别：nonconst |
| DecreeType | GetDesc |  | CString | 类别：nonconst |
| DecreeType | GetEffects |  | CString | 类别：nonconst |
| DecreeType | GetErrors | Unknown | CString | 类别：nonconst |
| DecreeType | GetModifier |  | Modifier | 类别：nonconst |
| DecreeType | GetName |  | CString | 类别：nonconst |
| DecreeType | GetNameNoFormatting |  | CString | 类别：nonconst |
| DecreeType | GetSetCommand | Unknown | Command | 类别：nonconst |
| DecreeType | GetTexture |  | Unknown | 类别：nonconst |
| DecreeType | GetTooltip | Country | CString | 类别：nonconst |
| DecreeType | GetTooltipForState | Unknown | CString | 类别：nonconst |
| DecreeType | GetTooltipTag |  | CString | 类别：nonconst |
| DecreeType | Self |  | DecreeType |  |
| DefineProxyNodeWindow | AccessSelf |  | DefineProxyNodeWindow | 类别：const |
| DefineProxyNodeWindow | GetName |  | CUTF8String | 类别：nonconst |
| DefineProxyNodeWindow | Self |  | DefineProxyNodeWindow |  |
| DefineProxyNodeWindow | SetName | PdxGuiWidget | void |  |
| DetailData | AccessSelf |  | DetailData | 类别：const |
| DetailData | ErrorsCount |  | int32 |  |
| DetailData | IsUpdating |  | bool |  |
| DetailData | MaterialIntensityBias |  | float |  |
| DetailData | MaterialsLimit |  | int32 |  |
| DetailData | Repack |  | void |  |
| DetailData | Self |  | DetailData |  |
| DetailData | SetMaterialIntensityBias | Unknown | void |  |
| DetailData | SetMaterialIntensityBiasStr |  | void |  |
| DetailData | SetMaterialsLimit | Unknown | void |  |
| DetailData | SupportedMaterialsLimits |  | Unknown |  |
| DiplomaticAction | AcceptActionProposal |  | Command |  |
| DiplomaticAction | AccessFirstCountry |  | Country | 类别：const |
| DiplomaticAction | AccessFirstState |  | State | 类别：const |
| DiplomaticAction | AccessSecondCountry |  | Country | 类别：const |
| DiplomaticAction | AccessSecondState |  | State | 类别：const |
| DiplomaticAction | AccessSelf |  | DiplomaticAction | 类别：const |
| DiplomaticAction | CanCallInObligation |  | bool |  |
| DiplomaticAction | CanOweObligation |  | bool |  |
| DiplomaticAction | CanPotentiallyOweObligation |  | bool |  |
| DiplomaticAction | DeclineActionProposal |  | Command |  |
| DiplomaticAction | ExecuteAction |  | Command |  |
| DiplomaticAction | ExecuteWithConfirmation |  | void |  |
| DiplomaticAction | GetAcceptanceValue |  | int32 | 类别：nonconst |
| DiplomaticAction | GetAcceptanceValueNoObligation |  | int32 | 类别：nonconst |
| DiplomaticAction | GetAcceptanceValueWithCallInObligation |  | int32 | 类别：nonconst |
| DiplomaticAction | GetAcceptanceValueWithOweObligation |  | int32 | 类别：nonconst |
| DiplomaticAction | GetActionAcceptEffectDesc |  | CString | 类别：nonconst |
| DiplomaticAction | GetActionDesc |  | CString | 类别：nonconst |
| DiplomaticAction | GetActionNotificationBreakDesc |  | CString | 类别：nonconst |
| DiplomaticAction | GetActionNotificationBreakName |  | CString | 类别：nonconst |
| DiplomaticAction | GetActionNotificationDesc |  | CString | 类别：nonconst |
| DiplomaticAction | GetActionNotificationName |  | CString | 类别：nonconst |
| DiplomaticAction | GetActionNotificationThirdPartyAcceptedDesc |  | CString | 类别：nonconst |
| DiplomaticAction | GetActionNotificationThirdPartyAcceptedName |  | CString | 类别：nonconst |
| DiplomaticAction | GetActionNotificationThirdPartyBreakAcceptedDesc |  | CString | 类别：nonconst |
| DiplomaticAction | GetActionNotificationThirdPartyBreakAcceptedName |  | CString | 类别：nonconst |
| DiplomaticAction | GetActionNotificationThirdPartyBreakDeclinedDesc |  | CString | 类别：nonconst |
| DiplomaticAction | GetActionNotificationThirdPartyBreakDeclinedName |  | CString | 类别：nonconst |
| DiplomaticAction | GetActionNotificationThirdPartyBreakDesc |  | CString | 类别：nonconst |
| DiplomaticAction | GetActionNotificationThirdPartyBreakName |  | CString | 类别：nonconst |
| DiplomaticAction | GetActionNotificationThirdPartyDeclinedDesc |  | CString | 类别：nonconst |
| DiplomaticAction | GetActionNotificationThirdPartyDeclinedName |  | CString | 类别：nonconst |
| DiplomaticAction | GetActionNotificationThirdPartyDesc |  | CString | 类别：nonconst |
| DiplomaticAction | GetActionNotificationThirdPartyName |  | CString | 类别：nonconst |
| DiplomaticAction | GetAskToBreakName |  | CString | 类别：nonconst |
| DiplomaticAction | GetBaseMaintenanceCost |  | CFixedPoint | 类别：nonconst |
| DiplomaticAction | GetBreakName |  | CString | 类别：nonconst |
| DiplomaticAction | GetCountryInfo |  | CString | 类别：nonconst |
| DiplomaticAction | GetCustom | CustomLocalization | CString | 类别：nonconst |
| DiplomaticAction | GetDesc |  | CString | 类别：nonconst |
| DiplomaticAction | GetEffectsDesc |  | CString | 类别：nonconst |
| DiplomaticAction | GetFirstCountry |  | Country | 类别：nonconst |
| DiplomaticAction | GetFirstState |  | State | 类别：nonconst |
| DiplomaticAction | GetID |  | uint32 | 类别：nonconst |
| DiplomaticAction | GetMaintenanceCost |  | CFixedPoint | 类别：nonconst |
| DiplomaticAction | GetMaintenanceCostDesc |  | CString | 类别：nonconst |
| DiplomaticAction | GetMaintenanceCostForAcceptingCountryDesc |  | CString | 类别：nonconst |
| DiplomaticAction | GetMaintenanceCostFormatted |  | CString | 类别：nonconst |
| DiplomaticAction | GetModifierDesc |  | CString | 类别：nonconst |
| DiplomaticAction | GetName |  | CString | 类别：nonconst |
| DiplomaticAction | GetNameNoFormatting |  | CString | 类别：nonconst |
| DiplomaticAction | GetNameWithContext |  | CString | 类别：nonconst |
| DiplomaticAction | GetPopupDesc |  | CString | 类别：nonconst |
| DiplomaticAction | GetProposalAcceptedDesc |  | CString | 类别：nonconst |
| DiplomaticAction | GetProposalAcceptedName |  | CString | 类别：nonconst |
| DiplomaticAction | GetProposalBreakAcceptedDesc |  | CString | 类别：nonconst |
| DiplomaticAction | GetProposalBreakAcceptedName |  | CString | 类别：nonconst |
| DiplomaticAction | GetProposalBreakDeclinedDesc |  | CString | 类别：nonconst |
| DiplomaticAction | GetProposalBreakDeclinedName |  | CString | 类别：nonconst |
| DiplomaticAction | GetProposalDeclinedDesc |  | CString | 类别：nonconst |
| DiplomaticAction | GetProposalDeclinedName |  | CString | 类别：nonconst |
| DiplomaticAction | GetProposalNotificationBreakDesc |  | CString | 类别：nonconst |
| DiplomaticAction | GetProposalNotificationBreakName |  | CString | 类别：nonconst |
| DiplomaticAction | GetProposalNotificationDesc |  | CString | 类别：nonconst |
| DiplomaticAction | GetProposalNotificationName |  | CString | 类别：nonconst |
| DiplomaticAction | GetProposeName |  | CString | 类别：nonconst |
| DiplomaticAction | GetRandomAcceptanceChance |  | CFixedPoint | 类别：nonconst |
| DiplomaticAction | GetRandomAcceptanceChanceNoObligation |  | CFixedPoint | 类别：nonconst |
| DiplomaticAction | GetRandomAcceptanceChanceWithCallInObligation |  | CFixedPoint | 类别：nonconst |
| DiplomaticAction | GetRandomAcceptanceChanceWithOweObligation |  | CFixedPoint | 类别：nonconst |
| DiplomaticAction | GetRivalryGains |  | CFixedPoint | 类别：nonconst |
| DiplomaticAction | GetRivalryGainsDetailsDesc |  | CString | 类别：nonconst |
| DiplomaticAction | GetSecondCountry |  | Country | 类别：nonconst |
| DiplomaticAction | GetSecondState |  | State | 类别：nonconst |
| DiplomaticAction | GetSoundWithConfirmation |  | Unknown | 类别：nonconst |
| DiplomaticAction | GetTargetStatesDesc |  | CString | 类别：nonconst |
| DiplomaticAction | GetTooltip |  | CString | 类别：nonconst |
| DiplomaticAction | GetTooltipTag |  | CString | 类别：nonconst |
| DiplomaticAction | GetType |  | DiplomaticActionType | 类别：nonconst |
| DiplomaticAction | GetWillAcceptBreakdown |  | CString | 类别：nonconst |
| DiplomaticAction | GetWillAcceptBreakdownNoObligation |  | CString | 类别：nonconst |
| DiplomaticAction | GetWillAcceptBreakdownWithCallInObligation |  | CString | 类别：nonconst |
| DiplomaticAction | GetWillAcceptBreakdownWithOweObligation |  | CString | 类别：nonconst |
| DiplomaticAction | GetWillAcceptDesc |  | CString | 类别：nonconst |
| DiplomaticAction | GetWillAcceptDescNoObligation |  | CString | 类别：nonconst |
| DiplomaticAction | GetWillAcceptDescWithCallInObligation |  | CString | 类别：nonconst |
| DiplomaticAction | GetWillAcceptDescWithOweObligation |  | CString | 类别：nonconst |
| DiplomaticAction | HasIncompleteTargetData |  | bool |  |
| DiplomaticAction | IsActivePact |  | bool |  |
| DiplomaticAction | IsCallingInObligation |  | bool |  |
| DiplomaticAction | IsHostile |  | bool |  |
| DiplomaticAction | IsHostileToBreak |  | bool |  |
| DiplomaticAction | IsHostileToPropose |  | bool |  |
| DiplomaticAction | IsNonActivePact |  | bool |  |
| DiplomaticAction | IsPersistentPact |  | bool |  |
| DiplomaticAction | IsPromisingObligation |  | bool |  |
| DiplomaticAction | IsRivalry |  | bool |  |
| DiplomaticAction | MakeScope |  | Scope |  |
| DiplomaticAction | RequiresApproval |  | bool |  |
| DiplomaticAction | RequiresApprovalToBreak |  | bool |  |
| DiplomaticAction | RequiresApprovalToPropose |  | bool |  |
| DiplomaticAction | RequiresConfirmation |  | bool |  |
| DiplomaticAction | Self |  | DiplomaticAction |  |
| DiplomaticAction | ViolatesSovereignty |  | bool |  |
| DiplomaticAction | WillAIAccept |  | bool |  |
| DiplomaticAction | WillAIAcceptNoObligation |  | bool |  |
| DiplomaticAction | WillAIAcceptWithCallInObligation |  | bool |  |
| DiplomaticAction | WillAIAcceptWithOweObligation |  | bool |  |
| DiplomaticAction | WillAIMaybeAccept |  | bool |  |
| DiplomaticAction | WillAIMaybeAcceptNoObligation |  | bool |  |
| DiplomaticAction | WillAIMaybeAcceptWithCallInObligation |  | bool |  |
| DiplomaticAction | WillAIMaybeAcceptWithOweObligation |  | bool |  |
| DiplomaticActionType | AccessSelf |  | DiplomaticActionType | 类别：const |
| DiplomaticActionType | CanSelectAnyState |  | bool |  |
| DiplomaticActionType | CanSelectFirstState |  | bool |  |
| DiplomaticActionType | CanSelectSecondState |  | bool |  |
| DiplomaticActionType | GetBaseMaintenanceCost |  | CFixedPoint | 类别：nonconst |
| DiplomaticActionType | GetDesc |  | CString | 类别：非 const |
| DiplomaticActionType | GetEffectDescriptionFirst | Country Country | CString | 类别：非 const |
| DiplomaticActionType | GetEffectDescriptionNoContext | Country Country | CString | 类别：非 const |
| DiplomaticActionType | GetEffectDescriptionThird | Country Country | CString | 类别：非 const |
| DiplomaticActionType | GetFirstModifier |  | Modifier | 类别：非 const |
| DiplomaticActionType | GetIncomeTransfer |  | CFixedPoint | 类别：非 const |
| DiplomaticActionType | GetKey |  | CString | 类别：非 const |
| DiplomaticActionType | GetMaintenanceCost | Country Country | CFixedPoint | 类别：非 const |
| DiplomaticActionType | GetMaintenanceCostDesc | Unknown Unknown | CString | 类别：非 const |
| DiplomaticActionType | GetMaintenanceCostFormatted | Country Country | CString | 类别：非 const |
| DiplomaticActionType | GetModifyPactActionType |  | DiplomaticActionType | 类别：非 const |
| DiplomaticActionType | GetName |  | CString | 类别：非 const |
| DiplomaticActionType | GetNameNoFormatting |  | CString | 类别：非 const |
| DiplomaticActionType | GetNameWithCountry | Unknown | CString | 类别：非 const |
| DiplomaticActionType | GetSecondModifier |  | Modifier | 类别：非 const |
| DiplomaticActionType | GetTexture |  | Unknown | 类别：非 const |
| DiplomaticActionType | GetTooltipTag |  | CString | 类别：非 const |
| DiplomaticActionType | GetTriggerDescriptionFirst | Country Country | CString | 类别：非 const |
| DiplomaticActionType | GetTriggerDescriptionFirstNot | Country Country | CString | 类别：非 const |
| DiplomaticActionType | GetTriggerDescriptionNoContext | Country Country | CString | 类别：非 const |
| DiplomaticActionType | GetTriggerDescriptionNoContextNot | Country Country | CString | 类别：非 const |
| DiplomaticActionType | GetTriggerDescriptionThird | Country Country | CString | 类别：非 const |
| DiplomaticActionType | GetTriggerDescriptionThirdNot | Country Country | CString | 类别：非 const |
| DiplomaticActionType | HasModifyPact |  | bool |  |
| DiplomaticActionType | HasReversePact |  | bool |  |
| DiplomaticActionType | HasTransferPact |  | bool |  |
| DiplomaticActionType | IsInstantDiplomaticAction |  | bool |  |
| DiplomaticActionType | IsOngoingDiplomaticAction |  | bool |  |
| DiplomaticActionType | IsOngoingDiplomaticPact |  | bool |  |
| DiplomaticActionType | MustSelectFirstState |  | bool |  |
| DiplomaticActionType | MustSelectSecondState |  | bool |  |
| DiplomaticActionType | Self |  | DiplomaticActionType |  |
| DiplomaticActionWindow | AccessDiplomaticAction |  | DiplomaticAction | 类别：const |
| DiplomaticActionWindow | AccessFirstState |  | State | 类别：const |
| DiplomaticActionWindow | AccessPossibleStates |  | Unknown | 类别：const |
| DiplomaticActionWindow | AccessSecondState |  | State | 类别：const |
| DiplomaticActionWindow | AccessSelf |  | DiplomaticActionWindow | 类别：const |
| DiplomaticActionWindow | AccessStateSelectionTarget |  | Country | 类别：const |
| DiplomaticActionWindow | CanSelectFirstState |  | bool |  |
| DiplomaticActionWindow | CanSelectSecondState |  | bool |  |
| DiplomaticActionWindow | ClearFirstState |  | void |  |
| DiplomaticActionWindow | ClearSecondState |  | void |  |
| DiplomaticActionWindow | ClearStateSelectionTarget |  | void |  |
| DiplomaticActionWindow | ExecuteAction |  | Command |  |
| DiplomaticActionWindow | GetConfirmationSound |  | Unknown | 类别：非 const |
| DiplomaticActionWindow | GetConfirmationTooltip |  | CString | 类别：非 const |
| DiplomaticActionWindow | GetDiplomaticAction |  | DiplomaticAction | 类别：非 const |
| DiplomaticActionWindow | GetFirstState |  | State | 类别：非 const |
| DiplomaticActionWindow | GetSecondState |  | State | 类别：非 const |
| DiplomaticActionWindow | GetStateSelectionTarget |  | Country | 类别：非 const |
| DiplomaticActionWindow | HasStateSelectionTarget |  | bool |  |
| DiplomaticActionWindow | IsUsingObligation |  | bool |  |
| DiplomaticActionWindow | SelectState | Unknown | void |  |
| DiplomaticActionWindow | Self |  | DiplomaticActionWindow |  |
| DiplomaticActionWindow | SetStateSelectionTarget | Unknown | void |  |
| DiplomaticActionWindow | ShowMapNotification |  | void |  |
| DiplomaticActionWindow | ToggleCallInObligation |  | void |  |
| DiplomaticActionWindow | ToggleOweObligation |  | void |  |
| DiplomaticActionWindow | WillCallInObligation |  | bool |  |
| DiplomaticActionWindow | WillOweObligation |  | bool |  |
| DiplomaticCatalyst | AccessDiplomaticCatalystType |  | DiplomaticCatalystType | 类别：const |
| DiplomaticCatalyst | AccessSelf |  | DiplomaticCatalyst | 类别：const |
| DiplomaticCatalyst | GetCountry |  | Country | 类别：非 const |
| DiplomaticCatalyst | GetCustom | CustomLocalization | CString | 类别：非 const |
| DiplomaticCatalyst | GetDesc |  | CString | 类别：非 const |
| DiplomaticCatalyst | GetDiplomaticCatalystType |  | DiplomaticCatalystType | 类别：非 const |
| DiplomaticCatalyst | GetOccuranceDate |  | Date | 类别：非 const |
| DiplomaticCatalyst | GetTargetCountry |  | Country | 类别：非 const |
| DiplomaticCatalyst | GetTooltipTag |  | CString | 类别：非 const |
| DiplomaticCatalyst | IsValid |  | bool |  |
| DiplomaticCatalyst | MakeScope |  | Scope |  |
| DiplomaticCatalyst | Self |  | DiplomaticCatalyst |  |
| DiplomaticCatalystCategory | AccessSelf |  | DiplomaticCatalystCategory | 类别：const |
| DiplomaticCatalystCategory | GetCatalystEffectCooldownDays |  | int32 | 类别：非 const |
| DiplomaticCatalystCategory | GetCustom | CustomLocalization | CString | 类别：非 const |
| DiplomaticCatalystCategory | GetName |  | CString | 类别：非 const |
| DiplomaticCatalystCategory | GetTooltipTag |  | CString | 类别：非 const |
| DiplomaticCatalystCategory | MakeScope |  | Scope |  |
| DiplomaticCatalystCategory | Self |  | DiplomaticCatalystCategory |  |
| DiplomaticCatalystType | AccessSelf |  | DiplomaticCatalystType | 类别：const |
| DiplomaticCatalystType | GetCategory |  | DiplomaticCatalystCategory | 类别：非 const |
| DiplomaticCatalystType | GetCustom | CustomLocalization | CString | 类别：非 const |
| DiplomaticCatalystType | GetDesc | Unknown Unknown | CString | 类别：非 const |
| DiplomaticCatalystType | GetName |  | CString | 类别：非 const |
| DiplomaticCatalystType | GetTooltipTag |  | CString | 类别：非 const |
| DiplomaticCatalystType | MakeScope |  | Scope |  |
| DiplomaticCatalystType | Self |  | DiplomaticCatalystType |  |
| DiplomaticDemand | AcceptDiplomaticDemand |  | Command |  |
| DiplomaticDemand | AccessSelf |  | DiplomaticDemand | 类别：const |
| DiplomaticDemand | GetCustom | CustomLocalization | CString | 类别：非 const |
| DiplomaticDemand | GetDemandedWarGoal |  | WarGoal | 类别：非 const |
| DiplomaticDemand | GetDiplomaticPlayType |  | DiplomaticPlayType | 类别：非 const |
| DiplomaticDemand | GetProposalDesc |  | CString | 类别：非 const |
| DiplomaticDemand | GetSender |  | Country | 类别：非 const |
| DiplomaticDemand | GetTarget |  | Country | 类别：非 const |
| DiplomaticDemand | GetTooltipTag |  | CString | 类别：非 const |
| DiplomaticDemand | IsValid |  | bool |  |
| DiplomaticDemand | MakeScope |  | Scope |  |
| DiplomaticDemand | RejectDiplomaticDemand |  | Command |  |
| DiplomaticDemand | Self |  | DiplomaticDemand |  |
| DiplomaticOverviewPanel | AccessSelf |  | DiplomaticOverviewPanel | 类别：const |
| DiplomaticOverviewPanel | GetCountries |  | Unknown | 类别：非 const |
| DiplomaticOverviewPanel | IsSorted | Unknown | bool |  |
| DiplomaticOverviewPanel | Self |  | DiplomaticOverviewPanel |  |
| DiplomaticOverviewPanel | Sort | CString | void |  |
| DiplomaticPact | AccessSelf |  | DiplomaticPact | 类别：const |
| DiplomaticPact | GetAboutToBreakReasonDesc |  | CString | 类别：非 const |
| DiplomaticPact | GetAutoBreakReasonDesc |  | CString | 类别：非 const |
| DiplomaticPact | GetCustom | CustomLocalization | CString | 类别：非 const |
| DiplomaticPact | GetDailyRelationsProgress |  | CFixedPoint | 类别：非 const |
| DiplomaticPact | GetDesc |  | CString | 类别：非 const |
| DiplomaticPact | GetDiplomaticAction |  | DiplomaticAction | 类别：非 const |
| DiplomaticPact | GetDiplomaticActionType |  | DiplomaticActionType | 类别：非 const |
| DiplomaticPact | GetFirstCountry |  | Country | 类别：非 const |
| DiplomaticPact | GetID |  | uint32 | 类别：非 const |
| DiplomaticPact | GetName |  | CString | 类别：非 const |
| DiplomaticPact | GetSecondCountry |  | Country | 类别：非 const |
| DiplomaticPact | GetTooltip |  | CString | 类别：非 const |
| DiplomaticPact | GetTooltipTag |  | CString | 类别：非 const |
| DiplomaticPact | HasDailyRelationsProgress |  | bool |  |
| DiplomaticPact | IsFirstCountry | Country | bool |  |
| DiplomaticPact | IsSecondCountry | Country | bool |  |
| DiplomaticPact | IsSubjectRelation |  | bool |  |
| DiplomaticPact | MakeScope |  | Scope |  |
| DiplomaticPact | Self |  | DiplomaticPact |  |
| DiplomaticPact | ShowInOutliner |  | bool |  |
| DiplomaticPlay | AccessExecutedWarGoalsAgainst | Country | Unknown | 类别：const |
| DiplomaticPlay | AccessInitiator |  | Country | 类别：const |
| DiplomaticPlay | AccessInitiatorBackers |  | Unknown | 类别：const |
| DiplomaticPlay | AccessInitiatorBackersNoLoyalSubjects |  | Unknown | 类别：const |
| DiplomaticPlay | AccessInitiatorLeaning |  | Unknown | 类别：const |
| DiplomaticPlay | AccessInitiatorSideCountries |  | Unknown | 类别：const |
| DiplomaticPlay | AccessInitiatorSideCountriesNoLoyalSubjects |  | Unknown | 类别：const |
| DiplomaticPlay | AccessOnTheFence |  | Unknown | 类别：const |
| DiplomaticPlay | AccessSelf |  | DiplomaticPlay | 类别：const |
| DiplomaticPlay | AccessTarget |  | Country | 类别：const |
| DiplomaticPlay | AccessTargetBackers |  | Unknown | 类别：const |
| DiplomaticPlay | AccessTargetBackersNoLoyalSubjects |  | Unknown | 类别：const |
| DiplomaticPlay | AccessTargetLeaning |  | Unknown | 类别：const |
| DiplomaticPlay | AccessTargetSideCountries |  | Unknown | 类别：const |
| DiplomaticPlay | AccessTargetSideCountriesNoLoyalSubjects |  | Unknown | 类别：const |
| DiplomaticPlay | AccessUndecided |  | Unknown | 类别：const |
| DiplomaticPlay | AccessWar |  | War | 类别：const |
| DiplomaticPlay | AddTreatyWarGoal | WarGoalDraft ArticleDraft | Command |  |
| DiplomaticPlay | AddWarGoal | WarGoalDraft | Command |  |
| DiplomaticPlay | AreOnSameSide | Country Country | bool |  |
| DiplomaticPlay | AtLeastOneCountryWouldAcceptAnySway | Country | bool |  |
| DiplomaticPlay | BeOnTheFence | Country | Command |  |
| DiplomaticPlay | CanAddWarGoal | Country | bool |  |
| DiplomaticPlay | CanAddWarGoalForOtherCountry | Unknown | bool |  |
| DiplomaticPlay | CanBeOnTheFence | Country | bool |  |
| DiplomaticPlay | CanDeclareNeutrality | Country | bool |  |
| DiplomaticPlay | CanLeanTowardsInitiator | Country | bool |  |
| DiplomaticPlay | CanLeanTowardsTarget | Country | bool |  |
| DiplomaticPlay | CanSupportInitiator | Country | bool |  |
| DiplomaticPlay | CanSupportTarget | Country | bool |  |
| DiplomaticPlay | CanSwayCountry | Country Country | bool |  |
| DiplomaticPlay | CanYield | Country | bool |  |
| DiplomaticPlay | CreateSway | Country Country SwayOffer | Command |  |
| DiplomaticPlay | DeclareNeutrality | Country | Command |  |
| DiplomaticPlay | GetAcceptedSway | Country | Sway | 类别：非 const |
| DiplomaticPlay | GetAllWarGoalsOfInitiatorSide |  | Unknown | 类别：非 const |
| DiplomaticPlay | GetAllWarGoalsOfTargetSide |  | Unknown | 类别：非 const |
| DiplomaticPlay | GetBeOnTheFenceValidTooltip | Country | CString | 类别：非 const |
| DiplomaticPlay | GetCanAddWarGoalDesc | WarGoalDraft | CString | 类别：非 const |
| DiplomaticPlay | GetCanSendSwayOfferDesc | Country Country SwayOffer | CString | 类别：非 const |
| DiplomaticPlay | GetCanSwayCountryDesc | Country Country | CString | 类别：非 const |
| DiplomaticPlay | GetConfidence | Unknown | int32 | 类别：非 const |
| DiplomaticPlay | GetConfidenceDesc | Country | CString | 类别：非 const |
| DiplomaticPlay | GetConfidenceLabel | Country | CString | 类别：非 const |
| DiplomaticPlay | GetCountryCanAddWarGoalDesc | Country | CString | 类别：非 const |
| DiplomaticPlay | GetCustom | CustomLocalization | CString | 类别：非 const |
| DiplomaticPlay | GetDeclareNeutralityValidTooltip | Country | CString | 类别：非 const |
| DiplomaticPlay | GetDiplomaticPlayType |  | DiplomaticPlayType | 类别：非 const |
| DiplomaticPlay | GetEndDate |  | CString | 类别：非 const |
| DiplomaticPlay | GetEscalation |  | int32 | 类别：非 const |
| DiplomaticPlay | GetEscalationPause |  | int32 | 类别：非 const |
| DiplomaticPlay | GetEscalationProgress |  | CFixedPoint | 类别：非 const |
| DiplomaticPlay | GetIncomingSway | Unknown Unknown | Sway | 类别：非 const |
| DiplomaticPlay | GetIncomingSwayByTargetAndSwayer | Unknown Unknown | Sway | 类别：非 const |
| DiplomaticPlay | GetInitiator |  | Country | 类别：非 const |
| DiplomaticPlay | GetInitiatorBackersBreakdown |  | CString | 类别：非 const |
| DiplomaticPlay | GetInitiatorPreferenceScore | Country | int32 | 类别：非 const |
| DiplomaticPlay | GetInitiatorPreferenceScoreDesc | Country | CString | 类别：非 const |
| DiplomaticPlay | GetInitiatorPrimaryWarGoals |  | Unknown | 类别：非 const |
| DiplomaticPlay | GetInitiatorSecondaryWarGoals |  | Unknown | 类别：非 const |
| DiplomaticPlay | GetInitiatorWarGoals |  | Unknown | 类别：非 const |
| DiplomaticPlay | GetInterestMarker | Unknown | Interest | 类别：非 const |
| DiplomaticPlay | GetLeanTowardsInitiatorValidTooltip | Country | CString | 类别：非 const |
| DiplomaticPlay | GetLeanTowardsTargetValidTooltip | Country | CString | 类别：非 const |
| DiplomaticPlay | GetName |  | CString | 类别：非 const |
| DiplomaticPlay | GetNumInitiatorManeuversRemaining |  | int32 | 类别：非 const |
| DiplomaticPlay | GetNumLeaningMobilizedBattalionsForSide | Unknown | int32 | 类别：非 const |
| DiplomaticPlay | GetNumLeaningMobilizedBattalionsForSideBreakdown | Unknown | CString | 类别：非 const |
| DiplomaticPlay | GetNumLeaningTotalBattalionsForSide | Unknown | int32 | 类别：非 const |
| DiplomaticPlay | GetNumLeaningTotalBattalionsForSideBreakdown | Unknown | CString | 类别：非 const |
| DiplomaticPlay | GetNumLeaningTotalWarshipsForSide | Unknown | int32 | 类别：非 const |
| DiplomaticPlay | GetNumLeaningTotalWarshipsForSideBreakdown | Unknown | CString | 类别：非 const |
| DiplomaticPlay | GetNumManeuversRemaining | Country | int32 | 类别：非 const |
| DiplomaticPlay | GetNumOnTheFenceBattalionsBreakdown |  | CString | 类别：非 const |
| DiplomaticPlay | GetNumOnTheFenceMobilizedBattalions |  | int32 | 类别：非 const |
| DiplomaticPlay | GetNumOnTheFenceTotalBattalions |  | int32 | 类别：非 const |
| DiplomaticPlay | GetNumOnTheFenceTotalWarships |  | int32 | 类别：非 const |
| DiplomaticPlay | GetNumOnTheFenceWarshipsBreakdown |  | CString | 类别：非 const |
| DiplomaticPlay | GetNumTargetManeuversRemaining |  | int32 | 类别：非 const |
| DiplomaticPlay | GetNumberOfPossibleSwayCountriesFormatted | Country | CString | 类别：非 const |
| DiplomaticPlay | GetOutgoingSway | Unknown Unknown | Sway | 类别：非 const |
| DiplomaticPlay | GetPhaseName |  | CString | 类别：非 const |
| DiplomaticPlay | GetPreferenceScoreDesc | Unknown | CString | 类别：非 const |
| DiplomaticPlay | GetStartDate |  | CString | 类别：非 const |
| DiplomaticPlay | GetStrategicRegion |  | StrategicRegion | 类别：非 const |
| DiplomaticPlay | GetSupportInitiatorValidTooltip | Country | CString | 类别：非 const |
| DiplomaticPlay | GetSupportStanceDesc | Country | CString | 类别：非 const |
| DiplomaticPlay | GetSupportTargetValidTooltip | Country | CString | 类别：非 const |
| DiplomaticPlay | GetSwitchSideBreakdown |  | CString | 类别：非 const |
| DiplomaticPlay | GetTarget |  | Country | 类别：非 const |
| DiplomaticPlay | GetTargetBackersBreakdown |  | CString | 类别：非 const |
| DiplomaticPlay | GetTargetPreferenceScore | Country | int32 | 类别：非 const |
| DiplomaticPlay | GetTargetPreferenceScoreDesc | Country | CString | 类别：非 const |
| DiplomaticPlay | GetTargetPrimaryWarGoals |  | Unknown | 类别：非 const |
| DiplomaticPlay | GetTargetSecondaryWarGoals |  | Unknown | 类别：非 const |
| DiplomaticPlay | GetTargetWarGoals |  | Unknown | 类别：非 const |
| DiplomaticPlay | GetTooltipTag |  | CString | 类别：非 const |
| DiplomaticPlay | GetTotalNumBattalionsForSide | Country | int32 | 类别：非 const |
| DiplomaticPlay | GetTotalNumMobilizedBattalionsForSide | Country | int32 | 类别：非 const |
| DiplomaticPlay | GetTotalNumMobilizedBattalionsForSideBreakdown | Country | CString | 类别：非 const |
| DiplomaticPlay | GetTotalNumWarshipsForSide | Country | int32 | 类别：非 const |
| DiplomaticPlay | GetTotalNumWarshipsForSideBreakdown | Country | CString | 类别：非 const |
| DiplomaticPlay | GetWar |  | War | 类别：非 const |
| DiplomaticPlay | GetYieldValidTooltip | Country | CString | 类别：非 const |
| DiplomaticPlay | HasAcceptedSway | Country | bool |  |
| DiplomaticPlay | HasAtLeastOneDesiredSwayOfType | Country Country SwayOfferType | bool |  |
| DiplomaticPlay | HasAtLeastOneDesiredSwayWargoalOfType | Country Country WarGoalType | bool |  |
| DiplomaticPlay | HasEscalatedIntoWar |  | bool |  |
| DiplomaticPlay | HasPreferenceForInitiator | Unknown | bool |  |
| DiplomaticPlay | HasPreferenceForTarget | Unknown | bool |  |
| DiplomaticPlay | IsAmongInitiatorBackers | Unknown | bool |  |
| DiplomaticPlay | IsAmongTargetBackers | Unknown | bool |  |
| DiplomaticPlay | IsBacker | Country | bool |  |
| DiplomaticPlay | IsCommittedParticipant | Country | bool |  |
| DiplomaticPlay | IsInitiator | Country | bool |  |
| DiplomaticPlay | IsInitiatorBacker | Unknown | bool |  |
| DiplomaticPlay | IsInitiatorLeaning | Country | bool |  |
| DiplomaticPlay | IsInitiatorOrBacker | Country | bool |  |
| DiplomaticPlay | IsInvolved | Country | bool |  |
| DiplomaticPlay | IsOnTheFence | Country | bool |  |
| DiplomaticPlay | IsPinnedInOutliner |  | bool |  |
| DiplomaticPlay | IsPrimaryParticipant | Unknown | bool |  |
| DiplomaticPlay | IsTarget | Country | bool |  |
| DiplomaticPlay | IsTargetBacker | Unknown | bool |  |
| DiplomaticPlay | IsTargetLeaning | Country | bool |  |
| DiplomaticPlay | IsTargetOrBacker | Unknown | bool |  |
| DiplomaticPlay | IsTargetOrInitiator | Country | bool |  |
| DiplomaticPlay | IsUndecidedParticipant | Country | bool |  |
| DiplomaticPlay | IsValid |  | bool |  |
| DiplomaticPlay | IsValidWarGoalDeclarer | Country | bool |  |
| DiplomaticPlay | LeanTowardsInitiator | Country | Command |  |
| DiplomaticPlay | LeanTowardsTarget | Country | Command |  |
| DiplomaticPlay | MakeScope |  | Scope |  |
| DiplomaticPlay | PlayerHasPotentialSwayOffers | Country | bool |  |
| DiplomaticPlay | Self |  | DiplomaticPlay |  |
| DiplomaticPlay | SupportInitiator | Unknown | Command |  |
| DiplomaticPlay | SupportTarget | Unknown | Command |  |
| DiplomaticPlay | SwitchSide | Country | Command |  |
| DiplomaticPlay | TogglePinInOutliner |  | void |  |
| DiplomaticPlay | WouldAcceptAnySway | Country Country | bool |  |
| DiplomaticPlay | Yield | Country | Command |  |
| DiplomaticPlayConfirmation | AccessCountryCreations |  | Unknown | 类别：const |
| DiplomaticPlayConfirmation | AccessInitiatorCountries |  | Unknown | 类别：const |
| DiplomaticPlayConfirmation | AccessInvolvedCountries |  | Unknown | 类别：const |
| DiplomaticPlayConfirmation | AccessSelf |  | DiplomaticPlayConfirmation | 类别：const |
| DiplomaticPlayConfirmation | AccessTargetCountries |  | Unknown | 类别：const |
| DiplomaticPlayConfirmation | AccessUndecidedCountries |  | Unknown | 类别：const |
| DiplomaticPlayConfirmation | CanJoinInitiator | Country | bool |  |
| DiplomaticPlayConfirmation | CanJoinTarget | Country | bool |  |
| DiplomaticPlayConfirmation | ConfirmAction |  | Command |  |
| DiplomaticPlayConfirmation | CreateDiplomaticDemand |  | Command |  |
| DiplomaticPlayConfirmation | GetConfirmationSound |  | Unknown | 类别：非 const |
| DiplomaticPlayConfirmation | GetCountryDefinition |  | CountryDefinition | 类别：非 const |
| DiplomaticPlayConfirmation | GetDescription |  | CString | 类别：非 const |
| DiplomaticPlayConfirmation | GetDiplomaticDemandAcceptanceDesc |  | CString | 类别：非 const |
| DiplomaticPlayConfirmation | GetInitiatorCountry |  | Country | 类别：非 const |
| DiplomaticPlayConfirmation | GetTargetCountry |  | Country | 类别：非 const |
| DiplomaticPlayConfirmation | GetTargetState |  | State | 类别：非 const |
| DiplomaticPlayConfirmation | GetType |  | DiplomaticPlayType | 类别：非 const |
| DiplomaticPlayConfirmation | IsSelectingCountryCreation |  | bool |  |
| DiplomaticPlayConfirmation | PredictCannotJoinOrPreferenceForInitiatorDesc | Unknown | CString |  |
| DiplomaticPlayConfirmation | PredictCannotJoinOrPreferenceForTargetDesc | Unknown | CString |  |
| DiplomaticPlayConfirmation | PredictHasPreferenceForInitiator | Country | bool |  |
| DiplomaticPlayConfirmation | PredictHasPreferenceForTarget | Country | bool |  |
| DiplomaticPlayConfirmation | PredictInitiatorPreferenceScore | Unknown | int32 |  |
| DiplomaticPlayConfirmation | PredictInitiatorPreferenceScoreDesc | Unknown | CString |  |
| DiplomaticPlayConfirmation | PredictInitiatorPreferenceScoreFormatted | Country | CString |  |
| DiplomaticPlayConfirmation | PredictPreferenceScoreDesc | Unknown | CString |  |
| DiplomaticPlayConfirmation | PredictTargetPreferenceScore | Unknown | int32 |  |
| DiplomaticPlayConfirmation | PredictTargetPreferenceScoreDesc | Unknown | CString |  |
| DiplomaticPlayConfirmation | PredictTargetPreferenceScoreFormatted | Country | CString |  |
| DiplomaticPlayConfirmation | Self |  | DiplomaticPlayConfirmation |  |
| DiplomaticPlayConfirmation | SetCountryDefinition | Unknown | void |  |
| DiplomaticPlayConfirmation | ShowMapNotification |  | void |  |
| DiplomaticPlayConfirmation | ToggleForceDiplomaticPlay |  | void |  |
| DiplomaticPlayConfirmation | ToggleSelectCountryCreation |  | void |  |
| DiplomaticPlayConfirmation | TriggerDiplomaticPlay |  | Command |  |
| DiplomaticPlayConfirmation | WillForceDiplomaticPlay |  | bool |  |
| DiplomaticPlayPanel | AccessDiplomaticPlay |  | DiplomaticPlay | 类别：const |
| DiplomaticPlayPanel | AccessSelf |  | DiplomaticPlayPanel | 类别：const |
| DiplomaticPlayPanel | GetDiplomaticPlay |  | DiplomaticPlay | 类别：非 const |
| DiplomaticPlayPanel | Self |  | DiplomaticPlayPanel |  |
| DiplomaticPlayType | AccessSelf |  | DiplomaticPlayType | 类别：const |
| DiplomaticPlayType | GetCustom | CustomLocalization | CString | 类别：非 const |
| DiplomaticPlayType | GetDiplomaticDemandAcceptanceDesc | Unknown Unknown Unknown Unknown | CString | 类别：非 const |
| DiplomaticPlayType | GetName |  | CString | 类别：非 const |
| DiplomaticPlayType | GetSoundWithConfirmation |  | Unknown | 类别：非 const |
| DiplomaticPlayType | GetStartCommandCountry | Country Country | Command | 类别：非 const |
| DiplomaticPlayType | GetStartCommandCountryWithDefinition | Unknown Unknown Unknown | Command | 类别：非 const |
| DiplomaticPlayType | GetStartCommandState | Country State | Command | 类别：非 const |
| DiplomaticPlayType | GetStartDescCountry | Country Country | CString | 类别：非常量 |
| DiplomaticPlayType | GetStartDescCountryWithDefinition | Country Country CountryDefinition | CString | 类别：非常量 |
| DiplomaticPlayType | GetStartDescState | Country State | CString | 类别：非常量 |
| DiplomaticPlayType | GetStartTooltipCountry | Country Country | CString | 类别：非常量 |
| DiplomaticPlayType | GetStartTooltipCountryWithDefinition | Unknown Unknown Unknown | CString | 类别：非常量 |
| DiplomaticPlayType | GetStartTooltipState | Country State | CString | 类别：非常量 |
| DiplomaticPlayType | GetTexture |  | Unknown | 类别：非常量 |
| DiplomaticPlayType | GetTooltipTag |  | CString | 类别：非常量 |
| DiplomaticPlayType | GetWarGoalType |  | WarGoalType | 类别：非常量 |
| DiplomaticPlayType | HasEnableSwitchSides |  | bool |  |
| DiplomaticPlayType | IsEpic |  | bool |  |
| DiplomaticPlayType | MakeScope |  | Scope |  |
| DiplomaticPlayType | Self |  | DiplomaticPlayType |  |
| DiplomaticPlayType | ShowConfirmationCountry | Country | void |  |
| DiplomaticPlayType | ShowConfirmationCountryWithDefinition | Unknown Unknown | void |  |
| DiplomaticPlayType | ShowConfirmationState | State | void |  |
| DiplomaticRelations | AccessSelf |  | DiplomaticRelations | 类别：常量 |
| DiplomaticRelations | CalcOwedObligationDaysLeft | Country | int32 |  |
| DiplomaticRelations | GetCountryWhichNotOwesObligation |  | Country | 类别：非常量 |
| DiplomaticRelations | GetCountryWhichOwesObligation |  | Country | 类别：非常量 |
| DiplomaticRelations | GetCustom | CustomLocalization | CString | 类别：非常量 |
| DiplomaticRelations | GetFirstCountry |  | Country | 类别：非常量 |
| DiplomaticRelations | GetID |  | uint32 | 类别：非常量 |
| DiplomaticRelations | GetSecondCountry |  | Country | 类别：非常量 |
| DiplomaticRelations | GetTooltipTag |  | CString | 类别：非常量 |
| DiplomaticRelations | MakeScope |  | Scope |  |
| DiplomaticRelations | Self |  | DiplomaticRelations |  |
| DiscriminationTrait | AccessSelf |  | DiscriminationTrait | 类别：常量 |
| DiscriminationTrait | GetCulturesDesc |  | CString | 类别：非常量 |
| DiscriminationTrait | GetName |  | CString | 类别：非常量 |
| DiscriminationTrait | GetNameNoFormatting |  | CString | 类别：非常量 |
| DiscriminationTrait | GetReligionsDesc |  | CString | 类别：非常量 |
| DiscriminationTrait | GetTooltipTag |  | CString | 类别：非常量 |
| DiscriminationTrait | GetTraitGroup |  | DiscriminationTraitGroup | 类别：非常量 |
| DiscriminationTrait | GetType |  | CString | 类别：非常量 |
| DiscriminationTrait | HasTraitGroup |  | bool |  |
| DiscriminationTrait | IsCulturalTrait |  | bool |  |
| DiscriminationTrait | Self |  | DiscriminationTrait |  |
| DiscriminationTraitGroup | AccessSelf |  | DiscriminationTraitGroup | 类别：常量 |
| DiscriminationTraitGroup | GetCulturesDesc |  | CString | 类别：非常量 |
| DiscriminationTraitGroup | GetName |  | CString | 类别：非常量 |
| DiscriminationTraitGroup | GetNameNoFormatting |  | CString | 类别：非常量 |
| DiscriminationTraitGroup | GetReligionsDesc |  | CString | 类别：非常量 |
| DiscriminationTraitGroup | GetTooltipTag |  | CString | 类别：非常量 |
| DiscriminationTraitGroup | GetType |  | CString | 类别：非常量 |
| DiscriminationTraitGroup | IsCulturalTrait |  | bool |  |
| DiscriminationTraitGroup | Self |  | DiscriminationTraitGroup |  |
| Dlc | AccessSelf |  | Dlc | 类别：常量 |
| Dlc | GetBanner |  | Unknown | 类别：非常量 |
| Dlc | GetDesc |  | CString | 类别：非常量 |
| Dlc | GetIcon |  | Unknown | 类别：非常量 |
| Dlc | GetName |  | CString | 类别：非常量 |
| Dlc | GetThemeBreakdown |  | CString | 类别：非常量 |
| Dlc | GetTooltipTag |  | CString | 类别：非常量 |
| Dlc | IsEnabled |  | bool |  |
| Dlc | IsMajor |  | bool |  |
| Dlc | IsThemeProvider |  | bool |  |
| Dlc | IsVerified |  | bool |  |
| Dlc | Self |  | Dlc |  |
| Dlc | ShowInStore |  | void |  |
| DockableLayout | AccessSelf |  | DockableLayout | 类别：常量 |
| DockableLayout | GetName |  | CString | 类别：非常量 |
| DockableLayout | Self |  | DockableLayout |  |
| DockableLayoutManager | AccessActiveLayout |  | DockableLayout | 类别：常量 |
| DockableLayoutManager | AccessLayoutSearchList |  | ToolPropertySearchList | 类别：常量 |
| DockableLayoutManager | AccessLayouts |  | Unknown | 类别：常量 |
| DockableLayoutManager | AccessSelectedLayout |  | DockableLayout | 类别：常量 |
| DockableLayoutManager | AccessSelf |  | DockableLayoutManager | 类别：常量 |
| DockableLayoutManager | DeleteUserLayout |  | void |  |
| DockableLayoutManager | SaveAsNewUserLayout |  | void |  |
| DockableLayoutManager | SaveUserLayout |  | void |  |
| DockableLayoutManager | Self |  | DockableLayoutManager |  |
| DockableLayoutManager | SwitchToSelectedLayout |  | void |  |
| DockableWindow | AccessSelf |  | DockableWindow | 类别：常量 |
| DockableWindow | Close |  | void |  |
| DockableWindow | IsHidden |  | bool |  |
| DockableWindow | IsMoving |  | bool |  |
| DockableWindow | Position |  | CVector2f |  |
| DockableWindow | ResizeHandleSize |  | CVector2f |  |
| DockableWindow | Self |  | DockableWindow |  |
| DockableWindow | Size |  | CVector2f |  |
| DockableWindow | Title |  | CString |  |
| DockableWindow | WidgetPosition |  | CVector2f |  |
| DockableWindow | WidgetSize |  | CVector2f |  |
| DrawCmdsList | AccessSelf |  | DrawCmdsList | 类别：常量 |
| DrawCmdsList | GetAttachmentInfo |  | CString | 类别：非常量 |
| DrawCmdsList | GetDrawNumber |  | CString | 类别：非常量 |
| DrawCmdsList | GetFormat |  | CString | 类别：非常量 |
| DrawCmdsList | GetResolution |  | CString | 类别：非常量 |
| DrawCmdsList | GetSize |  | uint64 | 类别：非常量 |
| DrawCmdsList | GetTextureName |  | Unknown | 类别：非常量 |
| DrawCmdsList | GetZoneName |  | CString | 类别：非常量 |
| DrawCmdsList | IsCaptured |  | bool |  |
| DrawCmdsList | Self |  | DrawCmdsList |  |
| DrawCmdsViewer | AccessSelf |  | DrawCmdsViewer | 类别：常量 |
| DrawCmdsViewer | CaptureFrame |  | void |  |
| DrawCmdsViewer | ClearCapture |  | void |  |
| DrawCmdsViewer | DecrementCapturedDrawCount |  | void |  |
| DrawCmdsViewer | DecrementCapturedDrawNumberOffset |  | void |  |
| DrawCmdsViewer | GetCapturedDrawCount |  | uint32 | 类别：非常量 |
| DrawCmdsViewer | GetCapturedDrawNumberOffset |  | uint32 | 类别：非常量 |
| DrawCmdsViewer | GetCapturedFrameNumber |  | uint32 | 类别：非常量 |
| DrawCmdsViewer | GetDrawCommandData |  | Unknown | 类别：非常量 |
| DrawCmdsViewer | IncrementCapturedDrawCount |  | void |  |
| DrawCmdsViewer | IncrementCapturedDrawNumberOffset |  | void |  |
| DrawCmdsViewer | Self |  | DrawCmdsViewer |  |
| DrawCmdsViewer | SetDrawCount |  | void |  |
| DrawCmdsViewer | SetDrawOffset |  | void |  |
| EditorSettingCategory | AccessSelf |  | EditorSettingCategory | 类别：常量 |
| EditorSettingCategory | GetName |  | CString | 类别：非常量 |
| EditorSettingCategory | Self |  | EditorSettingCategory |  |
| EditorSettingsPage | AccessCategories |  | Unknown | 类别：常量 |
| EditorSettingsPage | AccessSelf |  | EditorSettingsPage | 类别：常量 |
| EditorSettingsPage | GetName |  | CString | 类别：非常量 |
| EditorSettingsPage | IsSelected |  | bool |  |
| EditorSettingsPage | OnClick |  | void |  |
| EditorSettingsPage | Self |  | EditorSettingsPage |  |
| EditorSettingsWindow | AccessActivePage |  | EditorSettingsPage | 类别：常量 |
| EditorSettingsWindow | AccessPages |  | Unknown | 类别：常量 |
| EditorSettingsWindow | AccessSelf |  | EditorSettingsWindow | 类别：常量 |
| EditorSettingsWindow | AllowApply |  | bool |  |
| EditorSettingsWindow | AppliedOnRestart |  | bool |  |
| EditorSettingsWindow | Close |  | void |  |
| EditorSettingsWindow | GetWindowName |  | CString | 类别：非常量 |
| EditorSettingsWindow | HasChanged |  | bool |  |
| EditorSettingsWindow | Hide |  | void |  |
| EditorSettingsWindow | OnApply |  | void |  |
| EditorSettingsWindow | RequireRestart |  | bool |  |
| EditorSettingsWindow | Restore |  | void |  |
| EditorSettingsWindow | Save |  | void |  |
| EditorSettingsWindow | SaveAndClose |  | void |  |
| EditorSettingsWindow | Self |  | EditorSettingsWindow |  |
| EditorSettingsWindow | Show |  | void |  |
| Election | AccessSelf |  | Election | 类别：常量 |
| Election | GetCountry |  | Country | 类别：非常量 |
| Election | GetCountryName |  | CString | 类别：非常量 |
| Election | GetDateFormatted |  | CString | 类别：非常量 |
| Election | GetEligibleVoters |  | int64 | 类别：非常量 |
| Election | GetIndependentIGs |  | Unknown | 类别：非常量 |
| Election | GetLastElectionDateDesc |  | CString | 类别：非常量 |
| Election | GetLastElectionYearRaw |  | int32 | 类别：非常量 |
| Election | GetNextElectionYearRaw |  | int32 | 类别：非常量 |
| Election | GetParties |  | Unknown | 类别：非常量 |
| Election | GetTitle |  | CString | 类别：非常量 |
| Election | GetTooltipTag |  | CString | 类别：非常量 |
| Election | GetTotalVoters |  | int64 | 类别：非常量 |
| Election | GetVoterTurnout |  | CFixedPoint | 类别：非常量 |
| Election | GetVotesGraphDateEnd |  | CString | 类别：非常量 |
| Election | GetVotesGraphDateStart |  | CString | 类别：非常量 |
| Election | GetVotesGraphMax |  | CFixedPoint | 类别：非常量 |
| Election | HasPreviousElection |  | bool |  |
| Election | IsInCampaignPeriod |  | bool |  |
| Election | Self |  | Election |  |
| ElectionPanel | AccessSelf |  | ElectionPanel | 类别：常量 |
| ElectionPanel | GetElection |  | Election | 类别：非常量 |
| ElectionPanel | Self |  | ElectionPanel |  |
| EmitterNodeWindow | AccessSelf |  | EmitterNodeWindow | 类别：常量 |
| EmitterNodeWindow | AddUserData | PdxGuiWidget | void |  |
| EmitterNodeWindow | GetNodeTitleColor |  | CVector4f | 类别：非常量 |
| EmitterNodeWindow | IsAnotherWindowIsolated |  | bool |  |
| EmitterNodeWindow | IsIsolated |  | bool |  |
| EmitterNodeWindow | IsVisuallyEnabled |  | bool |  |
| EmitterNodeWindow | Self |  | EmitterNodeWindow |  |
| EmitterNodeWindow | ToggleSetEmitterIsolatedExclusive |  | void |  |
| EmitterNodeWindow | ToggleSetEmitterIsolatedIncremental |  | void |  |
| EmitterNodeWindow | ToggleSetVisuallyEnabled |  | void |  |
| EmployeeTransfer | AccessSelf |  | EmployeeTransfer | 类别：常量 |
| EmployeeTransfer | GetIlliterate |  | int64 | 类别：非常量 |
| EmployeeTransfer | GetLiterate |  | int64 | 类别：非常量 |
| EmployeeTransfer | GetTooltipTag |  | CString | 类别：非常量 |
| EmployeeTransfer | GetTotal |  | int64 | 类别：非常量 |
| EmployeeTransfer | Self |  | EmployeeTransfer |  |
| Encyclopedia | AccessCurrentPage |  | EncyclopediaPage | 类别：常量 |
| Encyclopedia | AccessPages |  | Unknown | 类别：常量 |
| Encyclopedia | AccessSelf |  | Encyclopedia | 类别：常量 |
| Encyclopedia | CanFilterFromHistoryBack |  | bool |  |
| Encyclopedia | CanFilterFromHistoryForward |  | bool |  |
| Encyclopedia | FilterFromHistoryBack |  | void |  |
| Encyclopedia | FilterFromHistoryForward |  | void |  |
| Encyclopedia | GetAllPage |  | EncyclopediaPage | 类别：非常量 |
| Encyclopedia | GetCurrentPage |  | EncyclopediaPage | 类别：非常量 |
| Encyclopedia | GetPages |  | Unknown | 类别：非常量 |
| Encyclopedia | GetViewedEntries |  | Unknown | 类别：非常量 |
| Encyclopedia | Hide |  | void |  |
| Encyclopedia | IsShown |  | bool |  |
| Encyclopedia | Self |  | Encyclopedia |  |
| Encyclopedia | SetCurrentPage | EncyclopediaPage | void |  |
| Encyclopedia | ViewAllEntries |  | void |  |
| EncyclopediaEntry | AccessSelf |  | EncyclopediaEntry | 类别：常量 |
| EncyclopediaEntry | GetBody |  | CString | 类别：非常量 |
| EncyclopediaEntry | GetFrame |  | int32 | 类别：非常量 |
| EncyclopediaEntry | GetFrameSize |  | CVector2i | 类别：非常量 |
| EncyclopediaEntry | GetImage |  | Unknown | 类别：非常量 |
| EncyclopediaEntry | GetTitle |  | CString | 类别：非常量 |
| EncyclopediaEntry | HasImage |  | bool |  |
| EncyclopediaEntry | Self |  | EncyclopediaEntry |  |
| EncyclopediaEntryView | AccessSelf |  | EncyclopediaEntryView | 类别：常量 |
| EncyclopediaEntryView | Get |  | EncyclopediaEntry |  |
| EncyclopediaEntryView | Self |  | EncyclopediaEntryView |  |
| EncyclopediaPage | AccessSelf |  | EncyclopediaPage | 类别：常量 |
| EncyclopediaPage | FilterFromText |  | void |  |
| EncyclopediaPage | GetTitle |  | CString | 类别：非常量 |
| EncyclopediaPage | ResetFilter |  | void |  |
| EncyclopediaPage | SearchFromEnteredText |  | void |  |
| EncyclopediaPage | Self |  | EncyclopediaPage |  |
| EndPrepConfirm | AccessSelf |  | EndPrepConfirm | 类别：常量 |
| EndPrepConfirm | Cancel |  | void |  |
| EndPrepConfirm | Confirm |  | void |  |
| EndPrepConfirm | Self |  | EndPrepConfirm |  |
| EntityEditor | AccessSelf |  | EntityEditor | 类别：常量 |
| EntityEditor | AddAudioLayer |  | void |  |
| EntityEditor | AddEntityRemovalLayer |  | void |  |
| EntityEditor | AddEntitySpawnLayer |  | void |  |
| EntityEditor | AddKeyframeOnMouseToHoveredLane |  | void |  |
| EntityEditor | AddKeyframeOnNeedleToHoveredLane |  | void |  |
| EntityEditor | AddVfxLayer |  | void |  |
| EntityEditor | CanInteract |  | bool |  |
| EntityEditor | CurrentAnimationMax |  | float |  |
| EntityEditor | DeleteKeyframe | EntityEditorKeyframe | void |  |
| EntityEditor | Entity |  | ViewerEntity |  |
| EntityEditor | FitCamera |  | void |  |
| EntityEditor | GetLastAutoSaveDuration |  | double | 类别：非常量 |
| EntityEditor | GetLastAutoSaveTimestamp |  | Unknown | 类别：非常量 |
| EntityEditor | HasEntities |  | bool |  |
| EntityEditor | HasEntity |  | bool |  |
| EntityEditor | HasLastSaveTimestamp |  | bool |  |
| EntityEditor | IsAutoSaving |  | bool |  |
| EntityEditor | IsGridVisible |  | bool |  |
| EntityEditor | IsLoading |  | bool |  |
| EntityEditor | IsScrubbing |  | bool |  |
| EntityEditor | IsWorldMuted |  | bool |  |
| EntityEditor | MovePlayerWithKeyframe |  | bool |  |
| EntityEditor | OnAddLayerClick |  | void |  |
| EntityEditor | OnKeyframeClick | KeyframeWidget EntityEditorKeyframe | void |  |
| EntityEditor | OnKeyframeMove | KeyframeWidget EntityEditorKeyframe | void |  |
| EntityEditor | OnKeyframePressed | KeyframeWidget EntityEditorKeyframe | void |  |
| EntityEditor | OnKeyframeReleased | KeyframeWidget EntityEditorKeyframe | void |  |
| EntityEditor | OnKeyframeRightClick | EntityEditorKeyframe | void |  |
| EntityEditor | OnLayerRightClick | EntityEditorEventLayer | void |  |
| EntityEditor | OnScrubEnd |  | void |  |
| EntityEditor | OnScrubStart |  | void |  |
| EntityEditor | OpenEventEditor | EntityEditorKeyframe | void |  |
| EntityEditor | SaveChanges |  | void |  |
| EntityEditor | ScrubPlayer |  | void |  |
| EntityEditor | Self |  | EntityEditor |  |
| EntityEditor | SetClickedLane | EntityEditorEventLayer | void |  |
| EntityEditor | SetMovePlayerWithKeyframe | Unknown | void |  |
| EntityEditor | ToggleGridVisible |  | void |  |
| EntityEditor | ToggleMovePlayerWithKeyframe |  | void |  |
| EntityEditor | ToggleMuteWorld |  | void |  |
| EntityEditorAudioEventHandler | AccessSelf |  | EntityEditorAudioEventHandler | 类别：常量 |
| EntityEditorAudioEventHandler | AddSoundParamter | EntityEditorKeyframe | void |  |
| EntityEditorAudioEventHandler | RemoveLastSoundParameter | EntityEditorKeyframe | void |  |
| EntityEditorAudioEventHandler | Self |  | EntityEditorAudioEventHandler |  |
| EntityEditorEventLayer | AccessSelf |  | EntityEditorEventLayer | 类别：常量 |
| EntityEditorEventLayer | AddStartEventKeyframe | EntityEditor | void |  |
| EntityEditorEventLayer | HasKeyframes |  | bool |  |
| EntityEditorEventLayer | IsExpanded |  | bool |  |
| EntityEditorEventLayer | IsHovered |  | bool |  |
| EntityEditorEventLayer | Keyframes |  | Unknown |  |
| EntityEditorEventLayer | Self |  | EntityEditorEventLayer |  |
| EntityEditorEventLayer | SetHovered | bool | void |  |
| EntityEditorEventLayer | Title |  | Unknown |  |
| EntityEditorEventLayer | ToggleExpanded |  | void |  |
| EntityEditorKeyframe | AccessSelf |  | EntityEditorKeyframe | 类别：常量 |
| EntityEditorKeyframe | HasEvent |  | bool |  |
| EntityEditorKeyframe | IsHovered |  | bool |  |
| EntityEditorKeyframe | IsSelected |  | bool |  |
| EntityEditorKeyframe | IsStartEvent |  | bool |  |
| EntityEditorKeyframe | KeyframeColor |  | CVector4f |  |
| EntityEditorKeyframe | Label |  | CString |  |
| EntityEditorKeyframe | Self |  | EntityEditorKeyframe |  |
| EntityEditorKeyframe | SetHovered | Unknown | void |  |
| EntityEditorKeyframe | SetSelected | Unknown | void |  |
| EntityEditorKeyframe | TimePoint |  | float |  |
| EntityEditorTimelineState | AccessSelf |  | EntityEditorTimelineState | 类别：常量 |
| EntityEditorTimelineState | AnimationLength |  | float |  |
| EntityEditorTimelineState | KeyframeLayers |  | Unknown |  |
| EntityEditorTimelineState | Name |  | Unknown |  |
| EntityEditorTimelineState | Self |  | EntityEditorTimelineState |  |
| EntityViewerProperties | AccessSelf |  | EntityViewerProperties | 类别：常量 |
| EntityViewerProperties | ClearSelection |  | void |  |
| EntityViewerProperties | IsBloomEvPropertiesVisible |  | bool |  |
| EntityViewerProperties | IsCubemapEvPropertiesVisible |  | bool |  |
| EntityViewerProperties | IsEnvSelected |  | bool |  |
| EntityViewerProperties | IsFogEvPropertiesVisible |  | bool |  |
| EntityViewerProperties | IsLightEnvPropertiesVisible |  | bool |  |
| EntityViewerProperties | IsMeshSelected |  | bool |  |
| EntityViewerProperties | SelectEnvWindow |  | void |  |
| EntityViewerProperties | SelectMeshWindow |  | void |  |
| EntityViewerProperties | Self |  | EntityViewerProperties |  |
| EntityViewerProperties | ToggleIsBloomEvPropertiesVisible |  | void |  |
| EntityViewerProperties | ToggleIsCubemapEvPropertiesVisible |  | void |  |
| EntityViewerProperties | ToggleIsFogEvPropertiesVisible |  | void |  |
| EntityViewerProperties | ToggleIsLightEvPropertiesVisible |  | void |  |
| EnumSettingEntry | AccessSelf |  | EnumSettingEntry | 类别：常量 |
| EnumSettingEntry | AccessSetting |  | Unknown | 类别：常量 |
| EnumSettingEntry | GetEnumString |  | CString | 类别：非常量 |
| EnumSettingEntry | GetGUIName |  | CUTF8String | 类别：非常量 |
| EnumSettingEntry | GetRecommendedText |  | CString | 类别：非常量 |
| EnumSettingEntry | GetTooltip |  | CUTF8String | 类别：非常量 |
| EnumSettingEntry | HasValueChanged |  | bool |  |
| EnumSettingEntry | IsSelected |  | bool |  |
| EnumSettingEntry | Self |  | EnumSettingEntry |  |
| Era | AccessSelf |  | Era | 类别：常量 |
| Era | GetName |  | CString | 类别：非常量 |
| Era | GetNumber |  | CString | 类别：非常量 |
| Era | GetTechnologyCost |  | int32 | 类别：非常量 |
| Era | GetTooltipTag |  | CString | 类别：非常量 |
| Era | Self |  | Era |  |
| ErrorDeer | AccessSelf |  | ErrorDeer | 类别：常量 |
| ErrorDeer | GetTooltip |  | CString | 类别：非常量 |
| ErrorDeer | HasErrors |  | bool |  |
| ErrorDeer | HasSlowTicks |  | bool |  |
| ErrorDeer | NumberOrErrors |  | int32 |  |
| ErrorDeer | OpenErrorLog |  | void |  |
| ErrorDeer | Self |  | ErrorDeer |  |
| Ethnicity | AccessSelf |  | Ethnicity | 类别：常量 |
| Ethnicity | GetName |  | CString | 类别：非常量 |
| Ethnicity | IsVisible |  | bool |  |
| Ethnicity | Self |  | Ethnicity |  |
| EthnicityItem | AccessSelf |  | EthnicityItem | 类别：常量 |
| EthnicityItem | GetName |  | CString | 类别：非常量 |
| EthnicityItem | Self |  | EthnicityItem |  |
| Event | AccessSelf |  | Event | 类别：常量 |
| Event | AccessState |  | State | 类别：常量 |
| Event | GetDLCIcon |  | Unknown | 类别：非常量 |
| Event | GetDLCName |  | CString | 类别：非常量 |
| Event | GetDescription |  | CString | 类别：非常量 |
| Event | GetEventIcon |  | Unknown | 类别：非常量 |
| Event | GetFlavor |  | CString | 类别：非常量 |
| Event | GetKey |  | CString | 类别：非常量 |
| Event | GetNumRemainingDays |  | int32 | 类别：非常量 |
| Event | GetOnCreatedSoundEvent |  | Unknown | 类别：非常量 |
| Event | GetOnOpenedSoundEvent |  | Unknown | 类别：非常量 |
| Event | GetPercentageRemainingDays |  | float | 类别：非常量 |
| Event | GetRemainingDays |  | CString | 类别：非常量 |
| Event | GetState |  | State | 类别：非常量 |
| Event | GetTexture |  | Unknown | 类别：非常量 |
| Event | GetTitle |  | CString | 类别：非常量 |
| Event | GetTooltip |  | CString | 类别：非常量 |
| Event | GetTooltipTag |  | CString | 类别：非常量 |
| Event | GetTriggerDesc |  | CString | 类别：非常量 |
| Event | GetVideo |  | CString | 类别：非常量 |
| Event | HasCategory | CString | bool |  |
| Event | HasTexture |  | bool |  |
| Event | HasVideo |  | bool |  |
| Event | IsDLCContent |  | bool |  |
| Event | OpenInEditor |  | void |  |
| Event | Self |  | Event |  |
| EventIcon | AccessSelf |  | EventIcon | 类别：常量 |
| EventIcon | GetTexture |  | Unknown | 类别：非常量 |
| EventIcon | IsCoatOfArms |  | bool |  |
| EventIcon | IsPortrait |  | bool |  |
| EventIcon | IsTexture |  | bool |  |
| EventIcon | IsVisible |  | bool |  |
| EventIcon | Self |  | EventIcon |  |
| EventLayerForEntityEditor | AccessSelf |  | EventLayerForEntityEditor | 类别：常量 |
| EventLayerForEntityEditor | HasKeyframes |  | bool |  |
| EventLayerForEntityEditor | IsHovered |  | bool |  |
| EventLayerForEntityEditor | Keyframes |  | Unknown |  |
| EventLayerForEntityEditor | Self |  | EventLayerForEntityEditor |  |
| EventLayerForEntityEditor | SetHovered | Unknown | void |  |
| EventMarker | AccessAnyEvent |  | Event | 类别：常量 |
| EventMarker | AccessSelf |  | EventMarker | 类别：常量 |
| EventMarker | GetAnyEvent |  | Event | 类别：非常量 |
| EventMarker | GetPosition |  | CVector2f | 类别：非常量 |
| EventMarker | GetTexture |  | Unknown | 类别：非常量 |
| EventMarker | Self |  | EventMarker |  |
| EventMarkerListItem | AccessSelf |  | EventMarkerListItem | 类别：常量 |
| EventMarkerListItem | GetDescription |  | CString | 类别：非常量 |
| EventMarkerListItem | Self |  | EventMarkerListItem |  |
| EventOption | AccessSelf |  | EventOption | 类别：常量 |
| EventOption | GetDesc |  | CString | 类别：非常量 |
| EventOption | GetText |  | CString | 类别：非常量 |
| EventOption | IsDefaultOption |  | bool |  |
| EventOption | IsEnabled |  | bool |  |
| EventOption | IsHighlightedOption |  | bool |  |
| EventOption | Select |  | void |  |
| EventOption | Self |  | EventOption |  |
| EventTargetSetupContext | AccessSelf |  | EventTargetSetupContext | 类别：常量 |
| EventTargetSetupContext | Self |  | EventTargetSetupContext |  |
| EventWindow | AccessEvent |  | Event | 类别：常量 |
| EventWindow | AccessSelf |  | EventWindow | 类别：常量 |
| EventWindow | GetDescription |  | CString | 类别：非常量 |
| EventWindow | GetEvent |  | Event | 类别：非常量 |
| EventWindow | GetFlavor |  | CString | 类别：非常量 |
| EventWindow | GetOptions |  | Unknown | 类别：非常量 |
| EventWindow | GetTitle |  | CString | 类别：非常量 |
| EventWindow | GetTitleTooltip |  | CString | 类别：非常量 |
| EventWindow | Self |  | EventWindow |  |
| ExilePool | AccessSelf |  | ExilePool | 类别：常量 |
| ExilePool | GetAllExiles |  | Unknown | 类别：非常量 |
| ExilePool | GetExiles |  | Unknown | 类别：nonconst |
| ExilePool | GetNumInviteableExiles |  | int32 | 类别：nonconst |
| ExilePool | IsInterestGroupFiltered | InterestGroup | bool |  |
| ExilePool | IsInterestGroupFilteredToShowOnly | InterestGroup | bool |  |
| ExilePool | IsSorted | Unknown | bool |  |
| ExilePool | Self |  | ExilePool |  |
| ExilePool | SetInterestGroupFilter | InterestGroup | void |  |
| ExilePool | Sort | CString | void |  |
| ExilePool | ToggleInterestGroupFilter | InterestGroup | void |  |
| ExportTool | AccessSelf |  | ExportTool | 类别：const |
| ExportTool | CanExport |  | bool |  |
| ExportTool | Cancel |  | void |  |
| ExportTool | CurrentProgress |  | float |  |
| ExportTool | CurrentProgressDesc |  | CString |  |
| ExportTool | Export |  | void |  |
| ExportTool | GetHeightmapTexture |  | Unknown | 类别：nonconst |
| ExportTool | GetMaskEffect |  | Unknown | 类别：nonconst |
| ExportTool | GetNotes |  | CString | 类别：nonconst |
| ExportTool | GetSelectedMaskIndex |  | CVector2i | 类别：nonconst |
| ExportTool | GetTexture |  | Unknown | 类别：nonconst |
| ExportTool | HasMasks |  | bool |  |
| ExportTool | IsExporting |  | bool |  |
| ExportTool | MaxProgress |  | float |  |
| ExportTool | Refresh |  | void |  |
| ExportTool | Self |  | ExportTool |  |
| ExportTool | SetExportNotes |  | void |  |
| ExportTool | SetSelectedMaskIndex |  | void |  |
| EyeDropper | AccessSelf |  | EyeDropper | 类别：const |
| EyeDropper | IsEnabled |  | bool |  |
| EyeDropper | PackedSamples |  | Unknown |  |
| EyeDropper | PackedSamplesDynamic |  | Unknown |  |
| EyeDropper | Self |  | EyeDropper |  |
| EyeDropper | SetEnabled | bool | void |  |
| EyeDropperPackedSample | AccessSelf |  | EyeDropperPackedSample | 类别：const |
| EyeDropperPackedSample | GetChannel |  | CString | 类别：nonconst |
| EyeDropperPackedSample | Self |  | EyeDropperPackedSample |  |
| FeedMessageItem | AccessSelf |  | FeedMessageItem | 类别：const |
| FeedMessageItem | ClickedExpand |  | bool |  |
| FeedMessageItem | ClickedExpandFinished |  | void |  |
| FeedMessageItem | ClickedHide |  | bool |  |
| FeedMessageItem | ClickedHideFinished |  | void |  |
| FeedMessageItem | Delete |  | void |  |
| FeedMessageItem | EndAnimation |  | void |  |
| FeedMessageItem | Expand |  | void |  |
| FeedMessageItem | GetPlayerMessageItem |  | PlayerMessageItem | 类别：nonconst |
| FeedMessageItem | GetTimeoutTimer |  | PieTimer | 类别：nonconst |
| FeedMessageItem | IsExpanded |  | bool |  |
| FeedMessageItem | IsSetToDelete |  | bool |  |
| FeedMessageItem | IsToggled |  | bool |  |
| FeedMessageItem | MarkToDelete |  | void |  |
| FeedMessageItem | Self |  | FeedMessageItem |  |
| FeedMessageItem | ShouldHide |  | bool |  |
| FeedMessageItem | ShouldShow |  | bool |  |
| FeedMessageItem | StartAnimation |  | void |  |
| FilterablePropertyList | AccessSelf |  | FilterablePropertyList | 类别：const |
| FilterablePropertyList | ClearSearchText |  | void |  |
| FilterablePropertyList | Filter |  | void |  |
| FilterablePropertyList | GetPropertiesLabel |  | CString | 类别：nonconst |
| FilterablePropertyList | GetSearchText |  | CString | 类别：nonconst |
| FilterablePropertyList | Search |  | void |  |
| FilterablePropertyList | Self |  | FilterablePropertyList |  |
| FoodSecurity | AccessSelf |  | FoodSecurity | 类别：const |
| FoodSecurity | GetNumPopsTotal |  | int64 | 类别：nonconst |
| FoodSecurity | GetNumStarvingPops |  | int64 | 类别：nonconst |
| FoodSecurity | GetNumStarvingPopsMild |  | int64 | 类别：nonconst |
| FoodSecurity | GetNumStarvingPopsSevere |  | int64 | 类别：nonconst |
| FoodSecurity | GetNumStatesWithFamineFormatted |  | CString | 类别：nonconst |
| FoodSecurity | GetNumStatesWithFamineRaw |  | int32 | 类别：nonconst |
| FoodSecurity | GetPercentageStarvingPops |  | CFixedPoint | 类别：nonconst |
| FoodSecurity | GetPercentageStarvingPopsMild |  | CFixedPoint | 类别：nonconst |
| FoodSecurity | GetPercentageStarvingPopsSevere |  | CFixedPoint | 类别：nonconst |
| FoodSecurity | GetStarvationTypePopulation | StarvationType | int64 | 类别：nonconst |
| FoodSecurity | GetStarvationTypePopulationAsFloat | Unknown | float | 类别：nonconst |
| FoodSecurity | GetStarvationTypePopulationAsPercentage | StarvationType | CFixedPoint | 类别：nonconst |
| FoodSecurity | HasFamine |  | bool |  |
| FoodSecurity | Self |  | FoodSecurity |  |

| 类型 | 函数 | 参数 | 输出 | 描述 |
|---|---|---|---|---|
| FoodSecurityFilter | AccessSelf |  | FoodSecurityFilter | 类别：const |
| FoodSecurityFilter | GetStates |  | Unknown | 类别：nonconst |
| FoodSecurityFilter | HasSpecificCountry |  | bool |  |
| FoodSecurityFilter | HasSpecificState |  | bool |  |
| FoodSecurityFilter | IsCountrySelected | Unknown | bool |  |
| FoodSecurityFilter | IsStateSelected | Unknown | bool |  |
| FoodSecurityFilter | ResetCountryFilter |  | void |  |
| FoodSecurityFilter | ResetStateFilter |  | void |  |
| FoodSecurityFilter | Self |  | FoodSecurityFilter |  |
| FoodSecurityFilter | SetCountryFilter | Unknown | void |  |
| FoodSecurityFilter | SetStateFilter | Unknown | void |  |
| FormationMarker | AccessSelf |  | FormationMarker | 类别：const |
| FormationMarker | CalcAverageAvailableDefense |  | CFixedPoint |  |
| FormationMarker | CalcAverageAvailableOffense |  | CFixedPoint |  |
| FormationMarker | CalcAverageMorale |  | CFixedPoint |  |
| FormationMarker | CalcAverageOrganizationPercentage |  | CFixedPoint |  |
| FormationMarker | CalcCurrentManpower |  | int64 |  |
| FormationMarker | CalcMaxManpower |  | int64 |  |
| FormationMarker | CalcTotalNumCombatUnits |  | int32 |  |
| FormationMarker | GetCombatUnitsTypeIcon |  | CString | 类别：nonconst |
| FormationMarker | GetDefenseTooltip |  | CString | 类别：nonconst |
| FormationMarker | GetFormations |  | Unknown | 类别：nonconst |
| FormationMarker | GetManpowerTooltip |  | CString | 类别：nonconst |
| FormationMarker | GetMoraleTooltip |  | CString | 类别：nonconst |
| FormationMarker | GetOffenseTooltip |  | CString | 类别：nonconst |
| FormationMarker | GetOrganizationTooltip |  | CString | 类别：nonconst |
| FormationMarker | GetPosition |  | CVector2f | 类别：nonconst |
| FormationMarker | GetPositionDesc |  | CString | 类别：nonconst |
| FormationMarker | GetSummaryTooltip |  | CString | 类别：nonconst |
| FormationMarker | HasMultipleFormations |  | bool |  |
| FormationMarker | IsAnyFormationHighlighted |  | bool |  |
| FormationMarker | IsAnyFormationTraveling |  | bool |  |
| FormationMarker | IsArmy |  | bool |  |
| FormationMarker | IsEnemies |  | bool |  |
| FormationMarker | IsFleet |  | bool |  |
| FormationMarker | OnCtrlClick |  | void |  |
| FormationMarker | OnLeftClick |  | void |  |
| FormationMarker | OnRightClick |  | void |  |
| FormationMarker | OnShiftClick |  | void |  |
| FormationMarker | Self |  | FormationMarker |  |
| FormationPanel | AccessCommanderOrdersPossibleForSelectedFormations |  | Unknown | 类别：const |
| FormationPanel | AccessSelf |  | FormationPanel | 类别：const |
| FormationPanel | GetFormation |  | MilitaryFormation | 类别：nonconst |
| FormationPanel | GetSelectedFormations |  | Unknown | 类别：nonconst |
| FormationPanel | HasSelectionView |  | bool |  |
| FormationPanel | SelectFormation | Unknown | void |  |
| FormationPanel | Self |  | FormationPanel |  |
| Friend | AccessSelf |  | Friend | 类别：const |
| Friend | GetAvailabilityString |  | CUTF8String | 类别：nonconst |
| Friend | GetName |  | CUTF8String | 类别：nonconst |
| Friend | GetNameWithColor |  | CUTF8String | 类别：nonconst |
| Friend | GetUnreadMessageCount |  | int32 | 类别：nonconst |
| Friend | HasUnreadMessages |  | bool |  |
| Friend | RemoveWithConfirmation |  | void |  |
| Friend | Self |  | Friend |  |
| Friend | StartChat |  | void |  |
| FriendListWindow | AccessSelf |  | FriendListWindow | 类别：const |
| FriendListWindow | Hide |  | void |  |
| FriendListWindow | Self |  | FriendListWindow |  |
| FriendListWindow | ShouldBeShown |  | bool |  |
| FriendListWindow | Show |  | void |  |
| FriendListWindow | ShowAddFriendWindow |  | void |  |
| FriendRequest | Accept |  | void |  |
| FriendRequest | AccessSelf |  | FriendRequest | 类别：const |
| FriendRequest | GetName |  | CUTF8String | 类别：nonconst |
| FriendRequest | Reject |  | void |  |
| FriendRequest | Self |  | FriendRequest |  |
| FriendSearchResult | AccessSelf |  | FriendSearchResult | 类别：const |
| FriendSearchResult | AddFriend |  | void |  |
| FriendSearchResult | GetName |  | CUTF8String | 类别：nonconst |
| FriendSearchResult | Self |  | FriendSearchResult |  |
| Friends | AccessAvailabilityEntries |  | Unknown | 类别：const |
| Friends | AccessFriendRequests |  | Unknown | 类别：const |
| Friends | AccessFriendSearchResults |  | Unknown | 类别：const |
| Friends | AccessFriends |  | Unknown | 类别：const |
| Friends | AccessOutgoingFriendRequests |  | Unknown | 类别：const |
| Friends | AccessSelf |  | Friends | 类别：const |
| Friends | CalcNumberOfOnlineFriends |  | int32 |  |
| Friends | GetAvailabilityStringForLocalAccount |  | CUTF8String | 类别：nonconst |
| Friends | GetLocalProfileName |  | CUTF8String | 类别：nonconst |
| Friends | GetSearchString |  | CUTF8String | 类别：nonconst |
| Friends | GetSelectedAvailabilityEntryIndex |  | CVector2i | 类别：nonconst |
| Friends | HasIngoingFriendRequests |  | bool |  |
| Friends | HasOutgoingFriendRequests |  | bool |  |
| Friends | Search |  | void |  |
| Friends | Self |  | Friends |  |
| Friends | SetSearchString |  | void |  |
| Friends | SetSelectedAvailabilityEntryIndex |  | void |  |
| Friends | UpdateFriends |  | void |  |
| Front | AccessActiveBattles |  | Unknown | 类别：const |
| Front | AccessAllBattles |  | Unknown | 类别：const |
| Front | AccessDiplomaticPlay |  | DiplomaticPlay | 类别：const |
| Front | AccessEndedBattles |  | Unknown | 类别：const |
| Front | AccessSelf |  | Front | 类别：const |
| Front | GetAdvantageFrame |  | int32 | 类别：nonconst |
| Front | GetCustom | CustomLocalization | CString | 类别：nonconst |
| Front | GetDeploySelectedFormationsCommand |  | Command | 类别：nonconst |
| Front | GetDesc |  | CString | 类别：nonconst |
| Front | GetID |  | uint32 | 类别：nonconst |
| Front | GetInitiatorTheatersDebugDesc |  | CString | 类别：nonconst |
| Front | GetName |  | CString | 类别：nonconst |
| Front | GetNameFromPerspective |  | CString | 类别：nonconst |
| Front | GetNameNoFormatting |  | CString | 类别：nonconst |
| Front | GetPlayerAdvantageDesc |  | CString | 类别：nonconst |
| Front | GetPlayerAdvantageRaw |  | int32 | 类别：nonconst |
| Front | GetPlayerSideAlliesCombatUnitsBreakdown |  | CString | 类别：nonconst |
| Front | GetPlayerSideAlliesCombatUnitsTravelingBreakdown |  | CString | 类别：nonconst |
| Front | GetPlayerSideCombatUnitsBreakdown |  | CString | 类别：nonconst |
| Front | GetPlayerSideCombatUnitsTravelingBreakdown |  | CString | 类别：nonconst |
| Front | GetPlayerSideNumUnitsAtFront |  | int32 | 类别：nonconst |
| Front | GetPlayerSideNumUnitsTraveling |  | int32 | 类别：nonconst |
| Front | GetPlayerSideUnitsTooltip |  | CString | 类别：nonconst |
| Front | GetRequiredAdvanceProgressForBattle |  | CFixedPoint | 类别：nonconst |
| Front | GetTargetTheatersDebugDesc |  | CString | 类别：nonconst |
| Front | GetTooltipTag |  | CString | 类别：nonconst |
| Front | HasCountry | Country | bool |  |
| Front | IsBeingHighlighted |  | bool |  |
| Front | IsBeingTutorialHighlighted |  | bool |  |
| Front | IsValid |  | bool |  |
| Front | IsVulnerable | Country | bool |  |
| Front | IsZoomingToFront |  | bool |  |
| Front | MakeScope |  | Scope |  |
| Front | Self |  | Front |  |
| Front | ZoomToFront |  | void |  |
| FrontEndCreditsView | AccessSelf |  | FrontEndCreditsView | 类别：const |
| FrontEndCreditsView | OnBack |  | void |  |
| FrontEndCreditsView | Self |  | FrontEndCreditsView |  |
| FrontEndLoadConfirmationWindow | AccessSelf |  | FrontEndLoadConfirmationWindow | 类别：const |
| FrontEndLoadConfirmationWindow | AnswerNo |  | void |  |
| FrontEndLoadConfirmationWindow | AnswerYes |  | void |  |
| FrontEndLoadConfirmationWindow | GetDesc |  | CString | 类别：nonconst |
| FrontEndLoadConfirmationWindow | Self |  | FrontEndLoadConfirmationWindow |  |
| FrontEndLoadView | AccessSelf |  | FrontEndLoadView | 类别：const |
| FrontEndLoadView | CanDoContinue |  | bool |  |
| FrontEndLoadView | GetContinueSave |  | SaveGameItem | 类别：nonconst |
| FrontEndLoadView | GetSaveGames |  | Unknown | 类别：nonconst |
| FrontEndLoadView | GetSelectedSavegame |  | SaveGameItem | 类别：nonconst |
| FrontEndLoadView | HasSelectedSavegame |  | bool |  |
| FrontEndLoadView | IsEmpty |  | bool |  |
| FrontEndLoadView | OnBack |  | void |  |
| FrontEndLoadView | OnConfirmContinue | CString | void |  |
| FrontEndLoadView | OnContinue |  | void |  |
| FrontEndLoadView | OnDelete |  | void |  |
| FrontEndLoadView | OnDeleteAll |  | void |  |
| FrontEndLoadView | OnIncompatibleLoadConfirm |  | void |  |
| FrontEndLoadView | OnIncompatibleLoadDeny |  | void |  |
| FrontEndLoadView | OnLoad |  | void |  |
| FrontEndLoadView | OnShowInvalidSavegames |  | void |  |
| FrontEndLoadView | PreContinueSaveCheck |  | void |  |
| FrontEndLoadView | Self |  | FrontEndLoadView |  |
| FrontEndLoadView | ShouldShowInvalidSavegames |  | bool |  |
| FrontEndMainView | AccessLoadView |  | FrontEndLoadView | 类别：const |
| FrontEndMainView | AccessSelf |  | FrontEndMainView | 类别：const |
| FrontEndMainView | GetMainMenuImage |  | CString | 类别：nonconst |
| FrontEndMainView | OnCredits |  | void |  |
| FrontEndMainView | OnHost |  | void |  |
| FrontEndMainView | OnLoad |  | void |  |
| FrontEndMainView | OnLogin |  | void |  |
| FrontEndMainView | OnMultiPlayer |  | void |  |
| FrontEndMainView | OnNewGame |  | void |  |
| FrontEndMainView | OnQuit |  | void |  |
| FrontEndMainView | OnSettings |  | void |  |
| FrontEndMainView | Self |  | FrontEndMainView |  |
| FrontEndMultiplayerView | AccessSelf |  | FrontEndMultiplayerView | 类别：const |
| FrontEndMultiplayerView | OnBack |  | void |  |
| FrontEndMultiplayerView | OnHost |  | void |  |
| FrontEndMultiplayerView | OnLoad |  | void |  |
| FrontEndMultiplayerView | OnNewGame |  | void |  |
| FrontEndMultiplayerView | Self |  | FrontEndMultiplayerView |  |
| FrontMarker | AccessSelf |  | FrontMarker | 类别：const |
| FrontMarker | GetPosition |  | CVector2f | 类别：nonconst |
| FrontMarker | OnClick |  | void |  |
| FrontMarker | Self |  | FrontMarker |  |
| FrontMovementMarker | AccessFront |  | Front | 类别：const |
| FrontMovementMarker | AccessSelf |  | FrontMovementMarker | 类别：const |
| FrontMovementMarker | CanDeploySelectedFormationsToFront |  | bool |  |
| FrontMovementMarker | GetFront |  | Front | 类别：nonconst |
| FrontMovementMarker | GetPosition |  | CVector2f | 类别：nonconst |
| FrontMovementMarker | GetPresentFormationsBreakdown |  | CString | 类别：nonconst |
| FrontMovementMarker | GetTravelTimeBreakdown |  | CString | 类别：nonconst |
| FrontMovementMarker | IsAllSelectedFormationsLocation |  | bool |  |
| FrontMovementMarker | IsAllSelectedFormationsTarget |  | bool |  |
| FrontMovementMarker | IsAnySelectedFormationsLocation |  | bool |  |
| FrontMovementMarker | IsAnySelectedFormationsTarget |  | bool |  |
| FrontMovementMarker | Self |  | FrontMovementMarker |  |
| FrontPanel | AccessFront |  | Front | 类别：const |
| FrontPanel | AccessSelf |  | FrontPanel | 类别：const |
| FrontPanel | GetFront |  | Front | 类别：nonconst |
| FrontPanel | IsShowingBattles |  | bool |  |
| FrontPanel | Self |  | FrontPanel |  |
| FrontPanel | ToggleShowPastBattles |  | void |  |
| FrontSide | AccessSelf |  | FrontSide | 类别：const |
| FrontSide | GetAdvancement |  | CFixedPoint | 类别：nonconst |
| FrontSide | GetAdvancementProgress |  | CFixedPoint | 类别：nonconst |
| FrontSide | GetAdvantage |  | int32 | 类别：nonconst |
| FrontSide | GetAdvantageDesc |  | CString | 类别：nonconst |
| FrontSide | GetAdvantageFrame |  | int32 | 类别：nonconst |
| FrontSide | GetArmies |  | Unknown | 类别：nonconst |
| FrontSide | GetCountries |  | Unknown | 类别：nonconst |
| FrontSide | GetCountry |  | Country | 类别：nonconst |
| FrontSide | GetNumCasualties | Country | int64 | 类别：nonconst |
| FrontSide | GetNumDead | Country | int64 | 类别：nonconst |
| FrontSide | GetNumUnits |  | int32 | 类别：nonconst |
| FrontSide | GetNumUnitsBreakdown |  | CString | 类别：nonconst |
| FrontSide | GetNumWounded | Country | int64 | 类别：nonconst |
| FrontSide | GetOutsideTopFiveArmies |  | Unknown | 类别：nonconst |
| FrontSide | GetOutsideTopFiveArmiesTooltip |  | CString | 类别：nonconst |
| FrontSide | GetTopFiveArmies |  | Unknown | 类别：nonconst |
| FrontSide | GetTotalNumCasualties |  | int64 | 类别：nonconst |
| FrontSide | GetTotalNumDead |  | int64 | 类别：nonconst |
| FrontSide | GetTotalNumWounded |  | int64 | 类别：nonconst |
| FrontSide | GetUnitDefense |  | CFixedPoint | 类别：nonconst |
| FrontSide | GetUnitMorale |  | CFixedPoint | 类别：nonconst |
| FrontSide | GetUnitMoraleDesc |  | CString | 类别：nonconst |
| FrontSide | GetUnitOffense |  | CFixedPoint | 类别：nonconst |
| FrontSide | HasCountry | Unknown | bool |  |
| FrontSide | IsInitiatorSide |  | bool |  |
| FrontSide | IsTargetSide |  | bool |  |
| FrontSide | Self |  | FrontSide |  |
| GUIAchievement | AccessLockedTexture |  | Unknown | 类别：const |
| GUIAchievement | AccessSelf |  | GUIAchievement | 类别：const |
| GUIAchievement | AccessTexture |  | Unknown | 类别：const |
| GUIAchievement | GetAchievement |  | Achievement | 类别：nonconst |
| GUIAchievement | GetDescription |  | CUTF8String | 类别：nonconst |
| GUIAchievement | GetHappenedDescription |  | CUTF8String | 类别：nonconst |
| GUIAchievement | GetName |  | CUTF8String | 类别：nonconst |
| GUIAchievement | IsPossible |  | bool |  |
| GUIAchievement | OnClick |  | void |  |
| GUIAchievement | Remove |  | void |  |
| GUIAchievement | Self |  | GUIAchievement |  |
| GameConceptType | AccessSelf |  | GameConceptType | 类别：const |
| GameConceptType | CanStartTutorialLesson |  | bool |  |
| GameConceptType | CanStartTutorialLessonDesc |  | CString |  |
| GameConceptType | GetDesc |  | CString | 类别：nonconst |
| GameConceptType | GetDescNoFormatting |  | CString | 类别：nonconst |
| GameConceptType | GetName |  | CString | 类别：nonconst |
| GameConceptType | GetNameNoFormatting |  | CString | 类别：nonconst |
| GameConceptType | GetTexture |  | Unknown | 类别：nonconst |
| GameConceptType | GetTitle |  | CString | 类别：nonconst |
| GameConceptType | GetTooltipTag |  | CString | 类别：nonconst |
| GameConceptType | HasTutorialLesson |  | bool |  |
| GameConceptType | Self |  | GameConceptType |  |
| GameConceptType | StartTutorialLesson |  | void |  |
| GameMpSetup | AccessSelf |  | GameMpSetup | 类别：const |
| GameMpSetup | CanStart |  | bool |  |
| GameMpSetup | GetEnabledDLCs |  | Unknown | 类别：nonconst |
| GameMpSetup | GetEnabledMods |  | Unknown | 类别：nonconst |
| GameMpSetup | GetSaveGames |  | Unknown | 类别：nonconst |
| GameMpSetup | GetSelectedSaveGame |  | SaveGameItem | 类别：nonconst |
| GameMpSetup | IsAutoAccept |  | bool |  |
| GameMpSetup | IsBookmarkSelected |  | bool |  |
| GameMpSetup | IsInvite |  | bool |  |
| GameMpSetup | IsPublicCrossplay |  | bool |  |
| GameMpSetup | IsPublicNoCrossplay |  | bool |  |
| GameMpSetup | IsSaveGameSelected |  | bool |  |
| GameMpSetup | OnBack |  | void |  |
| GameMpSetup | OnDelete |  | void |  |
| GameMpSetup | OnShowInvalidSavegames |  | void |  |
| GameMpSetup | OnStart |  | void |  |
| GameMpSetup | SelectBookmark |  | void |  |
| GameMpSetup | Self |  | GameMpSetup |  |
| GameMpSetup | SetVisibilityInvite |  | void |  |
| GameMpSetup | SetVisibilityPublicCrossplay |  | void |  |
| GameMpSetup | SetVisibilityPublicNoCrossplay |  | void |  |
| GameMpSetup | ShouldShowInvalidSavegames |  | bool |  |
| GameMpSetup | StartTooltip |  | CString |  |
| GameMpSetup | ToggleAutoAccept |  | void |  |
| GameMpSetup | ToggleVisibility |  | void |  |
| GameOverScreen | AccessSelf |  | GameOverScreen | 类别：const |
| GameOverScreen | CanContinueAsObserver |  | bool |  |
| GameOverScreen | CanGoToLobby |  | bool |  |
| GameOverScreen | CanLoadGame |  | bool |  |
| GameOverScreen | ContinueAsObserver |  | void |  |
| GameOverScreen | GetGameOverDateString |  | CString | 类别：nonconst |
| GameOverScreen | GetGameOverSoundEvent |  | Unknown | 类别：nonconst |
| GameOverScreen | GetLoadGameDesc |  | CString | 类别：nonconst |
| GameOverScreen | GetQuitName |  | CString | 类别：nonconst |
| GameOverScreen | GoToLobby |  | void |  |
| GameOverScreen | OpenLoadView |  | void |  |
| GameOverScreen | Quit |  | void |  |
| GameOverScreen | Self |  | GameOverScreen |  |
| GameRule | AccessSelf |  | GameRule | 类别：const |
| GameRule | GetName |  | CString | 类别：nonconst |
| GameRule | GetSettings |  | Unknown | 类别：nonconst |
| GameRule | Self |  | GameRule |  |
| GameRuleSetting | AccessSelf |  | GameRuleSetting | 类别：const |
| GameRuleSetting | GetDescription |  | CString | 类别：nonconst |
| GameRuleSetting | GetDescriptionWithObjectiveRecommendation |  | CString | 类别：nonconst |
| GameRuleSetting | GetKey |  | CString | 类别：nonconst |
| GameRuleSetting | GetName |  | CString | 类别：nonconst |
| GameRuleSetting | HasFlag | CString | bool |  |
| GameRuleSetting | Self |  | GameRuleSetting |  |
| GameSetup | AccessSelf |  | GameSetup | 类别：const |
| GameSetup | GetCustomRNGSeed |  | CString | 类别：nonconst |
| GameSetup | GetObjectives |  | Unknown | 类别：nonconst |
| GameSetup | GetSelectedObjective |  | ObjectiveType | 类别：nonconst |
| GameSetup | GetSelectedTag |  | CountryDefinition | 类别：nonconst |
| GameSetup | HasSelectedObjective |  | bool |  |
| GameSetup | HasSelectedTag |  | bool |  |
| GameSetup | OnBack |  | void |  |
| GameSetup | OnEditRNGSeed |  | void |  |
| GameSetup | OnStart |  | void |  |
| GameSetup | Self |  | GameSetup |  |
| GameSetup | ToggleObjective | ObjectiveType | void |  |
| GameSetup | ToggleTag | CountryDefinition | void |  |
| GeneCategory | AccessSelf |  | GeneCategory | 类别：const |
| GeneCategory | GetName |  | CString | 类别：nonconst |
| GeneCategory | IsType | Unknown | bool |  |
| GeneCategory | Self |  | GeneCategory |  |
| GeneItem | AccessSelf |  | GeneItem | 类别：const |
| GeneItem | GetName |  | CString | 类别：nonconst |
| GeneItem | Self |  | GeneItem |  |
| GeneTemplate | AccessSelf |  | GeneTemplate | 类别：const |
| GeneTemplate | GetName |  | CString | 类别：nonconst |
| GeneTemplate | Self |  | GeneTemplate |  |
| GeneralInformationWindow | AccessSelf |  | GeneralInformationWindow | 类别：const |
| GeneralInformationWindow | GetText |  | CString | 类别：nonconst |
| GeneralInformationWindow | GetTitle |  | CString | 类别：nonconst |
| GeneralInformationWindow | Self |  | GeneralInformationWindow |  |
| GenerationItem | AccessSelf |  | GenerationItem | 类别：const |
| GenerationItem | GetChildPortraitItems |  | Unknown | 类别：nonconst |
| GenerationItem | Self |  | GenerationItem |  |
| GeographicRegion | AccessSelf |  | GeographicRegion | 类别：const |
| GeographicRegion | GetCountryPagedList |  | CString | 类别：非常量 |
| GeographicRegion | GetCustom | CustomLocalization | CString | 类别：非常量 |
| GeographicRegion | GetDescription |  | CString | 类别：非常量 |
| GeographicRegion | GetName |  | CString | 类别：非常量 |
| GeographicRegion | GetNameNoFormatting |  | CString | 类别：非常量 |
| GeographicRegion | GetNumCountries |  | int32 | 类别：非常量 |
| GeographicRegion | GetNumStates |  | int32 | 类别：非常量 |
| GeographicRegion | GetNumStrategicRegions |  | int32 | 类别：非常量 |
| GeographicRegion | GetStatePagedList |  | CString | 类别：非常量 |
| GeographicRegion | GetStrategicRegionPagedList |  | CString | 类别：非常量 |
| GeographicRegion | GetStrategicRegionTooltip |  | CString | 类别：非常量 |
| GeographicRegion | GetTooltip |  | CString | 类别：非常量 |
| GeographicRegion | GetTooltipTag |  | CString | 类别：非常量 |
| GeographicRegion | GetUnlocks |  | CString | 类别：非常量 |
| GeographicRegion | MakeScope |  | Scope |  |
| GeographicRegion | Self |  | GeographicRegion |  |
| GeographicRegion | ZoomToRegion |  | void |  |
| GfxSkin | AccessSelf |  | GfxSkin | 类别：常量 |
| GfxSkin | GetFolders |  | Unknown | 类别：非常量 |
| GfxSkin | GetName |  | CString | 类别：非常量 |
| GfxSkin | GetPath |  | CString | 类别：非常量 |
| GfxSkin | GetTextures |  | Unknown | 类别：非常量 |
| GfxSkin | Self |  | GfxSkin |  |
| Goods | AccessBuildingsProducingThis |  | Unknown | 类别：常量 |
| Goods | AccessBuildingsUsingThis |  | Unknown | 类别：常量 |
| Goods | AccessMarket |  | Market | 类别：常量 |
| Goods | AccessProductionMethodsProducingThis |  | Unknown | 类别：常量 |
| Goods | AccessProductionMethodsUsingThis |  | Unknown | 类别：常量 |
| Goods | AccessSelf |  | Goods | 类别：常量 |
| Goods | AccessState |  | State | 类别：常量 |
| Goods | CalcConsumptionTaxAmount | Country | CFixedPoint |  |
| Goods | CalcConsumptionTaxAuthorityCost | Country | CFixedPoint |  |
| Goods | CalcPotentialConsumptionTaxAmount | Country | CFixedPoint |  |
| Goods | CanEditName |  | bool |  |
| Goods | GetAccessAdjustedStateBuy |  | CFixedPoint | 类别：非常量 |
| Goods | GetAccessAdjustedStateSell |  | CFixedPoint | 类别：非常量 |
| Goods | GetBaseGoods |  | Goods | 类别：非常量 |
| Goods | GetBasePrice |  | CFixedPoint | 类别：非常量 |
| Goods | GetBasePricePlotPoints |  | Unknown | 类别：非常量 |
| Goods | GetBreakdownOfBuildingsAffectedByShortageInMarket |  | CString | 类别：非常量 |
| Goods | GetBreakdownOfBuildingsAffectedByShortageInState |  | CString | 类别：非常量 |
| Goods | GetBuildingsProducingThisDesc |  | CString | 类别：非常量 |
| Goods | GetBuildingsUsingThisDesc |  | CString | 类别：非常量 |
| Goods | GetCategoryColor |  | CVector4f | 类别：非常量 |
| Goods | GetCategoryName |  | CString | 类别：非常量 |
| Goods | GetColor |  | CVector4f | 类别：非常量 |
| Goods | GetCompareDescAgainstBasePrice | CFixedPoint | CString | 类别：非常量 |
| Goods | GetCompareIconAgainstBasePrice | CFixedPoint | CString | 类别：非常量 |
| Goods | GetCompareIconAgainstBasePriceNoFormatting | CFixedPoint | CString | 类别：非常量 |
| Goods | GetCompareIconAgainstBasePriceNoTooltip | CFixedPoint | CString | 类别：非常量 |
| Goods | GetConsumptionPercentage |  | CFixedPoint | 类别：非常量 |
| Goods | GetCustom | CustomLocalization | CString | 类别：非常量 |
| Goods | GetExportersToMarket |  | Unknown | 类别：非常量 |
| Goods | GetExportersToState |  | Unknown | 类别：非常量 |
| Goods | GetGoodsShortageDesc |  | CString | 类别：非常量 |
| Goods | GetImportersFromMarket |  | Unknown | 类别：非常量 |
| Goods | GetImportersFromState |  | Unknown | 类别：非常量 |
| Goods | GetKey |  | CString | 类别：非常量 |
| Goods | GetLeaderboardDesc |  | CString | 类别：非常量 |
| Goods | GetLeaderboardSpot | Country | int32 | 类别：非常量 |
| Goods | GetLeaderboardSpotDesc | Country | CString | 类别：非常量 |
| Goods | GetLocalPriceShare |  | CFixedPoint | 类别：非常量 |
| Goods | GetLocalPricesDesc |  | CString | 类别：非常量 |
| Goods | GetMarket |  | Market | 类别：非常量 |
| Goods | GetMarketAverageSubventionRate |  | CFixedPoint | 类别：非常量 |
| Goods | GetMarketAverageTariffRate |  | CFixedPoint | 类别：非常量 |
| Goods | GetMarketBalanceLabel |  | CString | 类别：非常量 |
| Goods | GetMarketBuildingTypeBuyOrdersBreakdown | Unknown | CString | 类别：非常量 |
| Goods | GetMarketBuildingTypeSellOrdersBreakdown | Unknown | CString | 类别：非常量 |
| Goods | GetMarketBuyAndSellOrdersBalance |  | CFixedPoint | 类别：非常量 |
| Goods | GetMarketBuyOrders |  | CFixedPoint | 类别：非常量 |
| Goods | GetMarketBuyOrdersBreakdown |  | CString | 类别：非常量 |
| Goods | GetMarketBuyOrdersWithTooltip |  | CString | 类别：非常量 |
| Goods | GetMarketConsumption |  | CFixedPoint | 类别：非常量 |
| Goods | GetMarketConsumptionBreakdown |  | CString | 类别：非常量 |
| Goods | GetMarketConsumptionWithTooltip |  | CString | 类别：非常量 |
| Goods | GetMarketExportAdvantage |  | CFixedPoint | 类别：非常量 |
| Goods | GetMarketExports |  | CFixedPoint | 类别：非常量 |
| Goods | GetMarketGoodsShortageDesc |  | CString | 类别：非常量 |
| Goods | GetMarketImportAdvantage |  | CFixedPoint | 类别：非常量 |
| Goods | GetMarketImports |  | CFixedPoint | 类别：非常量 |
| Goods | GetMarketMonopolyFraction |  | CFixedPoint | 类别：非常量 |
| Goods | GetMarketMonopolyPriceImpact |  | CFixedPoint | 类别：非常量 |
| Goods | GetMarketPopConsumptionBreakdown |  | CString | 类别：非常量 |
| Goods | GetMarketPrestigeGoods |  | Unknown | 类别：非常量 |
| Goods | GetMarketPrestigeGoodsBought |  | Unknown | 类别：非常量 |
| Goods | GetMarketPrestigeGoodsSold |  | Unknown | 类别：非常量 |
| Goods | GetMarketPrice |  | CFixedPoint | 类别：非常量 |
| Goods | GetMarketPriceDesc |  | CString | 类别：非常量 |
| Goods | GetMarketPriceLabel |  | CString | 类别：非常量 |
| Goods | GetMarketPriceShare |  | CFixedPoint | 类别：非常量 |
| Goods | GetMarketPriceShareDesc |  | CString | 类别：非常量 |
| Goods | GetMarketPriceWithTooltip |  | CString | 类别：非常量 |
| Goods | GetMarketProduction |  | CFixedPoint | 类别：非常量 |
| Goods | GetMarketProductionAndConsumptionDiff |  | CFixedPoint | 类别：非常量 |
| Goods | GetMarketProductionBreakdown |  | CString | 类别：非常量 |
| Goods | GetMarketProductionWithTooltip |  | CString | 类别：非常量 |
| Goods | GetMarketRelativeExportAdvantage |  | CFixedPoint | 类别：非常量 |
| Goods | GetMarketRelativeExportAdvantageDesc |  | CString | 类别：非常量 |
| Goods | GetMarketRelativeImportAdvantage |  | CFixedPoint | 类别：非常量 |
| Goods | GetMarketRelativeImportAdvantageDesc |  | CString | 类别：非常量 |
| Goods | GetMarketSellOrders |  | CFixedPoint | 类别：非常量 |
| Goods | GetMarketSellOrdersBreakdown |  | CString | 类别：非常量 |
| Goods | GetMarketSellOrdersWithTooltip |  | CString | 类别：非常量 |
| Goods | GetMarketTariffsSubventionsBalance |  | CFixedPoint | 类别：非常量 |
| Goods | GetMarketTariffsSubventionsBalanceDesc |  | CString | 类别：非常量 |
| Goods | GetMarketWithLargestExportShare |  | Market | 类别：非常量 |
| Goods | GetMarketWithLargestImportShare |  | Market | 类别：非常量 |
| Goods | GetMaxImbalance |  | CFixedPoint | 类别：非常量 |
| Goods | GetMaxPrice |  | CFixedPoint | 类别：非常量 |
| Goods | GetMinPrice |  | CFixedPoint | 类别：非常量 |
| Goods | GetName |  | CString | 类别：非常量 |
| Goods | GetNameNoFormatting |  | CString | 类别：非常量 |
| Goods | GetNameNoIcon |  | CString | 类别：非常量 |
| Goods | GetNeedLevelsContainingThisDesc |  | CString | 类别：非常量 |
| Goods | GetNonPrestigeGoodsMarketBuyOrders |  | CFixedPoint | 类别：非常量 |
| Goods | GetNonPrestigeGoodsMarketSellOrders |  | CFixedPoint | 类别：非常量 |
| Goods | GetNonPrestigeGoodsStateConsumption |  | CFixedPoint | 类别：非常量 |
| Goods | GetNonPrestigeGoodsStateProduction |  | CFixedPoint | 类别：非常量 |
| Goods | GetNonPrestigeGoodsWorldMarketExports |  | CFixedPoint | 类别：非常量 |
| Goods | GetNonPrestigeGoodsWorldMarketImports |  | CFixedPoint | 类别：非常量 |
| Goods | GetNumBuildingsAffectedByShortageInMarket |  | int32 | 类别：非常量 |
| Goods | GetNumBuildingsAffectedByShortageInState |  | int32 | 类别：非常量 |
| Goods | GetPercentageDeltaAgainstBasePrice | CFixedPoint | CFixedPoint | 类别：非常量 |
| Goods | GetPrestigeAwardForPrestigeGoodSpot | Unknown | int32 | 类别：非常量 |
| Goods | GetPrestigeAwardForPrestigeGoodSpotDesc | int32 | CString | 类别：非常量 |
| Goods | GetPrestigeAwardForSpot | Unknown | int32 | 类别：非常量 |
| Goods | GetPrestigeAwardForSpotDesc | int32 | CString | 类别：非常量 |
| Goods | GetPrestigeGoodCombatUnitEffectDesc |  | CString | 类别：非常量 |
| Goods | GetPrestigeGoodLeaderboardDesc |  | CString | 类别：非常量 |
| Goods | GetPrestigeGoodLeaderboardSpot | Country | int32 | 类别：非常量 |
| Goods | GetPrestigeGoodLeaderboardSpotDesc | Country | CString | 类别：非常量 |
| Goods | GetPrestigeGoodSoLEffectDesc |  | CString | 类别：非常量 |
| Goods | GetPrestigeGoodThroughputEffectDesc |  | CString | 类别：非常量 |
| Goods | GetPrestigeGoodTradeAdvantageEffectDesc |  | CString | 类别：非常量 |
| Goods | GetPriceTrend |  | DataTrend | 类别：非常量 |
| Goods | GetProductionPercentage |  | CFixedPoint | 类别：非常量 |
| Goods | GetShortCompareDescAgainstBasePrice | CFixedPoint | CString | 类别：非常量 |
| Goods | GetShortageRatioInMarket |  | CFixedPoint | 类别：非常量 |
| Goods | GetShortageRatioInState |  | CFixedPoint | 类别：非常量 |
| Goods | GetState |  | State | 类别：非常量 |
| Goods | GetStateBalanceLabel |  | CString | 类别：非常量 |
| Goods | GetStateConsumption |  | CFixedPoint | 类别：非常量 |
| Goods | GetStateConsumptionBreakdown |  | CString | 类别：非常量 |
| Goods | GetStateConsumptionLabel |  | CString | 类别：非常量 |
| Goods | GetStateConsumptionWithTooltip |  | CString | 类别：非常量 |
| Goods | GetStateExportAdvantage |  | CFixedPoint | 类别：非常量 |
| Goods | GetStateExportAdvantageDesc |  | CString | 类别：非常量 |
| Goods | GetStateExportPrice |  | CFixedPoint | 类别：非常量 |
| Goods | GetStateExportPriceDesc |  | CString | 类别：非常量 |
| Goods | GetStateExportSubventionRate |  | CFixedPoint | 类别：非常量 |
| Goods | GetStateExportSubventionRateDesc |  | CString | 类别：非常量 |
| Goods | GetStateExportTariffRate |  | CFixedPoint | 类别：非常量 |
| Goods | GetStateExportTariffRateDesc |  | CString | 类别：非常量 |
| Goods | GetStateExports |  | CFixedPoint | 类别：非常量 |
| Goods | GetStateExportsDesc |  | CString | 类别：非常量 |
| Goods | GetStateGoodsShortageDesc |  | CString | 类别：非常量 |
| Goods | GetStateImportAdvantage |  | CFixedPoint | 类别：非常量 |
| Goods | GetStateImportAdvantageDesc |  | CString | 类别：非常量 |
| Goods | GetStateImportPrice |  | CFixedPoint | 类别：非常量 |
| Goods | GetStateImportPriceDesc |  | CString | 类别：非常量 |
| Goods | GetStateImportSubventionRate |  | CFixedPoint | 类别：非常量 |
| Goods | GetStateImportSubventionRateDesc |  | CString | 类别：非常量 |
| Goods | GetStateImportTariffRate |  | CFixedPoint | 类别：非常量 |
| Goods | GetStateImportTariffRateDesc |  | CString | 类别：非常量 |
| Goods | GetStateImports |  | CFixedPoint | 类别：非常量 |
| Goods | GetStateImportsDesc |  | CString | 类别：非常量 |
| Goods | GetStateMonopolyFraction |  | CFixedPoint | 类别：非常量 |
| Goods | GetStateMonopolyPriceImpact |  | CFixedPoint | 类别：非常量 |
| Goods | GetStatePopDemandBreakdown | State PopType | CString | 类别：非常量 |
| Goods | GetStatePopProductionBreakdown | State PopType | CString | 类别：非常量 |
| Goods | GetStatePopTypeDemandBreakdown | State | CString | 类别：非常量 |
| Goods | GetStatePopTypeProductionBreakdown | State | CString | 类别：非常量 |
| Goods | GetStatePrestigeGoods |  | Unknown | 类别：非常量 |
| Goods | GetStatePrestigeGoodsBought |  | Unknown | 类别：非常量 |
| Goods | GetStatePrestigeGoodsSold |  | Unknown | 类别：非常量 |
| Goods | GetStatePrice |  | CFixedPoint | 类别：非常量 |
| Goods | GetStatePriceDesc |  | CString | 类别：非常量 |
| Goods | GetStatePriceLabel |  | CString | 类别：非常量 |
| Goods | GetStatePriceWithTooltip |  | CString | 类别：非常量 |
| Goods | GetStateProduction |  | CFixedPoint | 类别：非常量 |
| Goods | GetStateProductionBreakdown |  | CString | 类别：非常量 |
| Goods | GetStateProductionConsumptionDiff |  | CFixedPoint | 类别：非常量 |
| Goods | GetStateProductionLabel |  | CString | 类别：非常量 |
| Goods | GetStateProductionWithTooltip |  | CString | 类别：非常量 |
| Goods | GetStateRelativeExportAdvantage |  | CFixedPoint | 类别：非常量 |
| Goods | GetStateRelativeExportAdvantageDesc |  | CString | 类别：非常量 |
| Goods | GetStateRelativeImportAdvantage |  | CFixedPoint | 类别：非常量 |
| Goods | GetStateRelativeImportAdvantageDesc |  | CString | 类别：非常量 |
| Goods | GetStateTariffsSubventionsBalance |  | CFixedPoint | 类别：非常量 |
| Goods | GetStateTariffsSubventionsBalanceDesc |  | CString | 类别：非常量 |
| Goods | GetStateToMarketPriceDiff |  | CFixedPoint | 类别：非常量 |
| Goods | GetTaxDesc | Country | CString | 类别：非常量 |
| Goods | GetTextIcon |  | CString | 类别：非常量 |
| Goods | GetTexture |  | Unknown | 类别：非常量 |
| Goods | GetTooltipTag |  | CString | 类别：非常量 |
| Goods | GetTotalImportExport |  | CFixedPoint | 类别：非常量 |
| Goods | GetTradedQuantity |  | CFixedPoint | 类别：非常量 |
| Goods | GetWorldMarketAdditionalExportsFromMarket |  | CFixedPoint | 类别：非常量 |
| Goods | GetWorldMarketAdditionalImportsToMarket |  | CFixedPoint | 类别：非常量 |
| Goods | GetWorldMarketBasePrice |  | CFixedPoint | 类别：非常量 |
| Goods | GetWorldMarketBasePriceDesc |  | CString | 类别：非常量 |
| Goods | GetWorldMarketExporters |  | Unknown | 类别：非常量 |
| Goods | GetWorldMarketExports |  | CFixedPoint | 类别：非常量 |
| Goods | GetWorldMarketExportsAndImportsBalance |  | CFixedPoint | 类别：非常量 |
| Goods | GetWorldMarketExportsBreakdown |  | CString | 类别：非常量 |
| Goods | GetWorldMarketExportsWithTooltip |  | CString | 类别：非常量 |
| Goods | GetWorldMarketImporters |  | Unknown | 类别：非常量 |
| Goods | GetWorldMarketImports |  | CFixedPoint | 类别：非常量 |
| Goods | GetWorldMarketImportsBreakdown |  | CString | 类别：非常量 |
| Goods | GetWorldMarketImportsWithTooltip |  | CString | 类别：非常量 |
| Goods | GetWorldMarketMonopolyFraction |  | CFixedPoint | 类别：非常量 |
| Goods | GetWorldMarketMonopolyPriceImpact |  | CFixedPoint | 类别：非常量 |
| Goods | GetWorldMarketPrestigeGoods |  | Unknown | 类别：非常量 |
| Goods | GetWorldMarketPrestigeGoodsExported |  | Unknown | 类别：非常量 |
| Goods | GetWorldMarketPrestigeGoodsImported |  | Unknown | 类别：非常量 |
| Goods | GetWorldPriceTrend |  | DataTrend | 类别：非常量 |
| Goods | HasGoodsShortage |  | bool |  |
| Goods | HasImportExportControl |  | bool |  |
| Goods | HasMarketContext |  | bool |  |
| Goods | HasPriceTrend |  | bool |  |
| Goods | HasShortageInMarket |  | bool |  |
| Goods | HasShortageInState |  | bool |  |
| Goods | HasStateContext |  | bool |  |
| Goods | IsBeingHighlighted |  | bool |  |
| Goods | IsGoodsMarketTabOpen |  | bool |  |
| Goods | IsLocal |  | bool |  |
| Goods | IsPinnedInOutliner |  | bool |  |
| Goods | IsPrestigeGoods |  | bool |  |
| Goods | IsTaxed | Unknown | bool |  |
| Goods | IsTradeable |  | bool |  |
| Goods | IsValid |  | bool |  |
| Goods | MakeScope |  | Scope |  |
| Goods | Self |  | Goods |  |
| Goods | TogglePinInOutliner |  | void |  |
| Goods | ToggleTaxation | Country | Command |  |
| Goods | WithMarketContext | Unknown | Goods |  |
| Goods | WithStateContext | Unknown | Goods |  |
| GoodsExpenseItem | AccessSelf |  | GoodsExpenseItem | 类别：常量 |
| GoodsExpenseItem | GetExpenseRatio |  | CFixedPoint | 类别：非常量 |
| GoodsExpenseItem | GetGoods |  | Goods | 类别：非常量 |
| GoodsExpenseItem | GetPrice |  | CFixedPoint | 类别：非常量 |
| GoodsExpenseItem | GetRelativePriceDiff |  | CFixedPoint | 类别：非常量 |
| GoodsExpenseItem | GetTotalCost |  | CFixedPoint | 类别：非常量 |
| GoodsExpenseItem | Self |  | GoodsExpenseItem |  |
| GoodsList | AccessSelf |  | GoodsList | 类别：常量 |
| GoodsList | GetGoods |  | Unknown | 类别：非常量 |
| GoodsList | GetPopConsumptionRatio | Goods | CFixedPoint | 类别：非常量 |
| GoodsList | GetPrice | Unknown | CFixedPoint | 类别：非常量 |
| GoodsList | HasMarketContext |  | bool |  |
| GoodsList | HasStateContext |  | bool |  |
| GoodsList | RestoreSort |  | void |  |
| GoodsList | Self |  | GoodsList |  |
| GoodsList | Sort | CString | void |  |
| GoodsLocalPricesPanel | AccessGoods |  | Goods | 类别：常量 |
| GoodsLocalPricesPanel | AccessLocalPrices |  | Unknown | 类别：常量 |
| GoodsLocalPricesPanel | AccessSelf |  | GoodsLocalPricesPanel | 类别：常量 |
| GoodsLocalPricesPanel | GetGoods |  | Goods | 类别：非常量 |
| GoodsLocalPricesPanel | Self |  | GoodsLocalPricesPanel |  |
| GoodsLocalPricesPanel | Sort | Unknown | void |  |
| GoodsPanel | AccessSelf |  | GoodsPanel | 类别：常量 |
| GoodsPanel | GetInputValues |  | Unknown | 类别：非常量 |
| GoodsPanel | GetInputValuesTotal |  | CFixedPoint | 类别：非常量 |
| GoodsPanel | GetOutputValues |  | Unknown | 类别：非常量 |
| GoodsPanel | GetOutputValuesTotal |  | CFixedPoint | 类别：非常量 |
| GoodsPanel | Self |  | GoodsPanel |  |
| GoodsPanelChildValue | AccessSelf |  | GoodsPanelChildValue | 类别：常量 |
| GoodsPanelChildValue | GetName |  | CString | 类别：非常量 |
| GoodsPanelChildValue | GetValue |  | CFixedPoint | 类别：非常量 |
| GoodsPanelChildValue | Self |  | GoodsPanelChildValue |  |
| GoodsPanelValue | AccessSelf |  | GoodsPanelValue | 类别：常量 |
| GoodsPanelValue | GetBuilding |  | Building | 类别：非常量 |
| GoodsPanelValue | GetBuildingType |  | BuildingType | 类别：非常量 |
| GoodsPanelValue | GetChildren |  | Unknown | 类别：非常量 |
| GoodsPanelValue | GetMarket |  | Market | 类别：非常量 |
| GoodsPanelValue | GetName |  | CString | 类别：非常量 |
| GoodsPanelValue | GetState |  | State | 类别：非常量 |
| GoodsPanelValue | GetValue |  | CFixedPoint | 类别：非常量 |
| GoodsPanelValue | HasBuildingInfo |  | bool |  |
| GoodsPanelValue | HasBuildingTypeInfo |  | bool |  |
| GoodsPanelValue | HasMarketContext |  | bool |  |
| GoodsPanelValue | Self |  | GoodsPanelValue |  |
| GoodsPanelValue | ShowChildValues |  | bool |  |
| GoodsProductionInfo | AccessGoods |  | Goods | 类别：常量 |
| GoodsProductionInfo | AccessSelf |  | GoodsProductionInfo | 类别：常量 |
| GoodsProductionInfo | GetAmount |  | CFixedPoint | 类别：非常量 |
| GoodsProductionInfo | GetMP |  | CFixedPoint | 类别：非常量 |
| GoodsProductionInfo | GetName |  | CString | 类别：非常量 |
| GoodsProductionInfo | GetPrice |  | CFixedPoint | 类别：非常量 |
| GoodsProductionInfo | GetSoldFor |  | CFixedPoint | 类别：非常量 |
| GoodsProductionInfo | GetTexture |  | Unknown | 类别：非常量 |
| GoodsProductionInfo | Self |  | GoodsProductionInfo |  |
| GoodsStatePanel | AccessSelf |  | GoodsStatePanel | 类别：常量 |
| GoodsStatePanel | GetInputValues |  | Unknown | 类别：非常量 |
| GoodsStatePanel | GetInputValuesTotal |  | CFixedPoint | 类别：非常量 |
| GoodsStatePanel | GetOutputValues |  | Unknown | 类别：非常量 |
| GoodsStatePanel | GetOutputValuesTotal |  | CFixedPoint | 类别：非常量 |
| GoodsStatePanel | Self |  | GoodsStatePanel |  |
| GoodsUsagePanel | AccessGoods |  | Goods | 类别：常量 |
| GoodsUsagePanel | AccessProductionValues |  | Unknown | 类别：常量 |
| GoodsUsagePanel | AccessSelf |  | GoodsUsagePanel | 类别：常量 |
| GoodsUsagePanel | GetGoods |  | Goods | 类别：非常量 |
| GoodsUsagePanel | Self |  | GoodsUsagePanel |  |
| GoodsWorldMarketPanel | AccessSelf |  | GoodsWorldMarketPanel | 类别：常量 |
| GoodsWorldMarketPanel | GetBaseGoods |  | Goods | 类别：非常量 |
| GoodsWorldMarketPanel | GetGoods |  | Goods | 类别：非常量 |
| GoodsWorldMarketPanel | GetMarkets |  | Unknown | 类别：非常量 |
| GoodsWorldMarketPanel | Self |  | GoodsWorldMarketPanel |  |
| GoodsWorldMarketPanel | SortMarkets | Unknown | void |  |
| GovernmentType | AccessSelf |  | GovernmentType | 类别：常量 |
| GovernmentType | GetDesc |  | CString | 类别：非常量 |
| GovernmentType | GetName |  | CString | 类别：非常量 |
| GovernmentType | GetPossibleTriggerDesc | Player | CString | 类别：非常量 |
| GovernmentType | GetTooltipTag |  | CString | 类别：非常量 |
| GovernmentType | GetTransferOfPowerDesc |  | CString | 类别：非常量 |
| GovernmentType | GetTransferOfPowerName |  | CString | 类别：非常量 |
| GovernmentType | Self |  | GovernmentType |  |
| Graph | AccessSelf |  | Graph | 类别：常量 |
| Graph | Errors |  | Unknown |  |
| Graph | HasErrors |  | bool |  |
| Graph | Self |  | Graph |  |
| GraphInterfaceNodeWindow | AccessSelf |  | GraphInterfaceNodeWindow | 类别：常量 |
| GraphInterfaceNodeWindow | AddPin | bool | void |  |
| GraphInterfaceNodeWindow | Self |  | GraphInterfaceNodeWindow |  |
| GraphPanel | AccessAnimationEditorSearch |  | NodeEditorSearch | 类别：常量 |
| GraphPanel | AccessMetadataWindow |  | MetadataWindow | 类别：常量 |
| GraphPanel | AccessSelf |  | GraphPanel | 类别：常量 |
| GraphPanel | ClearSelection |  | void |  |
| GraphPanel | CompoundNodeUpdated | Unknown | void |  |
| GraphPanel | Copy |  | void |  |
| GraphPanel | CreateInfoBoxNode |  | int32 |  |
| GraphPanel | CreateNodeByName | Unknown | int32 |  |
| GraphPanel | Cut |  | void |  |
| GraphPanel | Delete |  | void |  |
| GraphPanel | Fit |  | void |  |
| GraphPanel | GetMetadataWindow |  | MetadataWindow | 类别：非常量 |
| GraphPanel | GetNodeLineMaskTexture | bool | Unknown | 类别：非常量 |
| GraphPanel | GetNodeLineTexture | bool | Unknown | 类别：非常量 |
| GraphPanel | GetViewportHotkeysDescription |  | CString | 类别：非常量 |
| GraphPanel | HasExportButton |  | bool |  |
| GraphPanel | HasImportButton |  | bool |  |
| GraphPanel | HasPreviewer |  | bool |  |
| GraphPanel | HasRenamingCapability |  | bool |  |
| GraphPanel | InvertSelection |  | void |  |
| GraphPanel | IsButtonEnabled | CString | bool |  |
| GraphPanel | IsNodeEditorSearchVisible |  | bool |  |
| GraphPanel | IsPasteable |  | bool |  |
| GraphPanel | IsSaveable |  | bool |  |
| GraphPanel | IsViewportHoteysDescriptionShown |  | bool |  |
| GraphPanel | LayoutNodes |  | void |  |
| GraphPanel | Load |  | void |  |
| GraphPanel | New |  | void |  |
| GraphPanel | OnEditorPreferencesClicked |  | void |  |
| GraphPanel | OnExportButton |  | void |  |
| GraphPanel | OnImportButton |  | void |  |
| GraphPanel | OpenPreviewer |  | void |  |
| GraphPanel | Paste |  | void |  |
| GraphPanel | PasteConnectedToExisting |  | void |  |
| GraphPanel | Properties |  | void |  |
| GraphPanel | RenameGraph |  | void |  |
| GraphPanel | Save |  | void |  |
| GraphPanel | SaveAs |  | void |  |
| GraphPanel | SelectAllNodes |  | void |  |
| GraphPanel | SelectionToCompoundNode |  | void |  |
| GraphPanel | SelectionToGroupNode |  | void |  |
| GraphPanel | Self |  | GraphPanel |  |
| GraphPanel | SetZoom | int32 | void |  |
| GraphPanel | ShatterSelectedGroup |  | void |  |
| GraphPanel | ShowNodeEditorSearch |  | void |  |
| GraphPanel | ShowNodeSearch |  | void |  |
| Group | AccessSelf |  | Group | 类别：const |
| Group | AccessVisibleAchievements |  | Unknown | 类别：const |
| Group | CalcNumberOfUnlockedVisibleAchievements |  | int32 |  |
| Group | GetName |  | CUTF8String | 类别：nonconst |
| Group | GetNumberOfVisibleAchievements |  | int32 | 类别：nonconst |
| Group | IsCollapsed |  | bool |  |
| Group | Self |  | Group |  |
| Group | ToggleCollapsed |  | void |  |
| GuiAnimationCurveEditor | AccessSelf |  | GuiAnimationCurveEditor | 类别：const |
| GuiAnimationCurveEditor | GetGraphLines |  | Unknown | 类别：nonconst |
| GuiAnimationCurveEditor | IsAnyEditorOpen |  | bool |  |
| GuiAnimationCurveEditor | Self |  | GuiAnimationCurveEditor |  |
| GuiAnimationCurveEditorControlPoint | AccessSelf |  | GuiAnimationCurveEditorControlPoint | 类别：const |
| GuiAnimationCurveEditorControlPoint | GetCoords |  | CVector2f | 类别：nonconst |
| GuiAnimationCurveEditorControlPoint | IsSelected | GuiAnimationEditorMetadataCtx | bool |  |
| GuiAnimationCurveEditorControlPoint | IsUnderMousePointer |  | bool |  |
| GuiAnimationCurveEditorControlPoint | Self |  | GuiAnimationCurveEditorControlPoint |  |
| GuiAnimationCurveEditorLine | AccessSelf |  | GuiAnimationCurveEditorLine | 类别：const |
| GuiAnimationCurveEditorLine | GetColor |  | CVector4f | 类别：nonconst |
| GuiAnimationCurveEditorLine | GetControlPoints |  | Unknown | 类别：nonconst |
| GuiAnimationCurveEditorLine | GetLineVertices |  | Unknown | 类别：nonconst |
| GuiAnimationCurveEditorLine | Self |  | GuiAnimationCurveEditorLine |  |
| GuiAnimationCurveEditorViewport | AccessSelf |  | GuiAnimationCurveEditorViewport | 类别：const |
| GuiAnimationCurveEditorViewport | GetNeedlePosition | Unknown Unknown Unknown | CVector2f | 类别：nonconst |
| GuiAnimationCurveEditorViewport | Self |  | GuiAnimationCurveEditorViewport |  |
| GuiAnimationEditor | AccessAnimSets |  | Unknown | 类别：const |
| GuiAnimationEditor | AccessAnimations |  | Unknown | 类别：const |
| GuiAnimationEditor | AccessAvailableTracks |  | Unknown | 类别：const |
| GuiAnimationEditor | AccessSelf |  | GuiAnimationEditor | 类别：const |
| GuiAnimationEditor | AccessUniversalTracks |  | Unknown | 类别：const |
| GuiAnimationEditor | AddKeyframesAtCurrentTime |  | void |  |
| GuiAnimationEditor | CanChangeSelectedAnimSetParent |  | bool |  |
| GuiAnimationEditor | CanCreateNewAnimation |  | bool |  |
| GuiAnimationEditor | CanDeleteSelectedAnimSet |  | bool |  |
| GuiAnimationEditor | CanDeleteSelectedAnimations |  | bool |  |
| GuiAnimationEditor | CanRenameSelectedAnimSet |  | bool |  |
| GuiAnimationEditor | CanRenameSelectedAnimation |  | bool |  |
| GuiAnimationEditor | ChangeSelectedAnimSetParent |  | void |  |
| GuiAnimationEditor | CreateNewAnimSet |  | void |  |
| GuiAnimationEditor | CreateNewAnimation |  | void |  |
| GuiAnimationEditor | DeleteSelectedAnimSet |  | void |  |
| GuiAnimationEditor | DeleteSelectedAnimations |  | void |  |
| GuiAnimationEditor | DeleteSelectedKeyframes |  | void |  |
| GuiAnimationEditor | GetAnimSets |  | Unknown | 类别：nonconst |
| GuiAnimationEditor | GetAnimations |  | Unknown | 类别：nonconst |
| GuiAnimationEditor | GetAvailableTracks |  | Unknown | 类别：nonconst |
| GuiAnimationEditor | GetUniversalTracks |  | Unknown | 类别：nonconst |
| GuiAnimationEditor | IsAnyCurveEditorOpen |  | bool |  |
| GuiAnimationEditor | IsKeyframeSelectionValidForCurvePreset |  | bool |  |
| GuiAnimationEditor | OnSave |  | void |  |
| GuiAnimationEditor | OnSaveAs |  | void |  |
| GuiAnimationEditor | RenameSelectedAnimSet |  | void |  |
| GuiAnimationEditor | RenameSelectedAnimation |  | void |  |
| GuiAnimationEditor | Self |  | GuiAnimationEditor |  |
| GuiAnimationEditorAnimSetEntry | AccessSelf |  | GuiAnimationEditorAnimSetEntry | 类别：const |
| GuiAnimationEditorAnimSetEntry | GetDisplayName |  | CString | 类别：nonconst |
| GuiAnimationEditorAnimSetEntry | IsSelected |  | bool |  |
| GuiAnimationEditorAnimSetEntry | Self |  | GuiAnimationEditorAnimSetEntry |  |
| GuiAnimationEditorAnimSetEntry | ToggleSelected |  | void |  |
| GuiAnimationEditorAnimationEntry | AccessSelf |  | GuiAnimationEditorAnimationEntry | 类别：const |
| GuiAnimationEditorAnimationEntry | GetDisplayName |  | CString | 类别：nonconst |
| GuiAnimationEditorAnimationEntry | GetTooltipMessage |  | CString | 类别：nonconst |
| GuiAnimationEditorAnimationEntry | IsAnimationInherited |  | bool |  |
| GuiAnimationEditorAnimationEntry | IsSelected |  | bool |  |
| GuiAnimationEditorAnimationEntry | OverrideInheritedAnimation |  | void |  |
| GuiAnimationEditorAnimationEntry | Self |  | GuiAnimationEditorAnimationEntry |  |
| GuiAnimationEditorAnimationEntry | ToggleSelected |  | void |  |
| GuiAnimationEditorAvailableTrack | AccessSelf |  | GuiAnimationEditorAvailableTrack | 类别：const |
| GuiAnimationEditorAvailableTrack | AddTrack |  | void |  |
| GuiAnimationEditorAvailableTrack | GetDescription |  | Unknown | 类别：nonconst |
| GuiAnimationEditorAvailableTrack | GetDisplayName |  | Unknown | 类别：nonconst |
| GuiAnimationEditorAvailableTrack | GetExcludedDisplayName |  | Unknown | 类别：nonconst |
| GuiAnimationEditorAvailableTrack | IsExcluded |  | bool |  |
| GuiAnimationEditorAvailableTrack | Self |  | GuiAnimationEditorAvailableTrack |  |
| GuiAnimationEditorKeyframe | AccessSelf |  | GuiAnimationEditorKeyframe | 类别：const |
| GuiAnimationEditorKeyframe | GetPosition |  | CVector2f | 类别：nonconst |
| GuiAnimationEditorKeyframe | GetTimeInSeconds |  | float | 类别：nonconst |
| GuiAnimationEditorKeyframe | IsDataFlowButton |  | bool |  |
| GuiAnimationEditorKeyframe | IsDataFlowToWidget |  | bool |  |
| GuiAnimationEditorKeyframe | IsDragged |  | bool |  |
| GuiAnimationEditorKeyframe | IsSelected |  | bool |  |
| GuiAnimationEditorKeyframe | IsUnderMousePointer |  | bool |  |
| GuiAnimationEditorKeyframe | IsValid |  | bool |  |
| GuiAnimationEditorKeyframe | Self |  | GuiAnimationEditorKeyframe |  |
| GuiAnimationEditorKeyframe | ToggleDataFlow |  | void |  |
| GuiAnimationEditorMetadataCtx | AccessSelf |  | GuiAnimationEditorMetadataCtx | 类别：const |
| GuiAnimationEditorMetadataCtx | DeselectAllKeyframes |  | void |  |
| GuiAnimationEditorMetadataCtx | HasSelectedAnyKeyframes |  | bool |  |
| GuiAnimationEditorMetadataCtx | IsAnimationsTabCollapsed |  | bool |  |
| GuiAnimationEditorMetadataCtx | IsKeyframeSnapping |  | bool |  |
| GuiAnimationEditorMetadataCtx | SelectAllKeyframes |  | void |  |
| GuiAnimationEditorMetadataCtx | Self |  | GuiAnimationEditorMetadataCtx |  |
| GuiAnimationEditorMetadataCtx | ToggleAnimationsTabCollapsed |  | void |  |
| GuiAnimationEditorMetadataCtx | ToggleKeyframeSnapping |  | void |  |
| GuiAnimationEditorPlayer | AccessSelf |  | GuiAnimationEditorPlayer | 类别：const |
| GuiAnimationEditorPlayer | CanPlay |  | bool |  |
| GuiAnimationEditorPlayer | GetCurrentSpeedMultiplierOptionIndex |  | CVector2i | 类别：nonconst |
| GuiAnimationEditorPlayer | GetCurrentTime |  | float | 类别：nonconst |
| GuiAnimationEditorPlayer | GetMaxDuration |  | float | 类别：nonconst |
| GuiAnimationEditorPlayer | GetSpeedMultiplier |  | float | 类别：nonconst |
| GuiAnimationEditorPlayer | GetSpeedMultiplierOptions |  | Unknown | 类别：nonconst |
| GuiAnimationEditorPlayer | IsDraggingTime |  | bool |  |
| GuiAnimationEditorPlayer | IsLoopEnabled |  | bool |  |
| GuiAnimationEditorPlayer | IsPlaying |  | bool |  |
| GuiAnimationEditorPlayer | Self |  | GuiAnimationEditorPlayer |  |
| GuiAnimationEditorPlayer | SetCurrentTime | float | void |  |
| GuiAnimationEditorPlayer | SetIsPlaying | Unknown | void |  |
| GuiAnimationEditorPlayer | SetLoopEnabled | Unknown | void |  |
| GuiAnimationEditorPlayer | SetSpeedMultiplier | Unknown | void |  |
| GuiAnimationEditorPlayer | SetSpeedMultiplierOptionIndex |  | void |  |
| GuiAnimationEditorPlayer | ShouldMoveNeedleWithKeyframe |  | bool |  |
| GuiAnimationEditorPlayer | StepBackwards |  | void |  |
| GuiAnimationEditorPlayer | StepForward |  | void |  |
| GuiAnimationEditorPlayer | ToggleIsPlaying |  | void |  |
| GuiAnimationEditorPlayer | ToggleLoopEnabled |  | void |  |
| GuiAnimationEditorPlayer | ToggleMoveNeedleWithKeyframe |  | void |  |
| GuiAnimationEditorPlayerSpeedMultiplierEntry | AccessSelf |  | GuiAnimationEditorPlayerSpeedMultiplierEntry | 类别：const |
| GuiAnimationEditorPlayerSpeedMultiplierEntry | GetDisplayName |  | CString | 类别：nonconst |
| GuiAnimationEditorPlayerSpeedMultiplierEntry | GetMultiplier |  | float | 类别：nonconst |
| GuiAnimationEditorPlayerSpeedMultiplierEntry | Self |  | GuiAnimationEditorPlayerSpeedMultiplierEntry |  |
| GuiAnimationEditorRuler | AccessRulerResolutionEntries |  | Unknown | 类别：const |
| GuiAnimationEditorRuler | AccessSelf |  | GuiAnimationEditorRuler | 类别：const |
| GuiAnimationEditorRuler | GetRulerResolutionEntries |  | Unknown | 类别：nonconst |
| GuiAnimationEditorRuler | Self |  | GuiAnimationEditorRuler |  |
| GuiAnimationEditorRulerResolutionEntry | AccessSelf |  | GuiAnimationEditorRulerResolutionEntry | 类别：const |
| GuiAnimationEditorRulerResolutionEntry | GetDisplayValue |  | CString | 类别：nonconst |
| GuiAnimationEditorRulerResolutionEntry | GetPosition |  | CVector2f | 类别：nonconst |
| GuiAnimationEditorRulerResolutionEntry | IsSubdivision |  | bool |  |
| GuiAnimationEditorRulerResolutionEntry | Self |  | GuiAnimationEditorRulerResolutionEntry |  |
| GuiAnimationEditorUniversalTrack | AccessKeyframes |  | Unknown | 类别：const |
| GuiAnimationEditorUniversalTrack | AccessSelf |  | GuiAnimationEditorUniversalTrack | 类别：const |
| GuiAnimationEditorUniversalTrack | AddKeyframeAtMousePointer |  | void |  |
| GuiAnimationEditorUniversalTrack | CleanAssignedWidgets |  | void |  |
| GuiAnimationEditorUniversalTrack | GetAssignedWidgetsCount |  | int32 | 类别：nonconst |
| GuiAnimationEditorUniversalTrack | GetDisplayName |  | CString | 类别：nonconst |
| GuiAnimationEditorUniversalTrack | GetDuration |  | float | 类别：nonconst |
| GuiAnimationEditorUniversalTrack | GetIndentationDepth |  | int32 | 类别：nonconst |
| GuiAnimationEditorUniversalTrack | GetKeyframes |  | Unknown | 类别：nonconst |
| GuiAnimationEditorUniversalTrack | GetTimelineViewRightCornerPosition |  | CVector2f | 类别：nonconst |
| GuiAnimationEditorUniversalTrack | GetTimelineViewSize |  | CVector2f | 类别：nonconst |
| GuiAnimationEditorUniversalTrack | HasDataToAnimate |  | bool |  |
| GuiAnimationEditorUniversalTrack | IsCollapsable |  | bool |  |
| GuiAnimationEditorUniversalTrack | IsCollapsed |  | bool |  |
| GuiAnimationEditorUniversalTrack | IsInWidgetAssignmentMode |  | bool |  |
| GuiAnimationEditorUniversalTrack | IsRemovable |  | bool |  |
| GuiAnimationEditorUniversalTrack | IsTimeAtKeyframe |  | bool |  |
| GuiAnimationEditorUniversalTrack | IsTimeWithinAnimation |  | bool |  |
| GuiAnimationEditorUniversalTrack | IsTrackTypeAnimation |  | bool |  |
| GuiAnimationEditorUniversalTrack | IsTrackTypeProperty |  | bool |  |
| GuiAnimationEditorUniversalTrack | IsUnderMousePointer |  | bool |  |
| GuiAnimationEditorUniversalTrack | NextKeyframe |  | void |  |
| GuiAnimationEditorUniversalTrack | OpenTrackSelection |  | void |  |
| GuiAnimationEditorUniversalTrack | PreviousKeyframe |  | void |  |
| GuiAnimationEditorUniversalTrack | Remove |  | void |  |
| GuiAnimationEditorUniversalTrack | Self |  | GuiAnimationEditorUniversalTrack |  |
| GuiAnimationEditorUniversalTrack | ToggleCollapsed |  | void |  |
| GuiAnimationEditorUniversalTrack | ToggleKeyframe |  | void |  |
| GuiAnimationEditorUniversalTrack | ToggleWidgetAssignmentMode |  | void |  |
| GuiAnimationEditorViewportBase | AccessSelf |  | GuiAnimationEditorViewportBase | 类别：const |
| GuiAnimationEditorViewportBase | GetNeedlePosition | PdxGuiWidget float float | CVector2f | 类别：nonconst |
| GuiAnimationEditorViewportBase | Self |  | GuiAnimationEditorViewportBase |  |
| GuiAnimationEditorViewportUserInput | AccessSelf |  | GuiAnimationEditorViewportUserInput | 类别：const |
| GuiAnimationEditorViewportUserInput | GetSelectionDragRectPosition | PdxGuiWidget | CVector2f | 类别：nonconst |
| GuiAnimationEditorViewportUserInput | GetSelectionDragRectSize |  | CVector2f | 类别：nonconst |
| GuiAnimationEditorViewportUserInput | IsDraggingSelectionRect |  | bool |  |
| GuiAnimationEditorViewportUserInput | Self |  | GuiAnimationEditorViewportUserInput |  |
| GuiAnimationTimelineViewport | AccessSelf |  | GuiAnimationTimelineViewport | 类别：const |
| GuiAnimationTimelineViewport | BeginDragDuration | GuiAnimationEditorUniversalTrack | void |  |
| GuiAnimationTimelineViewport | CanBeginDragDuration |  | bool |  |
| GuiAnimationTimelineViewport | GetNeedlePosition | Unknown Unknown Unknown | CVector2f | 类别：nonconst |
| GuiAnimationTimelineViewport | Self |  | GuiAnimationTimelineViewport |  |
| GuiContext | AccessSelf |  | GuiContext | 类别：const |
| GuiContext | GetScreenResolution |  | CVector2f | 类别：nonconst |
| GuiContext | Self |  | GuiContext |  |
| GuiCurrentDrag | AccessSelf |  | GuiCurrentDrag | 类别：const |
| GuiCurrentDrag | CurrentPosition |  | CVector2f |  |
| GuiCurrentDrag | Self |  | GuiCurrentDrag |  |
| GuiCurrentDrag | StartPosition |  | CVector2f |  |
| GuiDataProfiler | AccessSelf |  | GuiDataProfiler | 类别：const |
| GuiDataProfiler | BeginRecording |  | void |  |
| GuiDataProfiler | CanBeginRecording |  | bool |  |
| GuiDataProfiler | GetCurrentDurationTypeDescription |  | CString | 类别：nonconst |
| GuiDataProfiler | GetCurrentFrame |  | uint32 | 类别：nonconst |
| GuiDataProfiler | GetDurationTypeIndex |  | CVector2i | 类别：nonconst |
| GuiDataProfiler | GetDurationTypeNames |  | Unknown | 类别：nonconst |
| GuiDataProfiler | GetDurationValueTypeIndex |  | CVector2i | 类别：nonconst |
| GuiDataProfiler | GetDurationValueTypeNames |  | Unknown | 类别：nonconst |
| GuiDataProfiler | GetNodeDuration | GuiDataProfilerEntryNode | CString | 类别：nonconst |
| GuiDataProfiler | GetNodeTree |  | Unknown | 类别：nonconst |
| GuiDataProfiler | GetNumFramesToCapture |  | uint32 | 类别：nonconst |
| GuiDataProfiler | GetSortingMethodIndex |  | CVector2i | 类别：nonconst |
| GuiDataProfiler | GetSortingMethodNames |  | Unknown | 类别：nonconst |
| GuiDataProfiler | GetTotalCapturedWidgets |  | uint32 | 类别：nonconst |
| GuiDataProfiler | GetViewTypeIndex |  | CVector2i | 类别：nonconst |
| GuiDataProfiler | GetViewTypeNames |  | Unknown | 类别：nonconst |
| GuiDataProfiler | IsCallsListView |  | bool |  |
| GuiDataProfiler | IsLocationColumnShown |  | bool |  |
| GuiDataProfiler | IsNodeExpanded | GuiDataProfilerEntryNode | bool |  |
| GuiDataProfiler | IsRecording |  | bool |  |
| GuiDataProfiler | NextFrame | int32 | void |  |
| GuiDataProfiler | Self |  | GuiDataProfiler |  |
| GuiDataProfiler | SetCurrentFrame |  | void |  |
| GuiDataProfiler | SetDurationTypeIndex |  | void |  |
| GuiDataProfiler | SetDurationValueTypeIndex |  | void |  |
| GuiDataProfiler | SetNumFramesToCapture |  | void |  |
| GuiDataProfiler | SetSortingMethodIndex |  | void |  |
| GuiDataProfiler | SetViewTypeIndex |  | void |  |
| GuiDataProfiler | ToggleLocationColumnShown |  | void |  |
| GuiDataProfiler | ToggleNodeExpanded | GuiDataProfilerEntryNode | void |  |
| GuiDataProfilerEntryNode | AccessSelf |  | GuiDataProfilerEntryNode | 类别：const |
| GuiDataProfilerEntryNode | CanOpenFileLocation |  | bool |  |
| GuiDataProfilerEntryNode | GetBranchDepth | int32 int32 | CVector2f | 类别：nonconst |
| GuiDataProfilerEntryNode | GetLocation |  | CString | 类别：nonconst |
| GuiDataProfilerEntryNode | GetName |  | Unknown | 类别：nonconst |
| GuiDataProfilerEntryNode | GetNumCalls |  | uint32 | 类别：nonconst |
| GuiDataProfilerEntryNode | HasChildren |  | bool |  |
| GuiDataProfilerEntryNode | OpenFileLocation |  | void |  |
| GuiDataProfilerEntryNode | Self |  | GuiDataProfilerEntryNode |  |
| GuiEditorTooltip | AccessSelf |  | GuiEditorTooltip | 类别：const |
| GuiEditorTooltip | GetDescription |  | CString | 类别：nonconst |
| GuiEditorTooltip | GetTitle |  | CString | 类别：nonconst |
| GuiEditorTooltip | HasDescription |  | bool |  |
| GuiEditorTooltip | HasTitle |  | bool |  |
| GuiEditorTooltip | IsVisible |  | bool |  |
| GuiEditorTooltip | Self |  | GuiEditorTooltip |  |
| GuiGameRule | AccessSelf |  | GuiGameRule | 类别：const |
| GuiGameRule | GetRule |  | GameRule | 类别：nonconst |
| GuiGameRule | GetSetting |  | GameRuleSetting | 类别：nonconst |
| GuiGameRule | Next |  | void |  |
| GuiGameRule | Prev |  | void |  |
| GuiGameRule | Self |  | GuiGameRule |  |
| GuiGameRulePreset | AccessSelf |  | GuiGameRulePreset | 类别：const |
| GuiGameRulePreset | GetName |  | CString | 类别：nonconst |
| GuiGameRulePreset | GetSettingForRule | Unknown | GameRuleSetting | 类别：nonconst |
| GuiGameRulePreset | HasRuleWithFlag | Unknown | bool |  |
| GuiGameRulePreset | IsIronmanEnabled |  | bool |  |
| GuiGameRulePreset | Self |  | GuiGameRulePreset |  |
| HQMarker | AccessSelf |  | HQMarker | 类别：const |
| HQMarker | Self |  | HQMarker |  |
| HQMovementMarker | AccessSelf |  | HQMovementMarker | 类别：const |
| HQMovementMarker | CanStationSelectedFormationsInHQ |  | bool |  |
| HQMovementMarker | GetHQ |  | Hq | 类别：nonconst |
| HQMovementMarker | GetPosition |  | CVector2f | 类别：nonconst |
| HQMovementMarker | GetPresentFormationsBreakdown |  | CString | 类别：nonconst |
| HQMovementMarker | GetTravelTimeBreakdown |  | CString | 类别：nonconst |
| HQMovementMarker | IsAllSelectedFormationsLocation |  | bool |  |
| HQMovementMarker | IsAllSelectedFormationsTarget |  | bool |  |
| HQMovementMarker | IsAnySelectedFormationsLocation |  | bool |  |
| HQMovementMarker | IsAnySelectedFormationsTarget |  | bool |  |
| HQMovementMarker | Self |  | HQMovementMarker |  |
| HarvestCondition | AccessSelf |  | HarvestCondition | 类别：const |
| HarvestCondition | GetCustom | CustomLocalization | CString | 类别：nonconst |
| HarvestCondition | GetDurationDays |  | int32 | 类别：nonconst |
| HarvestCondition | GetEffectDesc |  | CString | 类别：nonconst |
| HarvestCondition | GetIntensity |  | CFixedPoint | 类别：nonconst |
| HarvestCondition | GetName |  | CString | 类别：nonconst |
| HarvestCondition | GetNameNoFormatting |  | CString | 类别：nonconst |
| HarvestCondition | GetNameNoIcon |  | CString | 类别：nonconst |
| HarvestCondition | GetNumStates |  | int32 | 类别：nonconst |
| HarvestCondition | GetRemainingDays |  | int32 | 类别：nonconst |
| HarvestCondition | GetRemainingDuration |  | CString | 类别：nonconst |
| HarvestCondition | GetRemainingDurationLabel |  | CString | 类别：nonconst |
| HarvestCondition | GetRemainingDurationRange |  | CString | 类别：nonconst |
| HarvestCondition | GetTooltipTag |  | CString | 类别：nonconst |
| HarvestCondition | MakeScope |  | Scope |  |
| HarvestCondition | Self |  | HarvestCondition |  |
| HarvestConditionArea | AccessSelf |  | HarvestConditionArea | 类别：const |
| HarvestConditionArea | GetCustom | CustomLocalization | CString | 类别：nonconst |
| HarvestConditionArea | GetEffectDesc |  | CString | 类别：nonconst |
| HarvestConditionArea | GetHarvestConditions |  | Unknown | 类别：nonconst |
| HarvestConditionArea | GetHarvestConditionsAffecting | Country | Unknown | 类别：nonconst |
| HarvestConditionArea | GetHarvestConditionsNotAffecting | Country | Unknown | 类别：nonconst |
| HarvestConditionArea | GetIntensity |  | CFixedPoint | 类别：nonconst |
| HarvestConditionArea | GetName |  | CString | 类别：nonconst |
| HarvestConditionArea | GetNameNoFormatting |  | CString | 类别：nonconst |
| HarvestConditionArea | GetNameNoIcon |  | CString | 类别：nonconst |
| HarvestConditionArea | GetNumStates |  | int32 | 类别：nonconst |
| HarvestConditionArea | GetRemainingDays |  | int32 | 类别：nonconst |
| HarvestConditionArea | GetRemainingDuration |  | CString | 类别：nonconst |
| HarvestConditionArea | GetRemainingDurationLabel |  | CString | 类别：nonconst |
| HarvestConditionArea | GetRemainingDurationRange |  | CString | 类别：nonconst |
| HarvestConditionArea | GetTooltipTag |  | CString | 类别：nonconst |
| HarvestConditionArea | IsValid |  | bool |  |
| HarvestConditionArea | MakeScope |  | Scope |  |
| HarvestConditionArea | Self |  | HarvestConditionArea |  |
| HarvestConditionList | AccessSelf |  | HarvestConditionList | 类别：const |
| HarvestConditionList | GetNumStatesWithType | HarvestConditionType | int32 | 类别：nonconst |
| HarvestConditionList | GetStatesBreakdown | HarvestConditionType | CString | 类别：nonconst |
| HarvestConditionList | GetTypes |  | Unknown | 类别：nonconst |
| HarvestConditionList | Self |  | HarvestConditionList |  |
| HarvestConditionRegionMarker | AccessSelf |  | HarvestConditionRegionMarker | 类别：const |
| HarvestConditionRegionMarker | GetHarvestConditionAreas |  | Unknown | 类别：nonconst |
| HarvestConditionRegionMarker | GetPosition |  | CVector2f | 类别：nonconst |
| HarvestConditionRegionMarker | Self |  | HarvestConditionRegionMarker |  |
| HarvestConditionType | AccessSelf |  | HarvestConditionType | 类别：const |
| HarvestConditionType | GetColor |  | CVector4f | 类别：nonconst |
| HarvestConditionType | GetCustom | CustomLocalization | CString | 类别：nonconst |
| HarvestConditionType | GetDescription |  | CString | 类别：nonconst |
| HarvestConditionType | GetEffectDesc |  | CString | 类别：nonconst |
| HarvestConditionType | GetIcon |  | Unknown | 类别：nonconst |
| HarvestConditionType | GetName |  | CString | 类别：nonconst |
| HarvestConditionType | GetNameNoFormatting |  | CString | 类别：nonconst |
| HarvestConditionType | GetNameNoIcon |  | CString | 类别：nonconst |
| HarvestConditionType | GetTooltipTag |  | CString | 类别：nonconst |
| HarvestConditionType | MakeScope |  | Scope |  |
| HarvestConditionType | Self |  | HarvestConditionType |  |
| Heightmap | AccessSelf |  | Heightmap | 类别：const |
| Heightmap | GetHeightmapSize |  | float | 类别：nonconst |
| Heightmap | Self |  | Heightmap |  |
| HeightmapPainter | AccessSelf |  | HeightmapPainter | 类别：const |
| HeightmapPainter | GenerateAndSaveHeightmapQuadTree |  | void |  |
| HeightmapPainter | GetSmoothAmount |  | int32 | 类别：nonconst |
| HeightmapPainter | ReloadHeightmap |  | void |  |
| HeightmapPainter | Self |  | HeightmapPainter |  |
| HeightmapPainter | SetSmoothAmount |  | void |  |
| HeightmapPainterMode | AccessSelf |  | HeightmapPainterMode | 类别：const |
| HeightmapPainterMode | IsSelected |  | bool |  |
| HeightmapPainterMode | Self |  | HeightmapPainterMode |  |
| HeightmapResolution | AccessSelf |  | HeightmapResolution | 类别：const |
| HeightmapResolution | ClearSelection（清除选择） |  | void |  |
| HeightmapResolution | Decrease（减少） |  | void |  |
| HeightmapResolution | GetRectangleSelect |  | bool | 类别：非 const |
| HeightmapResolution | Increase（增加） |  | void |  |
| HeightmapResolution | InvertSelection（反选） |  | void |  |
| HeightmapResolution | Is16Bit |  | bool |  |
| HeightmapResolution | Is8Bit |  | bool |  |
| HeightmapResolution | ReloadHeightmap（重新加载高度图） |  | void |  |
| HeightmapResolution | SelectAll（全选） |  | void |  |
| HeightmapResolution | SelectedCount |  | int32 |  |
| HeightmapResolution | Self |  | HeightmapResolution |  |
| HeightmapResolution | Set16Bit |  | void |  |
| HeightmapResolution | Set8Bit |  | void |  |
| HighlightManager | AccessSelf |  | HighlightManager | 类别：const |
| HighlightManager | HighlightBattle | Battle | void |  |
| HighlightManager | HighlightBuilding | Building | void |  |
| HighlightManager | HighlightCharacter | Character | void |  |
| HighlightManager | HighlightCivilWarCountry | 未知 | void |  |
| HighlightManager | HighlightCountry | Country | void |  |
| HighlightManager | HighlightCountryCreation | CountryCreation | void |  |
| HighlightManager | HighlightCountryFormation | 未知 | void |  |
| HighlightManager | HighlightFront | Front | void |  |
| HighlightManager | HighlightGeographicRegion | GeographicRegion | void |  |
| HighlightManager | HighlightGoods | 未知 | void |  |
| HighlightManager | HighlightHQ | Hq | void |  |
| HighlightManager | HighlightHarvestConditionArea | HarvestConditionArea | void |  |
| HighlightManager | HighlightHarvestConditionType | HarvestConditionType | void |  |
| HighlightManager | HighlightInvasion | Invasion | void |  |
| HighlightManager | HighlightMarket | Market | void |  |
| HighlightManager | HighlightMilitaryFormation | MilitaryFormation | void |  |
| HighlightManager | HighlightMilitaryFormationSupplyNetwork | 未知 | void |  |
| HighlightManager | HighlightPoliticalMovement | PoliticalMovement | void |  |
| HighlightManager | HighlightPowerBloc | PowerBloc | void |  |
| HighlightManager | HighlightShippingLane | ShippingLane | void |  |
| HighlightManager | HighlightState | State | void |  |
| HighlightManager | HighlightStateOccupation | State Country | void |  |
| HighlightManager | HighlightStateRegion | StateRegion | void |  |
| HighlightManager | HighlightStateTrait | StateTrait | void |  |
| HighlightManager | HighlightStrategicObjective | State | void |  |
| HighlightManager | HighlightStrategicRegion | StrategicRegion | void |  |
| HighlightManager | HighlightSupplyNetwork | Country | void |  |
| HighlightManager | HighlightTechnology | 未知 | void |  |
| HighlightManager | HighlightTheaters | 未知 | void |  |
| HighlightManager | RemoveHighlight（移除高亮） |  | void |  |
| HighlightManager | Self |  | HighlightManager |  |
| HistoryViewer | AccessSelf |  | HistoryViewer | 类别：const |
| HistoryViewer | GetEntryName | 未知 | CString | 类别：非 const |
| HistoryViewer | IsEntryAhead | 未知 | bool |  |
| HistoryViewer | IsEntryCurrent | 未知 | bool |  |
| HistoryViewer | IsEntryExecutable | 未知 | bool |  |
| HistoryViewer | Self |  | HistoryViewer |  |
| HistoryViewer | SetEntryCurrent | 未知 | void |  |
| HomelandMarker | AccessSelf |  | HomelandMarker | 类别：const |
| HomelandMarker | GetCulture |  | Culture | 类别：非 const |
| HomelandMarker | GetPosition |  | CVector2f | 类别：非 const |
| HomelandMarker | GetState |  | State | 类别：非 const |
| HomelandMarker | Self |  | HomelandMarker |  |
| Hq | AccessSelf |  | Hq | 类别：const |
| Hq | GetCombatUnitsIcon |  | CString | 类别：非 const |
| Hq | GetCustom | CustomLocalization | CString | 类别：非 const |
| Hq | GetName |  | CString | 类别：非 const |
| Hq | GetNameNoFlag |  | CString | 类别：非 const |
| Hq | GetNameNoFlagNoConcept |  | CString | 类别：非 const |
| Hq | GetStates |  | 未知 | 类别：非 const |
| Hq | GetStationSelectedFormationsCommand |  | Command | 类别：非 const |
| Hq | GetTooltipTag |  | CString | 类别：非 const |
| Hq | IsBeingHighlighted |  | bool |  |
| Hq | IsBeingTutorialHighlighted |  | bool |  |
| Hq | IsLandHQ |  | bool |  |
| Hq | IsNavalHQ |  | bool |  |
| Hq | IsTemporaryHQ |  | bool |  |
| Hq | IsValid |  | bool |  |
| Hq | IsZoomingToHQ |  | bool |  |
| Hq | MakeScope |  | Scope |  |
| Hq | Self |  | Hq |  |
| Hq | ZoomToHQ（缩放至总部） |  | void |  |
| Ideology | AccessSelf |  | Ideology | 类别：const |
| Ideology | EndorsesLaw | Law | bool |  |
| Ideology | GetCustom | CustomLocalization | CString | 类别：非 const |
| Ideology | GetDesc |  | CString | 类别：非 const |
| Ideology | GetEndorsedLawsInLawGroup | LawGroup | 未知 | 类别：非 const |
| Ideology | GetLawGroups |  | 未知 | 类别：非 const |
| Ideology | GetLawStanceDesc |  | CString | 类别：非 const |
| Ideology | GetName |  | CString | 类别：非 const |
| Ideology | GetNameNoFormatting |  | CString | 类别：非 const |
| Ideology | GetNeutralLawsInLawGroup | LawGroup | 未知 | 类别：非 const |
| Ideology | GetOpposedLawsInLawGroup | LawGroup | 未知 | 类别：非 const |
| Ideology | GetTexture |  | 未知 | 类别：非 const |
| Ideology | GetTooltipTag |  | CString | 类别：非 const |
| Ideology | IsCharacterIdeology |  | bool |  |
| Ideology | MakeScope |  | Scope |  |
| Ideology | OpposesLaw | Law | bool |  |
| Ideology | Self |  | Ideology |  |
| ImportTool | AccessSelf |  | ImportTool | 类别：const |
| ImportTool | AreAllSelected |  | bool |  |
| ImportTool | Cancel（取消） |  | void |  |
| ImportTool | GetExportMaskTexture |  | 未知 | 类别：非 const |
| ImportTool | GetExportNotes |  | CString | 类别：非 const |
| ImportTool | GetHeightmapTexture |  | 未知 | 类别：非 const |
| ImportTool | GetMaskEffect |  | 未知 | 类别：非 const |
| ImportTool | HasExportNotes |  | bool |  |
| ImportTool | Import（导入） |  | void |  |
| ImportTool | IsImporting |  | bool |  |
| ImportTool | IsSelectedIndeterminable |  | bool |  |
| ImportTool | IsZipLoaded |  | bool |  |
| ImportTool | RefreshHeightmap（刷新高度图） |  | void |  |
| ImportTool | Self |  | ImportTool |  |
| ImportTool | SetMaskAsReferenceOverlay |  | void |  |
| ImportTool | ToggleAllSelected |  | void |  |
| Importable | AccessSelf |  | Importable | 类别：const |
| Importable | GetName |  | CString | 类别：非 const |
| Importable | IsSelected |  | bool |  |
| Importable | Self |  | Importable |  |
| Importable | SetSelected | bool | void |  |
| ImportableGroup | AccessSelf |  | ImportableGroup | 类别：const |
| ImportableGroup | AreAllSelected |  | bool |  |
| ImportableGroup | GetImportableCount |  | int32 | 类别：非 const |
| ImportableGroup | GetImportables |  | 未知 | 类别：非 const |
| ImportableGroup | GetTitle |  | CString | 类别：非 const |
| ImportableGroup | HasDiffTool |  | bool |  |
| ImportableGroup | IsCollapsed |  | bool |  |
| ImportableGroup | IsSelectedIndeterminable |  | bool |  |
| ImportableGroup | LaunchDiffTool |  | void |  |
| ImportableGroup | Self |  | ImportableGroup |  |
| ImportableGroup | ToggleAllSelected |  | void |  |
| ImportableGroup | ToggleCollapsed |  | void |  |
| ImportantAlert | AccessSelf |  | ImportantAlert | 类别：const |
| ImportantAlert | GetAlert |  | Alert | 类别：非 const |
| ImportantAlert | GetAlertGroup |  | 未知 | 类别：非 const |
| ImportantAlert | GetAlerts |  | 未知 | 类别：非 const |
| ImportantAlert | GetDescription |  | CString | 类别：非 const |
| ImportantAlert | GetName |  | CString | 类别：非 const |
| ImportantAlert | GetNumAlerts |  | int32 | 类别：非 const |
| ImportantAlert | GetTexture |  | 未知 | 类别：非 const |
| ImportantAlert | GetToolTip |  | CString | 类别：非 const |
| ImportantAlert | HasGroup |  | bool |  |
| ImportantAlert | IsAlertGroupExpanded |  | bool |  |
| ImportantAlert | IsRead |  | bool |  |
| ImportantAlert | MarkAsHidden |  | void |  |
| ImportantAlert | MarkAsRead |  | void |  |
| ImportantAlert | Self |  | ImportantAlert |  |
| ImportantAlert | ToggleAlertGroupExpanded |  | void |  |
| InfoboxNodeWindow | AccessSelf |  | InfoboxNodeWindow | 类别：const |
| InfoboxNodeWindow | GetTitleScale |  | float | 类别：非 const |
| InfoboxNodeWindow | Self |  | InfoboxNodeWindow |  |
| InformationPanel | AccessSelf |  | InformationPanel | 类别：const |
| InformationPanel | IsTabSelected | CString | bool |  |
| InformationPanel | SelectTab | CString | void |  |
| InformationPanel | Self |  | InformationPanel |  |
| InformationPanelBar | AccessSelf |  | InformationPanelBar | 类别：const |
| InformationPanelBar | ClosePanel（关闭面板） |  | void |  |
| InformationPanelBar | IsAnyPanelOpen |  | bool |  |
| InformationPanelBar | IsAvailable |  | bool |  |
| InformationPanelBar | IsPanelOpen | CString | bool |  |
| InformationPanelBar | IsPanelTabOpen | 未知 未知 | bool |  |
| InformationPanelBar | OpenAddWarGoalPanel | DiplomaticPlay Country | void |  |
| InformationPanelBar | OpenBattlePanel | Battle | void |  |
| InformationPanelBar | OpenBattlePanelTab | Battle CString | void |  |
| InformationPanelBar | OpenBattleParticipantsPanel | 未知 未知 | void |  |
| InformationPanelBar | OpenBuildingBrowserPanel | Country | void |  |
| InformationPanelBar | OpenBuildingBrowserPanelForType | 未知 未知 | void |  |
| InformationPanelBar | OpenBuildingDetailsPanel | Building | void |  |
| InformationPanelBar | OpenBuildingDetailsPanelTab | 未知 未知 | void |  |
| InformationPanelBar | OpenChangeLaw | LawGroup | void |  |
| InformationPanelBar | OpenCommanderPanel | Character | void |  |
| InformationPanelBar | OpenCompactBuildingBrowserPanel | 未知 | void |  |
| InformationPanelBar | OpenCompactBuildingBrowserPanelCycleFilters | Country CString | void |  |
| InformationPanelBar | OpenCompanyPanel | Company | void |  |
| InformationPanelBar | OpenConstructionCampPanel | 未知 | void |  |
| InformationPanelBar | OpenConstructionCampPanelTab | 未知 未知 | void |  |
| InformationPanelBar | OpenConstructionPanel | Country | void |  |
| InformationPanelBar | OpenCountryFormationPanel | CountryFormation | void |  |
| InformationPanelBar | OpenCountryPanel | Country | void |  |
| InformationPanelBar | OpenCountryPanelTab | Country CString | void |  |
| InformationPanelBar | OpenCultureInfoPanel | Culture | void |  |
| InformationPanelBar | OpenDiplomaticPlayPanel | DiplomaticPlay | void |  |
| InformationPanelBar | OpenDiplomaticPlayPanelTab | DiplomaticPlay CString | void |  |
| InformationPanelBar | OpenElectionPanel | Player | void |  |
| InformationPanelBar | OpenFrontPanel | Front | void |  |
| InformationPanelBar | OpenGoodsLocalPricesPanel | Goods | void |  |
| InformationPanelBar | OpenGoodsPanel | Market Goods | void |  |
| InformationPanelBar | OpenGoodsStatePanel | State Goods | void |  |
| InformationPanelBar | OpenGoodsUsagePanel | Goods | void |  |
| InformationPanelBar | OpenGoodsWorldMarketPanel | Goods | void |  |
| InformationPanelBar | OpenInterestGroupPanel | InterestGroup | void |  |
| InformationPanelBar | OpenInvasionPanel | Invasion | void |  |
| InformationPanelBar | OpenInvasionPanelTab | Invasion CString | void |  |
| InformationPanelBar | OpenJournalEntryPanel | JournalEntry | void |  |
| InformationPanelBar | OpenJournalEntryPanelDontToggle | 未知 | void |  |
| InformationPanelBar | OpenMarketPanel | Market | void |  |
| InformationPanelBar | OpenMarketPanelCycleTabs | Market CString CString | void |  |
| InformationPanelBar | OpenMarketPanelTab | Market CString | void |  |
| InformationPanelBar | OpenMilitaryFormationPanel | MilitaryFormation | void |  |
| InformationPanelBar | OpenMilitaryFormationPanelTab | MilitaryFormation CString | void |  |
| InformationPanelBar | OpenMilitaryPanelTab | CString | void |  |
| InformationPanelBar | OpenPanel | CString | void |  |
| InformationPanelBar | OpenPanelCycleTabs | CString CString | void |  |
| InformationPanelBar | OpenPanelDontToggle | 未知 | void |  |
| InformationPanelBar | OpenPanelTab | CString CString | void |  |
| InformationPanelBar | OpenPanelTabDontToggle | 未知 未知 | void |  |
| InformationPanelBar | OpenPartyPanel | 未知 | void |  |
| InformationPanelBar | OpenPoliticalLobbyPanel | PoliticalLobby | void |  |
| InformationPanelBar | OpenPoliticalMovementPanel | PoliticalMovement | void |  |
| InformationPanelBar | OpenPopBrowserPanel | Country | void |  |
| InformationPanelBar | OpenPopDetailsPanel | Pop | void |  |
| InformationPanelBar | OpenPowerBlocFormationPanel |  | void |  |
| InformationPanelBar | OpenPowerBlocPanel | PowerBloc | void |  |
| InformationPanelBar | OpenPowerBlocPanelTab | PowerBloc CString | void |  |
| InformationPanelBar | OpenPreviousPanel（打开上一个面板） |  | void |  |
| InformationPanelBar | OpenReligionInfoPanel | Religion | void |  |
| InformationPanelBar | OpenSeaRegionPanel | 未知 | void |  |
| InformationPanelBar | OpenSeaRegionPanelTab | Province CString | void |  |
| InformationPanelBar | OpenStatePanel | State | void |  |
| InformationPanelBar | OpenStatePanelTab | 未知 未知 | void |  |
| InformationPanelBar | OpenStatePopulationPanel | 未知 | void |  |
| InformationPanelBar | OpenSwayCountryPanel | DiplomaticPlay Country | void |  |
| InformationPanelBar | OpenTreatyDraftPanel | Treaty | void |  |
| InformationPanelBar | OpenTreatyDraftPanelForNewDraft | Country Country | void |  |
| InformationPanelBar | OpenTreatyPanel | Treaty | void |  |
| InformationPanelBar | Self |  | InformationPanelBar |  |
| InformationPanelBar | ToggleLocationFinder |  | void |  |
| InformationPanelBar | ToggleTop |  | void |  |
| IngameHud | AccessSelf |  | IngameHud | 类别：const |
| IngameHud | Self |  | IngameHud |  |
| InputActionBinding | AccessSelf |  | InputActionBinding | 类别：const |
| InputActionBinding | Self |  | InputActionBinding |  |
| InspectorPanel | AccessSelf |  | InspectorPanel | 类别：const |
| InspectorPanel | GetAnchorItems |  | 未知 | 类别：非 const |
| InspectorPanel | GetSearchFilter |  | CString | 类别：非 const |
| InspectorPanel | Self |  | InspectorPanel |  |
| InspectorPanel | SetSearchFilter |  | void |  |
| Institution | AccessInvestmentLevels |  | 未知 | 类别：const |
| Institution | AccessModifier |  | Modifier | 类别：const |
| Institution | AccessSelf |  | Institution | 类别：const |
| Institution | CanChangeLevelTo | 未知 | bool |  |
| Institution | GetBackground |  | 未知 | 类别：非 const |
| Institution | GetChangeLevelDesc | int32 | CString | 类别：非 const |
| Institution | GetCountry |  | Country | 类别：非 const |
| Institution | GetCustom | CustomLocalization | CString | 类别：非 const |
| Institution | GetDesc |  | CString | 类别：非 const |
| Institution | GetGrowDesc |  | CString | 类别：非 const |
| Institution | GetGrowthProgress |  | CFixedPoint | 类别：非 const |
| Institution | GetIcon |  | 未知 | 类别：非 const |
| Institution | GetInvestmentCost |  | CFixedPoint | 类别：非 const |
| Institution | GetInvestmentLevel |  | int32 | 类别：非 const |
| Institution | GetMaxLevel |  | int32 | 类别：非 const |
| Institution | GetModifier |  | Modifier | 类别：非 const |
| Institution | GetModifierDesc |  | CString | 类别：非 const |
| Institution | GetName |  | CString | 类别：非 const |
| Institution | GetNameNoFormatting |  | CString | 类别：非 const |
| Institution | GetProvidingLawsDesc |  | CString | 类别：非 const |
| Institution | GetShrinkDesc |  | CString | 类别：非 const |
| Institution | GetShrinkProgress |  | CFixedPoint | 类别：非 const |
| Institution | GetTargetInvestmentLevel |  | int32 | 类别：非 const |
| Institution | GetTimeToReachTargetLevelDesc |  | CString | 类别：非 const |
| Institution | GetTimedModifiersDesc |  | CString | 类别：非 const |
| Institution | GetTooltipModifierDesc |  | CString | 类别：非 const |
| Institution | GetTooltipTag |  | CString | 类别：非 const |
| Institution | IsChangingLevel |  | bool |  |
| Institution | IsGrowing |  | bool |  |
| Institution | IsShrinking |  | bool |  |
| Institution | IsValid |  | bool |  |
| Institution | MakeScope |  | Scope |  |
| Institution | Self |  | Institution |  |
| Institution | StartChangingLevelTo | int32 | Command |  |
| Institution | StartGrowing |  | Command |  |
| Institution | StartShrinking |  | Command |  |
| Institution | StopSizeChange |  | Command |  |
| InstitutionInvestmentLevel | AccessSelf |  | InstitutionInvestmentLevel | 类别：const |
| InstitutionInvestmentLevel | GetLevel |  | int32 | 类别：非 const |
| InstitutionInvestmentLevel | IsActive |  | bool |  |
| InstitutionInvestmentLevel | IsDecreasing |  | bool |  |
| InstitutionInvestmentLevel | IsDecreasingToThisLevel |  | bool |  |
| InstitutionInvestmentLevel | IsIncreasing |  | bool |  |
| InstitutionInvestmentLevel | IsIncreasingToThisLevel |  | bool |  |
| InstitutionInvestmentLevel | IsTargetLevel |  | bool |  |
| InstitutionInvestmentLevel | Self |  | InstitutionInvestmentLevel |  |
| InstitutionType | AccessSelf |  | InstitutionType | 类别：const |
| InstitutionType | GetBackground |  | 未知 | 类别：非 const |
| InstitutionType | GetCustom | CustomLocalization | CString | 类别：非 const |
| InstitutionType | GetDesc |  | CString | 类别：非 const |
| InstitutionType | GetIcon |  | 未知 | 类别：非 const |
| InstitutionType | GetModifier |  | Modifier | 类别：非 const |
| InstitutionType | GetName |  | CString | 类别：非 const |
| InstitutionType | GetNameNoFormatting |  | CString | 类别：非 const |
| InstitutionType | GetTooltipTag |  | CString | 类别：非 const |
| InstitutionType | IsValid |  | bool |  |
| InstitutionType | MakeScope |  | Scope |  |
| InstitutionType | Self |  | InstitutionType |  |
| Interest | AccessSelf |  | Interest | 类别：const |
| Interest | GetCustom | CustomLocalization | CString | 类别：非 const |
| Interest | GetIconTooltip |  | CString | 类别：非 const |
| Interest | GetInterestSourceDesc |  | CString | 类别：非 const |
| Interest | GetInterestStatusIcon |  | CString | 类别：非 const |
| Interest | GetInterestStatusName |  | CString | 类别：非 const |
| Interest | GetOwner |  | Country | 类别：非 const |
| Interest | GetProgress |  | float | 类别：非 const |
| Interest | GetProgressBarTooltip |  | CString | 类别：非 const |
| Interest | GetStrategicRegion |  | StrategicRegion | 类别：非 const |
| Interest | GetTooltipTag |  | CString | 类别：非 const |
| Interest | IsActive |  | bool |  |
| Interest | IsDeclared |  | bool |  |
| Interest | MakeScope |  | Scope |  |
| Interest | Self |  | Interest |  |
| Interest | ShouldShowProgressBar |  | bool |  |
| InterestGroup | AccessAllIdeologies |  | 未知 | 类别：const |
| InterestGroup | AccessCheapestLawsToPass |  | 未知 | 类别：const |
| InterestGroup | AccessCountry |  | Country | 类别：const |
| InterestGroup | AccessIntrinsicIdeologies |  | 未知 | 类别：const |
| InterestGroup | AccessLeader |  | Character | 类别：const |
| InterestGroup | AccessModifier |  | Modifier | 类别：const |
| InterestGroup | AccessSelf |  | InterestGroup | 类别：const |
| InterestGroup | AccessTraits |  | 未知 | 类别：const |
| InterestGroup | CalcApprovalFromLoyalties |  | int32 |  |
| InterestGroup | CalcApprovalFromLoyaltiesDesc |  | CString |  |
| InterestGroup | GetAffiliationBreakdown |  | CString | 类别：非 const |
| InterestGroup | GetAffiliationBreakdownForParty | Party | CString | 类别：非 const |
| InterestGroup | GetAffiliationRaw |  | CFixedPoint | 类别：非 const |
| InterestGroup | GetAgitators |  | 未知 | 类别：非 const |
| InterestGroup | GetAmenability |  | CFixedPoint | 类别：非 const |
| InterestGroup | GetAmenabilityLabel |  | CString | 类别：非 const |
| InterestGroup | GetApprovalRating |  | CString | 类别：非 const |
| InterestGroup | GetApprovalValue |  | int32 | 类别：非 const |
| InterestGroup | GetApprovalValueDecayIfEnactedDesc | LawType | CString | 类别：非 const |
| InterestGroup | GetApprovalValueDeltaFromEnactment | LawType | int32 | 类别：非 const |
| InterestGroup | GetApprovalValueDesc |  | CString | 类别：非 const |
| InterestGroup | GetApprovalValueIfEnacted | LawType | int32 | 类别：非 const |
| InterestGroup | GetClout |  | CFixedPoint | 类别：非 const |
| InterestGroup | GetCloutAsFloat |  | float | 类别：非 const |
| InterestGroup | GetCloutSupportingMovement | PoliticalMovement | CFixedPoint | 类别：非 const |
| InterestGroup | GetCloutTrend |  | DataTrend | 类别：非 const |
| InterestGroup | GetColor |  | CVector4f | 类别：非 const |
| InterestGroup | GetCountry |  | Country | 类别：非 const |
| InterestGroup | GetCountrySupport |  | CFixedPoint | 类别：非 const |
| InterestGroup | GetCustom | CustomLocalization | CString | 类别：非 const |
| InterestGroup | GetDesc |  | CString | 类别：非 const |
| InterestGroup | GetFractionOfCloutSupportingMovement | PoliticalMovement | CFixedPoint | 类别：非 const |
| InterestGroup | GetGraphicalLoyalistsRatioInAllInterestGroups |  | float | 类别：非 const |
| InterestGroup | GetGraphicalRadicalsRatioInAllInterestGroups |  | float | 类别：非 const |
| InterestGroup | GetID |  | uint32 | 类别：非 const |
| InterestGroup | GetIdeologyDesc |  | CString | 类别：非 const |
| InterestGroup | GetInfluenceDesc |  | CString | 类别：非 const |
| InterestGroup | GetInfluenceReason |  | CString | 类别：非 const |
| InterestGroup | GetInfluencingMovements |  | 未知 | 类别：非 const |
| InterestGroup | GetLawApprovalBreakdown | Law | CString | 类别：非 const |
| InterestGroup | GetLawApprovalValue | 未知 | int32 | 类别：非 const |
| InterestGroup | GetLawStanceLabel | LawType | CString | 类别：非 const |
| InterestGroup | GetLeader |  | Character | 类别：非 const |
| InterestGroup | GetLeaderIdeology |  | Ideology | 类别：非 const |
| InterestGroup | GetLeaderIdeologyDesc |  | CString | 类别：非 const |
| InterestGroup | GetLoyalistsPoliticalStrength |  | int64 | 类别：非 const |
| InterestGroup | GetLoyalistsTrend |  | DataTrend | 类别：非 const |
| InterestGroup | GetModifier |  | Modifier | 类别：非 const |
| InterestGroup | GetName |  | CString | 类别：非 const |
| InterestGroup | GetNameNoFormatting |  | CString | 类别：非 const |
| InterestGroup | GetNameNoIcon |  | CString | 类别：非 const |
| InterestGroup | GetNameWithCountryVariant |  | CString | 类别：非 const |
| InterestGroup | GetNumLoyalists |  | int64 | 类别：非 const |
| InterestGroup | GetNumLoyalistsRatio |  | float | 类别：非 const |
| InterestGroup | GetNumNeutrals |  | int64 | 类别：非 const |
| InterestGroup | GetNumNeutralsRatio |  | float | 类别：非 const |
| InterestGroup | GetNumPossibleLeaderIdeologies |  | int32 | 类别：非 const |
| InterestGroup | GetNumRadicals |  | int64 | 类别：非 const |
| InterestGroup | GetNumRadicalsRatio |  | float | 类别：非 const |
| InterestGroup | GetNumSupportersForMovement | PoliticalMovement | int64 | 类别：非 const |
| InterestGroup | GetParty |  | Party | 类别：非 const |
| InterestGroup | GetPartyAffiliationHighest |  | Party | 类别：非 const |
| InterestGroup | GetPartyAffiliationTooltip |  | CString | 类别：非 const |
| InterestGroup | GetPoliticalLobbies |  | 未知 | 类别：非 const |
| InterestGroup | GetPoliticalStrength |  | int64 | 类别：非 const |
| InterestGroup | GetPoliticalStrengthDesc |  | CString | 类别：非 const |
| InterestGroup | GetPoliticalStrengthInState | State | int64 | 类别：非 const |
| InterestGroup | GetPoliticalStrengthInStateAsPercentage | State | CFixedPoint | 类别：非 const |
| InterestGroup | GetPoliticallyActivePercentage |  | CFixedPoint | 类别：非常量 |
| InterestGroup | GetPoliticallyActiveRaw |  | int64 | 类别：非常量 |
| InterestGroup | GetPopPotentialDesc |  | CString | 类别：非常量 |
| InterestGroup | GetPopWithIG | 未知 | PopWithIG | 类别：非常量 |
| InterestGroup | GetPopulation |  | int64 | 类别：非常量 |
| InterestGroup | GetPopulationAsFloat |  | float | 类别：非常量 |
| InterestGroup | GetPopulationInCountryAsPercentage |  | CFixedPoint | 类别：非常量 |
| InterestGroup | GetPopulationInState | State | int64 | 类别：非常量 |
| InterestGroup | GetPopulationNonZero |  | int64 | 类别：非常量 |
| InterestGroup | GetPossibleCharacterLeaderIdeologies |  | 未知 | 类别：非常量 |
| InterestGroup | GetPossibleRandomLeaderIdeologies |  | 未知 | 类别：非常量 |
| InterestGroup | GetRadicalsPoliticalStrength |  | int64 | 类别：非常量 |
| InterestGroup | GetRadicalsTrend |  | DataTrend | 类别：非常量 |
| InterestGroup | GetStatusTooltip |  | CString | 类别：非常量 |
| InterestGroup | GetSupportingPopTypesDesc |  | CString | 类别：非常量 |
| InterestGroup | GetTextIcon |  | CString | 类别：非常量 |
| InterestGroup | GetTexture |  | 未知 | 类别：非常量 |
| InterestGroup | GetTooltipTag |  | CString | 类别：非常量 |
| InterestGroup | GetTotalPoliticalStrengthIncludingPartyVotes |  | int64 | 类别：非常量 |
| InterestGroup | GetTraitsDesc |  | CString | 类别：非常量 |
| InterestGroup | GetWillJoinPartyDesc |  | CString | 类别：非常量 |
| InterestGroup | GetWillJoinPartyTooltip |  | CString | 类别：非常量 |
| InterestGroup | HasNegotiated |  | bool |  |
| InterestGroup | HasParty |  | bool |  |
| InterestGroup | IsEndorsingLawEnactment | 未知 | bool |  |
| InterestGroup | IsInGovernment |  | bool |  |
| InterestGroup | IsIndifferentToLawEnactment | 未知 | bool |  |
| InterestGroup | IsInfluencedByMovement | 未知 | bool |  |
| InterestGroup | IsInsurrectionary |  | bool |  |
| InterestGroup | IsLeaderInfluencingEnactment | LawType | bool |  |
| InterestGroup | IsLeadingGovernment |  | bool |  |
| InterestGroup | IsMarginal |  | bool |  |
| InterestGroup | IsNegotiating |  | bool |  |
| InterestGroup | IsOpposingLawEnactment | Law | bool |  |
| InterestGroup | IsPinnedInOutliner |  | bool |  |
| InterestGroup | IsPowerful |  | bool |  |
| InterestGroup | IsRevolutionary |  | bool |  |
| InterestGroup | IsSecessionist |  | bool |  |
| InterestGroup | IsValid |  | bool |  |
| InterestGroup | MakeScope |  | Scope |  |
| InterestGroup | PredictLegitimacyChangeDesc |  | CString |  |
| InterestGroup | PredictLegitimacyChangeToSwitch |  | CFixedPoint |  |
| InterestGroup | Self |  | InterestGroup |  |
| InterestGroup | TogglePinInOutliner |  | void |  |
| InterestGroup | WillRadicalizeIfEnacted | LawType | bool |  |
| InterestGroupAndTraitPair | AccessInterestGroup |  | InterestGroup | 类别：常量 |
| InterestGroupAndTraitPair | AccessSelf |  | InterestGroupAndTraitPair | 类别：常量 |
| InterestGroupAndTraitPair | GetInterestGroup |  | InterestGroup | 类别：非常量 |
| InterestGroupAndTraitPair | GetTrait |  | InterestGroupTrait | 类别：非常量 |
| InterestGroupAndTraitPair | Self |  | InterestGroupAndTraitPair |  |
| InterestGroupMarker | AccessInterestGroup |  | InterestGroup | 类别：常量 |
| InterestGroupMarker | AccessSelf |  | InterestGroupMarker | 类别：常量 |
| InterestGroupMarker | GetInterestGroup |  | InterestGroup | 类别：非常量 |
| InterestGroupMarker | GetPosition |  | CVector2f | 类别：非常量 |
| InterestGroupMarker | Self |  | InterestGroupMarker |  |
| InterestGroupPanel | AccessInterestGroup |  | InterestGroup | 类别：常量 |
| InterestGroupPanel | AccessPops |  | 未知 | 类别：常量 |
| InterestGroupPanel | AccessPopsList |  | PopList | 类别：常量 |
| InterestGroupPanel | AccessSelf |  | InterestGroupPanel | 类别：常量 |
| InterestGroupPanel | GetInterestGroup |  | InterestGroup | 类别：非常量 |
| InterestGroupPanel | Self |  | InterestGroupPanel |  |
| InterestGroupTrait | AccessSelf |  | InterestGroupTrait | 类别：常量 |
| InterestGroupTrait | GetBaseModifiersDesc |  | CString | 类别：非常量 |
| InterestGroupTrait | GetBaseTriggersDesc |  | CString | 类别：非常量 |
| InterestGroupTrait | GetCustom | CustomLocalization | CString | 类别：非常量 |
| InterestGroupTrait | GetDesc |  | CString | 类别：非常量 |
| InterestGroupTrait | GetInactiveString | InterestGroup | CString | 类别：非常量 |
| InterestGroupTrait | GetModifiersDesc | InterestGroup | CString | 类别：非常量 |
| InterestGroupTrait | GetName | InterestGroup | CString | 类别：非常量 |
| InterestGroupTrait | GetNameNoFormatting |  | CString | 类别：非常量 |
| InterestGroupTrait | GetNameWithStatus | 未知 | CString | 类别：非常量 |
| InterestGroupTrait | GetTexture |  | 未知 | 类别：非常量 |
| InterestGroupTrait | GetTooltipTag |  | CString | 类别：非常量 |
| InterestGroupTrait | GetTriggersDesc | InterestGroup | CString | 类别：非常量 |
| InterestGroupTrait | IsEnabled | InterestGroup | bool |  |
| InterestGroupTrait | MakeScope |  | Scope |  |
| InterestGroupTrait | Self |  | InterestGroupTrait |  |
| InterestingCountryItem | AccessSelf |  | InterestingCountryItem | 类别：常量 |
| InterestingCountryItem | GetCountry |  | Country | 类别：非常量 |
| InterestingCountryItem | GetSetting |  | InterestingCountrySetting | 类别：非常量 |
| InterestingCountryItem | OnSelectOption |  | void |  |
| InterestingCountryItem | Self |  | InterestingCountryItem |  |
| InterestingCountrySetting | AccessSelf |  | InterestingCountrySetting | 类别：常量 |
| InterestingCountrySetting | GetIsActiveDesc | 未知 | CString | 类别：非常量 |
| InterestingCountrySetting | GetName |  | CString | 类别：非常量 |
| InterestingCountrySetting | Self |  | InterestingCountrySetting |  |
| Invasion | AccessSelf |  | Invasion | 类别：常量 |
| Invasion | CanFormationBlockLanding | 未知 | bool |  |
| Invasion | Cancel |  | Command |  |
| Invasion | DeployArmyToDefend | MilitaryFormation | Command |  |
| Invasion | DeployFleetToDefend | MilitaryFormation | Command |  |
| Invasion | GetActiveLandBattles |  | 未知 | 类别：非常量 |
| Invasion | GetActiveNavalBattles |  | 未知 | 类别：非常量 |
| Invasion | GetAdvancementProgress |  | CFixedPoint | 类别：非常量 |
| Invasion | GetArmy |  | MilitaryFormation | 类别：非常量 |
| Invasion | GetBlockingFleets |  | 未知 | 类别：非常量 |
| Invasion | GetCustom | CustomLocalization | CString | 类别：非常量 |
| Invasion | GetDefenderHQ |  | Hq | 类别：非常量 |
| Invasion | GetDefendingArmies |  | 未知 | 类别：非常量 |
| Invasion | GetDefendingArmiesTooltipBreakdown |  | CString | 类别：非常量 |
| Invasion | GetDefendingFleets |  | 未知 | 类别：非常量 |
| Invasion | GetDefendingFleetsTooltipBreakdown |  | CString | 类别：非常量 |
| Invasion | GetDeploySelectedFormationsCommand |  | Command | 类别：非常量 |
| Invasion | GetEndedLandBattles |  | 未知 | 类别：非常量 |
| Invasion | GetEndedNavalBattles |  | 未知 | 类别：非常量 |
| Invasion | GetEnemyState |  | State | 类别：非常量 |
| Invasion | GetFleet |  | MilitaryFormation | 类别：非常量 |
| Invasion | GetFront |  | Front | 类别：非常量 |
| Invasion | GetInvadedCountry |  | Country | 类别：非常量 |
| Invasion | GetInvaderCountry |  | Country | 类别：非常量 |
| Invasion | GetInvadingArmies |  | 未知 | 类别：非常量 |
| Invasion | GetInvadingArmiesTooltipBreakdown |  | CString | 类别：非常量 |
| Invasion | GetInvadingFleets |  | 未知 | 类别：非常量 |
| Invasion | GetInvadingFleetsTooltipBreakdown |  | CString | 类别：非常量 |
| Invasion | GetLandingProgress |  | CFixedPoint | 类别：非常量 |
| Invasion | GetMaxLandBattleDefeatsAtZeroOccupation |  | int32 | 类别：非常量 |
| Invasion | GetName |  | CString | 类别：非常量 |
| Invasion | GetNonBlockingFleets |  | 未知 | 类别：非常量 |
| Invasion | GetNumBlockingFleets |  | int32 | 类别：非常量 |
| Invasion | GetNumBlockingFleetsUnits |  | int32 | 类别：非常量 |
| Invasion | GetNumDefendingArmies |  | int32 | 类别：非常量 |
| Invasion | GetNumDefendingArmiesUnits |  | int32 | 类别：非常量 |
| Invasion | GetNumDefendingFleets |  | int32 | 类别：非常量 |
| Invasion | GetNumDefendingFleetsUnits |  | int32 | 类别：非常量 |
| Invasion | GetNumInvadingArmies |  | int32 | 类别：非常量 |
| Invasion | GetNumInvadingArmiesUnits |  | int32 | 类别：非常量 |
| Invasion | GetNumInvadingFleets |  | int32 | 类别：非常量 |
| Invasion | GetNumInvadingFleetsUnits |  | int32 | 类别：非常量 |
| Invasion | GetNumLandBattleDefeatsAtZeroOccupation |  | int32 | 类别：非常量 |
| Invasion | GetNumNonBlockingFleets |  | int32 | 类别：非常量 |
| Invasion | GetNumNonBlockingFleetsUnits |  | int32 | 类别：非常量 |
| Invasion | GetPreparationDaysLeftRaw |  | int32 | 类别：非常量 |
| Invasion | GetProgress |  | CFixedPoint | 类别：非常量 |
| Invasion | GetSeaNode |  | Province | 类别：非常量 |
| Invasion | GetSeaNodeName |  | CString | 类别：非常量 |
| Invasion | GetSourceState |  | State | 类别：非常量 |
| Invasion | GetStatus |  | CString | 类别：非常量 |
| Invasion | GetTargetState |  | State | 类别：非常量 |
| Invasion | GetTooltipTag |  | CString | 类别：非常量 |
| Invasion | HasBlockingEnemyFleetOnSeaNode |  | bool |  |
| Invasion | HasEnded |  | bool |  |
| Invasion | HasFailed |  | bool |  |
| Invasion | HasSucceeded |  | bool |  |
| Invasion | IsBeingHighlighted |  | bool |  |
| Invasion | IsBeingTutorialHighlighted |  | bool |  |
| Invasion | IsFightingLandBattle |  | bool |  |
| Invasion | IsFightingNavalBattle |  | bool |  |
| Invasion | IsLandInvasion |  | bool |  |
| Invasion | IsNavalInvasion |  | bool |  |
| Invasion | IsOnInvaderSide | Country | bool |  |
| Invasion | IsPreparing |  | bool |  |
| Invasion | IsRelevantForCountry | Country | bool |  |
| Invasion | IsStalledDueToCommanderOrders |  | bool |  |
| Invasion | IsValid |  | bool |  |
| Invasion | IsWaiting |  | bool |  |
| Invasion | IsZoomingToMapMarkerPosition |  | bool |  |
| Invasion | MakeScope |  | Scope |  |
| Invasion | Self |  | Invasion |  |
| Invasion | ZoomToMapMarkerPosition |  | void |  |
| InvasionMarker | AccessSelf |  | InvasionMarker | 类别：常量 |
| InvasionMarker | CanDeploySelectedFormationsToDefend |  | bool |  |
| InvasionMarker | GetPosition |  | CVector2f | 类别：非常量 |
| InvasionMarker | Self |  | InvasionMarker |  |
| InvasionPanel | AccessSelf |  | InvasionPanel | 类别：常量 |
| InvasionPanel | Self |  | InvasionPanel |  |
| InvasionPlannerPopup | AccessSelf |  | InvasionPlannerPopup | 类别：常量 |
| InvasionPlannerPopup | CanLandInvade |  | bool |  |
| InvasionPlannerPopup | CanMilitaryFormationBeSelected | MilitaryFormation | bool |  |
| InvasionPlannerPopup | CanNavalInvade |  | bool |  |
| InvasionPlannerPopup | GetArmyDaysDesc |  | CString | 类别：非常量 |
| InvasionPlannerPopup | GetCanMilitaryFormationBeSelectedTooltip | MilitaryFormation | CString | 类别：非常量 |
| InvasionPlannerPopup | GetCommandValidityDesc |  | CString | 类别：非常量 |
| InvasionPlannerPopup | GetEfficiencyRaw |  | CFixedPoint | 类别：非常量 |
| InvasionPlannerPopup | GetFleetDaysDesc |  | CString | 类别：非常量 |
| InvasionPlannerPopup | GetLandingPenaltyModifierMultiplier |  | CFixedPoint | 类别：非常量 |
| InvasionPlannerPopup | GetSelectedAdmirals |  | 未知 | 类别：非常量 |
| InvasionPlannerPopup | GetSelectedArmies |  | 未知 | 类别：非常量 |
| InvasionPlannerPopup | GetSelectedFleets |  | 未知 | 类别：非常量 |
| InvasionPlannerPopup | GetSelectedGenerals |  | 未知 | 类别：非常量 |
| InvasionPlannerPopup | GetSlowestArmy |  | MilitaryFormation | 类别：非常量 |
| InvasionPlannerPopup | GetSlowestFleet |  | MilitaryFormation | 类别：非常量 |
| InvasionPlannerPopup | GetSourceState |  | State | 类别：非常量 |
| InvasionPlannerPopup | GetTargetState |  | State | 类别：非常量 |
| InvasionPlannerPopup | GetTravelDaysDesc |  | CString | 类别：非常量 |
| InvasionPlannerPopup | GetTravelTimeDesc |  | CString | 类别：非常量 |
| InvasionPlannerPopup | HasAdvancingGeneral |  | bool |  |
| InvasionPlannerPopup | HasInterceptingAdmiral |  | bool |  |
| InvasionPlannerPopup | HasNavalInvasionContext |  | bool |  |
| InvasionPlannerPopup | HasSelectedNecessaryFormations |  | bool |  |
| InvasionPlannerPopup | IsMilitaryFormationSelected | 未知 | bool |  |
| InvasionPlannerPopup | OnSelectedArmy | 未知 | void |  |
| InvasionPlannerPopup | OnSelectedFleet | 未知 | void |  |
| InvasionPlannerPopup | RemoveFormation | 未知 | void |  |
| InvasionPlannerPopup | Self |  | InvasionPlannerPopup |  |
| InvasionPlannerPopup | StartInvasion |  | Command |  |
| JominiGUISetting | AccessSelf |  | JominiGUISetting | 类别：常量 |
| JominiGUISetting | GetDesc |  | CString | 类别：非常量 |
| JominiGUISetting | HasChanged |  | bool |  |
| JominiGUISetting | HasChangedSinceStartup |  | bool |  |
| JominiGUISetting | Self |  | JominiGUISetting |  |
| JominiGUISetting | ShouldShow |  | bool |  |
| JominiGameRules | AccessSelf |  | JominiGameRules | 类别：常量 |
| JominiGameRules | ApplySettings |  | void |  |
| JominiGameRules | DeletePresetAtIndex | int32 | void |  |
| JominiGameRules | DeletePresetWithName | CString | void |  |
| JominiGameRules | GetInvalidPresetNameTooltip |  | CString | 类别：非常量 |
| JominiGameRules | GetPresetSaveName |  | CString | 类别：非常量 |
| JominiGameRules | GetRulePresets |  | 未知 | 类别：非常量 |
| JominiGameRules | GetSelectedPreset |  | GuiGameRulePreset | 类别：非常量 |
| JominiGameRules | GetSelectedPresetIndex |  | int32 | 类别：非常量 |
| JominiGameRules | GetSettings |  | 未知 | 类别：非常量 |
| JominiGameRules | HasPresetWithName | CString | bool |  |
| JominiGameRules | HasRuleWithFlag | 未知 | bool |  |
| JominiGameRules | HasValidPresetSelected |  | bool |  |
| JominiGameRules | Hide |  | void |  |
| JominiGameRules | HidePresetWindow |  | void |  |
| JominiGameRules | IsIronman |  | bool |  |
| JominiGameRules | IsPresetWindowShown |  | bool |  |
| JominiGameRules | IsValidPresetName |  | bool |  |
| JominiGameRules | OnPresetSaveNameChange | 未知 | void |  |
| JominiGameRules | OnPresetSaveNameEdit |  | void |  |
| JominiGameRules | OnSelectPreset |  | void |  |
| JominiGameRules | ResetAllToDefaults |  | void |  |
| JominiGameRules | SavePreset |  | void |  |
| JominiGameRules | Self |  | JominiGameRules |  |
| JominiGameRules | SetIronman | 未知 | void |  |
| JominiGameRules | SetPresetSaveName |  | void |  |
| JominiGameRules | ShowPresetWindow |  | void |  |
| JominiNotification | AccessSelf |  | JominiNotification | 类别：常量 |
| JominiNotification | GetAcceptButtonText |  | CString | 类别：非常量 |
| JominiNotification | GetDate |  | Date | 类别：非常量 |
| JominiNotification | GetDateOrTimestamp |  | CString | 类别：非常量 |
| JominiNotification | GetDeclineButtonText |  | CString | 类别：非常量 |
| JominiNotification | GetText |  | CString | 类别：非常量 |
| JominiNotification | GetTimestamp |  | CString | 类别：非常量 |
| JominiNotification | GetTitle |  | CString | 类别：非常量 |
| JominiNotification | HasDate |  | bool |  |
| JominiNotification | HasOnAccept |  | bool |  |
| JominiNotification | HasOnDecline |  | bool |  |
| JominiNotification | OnAccept |  | void |  |
| JominiNotification | OnDecline |  | void |  |
| JominiNotification | OnNotificationClick |  | void |  |
| JominiNotification | Self |  | JominiNotification |  |
| JominiNotificationOverlay | AccessSelf |  | JominiNotificationOverlay | 类别：常量 |
| JominiNotificationOverlay | GetAlertCount |  | int32 | 类别：非常量 |
| JominiNotificationOverlay | GetAlerts |  | 未知 | 类别：非常量 |
| JominiNotificationOverlay | GetNotificationCategoryCount | 未知 | int32 | 类别：非常量 |
| JominiNotificationOverlay | GetNotificationCount |  | int32 | 类别：非常量 |
| JominiNotificationOverlay | GetNotifications |  | 未知 | 类别：非常量 |
| JominiNotificationOverlay | HideSidebar |  | void |  |
| JominiNotificationOverlay | Self |  | JominiNotificationOverlay |  |
| JominiNotificationOverlay | ShowSidebar |  | void |  |
| JominiNotificationOverlay | ToggleSidebar |  | void |  |
| JominiPasswordPopup | AccessSelf |  | JominiPasswordPopup | 类别：常量 |
| JominiPasswordPopup | OnDecline |  | void |  |
| JominiPasswordPopup | OnSubmit |  | void |  |
| JominiPasswordPopup | Self |  | JominiPasswordPopup |  |
| JominiServer | AccessSelf |  | JominiServer | 类别：常量 |
| JominiServer | GetHasPassword |  | bool | 类别：非常量 |
| JominiServer | GetMaxPlayers |  | int32 | 类别：非常量 |
| JominiServer | GetName |  | CString | 类别：非常量 |
| JominiServer | GetNumPlayers |  | int32 | 类别：非常量 |
| JominiServer | GetStatus |  | CString | 类别：非常量 |
| JominiServer | GetVersion |  | CString | 类别：非常量 |
| JominiServer | IsSameVersion |  | bool |  |
| JominiServer | Join |  | void |  |
| JominiServer | Self |  | JominiServer |  |
| JominiServerBrowserGui | AccessSelf |  | JominiServerBrowserGui | 类别：常量 |
| JominiServerBrowserGui | AccessServers |  | 未知 | 类别：常量 |
| JominiServerBrowserGui | GetServers |  | 未知 | 类别：非常量 |
| JominiServerBrowserGui | IsCrossPlatformFilterSet |  | bool |  |
| JominiServerBrowserGui | IsEmptyFilterSet |  | bool |  |
| JominiServerBrowserGui | IsFullFilterSet |  | bool |  |
| JominiServerBrowserGui | IsHasPasswordFilterSet |  | bool |  |
| JominiServerBrowserGui | IsRefreshing |  | bool |  |
| JominiServerBrowserGui | IsSameModsFilterSet |  | bool |  |
| JominiServerBrowserGui | IsSameVersionFilterSet |  | bool |  |
| JominiServerBrowserGui | IsSortAscending |  | bool |  |
| JominiServerBrowserGui | IsSortedBy | 未知 | bool |  |
| JominiServerBrowserGui | JoinServerWithId |  | void |  |
| JominiServerBrowserGui | JoinServerWithTextWidget | 未知 | void |  |
| JominiServerBrowserGui | OnFilterTextEdit |  | void |  |
| JominiServerBrowserGui | RefreshServers |  | void |  |
| JominiServerBrowserGui | Self |  | JominiServerBrowserGui |  |
| JominiServerBrowserGui | SetFilterText |  | void |  |
| JominiServerBrowserGui | SetServerId |  | void |  |
| JominiServerBrowserGui | Sort | CString | void |  |
| JominiServerBrowserGui | ToggleCrossPlatformFilter |  | void |  |
| JominiServerBrowserGui | ToggleEmptyFilter |  | void |  |
| JominiServerBrowserGui | ToggleFullFilter |  | void |  |
| JominiServerBrowserGui | ToggleHasPasswordFilter |  | void |  |
| JominiServerBrowserGui | ToggleSameModsFilter |  | void |  |
| JominiServerBrowserGui | ToggleSameVersionFilter |  | void |  |
| JominiSettingsWindow | AccessActivePage |  | SettingsPage | 类别：常量 |
| JominiSettingsWindow | AccessPages |  | 未知 | 类别：常量 |
| JominiSettingsWindow | AccessSelf |  | JominiSettingsWindow | 类别：常量 |
| JominiSettingsWindow | AllowApply |  | bool |  |
| JominiSettingsWindow | AppliedOnApply |  | bool |  |
| JominiSettingsWindow | AppliedOnRestart |  | bool |  |
| JominiSettingsWindow | Close |  | void |  |
| JominiSettingsWindow | GetInputActionName | InputActionBinding | CString | 类别：非常量 |
| JominiSettingsWindow | GetInputBindingText |  | CString | 类别：非常量 |
| JominiSettingsWindow | GetKeyCodeName | InputActionBinding int32 | CString | 类别：非常量 |
| JominiSettingsWindow | GetUserBindingFileName |  | CString | 类别：非常量 |
| JominiSettingsWindow | GetWarningText |  | CString | 类别：非常量 |
| JominiSettingsWindow | HasChanged |  | bool |  |
| JominiSettingsWindow | HasUserBindingFileName |  | bool |  |
| JominiSettingsWindow | Hide |  | void |  |
| JominiSettingsWindow | IsConfirmButtonEnabled |  | bool |  |
| JominiSettingsWindow | IsCurrentActivePageId | 未知 | bool |  |
| JominiSettingsWindow | IsInputPopUpEnabled |  | bool |  |
| JominiSettingsWindow | OnApply |  | void |  |
| JominiSettingsWindow | OnClickCancel |  | void |  |
| JominiSettingsWindow | OnClickClear |  | void |  |
| JominiSettingsWindow | OnClickConfirm |  | void |  |
| JominiSettingsWindow | OnClickLoadDefaultProfile |  | void |  |
| JominiSettingsWindow | OnClickLoadProfile |  | void |  |
| JominiSettingsWindow | OnClickSaveProfile |  | void |  |
| JominiSettingsWindow | OnEditProfileFileName |  | void |  |
| JominiSettingsWindow | RequireRestart |  | bool |  |
| JominiSettingsWindow | Restore |  | void |  |
| JominiSettingsWindow | Save |  | void |  |
| JominiSettingsWindow | SaveAndClose |  | void |  |
| JominiSettingsWindow | Self |  | JominiSettingsWindow |  |
| JominiSettingsWindow | ShouldShowWarningText |  | bool |  |
| JominiSettingsWindow | Show |  | void |  |
| JominiSettingsWindow | ShowInputPopUp | CPdxInputBindingSetting InputActionBinding int32 | void |  |
| JournalEntry | AccessModifier |  | Modifier | 类别：常量 |
| JournalEntry | AccessSelf |  | JournalEntry | 类别：常量 |
| JournalEntry | CalcCurrentGoalValue |  | CFixedPoint |  |
| JournalEntry | CalcInitialGoalAddValue |  | CFixedPoint |  |
| JournalEntry | CanComplete |  | bool |  |
| JournalEntry | CanStartTutorialLesson |  | bool |  |
| JournalEntry | CanStartTutorialLessonDesc |  | CString |  |
| JournalEntry | CanTimeOut |  | bool |  |
| JournalEntry | GetActivationTooltip |  | CString | 类别：非常量 |
| JournalEntry | GetBaselineValue |  | CFixedPoint | 类别：非常量 |
| JournalEntry | GetBuildingTarget |  | Building | 类别：非常量 |
| JournalEntry | GetCompletionTooltip |  | CString | 类别：非常量 |
| JournalEntry | GetCountry |  | Country | 类别：非常量 |
| JournalEntry | GetCurrentBarProgress | ScriptedProgressBar | float | 类别：非常量 |
| JournalEntry | GetCurrentBarValue | ScriptedProgressBar | CFixedPoint | 类别：非常量 |
| JournalEntry | GetCustom | CustomLocalization | CString | 类别：非常量 |
| JournalEntry | GetFailureTooltip |  | CString | 类别：非常量 |
| JournalEntry | GetGoalAddValue |  | CFixedPoint | 类别：非常量 |
| JournalEntry | GetGoalDesc |  | CString | 类别：非常量 |
| JournalEntry | GetGoalProgressPercent |  | CFixedPoint | 类别：非常量 |
| JournalEntry | GetGoalProgressValue |  | CFixedPoint | 类别：非常量 |
| JournalEntry | GetIcon |  | 未知 | 类别：非常量 |
| JournalEntry | GetInvalidationTooltip |  | CString | 类别：非常量 |
| JournalEntry | GetInvolvedCountries |  | 未知 | 类别：非常量 |
| JournalEntry | GetInvolvedCountriesDesc |  | CString | 类别：非常量 |
| JournalEntry | GetModifier |  | Modifier | 类别：非常量 |
| JournalEntry | GetName |  | CString | 类别：非常量 |
| JournalEntry | GetNumPossibleScriptedButtons |  | int32 | 类别：非常量 |
| JournalEntry | GetOnActivationTooltip |  | CString | 类别：非常量 |
| JournalEntry | GetOnCompleteTooltip |  | CString | 类别：非常量 |
| JournalEntry | GetOnFailTooltip |  | CString | 类别：非常量 |
| JournalEntry | GetOnInvalidationTooltip |  | CString | 类别：非常量 |
| JournalEntry | GetOnTimeoutTooltip |  | CString | 类别：非常量 |
| JournalEntry | GetProgressDesc |  | CString | 类别：非常量 |
| JournalEntry | GetReason |  | CString | 类别：非常量 |
| JournalEntry | GetRemainingProgressValue |  | CFixedPoint | 类别：nonconst |
| JournalEntry | GetScriptedButtons |  | Unknown | 类别：nonconst |
| JournalEntry | GetScriptedProgressBars |  | Unknown | 类别：nonconst |
| JournalEntry | GetStatusDesc |  | CString | 类别：nonconst |
| JournalEntry | GetTarget |  | Scope | 类别：nonconst |
| JournalEntry | GetTimedModifiers |  | Unknown | 类别：nonconst |
| JournalEntry | GetTimedModifiersTooltip |  | CString | 类别：nonconst |
| JournalEntry | GetTimeoutDaysLeft |  | int32 | 类别：nonconst |
| JournalEntry | GetTimeoutTooltip |  | CString | 类别：nonconst |
| JournalEntry | GetTooltip |  | CString | 类别：nonconst |
| JournalEntry | GetTooltipTag |  | CString | 类别：nonconst |
| JournalEntry | GetTotalGoalValue |  | CFixedPoint | 类别：nonconst |
| JournalEntry | GetType |  | JournalEntryType | 类别：nonconst |
| JournalEntry | HasGoal |  | bool |  |
| JournalEntry | HasHowTutorialLesson |  | bool |  |
| JournalEntry | HasProgressBar |  | bool |  |
| JournalEntry | HasWhyTutorialLesson |  | bool |  |
| JournalEntry | IsActive |  | bool |  |
| JournalEntry | IsBeingHighlighted |  | bool |  |
| JournalEntry | IsBeingTutorialHighlighted |  | bool |  |
| JournalEntry | IsComplete |  | bool |  |
| JournalEntry | IsContextless |  | bool |  |
| JournalEntry | IsDead |  | bool |  |
| JournalEntry | IsPinnedInOutliner |  | bool |  |
| JournalEntry | IsProgressing |  | bool |  |
| JournalEntry | IsValid |  | bool |  |
| JournalEntry | MakeScope |  | Scope |  |
| JournalEntry | Self |  | JournalEntry |  |
| JournalEntry | ShowProgressbarAsMonths |  | bool |  |
| JournalEntry | ShowProgressbarAsTime |  | bool |  |
| JournalEntry | ShowProgressbarAsWeeks |  | bool |  |
| JournalEntry | StartHowTutorialLesson |  | void |  |
| JournalEntry | StartWhyTutorialLesson |  | void |  |
| JournalEntry | TogglePinInOutliner |  | void |  |
| JournalEntryGroup | AccessSelf |  | JournalEntryGroup | 类别：const |
| JournalEntryGroup | GetActiveJournalEntryTypes | Country | Unknown | 类别：nonconst |
| JournalEntryGroup | GetInactiveJournalEntryTypes | Unknown | Unknown | 类别：nonconst |
| JournalEntryGroup | GetKey |  | CString | 类别：nonconst |
| JournalEntryGroup | GetName |  | CString | 类别：nonconst |
| JournalEntryGroup | GetTooltipTag |  | CString | 类别：nonconst |
| JournalEntryGroup | Self |  | JournalEntryGroup |  |
| JournalEntryPanel | AccessJournalEntry |  | JournalEntry | 类别：const |
| JournalEntryPanel | AccessSelf |  | JournalEntryPanel | 类别：const |
| JournalEntryPanel | GetJournalEntry |  | JournalEntry | 类别：nonconst |
| JournalEntryPanel | Self |  | JournalEntryPanel |  |
| JournalEntryType | AccessSelf |  | JournalEntryType | 类别：const |
| JournalEntryType | GetGroup |  | JournalEntryGroup | 类别：nonconst |
| JournalEntryType | GetIcon |  | Unknown | 类别：nonconst |
| JournalEntryType | GetLobbyDesc |  | CString | 类别：nonconst |
| JournalEntryType | GetName |  | CString | 类别：nonconst |
| JournalEntryType | GetTooltipTag |  | CString | 类别：nonconst |
| JournalEntryType | Self |  | JournalEntryType |  |
| JournalPanel | AccessSelf |  | JournalPanel | 类别：const |
| JournalPanel | Self |  | JournalPanel |  |
| KeyframeEditor | AccessSelf |  | KeyframeEditor | 类别：const |
| KeyframeEditor | OnLaneClick | PdxGuiWidget | void |  |
| KeyframeEditor | Self |  | KeyframeEditor |  |
| KeyframeEventEditor | AccessSelf |  | KeyframeEventEditor | 类别：const |
| KeyframeEventEditor | EventDescription |  | Unknown |  |
| KeyframeEventEditor | HasEvent |  | bool |  |
| KeyframeEventEditor | HasKeyframe |  | bool |  |
| KeyframeEventEditor | IsAudioHandler |  | bool |  |
| KeyframeEventEditor | IsVfxHandler |  | bool |  |
| KeyframeEventEditor | KeyframeEditorId |  | Unknown |  |
| KeyframeEventEditor | KeyframeId |  | CString |  |
| KeyframeEventEditor | Self |  | KeyframeEventEditor |  |
| KeyframeWidget | AccessSelf |  | KeyframeWidget | 类别：const |
| KeyframeWidget | GetValue |  | float | 类别：nonconst |
| KeyframeWidget | Self |  | KeyframeWidget |  |
| Label | AccessSelf |  | Label | 类别：const |
| Label | GetDesc |  | CString | 类别：nonconst |
| Label | GetName |  | CString | 类别：nonconst |
| Label | GetTooltipTag |  | CString | 类别：nonconst |
| Label | GetTypeList |  | CString | 类别：nonconst |
| Label | Self |  | Label |  |
| LabelingHelper | AccessSelf |  | LabelingHelper | 类别：const |
| LabelingHelper | CapitalizeOnlyFirst | CString | CString |  |
| LabelingHelper | GetDaysLocWithTooltip | int32 Localization | CString | 类别：nonconst |
| LabelingHelper | GetDaysLocWithoutTooltip | int32 | CString | 类别：nonconst |
| LabelingHelper | GetFormattedDays | int32 | CString | 类别：nonconst |
| LabelingHelper | GetIconForStandardOfLiving | Unknown | CString | 类别：nonconst |
| LabelingHelper | GetIconForStandardOfLivingCFixedPoint | CFixedPoint | CString | 类别：nonconst |
| LabelingHelper | GetIconForStandardOfLivingFloat | Unknown | CString | 类别：nonconst |
| LabelingHelper | GetLabelForPopularityCFixedPoint | CFixedPoint | CString | 类别：nonconst |
| LabelingHelper | GetLabelForPopularityFloat | Unknown | CString | 类别：nonconst |
| LabelingHelper | GetLabelForRadicalism | CFixedPoint | CString | 类别：nonconst |
| LabelingHelper | GetLabelForStandardOfLiving | int32 | CString | 类别：nonconst |
| LabelingHelper | GetLabelForStandardOfLivingCFixedPoint | CFixedPoint | CString | 类别：nonconst |
| LabelingHelper | GetLabelForStandardOfLivingCFixedPointFormatFromExpected | Unknown Unknown | CString | 类别：nonconst |
| LabelingHelper | GetLabelForStandardOfLivingFloat | float | CString | 类别：nonconst |
| LabelingHelper | GetLabelForStandardOfLivingFloatFormatFromExpected | Unknown Unknown | CString | 类别：nonconst |
| LabelingHelper | GetLabelForStandardOfLivingFormatFromExpected | Unknown Unknown | CString | 类别：nonconst |
| LabelingHelper | GetLabelForStandardOfLivingNoIcon | Unknown | CString | 类别：nonconst |
| LabelingHelper | GetLabelForStandardOfLivingNoIconCFixedPoint | CFixedPoint | CString | 类别：nonconst |
| LabelingHelper | GetLabelForStandardOfLivingNoIconCFixedPointFormatFromExpected | CFixedPoint CFixedPoint | CString | 类别：nonconst |
| LabelingHelper | GetLabelForStandardOfLivingNoIconFloat | Unknown | CString | 类别：nonconst |
| LabelingHelper | GetLabelForStandardOfLivingNoIconFloatFormatFromExpected | Unknown Unknown | CString | 类别：nonconst |
| LabelingHelper | GetLabelForStandardOfLivingNoIconFormatFromExpected | Unknown Unknown | CString | 类别：nonconst |
| LabelingHelper | GetLabelForSupport | CFixedPoint | CString | 类别：nonconst |
| LabelingHelper | GetMultiTypeGameTimeDifferenceFromDays | int32 int32 CString | CString | 类别：nonconst |
| LabelingHelper | GetMultiTypeGameTimeDifferenceFromMonths | int32 int32 CString | CString | 类别：nonconst |
| LabelingHelper | GetMultiTypeGameTimeDifferenceFromWeeks | int32 int32 CString | CString | 类别：nonconst |
| LabelingHelper | GetPriceCompareDesc | Unknown Unknown Unknown | CString | 类别：nonconst |
| LabelingHelper | GetPriceCompareDescShort | Unknown | CString | 类别：nonconst |
| LabelingHelper | GetPriceCompareIcon | CFixedPoint | CString | 类别：nonconst |
| LabelingHelper | GetPriceCompareIconNoFormatting | CFixedPoint | CString | 类别：nonconst |
| LabelingHelper | GetPriceCompareIconNoTooltip | Unknown | CString | 类别：nonconst |
| LabelingHelper | GetRemainingDuration | Date CString | CString | 类别：nonconst |
| LabelingHelper | Self |  | LabelingHelper |  |
| Law | AccessApprovingIGs |  | Unknown | 类别：const |
| Law | AccessDisapprovingIGs |  | Unknown | 类别：const |
| Law | AccessNeutralIGs |  | Unknown | 类别：const |
| Law | AccessSelf |  | Law | 类别：const |
| Law | AppliesTo | Country | bool |  |
| Law | CannotEnactDesc |  | CString |  |
| Law | GetActiveAmendments |  | Unknown | 类别：nonconst |
| Law | GetActiveGroupLaw |  | Law | 类别：nonconst |
| Law | GetAffectedMovementsFromCancelEnact |  | Unknown | 类别：nonconst |
| Law | GetAffectedMovementsFromStartEnact |  | Unknown | 类别：nonconst |
| Law | GetAllAmendments |  | Unknown | 类别：nonconst |
| Law | GetCancelTooltip |  | CString | 类别：nonconst |
| Law | GetCheckpointAdvanceBreakdown |  | CString | 类别：nonconst |
| Law | GetCheckpointAdvanceChance |  | CFixedPoint | 类别：nonconst |
| Law | GetCheckpointAdvanceWithImpositionBreakdown |  | CString | 类别：nonconst |
| Law | GetCheckpointAdvanceWithImpositionChance |  | CFixedPoint | 类别：nonconst |
| Law | GetCheckpointBaseDays |  | int32 | 类别：nonconst |
| Law | GetCheckpointDebateBreakdown |  | CString | 类别：nonconst |
| Law | GetCheckpointDebateChance |  | CFixedPoint | 类别：nonconst |
| Law | GetCheckpointDebateWithImpositionBreakdown |  | CString | 类别：nonconst |
| Law | GetCheckpointDebateWithImpositionChance |  | CFixedPoint | 类别：nonconst |
| Law | GetCheckpointEndDateString |  | CString | 类别：nonconst |
| Law | GetCheckpointProgress |  | CFixedPoint | 类别：nonconst |
| Law | GetCheckpointRemainingDays |  | int32 | 类别：nonconst |
| Law | GetCheckpointStallBreakdown |  | CString | 类别：nonconst |
| Law | GetCheckpointStallChance |  | CFixedPoint | 类别：nonconst |
| Law | GetCheckpointStallWithImpositionBreakdown |  | CString | 类别：nonconst |
| Law | GetCheckpointStallWithImpositionChance |  | CFixedPoint | 类别：nonconst |
| Law | GetCheckpointSuccessBreakdown |  | CString | 类别：nonconst |
| Law | GetCheckpointSuccessChance |  | CFixedPoint | 类别：nonconst |
| Law | GetCheckpointSuccessWithImpositionBreakdown |  | CString | 类别：nonconst |
| Law | GetCheckpointSuccessWithImpositionChance |  | CFixedPoint | 类别：nonconst |
| Law | GetCheckpointTotalDays |  | int32 | 类别：nonconst |
| Law | GetCheckpointTotalDaysBreakdown |  | CString | 类别：nonconst |
| Law | GetCountry |  | Country | 类别：nonconst |
| Law | GetCurrentEnactmentPhaseKey |  | CString | 类别：nonconst |
| Law | GetCustom | CustomLocalization | CString | 类别：nonconst |
| Law | GetDailyProgress |  | CFixedPoint | 类别：nonconst |
| Law | GetDesc |  | CString | 类别：nonconst |
| Law | GetEnactmentLastCheckpointDate |  | Date | 类别：nonconst |
| Law | GetEnactmentLastCheckpointResult |  | CString | 类别：nonconst |
| Law | GetEnactmentPhase |  | int32 | 类别：nonconst |
| Law | GetEnactmentPhaseKey | Unknown | CString | 类别：nonconst |
| Law | GetEnactmentSetbackCount |  | int32 | 类别：nonconst |
| Law | GetExilesThatWouldJoinMovementSupportingLaw |  | Unknown | 类别：nonconst |
| Law | GetExilesThatWouldStartMovementSupportingLaw |  | Unknown | 类别：nonconst |
| Law | GetFlavor |  | CString | 类别：nonconst |
| Law | GetFullName |  | CString | 类别：nonconst |
| Law | GetFullNameWithStatus |  | CString | 类别：nonconst |
| Law | GetGroup |  | LawGroup | 类别：nonconst |
| Law | GetGroupName |  | CString | 类别：nonconst |
| Law | GetIGsApproveList |  | CString | 类别：nonconst |
| Law | GetIGsDisapproveList |  | CString | 类别：nonconst |
| Law | GetIGsEnactmentList |  | CString | 类别：nonconst |
| Law | GetIGsUndecidedList |  | CString | 类别：nonconst |
| Law | GetIGsWithApprovalChanges |  | Unknown | 类别：nonconst |
| Law | GetInstitution |  | Institution | 类别：nonconst |
| Law | GetInstitutionModifier |  | Modifier | 类别：nonconst |
| Law | GetInstitutionTooltip |  | CString | 类别：nonconst |
| Law | GetInstitutionType |  | InstitutionType | 类别：nonconst |
| Law | GetLawAlternatives |  | Unknown | 类别：nonconst |
| Law | GetLawType |  | LawType | 类别：nonconst |
| Law | GetMarginalizedIGsWithApprovalChanges |  | Unknown | 类别：nonconst |
| Law | GetName |  | CString | 类别：nonconst |
| Law | GetNameNoFormatting |  | CString | 类别：nonconst |
| Law | GetNextEnactmentPhaseKey |  | CString | 类别：nonconst |
| Law | GetNumIGsApprove |  | uint32 | 类别：nonconst |
| Law | GetNumIGsDisapprove |  | uint32 | 类别：nonconst |
| Law | GetNumIGsUndecided |  | uint32 | 类别：nonconst |
| Law | GetNumSupportingInterestGroups |  | int32 | 类别：nonconst |
| Law | GetOnActivateDesc |  | CString | 类别：nonconst |
| Law | GetOnDeactivateDesc |  | CString | 类别：nonconst |
| Law | GetOnEnactDesc |  | CString | 类别：nonconst |
| Law | GetOnImposeDesc |  | CString | 类别：nonconst |
| Law | GetPercentPolStrApprove |  | CFixedPoint | 类别：nonconst |
| Law | GetPercentPolStrDisapprove |  | CFixedPoint | 类别：nonconst |
| Law | GetPercentPolStrUndecided |  | CFixedPoint | 类别：nonconst |
| Law | GetPreviousEnactmentPhaseKey |  | CString | 类别：nonconst |
| Law | GetRadicalismDriftTargetOnMovementFromCancelEnact | PoliticalMovement | CFixedPoint | 类别：nonconst |
| Law | GetRadicalismDriftTargetOnMovementFromStartEnact | PoliticalMovement | CFixedPoint | 类别：nonconst |
| Law | GetRadicalismEffectOnMovementFromCancelEnact | PoliticalMovement | CFixedPoint | 类别：nonconst |
| Law | GetRadicalismEffectOnMovementFromStartEnact | PoliticalMovement | CFixedPoint | 类别：nonconst |
| Law | GetReplacedLawEffect |  | CString | 类别：nonconst |
| Law | GetSupportingInterestGroupsBreakdown |  | CString | 类别：nonconst |
| Law | GetSupportingInterestGroupsSummary |  | CString | 类别：nonconst |
| Law | GetTexture |  | Unknown | 类别：nonconst |
| Law | GetTooltip |  | CString | 类别：nonconst |
| Law | GetTooltipNoRequirements |  | CString | 类别：nonconst |
| Law | GetTooltipTag |  | CString | 类别：nonconst |
| Law | GetTypeDesc |  | CString | 类别：nonconst |
| Law | HasEnactmentLastCheckpoint |  | bool |  |
| Law | HasInstitution |  | bool |  |
| Law | HasNecessaryLaws |  | bool |  |
| Law | HasNecessaryTech |  | bool |  |
| Law | IsActive |  | bool |  |
| Law | IsBeingEnacted |  | bool |  |
| Law | IsMissingSupport |  | bool |  |
| Law | IsSelected |  | bool |  |
| Law | IsSupported |  | bool |  |
| Law | IsValid |  | bool |  |
| Law | IsVisible |  | bool |  |
| Law | MakeScope |  | Scope |  |
| Law | PredictApprovalChangesDuringEnactmentDesc |  | CString |  |
| Law | PredictLegitimacyChangeToEnact |  | int32 |  |
| Law | PredictLegitimacyChangeToEnactDesc |  | CString |  |
| Law | PredictMovementLoyalistsFromEnactmentDesc |  | CString |  |
| Law | PredictRadicalismChangesFromCancellationDesc |  | CString |  |
| Law | PredictRadicalismChangesFromEnactmentDesc |  | CString |  |
| Law | Select |  | void |  |
| Law | Self |  | Law |  |
| Law | StartEnacting |  | Command |  |
| Law | StartImposing |  | Command |  |
| Law | StopEnacting |  | Command |  |
| LawGroup | AccessSelf |  | LawGroup | 类别：const |
| LawGroup | GetDesc |  | CString | 类别：nonconst |
| LawGroup | GetFirstInstitutionType |  | InstitutionType | 类别：nonconst |
| LawGroup | GetKey |  | CString | 类别：nonconst |
| LawGroup | GetName |  | CString | 类别：nonconst |
| LawGroup | GetNameNoFormatting |  | CString | 类别：nonconst |
| LawGroup | GetNumEnactable |  | int32 | 类别：nonconst |
| LawGroup | GetNumImposeOptions | Country | int32 | 类别：nonconst |
| LawGroup | GetNumPotentialEnactable |  | int32 | 类别：nonconst |
| LawGroup | GetTexture |  | Unknown | 类别：nonconst |
| LawGroup | GetTooltipTag |  | CString | 类别：nonconst |
| LawGroup | Self |  | LawGroup |  |
| LawType | AccessSelf |  | LawType | 类别：const |
| LawType | GetAdditionalEffectDesc |  | CString | 类别：nonconst |
| LawType | GetBlockingRequirements | Country | CString | 类别：nonconst |
| LawType | GetCustom | CustomLocalization | CString | 类别：nonconst |
| LawType | GetDesc |  | CString | 类别：nonconst |
| LawType | GetEffectDesc | Country | CString | 类别：nonconst |
| LawType | GetFullName |  | CString | 类别：nonconst |
| LawType | GetFullNameWithStatus | Unknown | CString | 类别：nonconst |
| LawType | GetGroup |  | LawGroup | 类别：nonconst |
| LawType | GetName |  | CString | 类别：nonconst |
| LawType | GetNameNoFormatting |  | CString | 类别：nonconst |
| LawType | GetParentLawType |  | LawType | 类别：nonconst |
| LawType | GetRequirements | Unknown | CString | 类别：nonconst |
| LawType | GetTexture |  | Unknown | 类别：nonconst |
| LawType | GetTooltip | Country | CString | 类别：nonconst |
| LawType | GetTooltipTag |  | CString | 类别：nonconst |
| LawType | GetTypeDesc |  | CString | 类别：nonconst |
| LawType | GetUnlocks |  | CString | 类别：nonconst |
| LawType | MakeScope |  | Scope |  |
| LawType | Self |  | LawType |  |
| Layer | AccessSelf |  | Layer | 类别：const |
| Layer | Self |  | Layer |  |
| LayerTreeItem | AccessSelf |  | LayerTreeItem | 类别：const |
| LayerTreeItem | GetInstanceCount |  | int32 | 类别：nonconst |
| LayerTreeItem | GetLayer |  | CString | 类别：nonconst |
| LayerTreeItem | IsExpanded |  | bool |  |
| LayerTreeItem | IsGenerated |  | bool |  |
| LayerTreeItem | IsHidden |  | bool |  |
| LayerTreeItem | IsLayer |  | bool |  |
| LayerTreeItem | IsLocked |  | bool |  |
| LayerTreeItem | IsSelected |  | bool |  |
| LayerTreeItem | SelectItem |  | void |  |
| LayerTreeItem | Self |  | LayerTreeItem |  |
| LayerTreeItem | ToggleExclusiveLayerHidden |  | void |  |
| LayerTreeItem | ToggleExclusiveLock |  | void |  |
| LayerTreeItem | ToggleLayerHidden |  | void |  |
| LayerTreeItem | ToggleLock |  | void |  |
| LegalDocsViewer | AccessSelf |  | LegalDocsViewer | 类别：const |
| LegalDocsViewer | Agree |  | void |  |
| LegalDocsViewer | GetDocumentText |  | CUTF8String | 类别：nonconst |
| LegalDocsViewer | Hide |  | void |  |
| LegalDocsViewer | Self |  | LegalDocsViewer |  |
| LegalDocsViewer | Show |  | void |  |
| LegitimacyLevel | AccessSelf |  | LegitimacyLevel | 类别：const |
| LegitimacyLevel | GetDeltaSign | int32 int32 | int32 | 类别：nonconst |
| LegitimacyLevel | GetEffects |  | CString | 类别：nonconst |
| LegitimacyLevel | GetEffectsWithLoyaltiesGain | Country | CString | 类别：nonconst |
| LegitimacyLevel | GetLowerBound |  | int32 | 类别：nonconst |
| LegitimacyLevel | GetName |  | CString | 类别：nonconst |
| LegitimacyLevel | GetNameNoFormatting |  | CString | 类别：nonconst |
| LegitimacyLevel | GetProgress | Unknown | float | 类别：nonconst |
| LegitimacyLevel | GetTooltipTag |  | CString | 类别：nonconst |
| LegitimacyLevel | GetUpperBound |  | int32 | 类别：nonconst |
| LegitimacyLevel | GetWidth |  | int32 | 类别：nonconst |
| LegitimacyLevel | IsActive | Unknown | bool |  |
| LegitimacyLevel | Self |  | LegitimacyLevel |  |
| LensOption | AccessSelf |  | LensOption | 类别：const |
| LensOption | Activate |  | void |  |
| LensOption | CanActivate |  | bool |  |
| LensOption | GetCostText |  | CString | 类别：nonconst |
| LensOption | GetDecreeType |  | DecreeType | 类别：nonconst |
| LensOption | GetDiplomaticAction |  | DiplomaticAction | 类别：nonconst |
| LensOption | GetKey |  | CString | 类别：nonconst |
| LensOption | GetMapInteraction |  | MapInteraction | 类别：nonconst |
| LensOption | GetNumberOfActiveOptions |  | int32 | 类别：nonconst |
| LensOption | GetNumberOfInactiveSelectableOptions |  | int32 | 类别：nonconst |
| LensOption | GetNumberOfSelections |  | int32 | 类别：nonconst |
| LensOption | GetText |  | CString | 类别：nonconst |
| LensOption | GetTexture |  | Unknown | 类别：nonconst |
| LensOption | GetTooltip |  | CString | 类别：nonconst |
| LensOption | IsActive |  | bool |  |
| LensOption | IsDecree |  | bool |  |
| LensOption | IsDiplomaticAction |  | bool |  |
| LensOption | IsMapInteraction |  | bool |  |
| LensOption | Self |  | LensOption |  |
| LensOption | ShouldShowNumberOfSelections |  | bool |  |
| LensOption | Toggle |  | void |  |
| LensTab | AccessSelf |  | LensTab | 类别：const |
| LensTab | GetKey |  | CString | 类别：nonconst |
| LensTab | GetText |  | CString | 类别：nonconst |
| LensTab | GetTexture |  | Unknown | 类别：nonconst |
| LensTab | GetTooltip |  | CString | 类别：nonconst |
| LensTab | IsOpen |  | bool |  |
| LensTab | IsVisible |  | bool |  |
| LensTab | Open |  | void |  |
| LensTab | Self |  | LensTab |  |
| LensToolbar | AccessSelf |  | LensToolbar | 类别：const |
| LensToolbar | ActivateOption | CString | void |  |
| LensToolbar | Close |  | void |  |
| LensToolbar | GetCurrentTab |  | LensTab | 类别：nonconst |
| LensToolbar | GetMaxNumItemsPerRow |  | int32 | 类别：nonconst |
| LensToolbar | GetOptions |  | Unknown | 类别：nonconst |
| LensToolbar | GetTabs |  | Unknown | 类别：nonconst |
| LensToolbar | IsAnyLensOpen |  | bool |  |
| LensToolbar | IsLensOpen | CString | bool |  |
| LensToolbar | Open | Unknown | void |  |
| LensToolbar | OpenTab | Unknown | void |  |
| LensToolbar | Self |  | LensToolbar |  |
| LensToolbar | Toggle | CString | void |  |
| LensToolbar | ToggleOption | Unknown | void |  |
| LibertyDesireLevel | AccessSelf |  | LibertyDesireLevel | 类别：const |
| LibertyDesireLevel | GetBackground |  | Unknown | 类别：nonconst |
| LibertyDesireLevel | GetEffects |  | CString | 类别：nonconst |
| LibertyDesireLevel | GetLowerBound |  | CFixedPoint | 类别：nonconst |
| LibertyDesireLevel | GetName |  | CString | 类别：nonconst |
| LibertyDesireLevel | GetNameNoFormatting |  | CString | 类别：nonconst |
| LibertyDesireLevel | GetProgress | Unknown | float | 类别：nonconst |
| LibertyDesireLevel | GetTooltipTag |  | CString | 类别：nonconst |
| LibertyDesireLevel | GetUpperBound |  | CFixedPoint | 类别：nonconst |
| LibertyDesireLevel | GetWidth |  | CFixedPoint | 类别：nonconst |
| LibertyDesireLevel | IsActive | CFixedPoint | bool |  |
| LibertyDesireLevel | Self |  | LibertyDesireLevel |  |
| LoadIngameWindow | AccessSelf |  | LoadIngameWindow | 类别：const |
| LoadIngameWindow | GetSaveGames |  | Unknown | 类别：nonconst |
| LoadIngameWindow | GetSelectedSavegame |  | SaveGameItem | 类别：nonconst |
| LoadIngameWindow | HasSelectedSavegame |  | bool |  |
| LoadIngameWindow | IsEmpty |  | bool |  |
| LoadIngameWindow | OnBack |  | void |  |
| LoadIngameWindow | OnDelete |  | void |  |
| LoadIngameWindow | OnDeleteAll |  | void |  |
| LoadIngameWindow | OnLoad |  | void |  |
| LoadIngameWindow | OnShowInvalidSavegames |  | void |  |
| LoadIngameWindow | Self |  | LoadIngameWindow |  |
| LoadIngameWindow | ShouldShowInvalidSavegames |  | bool |  |
| LoadingScreenManager | AccessSelf |  | LoadingScreenManager | 类别：const |
| LoadingScreenManager | GetConceptTip |  | GameConceptType | 类别：nonconst |
| LoadingScreenManager | GetStaticTip |  | CString | 类别：nonconst |
| LoadingScreenManager | HasConceptTip |  | bool |  |
| LoadingScreenManager | HasStaticTip |  | bool |  |
| LoadingScreenManager | RollLoadingTip |  | void |  |
| LoadingScreenManager | Self |  | LoadingScreenManager |  |
| LobbyPlayer | AccessSelf |  | LobbyPlayer | 类别：const |
| LobbyPlayer | CanRemovePlayer |  | bool |  |
| LobbyPlayer | GetID |  | int32 | 类别：nonconst |
| LobbyPlayer | GetLoadingString |  | CString | 类别：nonconst |
| LobbyPlayer | GetName |  | CString | 类别：nonconst |
| LobbyPlayer | GetTransferProgress |  | float | 类别：nonconst |
| LobbyPlayer | HasPlayable |  | bool |  |
| LobbyPlayer | IsHost |  | bool |  |
| LobbyPlayer | IsHotjoining |  | bool |  |
| LobbyPlayer | IsLocalPlayer |  | bool |  |
| LobbyPlayer | IsObserver |  | bool |  |
| LobbyPlayer | IsReady |  | bool |  |
| LobbyPlayer | RemovePlayer |  | void |  |
| LobbyPlayer | Self |  | LobbyPlayer |  |
| LobbyPlayer | ShowReadyStatus |  | bool |  |
| LobbyView | AccessSelectedPlayable |  | Playable | 类别：const |
| LobbyView | AccessSelf |  | LobbyView | 类别：const |
| LobbyView | CanControlSelected |  | bool |  |
| LobbyView | CanGoBack |  | bool |  |
| LobbyView | CanReady |  | bool |  |
| LobbyView | CanStart |  | bool |  |
| LobbyView | ClearSelection |  | void |  |
| LobbyView | ControlSelected |  | void |  |
| LobbyView | CopyServerID |  | void |  |
| LobbyView | GetControlToolTip |  | CString | 类别：nonconst |
| LobbyView | GetEnabledDLCs |  | Unknown | 类别：nonconst |
| LobbyView | GetEnabledMods |  | Unknown | 类别：nonconst |
| LobbyView | GetGoBackToolTip |  | CString | 类别：nonconst |
| LobbyView | GetOpenMultiplayerToolTip |  | CString | 类别：nonconst |
| LobbyView | GetOtherPlayersCount |  | int32 | 类别：nonconst |
| LobbyView | GetReadyToolTip |  | CString | 类别：nonconst |
| LobbyView | GetSelectText |  | CString | 类别：nonconst |
| LobbyView | GetTransferSpeedSettingIndex |  | CVector2i | 类别：nonconst |
| LobbyView | GetTransferSpeedSettingOptions |  | Unknown | 类别：nonconst |
| LobbyView | GoBack |  | void |  |
| LobbyView | HasEnabledDLCs |  | bool |  |
| LobbyView | HasEnabledMods |  | bool |  |
| LobbyView | HasGameConfigurationWindow |  | bool |  |
| LobbyView | HasSelectedPlayable |  | bool |  |
| LobbyView | HasServerInfo |  | bool |  |
| LobbyView | IsAutoAccept |  | bool |  |
| LobbyView | IsInvite |  | bool |  |
| LobbyView | IsObserver |  | bool |  |
| LobbyView | IsPublicCrossplay |  | bool |  |
| LobbyView | IsPublicNoCrossplay |  | bool |  |
| LobbyView | IsReady |  | bool |  |
| LobbyView | OnNameEdit |  | void |  |
| LobbyView | OnPasswordEdit |  | void |  |
| LobbyView | OnTransferSpeedSettingChanged |  | void |  |
| LobbyView | OpenGameConfigurationWindow |  | void |  |
| LobbyView | OpenMultiplayer |  | void |  |
| LobbyView | Players |  | Unknown |  |
| LobbyView | Ready |  | void |  |
| LobbyView | Self |  | LobbyView |  |
| LobbyView | SetInvite |  | void |  |
| LobbyView | SetName |  | void |  |
| LobbyView | SetPassword |  | void |  |
| LobbyView | SetPublicCrossplay |  | void |  |
| LobbyView | SetPublicNoCrossplay |  | void |  |
| LobbyView | SetShowPlayerList | Unknown | void |  |
| LobbyView | ShouldShowEnabledDLCs |  | bool |  |
| LobbyView | ShouldShowEnabledMods |  | bool |  |
| LobbyView | ShowHosting |  | bool |  |
| LobbyView | ShowModifyServer |  | bool |  |
| LobbyView | ShowPlayerList |  | bool |  |
| LobbyView | Start |  | void |  |
| LobbyView | StartToolTip |  | CString |  |
| LobbyView | ToggleAutoAccept |  | void |  |
| LobbyView | ToggleObserve |  | void |  |
| LobbyView | ToggleShowEnabledDLCs |  | void |  |
| LobbyView | ToggleShowEnabledMods |  | void |  |
| LobbyView | ToggleVisibility |  | void |  |
| LobbyView | UnReady |  | void |  |
| Location | AccessSelf |  | Location | 类别：const |
| Location | GetID |  | CString | 类别：nonconst |
| Location | GetName |  | CString | 类别：nonconst |
| Location | GetType |  | CString | 类别：nonconst |
| Location | GoToLocation |  | void |  |
| Location | Self |  | Location |  |
| LocationFinder | AccessSelf |  | LocationFinder | 类别：const |
| LocationFinder | Close |  | void |  |
| LocationFinder | GetLocations |  | Unknown | 类别：nonconst |
| LocationFinder | Self |  | LocationFinder |  |
| LogEntry | AccessSelf |  | LogEntry | 类别：const |
| LogEntry | GetColor |  | CVector4f | 类别：nonconst |
| LogEntry | GetText |  | CString | 类别：nonconst |
| LogEntry | GetTime |  | CString | 类别：nonconst |
| LogEntry | Self |  | LogEntry |  |
| LogViewer | AccessCategories |  | Unknown | 类别：const |
| LogViewer | AccessSelf |  | LogViewer | 类别：const |
| LogViewer | AccessTypes |  | Unknown | 类别：const |
| LogViewer | DecreaseLogInfoExpandSize |  | void |  |
| LogViewer | FlushLog |  | void |  |
| LogViewer | GetFilteredNum |  | int32 | 类别：nonconst |
| LogViewer | GetLastLogEntry |  | LogViewerEntry | 类别：nonconst |
| LogViewer | GetLogInfoExpandSize |  | int32 | 类别：nonconst |
| LogViewer | GetLogInfoExpandSizeVector | float | CVector2f | 类别：nonconst |
| LogViewer | GetSelectedLogEntry |  | LogViewerEntry | 类别：nonconst |
| LogViewer | GetTextFilter |  | CUTF8String | 类别：nonconst |
| LogViewer | HasEntries |  | bool |  |
| LogViewer | IncreaseLogInfoExpandSize |  | void |  |
| LogViewer | IsAnyEntrySelected |  | bool |  |
| LogViewer | OpenLinkedLogViewer |  | void |  |
| LogViewer | OpenLinkedLogViewerFilteredByType | int32 | void |  |
| LogViewer | ResetFilters |  | void |  |
| LogViewer | ResetTextFilter |  | void |  |
| LogViewer | Self |  | LogViewer |  |
| LogViewer | SetTextFilter |  | void |  |
| LogViewer | ToggleHidden |  | void |  |
| LogViewerCategory | AccessSelf |  | LogViewerCategory | 类别：const |
| LogViewerCategory | GetFilteredCount |  | int32 | 类别：nonconst |
| LogViewerCategory | GetIcon |  | Unknown | 类别：nonconst |
| LogViewerCategory | GetIsFiltered |  | bool | 类别：nonconst |
| LogViewerCategory | GetName |  | CString | 类别：nonconst |
| LogViewerCategory | Self |  | LogViewerCategory |  |
| LogViewerCategory | SetIsFiltered | Unknown | void |  |
| LogViewerEntry | AccessSelf |  | LogViewerEntry | 类别：const |
| LogViewerEntry | ContainsScriptFile |  | bool |  |
| LogViewerEntry | GetFileLineNo |  | int32 | 类别：nonconst |
| LogViewerEntry | GetFilename |  | Unknown | 类别：nonconst |
| LogViewerEntry | GetFilepath |  | CString | 类别：nonconst |
| LogViewerEntry | GetIcon |  | Unknown | 类别：nonconst |
| LogViewerEntry | GetMessage |  | CString | 类别：nonconst |
| LogViewerEntry | GetTimestampLong |  | CString | 类别：nonconst |
| LogViewerEntry | GetTimestampShort |  | CString | 类别：nonconst |
| LogViewerEntry | IsSelected |  | bool |  |
| LogViewerEntry | OpenInCodeEditor |  | void |  |
| LogViewerEntry | OpenInEditor |  | void |  |
| LogViewerEntry | OpenInExternalLogViewer |  | void |  |
| LogViewerEntry | OpenInScriptEditor |  | void |  |
| LogViewerEntry | Self |  | LogViewerEntry |  |
| LogViewerEntry | SetSelected | bool | void |  |
| LogViewerType | AccessSelf |  | LogViewerType | 类别：const |
| LogViewerType | GetFilteredCount |  | int32 | 类别：nonconst |
| LogViewerType | GetIcon |  | Unknown | 类别：nonconst |
| LogViewerType | GetId |  | int32 | 类别：nonconst |
| LogViewerType | GetIsFiltered |  | bool | 类别：nonconst |
| LogViewerType | GetName |  | CString | 类别：nonconst |
| LogViewerType | Self |  | LogViewerType |  |
| LogViewerType | SetIsFiltered | bool | void |  |
| LoginView | AccessSelf |  | LoginView | 类别：const |
| LoginView | GetEmail |  | CUTF8String | 类别：nonconst |
| LoginView | GetErrorMessage |  | CUTF8String | 类别：nonconst |
| LoginView | GetLoginString |  | CUTF8String | 类别：nonconst |
| LoginView | GetPassword |  | CUTF8String | 类别：nonconst |
| LoginView | Hide |  | void |  |
| LoginView | IsChangingUserName |  | bool |  |
| LoginView | IsConnectingAccount |  | bool |  |
| LoginView | IsEmailSent |  | bool |  |
| LoginView | IsEmptyUserNamePrompt |  | bool |  |
| LoginView | IsLoggedIn |  | bool |  |
| LoginView | IsLogin |  | bool |  |
| LoginView | IsRestoringPassword |  | bool |  |
| LoginView | IsSuccessfulSetName |  | bool |  |
| LoginView | IsValidLoginInfo |  | bool |  |
| LoginView | Login |  | void |  |
| LoginView | Logout |  | void |  |
| LoginView | OnUserNameChange |  | void |  |
| LoginView | ResetPassword |  | void |  |
| LoginView | Self |  | LoginView |  |
| LoginView | SetEmail |  | void |  |
| LoginView | SetPassword |  | void |  |
| LoginView | SetState | CString | void |  |
| LoginView | SetUserName |  | void |  |
| LoginView | Show |  | void |  |
| LoginView | ToggleConnected |  | void |  |
| LoyaltyType | AccessSelf |  | LoyaltyType | 类别：const |
| LoyaltyType | GetColor |  | CVector4f | 类别：nonconst |
| LoyaltyType | GetCountryGraphicalRatio | Country | float | 类别：nonconst |
| LoyaltyType | GetCountryTooltip | Country | CString | 类别：nonconst |
| LoyaltyType | GetCountryTrend | Country | DataTrend | 类别：nonconst |
| LoyaltyType | GetHeader |  | CString | 类别：nonconst |
| LoyaltyType | GetInterestGroupTooltip | Unknown | CString | 类别：nonconst |
| LoyaltyType | GetInterestGroupTrend | Unknown | DataTrend | 类别：nonconst |
| LoyaltyType | HasTrend |  | bool |  |
| LoyaltyType | Self |  | LoyaltyType |  |
| MPConfig | AccessSelf |  | MPConfig | 类别：const |
| MPConfig | GetOfflinePlayerToolTip |  | CString | 类别：nonconst |
| MPConfig | GetPrivateToolTip |  | CString | 类别：nonconst |
| MPConfig | GetPublicToolTip |  | CString | 类别：nonconst |
| MPConfig | IsCrossplayChecked |  | bool |  |
| MPConfig | IsHotjoinAutoAccept |  | bool |  |
| MPConfig | IsOffline |  | bool |  |
| MPConfig | IsPrivate |  | bool |  |
| MPConfig | IsPublic |  | bool |  |
| MPConfig | Self |  | MPConfig |  |
| MPConfig | SetOffline |  | void |  |
| MPConfig | SetPrivate |  | void |  |
| MPConfig | SetPublic |  | void |  |
| MPConfig | ToggleCrossplay |  | void |  |
| MPConfig | ToggleHotjoinAutoAccept |  | void |  |
| MapContentEditorMode | AccessSelf |  | MapContentEditorMode | 类别：const |
| MapContentEditorMode | IsSelected |  | bool |  |
| MapContentEditorMode | Self |  | MapContentEditorMode |  |
| MapContentEditorOptions | AccessSelf |  | MapContentEditorOptions | 类别：const |
| MapContentEditorOptions | ApplyChanges |  | void |  |
| MapContentEditorOptions | CanApplyChanges |  | bool |  |
| MapContentEditorOptions | CanErase |  | bool |  |
| MapContentEditorOptions | CanMakeGroupingOperation |  | bool |  |
| MapContentEditorOptions | CurrentLayerHasChanges |  | bool |  |
| MapContentEditorOptions | DiscardChanges |  | void |  |
| MapContentEditorOptions | GetAddToGroupModeDescription |  | CString | 类别：nonconst |
| MapContentEditorOptions | GetApplyButtonDescription |  | CString | 类别：nonconst |
| MapContentEditorOptions | GetEraserDescription |  | CString | 类别：nonconst |
| MapContentEditorOptions | GetMapContentSelectionModeDescription |  | CString | 类别：nonconst |
| MapContentEditorOptions | GetPaintModeDescription |  | CString | 类别：nonconst |
| MapContentEditorOptions | GetRemoveFromGroupModeDescription |  | CString | 类别：nonconst |
| MapContentEditorOptions | IsAddToGroupMode |  | bool |  |
| MapContentEditorOptions | IsAddToGroupModeAllowed |  | bool |  |
| MapContentEditorOptions | IsCurrentLayerPixelBased |  | bool |  |
| MapContentEditorOptions | IsEraserMode |  | bool |  |
| MapContentEditorOptions | IsEraserModeAllowed |  | bool |  |
| MapContentEditorOptions | IsMapContentSelectionMode |  | bool |  |
| MapContentEditorOptions | IsMapContentSelectionModeAllowed |  | bool |  |
| MapContentEditorOptions | IsPaintMode |  | bool |  |
| MapContentEditorOptions | IsPaintModeAllowed |  | bool |  |
| MapContentEditorOptions | IsPaintingAllowed |  | bool |  |
| MapContentEditorOptions | IsRemoveFromGroupMode |  | bool |  |
| MapContentEditorOptions | IsRemoveFromGroupModeAllowed |  | bool |  |
| MapContentEditorOptions | Self |  | MapContentEditorOptions |  |
| MapContentEditorOptions | SetAddToGroupMode |  | void |  |
| MapContentEditorOptions | SetEraserMode |  | void |  |
| MapContentEditorOptions | SetMapContentSelectionMode | bool | void |  |
| MapContentEditorOptions | SetPaintMode |  | void |  |
| MapContentEditorOptions | SetRemoveFromGroupMode |  | void |  |
| MapContentEditorViewport | AccessSelf |  | MapContentEditorViewport | 类别：const |
| MapContentEditorViewport | CancelPropertyPainting |  | void |  |
| MapContentEditorViewport | GetPropertyPaintingModeDesc |  | CString | 类别：nonconst |
| MapContentEditorViewport | IsInPropertyPaintingMode |  | bool |  |
| MapContentEditorViewport | Self |  | MapContentEditorViewport |  |
| MapContentEntryDesc | AccessSelf |  | MapContentEntryDesc | 类别：const |
| MapContentEntryDesc | ContainsErrors |  | bool |  |
| MapContentEntryDesc | GetErrorMessage |  | CString | 类别：nonconst |
| MapContentEntryDesc | GetName |  | CString | 类别：nonconst |
| MapContentEntryDesc | GetUniqueId |  | int32 | 类别：nonconst |
| MapContentEntryDesc | IsDone |  | bool |  |
| MapContentEntryDesc | IsSelected |  | bool |  |
| MapContentEntryDesc | Self |  | MapContentEntryDesc |  |
| MapContentLayerDesc | AccessSelf |  | MapContentLayerDesc | 类别：const |
| MapContentLayerDesc | GetName |  | CString | 类别：nonconst |
| MapContentLayerDesc | Self |  | MapContentLayerDesc |  |
| MapContentPanel | AccessSelf |  | MapContentPanel | 类别：const |
| MapContentPanel | CanCreateNewEntry |  | bool |  |
| MapContentPanel | CanDeleteAnySelectedEntry |  | bool |  |
| MapContentPanel | CreateNewEntry |  | void |  |
| MapContentPanel | DeleteSelectedEntries |  | void |  |
| MapContentPanel | GetCreateNewEntryTooltip |  | CString | 类别：nonconst |
| MapContentPanel | GetDeleteSelectedEntriesTooltip |  | CString | 类别：nonconst |
| MapContentPanel | Self |  | MapContentPanel |  |
| MapContentPropertyGroup | AccessSelf |  | MapContentPropertyGroup | 类别：const |
| MapContentPropertyGroup | GetName |  | CString | 类别：nonconst |
| MapContentPropertyGroup | IsExpanded |  | bool |  |
| MapContentPropertyGroup | Self |  | MapContentPropertyGroup |  |
| MapContentPropertyGroup | ToggleExpanded |  | void |  |
| MapContentPropertyGroupsGui | AccessSelf |  | MapContentPropertyGroupsGui | 类别：const |
| MapContentPropertyGroupsGui | CanActivatePropertyPaintingMode |  | bool |  |
| MapContentPropertyGroupsGui | IsInPropertyPaintingModeForBool | Unknown | bool |  |
| MapContentPropertyGroupsGui | IsInPropertyPaintingModeForCColor | Unknown | bool |  |
| MapContentPropertyGroupsGui | IsInPropertyPaintingModeForCString | Unknown | bool |  |
| MapContentPropertyGroupsGui | IsInPropertyPaintingModeForColor | Unknown | bool |  |
| MapContentPropertyGroupsGui | IsInPropertyPaintingModeForEnum | Unknown | bool |  |
| MapContentPropertyGroupsGui | IsInPropertyPaintingModeForFloat | Unknown | bool |  |
| MapContentPropertyGroupsGui | IsInPropertyPaintingModeForInt | Unknown | bool |  |
| MapContentPropertyGroupsGui | IsInPropertyPaintingModeForString | Unknown | bool |  |
| MapContentPropertyGroupsGui | IsInPropertyPaintingModeForUint | Unknown | bool |  |
| MapContentPropertyGroupsGui | Self |  | MapContentPropertyGroupsGui |  |
| MapContentPropertyGroupsGui | TogglePropertyPaintingModeBool | Unknown | void |  |
| MapContentPropertyGroupsGui | TogglePropertyPaintingModeCColor | Unknown | void |  |
| MapContentPropertyGroupsGui | TogglePropertyPaintingModeCString | Unknown | void |  |
| MapContentPropertyGroupsGui | TogglePropertyPaintingModeColor | Unknown | void |  |
| MapContentPropertyGroupsGui | TogglePropertyPaintingModeEnum | Unknown | void |  |
| MapContentPropertyGroupsGui | TogglePropertyPaintingModeFloat | Unknown | void |  |
| MapContentPropertyGroupsGui | TogglePropertyPaintingModeInt | Unknown | void |  |
| MapContentPropertyGroupsGui | TogglePropertyPaintingModeString | Unknown | void |  |
| MapContentPropertyGroupsGui | TogglePropertyPaintingModeUint | Unknown | void |  |
| MapContentSelector | AccessSelf |  | MapContentSelector | 类别：const |
| MapContentSelector | GetErrorsCount |  | int32 | 类别：nonconst |
| MapContentSelector | GetSelectedCount |  | int32 | 类别：nonconst |
| MapContentSelector | IsAllSelectedDone |  | bool |  |
| MapContentSelector | IsAllSelectedHasErrors |  | bool |  |
| MapContentSelector | IsShowProgress |  | bool |  |
| MapContentSelector | Self |  | MapContentSelector |  |
| MapContentSelector | SetSelectedDone | Unknown | void |  |
| MapContentSelector | SetShowProgress | Unknown | void |  |
| MapContentSelectorGui | AccessSelf |  | MapContentSelectorGui | 类别：const |
| MapContentSelectorGui | ClearEntriesFilter |  | void |  |
| MapContentSelectorGui | GetCurrentLayerIndex |  | CVector2i | 类别：nonconst |
| MapContentSelectorGui | GetEntriesFilter |  | CString | 类别：nonconst |
| MapContentSelectorGui | GetEntriesWithErrorsCount |  | int32 | 类别：nonconst |
| MapContentSelectorGui | GetSelectedEntriesCount |  | int32 | 类别：nonconst |
| MapContentSelectorGui | IsAllSelectedDone |  | bool |  |
| MapContentSelectorGui | IsAllSelectedError |  | bool |  |
| MapContentSelectorGui | IsFilterErrors |  | bool |  |
| MapContentSelectorGui | IsShowProgress |  | bool |  |
| MapContentSelectorGui | OnEntrySelected | MapContentEntryDesc | void |  |
| MapContentSelectorGui | Self |  | MapContentSelectorGui |  |
| MapContentSelectorGui | SetCurrentLayerIndex |  | void |  |
| MapContentSelectorGui | SetEntriesFilter |  | void |  |
| MapContentSelectorGui | SetFilterErrors | bool | void |  |
| MapContentSelectorGui | SetSelectedDone | bool | void |  |
| MapContentSelectorGui | SetShowProgress | bool | void |  |
| MapEditor | AccessSelf |  | MapEditor | 类别：const |
| MapEditor | AccessUndoHistoryViewerClient |  | UndoHistoryViewerClient | 类别：const |
| MapEditor | CanToggleMaterialVisibility |  | bool |  |
| MapEditor | Exit |  | void |  |
| MapEditor | ExportTool |  | void |  |
| MapEditor | GetReferenceOverlayVisibility |  | bool | 类别：nonconst |
| MapEditor | GetTerrainColorMapVisibility |  | bool | 类别：nonconst |
| MapEditor | GetUndoHistoryViewerClient |  | UndoHistoryViewerClient | 类别：nonconst |
| MapEditor | ImportTool |  | void |  |
| MapEditor | IsAutoSaving |  | bool |  |
| MapEditor | IsDynamicTerrainMaterialFeatureTogglable |  | bool |  |
| MapEditor | IsDynamicTerrainMaterialSupported |  | bool |  |
| MapEditor | IsEnabled |  | bool |  |
| MapEditor | IsSavable |  | bool |  |
| MapEditor | ReloadHeightmap |  | void |  |
| MapEditor | Save |  | void |  |
| MapEditor | SaveAll |  | void |  |
| MapEditor | SaveAs |  | void |  |
| MapEditor | Self |  | MapEditor |  |
| MapEditor | SetDynamicTerrainMaterialSupported | bool | void |  |
| MapEditor | SetReferenceOverlayVisibility | bool | void |  |
| MapEditor | ToggleTerrainColorMapVisibility |  | void |  |
| MapEditorGui | AccessLogViewer |  | LogViewer | 类别：const |
| MapEditorGui | AccessSelf |  | MapEditorGui | 类别：const |
| MapEditorGui | GetReferenceOverlayOpacity |  | float | 类别：nonconst |
| MapEditorGui | Self |  | MapEditorGui |  |
| MapEditorGui | SetReferenceOverlayOpacity |  | void |  |
| MapEditorGui | ShowSettingsWindow |  | void |  |
| MapEditorGui | ToggleBordersSettingsOptions |  | void |  |
| MapEditorGui | ToggleReferenceOverlayOptions |  | void |  |
| MapEditorLayerBorder | AccessSelf |  | MapEditorLayerBorder | 类别：const |
| MapEditorLayerBorder | GetLayerIndex |  | int32 | 类别：nonconst |
| MapEditorLayerBorder | IsForceShown |  | bool |  |
| MapEditorLayerBorder | Self |  | MapEditorLayerBorder |  |
| MapEditorLayerBorder | SetForceShown | bool | void |  |
| MapEditorLayerBorderDockable | AccessSelf |  | MapEditorLayerBorderDockable | 类别：const |
| MapEditorLayerBorderDockable | GetLayerName | MapEditorLayerBorder | CString | 类别：nonconst |
| MapEditorLayerBorderDockable | Self |  | MapEditorLayerBorderDockable |  |
| MapInteraction | AccessSelf |  | MapInteraction | 类别：const |
| MapInteraction | Self |  | MapInteraction |  |
| MapInteractionManager | AccessSelf |  | MapInteractionManager | 类别：const |
| MapInteractionManager | HasAnyActiveMapInteraction |  | bool |  |
| MapInteractionManager | IsActiveMapInteraction | Unknown | bool |  |
| MapInteractionManager | ResetActiveMapInteraction |  | void |  |
| MapInteractionManager | Self |  | MapInteractionManager |  |
| MapInteractionManager | ShowMapInteractionNotification |  | void |  |
| MapListActivateConscriptionCenterOption | AccessSelf |  | MapListActivateConscriptionCenterOption | 类别：const |
| MapListActivateConscriptionCenterOption | GetConscriptionLimit |  | int32 | 类别：nonconst |
| MapListActivateConscriptionCenterOption | GetHQ |  | Hq | 类别：nonconst |
| MapListActivateConscriptionCenterOption | GetMilitaryFormation |  | MilitaryFormation | 类别：nonconst |
| MapListActivateConscriptionCenterOption | GetNumExpectedConscripts |  | int32 | 类别：nonconst |
| MapListActivateConscriptionCenterOption | GetState |  | State | 类别：nonconst |
| MapListActivateConscriptionCenterOption | Self |  | MapListActivateConscriptionCenterOption |  |
| MapListActivateConscriptionCenterPanel | AccessSelf |  | MapListActivateConscriptionCenterPanel | 类别：const |
| MapListActivateConscriptionCenterPanel | Self |  | MapListActivateConscriptionCenterPanel |  |
| MapListBuildingOption | AccessBuilding |  | Building | 类别：const |
| MapListBuildingOption | AccessMilitaryFormation |  | MilitaryFormation | 类别：const |
| MapListBuildingOption | AccessSelf |  | MapListBuildingOption | 类别：const |
| MapListBuildingOption | AccessState |  | State | 类别：const |
| MapListBuildingOption | GetBuilding |  | Building | 类别：nonconst |
| MapListBuildingOption | GetCombatUnitType |  | CombatUnitType | 类别：nonconst |
| MapListBuildingOption | GetConstructionNeeded |  | CFixedPoint | 类别：nonconst |
| MapListBuildingOption | GetMilitaryFormation |  | MilitaryFormation | 类别：nonconst |
| MapListBuildingOption | GetState |  | State | 类别：nonconst |
| MapListBuildingOption | Self |  | MapListBuildingOption |  |
| MapListBuildingPanel | AccessSelf |  | MapListBuildingPanel | 类别：const |
| MapListBuildingPanel | GetBuildingType |  | BuildingType | 类别：nonconst |
| MapListBuildingPanel | HasFilter | CString | bool |  |
| MapListBuildingPanel | Self |  | MapListBuildingPanel |  |
| MapListBuildingPanel | SetFilter | CString | void |  |
| MapListColonyOption | AccessSelf |  | MapListColonyOption | 类别：const |
| MapListColonyOption | GetRegion |  | CString | 类别：nonconst |
| MapListColonyOption | GetState |  | CString | 类别：nonconst |
| MapListColonyOption | GetStateRegion |  | StateRegion | 类别：nonconst |
| MapListColonyOption | Self |  | MapListColonyOption |  |
| MapListCountriesPanel | AccessSelf |  | MapListCountriesPanel | 类别：const |
| MapListCountriesPanel | Self |  | MapListCountriesPanel |  |
| MapListCountryOption | AccessSelf |  | MapListCountryOption | 类别：const |
| MapListCountryOption | Self |  | MapListCountryOption |  |
| MapListDecreeOption | AccessSelf |  | MapListDecreeOption | 类别：const |
| MapListDecreeOption | GetCost |  | CFixedPoint | 类别：nonconst |
| MapListDecreeOption | GetState |  | State | 类别：nonconst |
| MapListDecreeOption | Self |  | MapListDecreeOption |  |
| MapListDecreePanel | AccessSelf |  | MapListDecreePanel | 类别：const |
| MapListDecreePanel | GetDecreeType |  | DecreeType | 类别：nonconst |
| MapListDecreePanel | Self |  | MapListDecreePanel |  |
| MapListDeployMilitaryFormationToFrontOption | AccessSelf |  | MapListDeployMilitaryFormationToFrontOption | 类别：const |
| MapListDeployMilitaryFormationToFrontOption | GetFront |  | Front | 类别：nonconst |
| MapListDeployMilitaryFormationToFrontOption | Self |  | MapListDeployMilitaryFormationToFrontOption |  |
| MapListDeployMilitaryFormationToFrontPanel | AccessSelf |  | MapListDeployMilitaryFormationToFrontPanel | 类别：const |
| MapListDeployMilitaryFormationToFrontPanel | Self |  | MapListDeployMilitaryFormationToFrontPanel |  |
| 类型 | 函数 | 参数 | 输出 | 描述 |
|---|---|---|---|---|
| MapListDiploActionOption | AccessSelf |  | MapListDiploActionOption | Category: const |
| MapListDiploActionOption | GetCountry |  | CString | Category: nonconst |
| MapListDiploActionOption | GetDiplomaticAction |  | DiplomaticAction | Category: nonconst |
| MapListDiploActionOption | Self |  | MapListDiploActionOption |  |
| MapListHarvestConditionAreasPanel | AccessSelf |  | MapListHarvestConditionAreasPanel | Category: const |
| MapListHarvestConditionAreasPanel | Self |  | MapListHarvestConditionAreasPanel |  |
| MapListHarvestConditionOption | AccessSelf |  | MapListHarvestConditionOption | Category: const |
| MapListHarvestConditionOption | GetArea |  | HarvestConditionArea | Category: nonconst |
| MapListHarvestConditionOption | Self |  | MapListHarvestConditionOption |  |
| MapListInterestGroupOption | AccessInterestGroup |  | InterestGroup | Category: const |
| MapListInterestGroupOption | AccessSelf |  | MapListInterestGroupOption | Category: const |
| MapListInterestGroupOption | GetInterestGroup |  | InterestGroup | Category: nonconst |
| MapListInterestGroupOption | Self |  | MapListInterestGroupOption |  |
| MapListInterestGroupsPanel | AccessSelf |  | MapListInterestGroupsPanel | Category: const |
| MapListInterestGroupsPanel | Self |  | MapListInterestGroupsPanel |  |
| MapListMarketOption | AccessMarket |  | Market | Category: const |
| MapListMarketOption | AccessSelf |  | MapListMarketOption | Category: const |
| MapListMarketOption | GetMarket |  | Market | Category: nonconst |
| MapListMarketOption | Self |  | MapListMarketOption |  |
| MapListMarketsPanel | AccessSelf |  | MapListMarketsPanel | Category: const |
| MapListMarketsPanel | Self |  | MapListMarketsPanel |  |
| MapListMilitaryFormationOption | AccessSelf |  | MapListMilitaryFormationOption | Category: const |
| MapListMilitaryFormationOption | CanTravelTo |  | bool |  |
| MapListMilitaryFormationOption | GetTravelDays |  | int32 | Category: nonconst |
| MapListMilitaryFormationOption | Self |  | MapListMilitaryFormationOption |  |
| MapListMilitaryFormationPanel | AccessSelf |  | MapListMilitaryFormationPanel | Category: const |
| MapListMilitaryFormationPanel | Self |  | MapListMilitaryFormationPanel |  |
| MapListOption | AccessSelf |  | MapListOption | Category: const |
| MapListOption | CanClick |  | bool |  |
| MapListOption | GetBackgroundStatusFrame |  | int32 | Category: nonconst |
| MapListOption | GetIconStatusFrame |  | int32 | Category: nonconst |
| MapListOption | GetSelectionIndex |  | uint64 | Category: nonconst |
| MapListOption | GetTitle |  | CString | Category: nonconst |
| MapListOption | GetTooltip |  | CString | Category: nonconst |
| MapListOption | IsMapTargetHighlighted |  | bool |  |
| MapListOption | OnClick |  | void |  |
| MapListOption | OnMouseEnter |  | void |  |
| MapListOption | OnMouseLeave |  | void |  |
| MapListOption | OnRightClick |  | void |  |
| MapListOption | Self |  | MapListOption |  |
| MapListOption | ShouldShowStatusIcon |  | bool |  |
| MapListPanel | AccessFailedOptions |  | Unknown | Category: const |
| MapListPanel | AccessInvalidOptions |  | Unknown | Category: const |
| MapListPanel | AccessSelf |  | MapListPanel | Category: const |
| MapListPanel | AccessValidOptions |  | Unknown | Category: const |
| MapListPanel | GetTitle |  | CString | Category: nonconst |
| MapListPanel | Self |  | MapListPanel |  |
| MapListPanel | Sort | CString | void |  |
| MapListPanelManager | AccessSelf |  | MapListPanelManager | Category: const |
| MapListPanelManager | CloseCurrentPanel |  | void |  |
| MapListPanelManager | HasCurrentInteraction |  | bool |  |
| MapListPanelManager | IsAvailable |  | bool |  |
| MapListPanelManager | IsShowingFailedOptions |  | bool |  |
| MapListPanelManager | IsShowingInvalidOptions |  | bool |  |
| MapListPanelManager | IsVisible |  | bool |  |
| MapListPanelManager | OpenCurrentPanel |  | void |  |
| MapListPanelManager | ResetActiveMapInteraction |  | void |  |
| MapListPanelManager | Self |  | MapListPanelManager |  |
| MapListPanelManager | ToggleCurrentPanel |  | void |  |
| MapListPanelManager | ToggleFailedOptions |  | void |  |
| MapListPanelManager | ToggleInvalidOptions |  | void |  |
| MapListPowerBlocInvitationPanel | AccessSelf |  | MapListPowerBlocInvitationPanel | Category: const |
| MapListPowerBlocInvitationPanel | GetDiplomaticAction | Unknown | DiplomaticAction | Category: nonconst |
| MapListPowerBlocInvitationPanel | GetPowerBloc |  | PowerBloc | Category: nonconst |
| MapListPowerBlocInvitationPanel | Self |  | MapListPowerBlocInvitationPanel |  |
| MapListPowerBlocOption | AccessPowerBloc |  | PowerBloc | Category: const |
| MapListPowerBlocOption | AccessSelf |  | MapListPowerBlocOption | Category: const |
| MapListPowerBlocOption | GetPowerBloc |  | PowerBloc | Category: nonconst |
| MapListPowerBlocOption | Self |  | MapListPowerBlocOption |  |
| MapListPowerBlocsPanel | AccessSelf |  | MapListPowerBlocsPanel | Category: const |
| MapListPowerBlocsPanel | GetDiplomaticAction | Unknown | DiplomaticAction | Category: nonconst |
| MapListPowerBlocsPanel | Self |  | MapListPowerBlocsPanel |  |
| MapListStateOption | AccessSelf |  | MapListStateOption | Category: const |
| MapListStateOption | AccessState |  | State | Category: const |
| MapListStateOption | GetState |  | State | Category: nonconst |
| MapListStateOption | Self |  | MapListStateOption |  |

| 类型 | 函数 | 参数 | 输出 | 描述 |
|---|---|---|---|---|
| MapListStatePanel | AccessSelf |  | MapListStatePanel | Category: const |
| MapListStatePanel | Self |  | MapListStatePanel |  |
| MapListStrategicRegionOption | AccessSelf |  | MapListStrategicRegionOption | Category: const |
| MapListStrategicRegionOption | AccessStrategicRegion |  | StrategicRegion | Category: const |
| MapListStrategicRegionOption | GetStrategicRegion |  | StrategicRegion | Category: nonconst |
| MapListStrategicRegionOption | Self |  | MapListStrategicRegionOption |  |
| MapListStrategicRegionsPanel | AccessSelf |  | MapListStrategicRegionsPanel | Category: const |
| MapListStrategicRegionsPanel | Self |  | MapListStrategicRegionsPanel |  |
| MapMode | AccessSelf |  | MapMode | Category: const |
| MapMode | GetIcon |  | Unknown | Category: nonconst |
| MapMode | GetName |  | CString | Category: nonconst |
| MapMode | GetTooltipTag |  | CString | Category: nonconst |
| MapMode | Self |  | MapMode |  |
| MapModeList | AccessSelf |  | MapModeList | Category: const |
| MapModeList | GetContextName |  | CString | Category: nonconst |
| MapModeList | GetMapModes |  | Unknown | Category: nonconst |
| MapModeList | IsSelected | Unknown | bool |  |
| MapModeList | IsSelectedByKey | MapMode | bool |  |
| MapModeList | Select | Unknown | void |  |
| MapModeList | SelectByKey | MapMode | void |  |
| MapModeList | SelectDefault |  | void |  |
| MapModeList | Self |  | MapModeList |  |
| MapNotification | AccessSelf |  | MapNotification | Category: const |
| MapNotification | GetText |  | CString | Category: nonconst |
| MapNotification | Self |  | MapNotification |  |
| MapObjectMask | AccessSelf |  | MapObjectMask | Category: const |
| MapObjectMask | GetGeneratorCount |  | int32 | Category: nonconst |
| MapObjectMask | GetGeneratorNames |  | CString | Category: nonconst |
| MapObjectMask | GetName |  | CString | Category: nonconst |
| MapObjectMask | GetTextValidator |  | Unknown | Category: nonconst |
| MapObjectMask | GetThumbnail |  | Unknown | Category: nonconst |
| MapObjectMask | IsModified |  | bool |  |
| MapObjectMask | IsSelected |  | bool |  |
| MapObjectMask | Self |  | MapObjectMask |  |
| MapObjectMask | SetModified |  | void |  |
| MapObjectMask | SetName |  | void |  |
| MapObjectMask | SetSelected |  | void |  |
| MapObjectPainter | AccessSelf |  | MapObjectPainter | Category: const |
| MapObjectPainter | GetTextValidator |  | Unknown | Category: nonconst |
| MapObjectPainter | MarkAllMasksModified |  | void |  |
| MapObjectPainter | MaskList |  | Unknown |  |
| MapObjectPainter | Self |  | MapObjectPainter |  |
| MapObjectPainterMode | AccessSelf |  | MapObjectPainterMode | Category: const |
| MapObjectPainterMode | IsSelected |  | bool |  |
| MapObjectPainterMode | Self |  | MapObjectPainterMode |  |
| MapObjectPainterOptions | AccessBlurThresholdCtx |  | BlurThreshold | Category: const |
| MapObjectPainterOptions | AccessSelf |  | MapObjectPainterOptions | Category: const |
| MapObjectPainterOptions | GetPaintValue |  | float | Category: nonconst |
| MapObjectPainterOptions | IsCurrentBlendMode | CString | bool |  |
| MapObjectPainterOptions | Self |  | MapObjectPainterOptions |  |
| MapObjectPainterOptions | SetBlendMode | CString | void |  |
| MapObjectPainterOptions | SetPaintValue |  | void |  |
| MapObjectPainterOptions | SetPaintValueStr |  | void |  |
| MapObjectTool | AccessSelf |  | MapObjectTool | Category: const |
| MapObjectTool | IsCreateTool |  | bool |  |
| MapObjectTool | IsMovingObjects |  | bool |  |
| MapObjectTool | IsRotatingObjects |  | bool |  |
| MapObjectTool | IsScalingObjects |  | bool |  |
| MapObjectTool | IsSelectionModeMapContent |  | bool |  |
| MapObjectTool | IsSelectionModeObjects |  | bool |  |
| MapObjectTool | RotateRandom |  | void |  |
| MapObjectTool | Self |  | MapObjectTool |  |
| MapObjectTool | SetCreateTool |  | void |  |
| MapObjectTool | SetMovingObjects |  | void |  |
| MapObjectTool | SetRotatingObjects |  | void |  |
| MapObjectTool | SetScalingObjects |  | void |  |
| MapObjectTool | SetSelectionModeMapContent |  | void |  |
| MapObjectTool | SetSelectionModeObjects |  | void |  |
| Market | AccessLocalGoods | Unknown | Unknown | Category: const |
| Market | AccessLocalPrices | Goods | Unknown | Category: const |
| Market | AccessMarketCapital |  | State | Category: const |
| Market | AccessMarketGoods | Unknown | Unknown | Category: const |
| Market | AccessMarketGoodsSortedOnExports | Unknown | Unknown | Category: const |
| Market | AccessMarketGoodsSortedOnImports | Unknown | Unknown | Category: const |
| Market | AccessMarketStates |  | Unknown | Category: const |
| Market | AccessParticipants |  | Unknown | Category: const |
| Market | AccessSelf |  | Market | Category: const |
| Market | CalcSupplyToDemandRatio | Unknown | CFixedPoint |  |
| Market | CanTradeGoods | Goods | bool |  |
| Market | GetBalance |  | CFixedPoint | Category: nonconst |
| Market | GetBalanceDesc |  | CString | Category: nonconst |
| Market | GetCountryExportedAmount | Unknown Unknown | CFixedPoint | Category: nonconst |
| Market | GetCountryImportedAmount | Unknown Unknown | CFixedPoint | Category: nonconst |
| Market | GetCountryTradeCapacity | Country | int32 | Category: nonconst |
| Market | GetCountryTradeCapacityBalance | Country | int32 | Category: nonconst |
| Market | GetCountryTradeCapacityDesc | Country | CString | Category: nonconst |
| Market | GetCountryTradeCapacityUsage | Country | int32 | Category: nonconst |
| Market | GetCustom | CustomLocalization | CString | Category: nonconst |
| Market | GetEmptyFilters |  | Unknown | Category: nonconst |
| Market | GetExportAdvantage | Unknown | CFixedPoint | Category: nonconst |
| Market | GetExportedAmount | Goods | CFixedPoint | Category: nonconst |
| Market | GetExportedAmountToMarket | Market Goods | CFixedPoint | Category: nonconst |
| Market | GetExports |  | Unknown | Category: nonconst |
| Market | GetGDPContributionPercentage | Country | CFixedPoint | Category: nonconst |
| Market | GetGoodsSortedByBalance |  | Unknown | Category: nonconst |
| Market | GetGoodsWithShortage |  | Unknown | Category: nonconst |
| Market | GetImportAdvantage | Unknown | CFixedPoint | Category: nonconst |
| Market | GetImportedAmount | Goods | CFixedPoint | Category: nonconst |
| Market | GetImportedAmountFromMarket | Market Goods | CFixedPoint | Category: nonconst |
| Market | GetImports |  | Unknown | Category: nonconst |
| Market | GetMarketCapital |  | State | Category: nonconst |
| Market | GetMarketGDPValue |  | CFixedPoint | Category: nonconst |
| Market | GetMarketSharePercentageFor | Country | CFixedPoint | Category: nonconst |
| Market | GetMaxImbalance |  | CFixedPoint | Category: nonconst |
| Market | GetMaxImbalanceScaledByBasePrice |  | CFixedPoint | Category: nonconst |
| Market | GetModifier |  | Modifier | Category: nonconst |
| Market | GetModifierDesc |  | CString | Category: nonconst |
| Market | GetName |  | CString | Category: nonconst |
| Market | GetNameNoFormatting |  | CString | Category: nonconst |
| Market | GetNameNoFormattingIncludingStatus |  | CString | Category: nonconst |
| Market | GetOwner |  | Country | Category: nonconst |
| Market | GetRelativeExportAdvantage | Unknown | CFixedPoint | Category: nonconst |
| Market | GetRelativeExportAdvantageDesc | Unknown | CString | Category: nonconst |
| Market | GetRelativeImportAdvantage | Unknown | CFixedPoint | Category: nonconst |
| Market | GetRelativeImportAdvantageDesc | Unknown | CString | Category: nonconst |
| Market | GetTooltipTag |  | CString | Category: nonconst |
| Market | GetTopGoodsByHighestBalance | int32 | Unknown | Category: nonconst |
| Market | GetTopGoodsByLowestBalance | int32 | Unknown | Category: nonconst |
| Market | GetTotalBuyOrders |  | CFixedPoint | Category: nonconst |
| Market | GetTotalExportedAmount |  | CFixedPoint | Category: nonconst |
| Market | GetTotalImportedAmount |  | CFixedPoint | Category: nonconst |
| Market | GetTotalSellOrders |  | CFixedPoint | Category: nonconst |
| Market | GetTradeSurplus |  | CFixedPoint | Category: nonconst |
| Market | GetTradeSurplusBreakdown |  | CString | Category: nonconst |
| Market | HasAnyGoodsShortage |  | bool |  |
| Market | HasBuildingGoodsShortage | Unknown | bool |  |
| Market | HasGoodsShortage | Unknown | bool |  |
| Market | HasPopGoodsShortage | Unknown | bool |  |
| Market | IsBeingHighlighted |  | bool |  |
| Market | IsBeingTutorialHighlighted |  | bool |  |
| Market | IsCapitalMarket | Unknown | bool |  |
| Market | IsPinnedInOutliner |  | bool |  |
| Market | IsSame | Market | bool |  |
| Market | IsValid |  | bool |  |
| Market | MakeScope |  | Scope |  |
| Market | RestoreSort |  | void |  |
| Market | Self |  | Market |  |
| Market | Sort | CString | void |  |
| Market | SortStates | CString | void |  |
| Market | TogglePinInOutliner |  | void |  |
| MarketGoods | AccessSelf |  | MarketGoods | Category: const |
| MarketGoods | GetBreakdownOfBuildingsAffectedByShortage |  | CString | Category: nonconst |
| MarketGoods | GetCustom | CustomLocalization | CString | Category: nonconst |
| MarketGoods | GetGoods |  | Goods | Category: nonconst |
| MarketGoods | GetIDString |  | CString | Category: nonconst |
| MarketGoods | GetMarket |  | Market | Category: nonconst |
| MarketGoods | GetNumBuildingsAffectedByShortage |  | int32 | Category: nonconst |
| MarketGoods | GetTooltipTag |  | CString | Category: nonconst |
| MarketGoods | MakeScope |  | Scope |  |
| MarketGoods | Self |  | MarketGoods |  |
| MarketPanel | AccessSelf |  | MarketPanel | Category: const |
| MarketPanel | Filter | CString | void |  |
| MarketPanel | GetFilters |  | Unknown | Category: nonconst |
| MarketPanel | IsSelected | CString | bool |  |
| MarketPanel | Self |  | MarketPanel |  |
| MarketsMarker | AccessSelf |  | MarketsMarker | Category: const |
| MarketsMarker | GetAnyMarket |  | Market | Category: nonconst |
| MarketsMarker | GetGoodsListCount |  | int32 | Category: nonconst |
| MarketsMarker | GetMarketsMarkerListItems |  | Unknown | Category: nonconst |
| MarketsMarker | GetPosition |  | CVector2f | Category: nonconst |
| MarketsMarker | OpenMarketPanel |  | void |  |
| MarketsMarker | Self |  | MarketsMarker |  |
| MarketsMarkerListItem | AccessSelf |  | MarketsMarkerListItem | Category: const |
| MarketsMarkerListItem | GetPanelDescription |  | CString | Category: nonconst |
| MarketsMarkerListItem | Self |  | MarketsMarkerListItem |  |
| MaskEntry | AccessSelf |  | MaskEntry | Category: const |
| MaskEntry | GetKey |  | CString | Category: nonconst |
| MaskEntry | Self |  | MaskEntry |  |
| MaskManagerEntry | AccessSelf |  | MaskManagerEntry | Category: const |
| MaskManagerEntry | GetKey |  | CString | Category: nonconst |
| MaskManagerEntry | IsLocked |  | bool |  |
| MaskManagerEntry | IsSelected |  | bool |  |
| MaskManagerEntry | Self |  | MaskManagerEntry |  |
| MaskManagerEntry | SetLocked | bool | void |  |
| MaskManagerEntry | SetSelected | bool | void |  |
| MaskPainterDynamicTerrain | AccessSelf |  | MaskPainterDynamicTerrain | Category: const |
| MaskPainterDynamicTerrain | ClearSelected |  | void |  |
| MaskPainterDynamicTerrain | GetTerrainType |  | CString | Category: nonconst |
| MaskPainterDynamicTerrain | GetTerrainValue |  | float | Category: nonconst |
| MaskPainterDynamicTerrain | HasAnySelectedSetTerrainType |  | bool |  |
| MaskPainterDynamicTerrain | OpenDatabase |  | void |  |
| MaskPainterDynamicTerrain | Self |  | MaskPainterDynamicTerrain |  |
| MaskPainterDynamicTerrain | SetTerrainValue |  | void |  |
| MaskPainterDynamicTerrain | SetTerrainValueStr |  | void |  |
| MaskPainterManager | AccessSelf |  | MaskPainterManager | Category: const |
| MaskPainterManager | CanModify |  | bool |  |
| MaskPainterManager | ClearFilter |  | void |  |
| MaskPainterManager | GetFilter |  | CString | Category: nonconst |
| MaskPainterManager | GetSelectedMaskDesc |  | CString | Category: nonconst |
| MaskPainterManager | IsAnyMaskSelected |  | bool |  |
| MaskPainterManager | IsSelectedMaskTypeDeveloper |  | bool |  |
| MaskPainterManager | IsSelectedMaskTypeLocal |  | bool |  |
| MaskPainterManager | OnClear |  | void |  |
| MaskPainterManager | OnClone |  | void |  |
| MaskPainterManager | OnDelete |  | void |  |
| MaskPainterManager | OnNew |  | void |  |
| MaskPainterManager | OnRename |  | void |  |
| MaskPainterManager | Self |  | MaskPainterManager |  |
| MaskPainterManager | SetFilter |  | void |  |
| MaskPainterManager | SetSelectedMaskDesc |  | void |  |
| MaskPainterManager | ToggleMaskTypeDeveloper |  | void |  |
| MaskPainterManager | ToggleMaskTypeLocal |  | void |  |
| MaskPainterMapContentPanel | AccessSelf |  | MaskPainterMapContentPanel | Category: const |
| MaskPainterMapContentPanel | Self |  | MaskPainterMapContentPanel |  |
| MaskPainterMode | AccessSelf |  | MaskPainterMode | Category: const |
| MaskPainterMode | IsSelected |  | bool |  |
| MaskPainterMode | Self |  | MaskPainterMode |  |
| MaskPainterTool | AccessSelf |  | MaskPainterTool | Category: const |
| MaskPainterTool | IsEraserMode |  | bool |  |
| MaskPainterTool | IsEyeDropperMode |  | bool |  |
| MaskPainterTool | IsMapContentSelectionMode |  | bool |  |
| MaskPainterTool | IsPaintMode |  | bool |  |
| MaskPainterTool | Self |  | MaskPainterTool |  |
| MaskPainterTool | SetEraserMode |  | void |  |
| MaskPainterTool | SetEyeDropperMode | bool | void |  |
| MaskPainterTool | SetMapContentSelectionMode | bool | void |  |
| MaskPainterTool | SetPaintMode |  | void |  |
| MaskPainterViewport | AccessSelf |  | MaskPainterViewport | Category: const |
| MaskPainterViewport | Self |  | MaskPainterViewport |  |
| Material | AccessSelf |  | Material | Category: const |
| Material | GetDiffuseTexture |  | Unknown | Category: nonconst |
| Material | GetName |  | CString | Category: nonconst |
| Material | GetThumbnail |  | Unknown | Category: nonconst |
| Material | IsHighlighted |  | bool |  |
| Material | IsLocked |  | bool |  |
| Material | IsSelected |  | bool |  |
| Material | Self |  | Material |  |
| Material | ToggleHighlight |  | void |  |
| Material | ToggleLocked |  | void |  |
| Material | ToggleSelected |  | void |  |
| MaterialBrowser | AccessSelf |  | MaterialBrowser | Category: const |
| MaterialBrowser | Apply |  | void |  |
| MaterialBrowser | Cancel |  | void |  |
| MaterialBrowser | GetCurrentMaterialsList |  | Unknown | Category: nonconst |
| MaterialBrowser | GetSearchFilter |  | CUTF8String | Category: nonconst |
| MaterialBrowser | IsAnyMaterialSelected |  | bool |  |
| MaterialBrowser | IsMaterialDisabled | Unknown | bool |  |
| MaterialBrowser | IsMaterialSelected | Unknown | bool |  |
| MaterialBrowser | Self |  | MaterialBrowser |  |
| MaterialBrowser | SetSearchFilter |  | void |  |
| MaterialBrowser | ToggleMaterialSelected | Unknown | void |  |
| MaterialEntry | AccessSelf |  | MaterialEntry | Category: const |
| MaterialEntry | GetRawValue |  | int32 | Category: nonconst |
| MaterialEntry | GetValue |  | float | Category: nonconst |
| MaterialEntry | IsVisible |  | bool |  |
| MaterialEntry | Self |  | MaterialEntry |  |
| MaterialMix | AccessMaterials |  | Unknown | Category: const |
| MaterialMix | AccessSelf |  | MaterialMix | Category: const |
| MaterialMix | CanAddMaterialEntry |  | bool |  |
| MaterialMix | GetMaterials |  | Unknown | Category: nonconst |
| MaterialMix | GetMaterialsCount |  | int32 | Category: nonconst |
| MaterialMix | GetName |  | CUTF8String | Category: nonconst |
| MaterialMix | IsPersistent |  | bool |  |
| MaterialMix | Self |  | MaterialMix |  |
| MaterialMix | SetValue | MaterialMixEntry | void |  |
| MaterialMix | TogglePersistence |  | void |  |
| MaterialMixBrush | AccessSamples |  | Unknown | Category: const |
| MaterialMixBrush | AccessSelf |  | MaterialMixBrush | Category: const |
| MaterialMixBrush | ChangeSampleEntryComposition | MaterialMix MaterialMixEntry | void |  |
| MaterialMixBrush | Delete | MaterialMix | void |  |
| MaterialMixBrush | EndSampleCompositionEdit | MaterialMix | void |  |
| MaterialMixBrush | IsSampling |  | bool |  |
| MaterialMixBrush | IsSelected | MaterialMix | bool |  |
| MaterialMixBrush | RenameSample | MaterialMix | void |  |
| MaterialMixBrush | Samples |  | Unknown |  |
| MaterialMixBrush | Self |  | MaterialMixBrush |  |
| MaterialMixBrush | StartSampleCompositionEdit | MaterialMix | void |  |
| MaterialMixBrush | ToggleSampleEntryLock | MaterialMix MaterialMixEntry | void |  |
| MaterialMixBrush | ToggleSamplePersistence | MaterialMix | void |  |
| MaterialMixBrush | ToggleSelected | MaterialMix | void |  |
| MaterialMixEntry | AccessSelf |  | MaterialMixEntry | Category: const |
| MaterialMixEntry | GetPercentageValue |  | float | Category: nonconst |
| MaterialMixEntry | GetValue |  | float | Category: nonconst |
| MaterialMixEntry | GetValueAsText |  | CString | Category: nonconst |
| MaterialMixEntry | IsLocked |  | bool |  |
| MaterialMixEntry | Self |  | MaterialMixEntry |  |
| MaterialMixEntry | SetPercentageValue | Unknown | void |  |
| MaterialMixEntry | ToggleLocked |  | void |  |
| MaterialPaintingMode | AccessBlurThresholdCtx |  | BlurThreshold | Category: const |
| MaterialPaintingMode | AccessSelf |  | MaterialPaintingMode | Category: const |
| MaterialPaintingMode | FocusCameraOnError |  | void |  |
| MaterialPaintingMode | IsBlurSelected |  | bool |  |
| MaterialPaintingMode | IsBrushSettingsLock |  | bool |  |
| MaterialPaintingMode | IsEraserSelected |  | bool |  |
| MaterialPaintingMode | IsEyeDropperSelected |  | bool |  |
| MaterialPaintingMode | IsPainterSelected |  | bool |  |
| MaterialPaintingMode | IsPaintingAllowed |  | bool |  |
| MaterialPaintingMode | IsSearchingForError |  | bool |  |
| MaterialPaintingMode | IsSelected |  | bool |  |
| MaterialPaintingMode | IsTrimWhilePainting |  | bool |  |
| MaterialPaintingMode | IsTrimmerSelected |  | bool |  |
| MaterialPaintingMode | SelectBlur |  | void |  |
| MaterialPaintingMode | SelectEraser |  | void |  |
| MaterialPaintingMode | SelectEyeDropper |  | void |  |
| MaterialPaintingMode | SelectPainter |  | void |  |
| MaterialPaintingMode | SelectTrimmer |  | void |  |
| MaterialPaintingMode | Self |  | MaterialPaintingMode |  |
| MaterialPaintingMode | SetBrushSettingsLock | bool | void |  |
| MaterialPaintingMode | SetTrimWhilePainting | bool | void |  |
| Materials | AccessSelf |  | Materials | Category: const |
| Materials | GetList |  | Unknown | 类别：nonconst |
| Materials | List |  | Unknown |  |
| Materials | SelectFirst |  | void |  |
| Materials | SelectLast |  | void |  |
| Materials | SelectNext |  | void |  |
| Materials | SelectPrevious |  | void |  |
| Materials | Self |  | Materials |  |
| Materials | ToggleHighlight |  | void |  |
| Materials | ToggleLocked |  | void |  |
| MaterialsSample | AccessSelf |  | MaterialsSample | 类别：const |
| MaterialsSample | Entries |  | Unknown |  |
| MaterialsSample | GetX |  | int32 | 类别：nonconst |
| MaterialsSample | GetY |  | int32 | 类别：nonconst |
| MaterialsSample | Self |  | MaterialsSample |  |
| MeshImporter | AccessMaterialImportSettings |  | MeshImporterMaterials | 类别：const |
| MeshImporter | AccessSelf |  | MeshImporter | 类别：const |
| MeshImporter | AccessUndoer |  | UndoStack | 类别：const |
| MeshImporter | EditShaderSets |  | void |  |
| MeshImporter | GetInputFileName |  | CString | 类别：nonconst |
| MeshImporter | GetLogEntryCountCritical |  | int32 | 类别：nonconst |
| MeshImporter | GetLogEntryCountError |  | int32 | 类别：nonconst |
| MeshImporter | GetLogEntryCountInfo |  | int32 | 类别：nonconst |
| MeshImporter | GetLogEntryCountWarning |  | int32 | 类别：nonconst |
| MeshImporter | GetSettingsFileName |  | CString | 类别：nonconst |
| MeshImporter | ImportCurrentlySelected |  | void |  |
| MeshImporter | IsAutoSaveOnImport |  | bool |  |
| MeshImporter | IsBrowserViewOpen |  | bool |  |
| MeshImporter | IsLogViewOpen |  | bool |  |
| MeshImporter | IsMeshLodded |  | bool |  |
| MeshImporter | IsSettingsDifferentThanDiskFile |  | bool |  |
| MeshImporter | IsSettingsDiskFileExist |  | bool |  |
| MeshImporter | IsTargetMesh2 |  | bool |  |
| MeshImporter | SaveSettings |  | void |  |
| MeshImporter | Self |  | MeshImporter |  |
| MeshImporter | ToggleAutoSaveOnImport |  | void |  |
| MeshImporter | ToggleBrowserView |  | void |  |
| MeshImporter | ToggleLogView |  | void |  |
| MeshImporterBrowser | AccessSelf |  | MeshImporterBrowser | 类别：const |
| MeshImporterBrowser | ClearQueue |  | void |  |
| MeshImporterBrowser | DeselectAllFiles |  | void |  |
| MeshImporterBrowser | GetAllFiles |  | Unknown | 类别：nonconst |
| MeshImporterBrowser | GetQueuedFiles |  | Unknown | 类别：nonconst |
| MeshImporterBrowser | ImportAllInQueue |  | void |  |
| MeshImporterBrowser | ReloadAllFiles |  | void |  |
| MeshImporterBrowser | SelectAllFiles |  | void |  |
| MeshImporterBrowser | Self |  | MeshImporterBrowser |  |
| MeshImporterBrowserEntry | AccessSelf |  | MeshImporterBrowserEntry | 类别：const |
| MeshImporterBrowserEntry | GetFileDescription |  | CString | 类别：nonconst |
| MeshImporterBrowserEntry | GetFileName |  | Unknown | 类别：nonconst |
| MeshImporterBrowserEntry | GetFullPath |  | Unknown | 类别：nonconst |
| MeshImporterBrowserEntry | IsInQueue |  | bool |  |
| MeshImporterBrowserEntry | IsSelected |  | bool |  |
| MeshImporterBrowserEntry | IsSettingsDifferentThanDiskFile |  | bool |  |
| MeshImporterBrowserEntry | IsSettingsDiskFileExist |  | bool |  |
| MeshImporterBrowserEntry | Self |  | MeshImporterBrowserEntry |  |
| MeshImporterBrowserEntry | ToggleQueue |  | void |  |
| MeshImporterBrowserEntry | ToggleSelect |  | void |  |
| MeshImporterMaterialEntry | AccessSelf |  | MeshImporterMaterialEntry | 类别：const |
| MeshImporterMaterialEntry | GetDetailsDescription |  | CString | 类别：nonconst |
| MeshImporterMaterialEntry | GetMaterialIndex |  | int32 | 类别：nonconst |
| MeshImporterMaterialEntry | GetName |  | CString | 类别：nonconst |
| MeshImporterMaterialEntry | GetNumberGeometriesUsingMaterial |  | int32 | 类别：nonconst |
| MeshImporterMaterialEntry | InjectPropertyList | PdxGuiWidget CString | void |  |
| MeshImporterMaterialEntry | IsCollision |  | bool |  |
| MeshImporterMaterialEntry | Self |  | MeshImporterMaterialEntry |  |
| MeshImporterMaterialEntry | ToggleCollision |  | void |  |
| MeshImporterMaterials | AccessMaterialEntries |  | Unknown | 类别：const |
| MeshImporterMaterials | AccessSelf |  | MeshImporterMaterials | 类别：const |
| MeshImporterMaterials | GetMaterialEntries |  | Unknown | 类别：nonconst |
| MeshImporterMaterials | Self |  | MeshImporterMaterials |  |
| MessageFeedHandler | AccessSelf |  | MessageFeedHandler | 类别：const |
| MessageFeedHandler | GetItems |  | Unknown | 类别：nonconst |
| MessageFeedHandler | GetNumberOfQueuedMessages |  | int32 | 类别：nonconst |
| MessageFeedHandler | HasQueuedMessages |  | bool |  |
| MessageFeedHandler | MarkAllForDelete |  | void |  |
| MessageFeedHandler | Self |  | MessageFeedHandler |  |
| MessageFeedHandler | ShowNotificationFeedNextToOutliner |  | bool |  |
| MessageSettingsWindow | AccessSelf |  | MessageSettingsWindow | 类别：const |
| MessageSettingsWindow | CurrentSituationLabelSelectTotal |  | void |  |
| MessageSettingsWindow | CurrentSituationLabelSelectUnread |  | void |  |
| MessageSettingsWindow | GetAlertSettingsItems |  | Unknown | 类别：nonconst |
| MessageSettingsWindow | GetInterestingCountryItems |  | Unknown | 类别：nonconst |
| MessageSettingsWindow | GetNotificationSettingsItems |  | Unknown | 类别：nonconst |
| MessageSettingsWindow | HasPauseOnEvent |  | bool |  |
| MessageSettingsWindow | HasSingleShownItem |  | bool |  |
| MessageSettingsWindow | IsCurrentSituationLabelTotal |  | bool |  |
| MessageSettingsWindow | OnChangeInterestingCountrySettings |  | void |  |
| MessageSettingsWindow | RemoveSingleShownItem |  | void |  |
| MessageSettingsWindow | ResetAlertSettings |  | void |  |
| MessageSettingsWindow | ResetNotificationSettings |  | void |  |
| MessageSettingsWindow | Self |  | MessageSettingsWindow |  |
| MessageSettingsWindow | SetSingleShownItem | Unknown | void |  |
| MessageSettingsWindow | ShouldBeShown | CString | bool |  |
| MessageSettingsWindow | SortInterestingCountryItemsIfNeeded |  | void |  |
| MessageSettingsWindow | TogglePauseOnEvent |  | void |  |
| MetadataWindow | AccessSelf |  | MetadataWindow | 类别：const |
| MetadataWindow | Close |  | void |  |
| MetadataWindow | GetTitle |  | CString | 类别：nonconst |
| MetadataWindow | IsOpen |  | bool |  |
| MetadataWindow | IsSelectedAnyNode |  | bool |  |
| MetadataWindow | Open |  | void |  |
| MetadataWindow | Self |  | MetadataWindow |  |
| MetadataWindow | Toggle |  | void |  |
| MilitaryFormation | AccessSelf |  | MilitaryFormation | 类别：const |
| MilitaryFormation | CanAnyUnitBeUpgraded |  | bool |  |
| MilitaryFormation | CanDeployToFront |  | bool |  |
| MilitaryFormation | CanDeployToSeaNode |  | bool |  |
| MilitaryFormation | CanInvade |  | bool |  |
| MilitaryFormation | CanRecruitConscriptUnit | CombatUnitType | bool |  |
| MilitaryFormation | CanRecruitConscriptUnitTooltip | CombatUnitType | CString |  |
| MilitaryFormation | CanRecruitRegularUnit | CombatUnitType | bool |  |
| MilitaryFormation | CanRecruitRegularUnitTooltip | CombatUnitType | CString |  |
| MilitaryFormation | CanStation |  | bool |  |
| MilitaryFormation | Demobilize |  | Command |  |
| MilitaryFormation | Deselect |  | void |  |
| MilitaryFormation | Disband |  | Command |  |
| MilitaryFormation | FindLeastExperiencedConscriptUnit | Unknown | CombatUnit |  |
| MilitaryFormation | FindLeastExperiencedRegularUnit | CombatUnitType | CombatUnit |  |
| MilitaryFormation | GetAIDebugInfo |  | CString | 类别：nonconst |
| MilitaryFormation | GetActiveBattles |  | Unknown | 类别：nonconst |
| MilitaryFormation | GetAttritionRaw |  | CFixedPoint | 类别：nonconst |
| MilitaryFormation | GetAttritionRiskDesc |  | CString | 类别：nonconst |
| MilitaryFormation | GetAverageAttritionPerWeek |  | CFixedPoint | 类别：nonconst |
| MilitaryFormation | GetAverageDefense |  | CFixedPoint | 类别：nonconst |
| MilitaryFormation | GetAverageDefenseExcludeUnavailableManpower |  | CFixedPoint | 类别：nonconst |
| MilitaryFormation | GetAverageOffense |  | CFixedPoint | 类别：nonconst |
| MilitaryFormation | GetAverageOffenseExcludeUnavailableManpower |  | CFixedPoint | 类别：nonconst |
| MilitaryFormation | GetBorrowSettings |  | Unknown | 类别：nonconst |
| MilitaryFormation | GetBuildings |  | Unknown | 类别：nonconst |
| MilitaryFormation | GetBuildingsDesc |  | CString | 类别：nonconst |
| MilitaryFormation | GetCombatUnitEntries |  | Unknown | 类别：nonconst |
| MilitaryFormation | GetCombatUnitsTypeIcon |  | CString | 类别：nonconst |
| MilitaryFormation | GetCommandLimit |  | CString | 类别：nonconst |
| MilitaryFormation | GetCommandLimitDesc |  | CString | 类别：nonconst |
| MilitaryFormation | GetCommandLimitRaw |  | int32 | 类别：nonconst |
| MilitaryFormation | GetCommanders |  | Unknown | 类别：nonconst |
| MilitaryFormation | GetCommandersWithRecruitableSlot |  | Unknown | 类别：nonconst |
| MilitaryFormation | GetCommonDebugInfo |  | CString | 类别：nonconst |
| MilitaryFormation | GetConscriptPowerProjection |  | CFixedPoint | 类别：nonconst |
| MilitaryFormation | GetConscriptPowerProjectionDesc |  | CString | 类别：nonconst |
| MilitaryFormation | GetConscriptUnitsByTypeBreakdown | CombatUnitType | CString | 类别：nonconst |
| MilitaryFormation | GetConscriptsGroupsBreakdown |  | CString | 类别：nonconst |
| MilitaryFormation | GetConscriptsMobilizationPercentage |  | CFixedPoint | 类别：nonconst |
| MilitaryFormation | GetCountry |  | Country | 类别：nonconst |
| MilitaryFormation | GetCurrentBlockadeStrength |  | CFixedPoint | 类别：nonconst |
| MilitaryFormation | GetCurrentFront |  | Front | 类别：nonconst |
| MilitaryFormation | GetCurrentHQ |  | Hq | 类别：nonconst |
| MilitaryFormation | GetCurrentManpower |  | int64 | 类别：nonconst |
| MilitaryFormation | GetCurrentSeaNode |  | Province | 类别：nonconst |
| MilitaryFormation | GetCustom | CustomLocalization | CString | 类别：nonconst |
| MilitaryFormation | GetDemobilizationStatus |  | CString | 类别：nonconst |
| MilitaryFormation | GetDisbandUnitCommand | CombatUnit | Command | 类别：nonconst |
| MilitaryFormation | GetDisbandUnitTypeConscriptCommand | CombatUnitType | Command | 类别：nonconst |
| MilitaryFormation | GetDisbandUnitTypeRegularCommand | CombatUnitType | Command | 类别：nonconst |
| MilitaryFormation | GetEffectFromBeingExiledDesc |  | CString | 类别：nonconst |
| MilitaryFormation | GetEffectFromCommandLimitDesc |  | CString | 类别：nonconst |
| MilitaryFormation | GetEffectFromSpecialUnitsDesc |  | CString | 类别：nonconst |
| MilitaryFormation | GetEffectOfDefaultUnitTypeChange | CombatUnitType | CString | 类别：nonconst |
| MilitaryFormation | GetEligibleGroups |  | Unknown | 类别：nonconst |
| MilitaryFormation | GetEligibleTypesByGroup | CombatUnitGroup | Unknown | 类别：nonconst |
| MilitaryFormation | GetEstimatedMobilizationCostDesc |  | CString | 类别：nonconst |
| MilitaryFormation | GetEstimatedMobilizationCostFormatted |  | CString | 类别：nonconst |
| MilitaryFormation | GetEstimatedMobilizationCostRaw |  | CFixedPoint | 类别：nonconst |
| MilitaryFormation | GetExpectedNumRegulars |  | int32 | 类别：nonconst |
| MilitaryFormation | GetFlag |  | Unknown | 类别：nonconst |
| MilitaryFormation | GetFlagColor |  | CVector4f | 类别：nonconst |
| MilitaryFormation | GetFlotillaGroupsBreakdown |  | CString | 类别：nonconst |
| MilitaryFormation | GetFormationStatusDesc |  | CString | 类别：nonconst |
| MilitaryFormation | GetFrontDistributionDesc |  | CString | 类别：nonconst |
| MilitaryFormation | GetGoodsConsumptionCostRaw |  | CFixedPoint | 类别：nonconst |
| MilitaryFormation | GetGoodsConsumptionDesc |  | CString | 类别：nonconst |
| MilitaryFormation | GetIDString |  | CString | 类别：nonconst |
| MilitaryFormation | GetIncomingNumRegulars |  | int32 | 类别：nonconst |
| MilitaryFormation | GetIncomingNumRegularsFromBuilding | Building | int32 | 类别：nonconst |
| MilitaryFormation | GetIncomingNumRegularsOfUnitType | CombatUnitType | int32 | 类别：nonconst |
| MilitaryFormation | GetInvasionTooltip |  | CString | 类别：nonconst |
| MilitaryFormation | GetLocationString |  | CString | 类别：nonconst |
| MilitaryFormation | GetLowOrganizationDesc |  | CString | 类别：nonconst |
| MilitaryFormation | GetMaxBlockadeStrength |  | CFixedPoint | 类别：nonconst |
| MilitaryFormation | GetMaxConscripts |  | int32 | 类别：nonconst |
| MilitaryFormation | GetMaxManpower |  | int64 | 类别：nonconst |
| MilitaryFormation | GetMobilizationModifier |  | Modifier | 类别：nonconst |
| MilitaryFormation | GetMobilizationOptions |  | Unknown | 类别：nonconst |
| MilitaryFormation | GetMobilizationPercentage |  | CFixedPoint | 类别：nonconst |
| MilitaryFormation | GetMobilizationPercentageFormatted |  | CString | 类别：nonconst |
| MilitaryFormation | GetModifier |  | Modifier | 类别：nonconst |
| MilitaryFormation | GetMorale |  | CFixedPoint | 类别：nonconst |
| MilitaryFormation | GetName |  | CString | 类别：nonconst |
| MilitaryFormation | GetNameNoFormatting |  | CString | 类别：nonconst |
| MilitaryFormation | GetNameWithCountryFlag |  | CString | 类别：nonconst |
| MilitaryFormation | GetNumCombatUnits |  | int32 | 类别：nonconst |
| MilitaryFormation | GetNumConscripts |  | int32 | 类别：nonconst |
| MilitaryFormation | GetNumConscriptsCombatUnitsOfType | CombatUnitType | int32 | 类别：nonconst |
| MilitaryFormation | GetNumConscriptsUnitsInGroup | CombatUnitGroup | int32 | 类别：nonconst |
| MilitaryFormation | GetNumDeployToFrontSelections |  | int32 | 类别：nonconst |
| MilitaryFormation | GetNumDeployToSeaNodeSelections |  | int32 | 类别：nonconst |
| MilitaryFormation | GetNumExpectedConscriptsCombatUnitsOfType | CombatUnitType | int32 | 类别：nonconst |
| MilitaryFormation | GetNumExpectedConscriptsCombatUnitsOfTypeFromState | Unknown Unknown | int32 | 类别：nonconst |
| MilitaryFormation | GetNumExpectedConscriptsUnitsInGroup | CombatUnitGroup | int32 | 类别：nonconst |
| MilitaryFormation | GetNumExpectedRegularCombatUnitsOfType | CombatUnitType | int32 | 类别：nonconst |
| MilitaryFormation | GetNumFlotillaUnitsInGroup | Unknown | int32 | 类别：nonconst |
| MilitaryFormation | GetNumFullyMobilizedConscripts |  | int32 | 类别：nonconst |
| MilitaryFormation | GetNumFullyMobilizedRegulars |  | int32 | 类别：nonconst |
| MilitaryFormation | GetNumFullyMobilizedTotalUnits |  | int32 | 类别：nonconst |
| MilitaryFormation | GetNumInvasionSelections |  | int32 | 类别：nonconst |
| MilitaryFormation | GetNumRegularCombatUnitsOfType | CombatUnitType | int32 | 类别：nonconst |
| MilitaryFormation | GetNumRegulars |  | int32 | 类别：nonconst |
| MilitaryFormation | GetNumRegularsUnitsInGroup | CombatUnitGroup | int32 | 类别：nonconst |
| MilitaryFormation | GetNumSpecialUnits |  | int32 | 类别：nonconst |
| MilitaryFormation | GetNumSpecialUnitsExpected |  | int32 | 类别：nonconst |
| MilitaryFormation | GetNumStationSelections |  | int32 | 类别：nonconst |
| MilitaryFormation | GetNumStrategicObjectiveActive |  | int32 | 类别：nonconst |
| MilitaryFormation | GetNumStrategicObjectiveSelections |  | int32 | 类别：nonconst |
| MilitaryFormation | GetNumTotalCombatUnitsExpectedInGroup | CombatUnitGroup | int32 | 类别：nonconst |
| MilitaryFormation | GetNumTotalCombatUnitsInGroup | CombatUnitGroup | int32 | 类别：nonconst |
| MilitaryFormation | GetNumTotalCombatUnitsOfType | Unknown | int32 | 类别：nonconst |
| MilitaryFormation | GetOrganization |  | CString | 类别：nonconst |
| MilitaryFormation | GetOrganizationDailyChange |  | CFixedPoint | 类别：nonconst |
| MilitaryFormation | GetOrganizationDailyChangeDesc |  | CString | 类别：nonconst |
| MilitaryFormation | GetOrganizationPercentage |  | CFixedPoint | 类别：nonconst |
| MilitaryFormation | GetOrganizationRaw |  | CFixedPoint | 类别：nonconst |
| MilitaryFormation | GetOrganizationTargetDesc |  | CString | 类别：nonconst |
| MilitaryFormation | GetOrganizationTargetFormatted |  | CString | 类别：nonconst |
| MilitaryFormation | GetOrganizationTargetPercentage |  | CFixedPoint | 类别：nonconst |
| MilitaryFormation | GetOrganizationTargetRaw |  | CFixedPoint | 类别：nonconst |
| MilitaryFormation | GetPowerProjection |  | CFixedPoint | 类别：nonconst |
| MilitaryFormation | GetPowerProjectionDesc |  | CString | 类别：nonconst |
| MilitaryFormation | GetPrimaryCultureForGroup | Unknown | Culture | 类别：nonconst |
| MilitaryFormation | GetPrimaryCultureForType | Unknown | Culture | 类别：nonconst |
| MilitaryFormation | GetRegularPowerProjection |  | CFixedPoint | 类别：nonconst |
| MilitaryFormation | GetRegularPowerProjectionDesc |  | CString | 类别：nonconst |
| MilitaryFormation | GetRegularUnitsByTypeBreakdown | CombatUnitType | CString | 类别：nonconst |
| MilitaryFormation | GetRegularsGroupsBreakdown |  | CString | 类别：nonconst |
| MilitaryFormation | GetRegularsMobilizationPercentage |  | CFixedPoint | 类别：nonconst |
| MilitaryFormation | GetRepairProgress |  | CFixedPoint | 类别：nonconst |
| MilitaryFormation | GetSeaPresence |  | CFixedPoint | 类别：nonconst |
| MilitaryFormation | GetSeaPresencePerDay |  | CFixedPoint | 类别：nonconst |
| MilitaryFormation | GetSelectedUnitTypeForGroup | CombatUnitGroup | CombatUnitType | 类别：nonconst |
| MilitaryFormation | GetSetDefaultUnitTypeCommand | CombatUnitType | Command | 类别：nonconst |
| MilitaryFormation | GetShippingLane |  | ShippingLane | 类别：nonconst |
| MilitaryFormation | GetShippingLaneDesc |  | CString | 类别：nonconst |
| MilitaryFormation | GetShortFormationStatusDesc |  | CString | 类别：nonconst |
| MilitaryFormation | GetSupply |  | CString | 类别：nonconst |
| MilitaryFormation | GetSupplyRaw |  | CFixedPoint | 类别：nonconst |
| MilitaryFormation | GetSupplyTooltip |  | CString | 类别：nonconst |
| MilitaryFormation | GetTargetSeaNode |  | Province | 类别：nonconst |
| MilitaryFormation | GetTooltipTag |  | CString | 类别：nonconst |
| MilitaryFormation | GetTravelDaysLeft |  | int32 | 类别：nonconst |
| MilitaryFormation | GetTravelTimeLeftLabel |  | CString | 类别：nonconst |
| MilitaryFormation | GetUnitIcon |  | CString | 类别：nonconst |
| MilitaryFormation | GetUnitLabel |  | CString | 类别：nonconst |
| MilitaryFormation | GetUnitTypesByConscriptsGroupBreakdown | CombatUnitGroup | CString | 类别：nonconst |
| MilitaryFormation | GetUnitTypesByFlotillaGroupBreakdown | CombatUnitGroup | CString | 类别：nonconst |
| MilitaryFormation | GetUnitTypesByRegularsGroupBreakdown | CombatUnitGroup | CString | 类别：nonconst |
| MilitaryFormation | GetUpgradeAllUnitsCommand |  | Command | 类别：nonconst |
| MilitaryFormation | GetUpgradeConscriptUnitTypeCommand | CombatUnitType | Command | 类别：nonconst |
| MilitaryFormation | GetUpgradeRegularUnitTypeCommand | CombatUnitType | Command | 类别：nonconst |
| MilitaryFormation | GetUpgradeUnitGroupCommand | CombatUnitGroup | Command | 类别：nonconst |
| MilitaryFormation | HasInvasion |  | bool |  |
| MilitaryFormation | HasRaisedConscripts |  | bool |  |
| MilitaryFormation | HasSelectedUnitTypeForGroup | CombatUnitGroup | bool |  |
| MilitaryFormation | HasShippingLane |  | bool |  |
| MilitaryFormation | HasTooManySpecialUnits |  | bool |  |
| MilitaryFormation | HasTooManySpecialUnitsExpected |  | bool |  |
| MilitaryFormation | HasTooManySpecialUnitsExpectedInGroup | CombatUnitGroup | bool |  |
| MilitaryFormation | HasTooManySpecialUnitsInGroup | CombatUnitGroup | bool |  |
| MilitaryFormation | IsAdvancing |  | bool |  |
| MilitaryFormation | IsAdvancingInBattle |  | bool |  |
| MilitaryFormation | IsArmy |  | bool |  |
| MilitaryFormation | IsBeingHighlighted |  | bool |  |
| MilitaryFormation | IsBeingTutorialHighlighted |  | bool |  |
| MilitaryFormation | IsConscriptUnitTypeUpgrading | CombatUnitType | bool |  |
| MilitaryFormation | IsCurrentHQ | Unknown | bool |  |
| MilitaryFormation | IsCurrentSeaNode | Unknown | bool |  |
| MilitaryFormation | IsDefendingInBattle |  | bool |  |
| MilitaryFormation | IsDemobilizing |  | bool |  |
| MilitaryFormation | IsExiled |  | bool |  |
| MilitaryFormation | IsFleet |  | bool |  |
| MilitaryFormation | IsFullyDefeated |  | bool |  |
| MilitaryFormation | IsFullyMobilized |  | bool |  |
| MilitaryFormation | IsInBattle |  | bool |  |
| MilitaryFormation | IsMobilized |  | bool |  |
| MilitaryFormation | IsMobilizing |  | bool |  |
| MilitaryFormation | IsPinnedInOutliner |  | bool |  |
| MilitaryFormation | IsReadyToDefendNavalInvasion |  | bool |  |
| MilitaryFormation | IsRegularUnitTypeUpgrading | CombatUnitType | bool |  |
| MilitaryFormation | IsSelected |  | bool |  |
| MilitaryFormation | IsTargetHQ | Unknown | bool |  |
| MilitaryFormation | IsTargetSeaNode | Unknown | bool |  |
| MilitaryFormation | IsTraveling |  | bool |  |
| MilitaryFormation | IsValid |  | bool |  |
| MilitaryFormation | IsZoomingToMapMarkerPosition |  | bool |  |
| MilitaryFormation | MakeScope |  | Scope |  |
| MilitaryFormation | Mobilize |  | Command |  |
| MilitaryFormation | OnClickRecruitCombatUnit | CombatUnitType | void |  |
| MilitaryFormation | OnClickRecruitConscript | CombatUnitType | void |  |
| MilitaryFormation | OnDeployToFrontClicked |  | void |  |
| MilitaryFormation | OnDeployToSeaNodeClicked |  | void |  |
| MilitaryFormation | OnInvasionClicked |  | void |  |
| MilitaryFormation | OnRehomeClicked |  | void |  |
| MilitaryFormation | OnSetStrategicObjectiveClicked |  | void |  |
| MilitaryFormation | OnStationClicked |  | void |  |
| MilitaryFormation | RaiseConscripts |  | Command |  |
| MilitaryFormation | Select |  | void |  |
| MilitaryFormation | Self |  | MilitaryFormation |  |
| MilitaryFormation | TogglePinInOutliner |  | void |  |
| MilitaryFormation | ToggleSelected |  | void |  |
| MilitaryFormation | ZoomToMapMarkerPosition |  | void |  |
| MilitaryFormationBorrowSetting | AccessSelf |  | MilitaryFormationBorrowSetting | 类别：const |
| MilitaryFormationBorrowSetting | GetBorrowingCommand |  | Command | 类别：nonconst |
| MilitaryFormationBorrowSetting | GetDesc |  | CString | 类别：nonconst |
| MilitaryFormationBorrowSetting | GetName |  | CString | 类别：nonconst |
| MilitaryFormationBorrowSetting | IsSelected |  | bool |  |
| MilitaryFormationBorrowSetting | OnClicked |  | void |  |
| MilitaryFormationBorrowSetting | Self |  | MilitaryFormationBorrowSetting |  |
| MilitaryFormationChangeNamePopup | AccessSelf |  | MilitaryFormationChangeNamePopup | 类别：const |
| MilitaryFormationChangeNamePopup | Confirm |  | Command |  |
| MilitaryFormationChangeNamePopup | GetArmyFormationColors |  | Unknown | 类别：nonconst |
| MilitaryFormationChangeNamePopup | GetArmyFormationFlags |  | Unknown | 类别：nonconst |
| MilitaryFormationChangeNamePopup | GetCurrentUnitName |  | CString | 类别：nonconst |
| MilitaryFormationChangeNamePopup | GetFleetFormationColors |  | Unknown | 类别：nonconst |
| MilitaryFormationChangeNamePopup | GetFleetFormationFlags |  | Unknown | 类别：nonconst |
| MilitaryFormationChangeNamePopup | GetFormation |  | MilitaryFormation | 类别：nonconst |
| MilitaryFormationChangeNamePopup | GetSelectedColor |  | CVector4f | 类别：nonconst |
| MilitaryFormationChangeNamePopup | IsColorSelected | Unknown | bool |  |
| MilitaryFormationChangeNamePopup | IsFlagSelected | Unknown | bool |  |
| MilitaryFormationChangeNamePopup | IsNameUnitsAfterCultureSelected |  | bool |  |
| MilitaryFormationChangeNamePopup | IsNameUnitsAfterStateSelected |  | bool |  |
| MilitaryFormationChangeNamePopup | OnEditName |  | void |  |
| MilitaryFormationChangeNamePopup | OnSelectColor | 未知 | void |  |
| MilitaryFormationChangeNamePopup | OnSelectFlag | 未知 | void |  |
| MilitaryFormationChangeNamePopup | SelectNameUnitsAfterCulture |  | void |  |
| MilitaryFormationChangeNamePopup | SelectNameUnitsAfterState |  | void |  |
| MilitaryFormationChangeNamePopup | Self |  | MilitaryFormationChangeNamePopup |  |
| MilitaryFormationColor | AccessSelf |  | MilitaryFormationColor | 类别：const |
| MilitaryFormationColor | GetColor |  | CVector4f | 类别：nonconst |
| MilitaryFormationColor | Self |  | MilitaryFormationColor |  |
| MilitaryFormationFlag | AccessSelf |  | MilitaryFormationFlag | 类别：const |
| MilitaryFormationFlag | GetIcon |  | 未知 | 类别：nonconst |
| MilitaryFormationFlag | GetKey |  | CString | 类别：nonconst |
| MilitaryFormationFlag | GetName |  | CString | 类别：nonconst |
| MilitaryFormationFlag | GetTooltipTag |  | CString | 类别：nonconst |
| MilitaryFormationFlag | Self |  | MilitaryFormationFlag |  |
| MilitaryFormationUnitEntry | AccessSelf |  | MilitaryFormationUnitEntry | 类别：const |
| MilitaryFormationUnitEntry | GetCombatUnits |  | 未知 | 类别：nonconst |
| MilitaryFormationUnitEntry | GetCurrentNumConscriptUnits |  | int32 | 类别：nonconst |
| MilitaryFormationUnitEntry | GetCurrentNumRegularUnits |  | int32 | 类别：nonconst |
| MilitaryFormationUnitEntry | GetCurrentNumTotalUnits |  | int32 | 类别：nonconst |
| MilitaryFormationUnitEntry | GetExpectedNumConscriptUnits |  | int32 | 类别：nonconst |
| MilitaryFormationUnitEntry | GetExpectedNumRegularUnits |  | int32 | 类别：nonconst |
| MilitaryFormationUnitEntry | GetExpectedNumTotalUnits |  | int32 | 类别：nonconst |
| MilitaryFormationUnitEntry | GetIDString |  | CString | 类别：nonconst |
| MilitaryFormationUnitEntry | GetMobilization |  | CFixedPoint | 类别：nonconst |
| MilitaryFormationUnitEntry | GetRegularUnitsAndRaisedConscripts |  | 未知 | 类别：nonconst |
| MilitaryFormationUnitEntry | GetUnitType |  | CombatUnitType | 类别：nonconst |
| MilitaryFormationUnitEntry | IsForGroup | CombatUnitGroup | bool |  |
| MilitaryFormationUnitEntry | IsFullyMobilized |  | bool |  |
| MilitaryFormationUnitEntry | IsMobilizing |  | bool |  |
| MilitaryFormationUnitEntry | Self |  | MilitaryFormationUnitEntry |  |
| MilitaryPanelBuildingEntry | AccessSelf |  | MilitaryPanelBuildingEntry | 类别：const |
| MilitaryPanelBuildingEntry | GetBuilding |  | Building | 类别：nonconst |
| MilitaryPanelBuildingEntry | IsExpanded |  | bool |  |
| MilitaryPanelBuildingEntry | Self |  | MilitaryPanelBuildingEntry |  |
| MilitaryPanelBuildingEntry | ToggleExpand |  | void |  |
| MixBrushMode | AccessSelf |  | MixBrushMode | 类别：const |
| MixBrushMode | IsSelected |  | bool |  |
| MixBrushMode | Self |  | MixBrushMode |  |
| MobilizationOption | AccessSelf |  | MobilizationOption | 类别：const |
| MobilizationOption | CanBeTurnedOff | 未知 | bool |  |
| MobilizationOption | GetCustom | CustomLocalization | CString | 类别：nonconst |
| MobilizationOption | GetDesc |  | CString | 类别：nonconst |
| MobilizationOption | GetName |  | CString | 类别：nonconst |
| MobilizationOption | GetNameNoFormatting |  | CString | 类别：nonconst |
| MobilizationOption | GetNumActiveForSelected |  | int32 | 类别：nonconst |
| MobilizationOption | GetNumBlockedForSelected |  | int32 | 类别：nonconst |
| MobilizationOption | GetNumCouldBeActivatedForSelected |  | int32 | 类别：nonconst |
| MobilizationOption | GetTexture |  | 未知 | 类别：nonconst |
| MobilizationOption | GetTooltip |  | CString | 类别：nonconst |
| MobilizationOption | GetTooltipTag |  | CString | 类别：nonconst |
| MobilizationOption | GetTooltipWithActivateDesc | MilitaryFormation | CString | 类别：nonconst |
| MobilizationOption | GetTooltipWithActivateDescForSelected |  | CString | 类别：nonconst |
| MobilizationOption | GetTooltipWithDeactivateDesc | MilitaryFormation | CString | 类别：nonconst |
| MobilizationOption | GetTooltipWithDeactivateDescForSelected |  | CString | 类别：nonconst |
| MobilizationOption | GetTooltipWithToggleDesc | 未知 | CString | 类别：nonconst |
| MobilizationOption | GetUnitModifier |  | Modifier | 类别：nonconst |
| MobilizationOption | GetUpkeepModifier |  | Modifier | 类别：nonconst |
| MobilizationOption | GetUpkeepUnscaledModifier |  | Modifier | 类别：nonconst |
| MobilizationOption | IsActivated | MilitaryFormation | bool |  |
| MobilizationOption | IsActivatedForSelected |  | bool |  |
| MobilizationOption | IsActiveForSomeButNotAllSelected |  | bool |  |
| MobilizationOption | IsBlockedForSomeSelected |  | bool |  |
| MobilizationOption | IsDeactivatedForSelected |  | bool |  |
| MobilizationOption | IsMixedActivationForSelected |  | bool |  |
| MobilizationOption | IsPossible | 未知 | bool |  |
| MobilizationOption | IsShown | 未知 | bool |  |
| MobilizationOption | MakeScope |  | Scope |  |
| MobilizationOption | Self |  | MobilizationOption |  |
| MobilizationOption | Toggle | MilitaryFormation | Command |  |
| MobilizationOption | ToggleForSelected |  | Command |  |
| MobilizationOptionGroup | AccessSelf |  | MobilizationOptionGroup | 类别：const |
| MobilizationOptionGroup | GetDesc |  | CString | 类别：nonconst |
| MobilizationOptionGroup | GetIcon |  | 未知 | 类别：nonconst |
| MobilizationOptionGroup | GetKey |  | CString | 类别：nonconst |
| MobilizationOptionGroup | GetMobilizationOptions |  | 未知 | 类别：nonconst |
| MobilizationOptionGroup | GetName |  | CString | 类别：nonconst |
| MobilizationOptionGroup | GetNameNoFormatting |  | CString | 类别：nonconst |
| MobilizationOptionGroup | GetTooltip |  | CString | 类别：nonconst |
| MobilizationOptionGroup | GetTooltipTag |  | CString | 类别：nonconst |
| MobilizationOptionGroup | GetUpkeepGoodsDescShort | MilitaryFormation | CString | 类别：nonconst |
| MobilizationOptionGroup | Self |  | MobilizationOptionGroup |  |
| Modifier | AccessSelf |  | Modifier | 类别：const |
| Modifier | GetBreakdownFor | 未知 | ModifierBreakdown | 类别：nonconst |
| Modifier | GetDesc |  | CString | 类别：nonconst |
| Modifier | GetDescFor | CString | CString | 类别：nonconst |
| Modifier | GetDescNoGoods |  | CString | 类别：nonconst |
| Modifier | GetEntries |  | 未知 | 类别：nonconst |
| Modifier | GetFormattedValueFor | 未知 | CString | 类别：nonconst |
| Modifier | GetFullEntryDescFor | 未知 | CString | 类别：nonconst |
| Modifier | GetInvertedValueFor | 未知 | CFixedPoint | 类别：nonconst |
| Modifier | GetName |  | CString | 类别：nonconst |
| Modifier | GetNonFormattedValueWithBreakdownAndNoDecimalsFor | 未知 | CString | 类别：nonconst |
| Modifier | GetNonFormattedValueWithBreakdownFor | 未知 | CString | 类别：nonconst |
| Modifier | GetTooltipFor | 未知 | CString | 类别：nonconst |
| Modifier | GetTooltipTag |  | CString | 类别：nonconst |
| Modifier | GetValueFor | 未知 | CFixedPoint | 类别：nonconst |
| Modifier | GetValueWithBreakdownFor | 未知 | CString | 类别：nonconst |
| Modifier | IsEmpty |  | bool |  |
| Modifier | Self |  | Modifier |  |
| ModifierBreakdown | AccessSelf |  | ModifierBreakdown | 类别：const |
| ModifierBreakdown | GetBreakdown |  | CString | 类别：nonconst |
| ModifierBreakdown | GetFormattedMultipliedValue |  | CString | 类别：nonconst |
| ModifierBreakdown | GetFormattedRawValue |  | CString | 类别：nonconst |
| ModifierBreakdown | GetModifier |  | Modifier | 类别：nonconst |
| ModifierBreakdown | GetMultipliedValue |  | CFixedPoint | 类别：nonconst |
| ModifierBreakdown | GetName |  | CString | 类别：nonconst |
| ModifierBreakdown | GetRawValue |  | CFixedPoint | 类别：nonconst |
| ModifierBreakdown | GetSourceMultiplier |  | CFixedPoint | 类别：nonconst |
| ModifierBreakdown | GetTooltipTag |  | CString | 类别：nonconst |
| ModifierBreakdown | GetTypeDescription |  | CString | 类别：nonconst |
| ModifierBreakdown | GetTypeName |  | CString | 类别：nonconst |
| ModifierBreakdown | Self |  | ModifierBreakdown |  |
| ModifierEntry | AccessSelf |  | ModifierEntry | 类别：const |
| ModifierEntry | GetBreakdown |  | CString | 类别：nonconst |
| ModifierEntry | GetDesc |  | CString | 类别：nonconst |
| ModifierEntry | GetFormattedValue |  | CString | 类别：nonconst |
| ModifierEntry | GetName |  | CString | 类别：nonconst |
| ModifierEntry | GetTooltip |  | CString | 类别：nonconst |
| ModifierEntry | GetValue |  | CFixedPoint | 类别：nonconst |
| ModifierEntry | GetValueWithBreakdown |  | CString | 类别：nonconst |
| ModifierEntry | Self |  | ModifierEntry |  |
| ModifierNodeData | AccessSelf |  | ModifierNodeData | 类别：const |
| ModifierNodeData | GetName |  | CString | 类别：nonconst |
| ModifierNodeData | GetTotalCount |  | int32 | 类别：nonconst |
| ModifierNodeData | GetUpdatedCount |  | int32 | 类别：nonconst |
| ModifierNodeData | GetUpdatedTrend |  | DataTrend | 类别：nonconst |
| ModifierNodeData | OpenDetails |  | void |  |
| ModifierNodeData | Self |  | ModifierNodeData |  |
| ModifierNodeDebuggerView | AccessSelf |  | ModifierNodeDebuggerView | 类别：const |
| ModifierNodeDebuggerView | GetGraphItems |  | 未知 | 类别：nonconst |
| ModifierNodeDebuggerView | GetGraphLines |  | 未知 | 类别：nonconst |
| ModifierNodeDebuggerView | Self |  | ModifierNodeDebuggerView |  |
| ModifierNodeDetailsView | AccessSelf |  | ModifierNodeDetailsView | 类别：const |
| ModifierNodeDetailsView | GetModifierNodeData |  | ModifierNodeData | 类别：nonconst |
| ModifierNodeDetailsView | Self |  | ModifierNodeDetailsView |  |
| ModifierNodeGraphItem | AccessSelf |  | ModifierNodeGraphItem | 类别：const |
| ModifierNodeGraphItem | GetKey |  | CString | 类别：nonconst |
| ModifierNodeGraphItem | GetModifierNodeData |  | ModifierNodeData | 类别：nonconst |
| ModifierNodeGraphItem | GetPosition |  | CVector2f | 类别：nonconst |
| ModifierNodeGraphItem | GetTooltip |  | CString | 类别：nonconst |
| ModifierNodeGraphItem | Self |  | ModifierNodeGraphItem |  |
| ModifierNodeGraphLine | AccessSelf |  | ModifierNodeGraphLine | 类别：const |
| ModifierNodeGraphLine | GetFrom |  | CVector2f | 类别：nonconst |
| ModifierNodeGraphLine | GetLineFrom |  | CVector2f | 类别：nonconst |
| ModifierNodeGraphLine | GetLineTo |  | CVector2f | 类别：nonconst |
| ModifierNodeGraphLine | GetPoints |  | 未知 | 类别：nonconst |
| ModifierNodeGraphLine | GetPointsInContainer |  | 未知 | 类别：nonconst |
| ModifierNodeGraphLine | GetPosition |  | CVector2f | 类别：nonconst |
| ModifierNodeGraphLine | GetSize |  | CVector2f | 类别：nonconst |
| ModifierNodeGraphLine | GetTo |  | CVector2f | 类别：nonconst |
| ModifierNodeGraphLine | IsFromNodeVirtual |  | bool |  |
| ModifierNodeGraphLine | IsToNodeVirtual |  | bool |  |
| ModifierNodeGraphLine | Self |  | ModifierNodeGraphLine |  |
| ModifierNodeListView | AccessSelf |  | ModifierNodeListView | 类别：const |
| ModifierNodeListView | GetModifierNodes |  | 未知 | 类别：nonconst |
| ModifierNodeListView | Self |  | ModifierNodeListView |  |
| ModifierNodeListView | Sort | CString | void |  |
| ModifiersPanel | AccessSelf |  | ModifiersPanel | 类别：const |
| ModifiersPanel | GetModifier |  | Modifier | 类别：nonconst |
| ModifiersPanel | GetTimedModifiers |  | 未知 | 类别：nonconst |
| ModifiersPanel | Self |  | ModifiersPanel |  |
| MoveTool | AccessSelf |  | MoveTool | 类别：const |
| MoveTool | Self |  | MoveTool |  |
| MultiplayerSetupWindow | AccessSelf |  | MultiplayerSetupWindow | 类别：const |
| MultiplayerSetupWindow | CanHost |  | bool |  |
| MultiplayerSetupWindow | Cancel |  | void |  |
| MultiplayerSetupWindow | GetDefaultServerName |  | CUTF8String | 类别：nonconst |
| MultiplayerSetupWindow | GetDefaultServerPassword |  | CUTF8String | 类别：nonconst |
| MultiplayerSetupWindow | Host |  | void |  |
| MultiplayerSetupWindow | HostToolTip |  | CString |  |
| MultiplayerSetupWindow | Self |  | MultiplayerSetupWindow |  |
| MultiplayerSetupWindow | ShouldShowMPConfig |  | bool |  |
| MultiplayerSynchronizationInfo | AccessSelf |  | MultiplayerSynchronizationInfo | 类别：const |
| MultiplayerSynchronizationInfo | GetPlayerDatesString |  | CString | 类别：nonconst |
| MultiplayerSynchronizationInfo | Self |  | MultiplayerSynchronizationInfo |  |
| MusicPlayer | AccessCategories |  | 未知 | 类别：const |
| MusicPlayer | AccessSelf |  | MusicPlayer | 类别：const |
| MusicPlayer | AccessTracksFromSelectedCategory |  | 未知 | 类别：const |
| MusicPlayer | GetCategoryEnabledText | MusicPlayerCategory | CString | 类别：nonconst |
| MusicPlayer | GetCategoryName | MusicPlayerCategory | CString | 类别：nonconst |
| MusicPlayer | GetCategoryNameLocKey | 未知 | CString | 类别：nonconst |
| MusicPlayer | GetMusicDensity |  | float | 类别：nonconst |
| MusicPlayer | GetMusicDensityString |  | CString | 类别：nonconst |
| MusicPlayer | GetPlaybackStatusFrameIndex |  | int32 | 类别：nonconst |
| MusicPlayer | GetPlayingTrackElapsedTime |  | CString | 类别：nonconst |
| MusicPlayer | GetPlayingTrackName |  | CString | 类别：nonconst |
| MusicPlayer | GetSelectedCategory |  | 未知 | 类别：nonconst |
| MusicPlayer | GetTrackEnabledText | 未知 | CString | 类别：nonconst |
| MusicPlayer | GetTrackName | 未知 | CString | 类别：nonconst |
| MusicPlayer | GetTrackTextColor | MusicTrack | CVector4f | 类别：nonconst |
| MusicPlayer | GetVolume |  | float | 类别：nonconst |
| MusicPlayer | GetVolumeString |  | CString | 类别：nonconst |
| MusicPlayer | HasSelectedCategory |  | bool |  |
| MusicPlayer | IsPlaying |  | bool |  |
| MusicPlayer | IsSelectedCategory | MusicPlayerCategory | bool |  |
| MusicPlayer | OnNextTrack |  | void |  |
| MusicPlayer | OnSelectAndPlayTrack | MusicTrack | void |  |
| MusicPlayer | OnSelectCategory | MusicPlayerCategory | void |  |
| MusicPlayer | OnSelectTrack | 未知 | void |  |
| MusicPlayer | OnToggleCategoryEnabled | MusicPlayerCategory | void |  |
| MusicPlayer | OnTogglePlayPause |  | void |  |
| MusicPlayer | OnToggleTrackEnabled | MusicTrack | void |  |
| MusicPlayer | Self |  | MusicPlayer |  |
| MusicPlayer | SetMusicDensity |  | void |  |
| MusicPlayer | SetVolume |  | void |  |
| MusicPlayerCategory | AccessSelf |  | MusicPlayerCategory | 类别：const |
| MusicPlayerCategory | GetName |  | CString | 类别：nonconst |
| MusicPlayerCategory | GetNameLocKey |  | CString | 类别：nonconst |
| MusicPlayerCategory | GetTexture |  | 未知 | 类别：nonconst |
| MusicPlayerCategory | GetTracks |  | 未知 | 类别：nonconst |
| MusicPlayerCategory | HasTexture |  | bool |  |
| MusicPlayerCategory | IsEnabled |  | bool |  |
| MusicPlayerCategory | IsPlaying |  | bool |  |
| MusicPlayerCategory | Self |  | MusicPlayerCategory |  |
| MusicTrack | AccessSelf |  | MusicTrack | 类别：const |
| MusicTrack | GetCategory |  | 未知 | 类别：nonconst |
| MusicTrack | GetName |  | CString | 类别：nonconst |
| MusicTrack | IsEnabled |  | bool |  |
| MusicTrack | IsPlaying |  | bool |  |
| MusicTrack | Self |  | MusicTrack |  |
| NationalAwakeningMarker | AccessSelf |  | NationalAwakeningMarker | 类别：const |
| NationalAwakeningMarker | GetPosition |  | CVector2f | 类别：nonconst |
| NationalAwakeningMarker | Self |  | NationalAwakeningMarker |  |
| NationalizeBuildingGroup | AccessSelf |  | NationalizeBuildingGroup | 类别：const |
| NationalizeBuildingGroup | GetColor |  | CVector4f | 类别：nonconst |
| NationalizeBuildingGroup | GetErrors |  | CString | 类别：nonconst |
| NationalizeBuildingGroup | GetFilterMaxLevels | CString | int32 | 类别：nonconst |
| NationalizeBuildingGroup | GetFilterNumSelectedLevels | CString | int32 | 类别：nonconst |
| NationalizeBuildingGroup | GetInvestor |  | Country | 类别：nonconst |
| NationalizeBuildingGroup | GetMaxLevels |  | int32 | 类别：nonconst |
| NationalizeBuildingGroup | GetName |  | CString | 类别：nonconst |
| NationalizeBuildingGroup | GetNumSelectedLevels |  | int32 | 类别：nonconst |
| NationalizeBuildingGroup | GetSelectedLevelsDesc |  | CString | 类别：nonconst |
| NationalizeBuildingGroup | HasFilter | 未知 | bool |  |
| NationalizeBuildingGroup | IsGovernment |  | bool |  |
| NationalizeBuildingGroup | IsNationalizable |  | bool |  |
| NationalizeBuildingGroup | IsPrivate |  | bool |  |
| NationalizeBuildingGroup | OnSelectedLevelsEditboxValueChanged |  | void |  |
| NationalizeBuildingGroup | OnSelectedLevelsSliderValueChanged |  | void |  |
| NationalizeBuildingGroup | Self |  | NationalizeBuildingGroup |  |
| NationalizeBuildingGroup | SetFilter | 未知 | void |  |
| NationalizeBuildingTypeGroup | AccessSelf |  | NationalizeBuildingTypeGroup | 类别：const |
| NationalizeBuildingTypeGroup | GetBuildingType |  | BuildingType | 类别：nonconst |
| NationalizeBuildingTypeGroup | GetCurrentLevels |  | int32 | 类别：nonconst |
| NationalizeBuildingTypeGroup | GetMaxLevels |  | int32 | 类别：nonconst |
| NationalizeBuildingTypeGroup | GetSelectedBuildingsBreakdown |  | CString | 类别：nonconst |
| NationalizeBuildingTypeGroup | Self |  | NationalizeBuildingTypeGroup |  |
| NationalizeBuildingWindow | AccessSelf |  | NationalizeBuildingWindow | 类别：const |
| NationalizeBuildingWindow | CanToggleCompensation |  | bool |  |
| NationalizeBuildingWindow | GetBuildingGroups |  | 未知 | 类别：nonconst |
| NationalizeBuildingWindow | GetBuildingTypeGroups |  | 未知 | 类别：nonconst |
| NationalizeBuildingWindow | GetBuildings |  | 未知 | 类别：nonconst |
| NationalizeBuildingWindow | GetCanToggleCompensationTooltip |  | CString | 类别：nonconst |
| NationalizeBuildingWindow | GetCompensationBreakdown |  | CString | 类别：nonconst |
| NationalizeBuildingWindow | GetCompensationShareToInvestmentPool |  | CFixedPoint | 类别：nonconst |
| NationalizeBuildingWindow | GetCompensationShareToPlayerInvestmentPool |  | CFixedPoint | 类别：nonconst |
| NationalizeBuildingWindow | GetCompensationTotal |  | CFixedPoint | 类别：nonconst |
| NationalizeBuildingWindow | GetDamagedRelationsListDesc |  | CString | 类别：nonconst |
| NationalizeBuildingWindow | GetNumLevelsToNationalize |  | int32 | 类别：nonconst |
| NationalizeBuildingWindow | GetPopRadicalizationListDesc |  | CString | 类别：nonconst |
| NationalizeBuildingWindow | HasNationalizableGroup |  | bool |  |
| NationalizeBuildingWindow | IsNationalizingAll |  | bool |  |
| NationalizeBuildingWindow | NationalizeBuildingGroupsConfirm |  | void |  |
| NationalizeBuildingWindow | NationalizeBuildingGroupsGetDesc |  | CString |  |
| NationalizeBuildingWindow | NationalizeBuildingGroupsIsValid |  | bool |  |
| NationalizeBuildingWindow | Self |  | NationalizeBuildingWindow |  |
| NationalizeBuildingWindow | SetNationalizeToAll |  | void |  |
| NationalizeBuildingWindow | SetNationalizeToNone |  | void |  |
| NationalizeBuildingWindow | Sort | 未知 | void |  |
| NationalizeBuildingWindow | ToggleGiveCompensation |  | void |  |
| NationalizeBuildingWindow | WillGiveCompensation |  | bool |  |
| Node | AccessSelf |  | Node | 类别：const |
| Node | ContextColor |  | CVector4f |  |
| Node | Description |  | CString |  |
| Node | ErrorColor |  | CVector4f |  |
| Node | ErrorTooltip |  | CString |  |
| Node | GetBackgroundColor |  | CVector4f | 类别：nonconst |
| Node | GetId |  | int32 | 类别：nonconst |
| Node | GetSelectedColor |  | CVector4f | 类别：nonconst |
| Node | HasDescription |  | bool |  |
| Node | HasError |  | bool |  |
| Node | IsSelected |  | bool |  |
| Node | Name |  | CString |  |
| Node | Self |  | Node |  |
| Node | TextColor |  | CVector4f |  |
| Node | Texture |  | 未知 |  |
| Node | Tooltip |  | CString |  |
| NodeEditorSearch | AccessSelf |  | NodeEditorSearch | 类别：const |
| NodeEditorSearch | ClearSearchText |  | void |  |
| NodeEditorSearch | CurrentResultIndex |  | int32 |  |
| NodeEditorSearch | GetSearchText |  | CUTF8String | 类别：nonconst |
| NodeEditorSearch | GoToNextResult |  | void |  |
| NodeEditorSearch | GoToPreviousResult |  | void |  |
| NodeEditorSearch | HasOccurrences |  | bool |  |
| NodeEditorSearch | Hide |  | void |  |
| NodeEditorSearch | IsVisible |  | bool |  |
| NodeEditorSearch | NumOccurrences |  | int32 |  |
| NodeEditorSearch | Search |  | void |  |
| NodeEditorSearch | Self |  | NodeEditorSearch |  |
| NodeError | AccessSelf |  | NodeError | 类别：const |
| NodeError | GoTo |  | void |  |
| NodeError | Message |  | CString |  |
| NodeError | Node |  | int32 |  |
| NodeError | Self |  | NodeError |  |
| NodeLine | AccessSelf |  | NodeLine | 类别：const |
| NodeLine | Color |  | CVector4f |  |
| NodeLine | From |  | CVector2f |  |
| NodeLine | GetAnimationSpeed |  | CVector2f | 类别：nonconst |
| NodeLine | GetOwnerNodeId |  | int32 | 类别：nonconst |
| NodeLine | Highlighted |  | bool |  |
| NodeLine | IsDisabled |  | bool |  |
| NodeLine | Self |  | NodeLine |  |
| NodeLine | SetHighlightedDirectly | bool | void |  |
| NodeLine | SetSelected | bool | void |  |
| NodeLine | To |  | CVector2f |  |
| NodeLine | Tooltip |  | 未知 |  |
| NodeLine | Width |  | float |  |
| NodePin | AccessSelf |  | NodePin | 类别：const |
| NodePin | Color |  | CVector4f |  |
| NodePin | DrawAsConnected |  | bool |  |
| NodePin | Highlight |  | bool |  |
| NodePin | IsInlinedNodeConnected |  | bool |  |
| NodePin | IsNodePinDisplayNameEmpty |  | bool |  |
| NodePin | Name |  | CString |  |
| NodePin | Self |  | NodePin |  |
| NodePin | Tooltip |  | CString |  |
| NodePin | TypeColor |  | CVector4f |  |
| NodeWindow | AccessSelf |  | NodeWindow | 类别：const |
| NodeWindow | Close |  | void |  |
| NodeWindow | DescriptionDialog |  | void |  |
| NodeWindow | NameDialog |  | void |  |
| NodeWindow | Self |  | NodeWindow |  |
| NodeWindow | SetDescription |  | void |  |
| NonRegisteredDockable | AccessSelf |  | NonRegisteredDockable | 类别：const |
| NonRegisteredDockable | GetID |  | CString | 类别：nonconst |
| NonRegisteredDockable | Self |  | NonRegisteredDockable |  |
| NotificationDummyContext | AccessSelf |  | NotificationDummyContext | 类别：const |
| NotificationDummyContext | Self |  | NotificationDummyContext |  |
| NotificationOptionItem | AccessSelf |  | NotificationOptionItem | 类别：const |
| NotificationOptionItem | GetName |  | CString | 类别：nonconst |
| NotificationOptionItem | GetNameWithConcept |  | CString | 类别：nonconst |
| NotificationOptionItem | IsDefault |  | bool |  |
| NotificationOptionItem | Self |  | NotificationOptionItem |  |
| NotificationSettingsItem | AccessSelf |  | NotificationSettingsItem | 类别：const |
| NotificationSettingsItem | GetCurrentOption |  | NotificationOptionItem | 类别：nonconst |
| NotificationSettingsItem | GetName |  | CString | 类别：nonconst |
| NotificationSettingsItem | GetTag |  | CString | 类别：nonconst |
| NotificationSettingsItem | GetValidOptions |  | 未知 | 类别：nonconst |
| NotificationSettingsItem | HasAutoPause |  | bool |  |
| NotificationSettingsItem | OnSelectOption |  | void |  |
| NotificationSettingsItem | Self |  | NotificationSettingsItem |  |
| NotificationSettingsItem | ToggleAutoPause |  | void |  |
| Nudger | AccessSelf |  | Nudger | 类别：const |
| Nudger | CreateNewBlankMapObjectType |  | void |  |
| Nudger | DeleteSelected |  | void |  |
| Nudger | Deselect |  | void |  |
| Nudger | FocusCameraOnSelection |  | void |  |
| Nudger | IsAnyMapObjectExpanded |  | bool |  |
| Nudger | IsAnyMapObjectHidden |  | bool |  |
| Nudger | IsAnyMapObjectLocked |  | bool |  |
| Nudger | IsAnyObjectEntrySelected |  | bool |  |
| Nudger | IsAnyObjectSelected |  | bool |  |
| Nudger | IsAnySelectedMapObjectDynamicType |  | bool |  |
| Nudger | IsMultiSpawnEnabled |  | bool |  |
| Nudger | OnMapObjectSelected | Unknown | void |  |
| Nudger | SelectAll |  | void |  |
| Nudger | Self |  | Nudger |  |
| Nudger | SetAllMapObjectsExpanded | bool | void |  |
| Nudger | SetAllMapObjectsHidden | bool | void |  |
| Nudger | SetAllMapObjectsLocked | bool | void |  |
| Nudger | SetMapObjectHidden | Unknown Unknown | void |  |
| Nudger | SetMapObjectLocked | Unknown Unknown | void |  |
| Nudger | SetMapObjectLockedExclusive | Unknown Unknown | void |  |
| Nudger | SetMultiSpawnEnabled | bool | void |  |
| Nudger | ToggleInstancesClampToWaterLevel |  | void |  |
| Nudger | ToggleInstancesRenderUnderwater |  | void |  |
| NudgerLayerEntryMapObjectDesc | AccessSelf |  | NudgerLayerEntryMapObjectDesc | 类别：const |
| NudgerLayerEntryMapObjectDesc | GetName |  | CString | 类别：nonconst |
| NudgerLayerEntryMapObjectDesc | IsAutoNudgingError |  | bool |  |
| NudgerLayerEntryMapObjectDesc | IsLocked |  | bool |  |
| NudgerLayerEntryMapObjectDesc | IsSelected |  | bool |  |
| NudgerLayerEntryMapObjectDesc | Select |  | void |  |
| NudgerLayerEntryMapObjectDesc | Self |  | NudgerLayerEntryMapObjectDesc |  |
| NudgerLayerEntryMapObjectDesc | SetLocked | bool | void |  |
| NudgerMapContentGui | AccessSelf |  | NudgerMapContentGui | 类别：const |
| NudgerMapContentGui | AutoNudgeSelection |  | void |  |
| NudgerMapContentGui | GetAutoNudgingReadyProgress |  | float | 类别：nonconst |
| NudgerMapContentGui | IsAutoNudgePreviewEnabled |  | bool |  |
| NudgerMapContentGui | IsAutoNudgingReady |  | bool |  |
| NudgerMapContentGui | IsAutoNudgingSettingsOpen |  | bool |  |
| NudgerMapContentGui | IsAutoNudgingSupported |  | bool |  |
| NudgerMapContentGui | Self |  | NudgerMapContentGui |  |
| NudgerMapContentGui | SetAutoNudgePreviewEnabled | Unknown | void |  |
| NudgerMapContentGui | SetAutoNudgingSettingsOpen | Unknown | void |  |
| NudgerMapObjectPropertyListDockable | AccessSelf |  | NudgerMapObjectPropertyListDockable | 类别：const |
| NudgerMapObjectPropertyListDockable | Delete |  | void |  |
| NudgerMapObjectPropertyListDockable | HasEntry |  | bool |  |
| NudgerMapObjectPropertyListDockable | IsGenerate |  | bool |  |
| NudgerMapObjectPropertyListDockable | Self |  | NudgerMapObjectPropertyListDockable |  |
| NudgerMode | AccessSelf |  | NudgerMode | 类别：const |
| NudgerMode | IsSelected |  | bool |  |
| NudgerMode | Self |  | NudgerMode |  |
| ObjectBrowser | AccessSelf |  | ObjectBrowser | 类别：const |
| ObjectBrowser | CopyAsCSV |  | void |  |
| ObjectBrowser | CreateNewPreset |  | void |  |
| ObjectBrowser | DeleteSelectedPreset |  | void |  |
| ObjectBrowser | ForceUpdate |  | void |  |
| ObjectBrowser | GetFilterString |  | CUTF8String | 类别：nonconst |
| ObjectBrowser | GetNumObjectsFiltered |  | int32 | 类别：nonconst |
| ObjectBrowser | GetNumObjectsTotal |  | int32 | 类别：nonconst |
| ObjectBrowser | GetPresets |  | Unknown | 类别：nonconst |
| ObjectBrowser | GetProviders |  | Unknown | 类别：nonconst |
| ObjectBrowser | GetSelectedProvider |  | CVector2i | 类别：nonconst |
| ObjectBrowser | GetSelectedView |  | CVector2i | 类别：nonconst |
| ObjectBrowser | GetViews |  | Unknown | 类别：nonconst |
| ObjectBrowser | HasConfig |  | bool |  |
| ObjectBrowser | IsObjectSelected | int32 | bool |  |
| ObjectBrowser | IsOutputFlattened |  | bool |  |
| ObjectBrowser | IsWaitingForProvider |  | bool |  |
| ObjectBrowser | RenameSelectedPreset |  | void |  |
| ObjectBrowser | RequestUpdate |  | void |  |
| ObjectBrowser | SaveCurrentChanges |  | void |  |
| ObjectBrowser | SaveDefaults |  | void |  |
| ObjectBrowser | SelectProvider |  | void |  |
| ObjectBrowser | SelectView |  | void |  |
| ObjectBrowser | Self |  | ObjectBrowser |  |
| ObjectBrowser | SetFilterString |  | void |  |
| ObjectBrowser | SetObjectSelected | Unknown | void |  |
| ObjectBrowser | SetSelectedPreset | ObjectPreset | void |  |
| ObjectBrowser | ToggleObjectSelected | int32 | void |  |
| ObjectBrowser | ToggleOutputFlattened |  | void |  |
| ObjectBrowserView | AccessSelf |  | ObjectBrowserView | 类别：const |
| ObjectBrowserView | Name |  | CUTF8String |  |
| ObjectBrowserView | Self |  | ObjectBrowserView |  |
| ObjectInspector | AccessPluginEntries |  | Unknown | 类别：const |
| ObjectInspector | AccessSelf |  | ObjectInspector | 类别：const |
| ObjectInspector | GetObjectName |  | CUTF8String | 类别：nonconst |
| ObjectInspector | GetTypeName |  | CUTF8String | 类别：nonconst |
| ObjectInspector | Self |  | ObjectInspector |  |
| ObjectInspectorDockable | AccessSelf |  | ObjectInspectorDockable | 类别：const |
| ObjectInspectorDockable | Detach |  | void |  |
| ObjectInspectorDockable | IsAttached |  | bool |  |
| ObjectInspectorDockable | Self |  | ObjectInspectorDockable |  |
| ObjectInspectorPlugin | AccessSelf |  | ObjectInspectorPlugin | 类别：const |
| ObjectInspectorPlugin | GetErrorMessage |  | CUTF8String | 类别：nonconst |
| ObjectInspectorPlugin | GetTitle |  | CUTF8String | 类别：nonconst |
| ObjectInspectorPlugin | HasError |  | bool |  |
| ObjectInspectorPlugin | Self |  | ObjectInspectorPlugin |  |
| ObjectPreset | AccessSelf |  | ObjectPreset | 类别：const |
| ObjectPreset | IsSelected |  | bool |  |
| ObjectPreset | PresetName |  | CUTF8String |  |
| ObjectPreset | Self |  | ObjectPreset |  |
| ObjectProvider | AccessSelf |  | ObjectProvider | 类别：const |
| ObjectProvider | Name |  | CUTF8String |  |
| ObjectProvider | RequestUpdate |  | void |  |
| ObjectProvider | Self |  | ObjectProvider |  |
| Objective | AccessSelf |  | Objective | 类别：const |
| Objective | GetCustom | CustomLocalization | CString | 类别：nonconst |
| Objective | GetDesc |  | CString | 类别：nonconst |
| Objective | GetDescForCountryDef | Unknown | CString | 类别：nonconst |
| Objective | GetDisabledBackground |  | Unknown | 类别：nonconst |
| Objective | GetEnabledBackground |  | Unknown | 类别：nonconst |
| Objective | GetIcon |  | Unknown | 类别：nonconst |
| Objective | GetName |  | CString | 类别：nonconst |
| Objective | GetNameNoFormatting |  | CString | 类别：nonconst |
| Objective | GetObjectiveType |  | ObjectiveType | 类别：nonconst |
| Objective | GetTooltipTag |  | CString | 类别：nonconst |
| Objective | MakeScope |  | Scope |  |
| Objective | Self |  | Objective |  |
| ObjectiveType | AccessSelf |  | ObjectiveType | 类别：const |
| ObjectiveType | GetDesc |  | CString | 类别：nonconst |
| ObjectiveType | GetDescForCountryDef | CountryDefinition | CString | 类别：nonconst |
| ObjectiveType | GetDisabledBackground |  | Unknown | 类别：nonconst |
| ObjectiveType | GetEnabledBackground |  | Unknown | 类别：nonconst |
| ObjectiveType | GetIcon |  | Unknown | 类别：nonconst |
| ObjectiveType | GetIdleHeader |  | CString | 类别：nonconst |
| ObjectiveType | GetIdleHint |  | CString | 类别：nonconst |
| ObjectiveType | GetIsAvailableDescription |  | CString | 类别：nonconst |
| ObjectiveType | GetName |  | CString | 类别：nonconst |
| ObjectiveType | GetNameForCountryDef | CountryDefinition | CString | 类别：nonconst |
| ObjectiveType | GetNameNoFormatting |  | CString | 类别：nonconst |
| ObjectiveType | GetRecommendedGameRules |  | Unknown | 类别：nonconst |
| ObjectiveType | GetRecommendedTags |  | Unknown | 类别：nonconst |
| ObjectiveType | GetTooltipTag |  | CString | 类别：nonconst |
| ObjectiveType | HasRecommendedGameRules |  | bool |  |
| ObjectiveType | IsAvailable |  | bool |  |
| ObjectiveType | IsAvailableForAllCountries |  | bool |  |
| ObjectiveType | Self |  | ObjectiveType |  |
| ObstinanceMarker | AccessSelf |  | ObstinanceMarker | 类别：const |
| ObstinanceMarker | GetPosition |  | CVector2f | 类别：nonconst |
| ObstinanceMarker | Self |  | ObstinanceMarker |  |
| OccupationPiechartData | AccessSelf |  | OccupationPiechartData | 类别：const |
| OccupationPiechartData | GetCountry |  | Country | 类别：nonconst |
| OccupationPiechartData | GetCountryColor |  | CVector4f | 类别：nonconst |
| OccupationPiechartData | GetOccupationFraction |  | CFixedPoint | 类别：nonconst |
| OccupationPiechartData | Self |  | OccupationPiechartData |  |
| OosData | AccessSelf |  | OosData | 类别：const |
| OosData | GetFolder |  | CString | 类别：nonconst |
| OosData | GetPlayerId |  | int32 | 类别：nonconst |
| OosData | GetPlayerName |  | CString | 类别：nonconst |
| OosData | GetType |  | CString | 类别：nonconst |
| OosData | IsLocalPlayer |  | bool |  |
| OosData | IsObserver |  | bool |  |
| OosData | Self |  | OosData |  |
| OosWindow | AccessSelf |  | OosWindow | 类别：const |
| OosWindow | Close |  | void |  |
| OosWindow | Continue |  | void |  |
| OosWindow | GetOosData |  | Unknown | 类别：nonconst |
| OosWindow | GoToMenu |  | void |  |
| OosWindow | IsLocalOos |  | bool |  |
| OosWindow | IsMultiplayerHost |  | bool |  |
| OosWindow | Resync |  | void |  |
| OosWindow | Self |  | OosWindow |  |
| OpinionMarker | AccessSelf |  | OpinionMarker | 类别：const |
| OpinionMarker | GetCountry |  | Country | 类别：nonconst |
| OpinionMarker | GetPosition |  | CVector2f | 类别：nonconst |
| OpinionMarker | Self |  | OpinionMarker |  |
| OutgoingFriendRequest | AccessSelf |  | OutgoingFriendRequest | 类别：const |
| OutgoingFriendRequest | GetName |  | CUTF8String | 类别：nonconst |
| OutgoingFriendRequest | Remove |  | void |  |
| OutgoingFriendRequest | Self |  | OutgoingFriendRequest |  |
| Outliner | AccessPlayers |  | Unknown | 类别：const |
| Outliner | AccessSelf |  | Outliner | 类别：const |
| Outliner | Self |  | Outliner |  |
| OutlinerEntry | AccessScope |  | Scope | 类别：const |
| OutlinerEntry | AccessSelf |  | OutlinerEntry | 类别：const |
| OutlinerEntry | AccessSituation |  | Event | 类别：const |
| OutlinerEntry | GetKey |  | int32 | 类别：nonconst |
| OutlinerEntry | GetNumSubEntries |  | int32 | 类别：nonconst |
| OutlinerEntry | GetPinnedSubEntries |  | Unknown | 类别：nonconst |
| OutlinerEntry | GetSubEntries |  | Unknown | 类别：nonconst |
| OutlinerEntry | GetTitle |  | CString | 类别：nonconst |
| OutlinerEntry | IsCategory |  | bool |  |
| OutlinerEntry | IsExpanded |  | bool |  |
| OutlinerEntry | IsPinned |  | bool |  |
| OutlinerEntry | IsPinnedExpanded |  | bool |  |
| OutlinerEntry | IsShown |  | bool |  |
| OutlinerEntry | IsShownPinned |  | bool |  |
| OutlinerEntry | Self |  | OutlinerEntry |  |
| OutlinerEntry | ToggleExpanded |  | void |  |
| OutlinerEntry | TogglePinned |  | void |  |
| OutlinerEntry | TogglePinnedExpanded |  | void |  |
| OutputEntry | AccessSelf |  | OutputEntry | 类别：const |
| OutputEntry | GetInputTextures |  | Unknown | 类别：nonconst |
| OutputEntry | GetPath |  | CString | 类别：nonconst |
| OutputEntry | IsSelected |  | bool |  |
| OutputEntry | IsValid |  | bool |  |
| OutputEntry | Self |  | OutputEntry |  |
| OutputEntry | ToggleIsSelected |  | void |  |
| PanelMilitary | AccessCountry |  | Country | 类别：const |
| PanelMilitary | AccessSelf |  | PanelMilitary | 类别：const |
| PanelMilitary | CanAnyUnitInAnyPlayerFormationBeUpgraded |  | bool |  |
| PanelMilitary | GetCountry |  | Country | 类别：nonconst |
| PanelMilitary | GetUpgradeAllUnitsInAllFormationsCommand |  | Command | 类别：nonconst |
| PanelMilitary | OnClickRecruitArmyFormation |  | void |  |
| PanelMilitary | OnClickRecruitFleetFormation |  | void |  |
| PanelMilitary | Self |  | PanelMilitary |  |
| ParametricSelect | AccessSelf |  | ParametricSelect | 类别：const |
| ParametricSelect | IsHeightDeltaEnabled |  | bool |  |
| ParametricSelect | IsHeightRangeEnabled |  | bool |  |
| ParametricSelect | Select |  | void |  |
| ParametricSelect | Self |  | ParametricSelect |  |
| ParametricSelect | SetHeightDeltaMax |  | void |  |
| ParametricSelect | SetHeightDeltaMin |  | void |  |
| ParametricSelect | SetHeightRangeMax |  | void |  |
| ParametricSelect | SetHeightRangeMin |  | void |  |
| ParametricSelect | Toggle |  | void |  |
| ParticleUserData | AccessSelf |  | ParticleUserData | 类别：const |
| ParticleUserData | Id |  | CString |  |
| ParticleUserData | IsSelected |  | bool |  |
| ParticleUserData | Label |  | CString |  |
| ParticleUserData | Remove |  | void |  |
| ParticleUserData | Self |  | ParticleUserData |  |
| ParticleUserData | ToggleSelected |  | void |  |
| ParticleUserData | TypeName |  | Unknown |  |
| ParticleUserData | TypeSize |  | int32 |  |
| Party | AccessSelf |  | Party | 类别：const |
| Party | CanJoinGovernment |  | bool |  |
| Party | GetCanJoinGovernmentDesc |  | CString | 类别：nonconst |
| Party | GetColor |  | CVector4f | 类别：nonconst |
| Party | GetCountry |  | Country | 类别：nonconst |
| Party | GetCurrentPollNumVoters |  | int64 | 类别：nonconst |
| Party | GetCurrentPollNumVotersDifference |  | int64 | 类别：nonconst |
| Party | GetCurrentPollVotingPower |  | int64 | 类别：nonconst |
| Party | GetCurrentPollVotingPowerDifference |  | int64 | 类别：nonconst |
| Party | GetCurrentPollVotingPowerShare |  | CFixedPoint | 类别：nonconst |
| Party | GetCurrentVotingPower |  | int64 | 类别：nonconst |
| Party | GetCurrentVotingPowerShare |  | CFixedPoint | 类别：nonconst |
| Party | GetCustom | CustomLocalization | CString | 类别：nonconst |
| Party | GetElectionVotesTrend |  | DataTrend | 类别：nonconst |
| Party | GetIcon |  | Unknown | 类别：nonconst |
| Party | GetIndependentIGs |  | Unknown | 类别：nonconst |
| Party | GetJoinWeightBreakdown | Unknown | CString | 类别：nonconst |
| Party | GetLeader |  | InterestGroup | 类别：nonconst |
| Party | GetLeaderCharacter |  | Character | 类别：nonconst |
| Party | GetMembers |  | Unknown | 类别：nonconst |
| Party | GetMembersBreakdown |  | CString | 类别：nonconst |
| Party | GetMembersSummary |  | CString | 类别：nonconst |
| Party | GetMomentum |  | CFixedPoint | 类别：nonconst |
| Party | GetMomentumDesc |  | CString | 类别：nonconst |
| Party | GetName |  | CString | 类别：nonconst |
| Party | GetNameNoFormatting |  | CString | 类别：nonconst |
| Party | GetNumVotersLastElection |  | int64 | 类别：nonconst |
| Party | GetTooltipTag |  | CString | 类别：nonconst |
| Party | IsInGovernment |  | bool |  |
| Party | IsValid |  | bool |  |
| Party | MakeScope |  | Scope |  |
| Party | Self |  | Party |  |
| PartyPanel | AccessParty |  | Party | 类别：const |
| PartyPanel | AccessSelf |  | PartyPanel | 类别：const |
| PartyPanel | GetParty |  | Party | 类别：nonconst |
| PartyPanel | Self |  | PartyPanel |  |
| PastBattleMarker | AccessSelf |  | PastBattleMarker | 类别：const |
| PastBattleMarker | GetBattle |  | Battle | 类别：nonconst |
| PastBattleMarker | GetPosition |  | CVector2f | 类别：nonconst |
| PastBattleMarker | Self |  | PastBattleMarker |  |
| PauseMenu | AccessSelf |  | PauseMenu | 类别：const |
| PauseMenu | CanLoadIngame |  | bool |  |
| PauseMenu | ExitGame |  | void |  |
| PauseMenu | GetExitName |  | CString | 类别：nonconst |
| PauseMenu | IsLobbyOpen |  | bool |  |
| PauseMenu | LoadIngame |  | void |  |
| PauseMenu | LoadIngameTooltip |  | CString |  |
| PauseMenu | OpenLobby |  | void |  |
| PauseMenu | OpenSettings |  | void |  |
| PauseMenu | Resume |  | void |  |
| PauseMenu | Save |  | void |  |
| PauseMenu | Self |  | PauseMenu |  |
| PauseMenu | SwitchCountry |  | void |  |
| PdxAccount | AccessSelf |  | PdxAccount | 类别：const |
| PdxAccount | GetLastLinkError |  | Unknown | 类别：nonconst |
| PdxAccount | GetLastLinkErrorLocalized |  | CString | 类别：nonconst |
| PdxAccount | GetThirdPartyProviderLocalizationKey |  | CString | 类别：nonconst |
| PdxAccount | GetThirdPartyProviderLocalizedName |  | CString | 类别：nonconst |
| PdxAccount | IsLinkingPossible |  | bool |  |
| PdxAccount | IsLoggedIn |  | bool |  |
| PdxAccount | Self |  | PdxAccount |  |
| PdxCoreSetting | AccessSelf |  | PdxCoreSetting | 类别：const |
| PdxCoreSetting | RequireApply |  | bool |  |
| PdxCoreSetting | RequireRestart |  | bool |  |
| PdxCoreSetting | Self |  | PdxCoreSetting |  |
| PdxEnumSetting | AccessSelf |  | PdxEnumSetting | 类别：const |
| PdxEnumSetting | HasValueChanged | Unknown | bool |  |
| PdxEnumSetting | Self |  | PdxEnumSetting |  |
| PdxGuiFoldOut | AccessSelf |  | PdxGuiFoldOut | 类别：const |
| PdxGuiFoldOut | Fold |  | void |  |
| PdxGuiFoldOut | IsFolded |  | bool |  |
| PdxGuiFoldOut | IsUnfolded |  | bool |  |
| PdxGuiFoldOut | Self |  | PdxGuiFoldOut |  |
| PdxGuiFoldOut | SetFoldState |  | void |  |
| PdxGuiFoldOut | Toggle |  | void |  |
| PdxGuiFoldOut | Unfold |  | void |  |
| PdxGuiGfxVideoControl | AccessSelf |  | PdxGuiGfxVideoControl | 类别：const |
| PdxGuiGfxVideoControl | IsLooping |  | bool |  |
| PdxGuiGfxVideoControl | IsPlaybackComplete |  | bool |  |
| PdxGuiGfxVideoControl | IsPlaying |  | bool |  |
| PdxGuiGfxVideoControl | Restart |  | void |  |
| PdxGuiGfxVideoControl | Self |  | PdxGuiGfxVideoControl |  |
| PdxGuiGfxVideoControl | SetLooping | Unknown | void |  |
| PdxGuiGfxVideoControl | Start |  | void |  |
| PdxGuiGfxVideoControl | Stop |  | void |  |
| PdxGuiTableRow | AccessSelf |  | PdxGuiTableRow | 类别：const |
| PdxGuiTableRow | GetIndex |  | int32 | 类别：nonconst |
| PdxGuiTableRow | Self |  | PdxGuiTableRow |  |
| PdxGuiTreeTable | AccessSelf |  | PdxGuiTreeTable | 类别：const |
| PdxGuiTreeTable | CanExpand | int32 | bool |  |
| PdxGuiTreeTable | Expand | Unknown | void |  |
| PdxGuiTreeTable | GetDepth | Unknown | int32 | 类别：nonconst |
| PdxGuiTreeTable | GetIndent | int32 float | CVector2f | 类别：nonconst |
| PdxGuiTreeTable | GetNumChildren | Unknown | int32 | 类别：nonconst |
| PdxGuiTreeTable | IsExpanded | int32 | bool |  |
| PdxGuiTreeTable | Self |  | PdxGuiTreeTable |  |
| PdxGuiTreeTable | ToggleExpand | int32 | void |  |
| PdxGuiTreeTable | Unexpand | Unknown | void |  |
| PdxGuiWidget | AccessParent |  | PdxGuiWidget | 类别：const |
| PdxGuiWidget | AccessSelf |  | PdxGuiWidget | 类别：const |
| PdxGuiWidget | CountVisibleChildren |  | int32 |  |
| PdxGuiWidget | DisableValueUpdate |  | void |  |
| PdxGuiWidget | EnableValueUpdate |  | void |  |
| PdxGuiWidget | FindChild | CString | PdxGuiWidget |  |
| PdxGuiWidget | GetChildrenCount |  | int32 | 类别：nonconst |
| PdxGuiWidget | GetIndexInDataModel |  | int32 | 类别：nonconst |
| PdxGuiWidget | GetRawShortcut |  | CUTF8String | 类别：nonconst |
| PdxGuiWidget | GetShortcut |  | CUTF8String | 类别：nonconst |
| PdxGuiWidget | GetTooltipLockProgress |  | float | 类别：nonconst |
| PdxGuiWidget | HasContext | CString | bool |  |
| PdxGuiWidget | Hide |  | void |  |
| PdxGuiWidget | InterruptAnimation | Unknown | void |  |
| PdxGuiWidget | InterruptThenTriggerAnimation | CString CString | void |  |
| PdxGuiWidget | IsNestedTooltip |  | bool |  |
| PdxGuiWidget | IsTooltipLocked |  | bool |  |
| PdxGuiWidget | IsVisible |  | bool |  |
| PdxGuiWidget | Parent |  | Unknown |  |
| PdxGuiWidget | Self |  | PdxGuiWidget |  |
| PdxGuiWidget | Show |  | void |  |
| PdxGuiWidget | StackBottom |  | void |  |
| PdxGuiWidget | StackTop |  | void |  |
| PdxGuiWidget | TriggerAnimation | CString | void |  |
| PdxSetting | AccessSelf |  | PdxSetting | 类别：const |
| PdxSetting | AccessSetting |  | Unknown | 类别：const |
| PdxSetting | ChangesNotSaved |  | bool |  |
| PdxSetting | GetSetting |  | Unknown | 类别：nonconst |
| PdxSetting | GetTitle |  | CUTF8String | 类别：nonconst |
| PdxSetting | GetTooltip |  | CUTF8String | 类别：nonconst |
| PdxSetting | Self |  | PdxSetting |  |
| PdxSettingsWindow | AccessSelf |  | PdxSettingsWindow | 类别：const |
| PdxSettingsWindow | AllowApply |  | bool |  |
| PdxSettingsWindow | AllowRestore |  | bool |  |
| PdxSettingsWindow | AppliedOnRestart |  | bool |  |
| PdxSettingsWindow | HasChanged |  | bool |  |
| PdxSettingsWindow | OnApply |  | void |  |
| PdxSettingsWindow | OnCancel |  | void |  |
| PdxSettingsWindow | OnRestore |  | void |  |
| PdxSettingsWindow | OnSave |  | void |  |
| PdxSettingsWindow | Self |  | PdxSettingsWindow |  |
| PdxSettingsWindowCategory | AccessSelf |  | PdxSettingsWindowCategory | 类别：const |
| PdxSettingsWindowCategory | GetName |  | CString | 类别：nonconst |
| PdxSettingsWindowCategory | Self |  | PdxSettingsWindowCategory |  |
| PdxValueSetting | AccessSelf |  | PdxValueSetting | 类别：const |
| PdxValueSetting | GetFormattedPendingValue | Unknown | CString | 类别：nonconst |
| PdxValueSetting | GetPendingValue | Unknown | float | 类别：nonconst |
| PdxValueSetting | HasValueChanged | Unknown | bool |  |
| PdxValueSetting | Self |  | PdxValueSetting |  |
| PieTimer | AccessSelf |  | PieTimer | 类别：const |
| PieTimer | GetSlices |  | Unknown | 类别：nonconst |
| PieTimer | GetSlicesInverted |  | Unknown | 类别：nonconst |
| PieTimer | Self |  | PieTimer |  |
| PieTimerSlice | AccessSelf |  | PieTimerSlice | 类别：const |
| PieTimerSlice | GetColor |  | CVector4f | 类别：nonconst |
| PieTimerSlice | GetValue |  | float | 类别：nonconst |
| PieTimerSlice | Self |  | PieTimerSlice |  |
| Playable | AccessSelf |  | Playable | 类别：const |
| Playable | Self |  | Playable |  |
| Player | AccessPlayedOrObservedCountry |  | Country | 类别：const |
| Player | AccessSelf |  | Player | 类别：const |
| Player | GetName |  | CString | 类别：nonconst |
| Player | GetPlayedOrObservedCountry |  | Country | 类别：nonconst |
| Player | GetTooltipTag |  | CString | 类别：nonconst |
| Player | HasPlayable |  | bool |  |
| Player | IsHost |  | bool |  |
| Player | IsObserver |  | bool |  |
| Player | IsPlayedOrObservedCountry | Country | bool |  |
| Player | Self |  | Player |  |
| PlayerJoinRequest | Accept |  | void |  |
| PlayerJoinRequest | AccessSelf |  | PlayerJoinRequest | 类别：const |
| PlayerJoinRequest | GetPlayerName |  | CString | 类别：nonconst |
| PlayerJoinRequest | IsChecked |  | bool |  |
| PlayerJoinRequest | Reject |  | void |  |
| PlayerJoinRequest | Self |  | PlayerJoinRequest |  |
| PlayerJoinRequest | Toggle |  | void |  |
| PlayerMessageItem | AccessSelf |  | PlayerMessageItem | 类别：const |
| PlayerMessageItem | GetColor |  | CVector4f | 类别：nonconst |
| PlayerMessageItem | GetCountry |  | Country | 类别：nonconst |
| PlayerMessageItem | GetDate |  | CString | 类别：nonconst |
| PlayerMessageItem | GetDescription |  | CString | 类别：nonconst |
| PlayerMessageItem | GetDiploPlay |  | DiplomaticPlay | 类别：nonconst |
| PlayerMessageItem | GetDiplomaticAction |  | DiplomaticAction | 类别：nonconst |
| PlayerMessageItem | GetInstitution |  | Institution | 类别：nonconst |
| PlayerMessageItem | GetLaw |  | Law | 类别：nonconst |
| PlayerMessageItem | GetMessageGroupTag |  | CString | 类别：nonconst |
| PlayerMessageItem | GetName |  | CString | 类别：nonconst |
| PlayerMessageItem | GetOnCreatedSoundEvent |  | Unknown | 类别：nonconst |
| PlayerMessageItem | GetPrevLaw |  | Law | 类别：nonconst |
| PlayerMessageItem | GetScopeActorCountry |  | Country | 类别：nonconst |
| PlayerMessageItem | GetScopeDiploPlay |  | DiplomaticPlay | 类别：nonconst |
| PlayerMessageItem | GetScopeTargetCountry |  | Country | 类别：nonconst |
| PlayerMessageItem | GetScopeTechnology |  | Technology | 类别：nonconst |
| PlayerMessageItem | GetTexture |  | Unknown | 类别：nonconst |
| PlayerMessageItem | GetTooltip |  | CString | 类别：nonconst |
| PlayerMessageItem | GetTopScope |  | TopScope | 类别：nonconst |
| PlayerMessageItem | Self |  | PlayerMessageItem |  |
| PlotLine | AccessSelf |  | PlotLine | 类别：const |
| PlotLine | GetInterpolatedIndexNearMouse |  | float | 类别：nonconst |
| PlotLine | GetInterpolatedValueNearMouse |  | CVector2f | 类别：nonconst |
| PlotLine | GetPlotRect |  | CPdxFloatRect | 类别：nonconst |
| PlotLine | GetSnappedIndexNearMouse |  | int32 | 类别：nonconst |
| PlotLine | GetSnappedValueNearMouse |  | CVector2f | 类别：nonconst |
| PlotLine | HasPositionNearMouse |  | bool |  |
| PlotLine | Self |  | PlotLine |  |
| PoliticalLobby | AccessSelf |  | PoliticalLobby | 类别：const |
| PoliticalLobby | CalcJoinWeight | InterestGroup | CFixedPoint |  |
| PoliticalLobby | CalcJoinWeightDesc | InterestGroup | CString |  |
| PoliticalLobby | GetAppeasement |  | int32 | 类别：nonconst |
| PoliticalLobby | GetAppeasementChangesDesc |  | CString | 类别：nonconst |
| PoliticalLobby | GetAppeasementEffectsDesc |  | CString | 类别：nonconst |
| PoliticalLobby | GetCountry |  | Country | 类别：nonconst |
| PoliticalLobby | GetCustom | CustomLocalization | CString | 类别：nonconst |
| PoliticalLobby | GetDeficitAppeasementForProgressBar |  | CFixedPoint | 类别：nonconst |
| PoliticalLobby | GetDisbandReasonDesc |  | CString | 类别：nonconst |
| PoliticalLobby | GetEstablishmentDate |  | Date | 类别：nonconst |
| PoliticalLobby | GetExcessAppeasementForProgressBar |  | CFixedPoint | 类别：nonconst |
| PoliticalLobby | GetMembers |  | Unknown | 类别：nonconst |
| PoliticalLobby | GetMembersDesc |  | CString | 类别：nonconst |
| PoliticalLobby | GetName |  | CString | 类别：nonconst |
| PoliticalLobby | GetNameNoFormatting |  | CString | 类别：nonconst |
| PoliticalLobby | GetNameNoIcon |  | CString | 类别：nonconst |
| PoliticalLobby | GetTargetCountry |  | Country | 类别：nonconst |
| PoliticalLobby | GetTextIcon |  | CString | 类别：nonconst |
| PoliticalLobby | GetTooltipTag |  | CString | 类别：nonconst |
| PoliticalLobby | GetTotalClout |  | CFixedPoint | 类别：nonconst |
| PoliticalLobby | GetTotalCloutBreakdown |  | CString | 类别：nonconst |
| PoliticalLobby | GetType |  | PoliticalLobbyType | 类别：nonconst |
| PoliticalLobby | IsPinnedInOutliner |  | bool |  |
| PoliticalLobby | IsValid |  | bool |  |
| PoliticalLobby | MakeScope |  | Scope |  |
| PoliticalLobby | Self |  | PoliticalLobby |  |
| PoliticalLobby | TogglePinInOutliner |  | void |  |
| PoliticalLobbyAppeasementFactor | AccessSelf |  | PoliticalLobbyAppeasementFactor | 类别：const |
| PoliticalLobbyAppeasementFactor | GetCustom | CustomLocalization | CString | 类别：nonconst |
| PoliticalLobbyAppeasementFactor | GetDesc |  | CString | 类别：nonconst |
| PoliticalLobbyAppeasementFactor | GetName |  | CString | 类别：nonconst |
| PoliticalLobbyAppeasementFactor | GetTooltipTag |  | CString | 类别：nonconst |
| PoliticalLobbyAppeasementFactor | MakeScope |  | Scope |  |
| PoliticalLobbyAppeasementFactor | Self |  | PoliticalLobbyAppeasementFactor |  |
| PoliticalLobbyMarker | AccessSelf |  | PoliticalLobbyMarker | 类别：const |
| PoliticalLobbyMarker | GetPlacementCountry |  | Country | 类别：nonconst |
| PoliticalLobbyMarker | GetPoliticalLobby |  | PoliticalLobby | 类别：nonconst |
| PoliticalLobbyMarker | GetPosition |  | CVector2f | 类别：nonconst |
| PoliticalLobbyMarker | Self |  | PoliticalLobbyMarker |  |
| PoliticalLobbyPanel | AccessSelf |  | PoliticalLobbyPanel | 类别：const |
| PoliticalLobbyPanel | GetPoliticalLobby |  | PoliticalLobby | 类别：nonconst |
| PoliticalLobbyPanel | Self |  | PoliticalLobbyPanel |  |
| PoliticalLobbyType | AccessSelf |  | PoliticalLobbyType | 类别：const |
| PoliticalLobbyType | GetAppeasementFactorsAnti |  | Unknown | 类别：nonconst |
| PoliticalLobbyType | GetAppeasementFactorsPro |  | Unknown | 类别：nonconst |
| PoliticalLobbyType | GetCategory |  | CString | 类别：nonconst |
| PoliticalLobbyType | GetCustom | CustomLocalization | CString | 类别：nonconst |
| PoliticalLobbyType | GetName |  | CString | 类别：nonconst |
| PoliticalLobbyType | GetTexture |  | Unknown | 类别：nonconst |
| PoliticalLobbyType | GetTooltipTag |  | CString | 类别：nonconst |
| PoliticalLobbyType | MakeScope |  | Scope |  |
| PoliticalLobbyType | Self |  | PoliticalLobbyType |  |
| PoliticalMovement | AccessSelf |  | PoliticalMovement | 类别：const |
| PoliticalMovement | CanCauseObstinance |  | bool |  |
| PoliticalMovement | GetAffectedLawsStall |  | Unknown | 类别：nonconst |
| PoliticalMovement | GetAffectedLawsSuccess |  | Unknown | 类别：nonconst |
| PoliticalMovement | GetAffectedStallPercentageOnLaw | Unknown | CFixedPoint | 类别：nonconst |
| PoliticalMovement | GetAffectedSuccessPercentageOnEndorsedLaws |  | CFixedPoint | 类别：nonconst |
| PoliticalMovement | GetAffectedSuccessPercentageOnLaw | Unknown | CFixedPoint | 类别：nonconst |
| PoliticalMovement | GetAffectedSuccessPercentageOnOpposedLaws |  | CFixedPoint | 类别：nonconst |
| PoliticalMovement | GetBolsteringEffectDesc |  | CString | 类别：nonconst |
| PoliticalMovement | GetBottomSupportingCharacters |  | Unknown | 类别：nonconst |
| PoliticalMovement | GetBottomSupportingCharactersDesc |  | CString | 类别：nonconst |
| PoliticalMovement | GetCharacterIdeologies |  | Unknown | 类别：nonconst |
| PoliticalMovement | GetCivilWar |  | CivilWar | 类别：nonconst |
| PoliticalMovement | GetCoreIdeology |  | Ideology | 类别：nonconst |
| PoliticalMovement | GetCountry |  | Country | 类别：nonconst |
| PoliticalMovement | GetCustom | CustomLocalization | CString | 类别：nonconst |
| PoliticalMovement | GetHighestStateObstinance |  | CFixedPoint | 类别：nonconst |
| PoliticalMovement | GetInfluencedInterestGroups |  | Unknown | 类别：nonconst |
| PoliticalMovement | GetMilitarySupport |  | CFixedPoint | 类别：nonconst |
| PoliticalMovement | GetName |  | CString | 类别：nonconst |
| PoliticalMovement | GetNameNoFormatting |  | CString | 类别：nonconst |
| PoliticalMovement | GetNameNoIcon |  | CString | 类别：nonconst |
| PoliticalMovement | GetNumOfObstinateStates |  | int32 | 类别：nonconst |
| PoliticalMovement | GetNumSupportingIndividuals |  | int64 | 类别：nonconst |
| PoliticalMovement | GetNumSupportingMilitaryIndividuals |  | int64 | 类别：nonconst |
| PoliticalMovement | GetNumSupportingRadicals |  | int64 | 类别：nonconst |
| PoliticalMovement | GetObstinateStatesBreakdown |  | CString | 类别：nonconst |
| PoliticalMovement | GetPopSupportFactors |  | Unknown | 类别：nonconst |
| PoliticalMovement | GetPopularSupport |  | CFixedPoint | 类别：nonconst |
| PoliticalMovement | GetRadicalism |  | CFixedPoint | 类别：nonconst |
| PoliticalMovement | GetRadicalismTrend |  | DataTrend | 类别：nonconst |
| PoliticalMovement | GetSupport |  | CFixedPoint | 类别：nonconst |
| PoliticalMovement | GetSupportDesc |  | CString | 类别：nonconst |
| PoliticalMovement | GetSupportTrend |  | DataTrend | 类别：nonconst |
| PoliticalMovement | GetSupportingCharacters |  | Unknown | 类别：nonconst |
| PoliticalMovement | GetSupportingInterestGroups |  | Unknown | 类别：nonconst |
| PoliticalMovement | GetSupportingPops |  | PopList | 类别：nonconst |
| PoliticalMovement | GetSuppressionEffectDesc |  | CString | 类别：nonconst |
| PoliticalMovement | GetTargetRadicalism |  | CFixedPoint | 类别：nonconst |
| PoliticalMovement | GetTargetRadicalismDesc |  | CString | 类别：nonconst |
| PoliticalMovement | GetTargetSupport |  | CFixedPoint | 类别：nonconst |
| PoliticalMovement | GetTextIcon |  | CString | 类别：nonconst |
| PoliticalMovement | GetTexture |  | Unknown | 类别：nonconst |
| PoliticalMovement | GetTimedModifiers |  | Unknown | 类别：nonconst |
| PoliticalMovement | GetTooltipTag |  | CString | 类别：nonconst |
| PoliticalMovement | GetTopSupportingCharacters |  | Unknown | 类别：nonconst |
| PoliticalMovement | GetType |  | PoliticalMovementType | 类别：nonconst |
| PoliticalMovement | GetUprisingDefinition |  | CountryDefinition | 类别：nonconst |
| PoliticalMovement | HasSeparateUprisingDefinition |  | bool |  |
| PoliticalMovement | IsBeingHighlighted |  | bool |  |
| PoliticalMovement | IsBolstered |  | bool |  |
| PoliticalMovement | IsCausingObstinance |  | bool |  |
| PoliticalMovement | IsInsurrectionary |  | bool |  |
| PoliticalMovement | IsPinnedInOutliner |  | bool |  |
| PoliticalMovement | IsRevolutionary |  | bool |  |
| PoliticalMovement | IsSecessionist |  | bool |  |
| PoliticalMovement | IsSuppressed |  | bool |  |
| PoliticalMovement | IsValid |  | bool |  |
| PoliticalMovement | MakeScope |  | Scope |  |
| PoliticalMovement | PredictNumberOfRadicalsEveryMonth |  | int64 |  |
| PoliticalMovement | Self |  | PoliticalMovement |  |
| PoliticalMovement | ToggleBolstering |  | Command |  |
| PoliticalMovement | TogglePinInOutliner |  | void |  |
| PoliticalMovement | ToggleSuppression |  | Command |  |
| PoliticalMovementCategory | AccessSelf |  | PoliticalMovementCategory | 类别：const |
| PoliticalMovementCategory | GetCustom | CustomLocalization | CString | 类别：nonconst |
| PoliticalMovementCategory | GetName |  | CString | 类别：nonconst |
| PoliticalMovementCategory | GetTexture |  | Unknown | 类别：nonconst |
| PoliticalMovementCategory | GetTooltipTag |  | CString | 类别：nonconst |
| PoliticalMovementCategory | HasCulturalIdentity |  | bool |  |
| PoliticalMovementCategory | HasReligiousIdentity |  | bool |  |
| PoliticalMovementCategory | MakeScope |  | Scope |  |
| PoliticalMovementCategory | Self |  | PoliticalMovementCategory |  |
| PoliticalMovementPanel | AccessSelf |  | PoliticalMovementPanel | 类别：const |
| PoliticalMovementPanel | GetPoliticalMovement |  | PoliticalMovement | 类别：nonconst |
| PoliticalMovementPanel | Self |  | PoliticalMovementPanel |  |
| PoliticalMovementPopSupportFactor | AccessSelf |  | PoliticalMovementPopSupportFactor | 类别：const |
| PoliticalMovementPopSupportFactor | GetName |  | CString | 类别：nonconst |
| PoliticalMovementPopSupportFactor | GetTooltipTag |  | CString | 类别：nonconst |
| PoliticalMovementPopSupportFactor | Self |  | PoliticalMovementPopSupportFactor |  |
| PoliticalMovementType | AccessSelf |  | PoliticalMovementType | 类别：const |
| PoliticalMovementType | GetCategory |  | PoliticalMovementCategory | 类别：nonconst |
| PoliticalMovementType | GetCoreIdeology |  | Ideology | 类别：nonconst |
| PoliticalMovementType | GetCustom | CustomLocalization | CString | 类别：nonconst |
| PoliticalMovementType | GetName |  | CString | 类别：nonconst |
| PoliticalMovementType | GetNameNoFormatting |  | CString | 类别：nonconst |
| PoliticalMovementType | GetTexture |  | Unknown | 类别：nonconst |
| PoliticalMovementType | GetTooltipTag |  | CString | 类别：nonconst |
| PoliticalMovementType | IsValid |  | bool |  |
| PoliticalMovementType | MakeScope |  | Scope |  |
| PoliticalMovementType | Self |  | PoliticalMovementType |  |
| PoliticsPanel | AccessActiveIGTraits |  | Unknown | 类别：const |
| PoliticsPanel | AccessReformGovernment |  | ReformGovernment | 类别：const |
| PoliticsPanel | AccessSelf |  | PoliticsPanel | 类别：const |
| PoliticsPanel | GetAgitatorSlots |  | Unknown | 类别：nonconst |
| PoliticsPanel | GetCloutGraphDateEnd |  | CString | 类别：nonconst |
| PoliticsPanel | GetCloutGraphDateStart |  | CString | 类别：nonconst |
| PoliticsPanel | GetCloutGraphMax |  | CFixedPoint | 类别：nonconst |
| PoliticsPanel | GetPopulationGroupingsForClout |  | Unknown | 类别：nonconst |
| PoliticsPanel | GetPopulationGroupingsForPopulation |  | Unknown | 类别：nonconst |
| PoliticsPanel | GetReformGovernment |  | ReformGovernment | 类别：nonconst |
| PoliticsPanel | IsCloutGraphInitialized |  | bool |  |
| PoliticsPanel | ResetAgitatorSlotInvites |  | void |  |
| PoliticsPanel | Self |  | PoliticsPanel |  |
| Pop | AccessBuilding |  | Building | 类别：const |
| Pop | AccessCulture |  | Culture | 类别：const |
| Pop | AccessLargestInterestGroup |  | InterestGroup | 类别：const |
| Pop | AccessPopType |  | PopType | 类别：const |
| Pop | AccessReligion |  | Religion | 类别：const |
| Pop | AccessSelf |  | Pop | 类别：const |
| Pop | AccessState |  | State | 类别：const |
| Pop | AccessSupportedInterestGroups |  | Unknown | 类别：const |
| Pop | CalcAnnualPollTaxAmount |  | CFixedPoint |  |
| Pop | GetAcceptanceStatus |  | AcceptanceStatus | 类别：nonconst |
| Pop | GetAcceptanceValue |  | int32 | 类别：nonconst |
| Pop | GetAcceptanceValueDesc |  | CString | 类别：nonconst |
| Pop | GetAdditionalSOLFactorsDesc |  | CString | 类别：nonconst |
| Pop | GetAnimatedPortrait | PortraitEnvironment PortraitCamera PortraitAnimation CVector2f CString int32 | Unknown | 类别：nonconst |
| Pop | GetAssimilatingCulture |  | Culture | 类别：nonconst |
| Pop | GetAverageAnnualWage |  | CFixedPoint | 类别：nonconst |
| Pop | GetConsumptionFactorDesc |  | CString | 类别：nonconst |
| Pop | GetConvertingReligion |  | Religion | 类别：nonconst |
| Pop | GetCulture |  | Culture | 类别：nonconst |
| Pop | GetCurrentJobSatisfaction |  | CFixedPoint | 类别：nonconst |
| Pop | GetCurrentSoLModifiers |  | int32 | 类别：nonconst |
| Pop | GetCurrentSoLModifiersDesc |  | CString | 类别：nonconst |
| Pop | GetCurrentStandardOfLiving |  | int32 | 类别：nonconst |
| Pop | GetCurrentStandardOfLivingTrend |  | DataTrend | 类别：nonconst |
| Pop | GetCurrentWealth |  | int32 | 类别：nonconst |
| Pop | GetCurrentWealthDesc |  | CString | 类别：nonconst |
| Pop | GetCustom | CustomLocalization | CString | 类别：nonconst |
| Pop | GetDebugInfo |  | CString | 类别：nonconst |
| Pop | GetDependentIncome |  | CFixedPoint | 类别：nonconst |
| Pop | GetDependentIncomeDesc |  | CString | 类别：nonconst |
| Pop | GetDependentIncomeSources |  | CString | 类别：nonconst |
| Pop | GetDependentsSize |  | int64 | 类别：nonconst |
| Pop | GetEducationAccess |  | CFixedPoint | 类别：nonconst |
| Pop | GetEducationAccessDetailsDesc |  | CString | 类别：nonconst |
| Pop | GetExpectedSOLFactorsDesc |  | CString | 类别：nonconst |
| Pop | GetExpectedStandardOfLiving |  | int32 | 类别：nonconst |
| Pop | GetExpectedStandardOfLivingDesc |  | CString | 类别：nonconst |
| Pop | GetExpectedStandardOfLivingFromLiteracy |  | int32 | 类别：nonconst |
| Pop | GetExpectedStandardOfLivingFromLiteracyDesc |  | int32 | 类别：nonconst |
| Pop | GetExpenses |  | CFixedPoint | 类别：nonconst |
| Pop | GetExpensesDesc |  | CString | 类别：nonconst |
| Pop | GetFoodSecurityDesc |  | CString | 类别：nonconst |
| Pop | GetFoodSecurityLabel |  | CString | 类别：nonconst |
| Pop | GetFoodSecurityRaw |  | CFixedPoint | 类别：nonconst |
| Pop | GetFormattedStandardOfLiving |  | CString | 类别：nonconst |
| Pop | GetFormattedStandardOfLivingLabel |  | CString | 类别：nonconst |
| Pop | GetGoodsConsumption |  | Unknown | 类别：nonconst |
| Pop | GetIGMembershipDesc |  | CString | 类别：nonconst |
| Pop | GetIncome |  | CFixedPoint | 类别：nonconst |
| Pop | GetIncomeDesc |  | CString | 类别：nonconst |
| Pop | GetIncomeExpensesBalanceDesc |  | CString | 类别：nonconst |
| Pop | GetInterestGroupDependentMembers | Unknown | int64 | 类别：nonconst |
| Pop | GetInterestGroupMembers | Unknown | int64 | 类别：nonconst |
| Pop | GetInterestGroupWorkingAdultMembers | Unknown | int64 | 类别：nonconst |
| Pop | GetLargestInterestGroup |  | InterestGroup | 类别：nonconst |
| Pop | GetLargestPoliticalMovement |  | PoliticalMovement | 类别：nonconst |
| Pop | GetLiteracyDesc |  | CString | 类别：nonconst |
| Pop | GetLiteracyRate |  | CFixedPoint | 类别：nonconst |
| Pop | GetLocation |  | CString | 类别：nonconst |
| Pop | GetMoney |  | CFixedPoint | 类别：nonconst |
| Pop | GetMovementMembershipDesc |  | CString | 类别：nonconst |
| Pop | GetName |  | CString | 类别：nonconst |
| Pop | GetNameNoFormatting |  | CString | 类别：nonconst |
| Pop | GetNameNoIcon |  | CString | 类别：nonconst |
| Pop | GetNeedsDesc |  | CString | 类别：nonconst |
| Pop | GetNetGrowthRate |  | CFixedPoint | 类别：nonconst |
| Pop | GetNextJobSatisfaction |  | CFixedPoint | 类别：nonconst |
| Pop | GetNextJobSatisfactionDesc |  | CFixedPoint | 类别：nonconst |
| Pop | GetNumAssimilatingIndividuals |  | int64 | 类别：nonconst |
| Pop | GetNumConvertingIndividuals |  | int64 | 类别：nonconst |
| Pop | GetNumDependentPoliticalParticipants |  | int64 | 类别：nonconst |
| Pop | GetNumLoyalists |  | int64 | 类别：nonconst |
| Pop | GetNumPoliticalNonParticipants |  | int64 | 类别：nonconst |
| Pop | GetNumPoliticalParticipants |  | int64 | 类别：nonconst |
| Pop | GetNumPoliticallyInactive |  | int64 | 类别：nonconst |
| Pop | GetNumRadicals |  | int64 | 类别：nonconst |
| Pop | GetNumWorkforce |  | int64 | 类别：nonconst |
| Pop | GetPoliticalMovementSupportFraction | PoliticalMovement | CFixedPoint | 类别：nonconst |
| Pop | GetPoliticalMovementSupporterCount | PoliticalMovement | int64 | 类别：nonconst |
| Pop | GetPoliticalMovementSupportersInterestGroupMembers | Unknown Unknown | int64 | 类别：nonconst |
| Pop | GetPoliticalMovementSupportersLoyalists | Unknown | int64 | 类别：nonconst |
| Pop | GetPoliticalMovementSupportersPoliticalStrength | PoliticalMovement | int64 | 类别：nonconst |
| Pop | GetPoliticalMovementSupportersRadicals | PoliticalMovement | int64 | 类别：nonconst |
| Pop | GetPoliticalMovementTotalSupport | PoliticalMovement | CFixedPoint | 类别：nonconst |
| Pop | GetPoliticalMovementTotalSupportDesc | PoliticalMovement | CString | 类别：nonconst |
| Pop | GetPoliticalStrength |  | int64 | 类别：nonconst |
| Pop | GetPoliticalStrengthDesc |  | CString | 类别：nonconst |
| Pop | GetPoliticalStrengthForIG | Unknown | int64 | 类别：nonconst |
| Pop | GetPoliticalStrengthTrend |  | DataTrend | 类别：nonconst |
| Pop | GetPopAssimilationDesc |  | CString | 类别：nonconst |
| Pop | GetPopConversionDesc |  | CString | 类别：nonconst |
| Pop | GetPopGrowth |  | CFixedPoint | 类别：nonconst |
| Pop | GetPopGrowthDesc |  | CString | 类别：nonconst |
| Pop | GetPopType |  | PopType | 类别：nonconst |
| Pop | GetQualificationsChangeDesc | PopType | CString | 类别：nonconst |
| Pop | GetQualificationsDesc |  | CString | 类别：nonconst |
| Pop | GetReligion |  | Religion | 类别：nonconst |
| Pop | GetSharesDesc |  | CString | 类别：nonconst |
| Pop | GetSizeTrend |  | DataTrend | 类别：nonconst |
| Pop | GetSocialClass |  | SocialClass | 类别：nonconst |
| Pop | GetStarvationEffectDesc |  | CString | 类别：nonconst |
| Pop | GetSupportedPoliticalMovements |  | Unknown | 类别：nonconst |
| Pop | GetTexture |  | Unknown | 类别：nonconst |
| Pop | GetTooltipTag |  | CString | 类别：nonconst |
| Pop | GetTopGoodsConsumption |  | Unknown | 类别：nonconst |
| Pop | GetTotalSize |  | int64 | 类别：nonconst |
| Pop | GetTypeDesc |  | CString | 类别：nonconst |
| Pop | GetTypedPortrait | PortraitEnvironment PortraitCamera PortraitAnimation CVector2f CString int32 | Unknown | 类别：nonconst |
| Pop | GetWageDiscriminationDesc |  | CString | 类别：nonconst |
| Pop | GetWageRequiredToHireFrom |  | CFixedPoint | 类别：nonconst |
| Pop | GetWealthProgression |  | CFixedPoint | 类别：nonconst |
| Pop | GetWeeklyExpenses |  | CFixedPoint | 类别：nonconst |
| Pop | GetWorkforceIncome |  | CFixedPoint | 类别：nonconst |
| Pop | GetWorkforceIncomeDesc |  | CString | 类别：nonconst |
| Pop | GetWorkforceRatio |  | CFixedPoint | 类别：nonconst |
| Pop | GetWorkforceRatioDesc |  | CString | 类别：nonconst |
| Pop | GetWorksAt |  | CString | 类别：nonconst |
| Pop | GetWorksAtList |  | CString | 类别：nonconst |
| Pop | HasSubsistenceIncome |  | bool |  |
| Pop | HasWelfarePayments |  | bool |  |
| Pop | IsAcceptanceStatusIncreasing |  | bool |  |
| Pop | IsAssimilating |  | bool |  |
| Pop | IsBeingHighlighted |  | bool |  |
| Pop | IsBeingTutorialHighlighted |  | bool |  |
| Pop | IsConverting |  | bool |  |
| Pop | IsEmployed |  | bool |  |
| Pop | IsInSevereStarvation |  | bool |  |
| Pop | IsInStarvation |  | bool |  |
| Pop | IsLookingForJob |  | bool |  |
| Pop | IsPaidWages |  | bool |  |
| Pop | IsSlave |  | bool |  |
| Pop | IsValid |  | bool |  |
| Pop | MakeScope |  | Scope |  |
| Pop | Self |  | Pop |  |
| PopBrowserPanel | AcceptanceFilterAreNoStatusesShown |  | bool |  |
| PopBrowserPanel | AcceptanceFilterHideAllStatuses |  | void |  |
| PopBrowserPanel | AcceptanceFilterIsStatusShown | AcceptanceStatus | bool |  |
| PopBrowserPanel | AcceptanceFilterShowAllStatuses |  | void |  |
| PopBrowserPanel | AcceptanceFilterToggleShown | AcceptanceStatus | void |  |
| PopBrowserPanel | AcceptanceFiltersAreAllStasusesShown |  | bool |  |
| PopBrowserPanel | AccessSelf |  | PopBrowserPanel | 类别：const |
| PopBrowserPanel | CultureFilterAreAllShown |  | bool |  |
| PopBrowserPanel | CultureFilterAreNoneShown |  | bool |  |
| PopBrowserPanel | CultureFilterHideAll |  | void |  |
| PopBrowserPanel | CultureFilterIsShown | Culture | bool |  |
| PopBrowserPanel | CultureFilterShowAll |  | void |  |
| PopBrowserPanel | CultureFilterToggleShown | Culture | void |  |
| PopBrowserPanel | Filter | Unknown | void |  |
| PopBrowserPanel | GetAllAcceptanceStatuses |  | Unknown | 类别：nonconst |
| PopBrowserPanel | GetAllPopTypes |  | Unknown | 类别：nonconst |
| PopBrowserPanel | GetAllStates |  | Unknown | 类别：nonconst |
| PopBrowserPanel | GetCountry |  | Country | 类别：nonconst |
| PopBrowserPanel | GetFilteredAverageJobSatisfaction |  | CFixedPoint | 类别：nonconst |
| PopBrowserPanel | GetFilteredAverageLiteracy |  | CFixedPoint | 类别：nonconst |
| PopBrowserPanel | GetFilteredAverageStandardOfLiving |  | CFixedPoint | 类别：nonconst |
| PopBrowserPanel | GetFilteredCultures |  | Unknown | 类别：nonconst |
| PopBrowserPanel | GetFilteredNumLoyalists |  | int64 | 类别：nonconst |
| PopBrowserPanel | GetFilteredNumRadicals |  | int64 | 类别：nonconst |
| PopBrowserPanel | GetFilteredPolStrForPopType | PopType | int64 | 类别：nonconst |
| PopBrowserPanel | GetFilteredPoliticalStrength |  | int64 | 类别：nonconst |
| PopBrowserPanel | GetFilteredPopTypes |  | Unknown | 类别：nonconst |
| PopBrowserPanel | GetFilteredPopTypesSortedByPolStr |  | Unknown | 类别：nonconst |
| PopBrowserPanel | GetFilteredReligions |  | Unknown | 类别：nonconst |
| PopBrowserPanel | GetFilteredStates |  | Unknown | 类别：nonconst |
| PopBrowserPanel | GetFilteredTotalSize |  | int64 | 类别：nonconst |
| PopBrowserPanel | GetFilteredTotalSizeForCulture | Culture | int64 | 类别：nonconst |
| PopBrowserPanel | GetFilteredTotalSizeForPopType | PopType | int64 | 类别：非常量 |
| PopBrowserPanel | GetFilteredTotalSizeForReligion | Religion | int64 | 类别：非常量 |
| PopBrowserPanel | GetFilteredTotalSizeForState | State | int64 | 类别：非常量 |
| PopBrowserPanel | GetSortedAndFilteredPops |  | Unknown | 类别：非常量 |
| PopBrowserPanel | IsAnyFilterActive |  | bool |  |
| PopBrowserPanel | IsFilterNo | Unknown | bool |  |
| PopBrowserPanel | IsFilterYes | Unknown | bool |  |
| PopBrowserPanel | IsFiltered | Unknown | bool |  |
| PopBrowserPanel | IsSorted | Unknown | bool |  |
| PopBrowserPanel | PopTypeFilterAreAllShown |  | bool |  |
| PopBrowserPanel | PopTypeFilterAreNoneShown |  | bool |  |
| PopBrowserPanel | PopTypeFilterHideAll |  | void |  |
| PopBrowserPanel | PopTypeFilterIsShown | Unknown | bool |  |
| PopBrowserPanel | PopTypeFilterShowAll |  | void |  |
| PopBrowserPanel | PopTypeFilterToggleShown | Unknown | void |  |
| PopBrowserPanel | ReligionFilterAreAllShown |  | bool |  |
| PopBrowserPanel | ReligionFilterAreNoneShown |  | bool |  |
| PopBrowserPanel | ReligionFilterHideAll |  | void |  |
| PopBrowserPanel | ReligionFilterIsShown | Unknown | bool |  |
| PopBrowserPanel | ReligionFilterShowAll |  | void |  |
| PopBrowserPanel | ReligionFilterToggleShown | Unknown | void |  |
| PopBrowserPanel | ResetAllFilters |  | void |  |
| PopBrowserPanel | Self |  | PopBrowserPanel |  |
| PopBrowserPanel | SetFilterMode | Unknown Unknown | void |  |
| PopBrowserPanel | Sort | Unknown | void |  |
| PopBrowserPanel | StateFilterAreNoStatesShown |  | bool |  |
| PopBrowserPanel | StateFilterHideAllStates |  | void |  |
| PopBrowserPanel | StateFilterIsStateShown | Unknown | bool |  |
| PopBrowserPanel | StateFilterShowAllStates |  | void |  |
| PopBrowserPanel | StateFilterToggleShown | Unknown | void |  |
| PopBrowserPanel | StateFiltersAreAllStatesShown |  | bool |  |
| PopConsumptionGoods | AccessSelf |  | PopConsumptionGoods | 类别：常量 |
| PopConsumptionGoods | GetConsumptionAmount |  | CFixedPoint | 类别：非常量 |
| PopConsumptionGoods | GetConsumptionRatio |  | CFixedPoint | 类别：非常量 |
| PopConsumptionGoods | GetGoods |  | Goods | 类别：非常量 |
| PopConsumptionGoods | GetPop |  | Pop | 类别：非常量 |
| PopConsumptionGoods | GetPopNeedsDesc |  | CString | 类别：非常量 |
| PopConsumptionGoods | GetTooltipTag |  | CString | 类别：非常量 |
| PopConsumptionGoods | Self |  | PopConsumptionGoods |  |
| PopDetailsPanel | AccessPop |  | Pop | 类别：常量 |
| PopDetailsPanel | AccessSelf |  | PopDetailsPanel | 类别：常量 |
| PopDetailsPanel | Self |  | PopDetailsPanel |  |
| PopList | AccessSelf |  | PopList | 类别：常量 |
| PopList | GetAverageStandardOfLiving |  | CFixedPoint | 类别：非常量 |
| PopList | GetAverageStandardOfLivingLabel |  | CString | 类别：非常量 |
| PopList | GetBuildingContext |  | Building | 类别：非常量 |
| PopList | GetInterestGroupContext |  | InterestGroup | 类别：非常量 |
| PopList | GetItem0 |  | PopListItem | 类别：非常量 |
| PopList | GetItem1 |  | PopListItem | 类别：非常量 |
| PopList | GetItem2 |  | PopListItem | 类别：非常量 |
| PopList | GetItem3 |  | PopListItem | 类别：非常量 |
| PopList | GetItems |  | Unknown | 类别：非常量 |
| PopList | GetPoliticalMovementContext |  | PoliticalMovement | 类别：非常量 |
| PopList | GetPoliticalStrengthAsPercentage | Unknown | CFixedPoint | 类别：非常量 |
| PopList | GetTotalPoliticalStrength |  | int64 | 类别：非常量 |
| PopList | GetTotalPopulation |  | int64 | 类别：非常量 |
| PopList | HasBuildingContext |  | bool |  |
| PopList | HasInterestGroupContext |  | bool |  |
| PopList | HasPoliticalMovementContext |  | bool |  |
| PopList | Self |  | PopList |  |
| PopListItem | AccessPopType |  | PopType | 类别：常量 |
| PopListItem | AccessSelf |  | PopListItem | 类别：常量 |
| PopListItem | AccessTwoLargestIGs |  | Unknown | 类别：常量 |
| PopListItem | GetAverageAnnualWage |  | CFixedPoint | 类别：非常量 |
| PopListItem | GetAverageSoL |  | float | 类别：非常量 |
| PopListItem | GetDependentsPopSize |  | int64 | 类别：非常量 |
| PopListItem | GetEmploymentDesc |  | CString | 类别：非常量 |
| PopListItem | GetFirstPop |  | Pop | 类别：非常量 |
| PopListItem | GetNumLoyalists |  | int64 | 类别：非常量 |
| PopListItem | GetNumRadicals |  | int64 | 类别：非常量 |
| PopListItem | GetNumTotalPops |  | int32 | 类别：非常量 |
| PopListItem | GetPopType |  | PopType | 类别：非常量 |
| PopListItem | GetPops |  | Unknown | 类别：非常量 |
| PopListItem | GetTotalPolStr |  | int64 | 类别：非常量 |
| PopListItem | GetTotalPolStrPercentage |  | float | 类别：非常量 |
| PopListItem | GetTotalPoliticalMovementSupport |  | CFixedPoint | 类别：非常量 |
| PopListItem | GetTotalPopSize |  | int64 | 类别：非常量 |
| PopListItem | GetTotalPopSizePercentage |  | float | 类别：非常量 |
| PopListItem | GetWorkingAdultsPopSize |  | int64 | 类别：非常量 |
| PopListItem | IsAllPopsShown |  | bool |  |
| PopListItem | IsExpanded |  | bool |  |
| PopListItem | Self |  | PopListItem |  |
| PopListItem | ToggleExpand |  | void |  |
| PopNeed | AccessSelf |  | PopNeed | 类别：常量 |
| PopNeed | CalcBaseCost |  | CFixedPoint |  |
| PopNeed | CalcTotalCost |  | CFixedPoint |  |
| PopNeed | GetConsumptionDesc |  | CString | 类别：非常量 |
| PopNeed | GetDefaultGoods |  | Goods | 类别：非常量 |
| PopNeed | GetDesc |  | CString | 类别：非常量 |
| PopNeed | GetDetailsDesc |  | CString | 类别：非常量 |
| PopNeed | GetExpensesDesc |  | CString | 类别：非常量 |
| PopNeed | GetGoods |  | Unknown | 类别：非常量 |
| PopNeed | GetGoodsDesc |  | CString | 类别：非常量 |
| PopNeed | GetGoodsEquivalenceDesc | Unknown | CString | 类别：非常量 |
| PopNeed | GetName |  | CString | 类别：非常量 |
| PopNeed | GetNameNoFormatting |  | CString | 类别：非常量 |
| PopNeed | GetPop |  | Pop | 类别：非常量 |
| PopNeed | GetTooltipTag |  | CString | 类别：非常量 |
| PopNeed | Self |  | PopNeed |  |
| PopType | AccessSelf |  | PopType | 类别：常量 |
| PopType | GetColor |  | CVector4f | 类别：非常量 |
| PopType | GetCustom | CustomLocalization | CString | 类别：非常量 |
| PopType | GetDependents | Country | int64 | 类别：非常量 |
| PopType | GetDependentsAsPercentage | Country | CFixedPoint | 类别：非常量 |
| PopType | GetDesc |  | CString | 类别：非常量 |
| PopType | GetInterestGroupSupportDesc | Country | CString | 类别：非常量 |
| PopType | GetLoyalists | Country | int64 | 类别：非常量 |
| PopType | GetName |  | CString | 类别：非常量 |
| PopType | GetNameNoFormatting |  | CString | 类别：非常量 |
| PopType | GetNameNoIcon |  | CString | 类别：非常量 |
| PopType | GetNameNoIconNoFormatting |  | CString | 类别：非常量 |
| PopType | GetPolStr | Country | int64 | 类别：非常量 |
| PopType | GetPolStrAsFloat | Unknown | float | 类别：非常量 |
| PopType | GetPolStrAsPercentage | Country | CFixedPoint | 类别：非常量 |
| PopType | GetPopulation | Country | int64 | 类别：非常量 |
| PopType | GetPopulationAsFloat | Unknown | float | 类别：非常量 |
| PopType | GetPopulationAsPercentage | Country | CFixedPoint | 类别：非常量 |
| PopType | GetQualificationsGrowthDesc |  | CString | 类别：非常量 |
| PopType | GetRadicals | Country | int64 | 类别：非常量 |
| PopType | GetStateDependents | State | int64 | 类别：非常量 |
| PopType | GetStateDependentsAsPercentage | State | CFixedPoint | 类别：非常量 |
| PopType | GetStatePolStr | State | int64 | 类别：非常量 |
| PopType | GetStatePolStrAsFloat | Unknown | float | 类别：非常量 |
| PopType | GetStatePolStrAsPercentage | State | CFixedPoint | 类别：非常量 |
| PopType | GetStatePopulation | State | int64 | 类别：非常量 |
| PopType | GetStatePopulationAsFloat | Unknown | float | 类别：非常量 |
| PopType | GetStatePopulationAsPercentage | State | CFixedPoint | 类别：非常量 |
| PopType | GetStateWorkforce | State | int64 | 类别：非常量 |
| PopType | GetStateWorkforceAsPercentage | State | CFixedPoint | 类别：非常量 |
| PopType | GetStrataBreakdownInCountry | Country | CString | 类别：非常量 |
| PopType | GetTextIcon |  | CString | 类别：非常量 |
| PopType | GetTexture |  | Unknown | 类别：非常量 |
| PopType | GetTooltipTag |  | CString | 类别：非常量 |
| PopType | GetWorkforce | Country | int64 | 类别：非常量 |
| PopType | GetWorkforceAsPercentage | Country | CFixedPoint | 类别：非常量 |
| PopType | HasSubsistenceIncome |  | bool |  |
| PopType | IsPaidWages | Building | bool |  |
| PopType | IsSlave |  | bool |  |
| PopType | IsValid |  | bool |  |
| PopType | MakeScope |  | Scope |  |
| PopType | Self |  | PopType |  |
| PopWithIG | AccessSelf |  | PopWithIG | 类别：常量 |
| PopWithIG | CalcAttractionToIG |  | CFixedPoint |  |
| PopWithIG | GetAttractionToIGDesc |  | CString | 类别：非常量 |
| PopWithIG | GetInterestGroup |  | InterestGroup | 类别：非常量 |
| PopWithIG | GetPop |  | Pop | 类别：非常量 |
| PopWithIG | GetTooltipTag |  | CString | 类别：非常量 |
| PopWithIG | Self |  | PopWithIG |  |
| PopsOverviewPanel | AccessPops |  | Unknown | 类别：常量 |
| PopsOverviewPanel | AccessPopsList |  | PopList | 类别：常量 |
| PopsOverviewPanel | AccessSelf |  | PopsOverviewPanel | 类别：常量 |
| PopsOverviewPanel | GetAverageIncomeMiddle |  | CFixedPoint | 类别：非常量 |
| PopsOverviewPanel | GetAverageIncomePoor |  | CFixedPoint | 类别：非常量 |
| PopsOverviewPanel | GetAverageIncomeRich |  | CFixedPoint | 类别：非常量 |
| PopsOverviewPanel | GetGoodsExpenseItemsMiddle |  | Unknown | 类别：非常量 |
| PopsOverviewPanel | GetGoodsExpenseItemsPoor |  | Unknown | 类别：非常量 |
| PopsOverviewPanel | GetGoodsExpenseItemsRich |  | Unknown | 类别：非常量 |
| PopsOverviewPanel | GetGoodsExpensesMiddle |  | CFixedPoint | 类别：非常量 |
| PopsOverviewPanel | GetGoodsExpensesPoor |  | CFixedPoint | 类别：非常量 |
| PopsOverviewPanel | GetGoodsExpensesRich |  | CFixedPoint | 类别：非常量 |
| PopsOverviewPanel | GetIncomeRemainderMiddle |  | CFixedPoint | 类别：非常量 |
| PopsOverviewPanel | GetIncomeRemainderPoor |  | CFixedPoint | 类别：非常量 |
| PopsOverviewPanel | GetIncomeRemainderRich |  | CFixedPoint | 类别：非常量 |
| PopsOverviewPanel | GetTaxBurdenItemsMiddle |  | Unknown | 类别：非常量 |
| PopsOverviewPanel | GetTaxBurdenItemsPoor |  | Unknown | 类别：非常量 |
| PopsOverviewPanel | GetTaxBurdenItemsRich |  | Unknown | 类别：非常量 |
| PopsOverviewPanel | GetTaxBurdenMiddle |  | CFixedPoint | 类别：非常量 |
| PopsOverviewPanel | GetTaxBurdenPoor |  | CFixedPoint | 类别：非常量 |
| PopsOverviewPanel | GetTaxBurdenRich |  | CFixedPoint | 类别：非常量 |
| PopsOverviewPanel | Self |  | PopsOverviewPanel |  |
| PopulationGrouping | AccessInterestGroup |  | InterestGroup | 类别：常量 |
| PopulationGrouping | AccessSelf |  | PopulationGrouping | 类别：常量 |
| PopulationGrouping | GetGroupName |  | CString | 类别：非常量 |
| PopulationGrouping | GetInterestGroup |  | InterestGroup | 类别：非常量 |
| PopulationGrouping | GetSizeInPercentage |  | float | 类别：非常量 |
| PopulationGrouping | IsInterestGroup |  | bool |  |
| PopulationGrouping | Self |  | PopulationGrouping |  |
| PopupManager | AccessSelf |  | PopupManager | 类别：常量 |
| PopupManager | AnswerNo | ConfirmationWindow | void |  |
| PopupManager | AnswerYes | ConfirmationWindow | void |  |
| PopupManager | AskConfirmation | Command | void |  |
| PopupManager | AskConfirmationCustom | Command CString | void |  |
| PopupManager | AskConfirmationCustomWithSound | Command CString Sound | void |  |
| PopupManager | AskConfirmationWithSound | Command Sound | void |  |
| PopupManager | CloseGeneralInformationWindow |  | void |  |
| PopupManager | CloseMessage | PlayerMessageItem | void |  |
| PopupManager | ClosePopups |  | void |  |
| PopupManager | CloseProposal | Proposal | void |  |
| PopupManager | DeclineProposal | Proposal | void |  |
| PopupManager | ExecuteOrAskConfirmationIfNeeded | Command | void |  |
| PopupManager | ExecuteOrAskConfirmationIfNeededCustom | Unknown Unknown | void |  |
| PopupManager | ExecuteOrAskConfirmationIfNeededCustomWithSound | Unknown Unknown Unknown | void |  |
| PopupManager | ExecuteOrAskConfirmationIfNeededWithSound | Unknown Unknown | void |  |
| PopupManager | GetRecruitFormation |  | MilitaryFormation | 类别：非常量 |
| PopupManager | GetRecruitHQ |  | Hq | 类别：非常量 |
| PopupManager | Hide |  | void |  |
| PopupManager | HideCompanyChangeName |  | void |  |
| PopupManager | HideDiplomaticActionConfirmation |  | void |  |
| PopupManager | HideDiplomaticPlayConfirmation |  | void |  |
| PopupManager | HideInvasionPlannerPopup |  | void |  |
| PopupManager | HideMilitaryFormationChangeName |  | void |  |
| PopupManager | HideNationalizeBuildingWindow |  | void |  |
| PopupManager | HideOpenEvent | Event | void |  |
| PopupManager | HidePowerBlocCustomizationPopup |  | bool |  |
| PopupManager | HidePowerBlocPrincipleSelectionWindow |  | bool |  |
| PopupManager | HidePrestigeGoodChangeName |  | void |  |
| PopupManager | HideProposal | Unknown | void |  |
| PopupManager | HideRecruitAdmiral |  | bool |  |
| PopupManager | HideRecruitGeneral |  | bool |  |
| PopupManager | HideReleaseCountryConfirmation |  | void |  |
| PopupManager | HideRulerSelectionPopup |  | void |  |
| PopupManager | HideStateChangeName |  | void |  |
| PopupManager | HideTransferFormation |  | void |  |
| PopupManager | OpenAlert | Alert | void |  |
| PopupManager | OpenEvent | Event | void |  |
| PopupManager | OpenProposal | Proposal | void |  |
| PopupManager | Self |  | PopupManager |  |
| PopupManager | ShowCompanyChangeName | Company | void |  |
| PopupManager | ShowDiplomaticPlayConfirmation | Unknown Unknown Unknown Unknown | void |  |
| PopupManager | ShowInvasionPlannerPopup | Unknown | void |  |
| PopupManager | ShowMilitaryFormationChangeName | MilitaryFormation | void |  |
| PopupManager | ShowNationalizeBuildingWindow | Building | void |  |
| PopupManager | ShowPowerBlocCustomizationPopup | Unknown | void |  |
| PopupManager | ShowPowerBlocPrincipleSelectionWindow | Unknown Unknown | void |  |
| PopupManager | ShowPrestigeGoodChangeName | Goods | void |  |
| PopupManager | ShowReleaseCountryConfirmation | CountryCreation | void |  |
| PopupManager | ShowRulerSelectionPopup | Country | void |  |
| PopupManager | ShowStateChangeName | Unknown | void |  |
| PopupManager | ShowTransferFormation | MilitaryFormation | void |  |
| PopupManager | TogglePowerBlocCustomizationPopup |  | void |  |
| PopupManager | ToggleRecruitAdmiral | Unknown | bool |  |
| PopupManager | ToggleRecruitFormationAdmiral | MilitaryFormation | bool |  |
| PopupManager | ToggleRecruitFormationGeneral | MilitaryFormation | bool |  |
| PopupManager | ToggleRecruitGeneral | Unknown | bool |  |
| Portrait3dView | AccessSelf |  | Portrait3dView | 类别：常量 |
| Portrait3dView | GetAnimationTooltip |  | CString | 类别：非常量 |
| Portrait3dView | GetPortraitContext |  | Unknown | 类别：非常量 |
| Portrait3dView | GetPortraitEntity | int32 | Unknown | 类别：非常量 |
| Portrait3dView | SaveScreenshot |  | void |  |
| Portrait3dView | Self |  | Portrait3dView |  |
| PortraitDataContext | AccessSelf |  | PortraitDataContext | 类别：常量 |
| PortraitDataContext | GetName |  | CString | 类别：非常量 |
| PortraitDataContext | Self |  | PortraitDataContext |  |
| PortraitEditorAnimationItem | AccessSelf |  | PortraitEditorAnimationItem | 类别：常量 |
| PortraitEditorAnimationItem | GetName |  | CString | 类别：非常量 |
| PortraitEditorAnimationItem | Self |  | PortraitEditorAnimationItem |  |
| PortraitEditorWindow | AccessSelf |  | PortraitEditorWindow | 类别：常量 |
| PortraitEditorWindow | CanOptimize |  | bool |  |
| PortraitEditorWindow | GetAge |  | int32 | 类别：非常量 |
| PortraitEditorWindow | GetAgePercent |  | float | 类别：非常量 |
| PortraitEditorWindow | GetAnimationItems |  | Unknown | 类别：非常量 |
| PortraitEditorWindow | GetAnimationTooltip | CString | CString | 类别：非常量 |
| PortraitEditorWindow | GetCameraName |  | CString | 类别：非常量 |
| PortraitEditorWindow | GetCurrentAnimationFileDesc |  | CString | 类别：非常量 |
| PortraitEditorWindow | GetCurrentCameraFileDesc |  | CString | 类别：非常量 |
| PortraitEditorWindow | GetCurrentEnvironmentFileDesc |  | CString | 类别：非常量 |
| PortraitEditorWindow | GetCurrentEthnicityFileDesc |  | CString | 类别：非常量 |
| PortraitEditorWindow | GetCurrentGeneAccessoryString |  | CString | 类别：非常量 |
| PortraitEditorWindow | GetCurrentGeneFileDesc |  | CString | 类别：非常量 |
| PortraitEditorWindow | GetDNA |  | CString | 类别：非常量 |
| PortraitEditorWindow | GetEnvironmentName |  | CString | 类别：非常量 |
| PortraitEditorWindow | GetPortraitTexture | Unknown | Unknown | 类别：非常量 |
| PortraitEditorWindow | GetSelectedAnimationIndex |  | CVector2i | 类别：非常量 |
| PortraitEditorWindow | GetSelectedGeneTemplateColorX |  | float | 类别：非常量 |
| PortraitEditorWindow | GetSelectedGeneTemplateColorY |  | float | 类别：非常量 |
| PortraitEditorWindow | GetSelectedGeneTemplateStrength |  | float | 类别：非常量 |
| PortraitEditorWindow | GetSliderMaxValue |  | float | 类别：非常量 |
| PortraitEditorWindow | GetSliderMinValue |  | float | 类别：非常量 |
| PortraitEditorWindow | HasAnySliders |  | bool |  |
| PortraitEditorWindow | HasPoses |  | bool |  |
| PortraitEditorWindow | HasSubGenes |  | bool |  |
| PortraitEditorWindow | IsCurrentContentTab | CString | bool |  |
| PortraitEditorWindow | IsSelectedAccessoryGene |  | bool |  |
| PortraitEditorWindow | IsSelectedColorGene |  | bool |  |
| PortraitEditorWindow | IsSelectedMorphGene |  | bool |  |
| PortraitEditorWindow | IsSliderMode | Unknown | bool |  |
| PortraitEditorWindow | IsSliderPortraitType | Unknown | bool |  |
| PortraitEditorWindow | OnAgeChanged |  | void |  |
| PortraitEditorWindow | OnChangeAnimationItemLeft |  | void |  |
| PortraitEditorWindow | OnChangeAnimationItemRight |  | void |  |
| PortraitEditorWindow | OnChangeEthnicityLeft |  | void |  |
| PortraitEditorWindow | OnChangeEthnicityRight |  | void |  |
| PortraitEditorWindow | OnChangeGeneLeft |  | void |  |
| PortraitEditorWindow | OnChangeGeneRight |  | void |  |
| PortraitEditorWindow | OnChangePoseItemLeft |  | void |  |
| PortraitEditorWindow | OnChangePoseItemRight |  | void |  |
| PortraitEditorWindow | OnChangeSubGeneItemLeft |  | void |  |
| PortraitEditorWindow | OnChangeSubGeneItemRight |  | void |  |
| PortraitEditorWindow | OnCopyDNA |  | void |  |
| PortraitEditorWindow | OnCopyPersistentPortraitInfo | CString | void |  |
| PortraitEditorWindow | OnGenerateFromEthnicity |  | void |  |
| PortraitEditorWindow | OnGenerateFromEthnicityExcept |  | void |  |
| PortraitEditorWindow | OnNextCamera |  | void |  |
| PortraitEditorWindow | OnNextEnvironment |  | void |  |
| PortraitEditorWindow | OnPasteDNA |  | void |  |
| PortraitEditorWindow | OnPastePersistentPortraitInfo |  | void |  |
| PortraitEditorWindow | OnPreviousCamera |  | void |  |
| PortraitEditorWindow | OnPreviousEnvironment |  | void |  |
| PortraitEditorWindow | OnRandomizePortraitId |  | void |  |
| PortraitEditorWindow | OnReloadAssets |  | void |  |
| PortraitEditorWindow | OnReloadColorPalettes |  | void |  |
| PortraitEditorWindow | OnReloadDecals |  | void |  |
| PortraitEditorWindow | OnResetDNA |  | void |  |
| PortraitEditorWindow | OnRestartPortrait |  | void |  |
| PortraitEditorWindow | OnRunTextureOptimization |  | void |  |
| PortraitEditorWindow | Open3dView | CString | void |  |
| PortraitEditorWindow | OpenCurrentAnimationFile |  | void |  |
| PortraitEditorWindow | OpenCurrentCameraFile |  | void |  |
| PortraitEditorWindow | OpenCurrentEnvironmentFile |  | void |  |
| PortraitEditorWindow | OpenCurrentEthnicityFile |  | void |  |
| PortraitEditorWindow | OpenCurrentGeneFile |  | void |  |
| PortraitEditorWindow | ResetSliders |  | void |  |
| PortraitEditorWindow | Self |  | PortraitEditorWindow |  |
| PortraitEditorWindow | SetContentTab | CString | void |  |
| PortraitEditorWindow | SetSelectedAnimation |  | void |  |
| PortraitEditorWindow | SetSliderMode | CString | void |  |
| PortraitEditorWindow | SetSliderPortraitType | CString | void |  |
| PortraitTooltip | AccessSelf |  | PortraitTooltip | 类别：常量 |
| PortraitTooltip | Self |  | PortraitTooltip |  |
| PotentialLeaderIdeology | AccessSelf |  | PotentialLeaderIdeology | 类别：常量 |
| PotentialLeaderIdeology | GetChanceBreakdown |  | CString | 类别：非常量 |
| PotentialLeaderIdeology | GetChancePercentage |  | CFixedPoint | 类别：非常量 |
| PotentialLeaderIdeology | GetCharacterFirstName |  | CString | 类别：非常量 |
| PotentialLeaderIdeology | GetCharacterFullName |  | CString | 类别：非常量 |
| PotentialLeaderIdeology | HasCharacter |  | bool |  |
| PotentialLeaderIdeology | HasMovement |  | bool |  |
| PotentialLeaderIdeology | Self |  | PotentialLeaderIdeology |  |
| PowerBloc | AccessSelf |  | PowerBloc | 类别：常量 |
| PowerBloc | GetBattalions |  | int32 | 类别：非常量 |
| PowerBloc | GetBattalionsBreakdown |  | CString | 类别：非常量 |
| PowerBloc | GetCohesion |  | CFixedPoint | 类别：非常量 |
| PowerBloc | GetCohesionDesc |  | CString | 类别：非常量 |
| PowerBloc | GetCohesionLevel |  | CohesionLevel | 类别：非常量 |
| PowerBloc | GetCohesionTarget |  | CFixedPoint | 类别：非常量 |
| PowerBloc | GetCohesionWeeklyChange |  | CFixedPoint | 类别：非常量 |
| PowerBloc | GetConscriptableBattalions |  | int32 | 类别：非常量 |
| PowerBloc | GetCurrentMandateProgress |  | CFixedPoint | 类别：非常量 |
| PowerBloc | GetCurrentMandateProgressPercentage |  | CFixedPoint | 类别：非常量 |
| PowerBloc | GetCustom | CustomLocalization | CString | 类别：非常量 |
| PowerBloc | GetFlag |  | CoatOfArms | 类别：非常量 |
| PowerBloc | GetFlagTextIcon |  | CString | 类别：非常量 |
| PowerBloc | GetFlotillas |  | int32 | 类别：非常量 |
| PowerBloc | GetFlotillasBreakdown |  | CString | 类别：非常量 |
| PowerBloc | GetFoundingDate |  | Date | 类别：非常量 |
| PowerBloc | GetGdp |  | CFixedPoint | 类别：非常量 |
| PowerBloc | GetGdpDesc |  | CString | 类别：非常量 |
| PowerBloc | GetIdentity |  | PowerBlocIdentity | 类别：非常量 |
| PowerBloc | GetIndividualLeverage | Country | CFixedPoint | 类别：非常量 |
| PowerBloc | GetLeader |  | Country | 类别：非常量 |
| PowerBloc | GetLeaderModifier |  | Modifier | 类别：非常量 |
| PowerBloc | GetLeverageAdvantage | Country | CFixedPoint | 类别：非常量 |
| PowerBloc | GetLeverageAdvantageDesc | Country | CString | 类别：非常量 |
| PowerBloc | GetLeverageFactor | Unknown | CFixedPoint | 类别：非常量 |
| PowerBloc | GetLeverageFactorDesc | Unknown | CString | 类别：非常量 |
| PowerBloc | GetMapTexture |  | Unknown | 类别：非常量 |
| PowerBloc | GetMember | Unknown | Country | 类别：非常量 |
| PowerBloc | GetMemberWithUniqueHeadOfState | Unknown | Country | 类别：非常量 |
| PowerBloc | GetMembers |  | Unknown | 类别：非常量 |
| PowerBloc | GetMembersBreakdown |  | CString | 类别：非常量 |
| PowerBloc | GetMembersWithUniqueHeadsOfState |  | Unknown | 类别：非常量 |
| PowerBloc | GetModifier |  | Modifier | 类别：非常量 |
| PowerBloc | GetName |  | CString | 类别：非常量 |
| PowerBloc | GetNameNoFormatting |  | CString | 类别：非常量 |
| PowerBloc | GetNameNoIcon |  | CString | 类别：非常量 |
| PowerBloc | GetNextMandateDate |  | Date | 类别：非常量 |
| PowerBloc | GetNonLeaderModifier |  | Modifier | 类别：非常量 |
| PowerBloc | GetNumMandates |  | int32 | 类别：非常量 |
| PowerBloc | GetNumMembers |  | int32 | 类别：非常量 |
| PowerBloc | GetParticipantWithHighestInfamy |  | Country | 类别：非常量 |
| PowerBloc | GetParticipantWithHighestLeaderLawProgressivenessDifference |  | Country | 类别：非常量 |
| PowerBloc | GetParticipantWithHighestLibertyDesire |  | Country | 类别：非常量 |
| PowerBloc | GetParticipantWithLowestEconomicDependence |  | Country | 类别：非常量 |
| PowerBloc | GetParticipantWithLowestEconomicDependenceOnLeader |  | Country | 类别：非常量 |
| PowerBloc | GetParticipantWithLowestLeaderRelations |  | Country | 类别：非常量 |
| PowerBloc | GetParticipantWithLowestLeaderReligionPercentage |  | Country | 类别：非常量 |
| PowerBloc | GetPowerBlocStatue |  | PowerBlocStatue | 类别：非常量 |
| PowerBloc | GetPowerStruggleContender |  | Country | 类别：非常量 |
| PowerBloc | GetPowerStruggleDesc |  | CString | 类别：非常量 |
| PowerBloc | GetPrestigeDesc |  | CString | 类别：非常量 |
| PowerBloc | GetPreviousName |  | CString | 类别：非常量 |
| PowerBloc | GetPrimaryColor |  | CVector4f | 类别：非常量 |
| PowerBloc | GetPrincipleData | Unknown | PowerBlocPrincipleData | 类别：非常量 |
| PowerBloc | GetPrinciples |  | Unknown | 类别：非常量 |
| PowerBloc | GetRankFormatted |  | CString | 类别：非常量 |
| PowerBloc | GetRankRaw |  | int32 | 类别：非常量 |
| PowerBloc | GetRankTooltip |  | CString | 类别：非常量 |
| PowerBloc | GetRegularBattalions |  | int32 | 类别：非常量 |
| PowerBloc | GetRequestToJoin | Unknown | DiplomaticAction | 类别：非常量 |
| PowerBloc | GetTimedModifiers |  | Unknown | 类别：非常量 |
| PowerBloc | GetTooltip |  | CString | 类别：非常量 |
| PowerBloc | GetTooltipTag |  | CString | 类别：非常量 |
| PowerBloc | GetTotalPrestige |  | int32 | 类别：非常量 |
| PowerBloc | GetWeeklyMandateProgress |  | CFixedPoint | 类别：非常量 |
| PowerBloc | GetWeeklyMandateProgressDesc |  | CString | 类别：非常量 |
| PowerBloc | HasIdentity | PowerBlocIdentity | bool |  |
| PowerBloc | HasPendingInvitationForCountry | Country | bool |  |
| PowerBloc | HasPendingRequestToJoinFromCountry | Country | bool |  |
| PowerBloc | HasPrinciple | PowerBlocPrinciple | bool |  |
| PowerBloc | HasPrincipleFromGroup | Unknown | bool |  |
| PowerBloc | Invite | Country | Command |  |
| PowerBloc | IsActive |  | bool |  |
| PowerBloc | IsBeingHighlighted |  | bool |  |
| PowerBloc | IsBeingTutorialHighlighted |  | bool |  |
| PowerBloc | IsLeader | Country | bool |  |
| PowerBloc | IsMember | Country | bool |  |
| PowerBloc | IsPrincipleOnCooldown | PowerBlocPrinciple | bool |  |
| PowerBloc | IsRanked | int32 | bool |  |
| PowerBloc | IsValid |  | bool |  |
| PowerBloc | IsZoomingToMapMarkerPosition |  | bool |  |
| PowerBloc | Kick | Country | Command |  |
| PowerBloc | MakeScope |  | Scope |  |
| PowerBloc | MeetsPrimaryPrincipleRequirement |  | bool |  |
| PowerBloc | OpenPendingInvitationForCountry | Country | void |  |
| PowerBloc | PredictCohesionWithMember | Unknown | CFixedPoint |  |
| PowerBloc | RequestToJoin |  | Command |  |
| PowerBloc | Self |  | PowerBloc |  |
| PowerBloc | SortMembers | CString | void |  |
| PowerBloc | ZoomToMapMarkerPosition |  | void |  |
| PowerBlocCoaPiece | AccessSelf |  | PowerBlocCoaPiece | 类别：常量 |
| PowerBlocCoaPiece | GetCoa |  | CoatOfArms | 类别：非常量 |
| PowerBlocCoaPiece | GetIndex |  | int32 | 类别：非常量 |
| PowerBlocCoaPiece | GetKey |  | CString | 类别：非常量 |
| PowerBlocCoaPiece | GetName |  | CString | 类别：非常量 |
| PowerBlocCoaPiece | IsSelected |  | bool |  |
| PowerBlocCoaPiece | OnClicked |  | void |  |
| PowerBlocCoaPiece | Self |  | PowerBlocCoaPiece |  |
| PowerBlocCoaPieceSelector | AccessSelf |  | PowerBlocCoaPieceSelector | 类别：常量 |
| PowerBlocCoaPieceSelector | GetItems |  | Unknown | 类别：非常量 |
| PowerBlocCoaPieceSelector | GetName |  | CString | 类别：非常量 |
| PowerBlocCoaPieceSelector | GetSelectedItem |  | PowerBlocCoaPiece | 类别：非常量 |
| PowerBlocCoaPieceSelector | OnNextClicked |  | void |  |
| PowerBlocCoaPieceSelector | OnPreviousClicked |  | void |  |
| PowerBlocCoaPieceSelector | Self |  | PowerBlocCoaPieceSelector |  |
| PowerBlocCustomizationPopup | AccessSelf |  | PowerBlocCustomizationPopup | 类别：常量 |
| PowerBlocCustomizationPopup | AccessStatueAccessorySelectors |  | Unknown | 类别：常量 |
| PowerBlocCustomizationPopup | ConfirmClicked |  | void |  |
| PowerBlocCustomizationPopup | ConfirmGetDesc |  | CString |  |
| PowerBlocCustomizationPopup | ConfirmIsValid |  | bool |  |
| PowerBlocCustomizationPopup | DisableStatueMouseRotation |  | void |  |
| PowerBlocCustomizationPopup | EnableStatueMouseRotation |  | void |  |
| PowerBlocCustomizationPopup | GetCameraPosition |  | CVector3f | 类别：非常量 |
| PowerBlocCustomizationPopup | GetCoaPieces |  | Unknown | 类别：非常量 |
| PowerBlocCustomizationPopup | GetColorPickers |  | Unknown | 类别：非常量 |
| PowerBlocCustomizationPopup | GetCustomCoaPreview |  | CoatOfArms | 类别：非常量 |
| PowerBlocCustomizationPopup | GetEmblemColor |  | CVector4f | 类别：非常量 |
| PowerBlocCustomizationPopup | GetMapColor |  | CVector4f | 类别：非常量 |
| PowerBlocCustomizationPopup | GetMapTexture |  | Unknown | 类别：非常量 |
| PowerBlocCustomizationPopup | GetNewCustomName |  | CString | 类别：非常量 |
| PowerBlocCustomizationPopup | GetPowerBloc |  | PowerBloc | 类别：非常量 |
| PowerBlocCustomizationPopup | GetPowerBlocMapTextureSelector |  | PowerBlocMapTextureSelector | 类别：非常量 |
| PowerBlocCustomizationPopup | GetPrimaryColor |  | CVector4f | 类别：非常量 |
| PowerBlocCustomizationPopup | GetSecondaryColor |  | CVector4f | 类别：非常量 |
| PowerBlocCustomizationPopup | GetStatueHeroTypeOptions |  | Unknown | 类别：非常量 |
| PowerBlocCustomizationPopup | GetStatuePedestalTypeOptions |  | Unknown | 类别：非常量 |
| PowerBlocCustomizationPopup | OnEditName |  | void |  |
| PowerBlocCustomizationPopup | RandomizeName |  | void |  |
| PowerBlocCustomizationPopup | RandomizeStatue |  | void |  |
| PowerBlocCustomizationPopup | Self |  | PowerBlocCustomizationPopup |  |
| PowerBlocCustomizationPopup | SetNextStatueHeroType |  | void |  |
| PowerBlocCustomizationPopup | SetNextStatuePedestalType |  | void |  |
| PowerBlocCustomizationPopup | SetPrevStatueHeroType |  | void |  |
| PowerBlocCustomizationPopup | SetPrevStatuePedestalType |  | void |  |
| PowerBlocCustomizationPopup | SetStatueHeroType |  | void |  |
| PowerBlocCustomizationPopup | SetStatuePedestalType |  | void |  |
| PowerBlocFormation | AccessSelf |  | PowerBlocFormation | 类别：常量 |
| PowerBlocFormation | CanSelectPrinciple | Unknown Unknown | bool |  |
| PowerBlocFormation | Confirm |  | Command |  |
| PowerBlocFormation | GetCanSelectPrincipleDesc | Unknown Unknown | CString | 类别：非常量 |
| PowerBlocFormation | GetChosenName |  | CString | 类别：非常量 |
| PowerBlocFormation | GetConfirmedCustomCoaPreview |  | CoatOfArms | 类别：非常量 |
| PowerBlocFormation | GetIdentities |  | Unknown | 类别：非常量 |
| PowerBlocFormation | GetMapColor |  | CVector4f | 类别：非常量 |
| PowerBlocFormation | GetMapTexture |  | Unknown | 类别：非常量 |
| PowerBlocFormation | GetNumSelectedPrinciples |  | int32 | 类别：非常量 |
| PowerBlocFormation | GetPrinciplePointsCostRaw |  | int32 | 类别：非常量 |
| PowerBlocFormation | GetPrinciplePointsRemainingRaw |  | int32 | 类别：非常量 |
| PowerBlocFormation | GetPrincipleSlot | Unknown | PowerBlocFormationPrincipleSlot | 类别：非常量 |
| PowerBlocFormation | GetPrincipleSlots |  | Unknown | 类别：非常量 |
| PowerBlocFormation | GetPrinciples |  | Unknown | 类别：非常量 |
| PowerBlocFormation | HasSelectedPrimaryPrinciple |  | bool |  |
| PowerBlocFormation | HasSelectedPrinciple | Unknown | bool |  |
| PowerBlocFormation | HasSelectedPrincipleGroup | Unknown | bool |  |
| PowerBlocFormation | IsAnyIdentitySelected |  | bool |  |
| PowerBlocFormation | IsSelectedIdentity | PowerBlocIdentity | bool |  |
| PowerBlocFormation | RandomizeName |  | void |  |
| PowerBlocFormation | ResetPrinciples |  | void |  |
| PowerBlocFormation | SelectIdentity | PowerBlocIdentity | void |  |
| PowerBlocFormation | Self |  | PowerBlocFormation |  |
| PowerBlocFormationPanel | AccessSelf |  | PowerBlocFormationPanel | 类别：常量 |
| PowerBlocFormationPanel | GetPowerBlocFormation |  | PowerBlocFormation | 类别：非常量 |
| PowerBlocFormationPanel | OnEditName |  | void |  |
| PowerBlocFormationPanel | Self |  | PowerBlocFormationPanel |  |
| PowerBlocFormationPanel | ToggleSelectPowerBlocIdentityMenu | Unknown | void |  |
| PowerBlocFormationPrincipleSlot | AccessSelf |  | PowerBlocFormationPrincipleSlot | 类别：常量 |
| PowerBlocFormationPrincipleSlot | IsActive |  | bool |  |
| PowerBlocFormationPrincipleSlot | IsAnyPrincipleSelected |  | bool |  |
| PowerBlocFormationPrincipleSlot | IsChangingPrinciple |  | bool |  |
| PowerBlocFormationPrincipleSlot | IsNext |  | bool |  |
| PowerBlocFormationPrincipleSlot | IsSelectedPrinciple | Unknown | bool |  |
| PowerBlocFormationPrincipleSlot | IsUnlocked |  | bool |  |
| PowerBlocFormationPrincipleSlot | OnAnimationFinished |  | void |  |
| PowerBlocFormationPrincipleSlot | RemovePrinciple |  | void |  |
| PowerBlocFormationPrincipleSlot | Self |  | PowerBlocFormationPrincipleSlot |  |
| PowerBlocIdentity | AccessSelf |  | PowerBlocIdentity | 类别：常量 |
| PowerBlocIdentity | GetBackground |  | Unknown | 类别：非常量 |
| PowerBlocIdentity | GetCustom | CustomLocalization | CString | 类别：非常量 |
| PowerBlocIdentity | GetDesc |  | CString | 类别：非常量 |
| PowerBlocIdentity | GetIcon |  | Unknown | 类别：非常量 |
| PowerBlocIdentity | GetIsPossibleDesc |  | CString | 类别：非常量 |
| PowerBlocIdentity | GetLeaderEffectDesc |  | CString | 类别：非常量 |
| PowerBlocIdentity | GetMemberEffectDesc |  | CString | 类别：非常量 |
| PowerBlocIdentity | GetName |  | CString | 类别：非常量 |
| PowerBlocIdentity | GetNameNoFormatting |  | CString | 类别：非常量 |
| PowerBlocIdentity | GetNonLeaderEffectDesc |  | CString | 类别：非常量 |
| PowerBlocIdentity | GetOnCreatedEffectDesc | Unknown | CString | 类别：非常量 |
| PowerBlocIdentity | GetPowerBlocEffectDesc |  | CString | 类别：非常量 |
| PowerBlocIdentity | GetPrimaryPrincipleGroups |  | Unknown | 类别：非常量 |
| PowerBlocIdentity | GetPrinciplesDesc |  | CString | 类别：非常量 |
| PowerBlocIdentity | GetProductionMethodsDesc |  | CString | 类别：非常量 |
| PowerBlocIdentity | GetTooltipTag |  | CString | 类别：非常量 |
| PowerBlocIdentity | GetUnlockedPrincipleGroups |  | Unknown | 类别：非常量 |
| PowerBlocIdentity | IsPossible |  | bool |  |
| PowerBlocIdentity | MakeScope |  | Scope |  |
| PowerBlocIdentity | Self |  | PowerBlocIdentity |  |
| PowerBlocMapTexture | AccessSelf |  | PowerBlocMapTexture | 类别：常量 |
| PowerBlocMapTexture | GetColor |  | CVector4f | 类别：非常量 |
| PowerBlocMapTexture | GetIndex |  | int32 | 类别：非常量 |
| PowerBlocMapTexture | GetKey |  | CString | 类别：非常量 |
| PowerBlocMapTexture | GetName |  | CString | 类别：非常量 |
| PowerBlocMapTexture | GetTexture |  | Unknown | 类别：非常量 |
| PowerBlocMapTexture | GetTooltipTag |  | CString | 类别：非常量 |
| PowerBlocMapTexture | IsSelected |  | bool |  |
| PowerBlocMapTexture | OnClicked |  | void |  |
| PowerBlocMapTexture | Self |  | PowerBlocMapTexture |  |
| PowerBlocMapTextureSelector | AccessSelf |  | PowerBlocMapTextureSelector | 类别：常量 |
| PowerBlocMapTextureSelector | GetItems |  | Unknown | 类别：非常量 |
| PowerBlocMapTextureSelector | GetSelectedItem |  | PowerBlocMapTexture | 类别：非常量 |
| PowerBlocMapTextureSelector | OnNextClicked |  | void |  |
| PowerBlocMapTextureSelector | OnPreviousClicked |  | void |  |
| PowerBlocMapTextureSelector | Self |  | PowerBlocMapTextureSelector |  |
| PowerBlocPanel | AccessSelf |  | PowerBlocPanel | 类别：常量 |
| PowerBlocPanel | GetNumInvitableCountries |  | int32 | 类别：非常量 |
| PowerBlocPanel | GetPrincipleSlot | Unknown | PowerBlocPrincipleSlot | 类别：非常量 |
| PowerBlocPanel | GetSelectedPowerBloc |  | PowerBloc | 类别：非常量 |
| PowerBlocPanel | IsPowerBlocSelected |  | bool |  |
| PowerBlocPanel | OnClickInviteCountries |  | void |  |
| PowerBlocPanel | Self |  | PowerBlocPanel |  |
| PowerBlocPanel | ToggleFormationSelectionWindow | PowerBlocFormationPrincipleSlot | void |  |
| PowerBlocPanel | ToggleSelectionWindow | PowerBlocPrincipleSlot | void |  |
| PowerBlocPrinciple | AccessSelf |  | PowerBlocPrinciple | 类别：常量 |
| PowerBlocPrinciple | GetBackground |  | Unknown | 类别：非常量 |
| PowerBlocPrinciple | GetBuildingTypesDesc |  | CString | 类别：非常量 |
| PowerBlocPrinciple | GetCompanyTypesDesc |  | CString | 类别：非常量 |
| PowerBlocPrinciple | GetCustom | CustomLocalization | CString | 类别：非常量 |
| PowerBlocPrinciple | GetDesc |  | CString | 类别：非常量 |
| PowerBlocPrinciple | GetGroup |  | PowerBlocPrincipleGroup | 类别：非常量 |
| PowerBlocPrinciple | GetIcon |  | Unknown | 类别：非常量 |
| PowerBlocPrinciple | GetIncompatibilitiesDesc |  | CString | 类别：非常量 |
| PowerBlocPrinciple | GetInstitutionEffectDesc |  | CString | 类别：非常量 |
| PowerBlocPrinciple | GetIsPossibleDesc |  | CString | 类别：非常量 |
| PowerBlocPrinciple | GetIsPossibleTriggerDesc |  | CString | 类别：非常量 |
| PowerBlocPrinciple | GetLeaderEffectDesc |  | CString | 类别：非常量 |
| PowerBlocPrinciple | GetMemberEffectDesc |  | CString | 类别：非常量 |
| PowerBlocPrinciple | GetMobilizationOptionsDesc |  | CString | 类别：非常量 |
| PowerBlocPrinciple | GetName |  | CString | 类别：非常量 |
| PowerBlocPrinciple | GetNameNoFormatting |  | CString | 类别：非常量 |
| PowerBlocPrinciple | GetNonLeaderEffectDesc |  | CString | 类别：非常量 |
| PowerBlocPrinciple | GetPowerBlocEffectDesc |  | CString | 类别：非常量 |
| PowerBlocPrinciple | GetProductionMethodsDesc |  | CString | 类别：非常量 |
| PowerBlocPrinciple | GetTooltipTag |  | CString | 类别：非常量 |
| PowerBlocPrinciple | IsPossible |  | bool |  |
| PowerBlocPrinciple | MakeScope |  | Scope |  |
| PowerBlocPrinciple | Self |  | PowerBlocPrinciple |  |
| PowerBlocPrinciple | UpgradeToNextLevel |  | Command |  |
| PowerBlocPrincipleData | AccessSelf |  | PowerBlocPrincipleData | 类别：常量 |
| PowerBlocPrincipleData | GetCooldownDate |  | Date | 类别：非常量 |
| PowerBlocPrincipleData | GetSelectionDate |  | Date | 类别：非常量 |
| PowerBlocPrincipleData | GetTooltipTag |  | CString | 类别：非常量 |
| PowerBlocPrincipleData | Self |  | PowerBlocPrincipleData |  |
| PowerBlocPrincipleGroup | AccessSelf |  | PowerBlocPrincipleGroup | 类别：常量 |
| PowerBlocPrincipleGroup | GetCustom | CustomLocalization | CString | 类别：非常量 |
| PowerBlocPrincipleGroup | GetDesc |  | CString | 类别：非常量 |
| PowerBlocPrincipleGroup | GetLevels |  | Unknown | 类别：非常量 |
| PowerBlocPrincipleGroup | GetLevelsDesc |  | CString | 类别：非常量 |
| PowerBlocPrincipleGroup | GetName |  | CString | 类别：非常量 |
| PowerBlocPrincipleGroup | GetNameNoFormatting |  | CString | 类别：非常量 |
| PowerBlocPrincipleGroup | GetTooltipTag |  | CString | 类别：非常量 |
| PowerBlocPrincipleGroup | IsPrimaryFor | PowerBlocIdentity | bool |  |
| PowerBlocPrincipleGroup | MakeScope |  | Scope |  |
| PowerBlocPrincipleGroup | Self |  | PowerBlocPrincipleGroup |  |
| PowerBlocPrincipleSelectionWindow | AccessSelf |  | PowerBlocPrincipleSelectionWindow | 类别：常量 |
| PowerBlocPrincipleSelectionWindow | CanAffordPrinciple | PowerBlocPrinciple | bool |  |
| PowerBlocPrincipleSelectionWindow | CanSelectPrinciple | PowerBlocPrinciple | bool |  |
| PowerBlocPrincipleSelectionWindow | GetAvailableGroups |  | Unknown | 类别：非常量 |
| PowerBlocPrincipleSelectionWindow | GetDescForPrincipleSelection | PowerBlocPrinciple | CString | 类别：非常量 |
| PowerBlocPrincipleSelectionWindow | GetMandateCostDescForSelectedPrinciple |  | CString | 类别：非常量 |
| PowerBlocPrincipleSelectionWindow | GetMandateCostForSelectedPrinciple |  | int32 | 类别：非常量 |
| PowerBlocPrincipleSelectionWindow | GetNumMandates |  | int32 | 类别：非常量 |
| PowerBlocPrincipleSelectionWindow | GetPotentialGroups |  | Unknown | 类别：非常量 |
| PowerBlocPrincipleSelectionWindow | GetPowerBloc |  | PowerBloc | 类别：非常量 |
| PowerBlocPrincipleSelectionWindow | GetPowerBlocFormation |  | PowerBlocFormation | 类别：非常量 |
| PowerBlocPrincipleSelectionWindow | GetReplacedPrinciple |  | PowerBlocPrinciple | 类别：非常量 |
| PowerBlocPrincipleSelectionWindow | GetSelectedPrinciple |  | PowerBlocPrinciple | 类别：非常量 |
| PowerBlocPrincipleSelectionWindow | HasPrinciple | Unknown | bool |  |
| PowerBlocPrincipleSelectionWindow | HasPrincipleFromGroup | Unknown | bool |  |
| PowerBlocPrincipleSelectionWindow | HasSelectedPrimaryPrinciple |  | bool |  |
| PowerBlocPrincipleSelectionWindow | HasSelectedPrinciple |  | bool |  |
| PowerBlocPrincipleSelectionWindow | IsPowerBlocFormation |  | bool |  |
| PowerBlocPrincipleSelectionWindow | IsReplacedPrinciple | PowerBlocPrinciple | bool |  |
| PowerBlocPrincipleSelectionWindow | IsReplacingPrinciple |  | bool |  |
| PowerBlocPrincipleSelectionWindow | IsSelectedPrinciple | PowerBlocPrinciple | bool |  |
| PowerBlocPrincipleSelectionWindow | IsUpgradingPrinciple |  | bool |  |
| PowerBlocPrincipleSelectionWindow | Self |  | PowerBlocPrincipleSelectionWindow |  |
| PowerBlocPrincipleSelectionWindow | SubmitFormationPrincipleSelection |  | void |  |
| PowerBlocPrincipleSelectionWindow | SubmitPrincipleSelection |  | Command |  |
| PowerBlocPrincipleSelectionWindow | TogglePrincipleSelection | PowerBlocPrinciple | void |  |
| PowerBlocPrincipleSlot | AccessSelf |  | PowerBlocPrincipleSlot | 类别：常量 |
| PowerBlocPrincipleSlot | GetPrinciple |  | PowerBlocPrinciple | 类别：非常量 |
| PowerBlocPrincipleSlot | GetUnlockDesc |  | CString | 类别：非常量 |
| PowerBlocPrincipleSlot | IsActive |  | bool |  |
| PowerBlocPrincipleSlot | IsChangingPrinciple |  | bool |  |
| PowerBlocPrincipleSlot | IsNext |  | bool |  |
| PowerBlocPrincipleSlot | IsUnlocked |  | bool |  |
| PowerBlocPrincipleSlot | OnAnimationFinished |  | void |  |
| PowerBlocPrincipleSlot | Self |  | PowerBlocPrincipleSlot |  |
| PowerBlocStatue | AccessSelf |  | PowerBlocStatue | 类别：常量 |
| PowerBlocStatue | GetEntity | PdxGuiWidget | Unknown | 类别：非常量 |
| PowerBlocStatue | GetTooltipTag |  | CString | 类别：非常量 |
| PowerBlocStatue | Self |  | PowerBlocStatue |  |
| PowerBlocStatueAccessoryType | AccessSelf |  | PowerBlocStatueAccessoryType | 类别：常量 |
| PowerBlocStatueAccessoryType | GetEntity |  | CString | 类别：非常量 |
| PowerBlocStatueAccessoryType | GetName |  | CString | 类别：非常量 |
| PowerBlocStatueAccessoryType | GetTooltipTag |  | CString | 类别：非常量 |
| PowerBlocStatueAccessoryType | Self |  | PowerBlocStatueAccessoryType |  |
| PowerBlocStatueAccessoryTypeSelector | AccessSelf |  | PowerBlocStatueAccessoryTypeSelector | 类别：常量 |
| PowerBlocStatueAccessoryTypeSelector | GetName |  | CString | 类别：非常量 |
| PowerBlocStatueAccessoryTypeSelector | GetStatueAccessoryTypeOptions |  | Unknown | 类别：非常量 |
| PowerBlocStatueAccessoryTypeSelector | Self |  | PowerBlocStatueAccessoryTypeSelector |  |
| PowerBlocStatueAccessoryTypeSelector | SetNextStatueAccessoryType |  | void |  |
| PowerBlocStatueAccessoryTypeSelector | SetPrevStatueAccessoryType |  | void |  |
| PowerBlocStatueAccessoryTypeSelector | SetStatueAccessoryType |  | void |  |
| PowerBlocStatueHeroType | AccessSelf |  | PowerBlocStatueHeroType | 类别：常量 |
| PowerBlocStatueHeroType | GetEntity |  | CString | 类别：非常量 |
| PowerBlocStatueHeroType | GetName |  | CString | 类别：非常量 |
| PowerBlocStatueHeroType | GetTooltipTag |  | CString | 类别：非常量 |
| PowerBlocStatueHeroType | Self |  | PowerBlocStatueHeroType |  |
| PowerBlocStatuePedestalType | AccessSelf |  | PowerBlocStatuePedestalType | 类别：常量 |
| PowerBlocStatuePedestalType | GetEntity |  | CString | 类别：非常量 |
| PowerBlocStatuePedestalType | GetName |  | CString | 类别：非常量 |
| PowerBlocStatuePedestalType | GetTooltipTag |  | CString | 类别：非常量 |
| PowerBlocStatuePedestalType | Self |  | PowerBlocStatuePedestalType |  |
| PrestigeGoodChangeNamePopup | AccessSelf |  | PrestigeGoodChangeNamePopup | 类别：常量 |
| PrestigeGoodChangeNamePopup | Confirm |  | Command |  |
| PrestigeGoodChangeNamePopup | GetPrestigeGood |  | Goods | 类别：非常量 |
| PrestigeGoodChangeNamePopup | OnEditName |  | void |  |
| PrestigeGoodChangeNamePopup | Self |  | PrestigeGoodChangeNamePopup |  |
| PreviewMaskTexture | AccessSelf |  | PreviewMaskTexture | 类别：常量 |
| PreviewMaskTexture | GetOpacity |  | float | 类别：非常量 |
| PreviewMaskTexture | Self |  | PreviewMaskTexture |  |
| PreviewMaskTexture | SetOpacity |  | void |  |
| PreviewMaskTexture | SetOpacityStr |  | void |  |
| ProductionMarker | AccessSelf |  | ProductionMarker | 类别：常量 |
| ProductionMarker | AccessState |  | State | 类别：常量 |
| ProductionMarker | AccessTopItems |  | Unknown | 类别：常量 |
| ProductionMarker | GetPosition |  | CVector2f | 类别：非常量 |
| ProductionMarker | Self |  | ProductionMarker |  |
| ProductionMethod | AccessSelf |  | ProductionMethod | 类别：常量 |
| ProductionMethod | GetBuildingTypesUsingThisDesc | Country | CString | 类别：非常量 |
| ProductionMethod | GetCompactEmploymentSummaryDesc |  | CString | 类别：非常量 |
| ProductionMethod | GetCompactGoodsSummaryDesc |  | CString | 类别：非常量 |
| ProductionMethod | GetKey |  | CString | 类别：非常量 |
| ProductionMethod | GetName |  | CString | 类别：非常量 |
| ProductionMethod | GetNameNoFormatting |  | CString | 类别：非常量 |
| ProductionMethod | GetNumOfBuildingsUsingThis | Country | int32 | 类别：非常量 |
| ProductionMethod | GetSwitch | Unknown | Command | 类别：非常量 |
| ProductionMethod | GetTexture |  | Unknown | 类别：非常量 |
| ProductionMethod | GetTooltip | Country | CString | 类别：非常量 |
| ProductionMethod | GetTooltipForBuilding | Country Building | CString | 类别：非常量 |
| ProductionMethod | GetTooltipTag |  | CString | 类别：非常量 |
| ProductionMethod | GetTooltipWithoutRequirements | Unknown Unknown | CString | 类别：非常量 |
| ProductionMethod | IsHiddenWhenUnavailable |  | bool |  |
| ProductionMethod | Self |  | ProductionMethod |  |
| ProductionMethodConfirmationPopup | AccessSelf |  | ProductionMethodConfirmationPopup | 类别：常量 |
| 类型 | 函数 | 参数 | 输出 | 描述 |
|---|---|---|---|---|
| ProductionMethodConfirmationPopup | CanExempt |  | bool |  |
| ProductionMethodConfirmationPopup | Cancel |  | void |  |
| ProductionMethodConfirmationPopup | Continue |  | void |  |
| ProductionMethodConfirmationPopup | Exempt |  | void |  |
| ProductionMethodConfirmationPopup | GetExemptedBuildingCount |  | int32 | 类别：非 const |
| ProductionMethodConfirmationPopup | GetLowProductivityBreakdown |  | CString | 类别：非 const |
| ProductionMethodConfirmationPopup | GetTotalBuildingCount |  | int32 | 类别：非 const |
| ProductionMethodConfirmationPopup | Self |  | ProductionMethodConfirmationPopup |  |
| ProductionMethodGroup | AccessBuildingProductionMethods | Building | Unknown | 类别：const |
| ProductionMethodGroup | AccessCountryProductionMethods | Country | Unknown | 类别：const |
| ProductionMethodGroup | AccessSelf |  | ProductionMethodGroup | 类别：const |
| ProductionMethodGroup | GetKey |  | CString | 类别：非 const |
| ProductionMethodGroup | GetMixedIcon |  | Unknown | 类别：非 const |
| ProductionMethodGroup | GetName |  | CString | 类别：非 const |
| ProductionMethodGroup | GetNumAvailableOptions | Building | int32 | 类别：非 const |
| ProductionMethodGroup | GetNumAvailableOptionsForBuildingType | BuildingType | int32 | 类别：非 const |
| ProductionMethodGroup | GetTooltipTag |  | CString | 类别：非 const |
| ProductionMethodGroup | Self |  | ProductionMethodGroup |  |
| ProgressInterface | AccessSelf |  | ProgressInterface | 类别：const |
| ProgressInterface | GetProgress |  | CString | 类别：非 const |
| ProgressInterface | Self |  | ProgressInterface |  |
| PropertyListCategory | AccessSelf |  | PropertyListCategory | 类别：const |
| PropertyListCategory | GetMargin |  | int32 | 类别：非 const |
| PropertyListCategory | GetName |  | CString | 类别：非 const |
| PropertyListCategory | IsEmpty |  | bool |  |
| PropertyListCategory | IsExpanded |  | bool |  |
| PropertyListCategory | IsRoot |  | bool |  |
| PropertyListCategory | Self |  | PropertyListCategory |  |
| PropertyListCategory | ToggleExpanded |  | void |  |
| PropertyListCategory | ToggleTreeExpanded |  | void |  |
| Proposal | AccessSelf |  | Proposal | 类别：const |
| Proposal | AccessTimeoutTimer |  | PieTimer | 类别：const |
| Proposal | GetActor |  | Country | 类别：非 const |
| Proposal | GetDescription |  | CString | 类别：非 const |
| Proposal | GetDiplomaticAction |  | DiplomaticAction | 类别：非 const |
| Proposal | GetDiplomaticDemand |  | DiplomaticDemand | 类别：非 const |
| Proposal | GetDiplomaticPlay |  | DiplomaticPlay | 类别：非 const |
| Proposal | GetName |  | CString | 类别：非 const |
| Proposal | GetRecipient |  | Country | 类别：非 const |
| Proposal | GetTarget |  | Country | 类别：非 const |
| Proposal | GetTexture |  | Unknown | 类别：非 const |
| Proposal | GetToolTip |  | CString | 类别：非 const |
| Proposal | GetTooltipTag |  | CString | 类别：非 const |
| Proposal | GetTreaty |  | Treaty | 类别：非 const |
| Proposal | IsHidden |  | bool |  |
| Proposal | MarkAsHidden |  | void |  |
| Proposal | Self |  | Proposal |  |
| Proposal | Unhide |  | void |  |
| Province | AccessSelf |  | Province | 类别：const |
| Province | AccessStateRegion |  | StateRegion | 类别：const |
| Province | GetArea |  | int32 | 类别：非 const |
| Province | GetBestTexture |  | Unknown | 类别：非 const |
| Province | GetController |  | Country | 类别：非 const |
| Province | GetCustom | CustomLocalization | CString | 类别：非 const |
| Province | GetDeploySelectedFormationsCommand |  | Command | 类别：非 const |
| Province | GetID |  | CString | 类别：非 const |
| Province | GetIndex |  | int32 | 类别：非 const |
| Province | GetScreenPosition |  | CVector2f | 类别：非 const |
| Province | GetSeaNodeName |  | CString | 类别：非 const |
| Province | GetState |  | State | 类别：非 const |
| Province | GetStateRegion |  | StateRegion | 类别：非 const |
| Province | GetTerrainCombatWidth |  | CFixedPoint | 类别：非 const |
| Province | GetTerrainName |  | CString | 类别：非 const |
| Province | GetTooltipTag |  | CString | 类别：非 const |
| Province | IsCoastal |  | bool |  |
| Province | MakeScope |  | Scope |  |
| Province | Self |  | Province |  |
| RandomizableValueFloat | AccessSelf |  | RandomizableValueFloat | 类别：const |
| RandomizableValueFloat | GetValue |  | float | 类别：非 const |
| RandomizableValueFloat | Randomize |  | void |  |
| RandomizableValueFloat | Self |  | RandomizableValueFloat |  |
| RandomizableValueFloat | SetValue |  | void |  |
| RandomizableValueInt | AccessSelf |  | RandomizableValueInt | 类别：const |
| RandomizableValueInt | GetValue |  | int32 | 类别：非 const |
| RandomizableValueInt | Randomize |  | void |  |
| RandomizableValueInt | Self |  | RandomizableValueInt |  |
| RandomizableValueInt | SetValue |  | void |  |
| ReformGovernment | AccessSelf |  | ReformGovernment | 类别：const |
| ReformGovernment | Confirm |  | Command |  |
| ReformGovernment | GetAllPotentialInterestGroups |  | Unknown | 类别：非 const |
| ReformGovernment | GetAllPotentialParties |  | Unknown | 类别：非 const |
| ReformGovernment | GetAllStagedInterestGroups |  | Unknown | 类别：非 const |
| ReformGovernment | GetAllStagedParties |  | Unknown | 类别：非 const |
| ReformGovernment | GetConfirmDesc |  | CString | 类别：非 const |
| ReformGovernment | GetCountry |  | Country | 类别：非 const |
| ReformGovernment | GetIndependentPotentialInterestGroups |  | Unknown | 类别：非 const |
| ReformGovernment | GetIndependentStagedInterestGroups |  | Unknown | 类别：非 const |
| ReformGovernment | GetLegitimacy |  | int32 | 类别：非 const |
| ReformGovernment | GetLegitimacyDesc |  | CString | 类别：非 const |
| ReformGovernment | GetLegitimacyLevel |  | LegitimacyLevel | 类别：非 const |
| ReformGovernment | GetOptionIndexText | int32 | CString | 类别：非 const |
| ReformGovernment | GetOptionIndexTooltip | int32 | CString | 类别：非 const |
| ReformGovernment | GetPredictedLawsWithGovernmentOrMovementSupport |  | Unknown | 类别：非 const |
| ReformGovernment | GetPredictedLawsWithGovernmentOrMovementSupportHeader |  | CString | 类别：非 const |
| ReformGovernment | GetPredictedLawsWithoutGovernmentOrMovementSupport |  | Unknown | 类别：非 const |
| ReformGovernment | GetPredictedLawsWithoutGovernmentOrMovementSupportHeader |  | CString | 类别：非 const |
| ReformGovernment | GetPredictedLegitimacy |  | int32 | 类别：非 const |
| ReformGovernment | GetPredictedLegitimacyDelta |  | int32 | 类别：非 const |
| ReformGovernment | GetPredictedLegitimacyDesc |  | CString | 类别：非 const |
| ReformGovernment | GetPredictedLegitimacyLevel |  | LegitimacyLevel | 类别：非 const |
| ReformGovernment | GetPredictedLoyalistsDelta |  | int64 | 类别：非 const |
| ReformGovernment | GetPredictedNewRuler | Unknown | Character | 类别：非 const |
| ReformGovernment | GetPredictedRadicalsDelta |  | int64 | 类别：非 const |
| ReformGovernment | HasMadeAnyChanges |  | bool |  |
| ReformGovernment | HasPredictedLawsWithGovernmentOrMovementSupportChanged |  | bool |  |
| ReformGovernment | HasPredictedLawsWithoutGovernmentOrMovementSupportChanged |  | bool |  |
| ReformGovernment | HasStagedGroup |  | bool |  |
| ReformGovernment | OptionIndexIsActiveGovernment | Unknown | bool |  |
| ReformGovernment | OptionIndexIsSelected | int32 | bool |  |
| ReformGovernment | OptionIndexIsValid | int32 | bool |  |
| ReformGovernment | Reset |  | void |  |
| ReformGovernment | SelectOptionIndex | int32 | void |  |
| ReformGovernment | Self |  | ReformGovernment |  |
| ReformGovernment | StageInterestGroup | InterestGroup | void |  |
| ReformGovernment | StageParty | Party | void |  |
| ReformGovernment | UnstageInterestGroup | InterestGroup | void |  |
| ReformGovernment | UnstageParty | Party | void |  |
| ReformGovernment | WouldGetNewRuler |  | bool |  |
| ReleaseCountryWindow | AccessCountryCreation |  | CountryCreation | 类别：const |
| ReleaseCountryWindow | AccessSelf |  | ReleaseCountryWindow | 类别：const |
| ReleaseCountryWindow | CanMakeIndependent |  | bool |  |
| ReleaseCountryWindow | CanMakeOwnSubject |  | bool |  |
| ReleaseCountryWindow | CanPlayAsReleased |  | bool |  |
| ReleaseCountryWindow | CanReleaseWithKeepHomelandStates |  | bool |  |
| ReleaseCountryWindow | GetCountryCreation |  | CountryCreation | 类别：非 const |
| ReleaseCountryWindow | GetKeepHomelandStatesTooltip |  | CString | 类别：非 const |
| ReleaseCountryWindow | GetMakeIndependentTooltip |  | CString | 类别：非 const |
| ReleaseCountryWindow | GetMakeOwnSubjectTooltip |  | CString | 类别：非 const |
| ReleaseCountryWindow | GetPlayAsReleasedTooltip |  | CString | 类别：非 const |
| ReleaseCountryWindow | GetPopupQuestion |  | CString | 类别：非 const |
| ReleaseCountryWindow | ReleaseCountry |  | Command |  |
| ReleaseCountryWindow | Self |  | ReleaseCountryWindow |  |
| ReleaseCountryWindow | SubjectTypeToMakeOwnSubjectExists |  | bool |  |
| ReleaseCountryWindow | ToggleKeepHomelandStates |  | void |  |
| ReleaseCountryWindow | ToggleMakeIndependent |  | void |  |
| ReleaseCountryWindow | ToggleMakeOwnSubject |  | void |  |
| ReleaseCountryWindow | TogglePlayAsReleased |  | void |  |
| ReleaseCountryWindow | WillKeepHomelandStates |  | bool |  |
| ReleaseCountryWindow | WillMakeIndependent |  | bool |  |
| ReleaseCountryWindow | WillMakeOwnSubject |  | bool |  |
| ReleaseCountryWindow | WillPlayAsReleased |  | bool |  |
| Religion | AccessSelf |  | Religion | 类别：const |
| Religion | GetAcceptanceDescIn | Country | CString | 类别：非 const |
| Religion | GetAcceptanceIn | Country | int32 | 类别：非 const |
| Religion | GetAcceptanceStatusSegmentsIn | Country | Unknown | 类别：非 const |
| Religion | GetColor |  | CVector4f | 类别：非 const |
| Religion | GetCustom | CustomLocalization | CString | 类别：非 const |
| Religion | GetDependents | Country | int64 | 类别：非 const |
| Religion | GetDependentsAsPercentage | Country | CFixedPoint | 类别：非 const |
| Religion | GetDesc |  | CString | 类别：非 const |
| Religion | GetIcon |  | Unknown | 类别：非 const |
| Religion | GetName |  | CString | 类别：非 const |
| Religion | GetNameNoFormatting |  | CString | 类别：非 const |
| Religion | GetNameNoIcon |  | CString | 类别：非 const |
| Religion | GetPolStr | Country | int64 | 类别：非 const |
| Religion | GetPolStrAsFloat | Unknown | float | 类别：非 const |
| Religion | GetPolStrAsPercentage | Country | CFixedPoint | 类别：非 const |
| Religion | GetPopulation | Country | int64 | 类别：非 const |
| Religion | GetPopulationAsFloat | Unknown | float | 类别：非 const |
| Religion | GetPopulationAsPercentage | Country | CFixedPoint | 类别：非 const |
| Religion | GetPopulationChange | Country | int64 | 类别：非 const |
| Religion | GetPopulationChangeDesc | Country | CString | 类别：非 const |
| Religion | GetReligiousTraitsDesc |  | CString | 类别：非 const |
| Religion | GetStateDependents | State | int64 | 类别：非 const |
| Religion | GetStateDependentsAsPercentage | State | CFixedPoint | 类别：非 const |
| Religion | GetStatePolStr | State | int64 | 类别：非 const |
| Religion | GetStatePolStrAsFloat | Unknown | float | 类别：非 const |
| Religion | GetStatePolStrAsPercentage | State | CFixedPoint | 类别：非 const |
| Religion | GetStatePopulation | State | int64 | 类别：非 const |
| Religion | GetStatePopulationAsFloat | Unknown | float | 类别：非 const |
| Religion | GetStatePopulationAsPercentage | State | CFixedPoint | 类别：非 const |
| Religion | GetStateWorkforce | State | int64 | 类别：非 const |
| Religion | GetStateWorkforceAsPercentage | State | CFixedPoint | 类别：非 const |
| Religion | GetTaboosDesc |  | CString | 类别：非 const |
| Religion | GetTextIcon |  | CString | 类别：非 const |
| Religion | GetTexture |  | Unknown | 类别：非 const |
| Religion | GetTooltipTag |  | CString | 类别：非 const |
| Religion | GetWorkforce | Country | int64 | 类别：非 const |
| Religion | GetWorkforceAsPercentage | Country | CFixedPoint | 类别：非 const |
| Religion | IsValid |  | bool |  |
| Religion | MakeScope |  | Scope |  |
| Religion | Self |  | Religion |  |
| ReligionInfoPanel | AccessPops |  | Unknown | 类别：const |
| ReligionInfoPanel | AccessPopsList |  | PopList | 类别：const |
| ReligionInfoPanel | AccessReligion |  | Religion | 类别：const |
| ReligionInfoPanel | AccessSelf |  | ReligionInfoPanel | 类别：const |
| ReligionInfoPanel | GetReligion |  | Religion | 类别：非 const |
| ReligionInfoPanel | IsShowingNationalOnly |  | bool |  |
| ReligionInfoPanel | Self |  | ReligionInfoPanel |  |
| ReligionInfoPanel | ToggleShowNationalOnly |  | void |  |
| RemoveFriendConfirmWindow | AccessSelf |  | RemoveFriendConfirmWindow | 类别：const |
| RemoveFriendConfirmWindow | ConfirmRemove |  | void |  |
| RemoveFriendConfirmWindow | Hide |  | void |  |
| RemoveFriendConfirmWindow | Self |  | RemoveFriendConfirmWindow |  |
| RemoveFriendConfirmWindow | ShouldBeShown |  | bool |  |
| RemoveFriendConfirmWindow | Show |  | void |  |
| RepackWindow | AccessSelf |  | RepackWindow | 类别：const |
| RepackWindow | GetCurrentTileSize |  | int32 | 类别：非 const |
| RepackWindow | Repack |  | void |  |
| RepackWindow | Self |  | RepackWindow |  |
| RepackWindow | SetTileSize | CString | void |  |
| RepackWindow | ShouldWrapX |  | bool |  |
| RepackWindow | Toggle |  | void |  |
| RepackWindow | ToggleShouldWrapX |  | void |  |
| ResignConfirmationWindow | AccessSelf |  | ResignConfirmationWindow | 类别：const |
| ResignConfirmationWindow | Cancel |  | void |  |
| ResignConfirmationWindow | GetText |  | CString | 类别：非 const |
| ResignConfirmationWindow | IsProgress |  | bool |  |
| ResignConfirmationWindow | IsShowSave |  | bool |  |
| ResignConfirmationWindow | OnDesktop |  | void |  |
| ResignConfirmationWindow | OnMenu |  | void |  |
| ResignConfirmationWindow | Self |  | ResignConfirmationWindow |  |
| ResignConfirmationWindow | SetShowSave | Unknown | void |  |
| ResignConfirmationWindow | ShouldSave |  | bool |  |
| ResignConfirmationWindow | ToggleShouldSave |  | void |  |
| RevolutionaryMovementMarker | AccessSelf |  | RevolutionaryMovementMarker | 类别：const |
| RevolutionaryMovementMarker | GetPoliticalMovement |  | PoliticalMovement | 类别：非 const |
| RevolutionaryMovementMarker | GetPosition |  | CVector2f | 类别：非 const |
| RevolutionaryMovementMarker | Self |  | RevolutionaryMovementMarker |  |

| 类型 | 函数 | 参数 | 输出 | 描述 |
|---|---|---|---|---|
| RightClickMenuManager | AccessSelf |  | RightClickMenuManager | 类别：const |
| RightClickMenuManager | Close |  | void |  |
| RightClickMenuManager | IsImportantActionsListOpen |  | bool |  |
| RightClickMenuManager | IsMenuOpen | Unknown | bool |  |
| RightClickMenuManager | IsResearchQueueOpen |  | bool |  |
| RightClickMenuManager | IsSwitchProductionMethodMenuOpen |  | bool |  |
| RightClickMenuManager | Self |  | RightClickMenuManager |  |
| RightClickMenuManager | ShowForBuilding | Building | void |  |
| RightClickMenuManager | ShowForBuildingType | BuildingType | void |  |
| RightClickMenuManager | ShowForCharacter | Character | void |  |
| RightClickMenuManager | ShowForCountry | Country | void |  |
| RightClickMenuManager | ShowForDecree | Decree | void |  |
| RightClickMenuManager | ShowForDiplomaticPlay | DiplomaticPlay | void |  |
| RightClickMenuManager | ShowForGoods | Goods | void |  |
| RightClickMenuManager | ShowForIG | InterestGroup | void |  |
| RightClickMenuManager | ShowForImposeLaw | Law | void |  |
| RightClickMenuManager | ShowForMarket | Market | void |  |
| RightClickMenuManager | ShowForMilitaryFormation | MilitaryFormation | void |  |
| RightClickMenuManager | ShowForPoliticalMovement | PoliticalMovement | void |  |
| RightClickMenuManager | ShowForPowerBloc | PowerBloc | void |  |
| RightClickMenuManager | ShowForSelectArmy |  | void |  |
| RightClickMenuManager | ShowForSelectFleet |  | void |  |
| RightClickMenuManager | ShowForSelectOrder | Character | void |  |
| RightClickMenuManager | ShowForSetDefaultCombatUnitType | MilitaryFormation CombatUnitGroup | void |  |
| RightClickMenuManager | ShowForState | State | void |  |
| RightClickMenuManager | ToggleAddArmyToInvasion | Invasion PdxGuiWidget | void |  |
| RightClickMenuManager | ToggleAddFleetToInvasion | Invasion PdxGuiWidget | void |  |
| RightClickMenuManager | ToggleArticleDraftInput | TreatyDraft ArticleDraft Country PdxGuiWidget CString | void |  |
| RightClickMenuManager | ToggleArticleTypeInput | TreatyDraft ArticleType Country PdxGuiWidget CString | void |  |
| RightClickMenuManager | ToggleBlocActions | Country PdxGuiWidget | void |  |
| RightClickMenuManager | ToggleBlocLeaderActions | Country PdxGuiWidget | void |  |
| RightClickMenuManager | ToggleBuildingActions | Building PdxGuiWidget | void |  |
| RightClickMenuManager | ToggleColorPicker | DataColorPicker PdxGuiWidget | void |  |
| RightClickMenuManager | ToggleCompanyCharterType | CompanyCharterType Company PdxGuiWidget | void |  |
| RightClickMenuManager | ToggleCustomizationOptionItems | Unknown Unknown | void |  |
| RightClickMenuManager | ToggleFilterUnitStates | StagedUnitsWithType StagedFormation PdxGuiWidget | void |  |
| RightClickMenuManager | ToggleImportantActionsList | TopFrontend PdxGuiWidget | void |  |
| RightClickMenuManager | ToggleMapModes | MapModeList PdxGuiWidget | void |  |
| RightClickMenuManager | ToggleMarketStarvationCountriesFilter | Market PdxGuiWidget | void |  |
| RightClickMenuManager | ToggleMarketStarvationStatesFilter | Market PdxGuiWidget | void |  |
| RightClickMenuManager | ToggleMilitaryFormation | MilitaryFormation PdxGuiWidget | void |  |
| RightClickMenuManager | ToggleNationalizePrivatelyOwnedFilter | Unknown Unknown | void |  |
| RightClickMenuManager | ToggleNegotiationIGSelect | Country Law PdxGuiWidget CString | void |  |
| RightClickMenuManager | ToggleOverlordActions | Country PdxGuiWidget | void |  |
| RightClickMenuManager | TogglePowerBlocCoaPieces | PowerBlocCoaPieceSelector PdxGuiWidget | void |  |
| RightClickMenuManager | TogglePowerBlocMapTextureItems | PowerBlocMapTextureSelector PdxGuiWidget | void |  |
| RightClickMenuManager | TogglePrivatizeOrMonopolize | BuildingBrowserBuildingTypeItem PdxGuiWidget | void |  |
| RightClickMenuManager | ToggleResearchQueue | PdxGuiWidget | void |  |
| RightClickMenuManager | ToggleSubjectActions | Country PdxGuiWidget | void |  |
| RightClickMenuManager | ToggleSwayOfferArticleTypeInput | Unknown Unknown Unknown | void |  |
| RightClickMenuManager | ToggleSwitchProductionMethodMenu | Building ProductionMethodGroup PdxGuiWidget | void |  |
| RightClickMenuManager | ToggleSwitchProductionMethodMenuForType | BuildingType ProductionMethodGroup PdxGuiWidget | void |  |
| RightClickMenuManager | ToggleTreatyDraftBindPeriodMenu | Unknown Unknown | void |  |
| RightClickMenuManager | ToggleTreatyDraftReset | TreatyDraft PdxGuiWidget | void |  |
| RightClickMenuManager | ToggleWarGoalArticleTypeInput | Unknown Unknown Unknown | void |  |
| RulerSelectionPopup | AccessRulersOffer |  | Unknown | 类别：const |
| RulerSelectionPopup | AccessSelf |  | RulerSelectionPopup | 类别：const |
| RulerSelectionPopup | RandomizeRulersOffer |  | Command |  |
| RulerSelectionPopup | Self |  | RulerSelectionPopup |  |
| RulerSelectionPopup | SetRulerCommand | Unknown | Command |  |
| Savable | AbsoluteLocationText |  | CString |  |
| Savable | AccessSelf |  | Savable | 类别：const |
| Savable | AllowsFileDialog |  | bool |  |
| Savable | Error |  | CString |  |
| Savable | Filename |  | CString |  |
| Savable | FolderSelect |  | void |  |
| Savable | HasError |  | bool |  |
| Savable | HasWarning |  | bool |  |
| Savable | IsDeletable |  | bool |  |
| Savable | IsFilenameModifiable |  | bool |  |
| Savable | IsRevertible |  | bool |  |
| Savable | IsSelected |  | bool |  |
| Savable | Location |  | CString |  |
| Savable | LocationTooltip |  | CString |  |
| Savable | RevertLocation |  | void |  |
| Savable | Self |  | Savable |  |
| Savable | SetFilename |  | void |  |
| Savable | SetLocation | Unknown | void |  |
| Savable | SetSelected | bool | void |  |
| Savable | Warning |  | CString |  |
| SavableGroup | AccessSelf |  | SavableGroup | 类别：const |
| SavableGroup | HasError |  | bool |  |
| SavableGroup | HasWarning |  | bool |  |
| SavableGroup | IsExpanded |  | bool |  |
| SavableGroup | IsRevertible |  | bool |  |
| SavableGroup | IsSelected |  | bool |  |
| SavableGroup | IsSelectedIndeterminable |  | bool |  |
| SavableGroup | Location |  | CString |  |
| SavableGroup | RevertLocation |  | void |  |
| SavableGroup | Savables |  | Unknown |  |
| SavableGroup | Self |  | SavableGroup |  |
| SavableGroup | SetLocation | Unknown | void |  |
| SavableGroup | SetSelected | bool | void |  |
| SavableGroup | Title |  | CString |  |
| SavableGroup | ToggleExpanded |  | void |  |
| SaveDialog | AccessSelf |  | SaveDialog | 类别：const |
| SaveDialog | FindGroupLocation | PdxGuiWidget SavableGroup | void |  |
| SaveDialog | FindLocation | PdxGuiWidget Savable | void |  |
| SaveDialog | Groups |  | Unknown |  |
| SaveDialog | IsSelected |  | bool |  |
| SaveDialog | IsSelectedIndeterminable |  | bool |  |
| SaveDialog | SavableCount |  | int32 |  |
| SaveDialog | Self |  | SaveDialog |  |
| SaveDialog | SetSelected | bool | void |  |
| SaveGame | AccessSelf |  | SaveGame | 类别：const |
| SaveGame | GetLastModified |  | CString | 类别：非 const |
| SaveGame | GetName |  | CString | 类别：非 const |
| SaveGame | Self |  | SaveGame |  |
| SaveGameAnalysisView | AccessSelf |  | SaveGameAnalysisView | 类别：const |
| SaveGameAnalysisView | GetNote | SaveGameBlockData | CUTF8String | 类别：非 const |
| SaveGameAnalysisView | GetProgress |  | float | 类别：非 const |
| SaveGameAnalysisView | GetSaveGame |  | SaveGame | 类别：非 const |
| SaveGameAnalysisView | GetShowHidden |  | bool | 类别：非 const |
| SaveGameAnalysisView | IsActive |  | bool |  |
| SaveGameAnalysisView | IsEmpty |  | bool |  |
| SaveGameAnalysisView | IsReading |  | bool |  |
| SaveGameAnalysisView | Self |  | SaveGameAnalysisView |  |
| SaveGameAnalysisView | Sort | CString | void |  |
| SaveGameAnalysisView | ToggleShowHidden |  | void |  |
| SaveGameAnalyzer | AccessSelf |  | SaveGameAnalyzer | 类别：const |
| SaveGameAnalyzer | CancelLoad |  | void |  |
| SaveGameAnalyzer | CloseNotes |  | void |  |
| SaveGameAnalyzer | EditNotes | CString | void |  |
| SaveGameAnalyzer | ListSaves |  | void |  |
| SaveGameAnalyzer | LoadSelected |  | void |  |
| SaveGameAnalyzer | Self |  | SaveGameAnalyzer |  |
| SaveGameBlockData | AccessSelf |  | SaveGameBlockData | 类别：const |
| SaveGameBlockData | GetCharCount |  | int32 | 类别：非 const |
| SaveGameBlockData | GetInstanceCount |  | int32 | 类别：非 const |
| SaveGameBlockData | GetOtherPaths |  | CString | 类别：非 const |
| SaveGameBlockData | GetOtherPathsCount |  | int32 | 类别：非 const |
| SaveGameBlockData | GetParentPercentage |  | float | 类别：非 const |
| SaveGameBlockData | GetPath |  | CString | 类别：非 const |
| SaveGameBlockData | GetPercentage |  | float | 类别：非 const |
| SaveGameBlockData | GetTitle |  | CString | 类别：非 const |
| SaveGameBlockData | GetTokenName |  | CString | 类别：非 const |
| SaveGameBlockData | GetWhitespaceCount |  | int32 | 类别：非 const |
| SaveGameBlockData | GetWhitespaceRatio |  | float | 类别：nonconst |
| SaveGameBlockData | Self |  | SaveGameBlockData |  |
| SaveGameConfigView | AccessSelf |  | SaveGameConfigView | 类别：const |
| SaveGameConfigView | GetTokenName |  | CString | 类别：nonconst |
| SaveGameConfigView | IsActive |  | bool |  |
| SaveGameConfigView | IsDirty |  | bool |  |
| SaveGameConfigView | Save |  | void |  |
| SaveGameConfigView | Self |  | SaveGameConfigView |  |
| SaveGameItem | AccessSelf |  | SaveGameItem | 类别：const |
| SaveGameItem | CanGetAchievements |  | bool |  |
| SaveGameItem | CanLoad |  | bool |  |
| SaveGameItem | CanLoadDesc |  | CString |  |
| SaveGameItem | GetAchievementBlockingGameRulesInfo |  | CString | 类别：nonconst |
| SaveGameItem | GetCountryFlag |  | CoatOfArms | 类别：nonconst |
| SaveGameItem | GetCountryName |  | CString | 类别：nonconst |
| SaveGameItem | GetCountryRank |  | CString | 类别：nonconst |
| SaveGameItem | GetDate |  | Date | 类别：nonconst |
| SaveGameItem | GetIncompatibilityTooltip |  | CString | 类别：nonconst |
| SaveGameItem | GetLastPlayed |  | CString | 类别：nonconst |
| SaveGameItem | GetMissingDLCInfo |  | CString | 类别：nonconst |
| SaveGameItem | GetMissingMods |  | CString | 类别：nonconst |
| SaveGameItem | GetModifiedDate |  | CString | 类别：nonconst |
| SaveGameItem | GetName |  | CString | 类别：nonconst |
| SaveGameItem | GetNumberOfPlayers |  | int32 | 类别：nonconst |
| SaveGameItem | GetVersionName |  | CString | 类别：nonconst |
| SaveGameItem | HasAchievementBlockingGameRules |  | bool |  |
| SaveGameItem | HasMissingDLCs |  | bool |  |
| SaveGameItem | HasMissingMods |  | bool |  |
| SaveGameItem | IsCloudSave |  | bool |  |
| SaveGameItem | IsDifferentVersion |  | bool |  |
| SaveGameItem | IsIronmanSave |  | bool |  |
| SaveGameItem | IsMultiplayer |  | bool |  |
| SaveGameItem | IsSelected |  | bool |  |
| SaveGameItem | IsValid |  | bool |  |
| SaveGameItem | OnLoad |  | void |  |
| SaveGameItem | Select |  | void |  |
| SaveGameItem | SelectAndLoad |  | void |  |
| SaveGameItem | Self |  | SaveGameItem |  |
| SaveGameListView | AccessSaves |  | Unknown | 类别：const |
| SaveGameListView | AccessSelf |  | SaveGameListView | 类别：const |
| SaveGameListView | HasSelection |  | bool |  |
| SaveGameListView | IsActive |  | bool |  |
| SaveGameListView | IsReading |  | bool |  |
| SaveGameListView | IsSelected | SaveGame | bool |  |
| SaveGameListView | Self |  | SaveGameListView |  |
| SaveGameListView | SetSelected | SaveGame | void |  |
| SaveGameListView | Sort | CString | void |  |
| SaveGameWindow | AccessCloudData |  | CloudSaveData | 类别：const |
| SaveGameWindow | AccessSelf |  | SaveGameWindow | 类别：const |
| SaveGameWindow | Cancel |  | void |  |
| SaveGameWindow | GetDefaultSaveName |  | CUTF8String | 类别：nonconst |
| SaveGameWindow | GetSaveGames |  | Unknown | 类别：nonconst |
| SaveGameWindow | IsIronman |  | bool |  |
| SaveGameWindow | IsOverwrite |  | bool |  |
| SaveGameWindow | IsSaveNameOk |  | bool |  |
| SaveGameWindow | IsSaving |  | bool |  |
| SaveGameWindow | IsShowInvalid |  | bool |  |
| SaveGameWindow | Save |  | void |  |
| SaveGameWindow | Self |  | SaveGameWindow |  |
| SaveGameWindow | ToggleShowInvalid |  | void |  |
| SaveGameWindow | UpdateSaveName |  | void |  |
| Scope | AccessSelf |  | Scope | 类别：const |
| Scope | GetFlagName |  | CString | 类别：nonconst |
| Scope | GetList | Unknown | Unknown | 类别：nonconst |
| Scope | GetScriptValueDesc | ScriptValue | CString | 类别：nonconst |
| Scope | GetValue |  | CFixedPoint | 类别：nonconst |
| Scope | GetValueWithDefault | Unknown | CFixedPoint | 类别：nonconst |
| Scope | IsSet |  | bool |  |
| Scope | ScriptValue | ScriptValue | CFixedPoint |  |
| Scope | Self |  | Scope |  |
| Scope | VarRemaining | Unknown | int32 |  |
| ScopeDebugData | AccessSelf |  | ScopeDebugData | 类别：const |
| ScopeDebugData | GetDebugInformation |  | CString | 类别：nonconst |
| ScopeDebugData | GetRawID |  | CString | 类别：nonconst |
| ScopeDebugData | GetTypeData |  | CString | 类别：nonconst |
| ScopeDebugData | GetTypeID |  | CString | 类别：nonconst |
| ScopeDebugData | GetTypeName |  | CString | 类别：nonconst |
| ScopeDebugData | IsValid |  | bool |  |
| ScopeDebugData | Self |  | ScopeDebugData |  |
| ScopeDebugData | SupportsVariables |  | bool |  |
| ScopeDebugInspectorPlugin | AccessSelf |  | ScopeDebugInspectorPlugin | 类别：const |
| ScopeDebugInspectorPlugin | Self |  | ScopeDebugInspectorPlugin |  |
| ScopeObjectEditor | AccessSelf |  | ScopeObjectEditor | 类别：const |
| ScopeObjectEditor | AsBool |  | bool |  |
| ScopeObjectEditor | AsString |  | CString |  |
| ScopeObjectEditor | GetID |  | uint64 | 类别：nonconst |
| ScopeObjectEditor | GetSelecte |  | CVector2i | 类别：nonconst |
| ScopeObjectEditor | GetTypeData |  | CString | 类别：nonconst |
| ScopeObjectEditor | GetValue |  | CString | 类别：nonconst |
| ScopeObjectEditor | GetVariableTypes |  | Unknown | 类别：nonconst |
| ScopeObjectEditor | IsBool |  | bool |  |
| ScopeObjectEditor | IsFlag |  | bool |  |
| ScopeObjectEditor | IsNumber |  | bool |  |
| ScopeObjectEditor | IsReference |  | bool |  |
| ScopeObjectEditor | Self |  | ScopeObjectEditor |  |
| ScopeObjectEditor | SetFromString |  | void |  |
| ScopeObjectEditor | SetIDFromString |  | void |  |
| ScopeObjectEditor | SetSelecte |  | void |  |
| ScopeObjectEditor | SetTypeDataFromString |  | void |  |
| ScopeObjectEditor | ToggleBool |  | void |  |
| ScopeObjectProvider | AccessSelf |  | ScopeObjectProvider | 类别：const |
| ScopeObjectProvider | GetError |  | CString | 类别：nonconst |
| ScopeObjectProvider | GetFilteredResultCount |  | int32 | 类别：nonconst |
| ScopeObjectProvider | GetTotalResultCount |  | int32 | 类别：nonconst |
| ScopeObjectProvider | GetTriggerString |  | CString | 类别：nonconst |
| ScopeObjectProvider | HasError |  | bool |  |
| ScopeObjectProvider | Self |  | ScopeObjectProvider |  |
| ScopeObjectProvider | SetTriggerString |  | void |  |
| ScopeObjectProvider | UpdateFilter |  | void |  |
| ScopeObjectType | AccessSelf |  | ScopeObjectType | 类别：const |
| ScopeObjectType | GetName |  | CString | 类别：nonconst |
| ScopeObjectType | Self |  | ScopeObjectType |  |
| ScopedEditorSettingsCategory | AccessSelf |  | ScopedEditorSettingsCategory | 类别：const |
| ScopedEditorSettingsCategory | Self |  | ScopedEditorSettingsCategory |  |
| ScriptProfilerEntry | AccessSelf |  | ScriptProfilerEntry | 类别：const |
| ScriptProfilerEntry | GetAverageTimeExclusive |  | double | 类别：nonconst |
| ScriptProfilerEntry | GetAverageTimeInclusive |  | double | 类别：nonconst |
| ScriptProfilerEntry | GetBottleneckTime |  | double | 类别：nonconst |
| ScriptProfilerEntry | GetCallCount |  | uint64 | 类别：nonconst |
| ScriptProfilerEntry | GetFile |  | Unknown | 类别：nonconst |
| ScriptProfilerEntry | GetFileAndLine |  | CString | 类别：nonconst |
| ScriptProfilerEntry | GetFileName |  | Unknown | 类别：nonconst |
| ScriptProfilerEntry | GetFileNameAndLine |  | CString | 类别：nonconst |
| ScriptProfilerEntry | GetFormattedBottleneckTiming |  | CString | 类别：nonconst |
| ScriptProfilerEntry | GetFormattedTiming |  | CString | 类别：nonconst |
| ScriptProfilerEntry | GetLine |  | int32 | 类别：nonconst |
| ScriptProfilerEntry | GetMaxTimeInclusive |  | double | 类别：nonconst |
| ScriptProfilerEntry | GetMinTimeInclusive |  | double | 类别：nonconst |
| ScriptProfilerEntry | GetPerFrameTimeExclusive |  | double | 类别：nonconst |
| ScriptProfilerEntry | GetPerFrameTimeInclusive |  | double | 类别：nonconst |
| ScriptProfilerEntry | GetPerTickTimeExclusive |  | double | 类别：nonconst |
| ScriptProfilerEntry | GetPerTickTimeInclusive |  | double | 类别：nonconst |
| ScriptProfilerEntry | GetShortDescription |  | CString | 类别：nonconst |
| ScriptProfilerEntry | GetTiming |  | double | 类别：nonconst |
| ScriptProfilerEntry | GetTotalTimeExclusive |  | double | 类别：nonconst |
| ScriptProfilerEntry | GetTotalTimeInclusive |  | double | 类别：nonconst |
| ScriptProfilerEntry | GetType |  | CString | 类别：nonconst |
| ScriptProfilerEntry | GetVariant |  | CString | 类别：nonconst |
| ScriptProfilerEntry | HasFileLocation |  | bool |  |
| ScriptProfilerEntry | HasSamples |  | bool |  |
| ScriptProfilerEntry | OpenInCodeEditor |  | void |  |
| ScriptProfilerEntry | OpenInScriptEditor |  | void |  |
| ScriptProfilerEntry | Select |  | void |  |
| ScriptProfilerEntry | SelectFile |  | void |  |
| ScriptProfilerEntry | Self |  | ScriptProfilerEntry |  |
| ScriptProfilerFileLine | AccessSelf |  | ScriptProfilerFileLine | 类别：const |
| ScriptProfilerFileLine | GetAverageTimeExclusive |  | double | 类别：nonconst |
| ScriptProfilerFileLine | GetAverageTimeInclusive |  | double | 类别：nonconst |
| ScriptProfilerFileLine | GetBottleneckTime |  | double | 类别：nonconst |
| ScriptProfilerFileLine | GetCallCount |  | uint64 | 类别：nonconst |
| ScriptProfilerFileLine | GetFormattedBottleneckTiming |  | CString | 类别：nonconst |
| ScriptProfilerFileLine | GetFormattedTiming |  | CString | 类别：nonconst |
| ScriptProfilerFileLine | GetLine |  | int32 | 类别：nonconst |
| ScriptProfilerFileLine | GetMaxTimeInclusive |  | double | 类别：nonconst |
| ScriptProfilerFileLine | GetMinTimeInclusive |  | double | 类别：nonconst |
| ScriptProfilerFileLine | GetPerFrameTimeExclusive |  | double | 类别：nonconst |
| ScriptProfilerFileLine | GetPerFrameTimeInclusive |  | double | 类别：nonconst |
| ScriptProfilerFileLine | GetPerTickTimeExclusive |  | double | 类别：nonconst |
| ScriptProfilerFileLine | GetPerTickTimeInclusive |  | double | 类别：nonconst |
| ScriptProfilerFileLine | GetText |  | Unknown | 类别：nonconst |
| ScriptProfilerFileLine | GetTiming |  | double | 类别：nonconst |
| ScriptProfilerFileLine | GetTooltip |  | CString | 类别：nonconst |
| ScriptProfilerFileLine | GetTotalTimeExclusive |  | double | 类别：nonconst |
| ScriptProfilerFileLine | GetTotalTimeInclusive |  | double | 类别：nonconst |
| ScriptProfilerFileLine | HasSamples |  | bool |  |
| ScriptProfilerFileLine | OpenInCodeEditor |  | void |  |
| ScriptProfilerFileLine | OpenInScriptEditor |  | void |  |
| ScriptProfilerFileLine | Select |  | void |  |
| ScriptProfilerFileLine | Self |  | ScriptProfilerFileLine |  |
| ScriptProfilerGui | AccessSelf |  | ScriptProfilerGui | 类别：const |
| ScriptProfilerGui | GetCaptureTime |  | double | 类别：nonconst |
| ScriptProfilerGui | GetCapturedFrames |  | uint64 | 类别：nonconst |
| ScriptProfilerGui | GetCapturedSamples |  | int32 | 类别：nonconst |
| ScriptProfilerGui | GetCapturedTicks |  | uint64 | 类别：nonconst |
| ScriptProfilerGui | GetCurrentEntry |  | ScriptProfilerEntry | 类别：nonconst |
| ScriptProfilerGui | GetCurrentEntryChildren |  | Unknown | 类别：nonconst |
| ScriptProfilerGui | GetCurrentEntryParents |  | Unknown | 类别：nonconst |
| ScriptProfilerGui | GetFileLines |  | Unknown | 类别：nonconst |
| ScriptProfilerGui | GetFileSearchList |  | ToolPropertySearchList | 类别：nonconst |
| ScriptProfilerGui | GetModeSearchList |  | ToolPropertySearchList | 类别：nonconst |
| ScriptProfilerGui | GetNextFile |  | Unknown | 类别：nonconst |
| ScriptProfilerGui | GetPreviousFile |  | Unknown | 类别：nonconst |
| ScriptProfilerGui | HasNextFile |  | bool |  |
| ScriptProfilerGui | HasPreviousFile |  | bool |  |
| ScriptProfilerGui | IsCapturing |  | bool |  |
| ScriptProfilerGui | OpenFileInCodeEditor |  | void |  |
| ScriptProfilerGui | OpenFileInScriptEditor |  | void |  |
| ScriptProfilerGui | OpenNextFile |  | void |  |
| ScriptProfilerGui | OpenPreviousFile |  | void |  |
| ScriptProfilerGui | ResetCaptureData |  | void |  |
| ScriptProfilerGui | RestartCapture |  | void |  |
| ScriptProfilerGui | SelectEdge |  | void |  |
| ScriptProfilerGui | SelectRoot |  | void |  |
| ScriptProfilerGui | Self |  | ScriptProfilerGui |  |
| ScriptProfilerGui | StartCapture |  | void |  |
| ScriptProfilerGui | StopCapture |  | void |  |
| ScriptRunnerInspector | AccessSelf |  | ScriptRunnerInspector | 类别：const |
| ScriptRunnerInspector | GetEffect |  | CString | 类别：nonconst |
| ScriptRunnerInspector | GetTrigger |  | CString | 类别：nonconst |
| ScriptRunnerInspector | ParseEffect |  | void |  |
| ScriptRunnerInspector | RunEffect |  | void |  |
| ScriptRunnerInspector | RunTrigger |  | void |  |
| ScriptRunnerInspector | Self |  | ScriptRunnerInspector |  |
| ScriptRunnerInspector | SetEffect |  | void |  |
| ScriptRunnerInspector | SetTrigger |  | void |  |
| ScriptRunnerInspector | ShouldModifyEventTargets |  | bool |  |
| ScriptRunnerInspector | ToggleModifyEventTargets |  | void |  |
| ScriptRunnerResult | AccessSelf |  | ScriptRunnerResult | 类别：const |
| ScriptRunnerResult | GetResult |  | CString | 类别：nonconst |
| ScriptRunnerResult | GetTooltip |  | CString | 类别：nonconst |
| ScriptRunnerResult | HasResult |  | bool |  |
| ScriptRunnerResult | IsMissingTooltip |  | bool |  |
| ScriptRunnerResult | IsOutputVisible |  | bool |  |
| ScriptRunnerResult | IsValid |  | bool |  |
| ScriptRunnerResult | Self |  | ScriptRunnerResult |  |
| ScriptRunnerResult | ToggleOutputVisible |  | void |  |
| ScriptedButton | AccessSelf |  | ScriptedButton | 类别：const |
| ScriptedButton | ExecuteEffect |  | Command |  |
| ScriptedButton | GetCooldownDesc |  | CString | 类别：nonconst |
| ScriptedButton | GetCooldownDuration |  | CString | 类别：nonconst |
| ScriptedButton | GetCooldownRemaining |  | CString | 类别：nonconst |
| ScriptedButton | GetDesc |  | CString | 类别：nonconst |
| ScriptedButton | GetEffectDesc |  | CString | 类别：nonconst |
| ScriptedButton | GetName |  | CString | 类别：nonconst |
| ScriptedButton | GetPossibleDesc |  | CString | 类别：nonconst |
| ScriptedButton | GetTooltipTag |  | CString | 类别：nonconst |
| ScriptedButton | HasCooldown |  | bool |  |
| ScriptedButton | IsOnCooldown |  | bool |  |
| ScriptedButton | IsPossible |  | bool |  |
| ScriptedButton | IsSelected |  | bool |  |
| ScriptedButton | IsVisible |  | bool |  |
| ScriptedButton | Self |  | ScriptedButton |  |
| ScriptedGui | AccessSelf |  | ScriptedGui | 类别：const |
| ScriptedGui | BuildTooltip | Unknown | CString |  |
| ScriptedGui | Execute | TopScope | void |  |
| ScriptedGui | ExecuteTooltip | TopScope | CString |  |
| ScriptedGui | IsShown | Unknown | bool |  |
| ScriptedGui | IsShownTooltip | Unknown | CString |  |
| ScriptedGui | IsValid | Unknown | bool |  |
| ScriptedGui | IsValidTooltip | Unknown | CString |  |
| ScriptedGui | Self |  | ScriptedGui |  |
| ScriptedProgressBar | AccessSelf |  | ScriptedProgressBar | 类别：const |
| ScriptedProgressBar | GetDesc |  | CString | 类别：nonconst |
| ScriptedProgressBar | GetMaxValue |  | CFixedPoint | 类别：nonconst |
| ScriptedProgressBar | GetMinValue |  | CFixedPoint | 类别：nonconst |
| ScriptedProgressBar | GetName |  | CString | 类别：nonconst |
| ScriptedProgressBar | GetPeriodicProgressBreakdown |  | CString | 类别：nonconst |
| ScriptedProgressBar | GetSecondDesc |  | CString | 类别：nonconst |
| ScriptedProgressBar | GetStartValue |  | CFixedPoint | 类别：nonconst |
| ScriptedProgressBar | GetTooltipTag |  | CString | 类别：nonconst |
| ScriptedProgressBar | IsDefault |  | bool |  |
| ScriptedProgressBar | IsDefaultBad |  | bool |  |
| ScriptedProgressBar | IsDefaultGreen |  | bool |  |
| ScriptedProgressBar | IsDoubleSidedBad |  | bool |  |
| ScriptedProgressBar | IsDoubleSidedGold |  | bool |  |
| ScriptedProgressBar | IsDoubleSidedSpain |  | bool |  |
| ScriptedProgressBar | Self |  | ScriptedProgressBar |  |
| SeaNodeMarker | AccessSelf |  | SeaNodeMarker | 类别：const |
| SeaNodeMarker | GetInteractionColor |  | CVector4f | 类别：nonconst |
| SeaNodeMarker | GetInteractionTooltip |  | CString | 类别：nonconst |
| SeaNodeMarker | GetSupplyNetworkTooltip |  | CString | 类别：nonconst |
| SeaNodeMarker | HasActiveSupplyNetwork |  | bool |  |
| SeaNodeMarker | HasAnyShippingLaneDamaged | Country | bool |  |
| SeaNodeMarker | IsActiveInteractionNode |  | bool |  |
| SeaNodeMarker | IsSeaNodeHighlighted |  | bool |  |
| SeaNodeMarker | IsSelected |  | bool |  |
| SeaNodeMarker | IsValidInteractionNode |  | bool |  |
| SeaNodeMarker | SelectClick |  | void |  |
| SeaNodeMarker | SelectInteractionClick |  | void |  |
| SeaNodeMarker | Self |  | SeaNodeMarker |  |
| SeaNodeMarker | ShouldShowInteraction |  | bool |  |
| SeaNodeMovementMarker | AccessSelf |  | SeaNodeMovementMarker | 类别：const |
| SeaNodeMovementMarker | CanDeploySelectedFormationsToSeaNode |  | bool |  |
| SeaNodeMovementMarker | GetActiveSupplyNetworkDesc |  | CString | 类别：nonconst |
| SeaNodeMovementMarker | GetConvoyRaidingDesc |  | CString | 类别：nonconst |
| SeaNodeMovementMarker | GetConvoyRaidingEnemyFleetsDesc |  | CString | 类别：nonconst |
| SeaNodeMovementMarker | GetInvasionDesc |  | CString | 类别：nonconst |
| SeaNodeMovementMarker | GetInvasionStatus |  | CString | 类别：nonconst |
| SeaNodeMovementMarker | GetPosition |  | CVector2f | 类别：nonconst |
| SeaNodeMovementMarker | GetPresentFormationsBreakdown |  | CString | 类别：nonconst |
| SeaNodeMovementMarker | GetSeaNode |  | Province | 类别：nonconst |
| SeaNodeMovementMarker | GetTravelTimeBreakdown |  | CString | 类别：nonconst |
| SeaNodeMovementMarker | HasActiveSupplyNetwork |  | bool |  |
| SeaNodeMovementMarker | IsAllSelectedFormationsLocation |  | bool |  |
| SeaNodeMovementMarker | IsAllSelectedFormationsTarget |  | bool |  |
| SeaNodeMovementMarker | IsAnySelectedFormationsLocation |  | bool |  |
| SeaNodeMovementMarker | IsAnySelectedFormationsTarget |  | bool |  |
| SeaNodeMovementMarker | IsBeingConvoyRaidedByEnemies |  | bool |  |
| SeaNodeMovementMarker | IsBeingNavallyInvadedByEnemies |  | bool |  |
| SeaNodeMovementMarker | Self |  | SeaNodeMovementMarker |  |
| SeaRegionInfraMarker | AccessSelf |  | SeaRegionInfraMarker | 类别：const |
| SeaRegionInfraMarker | GetPosition |  | CVector2f | 类别：nonconst |
| SeaRegionInfraMarker | GetStateRegion |  | StateRegion | 类别：nonconst |
| SeaRegionInfraMarker | GetTooltip |  | CString | 类别：nonconst |
| SeaRegionInfraMarker | Self |  | SeaRegionInfraMarker |  |
| SeaRegionPanel | AccessActiveBattles |  | Unknown | 类别：const |
| SeaRegionPanel | AccessCountriesWithShippingLanes |  | Unknown | 类别：const |
| SeaRegionPanel | AccessEndedBattles |  | Unknown | 类别：const |
| SeaRegionPanel | AccessProvince |  | Province | 类别：const |
| SeaRegionPanel | AccessSelf |  | SeaRegionPanel | 类别：const |
| SeaRegionPanel | AccessShippingLanes |  | Unknown | 类别：const |
| SeaRegionPanel | GetExporters | Goods | Unknown | 类别：nonconst |
| SeaRegionPanel | GetImporters | Goods | Unknown | 类别：nonconst |
| SeaRegionPanel | GetNumTradedInWorldMarket | Goods | CFixedPoint | 类别：nonconst |
| SeaRegionPanel | GetPlayerSeaRegionWars |  | Unknown | 类别：nonconst |
| SeaRegionPanel | GetPresentNeutralFleets |  | Unknown | 类别：nonconst |
| SeaRegionPanel | GetProvince |  | Province | 类别：nonconst |
| SeaRegionPanel | GetWorldMarketTradeBreakdown | Goods | CString | 类别：nonconst |
| SeaRegionPanel | GetWorldMarketTradedGoods |  | Unknown | 类别：nonconst |
| SeaRegionPanel | Self |  | SeaRegionPanel |  |
| SeaRegionPanel | Sort | CString | void |  |
| SeaRegionWar | AccessSelf |  | SeaRegionWar | 类别：const |
| SeaRegionWar | GetAlliedCountriesWithShippingLanes |  | Unknown | 类别：nonconst |
| SeaRegionWar | GetAlliedFleets |  | Unknown | 类别：nonconst |
| SeaRegionWar | GetEnemyCountriesWithShippingLanes |  | Unknown | 类别：nonconst |
| SeaRegionWar | GetEnemyFleets |  | Unknown | 类别：nonconst |
| SeaRegionWar | GetInvasions |  | Unknown | 类别：nonconst |
| SeaRegionWar | GetWar |  | War | 类别：nonconst |
| SeaRegionWar | Self |  | SeaRegionWar |  |
| SearchListNodeWindow | AccessSelf |  | SearchListNodeWindow | 类别：const |
| SearchListNodeWindow | CanEditEntry |  | bool |  |
| SearchListNodeWindow | GetEntryTooltip |  | CString | 类别：nonconst |
| SearchListNodeWindow | IsEntryEditingSupported |  | bool |  |
| SearchListNodeWindow | OnEntryEditClick |  | void |  |
| SearchListNodeWindow | Self |  | SearchListNodeWindow |  |
| SelectFromInputNodeWindow | AccessSelf |  | SelectFromInputNodeWindow | 类别：const |
| SelectFromInputNodeWindow | AddPin |  | void |  |
| SelectFromInputNodeWindow | GetNumberOfPins |  | int32 | 类别：nonconst |
| SelectFromInputNodeWindow | RemovePin |  | void |  |
| SelectFromInputNodeWindow | Self |  | SelectFromInputNodeWindow |  |
| SelectFromInputNodeWindow | SetNumberOfPins |  | void |  |
| SelectParticleUserDataDialog | AccessSelf |  | SelectParticleUserDataDialog | 类别：const |
| SelectParticleUserDataDialog | DataModel |  | Unknown |  |
| SelectParticleUserDataDialog | Self |  | SelectParticleUserDataDialog |  |
| SelectTool | AccessSelf |  | SelectTool | 类别：const |
| SelectTool | IsHideSelection |  | bool |  |
| SelectTool | Self |  | SelectTool |  |
| SelectTool | SetHideSelection | bool | void |  |
| ServerInformation | AccessSelf |  | ServerInformation | 类别：const |
| ServerInformation | GetMPMode |  | CString | 类别：nonconst |
| ServerInformation | GetServerID |  | CUTF8String | 类别：nonconst |
| ServerInformation | GetServerName |  | CUTF8String | 类别：nonconst |
| ServerInformation | HasServerID |  | bool |  |
| ServerInformation | HasServerName |  | bool |  |
| ServerInformation | IsInvite |  | bool |  |
| ServerInformation | IsPublic |  | bool |  |
| ServerInformation | IsSingleplayer |  | bool |  |
| ServerInformation | Self |  | ServerInformation |  |
| SettingCategory | AccessSelf |  | SettingCategory | 类别：const |
| SettingCategory | AccessSettingsOrder |  | Unknown | 类别：const |
| SettingCategory | GetName |  | CUTF8String | 类别：nonconst |
| SettingCategory | GetSettingsOrder |  | Unknown | 类别：nonconst |
| SettingCategory | HasSettingsWidgets |  | bool |  |
| SettingCategory | Self |  | SettingCategory |  |
| SettingsPage | AccessCategories |  | Unknown | 类别：const |
| SettingsPage | AccessSelf |  | SettingsPage | 类别：const |
| SettingsPage | GetName |  | CUTF8String | 类别：nonconst |
| SettingsPage | IsSelected |  | bool |  |
| SettingsPage | OnClick |  | void |  |
| SettingsPage | Self |  | SettingsPage |  |
| ShippingLane | AccessSelf |  | ShippingLane | 类别：const |
| ShippingLane | GetBeginState |  | State | 类别：nonconst |
| ShippingLane | GetConvoyCostFormatted |  | CString | 类别：nonconst |
| ShippingLane | GetConvoyCostFormattedShort |  | CString | 类别：nonconst |
| ShippingLane | GetConvoyCostRaw |  | int32 | 类别：nonconst |
| ShippingLane | GetCountry |  | Country | 类别：nonconst |
| ShippingLane | GetCustom | CustomLocalization | CString | 类别：nonconst |
| ShippingLane | GetDesc |  | CString | 类别：nonconst |
| ShippingLane | GetEffectivenessFormatted |  | CString | 类别：nonconst |
| ShippingLane | GetEffectivenessRaw |  | CFixedPoint | 类别：nonconst |
| ShippingLane | GetEndState |  | State | 类别：nonconst |
| ShippingLane | GetName |  | CString | 类别：nonconst |
| ShippingLane | GetTooltipTag |  | CString | 类别：nonconst |
| ShippingLane | IsGoodsTransfer |  | bool |  |
| ShippingLane | IsPortConnection |  | bool |  |
| ShippingLane | IsSupplyRoute |  | bool |  |
| ShippingLane | MakeScope |  | Scope |  |
| ShippingLane | Self |  | ShippingLane |  |
| SkinEditor | AccessSelf |  | SkinEditor | 类别：常量 |
| SkinEditor | Self |  | SkinEditor |  |
| SmartBrushHeightRange | AccessPattern |  | SmartBrushPattern | 类别：常量 |
| SmartBrushHeightRange | AccessSelf |  | SmartBrushHeightRange | 类别：常量 |
| SmartBrushHeightRange | GetName |  | CUTF8String | 类别：非常量 |
| SmartBrushHeightRange | GetOpacityMaskTexturePath |  | CString | 类别：非常量 |
| SmartBrushHeightRange | IsVisible |  | bool |  |
| SmartBrushHeightRange | Self |  | SmartBrushHeightRange |  |
| SmartBrushPattern | AccessMaterialMix |  | MaterialMix | 类别：常量 |
| SmartBrushPattern | AccessSelf |  | SmartBrushPattern | 类别：常量 |
| SmartBrushPattern | GetAngleL |  | float | 类别：非常量 |
| SmartBrushPattern | GetAngleR |  | float | 类别：非常量 |
| SmartBrushPattern | GetBleeding |  | uint32 | 类别：非常量 |
| SmartBrushPattern | GetDensity |  | int32 | 类别：非常量 |
| SmartBrushPattern | GetInterpolationIndex |  | CVector2i | 类别：非常量 |
| SmartBrushPattern | GetModeIndex |  | int32 | 类别：非常量 |
| SmartBrushPattern | GetPatternIndex |  | CVector2i | 类别：非常量 |
| SmartBrushPattern | GetSharpness |  | uint32 | 类别：非常量 |
| SmartBrushPattern | Self |  | SmartBrushPattern |  |
| SmartBrushPresetManager | AccessPresets |  | Unknown | 类别：常量 |
| SmartBrushPresetManager | AccessSelf |  | SmartBrushPresetManager | 类别：常量 |
| SmartBrushPresetManager | GetPresets |  | Unknown | 类别：非常量 |
| SmartBrushPresetManager | Self |  | SmartBrushPresetManager |  |
| SmartMaterialPaintingMode | AccessCurrentPreset |  | Unknown | 类别：常量 |
| SmartMaterialPaintingMode | AccessCurrentPresetRanges |  | Unknown | 类别：常量 |
| SmartMaterialPaintingMode | AccessOpacityMaskTexturePreview | SmartBrushHeightRange | Unknown | 类别：常量 |
| SmartMaterialPaintingMode | AccessPatternCurveTexture | SmartBrushPattern | Unknown | 类别：常量 |
| SmartMaterialPaintingMode | AccessPatternTypeTexture | SmartBrushPattern | Unknown | 类别：常量 |
| SmartMaterialPaintingMode | AccessSelf |  | SmartMaterialPaintingMode | 类别：常量 |
| SmartMaterialPaintingMode | AddAngle | SmartBrushPattern bool float | void |  |
| SmartMaterialPaintingMode | AddBleeding | SmartBrushPattern int32 | void |  |
| SmartMaterialPaintingMode | AddDensity | SmartBrushPattern int32 | void |  |
| SmartMaterialPaintingMode | AddOpacityMaskOffset | bool SmartBrushHeightRange float | void |  |
| SmartMaterialPaintingMode | AddOpacityMaskRotation | SmartBrushHeightRange float | void |  |
| SmartMaterialPaintingMode | AddOpacityMaskScale | bool SmartBrushHeightRange float | void |  |
| SmartMaterialPaintingMode | AddSharpness | SmartBrushPattern int32 | void |  |
| SmartMaterialPaintingMode | ApplyChanges |  | void |  |
| SmartMaterialPaintingMode | CanApplyChanges |  | bool |  |
| SmartMaterialPaintingMode | CanReorderRangeToNext | SmartBrushHeightRange | bool |  |
| SmartMaterialPaintingMode | CanReorderRangeToPrev | SmartBrushHeightRange | bool |  |
| SmartMaterialPaintingMode | ChangeSampleEntryComposition | MaterialMix MaterialMixEntry SmartBrushHeightRange Unknown | void |  |
| SmartMaterialPaintingMode | ClearOpacityMaskTexture | SmartBrushHeightRange | void |  |
| SmartMaterialPaintingMode | ClonePreset |  | void |  |
| SmartMaterialPaintingMode | CopyCurveToClipboard | ToolPropertyCurve | void |  |
| SmartMaterialPaintingMode | CreateNewPreset |  | void |  |
| SmartMaterialPaintingMode | CreateNewRange |  | void |  |
| SmartMaterialPaintingMode | DeletePreset |  | void |  |
| SmartMaterialPaintingMode | DeleteRange | SmartBrushHeightRange | void |  |
| SmartMaterialPaintingMode | DiscardChanges |  | void |  |
| SmartMaterialPaintingMode | EndSampleCompositionEdit | MaterialMix SmartBrushHeightRange Unknown | void |  |
| SmartMaterialPaintingMode | GetBackgroundProcessingDesc |  | CString | 类别：非常量 |
| SmartMaterialPaintingMode | GetCurrentPreset |  | Unknown | 类别：非常量 |
| SmartMaterialPaintingMode | GetCurveFromClipboard |  | Unknown | 类别：非常量 |
| SmartMaterialPaintingMode | GetDebugDesc |  | CString | 类别：非常量 |
| SmartMaterialPaintingMode | GetDebugUIHint |  | CString | 类别：非常量 |
| SmartMaterialPaintingMode | GetOpacityMaskOffset | bool SmartBrushHeightRange | float | 类别：非常量 |
| SmartMaterialPaintingMode | GetOpacityMaskRotation | SmartBrushHeightRange | float | 类别：非常量 |
| SmartMaterialPaintingMode | GetOpacityMaskScale | bool SmartBrushHeightRange | float | 类别：非常量 |
| SmartMaterialPaintingMode | GetPaintingForbiddenDesc |  | CString | 类别：非常量 |
| SmartMaterialPaintingMode | GetPresetIndex |  | CVector2i | 类别：非常量 |
| SmartMaterialPaintingMode | GetRangeName | Unknown | CUTF8String | 类别：非常量 |
| SmartMaterialPaintingMode | GetTopologyPickerDesc |  | CString | 类别：非常量 |
| SmartMaterialPaintingMode | HasAnyPresets |  | bool |  |
| SmartMaterialPaintingMode | HasDoneAnyChangesToPresets |  | bool |  |
| SmartMaterialPaintingMode | HasOpacityMaskTexture | SmartBrushHeightRange | bool |  |
| SmartMaterialPaintingMode | IsAutosave |  | bool |  |
| SmartMaterialPaintingMode | IsBackgroundProcessing |  | bool |  |
| SmartMaterialPaintingMode | IsCurrentPresetValid |  | bool |  |
| SmartMaterialPaintingMode | IsCurveClipboardEmpty |  | bool |  |
| SmartMaterialPaintingMode | IsDebugActive |  | bool |  |
| SmartMaterialPaintingMode | IsDebugActiveFor | SmartBrushHeightRange | bool |  |
| SmartMaterialPaintingMode | IsDebugTooltipVisible |  | bool |  |
| SmartMaterialPaintingMode | IsDebuggingSinglePoint |  | bool |  |
| SmartMaterialPaintingMode | IsEraserSelected |  | bool |  |
| SmartMaterialPaintingMode | IsEyeDropperSelected |  | bool |  |
| SmartMaterialPaintingMode | IsHeightRangeVisible | SmartBrushHeightRange | bool |  |
| SmartMaterialPaintingMode | IsOpacityMaskTextureLoading | SmartBrushHeightRange | bool |  |
| SmartMaterialPaintingMode | IsPainterSelected |  | bool |  |
| SmartMaterialPaintingMode | IsPaintingForbidden |  | bool |  |
| SmartMaterialPaintingMode | IsPaintingForbiddenTooltipActive |  | bool |  |
| SmartMaterialPaintingMode | IsSelected |  | bool |  |
| SmartMaterialPaintingMode | IsTopologyPickerEnabled |  | bool |  |
| SmartMaterialPaintingMode | IsTopologyPickerTooltipActive |  | bool |  |
| SmartMaterialPaintingMode | IsVisualDebuggingTooltipActive |  | bool |  |
| SmartMaterialPaintingMode | ReloadPresets |  | void |  |
| SmartMaterialPaintingMode | RemoveMaterialEntry | MaterialMix MaterialMixEntry | void |  |
| SmartMaterialPaintingMode | RenamePreset |  | void |  |
| SmartMaterialPaintingMode | ReorderRangeToNext | SmartBrushHeightRange | void |  |
| SmartMaterialPaintingMode | ReorderRangeToPrev | SmartBrushHeightRange | void |  |
| SmartMaterialPaintingMode | SavePresets |  | void |  |
| SmartMaterialPaintingMode | Self |  | SmartMaterialPaintingMode |  |
| SmartMaterialPaintingMode | SetAngleAsString | bool SmartBrushPattern | void |  |
| SmartMaterialPaintingMode | SetBleedingAsString | SmartBrushPattern | void |  |
| SmartMaterialPaintingMode | SetDensityAsString | SmartBrushPattern | void |  |
| SmartMaterialPaintingMode | SetEraserSelected |  | void |  |
| SmartMaterialPaintingMode | SetEyeDropperSelected |  | void |  |
| SmartMaterialPaintingMode | SetHeightRangeName | SmartBrushHeightRange | void |  |
| SmartMaterialPaintingMode | SetInterpolationIndex | SmartBrushPattern | void |  |
| SmartMaterialPaintingMode | SetOpacityMaskOffsetAsString | bool SmartBrushHeightRange | void |  |
| SmartMaterialPaintingMode | SetOpacityMaskRotationAsString | SmartBrushHeightRange | void |  |
| SmartMaterialPaintingMode | SetOpacityMaskScaleAsString | bool SmartBrushHeightRange | void |  |
| SmartMaterialPaintingMode | SetPainterSelected |  | void |  |
| SmartMaterialPaintingMode | SetPatternIndex | SmartBrushPattern bool | void |  |
| SmartMaterialPaintingMode | SetPatternMode | SmartBrushHeightRange int32 | void |  |
| SmartMaterialPaintingMode | SetPresetIndex |  | void |  |
| SmartMaterialPaintingMode | SetSharpnessAsString | SmartBrushPattern | void |  |
| SmartMaterialPaintingMode | ShowMaterialBrowserAndAddToCurrentPattern | SmartBrushPattern | void |  |
| SmartMaterialPaintingMode | ShowMaterialBrowserAndSetEntryInCurrentPattern | SmartBrushPattern MaterialMixEntry | void |  |
| SmartMaterialPaintingMode | StartSampleCompositionEdit | MaterialMix | void |  |
| SmartMaterialPaintingMode | ToggleAutosave |  | void |  |
| SmartMaterialPaintingMode | ToggleDebugActiveFor | SmartBrushHeightRange | void |  |
| SmartMaterialPaintingMode | ToggleHeightRangeVisible | SmartBrushHeightRange | void |  |
| SmartMaterialPaintingMode | ToggleMaterialLock | Material | void |  |
| SmartMaterialPaintingMode | ToggleSampleEntryLock | MaterialMix MaterialMixEntry SmartBrushHeightRange Unknown | void |  |
| SmartMaterialPaintingMode | ToggleTopologyPicker |  | void |  |
| Social | AccessSelf |  | Social | 类别：常量 |
| Social | GetTotalUnreadChatMessages |  | int32 | 类别：非常量 |
| Social | Self |  | Social |  |
| SocialClass | AccessSelf |  | SocialClass | 类别：常量 |
| SocialClass | GetAllowedProfessions |  | Unknown | 类别：非常量 |
| SocialClass | GetAllowedStatusesIn | Country | Unknown | 类别：非常量 |
| SocialClass | GetDesc |  | CString | 类别：非常量 |
| SocialClass | GetEffectsDescIn | Country | CString | 类别：非常量 |
| SocialClass | GetMaxAcceptanceIn | Country | int32 | 类别：非常量 |
| SocialClass | GetMaxAllowedStatusIn | Country | AcceptanceStatus | 类别：非常量 |
| SocialClass | GetMinAcceptanceIn | Country | int32 | 类别：非常量 |
| SocialClass | GetMinAllowedStatusIn | Country | AcceptanceStatus | 类别：非常量 |
| SocialClass | GetName |  | CString | 类别：非常量 |
| SocialClass | GetNameNoFormatting |  | CString | 类别：非常量 |
| SocialClass | GetPopTriggerDesc |  | CString | 类别：非常量 |
| SocialClass | GetSocialHierarchy |  | SocialHierarchy | 类别：非常量 |
| SocialClass | GetStrataConcept |  | CString | 类别：非常量 |
| SocialClass | GetTooltipTag |  | CString | 类别：非常量 |
| SocialClass | GetTotalPopulationIn | Country | int64 | 类别：非常量 |
| SocialClass | HasBoundedAcceptanceIn | Country | bool |  |
| SocialClass | Self |  | SocialClass |  |
| SocialHierarchy | AccessSelf |  | SocialHierarchy | 类别：常量 |
| SocialHierarchy | GetAllSocialClassesDesc |  | CString | 类别：非常量 |
| SocialHierarchy | GetDesc |  | CString | 类别：非常量 |
| SocialHierarchy | GetLowerStrataPopTypesDesc |  | CString | 类别：非常量 |
| SocialHierarchy | GetLowerStrataSocialClasses |  | Unknown | 类别：非常量 |
| SocialHierarchy | GetLowerStrataSocialClassesDesc |  | CString | 类别：非常量 |
| SocialHierarchy | GetMaxSocialClassesInAnyStrata |  | int32 | 类别：非常量 |
| SocialHierarchy | GetMiddleStrataPopTypesDesc |  | CString | 类别：非常量 |
| SocialHierarchy | GetMiddleStrataSocialClasses |  | Unknown | 类别：非常量 |
| SocialHierarchy | GetMiddleStrataSocialClassesDesc |  | CString | 类别：非常量 |
| SocialHierarchy | GetName |  | CString | 类别：非常量 |
| SocialHierarchy | GetNameNoFormatting |  | CString | 类别：非常量 |
| SocialHierarchy | GetPopTriggerDesc |  | CString | 类别：非常量 |
| SocialHierarchy | GetTooltipTag |  | CString | 类别：非常量 |
| SocialHierarchy | GetTotalPopulationIn | Country | int64 | 类别：非常量 |
| SocialHierarchy | GetUpperStrataPopTypesDesc |  | CString | 类别：非常量 |
| SocialHierarchy | GetUpperStrataSocialClasses |  | Unknown | 类别：非常量 |
| SocialHierarchy | GetUpperStrataSocialClassesDesc |  | CString | 类别：非常量 |
| SocialHierarchy | IsDefault |  | bool |  |
| SocialHierarchy | Self |  | SocialHierarchy |  |
| SocialNotificationWindow | AccessChatMessages |  | Unknown | 类别：常量 |
| SocialNotificationWindow | AccessSelf |  | SocialNotificationWindow | 类别：常量 |
| SocialNotificationWindow | GetNotificationsLayoutAnchor |  | Unknown | 类别：非常量 |
| SocialNotificationWindow | Hide |  | void |  |
| SocialNotificationWindow | Self |  | SocialNotificationWindow |  |
| SocialNotificationWindow | ShouldBeShown |  | bool |  |
| SocialNotificationWindow | Show |  | void |  |
| SocialUI | AccessSelf |  | SocialUI | 类别：常量 |
| SocialUI | Hide |  | void |  |
| SocialUI | IsAllowedToBeShown |  | bool |  |
| SocialUI | Self |  | SocialUI |  |
| SocialUI | Show |  | void |  |
| SocialUI | ToggleShow |  | void |  |
| SocialUI | WantsToBeShown |  | bool |  |
| SocialWidget | AccessSelf |  | SocialWidget | 类别：常量 |
| SocialWidget | Self |  | SocialWidget |  |
| SocietyPanel | AccessRepresentativePops |  | Unknown | 类别：常量 |
| SocietyPanel | AccessSelf |  | SocietyPanel | 类别：常量 |
| SocietyPanel | GetPopList |  | PopList | 类别：非常量 |
| SocietyPanel | GetSelectedAcceptanceStatus |  | AcceptanceStatus | 类别：非常量 |
| SocietyPanel | GetSelectedAcceptanceStatusSegment |  | AcceptanceStatusSegment | 类别：非常量 |
| SocietyPanel | IsAcceptanceStatusSelected | Unknown | bool |  |
| SocietyPanel | SelectAcceptanceStatus | Unknown | void |  |
| SocietyPanel | Self |  | SocietyPanel |  |
| SplineAdjustmentTool | AccessSelf |  | SplineAdjustmentTool | 类别：常量 |
| SplineAdjustmentTool | AddAnchorsToAdjacentSelectedPairs |  | void |  |
| SplineAdjustmentTool | CanAddAnchorsInSelection |  | bool |  |
| SplineAdjustmentTool | CanDeleteSelection |  | bool |  |
| SplineAdjustmentTool | DeleteSelected |  | void |  |
| SplineAdjustmentTool | HasMapContent |  | bool |  |
| SplineAdjustmentTool | HasMergeNotes |  | bool |  |
| SplineAdjustmentTool | IsAnchorCreationSelected |  | bool |  |
| SplineAdjustmentTool | IsAnchorSelectionSelected |  | bool |  |
| SplineAdjustmentTool | IsMapContentSelectionSelected |  | bool |  |
| SplineAdjustmentTool | IsNavMeshVisible |  | bool |  |
| SplineAdjustmentTool | IsShowingAllMergeNotes |  | bool |  |
| SplineAdjustmentTool | IsShowingConflictsMergeNotes |  | bool |  |
| SplineAdjustmentTool | SelectAnchorCreation |  | void |  |
| SplineAdjustmentTool | SelectAnchorSelection |  | void |  |
| SplineAdjustmentTool | SelectMapContentSelection |  | void |  |
| SplineAdjustmentTool | Self |  | SplineAdjustmentTool |  |
| SplineAdjustmentTool | ToggleNavMeshVisibility |  | void |  |
| SplineAdjustmentTool | ToggleShowingAllMergeNotes |  | void |  |
| SplineAdjustmentTool | ToggleShowingConflictsMergeNotes |  | void |  |
| SplineAdjustmentToolMode | AccessSelf |  | SplineAdjustmentToolMode | 类别：常量 |
| SplineAdjustmentToolMode | IsSelected |  | bool |  |
| SplineAdjustmentToolMode | Self |  | SplineAdjustmentToolMode |  |
| SplineRiverInteractionMode | AccessSelf |  | SplineRiverInteractionMode | 类别：常量 |
| SplineRiverInteractionMode | IsSelected |  | bool |  |
| SplineRiverInteractionMode | Self |  | SplineRiverInteractionMode |  |
| SplineRiverTool | AccessSelf |  | SplineRiverTool | 类别：常量 |
| SplineRiverTool | GetWidth |  | float | 类别：非常量 |
| SplineRiverTool | ModifyWidth | float | void |  |
| SplineRiverTool | Self |  | SplineRiverTool |  |
| SplineRiverTool | SetWidth |  | void |  |
| SplineRiverTool | SetWidthStr |  | void |  |
| SplineStripTool | AccessSelf |  | SplineStripTool | 类别：常量 |
| SplineStripTool | CanDeleteSelection |  | bool |  |
| SplineStripTool | CheckAllStripsForErrors |  | void |  |
| SplineStripTool | DeleteSelected |  | void |  |
| SplineStripTool | FocusCameraOnSelection |  | void |  |
| SplineStripTool | FocusCameraOnStripError |  | void |  |
| SplineStripTool | GetStripErrorCount |  | int32 | 类别：非常量 |
| SplineStripTool | HasMapContent |  | bool |  |
| SplineStripTool | HasMergeNotes |  | bool |  |
| SplineStripTool | HasSelectedStrips |  | bool |  |
| SplineStripTool | IsAnchorCreationSelected |  | bool |  |
| SplineStripTool | IsAnchorSelectionSelected |  | bool |  |
| SplineStripTool | IsMapContentSelectionSelected |  | bool |  |
| SplineStripTool | IsNavMeshVisible |  | bool |  |
| SplineStripTool | IsShowingAllMergeNotes |  | bool |  |
| SplineStripTool | IsShowingConflictsMergeNotes |  | bool |  |
| SplineStripTool | IsStripCreationSelected |  | bool |  |
| SplineStripTool | IsStripSelectionSelected |  | bool |  |
| SplineStripTool | SelectAnchorCreation |  | void |  |
| SplineStripTool | SelectAnchorSelection |  | void |  |
| SplineStripTool | SelectMapContentSelection |  | void |  |
| SplineStripTool | SelectStripCreation |  | void |  |
| SplineStripTool | SelectStripSelection |  | void |  |
| SplineStripTool | Self |  | SplineStripTool |  |
| SplineStripTool | ToggleNavMeshVisibility |  | void |  |
| SplineStripTool | ToggleShowingAllMergeNotes |  | void |  |
| SplineStripTool | ToggleShowingConflictsMergeNotes |  | void |  |
| SplineStripToolMode | AccessSelf |  | SplineStripToolMode | 类别：常量 |
| SplineStripToolMode | IsSelected |  | bool |  |
| SplineStripToolMode | Self |  | SplineStripToolMode |  |
| SplineToolsMapContentPanel | AccessSelf |  | SplineToolsMapContentPanel | 类别：常量 |
| SplineToolsMapContentPanel | AutoPlaceHubAnchors |  | void |  |
| SplineToolsMapContentPanel | HasMapContent |  | bool |  |
| SplineToolsMapContentPanel | Self |  | SplineToolsMapContentPanel |  |
| SplineTypeCreateSelectionDropdown | AccessSelf |  | SplineTypeCreateSelectionDropdown | 类别：常量 |
| SplineTypeCreateSelectionDropdown | IsSplineTypeSelected | uint8 | bool |  |
| SplineTypeCreateSelectionDropdown | SelectSplineType | uint8 | void |  |
| SplineTypeCreateSelectionDropdown | Self |  | SplineTypeCreateSelectionDropdown |  |
| SplineTypeCreateSelectionDropdown | SplineTypes |  | Unknown |  |
| SplineTypeCreateSelectionDropdown | Toggle |  | void |  |
| SplineTypeItem | AccessSelf |  | SplineTypeItem | 类别：常量 |
| SplineTypeItem | GetId |  | uint8 | 类别：非常量 |
| SplineTypeItem | GetName |  | CString | 类别：非常量 |
| SplineTypeItem | Self |  | SplineTypeItem |  |
| SplineTypeSwitchSelectionDropdown | AccessSelf |  | SplineTypeSwitchSelectionDropdown | 类别：常量 |
| SplineTypeSwitchSelectionDropdown | ChangeSelectedStripsType | uint8 | void |  |
| SplineTypeSwitchSelectionDropdown | IsSplineTypeSelected | Unknown | bool |  |
| SplineTypeSwitchSelectionDropdown | Self |  | SplineTypeSwitchSelectionDropdown |  |
| SplineTypeSwitchSelectionDropdown | SplineTypes |  | Unknown |  |
| SplineTypeSwitchSelectionDropdown | Toggle |  | void |  |
| SplineVisibilityDropdown | AccessSelf |  | SplineVisibilityDropdown | 类别：常量 |
| SplineVisibilityDropdown | IsVisibilityModeAll |  | bool |  |
| SplineVisibilityDropdown | IsVisibilityModeFirst |  | bool |  |
| SplineVisibilityDropdown | IsVisibilityModeLast |  | bool |  |
| SplineVisibilityDropdown | Self |  | SplineVisibilityDropdown |  |
| SplineVisibilityDropdown | SetVisibilityModeToAll |  | void |  |
| SplineVisibilityDropdown | SetVisibilityModeToFirst |  | void |  |
| SplineVisibilityDropdown | SetVisibilityModeToLast |  | void |  |
| SplineVisibilityDropdown | Toggle |  | void |  |
| StagedCommanderTransfer | AccessSelf |  | StagedCommanderTransfer | 类别：常量 |
| StagedCommanderTransfer | GetCommander |  | Character | 类别：非常量 |
| StagedCommanderTransfer | GetInvalidTransferDesc |  | CString | 类别：非常量 |
| StagedCommanderTransfer | HasMoved |  | bool |  |
| StagedCommanderTransfer | Self |  | StagedCommanderTransfer |  |
| StagedFormation | AccessSelf |  | StagedFormation | 类别：常量 |
| StagedFormation | GetCommandLimit |  | CString | 类别：非常量 |
| StagedFormation | GetCommandLimitRaw |  | int32 | 类别：非常量 |
| StagedFormation | GetCommandLimitRawIfTransferred |  | int32 | 类别：非常量 |
| StagedFormation | GetCommanders |  | Unknown | 类别：非常量 |
| StagedFormation | GetFormationResultBreakdown |  | CString | 类别：非常量 |
| StagedFormation | GetHQs |  | Unknown | 类别：非常量 |
| StagedFormation | GetIDString |  | CString | 类别：非常量 |
| StagedFormation | GetIDStringForUnitType | StagedUnitsWithType | CString | 类别：非常量 |
| StagedFormation | GetMilitaryFormation |  | MilitaryFormation | 类别：非常量 |
| StagedFormation | GetName |  | CString | 类别：非常量 |
| StagedFormation | GetNumCombatUnits |  | int32 | 类别：非常量 |
| StagedFormation | GetNumCombatUnitsIfTransferred |  | int32 | 类别：非常量 |
| StagedFormation | GetNumConscriptsFromHQ | Hq | int32 | 类别：非常量 |
| StagedFormation | GetNumConscriptsFromState | State | int32 | 类别：非常量 |
| StagedFormation | GetNumRegularsFromHQ | Hq | int32 | 类别：非常量 |
| StagedFormation | GetNumRegularsFromState | State | int32 | 类别：非常量 |
| StagedFormation | GetResultingNumbersDesc |  | CString | 类别：非常量 |
| StagedFormation | GetStates |  | Unknown | 类别：非常量 |
| StagedFormation | GetUnitTypes |  | Unknown | 类别：非常量 |
| StagedFormation | HasValidFormation |  | bool |  |
| StagedFormation | IsAllSelectedFromHQ | Hq | bool |  |
| StagedFormation | IsAllSelectedFromState | State | bool |  |
| StagedFormation | IsFormationSelected | Unknown | bool |  |
| StagedFormation | Self |  | StagedFormation |  |
| StagedFormation | ToggleSelectionOnAllFromHQ | Hq | void |  |
| StagedFormation | ToggleSelectionOnAllFromState | State | void |  |
| StagedUnitsWithType | AccessSelf |  | StagedUnitsWithType | 类别：常量 |
| StagedUnitsWithType | CanMoveConscriptsToStaged |  | bool |  |
| StagedUnitsWithType | CanMoveRegularsToStaged |  | bool |  |
| StagedUnitsWithType | ClearStateFilter |  | void |  |
| StagedUnitsWithType | GetInvalidConscriptTransferDesc |  | CString | 类别：非常量 |
| StagedUnitsWithType | GetInvalidRegularTransferDesc |  | CString | 类别：非常量 |
| StagedUnitsWithType | GetNumCombatUnits |  | int32 | 类别：非常量 |
| StagedUnitsWithType | GetNumConscripts |  | int32 | 类别：非常量 |
| StagedUnitsWithType | GetNumConscriptsInState | State | int32 | 类别：非常量 |
| StagedUnitsWithType | GetNumFilteredConscripts |  | int32 | 类别：非常量 |
| StagedUnitsWithType | GetNumFilteredRegulars |  | int32 | 类别：非常量 |
| StagedUnitsWithType | GetNumRegulars |  | int32 | 类别：非常量 |
| StagedUnitsWithType | GetNumRegularsInState | State | int32 | 类别：非常量 |
| StagedUnitsWithType | GetNumSelectedConscripts |  | int32 | 类别：非常量 |
| StagedUnitsWithType | GetNumSelectedRegulars |  | int32 | 类别：非常量 |
| StagedUnitsWithType | GetStagedCombatUnitStates |  | Unknown | 类别：非常量 |
| StagedUnitsWithType | GetStagedCombatUnits |  | Unknown | 类别：非常量 |
| StagedUnitsWithType | GetStagedCombatUnitsInState | State | Unknown | 类别：非常量 |
| StagedUnitsWithType | GetStateFilter |  | State | 类别：非常量 |
| StagedUnitsWithType | GetUnitType |  | CombatUnitType | 类别：非常量 |
| StagedUnitsWithType | HasMoved |  | bool |  |
| StagedUnitsWithType | HasStateFilter |  | bool |  |
| StagedUnitsWithType | IsUnitSelected | CombatUnit | bool |  |
| StagedUnitsWithType | OnConscriptsEditboxValueChanged |  | void |  |
| StagedUnitsWithType | OnConscriptsSliderValueChanged |  | void |  |
| StagedUnitsWithType | OnRegularsEditboxValueChanged |  | void |  |
| StagedUnitsWithType | OnRegularsSliderValueChanged |  | void |  |
| StagedUnitsWithType | Self |  | StagedUnitsWithType |  |
| StagedUnitsWithType | SetStateFilter | Unknown | void |  |
| StagedUnitsWithType | ToggleUnitSelected | CombatUnit | void |  |
| StarvationType | AccessSelf |  | StarvationType | 类别：const |
| StarvationType | GetColor |  | CVector4f | 类别：nonconst |
| StarvationType | GetIcon |  | Unknown | 类别：nonconst |
| StarvationType | GetName |  | CString | 类别：nonconst |
| StarvationType | IsMild |  | bool |  |
| StarvationType | IsSevere |  | bool |  |
| StarvationType | Self |  | StarvationType |  |
| State | AbandonColony |  | Command |  |
| State | AccessAllBuiltRuralBuildings |  | Unknown | 类别：const |
| State | AccessBuilding | BuildingType | Building | 类别：const |
| State | AccessBuildings |  | Unknown | 类别：const |
| State | AccessCappedRuralBuildings |  | Unknown | 类别：const |
| State | AccessDecrees |  | Unknown | 类别：const |
| State | AccessDevelopmentBuildings |  | Unknown | 类别：const |
| State | AccessMarket |  | Market | 类别：const |
| State | AccessModifier |  | Modifier | 类别：const |
| State | AccessOwner |  | Country | 类别：const |
| State | AccessPopCultures |  | Unknown | 类别：const |
| State | AccessPopInterestGroups |  | Unknown | 类别：const |
| State | AccessPopReligions |  | Unknown | 类别：const |
| State | AccessPopTypes |  | Unknown | 类别：const |
| State | AccessPopsList |  | PopList | 类别：const |
| State | AccessSelf |  | State | 类别：const |
| State | AccessShippingLanesFromThisState | Province | Unknown | 类别：const |
| State | AccessShippingLanesOnlyGoodsTransferFromThisState | Province | Unknown | 类别：const |
| State | AccessShippingLanesOnlyPortConnectionsFromThisState | Province | Unknown | 类别：const |
| State | AccessShippingLanesOnlySupplyRoutesFromThisState | Province | Unknown | 类别：const |
| State | AccessSubsistenceBuilding |  | Building | 类别：const |
| State | AccessUncappedRuralBuildings |  | Unknown | 类别：const |
| State | AccessUrbanBuildings |  | Unknown | 类别：const |
| State | CalcPopInstitutionBureaucracyCost |  | CFixedPoint |  |
| State | CalcSupplyToDemandRatio | Goods | CFixedPoint |  |
| State | CalcTaxCapacity |  | CFixedPoint |  |
| State | CalcTaxCapacityBalance |  | CFixedPoint |  |
| State | CalcTaxCapacityUsage |  | CFixedPoint |  |
| State | CalcTurmoil |  | CFixedPoint |  |
| State | GetAdditionalSOLFactorsDescAll |  | CString | 类别：nonconst |
| State | GetAdditionalSOLFactorsDescMiddle |  | CString | 类别：nonconst |
| State | GetAdditionalSOLFactorsDescPoor |  | CString | 类别：nonconst |
| State | GetAdditionalSOLFactorsDescRich |  | CString | 类别：nonconst |
| State | GetAnnualPopNetMigration |  | int64 | 类别：nonconst |
| State | GetArableLandCapacity |  | int32 | 类别：nonconst |
| State | GetAverageAnnualWage |  | CFixedPoint | 类别：nonconst |
| State | GetAverageAnnualWageDesc |  | CString | 类别：nonconst |
| State | GetAverageStandardOfLivingAll |  | CFixedPoint | 类别：nonconst |
| State | GetAverageStandardOfLivingMiddle |  | CFixedPoint | 类别：nonconst |
| State | GetAverageStandardOfLivingPoor |  | CFixedPoint | 类别：nonconst |
| State | GetAverageStandardOfLivingRich |  | CFixedPoint | 类别：nonconst |
| State | GetBaseBureaucracyCostRaw |  | CFixedPoint | 类别：nonconst |
| State | GetBasePopBureaucracyCostRaw |  | CFixedPoint | 类别：nonconst |
| State | GetBestTexture |  | Unknown | 类别：nonconst |
| State | GetBestTextureEffect |  | CString | 类别：nonconst |
| State | GetBlockadeEffectsDesc |  | CString | 类别：nonconst |
| State | GetBlockadeLevel |  | CFixedPoint | 类别：nonconst |
| State | GetBuilding | BuildingType | Building | 类别：nonconst |
| State | GetBuildingsWithGovernmentExpenses |  | Unknown | 类别：nonconst |
| State | GetBuildingsWithTaxationRevenue |  | Unknown | 类别：nonconst |
| State | GetBureaucracyCost |  | CFixedPoint | 类别：nonconst |
| State | GetBureaucracyCostDesc |  | CString | 类别：nonconst |
| State | GetCapitalEffectsDesc |  | CString | 类别：nonconst |
| State | GetCityHubName |  | CString | 类别：nonconst |
| State | GetClaimsDesc |  | CString | 类别：nonconst |
| State | GetColonizers | CString | CString | 类别：nonconst |
| State | GetColonyCompany |  | Company | 类别：nonconst |
| State | GetColonyGrowthDateDesc |  | CString | 类别：nonconst |
| State | GetColonyGrowthModifierDesc |  | CString | 类别：nonconst |
| State | GetColonyProgress |  | CFixedPoint | 类别：nonconst |
| State | GetColonyProgressAsDays |  | int32 | 类别：nonconst |
| State | GetColonyProgressAsFloat |  | float | 类别：nonconst |
| State | GetColonyProvinceProgressDesc |  | CString | 类别：nonconst |
| State | GetColonyTransferName |  | CString | 类别：nonconst |
| State | GetColor |  | CVector4f | 类别：nonconst |
| State | GetConscriptionLimit |  | int32 | 类别：nonconst |
| State | GetConscriptionLimitDesc |  | CString | 类别：nonconst |
| State | GetConstructionEfficiency |  | CFixedPoint | 类别：nonconst |
| State | GetConstructionEfficiencyForBuildingType | BuildingType | CFixedPoint | 类别：nonconst |
| State | GetConstructionEfficiencyForBuildingTypeTooltip | BuildingType | CString | 类别：nonconst |
| State | GetConstructionEfficiencyTooltip |  | CString | 类别：nonconst |
| State | GetController |  | Country | 类别：nonconst |
| State | GetCountry |  | Country | 类别：nonconst |
| State | GetCulturalCommunities |  | Unknown | 类别：nonconst |
| State | GetCurrentBlockadeStrength |  | CFixedPoint | 类别：nonconst |
| State | GetCustom | CustomLocalization | CString | 类别：nonconst |
| State | GetDailyColonyProgress |  | CFixedPoint | 类别：nonconst |
| State | GetDevastationDailyChange |  | CFixedPoint | 类别：nonconst |
| State | GetDevastationDailyChangeBreakdown |  | CString | 类别：nonconst |
| State | GetDevastationEffects |  | CString | 类别：nonconst |
| State | GetDevastationLevel |  | CFixedPoint | 类别：nonconst |
| State | GetEnemyWithHighestOccupation |  | Country | 类别：nonconst |
| State | GetExpectedSOLFactorsDescAll |  | CString | 类别：nonconst |
| State | GetExpectedSOLFactorsDescMiddle |  | CString | 类别：nonconst |
| State | GetExpectedSOLFactorsDescPoor |  | CString | 类别：nonconst |
| State | GetExpectedSOLFactorsDescRich |  | CString | 类别：nonconst |
| State | GetExpectedStandardOfLivingAll |  | CFixedPoint | 类别：nonconst |
| State | GetExpectedStandardOfLivingMiddle |  | CFixedPoint | 类别：nonconst |
| State | GetExpectedStandardOfLivingPoor |  | CFixedPoint | 类别：nonconst |
| State | GetExpectedStandardOfLivingRich |  | CFixedPoint | 类别：nonconst |
| State | GetExportRevenue | Goods | CFixedPoint | 类别：nonconst |
| State | GetExportedAmount | Goods | CFixedPoint | 类别：nonconst |
| State | GetExports |  | Unknown | 类别：nonconst |
| State | GetFamineDesc |  | CString | 类别：nonconst |
| State | GetFarmHubName |  | CString | 类别：nonconst |
| State | GetForestryHubName |  | CString | 类别：nonconst |
| State | GetFormattedStandardOfLivingAll |  | CString | 类别：nonconst |
| State | GetFormattedStandardOfLivingLabelAll |  | CString | 类别：nonconst |
| State | GetFormattedStandardOfLivingLabelMiddle |  | CString | 类别：nonconst |
| State | GetFormattedStandardOfLivingLabelPoor |  | CString | 类别：nonconst |
| State | GetFormattedStandardOfLivingLabelRich |  | CString | 类别：nonconst |
| State | GetFormattedStandardOfLivingMiddle |  | CString | 类别：nonconst |
| State | GetFormattedStandardOfLivingPoor |  | CString | 类别：nonconst |
| State | GetFormattedStandardOfLivingRich |  | CString | 类别：nonconst |
| State | GetFreeArableLandAfterInactiveQueuedEntry |  | CString | 类别：nonconst |
| State | GetGDPContribution |  | CFixedPoint | 类别：nonconst |
| State | GetGDPContributionPercentage |  | CFixedPoint | 类别：nonconst |
| State | GetGDPGoodsContribution | Unknown | CFixedPoint | 类别：nonconst |
| State | GetGDPGoodsContributionBreakdown |  | CString | 类别：nonconst |
| State | GetGDPGoodsContributionPercentage | Unknown | CFixedPoint | 类别：nonconst |
| State | GetGdpRatioOwnedBy | Unknown | CFixedPoint | 类别：nonconst |
| State | GetGdpRatioOwnedByDesc | Country | CString | 类别：nonconst |
| State | GetGoodsSortedByGDP |  | Unknown | 类别：nonconst |
| State | GetGovernmentExpenses |  | CFixedPoint | 类别：nonconst |
| State | GetHarvestConditions |  | Unknown | 类别：nonconst |
| State | GetHomelandsDesc |  | CString | 类别：nonconst |
| State | GetID |  | int32 | 类别：nonconst |
| State | GetIDString |  | CString | 类别：nonconst |
| State | GetImportRevenue | Goods | CFixedPoint | 类别：nonconst |
| State | GetImportedAmount | Goods | CFixedPoint | 类别：nonconst |
| State | GetImports |  | Unknown | 类别：nonconst |
| State | GetIncorporationPartialEffectsDesc |  | CString | 类别：nonconst |
| State | GetIncorporationProgress |  | CFixedPoint | 类别：nonconst |
| State | GetIncorporationTimeDesc |  | CString | 类别：nonconst |
| State | GetIncorporationTimeLeft |  | CString | 类别：nonconst |
| State | GetInfrastructure |  | CFixedPoint | 类别：nonconst |
| State | GetInfrastructureBalance |  | CFixedPoint | 类别：nonconst |
| State | GetInfrastructureDesc |  | CString | 类别：nonconst |
| State | GetInfrastructureUsage |  | CFixedPoint | 类别：nonconst |
| State | GetInfrastructureUsageDesc |  | CString | 类别：nonconst |
| State | GetInsufficientQualificationsForAvailablePositionsDesc |  | CString | 类别：nonconst |
| State | GetInvasions |  | Unknown | 类别：nonconst |
| State | GetJobseekersDesc |  | CString | 类别：nonconst |
| State | GetLiteracy |  | CFixedPoint | 类别：nonconst |
| State | GetMarket |  | Market | 类别：nonconst |
| State | GetMarketAccess |  | CFixedPoint | 类别：nonconst |
| State | GetMarketAccessDesc |  | CString | 类别：nonconst |
| State | GetMarketAccessStatus |  | CString | 类别：nonconst |
| State | GetMarketCapitalEffectsDesc |  | CString | 类别：nonconst |
| State | GetMassMigrationCulture |  | Culture | 类别：nonconst |
| State | GetMassMigrationEndDate |  | CString | 类别：nonconst |
| State | GetMassMigrationOriginCountry |  | Country | 类别：nonconst |
| State | GetMaxBattalions |  | int32 | 类别：nonconst |
| State | GetMaxImbalance |  | CFixedPoint | 类别：nonconst |
| State | GetMaxImbalanceScaledByBasePrice |  | CFixedPoint | 类别：nonconst |
| State | GetMaxPotentialFor | Building | int32 | 类别：nonconst |
| State | GetMigrationAndSlaveTradeDetailsDesc |  | CString | 类别：nonconst |
| State | GetMigrationDesc |  | CString | 类别：nonconst |
| State | GetMigrationDetailsDesc |  | CString | 类别：nonconst |
| State | GetMigrationLabel |  | CString | 类别：nonconst |
| State | GetMigrationPull |  | CFixedPoint | 类别：nonconst |
| State | GetMigrationPullDesc |  | CString | 类别：nonconst |
| State | GetMineHubName |  | CString | 类别：nonconst |
| State | GetModifier |  | Modifier | 类别：nonconst |
| State | GetName |  | CString | 类别：nonconst |
| State | GetNameNoFormatting |  | CString | 类别：nonconst |
| State | GetNameWithCountryFlag |  | CString | 类别：nonconst |
| State | GetNextColonyProvince |  | Province | 类别：nonconst |
| State | GetNonPotentialDiploPlays |  | Unknown | 类别：nonconst |
| State | GetNumArableLandReservedForSubsistence |  | int32 | 类别：nonconst |
| State | GetNumBaseFreeArableLand |  | int32 | 类别：nonconst |
| State | GetNumBuildingsAffectedByGoodsShortage |  | int32 | 类别：nonconst |
| State | GetNumColonizers |  | int32 | 类别：nonconst |
| State | GetNumConstructableUrbanBuildings |  | int32 | 类别：nonconst |
| State | GetNumConsumed | Goods | CFixedPoint | 类别：nonconst |
| State | GetNumFreeArableLand |  | int32 | 类别：nonconst |
| State | GetNumInactiveQueuedArableLandEntry |  | CString | 类别：nonconst |
| State | GetNumJobseekers |  | int64 | 类别：nonconst |
| State | GetNumLoyalists |  | int64 | 类别：nonconst |
| State | GetNumObstinanceSupporters |  | int64 | 类别：nonconst |
| State | GetNumOfObstinatePopsFromMovement | Unknown | int64 | 类别：nonconst |
| State | GetNumProduced | Goods | CFixedPoint | 类别：nonconst |
| State | GetNumProvinces |  | int32 | 类别：nonconst |
| State | GetNumRadicals |  | int64 | 类别：nonconst |
| State | GetNumSubsistenceWorkingAdults |  | int64 | 类别：nonconst |
| State | GetNumUnemployedWorkingAdults |  | int64 | 类别：nonconst |
| State | GetNumUsedArableLand |  | int32 | 类别：nonconst |
| State | GetNumUsedArableLandFullyBuilt |  | int32 | 类别：nonconst |
| State | GetNumUsedArableLandFullyBuiltEntry |  | CString | 类别：nonconst |
| State | GetNumUsedArableLandUnderConstruction |  | int32 | 类别：nonconst |
| State | GetNumUsedArableLandUnderConstructionEntry |  | CString | 类别：nonconst |
| State | GetNumberOfPopsMiddle |  | int64 | 类别：nonconst |
| State | GetNumberOfPopsPoor |  | int64 | 类别：nonconst |
| State | GetNumberOfPopsRich |  | int64 | 类别：nonconst |
| State | GetObstinance |  | CFixedPoint | 类别：nonconst |
| State | GetObstinanceDesc |  | CString | 类别：nonconst |
| State | GetObstinanceEffectScale |  | CFixedPoint | 类别：nonconst |
| State | GetObstinanceEffectsDesc |  | CString | 类别：nonconst |
| State | GetObstinanceFromMovement | Unknown | CFixedPoint | 类别：nonconst |
| State | GetOccupant |  | Country | 类别：nonconst |
| State | GetOccupantsTooltip |  | CString | 类别：nonconst |
| State | GetOccupationPiechartData |  | Unknown | 类别：nonconst |
| State | GetOwner |  | Country | 类别：nonconst |
| State | GetPlanInvasionDesc |  | CString | 类别：nonconst |
| State | GetPolStrForCulture | Culture | int64 | 类别：nonconst |
| State | GetPolStrForReligion | Religion | int64 | 类别：nonconst |
| State | GetPollutionGeneration |  | CFixedPoint | 类别：nonconst |
| State | GetPollutionGenerationDesc |  | CString | 类别：nonconst |
| State | GetPollutionHealthEffectsReduction |  | CFixedPoint | 类别：nonconst |
| State | GetPollutionHealthEffectsReductionDesc |  | CString | 类别：nonconst |
| State | GetPopBirthrate |  | CFixedPoint | 类别：nonconst |
| State | GetPopCultureDesc |  | CString | 类别：nonconst |
| State | GetPopCultureDescByIndex | Unknown | CString | 类别：nonconst |
| State | GetPopGrowthDesc |  | CString | 类别：nonconst |
| State | GetPopMortality |  | CFixedPoint | 类别：nonconst |
| State | GetPopNetGrowth |  | int64 | 类别：nonconst |
| State | GetPopReligionDesc |  | CString | 类别：nonconst |
| State | GetPopReligionDescByIndex | Unknown | CString | 类别：nonconst |
| State | GetPopTotalChange |  | int64 | 类别：nonconst |
| State | GetPops |  | Unknown | 类别：nonconst |
| State | GetPopulationForCulture | Culture | int64 | 类别：nonconst |
| State | GetPopulationForReligion | Religion | int64 | 类别：nonconst |
| State | GetPopulationRatioBelowExpectedStandardOfLiving |  | CFixedPoint | 类别：nonconst |
| State | GetPopulationSize |  | int64 | 类别：nonconst |
| State | GetPortHubName |  | CString | 类别：nonconst |
| State | GetPotentialDecrees |  | Unknown | 类别：nonconst |
| State | GetPotentialDiploPlays |  | Unknown | 类别：nonconst |
| State | GetPotentialLabor |  | int64 | 类别：nonconst |
| State | GetPotentialPopTypeQualificationsDesc |  | CString | 类别：nonconst |
| State | GetPotentialProductionForCountry | Goods Country | CFixedPoint | 类别：nonconst |
| State | GetPotentialProductionForCountryDesc | Goods Country | CString | 类别：nonconst |
| State | GetPotentialQualifications | PopType | int64 | 类别：nonconst |
| State | GetPotentialQualificationsBreakdown | PopType | CString | 类别：nonconst |
| State | GetPotentialQualificationsDesc |  | CString | 类别：nonconst |
| State | GetPotentialUrbanBuildings |  | Unknown | 类别：nonconst |
| State | GetProductionInfo |  | Unknown | 类别：nonconst |
| State | GetRequiredBlockadeStrength |  | CFixedPoint | 类别：nonconst |
| State | GetSamplePops |  | Unknown | 类别：nonconst |
| State | GetSlaveExportMarkersDesc |  | CString | 类别：nonconst |
| State | GetSlaveImportMarkerDesc |  | CString | 类别：nonconst |
| State | GetSlaveTradeDetailsDesc |  | CString | 类别：nonconst |
| State | GetStateRegion |  | StateRegion | 类别：nonconst |
| State | GetSubsistenceBuilding |  | Building | 类别：nonconst |
| State | GetTaxCapacityDesc |  | CString | 类别：nonconst |
| State | GetTaxCapacityEffectsDesc |  | CString | 类别：nonconst |
| State | GetTaxCapacityUsageDesc |  | CString | 类别：nonconst |
| State | GetTaxationRevenue |  | CFixedPoint | 类别：nonconst |
| State | GetTheater | Unknown | Theater | 类别：nonconst |
| State | GetTimedModifiers |  | Unknown | 类别：nonconst |
| State | GetTimedModifiersBreakdown |  | CString | 类别：nonconst |
| State | GetTooltipTag |  | CString | 类别：nonconst |
| State | GetTotalConsumption |  | CFixedPoint | 类别：nonconst |
| State | GetTotalConvoysFromShippingLanesViaState | Province | int32 | 类别：nonconst |
| State | GetTotalExportRevenue |  | CFixedPoint | 类别：nonconst |
| State | GetTotalExportedAmount |  | CFixedPoint | 类别：nonconst |
| State | GetTotalImportRevenue |  | CFixedPoint | 类别：nonconst |
| State | GetTotalImportedAmount |  | CFixedPoint | 类别：nonconst |
| State | GetTotalLabor |  | int64 | 类别：nonconst |
| State | GetTotalPolStr |  | int64 | 类别：nonconst |
| State | GetTotalPortConnectionsViaState | Province | int32 | 类别：nonconst |
| State | GetTotalProduction |  | CFixedPoint | 类别：nonconst |
| State | GetTradeCapacity |  | int32 | 类别：nonconst |
| State | GetTradeCapacityBalance |  | int32 | 类别：nonconst |
| State | GetTradeCapacityDesc |  | CString | 类别：nonconst |
| State | GetTradeCapacityUsage |  | int32 | 类别：nonconst |
| State | GetTradeCapacityUsageDesc |  | CString | 类别：nonconst |
| State | GetTradePotential |  | CFixedPoint | 类别：nonconst |
| State | GetTradePotentialDesc |  | CString | 类别：nonconst |
| State | GetTurmoilEffects |  | CString | 类别：nonconst |
| State | GetUrbanization |  | int32 | 类别：nonconst |
| State | GetUrbanizationBuildingsMaxLevelDesc |  | CString | 类别：nonconst |
| State | GetUrbanizationDesc |  | CString | 类别：nonconst |
| State | GetUrbanizationNeededPerLevelFormatted |  | CString | 类别：nonconst |
| State | GetUrbanizationNeededPerLevelRaw |  | int32 | 类别：nonconst |
| State | GetWeeklyEmigration |  | int64 | 类别：nonconst |
| State | GetWeeklyImmigration |  | int64 | 类别：nonconst |
| State | GetWeeklyPopNetMigration |  | int64 | 类别：nonconst |
| State | GetWeeklySlaveExport |  | int64 | 类别：nonconst |
| State | GetWeeklySlaveImport |  | int64 | 类别：nonconst |
| State | GetWorldMarketAccess |  | CFixedPoint | 类别：nonconst |
| State | GetWorldMarketAccessDesc |  | CString | 类别：nonconst |
| State | GetWorldMarketAccessFormatted |  | CString | 类别：nonconst |
| State | GetYearlyGDP |  | CFixedPoint | 类别：nonconst |
| State | GetYearsToIncorporate |  | CFixedPoint | 类别：nonconst |
| State | HasAnyGoodsShortage |  | bool |  |
| State | HasBuildingGoodsShortage | Unknown | bool |  |
| State | HasClaims |  | bool |  |
| State | HasConstructionQueued |  | bool |  |
| State | HasDevastation |  | bool |  |
| State | HasDiscoverableResources |  | bool |  |
| State | HasFamine |  | bool |  |
| State | HasGoodsShortage | Unknown | bool |  |
| State | HasHomelands |  | bool |  |
| State | HasInsufficientQualificationsForAvailablePositions |  | bool |  |
| State | HasOccupation |  | bool |  |
| State | HasPopGoodsShortage | Unknown | bool |  |
| State | HasSlaveExportMarkers |  | bool |  |
| State | HasTimedModifiers |  | bool |  |
| State | HasTurmoilEffects |  | bool |  |
| State | IncorporateState |  | Command |  |
| State | IsBeingColonized |  | bool |  |
| State | IsBeingHighlighted |  | bool |  |
| State | IsBeingTutorialHighlighted |  | bool |  |
| State | IsCapitalState |  | bool |  |
| State | IsCoastal |  | bool |  |
| State | IsColonizationPaused |  | bool |  |
| State | IsColonyProgressBlockedByInactiveInterest |  | bool |  |
| State | IsCompanyColony |  | bool |  |
| State | IsContested |  | bool |  |
| State | IsEligibleForMassMigration |  | bool |  |
| State | IsFullyOccupied |  | bool |  |
| State | IsGrowingColony |  | bool |  |
| State | IsImportingSlaves |  | bool |  |
| State | IsIncorporated |  | bool |  |
| State | IsIncorporating |  | bool |  |
| State | IsIsolatedFromMarket |  | bool |  |
| State | IsMarketCapital |  | bool |  |
| State | IsMassMigrationTarget |  | bool |  |
| State | IsOwner | Country | bool |  |
| State | IsPinnedInOutliner |  | bool |  |
| State | IsSlaveState |  | bool |  |
| State | IsSplitState |  | bool |  |
| State | IsStrategicObjective | Country | bool |  |
| State | IsTreatyPort |  | bool |  |
| State | IsUnincorporated |  | bool |  |
| State | IsValid |  | bool |  |
| State | IsValidInvasionTarget |  | bool |  |
| State | IsWorldMarketHub |  | bool |  |
| State | IsZoomingToCapital |  | bool |  |
| State | MakeScope |  | Scope |  |
| State | PanCamera |  | void |  |
| State | PredictBureaucracyCost |  | CFixedPoint |  |
| State | Self |  | State |  |
| State | SortBuildings | Unknown | void |  |
| State | SortBuildingsWithOrder | Unknown Unknown | void |  |
| State | TogglePauseColonization |  | Command |  |
| State | TogglePinInOutliner |  | void |  |
| State | UnincorporatedState |  | Command |  |
| State | UnincorporateState |  | Command |  |
| State | ZoomExtraCloseToCapital |  | void |  |
| State | ZoomToCapital |  | void |  |
| StateGoods | AccessSelf |  | StateGoods | 类别：const |
| StateGoods | GetBreakdownOfBuildingsAffectedByShortage |  | CString | 类别：nonconst |
| StateGoods | GetCustom | CustomLocalization | CString | 类别：nonconst |
| StateGoods | GetGoods |  | Goods | 类别：nonconst |
| StateGoods | GetIDString |  | CString | 类别：nonconst |
| StateGoods | GetNumBuildingsAffectedByShortage |  | int32 | 类别：nonconst |
| StateGoods | GetState |  | State | 类别：nonconst |
| StateGoods | GetTooltipTag |  | CString | 类别：nonconst |
| StateGoods | MakeScope |  | Scope |  |
| StateGoods | Self |  | StateGoods |  |
| StateInfraMarker | AccessSelf |  | StateInfraMarker | 类别：const |
| StateInfraMarker | GetPosition |  | CVector2f | 类别：nonconst |
| StateInfraMarker | GetState |  | State | 类别：nonconst |
| StateInfraMarker | GetTooltip |  | CString | 类别：nonconst |
| StateInfraMarker | IsConnectedMarker |  | bool |  |
| StateInfraMarker | Self |  | StateInfraMarker |  |
| StateMarker | AccessSelf |  | StateMarker | 类别：const |
| StateMarker | GetGoods |  | Goods | 类别：nonconst |
| StateMarker | GetState |  | State | 类别：nonconst |
| StateMarker | Self |  | StateMarker |  |
| StateNameChangePopup | AccessSelf |  | StateNameChangePopup | 类别：const |
| StateNameChangePopup | Confirm |  | Command |  |
| StateNameChangePopup | GetState |  | State | 类别：nonconst |
| StateNameChangePopup | OnEditCityName |  | void |  |
| StateNameChangePopup | OnEditFarmName |  | void |  |
| StateNameChangePopup | OnEditMineName |  | void |  |
| StateNameChangePopup | OnEditName |  | void |  |
| StateNameChangePopup | OnEditPortName |  | void |  |
| StateNameChangePopup | OnEditWoodName |  | void |  |
| StateNameChangePopup | Self |  | StateNameChangePopup |  |
| StateNameChangePopup | ShouldHaveCityHub |  | bool |  |
| StateNameChangePopup | ShouldHaveFarmHub |  | bool |  |
| StateNameChangePopup | ShouldHaveMineHub |  | bool |  |
| StateNameChangePopup | ShouldHavePortHub |  | bool |  |
| StateNameChangePopup | ShouldHaveWoodHub |  | bool |  |
| StatePopulationPanel | AccessSelf |  | StatePopulationPanel | 类别：const |
| StatePopulationPanel | AccessState |  | State | 类别：const |
| StatePopulationPanel | GetState |  | State | 类别：nonconst |
| StatePopulationPanel | Self |  | StatePopulationPanel |  |
| StateRegion | AccessLargestStateOwner |  | Country | 类别：const |
| StateRegion | AccessSelf |  | StateRegion | 类别：const |
| StateRegion | AccessStrategicRegion |  | StrategicRegion | 类别：const |
| StateRegion | AccessTraits |  | Unknown | 类别：const |
| StateRegion | Colonize |  | Command |  |
| StateRegion | GetAdjacentLandStateRegionsDesc |  | CString | 类别：nonconst |
| StateRegion | GetAdjacentSeaStateRegionsDesc |  | CString | 类别：nonconst |
| StateRegion | GetCityHubName |  | CString | 类别：nonconst |
| StateRegion | GetColonizeTooltip |  | CString | 类别：nonconst |
| StateRegion | GetCustom | CustomLocalization | CString | 类别：nonconst |
| StateRegion | GetFarmHubName |  | CString | 类别：nonconst |
| StateRegion | GetForestryHubName |  | CString | 类别：nonconst |
| StateRegion | GetID |  | int32 | 类别：nonconst |
| StateRegion | GetLargestStateInRegion |  | State | 类别：nonconst |
| StateRegion | GetLargestStateOwner |  | Country | 类别：nonconst |
| StateRegion | GetMineHubName |  | CString | 类别：nonconst |
| StateRegion | GetName |  | CString | 类别：nonconst |
| StateRegion | GetNameNoFormatting |  | CString | 类别：nonconst |
| StateRegion | GetNavalExitStateRegionDesc |  | CString | 类别：nonconst |
| StateRegion | GetPollutionEffects |  | CString | 类别：nonconst |
| StateRegion | GetPollutionImpact |  | CFixedPoint | 类别：nonconst |
| StateRegion | GetPollutionImpactDailyChange |  | CFixedPoint | 类别：nonconst |
| StateRegion | GetPollutionImpactTargetLevel |  | CFixedPoint | 类别：nonconst |
| StateRegion | GetPollutionLevel |  | CFixedPoint | 类别：nonconst |
| StateRegion | GetPortHubName |  | CString | 类别：nonconst |
| StateRegion | GetSeaInfrastructure | Country | CFixedPoint | 类别：nonconst |
| StateRegion | GetSeaInfrastructureDesc | Country | CString | 类别：nonconst |
| StateRegion | GetStatesDesc |  | CString | 类别：nonconst |
| StateRegion | GetStrategicRegion |  | StrategicRegion | 类别：nonconst |
| StateRegion | GetTooltipTag |  | CString | 类别：nonconst |
| StateRegion | IsSplitState |  | bool |  |
| StateRegion | IsValid |  | bool |  |
| StateRegion | MakeScope |  | Scope |  |
| StateRegion | PanCamera |  | void |  |
| StateRegion | Self |  | StateRegion |  |
| StateTrait | AccessSelf |  | StateTrait | 类别：const |
| StateTrait | GetCustom | CustomLocalization | CString | 类别：nonconst |
| StateTrait | GetModifiersDesc |  | CString | 类别：nonconst |
| StateTrait | GetName |  | CString | 类别：nonconst |
| StateTrait | GetTexture |  | Unknown | 类别：nonconst |
| StateTrait | GetTooltipTag |  | CString | 类别：nonconst |
| StateTrait | GetUnlocks |  | CString | 类别：nonconst |
| StateTrait | MakeScope |  | Scope |  |
| StateTrait | Self |  | StateTrait |  |
| StatesPanel | AccessBuilding | BuildingType | Building | 类别：const |
| StatesPanel | AccessLocalGoods |  | Unknown | 类别：const |
| StatesPanel | AccessNonLocalGoods |  | Unknown | 类别：const |
| StatesPanel | AccessSelf |  | StatesPanel | 类别：const |
| StatesPanel | AccessState |  | State | 类别：const |
| StatesPanel | AccessSubsistenceBuilding |  | Building | 类别：const |
| StatesPanel | CalcBuildUrbanBuildingsButtonPosition |  | CVector2f |  |
| StatesPanel | GetNumAgricultureLevels |  | int32 | 类别：nonconst |
| StatesPanel | GetNumAgricultureLevelsDesc |  | CString | 类别：nonconst |
| StatesPanel | GetNumAgricultureLevelsInQueue |  | int32 | 类别：nonconst |
| StatesPanel | GetNumDevelopmentLevels |  | int32 | 类别：nonconst |
| StatesPanel | GetNumDevelopmentLevelsDesc |  | CString | 类别：nonconst |
| StatesPanel | GetNumDevelopmentLevelsInQueue |  | int32 | 类别：nonconst |
| StatesPanel | GetNumResourceLevels |  | int32 | 类别：nonconst |
| StatesPanel | GetNumResourceLevelsDesc |  | CString | 类别：nonconst |
| StatesPanel | GetNumResourceLevelsInQueue |  | int32 | 类别：nonconst |
| StatesPanel | GetNumUrbanLevels |  | int32 | 类别：nonconst |
| StatesPanel | GetNumUrbanLevelsDesc |  | CString | 类别：nonconst |
| StatesPanel | GetNumUrbanLevelsInQueue |  | int32 | 类别：nonconst |
| StatesPanel | GetState |  | State | 类别：nonconst |
| StatesPanel | IsBuildUrbanBuildingsMenuOpen |  | bool |  |
| StatesPanel | IsExpanded | Unknown | bool |  |
| StatesPanel | Self |  | StatesPanel |  |
| StatesPanel | Sort | Unknown | void |  |
| StatesPanel | ToggleBuildUrbanBuildingsMenu | PdxGuiWidget | void |  |
| StatesPanel | ToggleSection | Unknown | void |  |
| StatusWidget | AccessSelf |  | StatusWidget | 类别：const |
| StatusWidget | ConnectAccount |  | void |  |
| StatusWidget | DisconnectAccount |  | void |  |
| StatusWidget | Hide |  | void |  |
| StatusWidget | IsAccountConnected |  | bool |  |
| StatusWidget | IsBusy |  | bool |  |
| StatusWidget | Logout |  | void |  |
| StatusWidget | Self |  | StatusWidget |  |
| StatusWidget | Show |  | void |  |
| StatusWidget | SupportsConnectAccount |  | bool |  |
| StatusWidget | ToggleCreateAccountWindow |  | void |  |
| StatusWidget | ToggleCreateProfileWindow |  | void |  |
| StatusWidget | ToggleLoginWindow |  | void |  |
| StrategicRegion | AccessFirstDiplomaticPlay |  | DiplomaticPlay | 类别：const |
| StrategicRegion | AccessSelf |  | StrategicRegion | 类别：const |
| StrategicRegion | GetConvoyRaidsDesc |  | CString | 类别：nonconst |
| StrategicRegion | GetCustom | CustomLocalization | CString | 类别：nonconst |
| StrategicRegion | GetFirstDiplomaticPlay |  | DiplomaticPlay | 类别：nonconst |
| StrategicRegion | GetIndex |  | uint32 | 类别：nonconst |
| StrategicRegion | GetInterest | Unknown | Interest | 类别：nonconst |
| StrategicRegion | GetInterests |  | Unknown | 类别：nonconst |
| StrategicRegion | GetLastConvoyRaidingCountriesToTargetDesc | Country | CString | 类别：nonconst |
| StrategicRegion | GetLastConvoyRaidingDamageBy | Country | int32 | 类别：nonconst |
| StrategicRegion | GetLastConvoyRaidingDamageEnemyReductionDesc | Country | CString | 类别：nonconst |
| StrategicRegion | GetLastConvoyRaidingDamageReductionDesc | Country | CString | 类别：nonconst |
| StrategicRegion | GetLastConvoyRaidingDamageTo | Country | int32 | 类别：nonconst |
| StrategicRegion | GetLastConvoyRaidingTargetCountriesByAttackerDesc | Country | CString | 类别：nonconst |
| StrategicRegion | GetName |  | CString | 类别：nonconst |
| StrategicRegion | GetNameNoFormatting |  | CString | 类别：nonconst |
| StrategicRegion | GetTooltipTag |  | CString | 类别：nonconst |
| StrategicRegion | GetTotalGDP |  | CFixedPoint | 类别：nonconst |
| StrategicRegion | HasDiplomaticPlay |  | bool |  |
| StrategicRegion | IsLand |  | bool |  |
| StrategicRegion | IsValid |  | bool |  |
| StrategicRegion | MakeScope |  | Scope |  |
| StrategicRegion | Self |  | StrategicRegion |  |
| StrategicRegionMarker | AccessSelf |  | StrategicRegionMarker | 类别：const |
| StrategicRegionMarker | AccessStrategicRegion |  | StrategicRegion | 类别：const |
| StrategicRegionMarker | GetPosition |  | CVector2f | 类别：nonconst |
| StrategicRegionMarker | GetStrategicRegion |  | StrategicRegion | 类别：nonconst |
| StrategicRegionMarker | Self |  | StrategicRegionMarker |  |
| SubjectType | AcceptsAnyOverlor |  | bool |  |
| SubjectType | AcceptsOnlyRecognizedOverlor |  | bool |  |
| SubjectType | AccessSelf |  | SubjectType | 类别：const |
| SubjectType | CanStartOwnDiplomaticPlays |  | bool |  |
| SubjectType | GetDesc |  | CString | 类别：nonconst |
| SubjectType | GetDiplomaticActionType |  | DiplomaticActionType | 类别：nonconst |
| SubjectType | GetHigherAutonomySubjectType | Unknown | SubjectType | 类别：nonconst |
| SubjectType | GetIncomeTransfer |  | CFixedPoint | 类别：nonconst |
| SubjectType | GetKey |  | CString | 类别：nonconst |
| SubjectType | GetLowerAutonomySubjectType | Unknown | SubjectType | 类别：nonconst |
| SubjectType | GetName |  | CString | 类别：nonconst |
| SubjectType | GetNameNoFormatting |  | CString | 类别：nonconst |
| SubjectType | GetNameNoIcon |  | CString | 类别：nonconst |
| SubjectType | GetNameNoIconNoFormatting |  | CString | 类别：nonconst |
| SubjectType | GetTextIcon |  | CString | 类别：nonconst |
| SubjectType | GetTexture |  | Unknown | 类别：nonconst |
| SubjectType | GetTooltipTag |  | CString | 类别：nonconst |
| SubjectType | HasCategory | Unknown | bool |  |
| SubjectType | IsValid |  | bool |  |
| SubjectType | JoinOverlordWars |  | bool |  |
| SubjectType | Self |  | SubjectType |  |
| SubjectType | ShouldAnnexOnCountryFormation |  | bool |  |
| SupplyNetworkEntry | AccessSelf |  | SupplyNetworkEntry | 类别：const |
| SupplyNetworkEntry | GetTooltip |  | CString | 类别：nonconst |
| SupplyNetworkEntry | GetValue |  | CFixedPoint | 类别：nonconst |
| SupplyNetworkEntry | RouteGetName |  | CString |  |
| SupplyNetworkEntry | Self |  | SupplyNetworkEntry |  |
| Sway | AcceptSway |  | Command |  |
| Sway | AccessSelf |  | Sway | 类别：const |
| Sway | GetCustom | CustomLocalization | CString | 类别：nonconst |
| Sway | GetProposalDesc |  | CString | 类别：nonconst |
| Sway | GetSwayOffer |  | SwayOffer | 类别：nonconst |
| Sway | GetTooltipTag |  | CString | 类别：nonconst |
| Sway | IsCallingInObligation |  | bool |  |
| Sway | IsReverseSway |  | bool |  |
| Sway | IsValid |  | bool |  |
| Sway | MakeScope |  | Scope |  |
| Sway | RejectSway |  | Command |  |
| Sway | Self |  | Sway |  |
| Sway | WouldRepudiateObligationIfRejected |  | bool |  |
| SwayCountryPanel | AccessCountry |  | Country | 类别：const |
| SwayCountryPanel | AccessDiplomaticPlay |  | DiplomaticPlay | 类别：const |
| SwayCountryPanel | AccessOtherCountry |  | Country | 类别：const |
| SwayCountryPanel | AccessSelf |  | SwayCountryPanel | 类别：const |
| SwayCountryPanel | AccessShownSwayOffers |  | Unknown | 类别：const |
| SwayCountryPanel | AccessSwayOfferTypes |  | Unknown | 类别：const |
| SwayCountryPanel | AccessSwayOfferWarGoalTypes |  | Unknown | 类别：const |
| SwayCountryPanel | DecreaseFilterLevel |  | void |  |
| SwayCountryPanel | GetCountry |  | Country | 类别：nonconst |
| SwayCountryPanel | GetDiplomaticPlay |  | DiplomaticPlay | 类别：nonconst |
| SwayCountryPanel | GetOtherCountry |  | Country | 类别：nonconst |
| SwayCountryPanel | IsReverseSway |  | bool |  |
| SwayCountryPanel | IsShowingSwayOfferTypes |  | bool |  |
| SwayCountryPanel | IsShowingSwayOfferWarGoalTypes |  | bool |  |
| SwayCountryPanel | IsShowingSwayOffers |  | bool |  |
| SwayCountryPanel | Self |  | SwayCountryPanel |  |
| SwayCountryPanel | SetSwayOfferType | SwayOfferType | void |  |
| SwayCountryPanel | SetSwayOfferWarGoalType | WarGoalType | void |  |
| SwayOffer | AccessSelf |  | SwayOffer | 类别：const |
| SwayOffer | CalcManeuversCost | Country Country DiplomaticPlay | int32 |  |
| SwayOffer | GetAcceptSwayScore | Unknown Unknown Unknown | int32 | 类别：nonconst |
| SwayOffer | GetAcceptSwayScoreWithArticle | DiplomaticPlay Country Country ArticleDraft | int32 | 类别：nonconst |
| SwayOffer | GetCountryForFlag | Country | Country | 类别：nonconst |
| SwayOffer | GetDiplomaticActionType |  | DiplomaticActionType | 类别：nonconst |
| SwayOffer | GetManeuversCostDesc | Country Country DiplomaticPlay | CString | 类别：nonconst |
| SwayOffer | GetName | Country Country DiplomaticPlay | CString | 类别：nonconst |
| SwayOffer | GetOfferedWarGoal |  | WarGoal | 类别：nonconst |
| SwayOffer | GetState |  | State | 类别：nonconst |
| SwayOffer | GetSwayOfferType |  | SwayOfferType | 类别：nonconst |
| SwayOffer | GetTexture |  | Unknown | 类别：nonconst |
| SwayOffer | GetThirdPartyCountry |  | Country | 类别：nonconst |
| SwayOffer | GetTooltipTag |  | CString | 类别：nonconst |
| SwayOffer | GetWouldAcceptSwayDesc | DiplomaticPlay Country Country | CString | 类别：nonconst |
| SwayOffer | GetWouldAcceptSwayDescWithArticle | DiplomaticPlay Country Country ArticleDraft | CString | 类别：nonconst |
| SwayOffer | RequiresAnyInput |  | bool |  |
| SwayOffer | Self |  | SwayOffer |  |
| SwayOffer | SetArticleInputsFromDraft | ArticleDraft | void |  |
| SwayOffer | TakesEffectImmediately |  | bool |  |
| SwayOffer | WouldAcceptSway | DiplomaticPlay Country Country | bool |  |
| SwayOffer | WouldAcceptSwayWithArticle | DiplomaticPlay Country Country ArticleDraft | bool |  |
| SwayOfferType | AccessSelf |  | SwayOfferType | 类别：const |
| SwayOfferType | GetName |  | CString | 类别：nonconst |
| SwayOfferType | GetTexture |  | Unknown | 类别：nonconst |
| SwayOfferType | GetTooltipTag |  | CString | 类别：nonconst |
| SwayOfferType | Self |  | SwayOfferType |  |
| TaxBurdenItem | AccessSelf |  | TaxBurdenItem | 类别：const |
| TaxBurdenItem | GetTaxType |  | CString | 类别：nonconst |
| TaxBurdenItem | GetValue |  | CFixedPoint | 类别：nonconst |
| TaxBurdenItem | Self |  | TaxBurdenItem |  |
| TechTreeItem | AccessSelf |  | TechTreeItem | 类别：const |
| TechTreeItem | GetKey |  | CString | 类别：nonconst |
| TechTreeItem | GetPosition |  | CVector2f | 类别：nonconst |
| TechTreeItem | GetTechnology |  | Technology | 类别：nonconst |
| TechTreeItem | Self |  | TechTreeItem |  |
| TechTreeLine | AccessSelf |  | TechTreeLine | 类别：const |
| TechTreeLine | GetFrom |  | CVector2f | 类别：nonconst |
| TechTreeLine | GetLineFrom |  | CVector2f | 类别：nonconst |
| TechTreeLine | GetLineTo |  | CVector2f | 类别：nonconst |
| TechTreeLine | GetPoints |  | Unknown | 类别：nonconst |
| TechTreeLine | GetPointsInContainer |  | Unknown | 类别：nonconst |
| TechTreeLine | GetPosition |  | CVector2f | 类别：nonconst |
| TechTreeLine | GetSize |  | CVector2f | 类别：nonconst |
| TechTreeLine | GetSourceTech |  | Technology | 类别：nonconst |
| TechTreeLine | GetTargetTech |  | Technology | 类别：nonconst |
| TechTreeLine | GetTo |  | CVector2f | 类别：nonconst |
| TechTreeLine | IsFromNodeVirtual |  | bool |  |
| TechTreeLine | IsToNodeVirtual |  | bool |  |
| TechTreeLine | Self |  | TechTreeLine |  |
| TechTreePanel | AccessSelf |  | TechTreePanel | 类别：const |
| TechTreePanel | GetMilitaryTechTreeItems |  | Unknown | 类别：nonconst |
| TechTreePanel | GetMilitaryTechTreeLines |  | Unknown | 类别：nonconst |
| TechTreePanel | GetProductionTechTreeItems |  | Unknown | 类别：nonconst |
| TechTreePanel | GetProductionTechTreeLines |  | Unknown | 类别：nonconst |
| TechTreePanel | GetSocietyTechTreeItems |  | Unknown | 类别：nonconst |
| TechTreePanel | GetSocietyTechTreeLines |  | Unknown | 类别：nonconst |
| TechTreePanel | ResetMilitaryView |  | void |  |
| TechTreePanel | ResetProductionView |  | void |  |
| TechTreePanel | ResetSocietyView |  | void |  |
| TechTreePanel | Self |  | TechTreePanel |  |
| Technology | AccessSelf |  | Technology | 类别：const |
| Technology | AddToQueue | Country | Command |  |
| Technology | AddToQueueWithUnlocks | Country | Command |  |
| Technology | GetCategoryKey |  | CString | 类别：nonconst |
| Technology | GetCategoryName |  | CString | 类别：nonconst |
| Technology | GetCost | Country | CFixedPoint | 类别：nonconst |
| Technology | GetCostDesc | Country | CString | 类别：nonconst |
| Technology | GetCustom | CustomLocalization | CString | 类别：nonconst |
| Technology | GetDesc |  | CString | 类别：nonconst |
| Technology | GetEra |  | Era | 类别：nonconst |
| Technology | GetModifiersAsString |  | CString | 类别：nonconst |
| Technology | GetName |  | CString | 类别：nonconst |
| Technology | GetNameNoFormatting |  | CString | 类别：nonconst |
| Technology | GetProgress | Country | CFixedPoint | 类别：nonconst |
| Technology | GetProgressPercentage | Country | float | 类别：nonconst |
| Technology | GetResearchQueuePosition | Country | int32 | 类别：nonconst |
| Technology | GetTexture |  | Unknown | 类别：nonconst |
| Technology | GetTimeLeftDesc | Country | CString | 类别：nonconst |
| Technology | GetTooltip | Country | CString | 类别：nonconst |
| Technology | GetTooltipTag |  | CString | 类别：nonconst |
| Technology | GetTooltipWithoutRequirements | Country | CString | 类别：nonconst |
| Technology | GetUnlocks | Country | Unknown | 类别：nonconst |
| Technology | HasResearchedTech | Country | bool |  |
| Technology | IsBeingHighlighted |  | bool |  |
| Technology | IsBeingTutorialHighlighted |  | bool |  |
| Technology | IsInResearchQueue | Country | bool |  |
| Technology | IsResearchable |  | bool |  |
| Technology | IsResearching | Country | bool |  |
| Technology | IsValid |  | bool |  |
| Technology | MakeScope |  | Scope |  |
| Technology | PredictTimeLeftDesc | Country | CString |  |
| Technology | PredictTimeLeftInQueueDesc | Country | CString |  |
| Technology | RemoveFromQueue | Country | Command |  |
| Technology | Research | Country | Command |  |
| Technology | ResearchWithUnlocks | Country | Command |  |
| Technology | Self |  | Technology |  |
| Technology | ShouldShow | Country | bool |  |
| TechnologyUnlock | AccessSelf |  | TechnologyUnlock | 类别：const |
| TechnologyUnlock | GetTexture |  | Unknown | 类别：nonconst |
| TechnologyUnlock | GetTooltip |  | CString | 类别：nonconst |
| TechnologyUnlock | HasFrame |  | bool |  |
| TechnologyUnlock | IsGroup |  | bool |  |
| TechnologyUnlock | Self |  | TechnologyUnlock |  |
| TerrainToolButton | AccessSelf |  | TerrainToolButton | 类别：const |
| TerrainToolButton | IsSelected |  | bool |  |
| TerrainToolButton | Self |  | TerrainToolButton |  |
| TextureEntry | AccessSelf |  | TextureEntry | 类别：const |
| TextureEntry | GetName |  | CString | 类别：nonconst |
| TextureEntry | GetResolution |  | CString | 类别：nonconst |
| TextureEntry | GetTexture |  | Unknown | 类别：nonconst |
| TextureEntry | IsAvailable |  | bool |  |
| TextureEntry | OpenTextureViewer |  | void |  |
| TextureEntry | Self |  | TextureEntry |  |
| TextureImporter | AccessOutputEntries |  | Unknown | 类别：const |
| TextureImporter | AccessSelf |  | TextureImporter | 类别：const |
| TextureImporter | AddCustomResolution |  | void |  |
| TextureImporter | Cancel |  | void |  |
| TextureImporter | GetLastConversion |  | CString | 类别：nonconst |
| TextureImporter | GetTextures |  | Unknown | 类别：nonconst |
| TextureImporter | HasLastConversion |  | bool |  |
| TextureImporter | Import |  | void |  |
| TextureImporter | IsCustomResolution |  | bool |  |
| TextureImporter | IsImporting |  | bool |  |
| TextureImporter | Refresh |  | void |  |
| TextureImporter | RemoveCustomResolution |  | void |  |
| TextureImporter | Self |  | TextureImporter |  |
| TextureImporter | SetOutputScale | CString | void |  |
| TextureImporter | SetResolution | Unknown | void |  |
| TextureList | AccessSelf |  | TextureList | 类别：const |
| TextureList | GetAutoUpdate |  | bool | 类别：nonconst |
| TextureList | GetCurrentDirectory |  | CString | 类别：nonconst |
| TextureList | GetDirectories |  | Unknown | 类别：nonconst |
| TextureList | GetFilterString |  | CUTF8String | 类别：nonconst |
| TextureList | GetTextures |  | Unknown | 类别：nonconst |
| TextureList | GetTotalSize |  | uint64 | 类别：nonconst |
| TextureList | GetTotalTextureCount |  | int32 | 类别：nonconst |
| TextureList | GoToParentDirectory |  | void |  |
| TextureList | IsFlatView |  | bool |  |
| TextureList | Self |  | TextureList |  |
| TextureList | SetAutoUpdate | bool | void |  |
| TextureList | SetFilterString |  | void |  |
| TextureList | SetFlatView | bool | void |  |
| TextureList | SortByFormat |  | void |  |
| TextureList | SortByMipMaps |  | void |  |
| TextureList | SortByName |  | void |  |
| TextureList | SortByRefCount |  | void |  |
| TextureList | SortByResolution |  | void |  |
| TextureList | SortBySize |  | void |  |
| TextureList | UpdateTextureList |  | void |  |
| TextureListDirectory | AccessSelf |  | TextureListDirectory | 类别：const |
| TextureListDirectory | GetMipMaps |  | int32 | 类别：nonconst |
| TextureListDirectory | GetName |  | Unknown | 类别：nonconst |
| TextureListDirectory | GetRefcount |  | int32 | 类别：nonconst |
| TextureListDirectory | GetSize |  | uint64 | 类别：nonconst |
| TextureListDirectory | GetSubDirectoryCount |  | int32 | 类别：nonconst |
| TextureListDirectory | GetTextureCount |  | int32 | 类别：nonconst |
| TextureListDirectory | Self |  | TextureListDirectory |  |
| TextureListTexture | AccessSelf |  | TextureListTexture | 类别：const |
| TextureListTexture | GetFormat |  | CString | 类别：nonconst |
| TextureListTexture | GetMipMaps |  | int32 | 类别：nonconst |
| TextureListTexture | GetName |  | Unknown | 类别：nonconst |
| TextureListTexture | GetRefcount |  | int32 | 类别：nonconst |
| TextureListTexture | GetResolution |  | CString | 类别：nonconst |
| TextureListTexture | GetSize |  | uint64 | 类别：nonconst |
| TextureListTexture | Self |  | TextureListTexture |  |
| TextureNodeWindow | AccessSelf |  | TextureNodeWindow | 类别：const |
| TextureNodeWindow | FileSelect |  | void |  |
| TextureNodeWindow | Filename |  | CString |  |
| TextureNodeWindow | Self |  | TextureNodeWindow |  |
| TextureNodeWindow | Texture |  | Unknown |  |
| TextureViewer | AccessSelf |  | TextureViewer | 类别：const |
| TextureViewer | Fit |  | void |  |
| TextureViewer | GetAlpha |  | bool | 类别：nonconst |
| TextureViewer | GetAutoFit |  | bool | 类别：nonconst |
| TextureViewer | GetBlue |  | bool | 类别：nonconst |
| TextureViewer | GetConstantBuffers |  | Unknown | 类别：nonconst |
| TextureViewer | GetEffect |  | Unknown | 类别：nonconst |
| TextureViewer | GetFlipV |  | bool | 类别：nonconst |
| TextureViewer | GetGreen |  | bool | 类别：nonconst |
| TextureViewer | GetPointSampling |  | bool | 类别：nonconst |
| TextureViewer | GetRed |  | bool | 类别：nonconst |
| TextureViewer | GetTexture |  | Unknown | 类别：nonconst |
| TextureViewer | GetTextureSize |  | CVector2f | 类别：nonconst |
| TextureViewer | GetTextureString |  | CString | 类别：nonconst |
| TextureViewer | GetTextureZoom |  | CString | 类别：nonconst |
| TextureViewer | GetToGamma |  | bool | 类别：nonconst |
| TextureViewer | OriginalSize |  | void |  |
| TextureViewer | Self |  | TextureViewer |  |
| TextureViewer | SetAlpha | bool | void |  |
| TextureViewer | SetAutoFit | bool | void |  |
| TextureViewer | SetBlue | bool | void |  |
| TextureViewer | SetFlipV | bool | void |  |
| TextureViewer | SetGreen | bool | void |  |
| TextureViewer | SetPointSampling | bool | void |  |
| TextureViewer | SetRed | bool | void |  |
| TextureViewer | SetToGamma | bool | void |  |
| TextureViewer | ShowFileList |  | void |  |
| Theater | AccessSelf |  | Theater | 类别：const |
| Theater | GetCustom | CustomLocalization | CString | 类别：nonconst |
| Theater | GetID |  | uint32 | 类别：nonconst |
| Theater | GetName |  | CString | 类别：nonconst |
| Theater | GetNumMobilizedUnitsInTheater |  | int32 | 类别：nonconst |
| Theater | GetNumProvinces |  | int32 | 类别：nonconst |
| Theater | GetOwner |  | Country | 类别：nonconst |
| Theater | GetTooltipTag |  | CString | 类别：nonconst |
| Theater | MakeScope |  | Scope |  |
| Theater | Self |  | Theater |  |
| Theme | AccessSelf |  | Theme | 类别：const |
| Theme | CanBeSelected |  | bool |  |
| Theme | GetCanBeSelectedDesc |  | CString | 类别：nonconst |
| Theme | GetCategory |  | ThemeCategory | 类别：nonconst |
| Theme | GetDesc |  | CString | 类别：nonconst |
| Theme | GetName |  | CString | 类别：nonconst |
| Theme | GetRequiredDlc |  | Dlc | 类别：nonconst |
| Theme | GetTooltipTag |  | CString | 类别：nonconst |
| Theme | HasDlcRequirement |  | bool |  |
| Theme | IsNew |  | bool |  |
| Theme | IsSelected |  | bool |  |
| Theme | IsUseDynamicTheme |  | bool |  |
| Theme | MarkAsSeen |  | void |  |
| Theme | SelectSingleChoiceTheme |  | void |  |
| Theme | Self |  | Theme |  |
| Theme | ToggleMultipleChoiceTheme |  | void |  |
| ThemeBulkSelectionGroup | AccessSelf |  | ThemeBulkSelectionGroup | 类别：const |
| ThemeBulkSelectionGroup | CanBeSelected |  | bool |  |
| ThemeBulkSelectionGroup | GetDesc |  | CString | 类别：nonconst |
| ThemeBulkSelectionGroup | GetName |  | CString | 类别：nonconst |
| ThemeBulkSelectionGroup | GetRequiredDlc |  | Dlc | 类别：nonconst |
| ThemeBulkSelectionGroup | GetThemeListDesc |  | CString | 类别：nonconst |
| ThemeBulkSelectionGroup | HasAvailableNewThemes |  | bool |  |
| ThemeBulkSelectionGroup | HasDlcRequirement |  | bool |  |
| ThemeBulkSelectionGroup | IsCustom |  | bool |  |
| ThemeBulkSelectionGroup | IsDynamic |  | bool |  |
| ThemeBulkSelectionGroup | IsSelected |  | bool |  |
| ThemeBulkSelectionGroup | IsSpecialGroupType |  | bool |  |
| ThemeBulkSelectionGroup | MarkThemesAsSeen |  | void |  |
| ThemeBulkSelectionGroup | Self |  | ThemeBulkSelectionGroup |  |
| ThemeCategory | AccessSelf |  | ThemeCategory | 类别：const |
| ThemeCategory | GetDesc |  | CString | 类别：nonconst |
| ThemeCategory | GetName |  | CString | 类别：nonconst |
| ThemeCategory | GetSelectedSingleChoiceTheme |  | Theme | 类别：nonconst |
| ThemeCategory | GetThemes |  | Unknown | 类别：nonconst |
| ThemeCategory | HasAnyAvailableNewThemes |  | bool |  |
| ThemeCategory | OnSelectSingleChoiceTheme |  | void |  |
| ThemeCategory | Self |  | ThemeCategory |  |
| ThemeWindow | AccessSelf |  | ThemeWindow | 类别：const |
| ThemeWindow | GetBulkSelectionGroups |  | Unknown | 类别：nonconst |
| ThemeWindow | GetFormattedValue | CString | CString | 类别：nonconst |
| ThemeWindow | GetMultipleChoiceThemeCategories |  | Unknown | 类别：nonconst |
| ThemeWindow | GetScrollbarMax | CString | float | 类别：nonconst |
| ThemeWindow | GetScrollbarMin | CString | float | 类别：nonconst |
| ThemeWindow | GetScrollbarStep | CString | float | 类别：nonconst |
| ThemeWindow | GetScrollbarValue | CString | float | 类别：nonconst |
| ThemeWindow | GetSelectedBulkSelectionGroup |  | ThemeBulkSelectionGroup | 类别：nonconst |
| ThemeWindow | GetSingleChoiceThemeCategories |  | Unknown | 类别：nonconst |
| ThemeWindow | HasAnyAvailableNewBulkGroups |  | bool |  |
| ThemeWindow | Hide |  | void |  |
| ThemeWindow | IsDawnOfWonderEnabled |  | bool |  |
| ThemeWindow | OnBulkGroupSelected |  | void |  |
| ThemeWindow | Save |  | void |  |
| ThemeWindow | SaveAndHide |  | void |  |
| ThemeWindow | ScrollbarOnValueChanged | CString | void |  |
| ThemeWindow | Self |  | ThemeWindow |  |
| ThemeWindow | Show |  | void |  |
| ThemeWindow | ToggleDayNightEnableManualTime |  | void |  |
| ThemeWindow | ToggleDayNightEnableSyncLocalTime |  | void |  |
| ThemeWindow | ToggleDayNightEnabled |  | void |  |
| TickTaskData | AccessSelf |  | TickTaskData | 类别：const |
| TickTaskData | GetAverageTime |  | int32 | 类别：nonconst |
| TickTaskData | GetExecutionPriority |  | CString | 类别：nonconst |
| TickTaskData | GetExecutionPriorityFrame |  | int32 | 类别：nonconst |
| TickTaskData | GetExecutionRate |  | CString | 类别：nonconst |
| TickTaskData | GetExecutionRateFrame |  | int32 | 类别：nonconst |
| TickTaskData | GetHighestLockTime |  | int32 | 类别：nonconst |
| TickTaskData | GetIndex |  | int32 | 类别：nonconst |
| TickTaskData | GetName |  | CString | 类别：nonconst |
| TickTaskData | GetTimesExecuted |  | int32 | 类别：nonconst |
| TickTaskData | IsPersisted |  | bool |  |
| TickTaskData | OpenDetails |  | void |  |
| TickTaskData | Self |  | TickTaskData |  |
| TickTaskDebuggerView | AccessSelf |  | TickTaskDebuggerView | 类别：const |
| TickTaskDebuggerView | GetGraphItems |  | Unknown | 类别：nonconst |
| TickTaskDebuggerView | GetGraphLines |  | Unknown | 类别：nonconst |
| TickTaskDebuggerView | Self |  | TickTaskDebuggerView |  |
| TickTaskDetailsView | AccessSelf |  | TickTaskDetailsView | 类别：const |
| TickTaskDetailsView | GetTickTask |  | TickTaskData | 类别：nonconst |
| TickTaskDetailsView | Self |  | TickTaskDetailsView |  |
| TickTaskGraphItem | AccessSelf |  | TickTaskGraphItem | 类别：const |
| TickTaskGraphItem | GetKey |  | CString | 类别：nonconst |
| TickTaskGraphItem | GetPosition |  | CVector2f | 类别：nonconst |
| TickTaskGraphItem | GetTickTask |  | TickTaskData | 类别：nonconst |
| TickTaskGraphItem | GetTooltip |  | CString | 类别：nonconst |
| TickTaskGraphItem | Self |  | TickTaskGraphItem |  |
| TickTaskGraphLine | AccessSelf |  | TickTaskGraphLine | 类别：const |
| TickTaskGraphLine | GetFrom |  | CVector2f | 类别：nonconst |
| TickTaskGraphLine | GetLineFrom |  | CVector2f | 类别：nonconst |
| TickTaskGraphLine | GetLineTo |  | CVector2f | 类别：nonconst |
| TickTaskGraphLine | GetPoints |  | Unknown | 类别：nonconst |
| TickTaskGraphLine | GetPointsInContainer |  | Unknown | 类别：nonconst |
| TickTaskGraphLine | GetPosition |  | CVector2f | 类别：nonconst |
| TickTaskGraphLine | GetSize |  | CVector2f | 类别：nonconst |
| TickTaskGraphLine | GetTo |  | CVector2f | 类别：nonconst |
| TickTaskGraphLine | IsFromNodeVirtual |  | bool |  |
| TickTaskGraphLine | IsToNodeVirtual |  | bool |  |
| TickTaskGraphLine | Self |  | TickTaskGraphLine |  |
| TickTaskListView | AccessSelf |  | TickTaskListView | 类别：const |
| TickTaskListView | GetTickTasks |  | Unknown | 类别：nonconst |
| TickTaskListView | Self |  | TickTaskListView |  |
| TickTaskListView | Sort | CString | void |  |
| TimeKeeper | AccessSelf |  | TimeKeeper | 类别：const |
| TimeKeeper | CanAnyoneUnpause |  | bool |  |
| TimeKeeper | CanDecreaseGameSpeed |  | bool |  |
| TimeKeeper | CanIncreaseGameSpeed |  | bool |  |
| TimeKeeper | CanSetGameSpeed |  | bool |  |
| TimeKeeper | CanTogglePause |  | bool |  |
| TimeKeeper | DecreaseGameSpeed |  | void |  |
| TimeKeeper | GetCurrentDateWithDiff | Unknown | CString | 类别：nonconst |
| TimeKeeper | GetDayOfWeek |  | CString | 类别：nonconst |
| TimeKeeper | GetDecreaseSpeedTooltip |  | CString | 类别：nonconst |
| TimeKeeper | GetGameSpeed |  | int32 | 类别：nonconst |
| TimeKeeper | GetGameSpeedFrame |  | int32 | 类别：nonconst |
| TimeKeeper | GetIncreaseSpeedTooltip |  | CString | 类别：nonconst |
| TimeKeeper | GetPausedBy |  | CString | 类别：nonconst |
| TimeKeeper | GetPausedText |  | CString | 类别：nonconst |
| TimeKeeper | GetProgressOfWeek |  | int32 | 类别：nonconst |
| TimeKeeper | GetTickOfDay |  | int32 | 类别：nonconst |
| TimeKeeper | GetTimeAnyoneUnpause |  | int32 | 类别：nonconst |
| TimeKeeper | GetTimeOfDay |  | CString | 类别：nonconst |
| TimeKeeper | GetTogglePauseTooltip |  | CString | 类别：nonconst |
| TimeKeeper | IncreaseGameSpeed |  | void |  |
| TimeKeeper | IsPaused |  | bool |  |
| TimeKeeper | IsPausedByMe |  | bool |  |
| TimeKeeper | Self |  | TimeKeeper |  |
| TimeKeeper | SetGameSpeed | int32 | void |  |
| TimeKeeper | TogglePause |  | void |  |
| TimedModifier | AccessSelf |  | TimedModifier | 类别：const |
| TimedModifier | GetDesc |  | CString | 类别：nonconst |
| TimedModifier | GetIcon |  | Unknown | 类别：nonconst |
| TimedModifier | GetName |  | CString | 类别：nonconst |
| TimedModifier | GetOneLineDesc |  | CString | 类别：nonconst |
| TimedModifier | GetRemainingDuration |  | CString | 类别：nonconst |
| TimedModifier | GetTooltip |  | CString | 类别：nonconst |
| TimedModifier | GetTooltipTag |  | CString | 类别：nonconst |
| TimedModifier | IsDecaying |  | bool |  |
| TimedModifier | Self |  | TimedModifier |  |
| TimelineKeyframe | AccessSelf |  | TimelineKeyframe | 类别：const |
| TimelineKeyframe | IsHovered |  | bool |  |
| TimelineKeyframe | IsSelected |  | bool |  |
| TimelineKeyframe | KeyframeColor |  | CVector4f |  |
| TimelineKeyframe | Label |  | CString |  |
| TimelineKeyframe | Self |  | TimelineKeyframe |  |
| TimelineKeyframe | SetHovered | Unknown | void |  |
| TimelineKeyframe | SetSelected | Unknown | void |  |
| TimelineKeyframe | TimePoint |  | float |  |
| ToastMessageHandler | AccessSelf |  | ToastMessageHandler | 类别：const |
| ToastMessageHandler | DismissMessage |  | void |  |
| ToastMessageHandler | GetMessageItem |  | PlayerMessageItem | 类别：nonconst |
| ToastMessageHandler | HasMessage |  | bool |  |
| ToastMessageHandler | Self |  | ToastMessageHandler |  |
| ToastMessageHandler | StartDelayingMessage |  | void |  |
| ToastMessageHandler | StopDelayingMessage |  | void |  |
| ToolDialog | AccessSelf |  | ToolDialog | 类别：const |
| ToolDialog | Buttons |  | Unknown |  |
| ToolDialog | Cancel |  | void |  |
| ToolDialog | Close |  | void |  |
| ToolDialog | Confirm |  | void |  |
| ToolDialog | Self |  | ToolDialog |  |
| ToolDialog | Title |  | CString |  |
| ToolDialogButton | AccessSelf |  | ToolDialogButton | 类别：const |
| ToolDialogButton | OnClick |  | bool |  |
| ToolDialogButton | Self |  | ToolDialogButton |  |
| ToolDialogButton | Text |  | CString |  |
| ToolMessageDialog | AccessSelf |  | ToolMessageDialog | 类别：const |
| ToolMessageDialog | IsError |  | bool |  |
| ToolMessageDialog | IsInfo |  | bool |  |
| ToolMessageDialog | IsWarning |  | bool |  |
| ToolMessageDialog | Message |  | CString |  |
| ToolMessageDialog | Self |  | ToolMessageDialog |  |
| ToolProgressDialog | AccessSelf |  | ToolProgressDialog | 类别：const |
| ToolProgressDialog | GetProgress |  | float | 类别：nonconst |
| ToolProgressDialog | Self |  | ToolProgressDialog |  |
| ToolProperty | AccessActions |  | Unknown | 类别：const |
| ToolProperty | AccessSelf |  | ToolProperty | 类别：const |
| ToolProperty | GetActions |  | Unknown | 类别：nonconst |
| ToolProperty | GetColor |  | CVector4f | 类别：nonconst |
| ToolProperty | GetLabel |  | CString | 类别：nonconst |
| ToolProperty | GetTooltip |  | CString | 类别：nonconst |
| ToolProperty | GetTooltipWithLabel |  | CString | 类别：nonconst |
| ToolProperty | HasCheckbox |  | bool |  |
| ToolProperty | HasDefaultValue |  | bool |  |
| ToolProperty | IsActive |  | bool |  |
| ToolProperty | IsSelected |  | bool |  |
| ToolProperty | IsValueDefault |  | bool |  |
| ToolProperty | IsVisible |  | bool |  |
| ToolProperty | Self |  | ToolProperty |  |
| ToolProperty | SetSelected | bool | void |  |
| ToolProperty | SetValueToDefault |  | void |  |
| ToolProperty2SearchList | AccessSelf |  | ToolProperty2SearchList | 类别：const |
| ToolProperty2SearchList | AreSelectButtonsVisible |  | bool |  |
| ToolProperty2SearchList | GetSelectedLabel |  | CUTF8String | 类别：nonconst |
| ToolProperty2SearchList | GetSelectedValueColor |  | CVector4f | 类别：nonconst |
| ToolProperty2SearchList | HasNext |  | bool |  |
| ToolProperty2SearchList | HasPrev |  | bool |  |
| ToolProperty2SearchList | NextEntryTooltip |  | CUTF8String |  |
| ToolProperty2SearchList | OpenSearchList |  | void |  |
| ToolProperty2SearchList | PrevEntryTooltip |  | CUTF8String |  |
| ToolProperty2SearchList | SelectNext |  | void |  |
| ToolProperty2SearchList | SelectPrev |  | void |  |
| ToolProperty2SearchList | Self |  | ToolProperty2SearchList |  |
| ToolPropertyAction | AccessSelf |  | ToolPropertyAction | 类别：const |
| ToolPropertyAction | Execute |  | void |  |
| ToolPropertyAction | GetIcon |  | Unknown | 类别：nonconst |
| ToolPropertyAction | GetTooltip |  | CString | 类别：nonconst |
| ToolPropertyAction | IsAvailable |  | bool |  |
| ToolPropertyAction | IsButton |  | bool |  |
| ToolPropertyAction | IsVisible |  | bool |  |
| ToolPropertyAction | Self |  | ToolPropertyAction |  |
| ToolPropertyBool | AccessSelf |  | ToolPropertyBool | 类别：const |
| ToolPropertyBool | IsEnabled |  | bool |  |
| ToolPropertyBool | Self |  | ToolPropertyBool |  |
| ToolPropertyBool | SetEnabled | bool | void |  |
| ToolPropertyCColor | AccessSelf |  | ToolPropertyCColor | 类别：const |
| ToolPropertyCColor | GetCColor |  | CVector4f | 类别：nonconst |
| ToolPropertyCColor | Self |  | ToolPropertyCColor |  |
| ToolPropertyCColor | SetCColor |  | void |  |
| ToolPropertyCString | AccessSelf |  | ToolPropertyCString | 类别：const |
| ToolPropertyCString | GetString |  | CString | 类别：nonconst |
| ToolPropertyCString | Self |  | ToolPropertyCString |  |
| ToolPropertyCString | SetString |  | void |  |
| ToolPropertyColor | AccessSelf |  | ToolPropertyColor | 类别：const |
| ToolPropertyColor | GetColor |  | CVector4f | 类别：nonconst |
| ToolPropertyColor | Self |  | ToolPropertyColor |  |
| ToolPropertyColor | SetColor |  | void |  |
| ToolPropertyCurve | AccessSelf |  | ToolPropertyCurve | 类别：const |
| ToolPropertyCurve | GetPreviewTexture | int32 int32 int32 int32 | Unknown | 类别：nonconst |
| ToolPropertyCurve | HasCurveEditor |  | bool |  |
| ToolPropertyCurve | OpenCurveEditor |  | void |  |
| ToolPropertyCurve | ResetCurve |  | void |  |
| ToolPropertyCurve | Self |  | ToolPropertyCurve |  |
| ToolPropertyCurve | SetCurve | Unknown | void |  |
| ToolPropertyCurve | ToggleCurveEditor |  | void |  |
| ToolPropertyFloat | AccessSelf |  | ToolPropertyFloat | 类别：const |
| ToolPropertyFloat | GetFloat |  | float | 类别：nonconst |
| ToolPropertyFloat | GetValueColor |  | CVector4f | 类别：nonconst |
| ToolPropertyFloat | Self |  | ToolPropertyFloat |  |
| ToolPropertyFloat | SetFloat |  | void |  |
| ToolPropertyInt | AccessSelf |  | ToolPropertyInt | 类别：const |
| ToolPropertyInt | GetInt |  | int32 | 类别：nonconst |
| ToolPropertyInt | GetValueColor |  | CVector4f | 类别：nonconst |
| ToolPropertyInt | Self |  | ToolPropertyInt |  |
| ToolPropertyInt | SetInt |  | void |  |
| ToolPropertyInt16 | AccessSelf |  | ToolPropertyInt16 | 类别：const |
| ToolPropertyInt16 | GetInt16 |  | int16 | 类别：nonconst |
| ToolPropertyInt16 | GetValueColor |  | CVector4f | 类别：nonconst |
| ToolPropertyInt16 | Self |  | ToolPropertyInt16 |  |
| ToolPropertyInt16 | SetInt16 |  | void |  |
| ToolPropertyInt8 | AccessSelf |  | ToolPropertyInt8 | 类别：const |
| ToolPropertyInt8 | GetInt8 |  | int8 | 类别：nonconst |
| ToolPropertyInt8 | GetValueColor |  | CVector4f | 类别：nonconst |
| ToolPropertyInt8 | Self |  | ToolPropertyInt8 |  |
| ToolPropertyInt8 | SetInt8 |  | void |  |
| ToolPropertyList | AccessSelf |  | ToolPropertyList | 类别：const |
| ToolPropertyList | GetColor |  | CVector4f | 类别：nonconst |
| ToolPropertyList | GetLabel |  | CString | 类别：nonconst |
| ToolPropertyList | IsExpanded |  | bool |  |
| ToolPropertyList | Self |  | ToolPropertyList |  |
| ToolPropertyList | SetExpanded | bool | void |  |
| ToolPropertySearchList | AccessSelf |  | ToolPropertySearchList | 类别：const |
| ToolPropertySearchList | GetSelectedText |  | CUTF8String | 类别：nonconst |
| ToolPropertySearchList | GetSelectedValueColor |  | CVector4f | 类别：nonconst |
| ToolPropertySearchList | OpenSearchList |  | void |  |
| ToolPropertySearchList | Self |  | ToolPropertySearchList |  |
| ToolPropertyString | AccessSelf |  | ToolPropertyString | 类别：const |
| ToolPropertyString | GetString |  | CUTF8String | 类别：nonconst |
| ToolPropertyString | Self |  | ToolPropertyString |  |
| ToolPropertyString | SetString |  | void |  |
| ToolPropertyUint | AccessSelf |  | ToolPropertyUint | 类别：const |
| ToolPropertyUint | GetUint |  | uint32 | 类别：nonconst |
| ToolPropertyUint | GetValueColor |  | CVector4f | 类别：nonconst |
| ToolPropertyUint | Self |  | ToolPropertyUint |  |
| ToolPropertyUint | SetUint |  | void |  |
| ToolPropertyUint16 | AccessSelf |  | ToolPropertyUint16 | 类别：const |
| ToolPropertyUint16 | GetUint16 |  | uint16 | 类别：nonconst |
| ToolPropertyUint16 | GetValueColor |  | CVector4f | 类别：nonconst |
| ToolPropertyUint16 | Self |  | ToolPropertyUint16 |  |
| ToolPropertyUint16 | SetUint16 |  | void |  |
| ToolPropertyUint8 | AccessSelf |  | ToolPropertyUint8 | 类别：const |
| ToolPropertyUint8 | GetUint8 |  | uint8 | 类别：nonconst |
| ToolPropertyUint8 | GetValueColor |  | CVector4f | 类别：nonconst |
| ToolPropertyUint8 | Self |  | ToolPropertyUint8 |  |
| ToolPropertyUint8 | SetUint8 |  | void |  |
| ToolPropertyUndoableSearchList | AccessSelf |  | ToolPropertyUndoableSearchList | 类别：const |
| ToolPropertyUndoableSearchList | AreSelectButtonsVisible |  | bool |  |
| ToolPropertyUndoableSearchList | GetSelectedText |  | CUTF8String | 类别：nonconst |
| ToolPropertyUndoableSearchList | GetSelectedValueColor |  | CVector4f | 类别：nonconst |
| ToolPropertyUndoableSearchList | HasNext |  | bool |  |
| ToolPropertyUndoableSearchList | HasPrev |  | bool |  |
| ToolPropertyUndoableSearchList | NextEntryTooltip |  | CString |  |
| ToolPropertyUndoableSearchList | OpenSearchList |  | void |  |
| ToolPropertyUndoableSearchList | PrevEntryTooltip |  | CString |  |
| ToolPropertyUndoableSearchList | SelectNext |  | void |  |
| ToolPropertyUndoableSearchList | SelectPrev |  | void |  |
| ToolPropertyUndoableSearchList | Self |  | ToolPropertyUndoableSearchList |  |
| ToolPropertyVec1fPercent | AccessSelf |  | ToolPropertyVec1fPercent | 类别：const |
| ToolPropertyVec1fPercent | GetValueColor |  | CVector4f | 类别：nonconst |
| ToolPropertyVec1fPercent | GetX |  | CString | 类别：nonconst |
| ToolPropertyVec1fPercent | Self |  | ToolPropertyVec1fPercent |  |
| ToolPropertyVec1fPercent | SetX |  | void |  |
| ToolPropertyVec2f | AccessSelf |  | ToolPropertyVec2f | 类别：const |
| ToolPropertyVec2f | GetValueColor |  | CVector4f | 类别：nonconst |
| ToolPropertyVec2f | GetX |  | CString | 类别：nonconst |
| ToolPropertyVec2f | GetY |  | CString | 类别：nonconst |
| ToolPropertyVec2f | Self |  | ToolPropertyVec2f |  |
| ToolPropertyVec2f | SetX |  | void |  |
| ToolPropertyVec2f | SetY |  | void |  |
| ToolPropertyVec2fPercent | AccessSelf |  | ToolPropertyVec2fPercent | 类别：const |
| ToolPropertyVec2fPercent | GetValueColor |  | CVector4f | 类别：nonconst |
| ToolPropertyVec2fPercent | GetX |  | CString | 类别：nonconst |
| ToolPropertyVec2fPercent | GetY |  | CString | 类别：nonconst |
| ToolPropertyVec2fPercent | Self |  | ToolPropertyVec2fPercent |  |
| ToolPropertyVec2fPercent | SetX |  | void |  |
| ToolPropertyVec2fPercent | SetY |  | void |  |
| ToolPropertyVec2i | AccessSelf |  | ToolPropertyVec2i | 类别：const |
| ToolPropertyVec2i | GetValueColor |  | CVector4f | 类别：nonconst |
| ToolPropertyVec2i | GetX |  | CString | 类别：nonconst |
| ToolPropertyVec2i | GetY |  | CString | 类别：nonconst |
| ToolPropertyVec2i | Self |  | ToolPropertyVec2i |  |
| ToolPropertyVec2i | SetX |  | void |  |
| ToolPropertyVec2i | SetY |  | void |  |
| ToolPropertyVec3f | AccessSelf |  | ToolPropertyVec3f | 类别：const |
| ToolPropertyVec3f | GetValue |  | CVector3f | 类别：nonconst |
| ToolPropertyVec3f | GetValueColor |  | CVector4f | 类别：nonconst |
| ToolPropertyVec3f | GetX |  | CString | 类别：nonconst |
| ToolPropertyVec3f | GetY |  | CString | 类别：nonconst |
| ToolPropertyVec3f | GetZ |  | CString | 类别：nonconst |
| ToolPropertyVec3f | Self |  | ToolPropertyVec3f |  |
| ToolPropertyVec3f | SetValueFromColor |  | void |  |
| ToolPropertyVec3f | SetX |  | void |  |
| ToolPropertyVec3f | SetY |  | void |  |
| ToolPropertyVec3f | SetZ |  | void |  |
| ToolPropertyVec3i | AccessSelf |  | ToolPropertyVec3i | 类别：const |
| ToolPropertyVec3i | GetValue |  | CVector3i | 类别：nonconst |
| ToolPropertyVec3i | GetValueColor |  | CVector4f | 类别：nonconst |
| ToolPropertyVec3i | GetX |  | CString | 类别：nonconst |
| ToolPropertyVec3i | GetY |  | CString | 类别：nonconst |
| ToolPropertyVec3i | GetZ |  | CString | 类别：nonconst |
| ToolPropertyVec3i | Self |  | ToolPropertyVec3i |  |
| ToolPropertyVec3i | SetValueFromColor |  | void |  |
| ToolPropertyVec3i | SetX |  | void |  |
| ToolPropertyVec3i | SetY |  | void |  |
| ToolPropertyVec3i | SetZ |  | void |  |
| ToolPropertyVec4i | AccessSelf |  | ToolPropertyVec4i | 类别：const |
| ToolPropertyVec4i | GetValue |  | CVector4i | 类别：nonconst |
| ToolPropertyVec4i | GetValueColor |  | CVector4f | 类别：nonconst |
| ToolPropertyVec4i | GetW |  | CString | 类别：nonconst |
| ToolPropertyVec4i | GetX |  | CString | 类别：nonconst |
| ToolPropertyVec4i | GetY |  | CString | 类别：nonconst |
| ToolPropertyVec4i | GetZ |  | CString | 类别：nonconst |
| ToolPropertyVec4i | Self |  | ToolPropertyVec4i |  |
| ToolPropertyVec4i | SetValueFromColor |  | void |  |
| ToolPropertyVec4i | SetW |  | void |  |
| ToolPropertyVec4i | SetX |  | void |  |
| ToolPropertyVec4i | SetY |  | void |  |
| ToolPropertyVec4i | SetZ |  | void |  |
| ToolsPropertyDraggableValueFloat | AccessSelf |  | ToolsPropertyDraggableValueFloat | 类别：const |
| ToolsPropertyDraggableValueFloat | GetValidator |  | Unknown | 类别：nonconst |
| ToolsPropertyDraggableValueFloat | GetValue |  | float | 类别：nonconst |
| ToolsPropertyDraggableValueFloat | OnMouseDragFinished |  | void |  |
| ToolsPropertyDraggableValueFloat | OnMouseDragStarted |  | void |  |
| ToolsPropertyDraggableValueFloat | Self |  | ToolsPropertyDraggableValueFloat |  |
| ToolsPropertyDraggableValueFloat | SetValueFromText |  | void |  |
| ToolsPropertyDraggableValueFloat | UpdateValue |  | void |  |
| ToolsPropertyDraggableValueInt | AccessSelf |  | ToolsPropertyDraggableValueInt | 类别：const |
| ToolsPropertyDraggableValueInt | GetValidator |  | Unknown | 类别：nonconst |
| ToolsPropertyDraggableValueInt | GetValue |  | int32 | 类别：nonconst |
| ToolsPropertyDraggableValueInt | OnMouseDragFinished |  | void |  |
| ToolsPropertyDraggableValueInt | OnMouseDragStarted |  | void |  |
| ToolsPropertyDraggableValueInt | Self |  | ToolsPropertyDraggableValueInt |  |
| ToolsPropertyDraggableValueInt | SetValueFromText |  | void |  |
| ToolsPropertyDraggableValueInt | UpdateValue |  | void |  |
| ToolsPropertyDraggableValueVector2f | AccessSelf |  | ToolsPropertyDraggableValueVector2f | 类别：const |
| ToolsPropertyDraggableValueVector2f | GetValidatorX |  | Unknown | 类别：nonconst |
| ToolsPropertyDraggableValueVector2f | GetValidatorY |  | Unknown | 类别：nonconst |
| ToolsPropertyDraggableValueVector2f | GetX |  | CString | 类别：nonconst |
| ToolsPropertyDraggableValueVector2f | GetY |  | CString | 类别：nonconst |
| ToolsPropertyDraggableValueVector2f | OnMouseDragFinishedX |  | void |  |
| ToolsPropertyDraggableValueVector2f | OnMouseDragFinishedY |  | void |  |
| ToolsPropertyDraggableValueVector2f | OnMouseDragStartedX |  | void |  |
| ToolsPropertyDraggableValueVector2f | OnMouseDragStartedY |  | void |  |
| ToolsPropertyDraggableValueVector2f | Self |  | ToolsPropertyDraggableValueVector2f |  |
| ToolsPropertyDraggableValueVector2f | SetX |  | void |  |
| ToolsPropertyDraggableValueVector2f | SetY |  | void |  |
| ToolsPropertyDraggableValueVector2f | UpdateValueX |  | void |  |
| ToolsPropertyDraggableValueVector2f | UpdateValueY |  | void |  |
| ToolsPropertyDraggableValueVector2i | AccessSelf |  | ToolsPropertyDraggableValueVector2i | 类别：const |
| ToolsPropertyDraggableValueVector2i | GetValidatorX |  | Unknown | 类别：nonconst |
| ToolsPropertyDraggableValueVector2i | GetValidatorY |  | Unknown | 类别：nonconst |
| ToolsPropertyDraggableValueVector2i | GetX |  | CString | 类别：nonconst |
| ToolsPropertyDraggableValueVector2i | GetY |  | CString | 类别：nonconst |
| ToolsPropertyDraggableValueVector2i | OnMouseDragFinishedX |  | void |  |
| ToolsPropertyDraggableValueVector2i | OnMouseDragFinishedY |  | void |  |
| ToolsPropertyDraggableValueVector2i | OnMouseDragStartedX |  | void |  |
| ToolsPropertyDraggableValueVector2i | OnMouseDragStartedY |  | void |  |
| ToolsPropertyDraggableValueVector2i | Self |  | ToolsPropertyDraggableValueVector2i |  |
| ToolsPropertyDraggableValueVector2i | SetX |  | void |  |
| ToolsPropertyDraggableValueVector2i | SetY |  | void |  |
| ToolsPropertyDraggableValueVector2i | UpdateValueX |  | void |  |
| ToolsPropertyDraggableValueVector2i | UpdateValueY |  | void |  |
| ToolsPropertyDraggableValueVector3f | AccessSelf |  | ToolsPropertyDraggableValueVector3f | 类别：const |
| ToolsPropertyDraggableValueVector3f | GetValidatorX |  | Unknown | 类别：nonconst |
| ToolsPropertyDraggableValueVector3f | GetValidatorY |  | Unknown | 类别：nonconst |
| ToolsPropertyDraggableValueVector3f | GetValidatorZ |  | Unknown | 类别：nonconst |
| ToolsPropertyDraggableValueVector3f | GetX |  | CString | 类别：nonconst |
| ToolsPropertyDraggableValueVector3f | GetY |  | CString | 类别：nonconst |
| ToolsPropertyDraggableValueVector3f | GetZ |  | CString | 类别：nonconst |
| ToolsPropertyDraggableValueVector3f | OnMouseDragFinishedX |  | void |  |
| ToolsPropertyDraggableValueVector3f | OnMouseDragFinishedY |  | void |  |
| ToolsPropertyDraggableValueVector3f | OnMouseDragFinishedZ |  | void |  |
| ToolsPropertyDraggableValueVector3f | OnMouseDragStartedX |  | void |  |
| ToolsPropertyDraggableValueVector3f | OnMouseDragStartedY |  | void |  |
| ToolsPropertyDraggableValueVector3f | OnMouseDragStartedZ |  | void |  |
| ToolsPropertyDraggableValueVector3f | Self |  | ToolsPropertyDraggableValueVector3f |  |
| ToolsPropertyDraggableValueVector3f | SetX |  | void |  |
| ToolsPropertyDraggableValueVector3f | SetY |  | void |  |
| ToolsPropertyDraggableValueVector3f | SetZ |  | void |  |
| ToolsPropertyDraggableValueVector3f | UpdateValueX |  | void |  |
| ToolsPropertyDraggableValueVector3f | UpdateValueY |  | void |  |
| ToolsPropertyDraggableValueVector3f | UpdateValueZ |  | void |  |
| ToolsPropertyDraggableValueVector3i | AccessSelf |  | ToolsPropertyDraggableValueVector3i | 类别：const |
| ToolsPropertyDraggableValueVector3i | GetValidatorX |  | Unknown | 类别：nonconst |
| ToolsPropertyDraggableValueVector3i | GetValidatorY |  | Unknown | 类别：nonconst |
| ToolsPropertyDraggableValueVector3i | GetValidatorZ |  | Unknown | 类别：nonconst |
| ToolsPropertyDraggableValueVector3i | GetX |  | CString | 类别：nonconst |
| ToolsPropertyDraggableValueVector3i | GetY |  | CString | 类别：nonconst |
| ToolsPropertyDraggableValueVector3i | GetZ |  | CString | 类别：nonconst |
| ToolsPropertyDraggableValueVector3i | OnMouseDragFinishedX |  | void |  |
| ToolsPropertyDraggableValueVector3i | OnMouseDragFinishedY |  | void |  |
| ToolsPropertyDraggableValueVector3i | OnMouseDragFinishedZ |  | void |  |
| ToolsPropertyDraggableValueVector3i | OnMouseDragStartedX |  | void |  |
| ToolsPropertyDraggableValueVector3i | OnMouseDragStartedY |  | void |  |
| ToolsPropertyDraggableValueVector3i | OnMouseDragStartedZ |  | void |  |
| ToolsPropertyDraggableValueVector3i | Self |  | ToolsPropertyDraggableValueVector3i |  |
| ToolsPropertyDraggableValueVector3i | SetX |  | void |  |
| ToolsPropertyDraggableValueVector3i | SetY |  | void |  |
| ToolsPropertyDraggableValueVector3i | SetZ |  | void |  |
| ToolsPropertyDraggableValueVector3i | UpdateValueX |  | void |  |
| ToolsPropertyDraggableValueVector3i | UpdateValueY |  | void |  |
| ToolsPropertyDraggableValueVector3i | UpdateValueZ |  | void |  |
| ToolsPropertyDraggableValueVector4i | AccessSelf |  | ToolsPropertyDraggableValueVector4i | 类别：const |
| ToolsPropertyDraggableValueVector4i | GetValidatorW |  | Unknown | 类别：nonconst |
| ToolsPropertyDraggableValueVector4i | GetValidatorX |  | Unknown | 类别：nonconst |
| ToolsPropertyDraggableValueVector4i | GetValidatorY |  | Unknown | 类别：nonconst |
| ToolsPropertyDraggableValueVector4i | GetValidatorZ |  | Unknown | 类别：nonconst |
| ToolsPropertyDraggableValueVector4i | GetW |  | CString | 类别：nonconst |
| ToolsPropertyDraggableValueVector4i | GetX |  | CString | 类别：nonconst |
| ToolsPropertyDraggableValueVector4i | GetY |  | CString | 类别：nonconst |
| ToolsPropertyDraggableValueVector4i | GetZ |  | CString | 类别：nonconst |
| ToolsPropertyDraggableValueVector4i | OnMouseDragFinishedW |  | void |  |
| ToolsPropertyDraggableValueVector4i | OnMouseDragFinishedX |  | void |  |
| ToolsPropertyDraggableValueVector4i | OnMouseDragFinishedY |  | void |  |
| ToolsPropertyDraggableValueVector4i | OnMouseDragFinishedZ |  | void |  |
| ToolsPropertyDraggableValueVector4i | OnMouseDragStartedW |  | void |  |
| ToolsPropertyDraggableValueVector4i | OnMouseDragStartedX |  | void |  |
| ToolsPropertyDraggableValueVector4i | OnMouseDragStartedY |  | void |  |
| ToolsPropertyDraggableValueVector4i | OnMouseDragStartedZ |  | void |  |
| ToolsPropertyDraggableValueVector4i | Self |  | ToolsPropertyDraggableValueVector4i |  |
| ToolsPropertyDraggableValueVector4i | SetW |  | void |  |
| ToolsPropertyDraggableValueVector4i | SetX |  | void |  |
| ToolsPropertyDraggableValueVector4i | SetY |  | void |  |
| ToolsPropertyDraggableValueVector4i | SetZ |  | void |  |
| ToolsPropertyDraggableValueVector4i | UpdateValueW |  | void |  |
| ToolsPropertyDraggableValueVector4i | UpdateValueX |  | void |  |
| ToolsPropertyDraggableValueVector4i | UpdateValueY |  | void |  |
| ToolsPropertyDraggableValueVector4i | UpdateValueZ |  | void |  |
| ToolsPropertyPath | AccessSelf |  | ToolsPropertyPath | 类别：const |
| ToolsPropertyPath | GetPathFontColor |  | CVector4f | 类别：nonconst |
| ToolsPropertyPath | GetPathValue |  | CString | 类别：nonconst |
| ToolsPropertyPath | GetTooltipText |  | CString | 类别：nonconst |
| ToolsPropertyPath | OpenFileDialog |  | void |  |
| ToolsPropertyPath | Self |  | ToolsPropertyPath |  |
| ToolsPropertyPath | SetPathFromText |  | void |  |
| ToolsPropertyRangedValueFloat | AccessSelf |  | ToolsPropertyRangedValueFloat | 类别：const |
| ToolsPropertyRangedValueFloat | GetMax |  | float | 类别：nonconst |
| ToolsPropertyRangedValueFloat | GetMin |  | float | 类别：nonconst |
| ToolsPropertyRangedValueFloat | GetStep |  | float | 类别：nonconst |
| ToolsPropertyRangedValueFloat | GetValue |  | float | 类别：nonconst |
| ToolsPropertyRangedValueFloat | GetWheelStep |  | float | 类别：nonconst |
| ToolsPropertyRangedValueFloat | OnSetValueEnd | PdxGuiWidget | void |  |
| ToolsPropertyRangedValueFloat | OnSetValueStart | PdxGuiWidget | void |  |
| ToolsPropertyRangedValueFloat | Self |  | ToolsPropertyRangedValueFloat |  |
| ToolsPropertyRangedValueFloat | SetValue |  | void |  |
| ToolsPropertyRangedValueFloat | SetValueFromText | Unknown | void |  |
| ToolsPropertyRangedValueInt | AccessSelf |  | ToolsPropertyRangedValueInt | 类别：const |
| ToolsPropertyRangedValueInt | GetMax |  | int32 | 类别：nonconst |
| ToolsPropertyRangedValueInt | GetMin |  | int32 | 类别：nonconst |
| ToolsPropertyRangedValueInt | GetStep |  | int32 | 类别：nonconst |
| ToolsPropertyRangedValueInt | GetValue |  | int32 | 类别：nonconst |
| ToolsPropertyRangedValueInt | GetWheelStep |  | int32 | 类别：nonconst |
| ToolsPropertyRangedValueInt | OnSetValueEnd | PdxGuiWidget | void |  |
| ToolsPropertyRangedValueInt | OnSetValueStart | PdxGuiWidget | void |  |
| ToolsPropertyRangedValueInt | Self |  | ToolsPropertyRangedValueInt |  |
| ToolsPropertyRangedValueInt | SetValue |  | void |  |
| ToolsPropertyRangedValueInt | SetValueFromText | Unknown | void |  |
| ToolsPropertyTextureStringValue | AccessSelf |  | ToolsPropertyTextureStringValue | 类别：const |
| ToolsPropertyTextureStringValue | GetTexture |  | Unknown | 类别：nonconst |
| ToolsPropertyTextureStringValue | GetTexturePath |  | CString | 类别：nonconst |
| ToolsPropertyTextureStringValue | SelectTexture |  | void |  |
| ToolsPropertyTextureStringValue | Self |  | ToolsPropertyTextureStringValue |  |
| ToolsPropertyTextureStringValue | SetValueFromText |  | void |  |
| ToolsPropertyTextureValue | AccessSelf |  | ToolsPropertyTextureValue | 类别：const |
| ToolsPropertyTextureValue | GetTexture |  | Unknown | 类别：nonconst |
| ToolsPropertyTextureValue | GetTexturePath |  | CString | 类别：nonconst |
| ToolsPropertyTextureValue | SelectTexture |  | void |  |
| ToolsPropertyTextureValue | Self |  | ToolsPropertyTextureValue |  |
| ToolsPropertyTextureValue | SetValueFromText |  | void |  |
| ToolsPropertyValueList | AccessSelf |  | ToolsPropertyValueList | 类别：const |
| ToolsPropertyValueList | AddItem |  | void |  |
| ToolsPropertyValueList | CanAddOrRemoveItems |  | bool |  |
| ToolsPropertyValueList | RemoveItem | int32 | void |  |
| ToolsPropertyValueList | Self |  | ToolsPropertyValueList |  |
| ToolsPropertyValueListEntry | AccessSelf |  | ToolsPropertyValueListEntry | 类别：const |
| ToolsPropertyValueListEntry | GetIndex |  | int32 | 类别：nonconst |
| ToolsPropertyValueListEntry | GetLabel |  | CString | 类别：nonconst |
| ToolsPropertyValueListEntry | HasLabel |  | bool |  |
| ToolsPropertyValueListEntry | IsItemVisible |  | bool |  |
| ToolsPropertyValueListEntry | Self |  | ToolsPropertyValueListEntry |  |
| ToolsPropertyVfsMountPath | AccessSelf |  | ToolsPropertyVfsMountPath | 类别：const |
| ToolsPropertyVfsMountPath | CloseBrowser |  | void |  |
| ToolsPropertyVfsMountPath | GetFullPath |  | CString | 类别：nonconst |
| ToolsPropertyVfsMountPath | GetFullPathFromMountTag | Unknown | CString | 类别：nonconst |
| ToolsPropertyVfsMountPath | GetMountTagIndex |  | CVector2i | 类别：nonconst |
| ToolsPropertyVfsMountPath | GetPathFontColor |  | CVector4f | 类别：nonconst |
| ToolsPropertyVfsMountPath | GetTags |  | Unknown | 类别：nonconst |
| ToolsPropertyVfsMountPath | GetVfsMountPathAsString |  | CString | 类别：nonconst |
| ToolsPropertyVfsMountPath | GetVfsPath |  | CString | 类别：nonconst |
| ToolsPropertyVfsMountPath | IsBrowserOpen |  | bool |  |
| ToolsPropertyVfsMountPath | IsDisplayModeFullPath |  | bool |  |
| ToolsPropertyVfsMountPath | OpenBrowser |  | void |  |
| ToolsPropertyVfsMountPath | Self |  | ToolsPropertyVfsMountPath |  |
| ToolsPropertyVfsMountPath | SetMountTagIndex |  | void |  |
| ToolsPropertyVfsMountPath | SetVfsPathFromText |  | void |  |
| ToolsPropertyVfsMountPath | ToggleBrowser |  | void |  |
| ToolsPropertyVfsMountPath | ToggleDisplayMode |  | void |  |
| ToolsSearch | AccessSelf |  | ToolsSearch | 类别：const |
| ToolsSearch | Results |  | Unknown |  |
| ToolsSearch | Search |  | void |  |
| ToolsSearch | Self |  | ToolsSearch |  |
| ToolsSearchResult | AccessSelf |  | ToolsSearchResult | 类别：const |
| ToolsSearchResult | Callback |  | void |  |
| ToolsSearchResult | Description |  | CUTF8String |  |
| ToolsSearchResult | DoesTooltipMatch |  | bool |  |
| ToolsSearchResult | Self |  | ToolsSearchResult |  |
| ToolsSearchResult | SortScore |  | int32 |  |
| ToolsSearchResult | Text |  | CUTF8String |  |
| ToolsSearchResult | Tooltip |  | CUTF8String |  |
| ToolsUndoableValueBundleBool | AccessSelf |  | ToolsUndoableValueBundleBool | 类别：const |
| ToolsUndoableValueBundleBool | Self |  | ToolsUndoableValueBundleBool |  |
| ToolsUndoableValueBundleBool | ShouldDisplayMixedValuesOverlay |  | bool |  |
| ToolsUndoableValueBundleCColor | AccessSelf |  | ToolsUndoableValueBundleCColor | 类别：const |
| ToolsUndoableValueBundleCColor | Self |  | ToolsUndoableValueBundleCColor |  |
| ToolsUndoableValueBundleCColor | ShouldDisplayMixedValuesOverlay |  | bool |  |
| ToolsUndoableValueBundleCString | AccessSelf |  | ToolsUndoableValueBundleCString | 类别：const |
| ToolsUndoableValueBundleCString | GetTextboxDisplayValue |  | CString | 类别：nonconst |
| ToolsUndoableValueBundleCString | Self |  | ToolsUndoableValueBundleCString |  |
| ToolsUndoableValueBundleCString | SetIsFocused | bool | void |  |
| ToolsUndoableValueBundleCString | SetValueOnFocusOut |  | void |  |
| ToolsUndoableValueBundleCString | ShouldDisplayMixedValuesOverlay |  | bool |  |
| ToolsUndoableValueBundleColor | AccessSelf |  | ToolsUndoableValueBundleColor | 类别：const |
| ToolsUndoableValueBundleColor | Self |  | ToolsUndoableValueBundleColor |  |
| ToolsUndoableValueBundleColor | ShouldDisplayMixedValuesOverlay |  | bool |  |
| ToolsUndoableValueBundleFloat | AccessSelf |  | ToolsUndoableValueBundleFloat | 类别：const |
| ToolsUndoableValueBundleFloat | GetTextboxDisplayValue |  | CString | 类别：nonconst |
| ToolsUndoableValueBundleFloat | Self |  | ToolsUndoableValueBundleFloat |  |
| ToolsUndoableValueBundleFloat | SetIsFocused | bool | void |  |
| ToolsUndoableValueBundleFloat | SetValueOnFocusOut |  | void |  |
| ToolsUndoableValueBundleFloat | ShouldDisplayMixedValuesOverlay |  | bool |  |
| ToolsUndoableValueBundleInt | AccessSelf |  | ToolsUndoableValueBundleInt | 类别：const |
| ToolsUndoableValueBundleInt | GetTextboxDisplayValue |  | CString | 类别：nonconst |
| ToolsUndoableValueBundleInt | Self |  | ToolsUndoableValueBundleInt |  |
| ToolsUndoableValueBundleInt | SetIsFocused | bool | void |  |
| ToolsUndoableValueBundleInt | SetValueOnFocusOut |  | void |  |
| ToolsUndoableValueBundleInt | ShouldDisplayMixedValuesOverlay |  | bool |  |
| ToolsUndoableValueBundleString | AccessSelf |  | ToolsUndoableValueBundleString | 类别：const |
| ToolsUndoableValueBundleString | GetTextboxDisplayValue |  | CString | 类别：nonconst |
| ToolsUndoableValueBundleString | Self |  | ToolsUndoableValueBundleString |  |
| ToolsUndoableValueBundleString | SetIsFocused | bool | void |  |
| ToolsUndoableValueBundleString | SetValueOnFocusOut |  | void |  |
| ToolsUndoableValueBundleString | ShouldDisplayMixedValuesOverlay |  | bool |  |
| ToolsUndoableValueBundleUint | AccessSelf |  | ToolsUndoableValueBundleUint | 类别：const |
| ToolsUndoableValueBundleUint | GetTextboxDisplayValue |  | CString | 类别：nonconst |
| ToolsUndoableValueBundleUint | Self |  | ToolsUndoableValueBundleUint |  |
| ToolsUndoableValueBundleUint | SetIsFocused | bool | void |  |
| ToolsUndoableValueBundleUint | SetValueOnFocusOut |  | void |  |
| ToolsUndoableValueBundleUint | ShouldDisplayMixedValuesOverlay |  | bool |  |
| ToolsUndoableValueBundleUint16 | AccessSelf |  | ToolsUndoableValueBundleUint16 | 类别：const |
| ToolsUndoableValueBundleUint16 | GetTextboxDisplayValue |  | CString | 类别：nonconst |
| ToolsUndoableValueBundleUint16 | Self |  | ToolsUndoableValueBundleUint16 |  |
| ToolsUndoableValueBundleUint16 | SetIsFocused | bool | void |  |
| ToolsUndoableValueBundleUint16 | SetValueOnFocusOut |  | void |  |
| ToolsUndoableValueBundleUint16 | ShouldDisplayMixedValuesOverlay |  | bool |  |
| ToolsUndoableValueBundleVec2f | AccessSelf |  | ToolsUndoableValueBundleVec2f | 类别：const |
| ToolsUndoableValueBundleVec2f | GetTextboxDisplayValue | int32 | CString | 类别：nonconst |
| ToolsUndoableValueBundleVec2f | Self |  | ToolsUndoableValueBundleVec2f |  |
| ToolsUndoableValueBundleVec2f | SetIsFocused | int32 bool | void |  |
| ToolsUndoableValueBundleVec2f | SetValue | int32 | void |  |
| ToolsUndoableValueBundleVec2f | SetValueOnFocusOut | int32 | void |  |
| ToolsUndoableValueBundleVec2f | ShouldDisplayMixedValuesOverlay | int32 | bool |  |
| ToolsUndoableValueBundleVec2i | AccessSelf |  | ToolsUndoableValueBundleVec2i | 类别：const |
| ToolsUndoableValueBundleVec2i | GetTextboxDisplayValue | int32 | CString | 类别：nonconst |
| ToolsUndoableValueBundleVec2i | Self |  | ToolsUndoableValueBundleVec2i |  |
| ToolsUndoableValueBundleVec2i | SetIsFocused | int32 bool | void |  |
| ToolsUndoableValueBundleVec2i | SetValue | int32 | void |  |
| ToolsUndoableValueBundleVec2i | SetValueOnFocusOut | int32 | void |  |
| ToolsUndoableValueBundleVec2i | ShouldDisplayMixedValuesOverlay | int32 | bool |  |
| ToolsUndoableValueBundleVec3f | AccessSelf |  | ToolsUndoableValueBundleVec3f | 类别：const |
| ToolsUndoableValueBundleVec3f | GetTextboxDisplayValue | int32 | CString | 类别：nonconst |
| ToolsUndoableValueBundleVec3f | GetValue |  | CVector3f | 类别：nonconst |
| ToolsUndoableValueBundleVec3f | Self |  | ToolsUndoableValueBundleVec3f |  |
| ToolsUndoableValueBundleVec3f | SetIsFocused | int32 bool | void |  |
| ToolsUndoableValueBundleVec3f | SetValue | int32 | void |  |
| ToolsUndoableValueBundleVec3f | SetValueFromColor |  | void |  |
| ToolsUndoableValueBundleVec3f | SetValueOnFocusOut | int32 | void |  |
| ToolsUndoableValueBundleVec3f | ShouldDisplayMixedValuesOverlay | int32 | bool |  |
| ToolsUndoableValueBundleVec3i | AccessSelf |  | ToolsUndoableValueBundleVec3i | 类别：const |
| ToolsUndoableValueBundleVec3i | GetTextboxDisplayValue | int32 | CString | 类别：nonconst |
| ToolsUndoableValueBundleVec3i | Self |  | ToolsUndoableValueBundleVec3i |  |
| ToolsUndoableValueBundleVec3i | SetIsFocused | int32 bool | void |  |
| ToolsUndoableValueBundleVec3i | SetValue | int32 | void |  |
| ToolsUndoableValueBundleVec3i | SetValueOnFocusOut | int32 | void |  |
| ToolsUndoableValueBundleVec3i | ShouldDisplayMixedValuesOverlay | int32 | bool |  |
| ToolsUndoableValueBundleVec4i | AccessSelf |  | ToolsUndoableValueBundleVec4i | 类别：const |
| ToolsUndoableValueBundleVec4i | GetTextboxDisplayValue | int32 | CString | 类别：nonconst |
| ToolsUndoableValueBundleVec4i | Self |  | ToolsUndoableValueBundleVec4i |  |
| ToolsUndoableValueBundleVec4i | SetIsFocused | int32 bool | void |  |
| ToolsUndoableValueBundleVec4i | SetValue | int32 | void |  |
| ToolsUndoableValueBundleVec4i | SetValueOnFocusOut | int32 | void |  |
| ToolsUndoableValueBundleVec4i | ShouldDisplayMixedValuesOverlay | int32 | bool |  |
| TooltipInfo | AccessSelf |  | TooltipInfo | 类别：const |
| TooltipInfo | GetTintColor |  | CVector4f | 类别：nonconst |
| TooltipInfo | Self |  | TooltipInfo |  |
| TopFrontend | AccessAlerts |  | Unknown | 类别：const |
| TopFrontend | AccessHiddenAlerts |  | Unknown | 类别：const |
| TopFrontend | AccessHiddenImportantActions |  | Unknown | 类别：const |
| TopFrontend | AccessHiddenProposals |  | Unknown | 类别：const |
| TopFrontend | AccessImportantActions |  | Unknown | 类别：const |
| TopFrontend | AccessProposals |  | Unknown | 类别：const |
| TopFrontend | AccessSelf |  | TopFrontend | 类别：const |
| TopFrontend | GetCurrentSituationSetting |  | int32 | 类别：nonconst |
| TopFrontend | GetNumHiddenImportantActions |  | int32 | 类别：nonconst |
| TopFrontend | GetNumUnreadImportantActions |  | int32 | 类别：nonconst |
| TopFrontend | GetTotalNumOfImportantActionGroups |  | int32 | 类别：nonconst |
| TopFrontend | Self |  | TopFrontend |  |
| TopFrontend | UnhideAllImportantActions |  | void |  |
| TopScope | AccessSelf |  | TopScope | 类别：const |
| TopScope | End |  | TopScope |  |
| TopScope | GetFlagName | Unknown | CString | 类别：nonconst |
| TopScope | GetLocalVariable | Unknown | Scope | 类别：nonconst |
| TopScope | GetRootScope |  | Scope | 类别：nonconst |
| TopScope | GetScriptValueDesc | ScriptValue | CString | 类别：nonconst |
| TopScope | GetValue | CString | CFixedPoint | 类别：nonconst |
| TopScope | ScriptValue | ScriptValue | CFixedPoint |  |
| TopScope | Self |  | TopScope |  |
| TopScope | gsIG | CString | InterestGroup |  |
| TopScope | gsInterestGroup | CString | InterestGroup |  |
| TopScope | sB | CString | Building |  |
| TopScope | sBG | CString | BuildingGroup |  |
| TopScope | sBT | CString | BuildingType |  |
| TopScope | sBuilding | CString | Building |  |
| TopScope | sBuildingGroup | CString | BuildingGroup |  |
| TopScope | sBuildingType | CString | BuildingType |  |
| TopScope | sC | CString | Country |  |
| TopScope | sCF | CString | CountryFormation |  |
| TopScope | sCM | CString | Company |  |
| TopScope | sCMT | CString | CompanyType |  |
| TopScope | sCOT | CString | CommanderOrderType |  |
| TopScope | sCU | CString | CombatUnit |  |
| TopScope | sCW | CString | CivilWar |  |
| TopScope | sCha | CString | Character |  |
| TopScope | sCharacter | CString | Character |  |
| TopScope | sCivilWar | CString | CivilWar |  |
| TopScope | sCommanderOrderType | CString | CommanderOrderType |  |
| TopScope | sCompany | CString | Company |  |
| TopScope | sCompanyType | CString | CompanyType |  |
| TopScope | sCountry | CString | Country |  |
| TopScope | sCountryFormation | CString | CountryFormation |  |
| TopScope | sCulture | CString | Culture |  |
| TopScope | sD | CString | Decision |  |
| TopScope | sDA | CString | DiplomaticAction |  |
| TopScope | sDC | CString | DiplomaticCatalyst |  |
| TopScope | sDCC | CString | DiplomaticCatalystCategory |  |
| TopScope | sDCT | CString | DiplomaticCatalystType |  |
| TopScope | sDD | CString | DiplomaticDemand |  |
| TopScope | sDP | CString | DiplomaticPlay |  |
| TopScope | sDPT | CString | DiplomaticPlayType |  |
| TopScope | sDR | CString | DiplomaticRelations |  |
| TopScope | sDecision | CString | Decision |  |
| TopScope | sDiplomaticAction | CString | DiplomaticAction |  |
| TopScope | sDiplomaticCatalyst | CString | DiplomaticCatalyst |  |
| TopScope | sDiplomaticCatalystCategory | CString | DiplomaticCatalystCategory |  |
| TopScope | sDiplomaticCatalystType | CString | DiplomaticCatalystType |  |
| TopScope | sDiplomaticDemand | CString | DiplomaticDemand |  |
| TopScope | sDiplomaticPact | CString | DiplomaticPact |  |
| TopScope | sDiplomaticPlay | CString | DiplomaticPlay |  |
| TopScope | sDiplomaticPlayType | CString | DiplomaticPlayType |  |
| TopScope | sDiplomaticRelations | CString | DiplomaticRelations |  |
| TopScope | sF | CString | Front |  |
| TopScope | sFront | CString | Front |  |
| TopScope | sG | CString | Goods |  |
| TopScope | sGoods | CString | Goods |  |
| TopScope | sHC | CString | HarvestCondition |  |
| TopScope | sHCA | CString | HarvestConditionArea |  |
| TopScope | sHCT | CString | HarvestConditionType |  |
| TopScope | sHQ | CString | Hq |  |
| TopScope | sHarvestCondition | CString | HarvestCondition |  |
| TopScope | sHarvestConditionArea | CString | HarvestConditionArea |  |
| TopScope | sHarvestConditionType | CString | HarvestConditionType |  |
| TopScope | sIGT | CString | InterestGroupTrait |  |
| TopScope | sIdeology | CString | 意识形态 |  |
| TopScope | sInstitution | CString | 机构 |  |
| TopScope | sInstitutionType | CString | 机构类型 |  |
| TopScope | sInterestGroupTrait | CString | 利益集团特质 |  |
| TopScope | sJE | CString | 日志条目 |  |
| TopScope | sJournalEntry | CString | 日志条目 |  |
| TopScope | sL | CString | 法律 |  |
| TopScope | sLaw | CString | 法律 |  |
| TopScope | sLawType | CString | 法律类型 |  |
| TopScope | sMilitaryFormation | CString | 军事编队 |  |
| TopScope | sP | CString | 政党 |  |
| TopScope | sPB | CString | 强权集团 |  |
| TopScope | sPBI | CString | 强权集团认同 |  |
| TopScope | sPBP | CString | 强权集团原则 |  |
| TopScope | sPL | CString | 政治游说团 |  |
| TopScope | sPLA | CString | 政治游说团安抚系数 |  |
| TopScope | sPLT | CString | 政治游说团类型 |  |
| TopScope | sPM | CString | 政治运动 |  |
| TopScope | sPMC | CString | 政治运动类别 |  |
| TopScope | sPMT | CString | 政治运动类型 |  |
| TopScope | sPT | CString | 人口类型 |  |
| TopScope | sPact | CString | 外交条约 |  |
| TopScope | sParty | CString | 政党 |  |
| TopScope | sPoliticalLobby | CString | 政治游说团 |  |
| TopScope | sPoliticalLobbyAppeasement | CString | 政治游说团安抚系数 |  |
| TopScope | sPoliticalLobbyType | CString | 政治游说团类型 |  |
| TopScope | sPoliticalMovement | CString | 政治运动 |  |
| TopScope | sPoliticalMovementCategory | CString | 政治运动类别 |  |
| TopScope | sPoliticalMovementType | CString | 政治运动类型 |  |
| TopScope | sPop | CString | 人口 |  |
| TopScope | sPopType | CString | 人口类型 |  |
| TopScope | sPowerBloc | CString | 强权集团 |  |
| TopScope | sPowerBlocIdentity | CString | 强权集团认同 |  |
| TopScope | sPowerBlocPrinciple | CString | 强权集团原则 |  |
| TopScope | sPowerBlocPrincipleGroup | CString | 强权集团原则组 |  |
| TopScope | sProvince | CString | 省份 |  |
| TopScope | sReligion | CString | 宗教 |  |
| TopScope | sS | CString | 州 |  |
| TopScope | sSR | CString | 战略区域 |  |
| TopScope | sSW | CString | 拉拢 |  |
| TopScope | sState | CString | 州 |  |
| TopScope | sStateRegion | CString | 州区域 |  |
| TopScope | sStrategicRegion | CString | 战略区域 |  |
| TopScope | sSway | CString | 拉拢 |  |
| TopScope | sT | CString | 技术 |  |
| TopScope | sTechnology | CString | 技术 |  |
| TopScope | sTreaty | CString | 条约 |  |
| TopScope | sTreatyArticle | CString | 条款 |  |
| TopScope | sW | CString | 战争 |  |
| TopScope | sWar | CString | 战争 |  |
| TopScope | sWarGoal | CString | 战争目标 |  |
| TopScope | sWarGoalType | CString | 战争目标类型 |  |
| TransferFormationPopup | AccessSelf |  | TransferFormationPopup | 类别：const |
| TransferFormationPopup | CanMoveCommander | StagedCommanderTransfer | bool |  |
| TransferFormationPopup | CanReset |  | bool |  |
| TransferFormationPopup | Confirm |  | Command |  |
| TransferFormationPopup | DeselectLeftFormation |  | void |  |
| TransferFormationPopup | DeselectRightFormation |  | void |  |
| TransferFormationPopup | GetConfirmDesc |  | CString | 类别：nonconst |
| TransferFormationPopup | GetConfirmationSound |  | Unknown | 类别：nonconst |
| TransferFormationPopup | GetContextualUnitTypeIcon |  | CString | 类别：nonconst |
| TransferFormationPopup | GetCulturalTexture | StagedUnitsWithType | Unknown | 类别：nonconst |
| TransferFormationPopup | GetHintDesc |  | CString | 类别：nonconst |
| TransferFormationPopup | GetInvalidCommanderTransferDesc | StagedCommanderTransfer | CString | 类别：nonconst |
| TransferFormationPopup | GetLeftFormation |  | MilitaryFormation | 类别：nonconst |
| TransferFormationPopup | GetLeftStagedFormation |  | StagedFormation | 类别：nonconst |
| TransferFormationPopup | GetOrganizationImpactDesc |  | CString | 类别：nonconst |
| TransferFormationPopup | GetResetDesc |  | CString | 类别：nonconst |
| TransferFormationPopup | GetRightFormation |  | MilitaryFormation | 类别：nonconst |
| TransferFormationPopup | GetRightStagedFormation |  | StagedFormation | 类别：nonconst |
| TransferFormationPopup | GetSelectedCommandersDesc |  | CString | 类别：nonconst |
| TransferFormationPopup | GetSelectedUnitsDesc |  | CString | 类别：nonconst |
| TransferFormationPopup | GetTravelTimeDesc |  | CString | 类别：nonconst |
| TransferFormationPopup | GetWarningsDesc |  | CString | 类别：nonconst |
| TransferFormationPopup | HasAnyUnitSelectedLeft |  | bool |  |
| TransferFormationPopup | HasAnyUnitSelectedRight |  | bool |  |
| TransferFormationPopup | HasArmyContext |  | bool |  |
| TransferFormationPopup | HasFleetContext |  | bool |  |
| TransferFormationPopup | HasLeftFormation |  | bool |  |
| TransferFormationPopup | HasRightFormation |  | bool |  |
| TransferFormationPopup | IsFormationSelected | Unknown | bool |  |
| TransferFormationPopup | MoveCommander | StagedCommanderTransfer | void |  |
| TransferFormationPopup | MoveConscripts | StagedUnitsWithType | void |  |
| TransferFormationPopup | MovePercentageLeft | Unknown | void |  |
| TransferFormationPopup | MovePercentageRight | Unknown | void |  |
| TransferFormationPopup | MoveRegulars | StagedUnitsWithType | void |  |
| TransferFormationPopup | MoveSelectedFromLeftToRight |  | void |  |
| TransferFormationPopup | MoveSelectedFromRightToLeft |  | void |  |
| TransferFormationPopup | Reset |  | void |  |
| TransferFormationPopup | SelectLeftFormation |  | void |  |
| TransferFormationPopup | SelectRightFormation |  | void |  |
| TransferFormationPopup | Self |  | TransferFormationPopup |  |
| TransferFormationPopup | SetSelectedLeftFormation | Unknown | void |  |
| TransferFormationPopup | SetSelectedRightFormation | Unknown | void |  |
| Treaty | AcceptTreatyProposal |  | Command |  |
| Treaty | AccessSelf |  | Treaty | 类别：const |
| Treaty | AreObligationsEffectuated |  | bool |  |
| Treaty | Binds | Country | bool |  |
| Treaty | DeclineTreatyProposal |  | Command |  |
| Treaty | DoesCallInObligation | Country | bool |  |
| Treaty | DoesOweObligation | Country | bool |  |
| Treaty | GetAcceptance | Country | int32 | 类别：nonconst |
| Treaty | GetAcceptanceBreakdown | Country | CString | 类别：nonconst |
| Treaty | GetAllArticles |  | Unknown | 类别：nonconst |
| Treaty | GetBindingDays |  | int32 | 类别：nonconst |
| Treaty | GetBindingDaysLeft |  | int32 | 类别：nonconst |
| Treaty | GetBindingPeriodEndGameDate |  | Date | 类别：nonconst |
| Treaty | GetBindingPeriodFormatted |  | CString | 类别：nonconst |
| Treaty | GetBindingPeriodRemainingFormatted |  | CString | 类别：nonconst |
| Treaty | GetBreakPenaltiesDesc | Country | CString | 类别：nonconst |
| Treaty | GetCanWithdrawDesc | Country | CString | 类别：nonconst |
| Treaty | GetCost | Country | CFixedPoint | 类别：nonconst |
| Treaty | GetCustom | CustomLocalization | CString | 类别：nonconst |
| Treaty | GetDemands |  | Unknown | 类别：nonconst |
| Treaty | GetDirectedEffectsDesc | Country | CString | 类别：nonconst |
| Treaty | GetEffectsDesc |  | CString | 类别：nonconst |
| Treaty | GetEnforcedOnCountry |  | Country | 类别：nonconst |
| Treaty | GetEnforcerCountry |  | Country | 类别：nonconst |
| Treaty | GetFirstCountry |  | Country | 类别：nonconst |
| Treaty | GetImmediateEffectsDesc | Unknown | CString | 类别：nonconst |
| Treaty | GetLeftCountry |  | Country | 类别：nonconst |
| Treaty | GetMutualAgreements |  | Unknown | 类别：nonconst |
| Treaty | GetMutualEffectsDesc |  | CString | 类别：nonconst |
| Treaty | GetMutualModifierDesc |  | CString | 类别：nonconst |
| Treaty | GetName |  | CString | 类别：nonconst |
| Treaty | GetNameNoFormatting |  | CString | 类别：nonconst |
| Treaty | GetNonFulfilledArticlesFromSource | Country | Unknown | 类别：nonconst |
| Treaty | GetNonFulfillmentDescFor | Country | CString | 类别：nonconst |
| Treaty | GetOffers |  | Unknown | 类别：nonconst |
| Treaty | GetOtherCountry | Country | Country | 类别：nonconst |
| Treaty | GetRelationsEffectDesc |  | CString | 类别：nonconst |
| Treaty | GetRightCountry |  | Country | 类别：nonconst |
| Treaty | GetSecondCountry |  | Country | 类别：nonconst |
| Treaty | GetShippingLaneOf | Unknown | ShippingLane | 类别：nonconst |
| Treaty | GetSourceModifierDesc |  | CString | 类别：nonconst |
| Treaty | GetStartDate |  | CString | 类别：nonconst |
| Treaty | GetStartGameDate |  | Date | 类别：nonconst |
| Treaty | GetTargetModifierDesc |  | CString | 类别：nonconst |
| Treaty | GetTooltipTag |  | CString | 类别：nonconst |
| Treaty | GetTreatyDeclineObligationDesc |  | CString | 类别：nonconst |
| Treaty | GetWithdrawPenaltiesDesc | Country | CString | 类别：nonconst |
| Treaty | IsDraft |  | bool |  |
| Treaty | IsEnforced |  | bool |  |
| Treaty | IsEnforcedOn | Country | bool |  |
| Treaty | IsFrozenFor | Country | bool |  |
| Treaty | IsFrozenForBothCountries |  | bool |  |
| Treaty | IsPinnedInOutliner |  | bool |  |
| Treaty | IsValid |  | bool |  |
| Treaty | MakeScope |  | Scope |  |
| Treaty | Self |  | Treaty |  |
| Treaty | TogglePinInOutliner |  | void |  |
| Treaty | WithdrawFromTreaty |  | Command |  |
| TreatyDraft | AccessSelf |  | TreatyDraft | 类别：const |
| TreatyDraft | AddArticle | ArticleType Country Country | void |  |
| TreatyDraft | AddArticleDraft | ArticleDraft | void |  |
| TreatyDraft | CanAskForObligation | Country | bool |  |
| TreatyDraft | CanCallInObligation | Country | bool |  |
| TreatyDraft | CanIncludeArticleDraft | ArticleDraft | bool |  |
| TreatyDraft | CanIncludeArticleType | ArticleType Country Country | bool |  |
| TreatyDraft | CanOweObligation | Country | bool |  |
| TreatyDraft | GetAcceptance | Country | int32 | 类别：nonconst |
| TreatyDraft | GetAcceptanceStatus | Country | CString | 类别：nonconst |
| TreatyDraft | GetAmendedTreaty |  | Treaty | 类别：nonconst |
| TreatyDraft | GetArticleTypeAcceptance | ArticleType Country | int32 | 类别：nonconst |
| TreatyDraft | GetArticleTypeAcceptanceBreakdown | ArticleType Country | CString | 类别：nonconst |
| TreatyDraft | GetArticleTypeAcceptanceBreakdownWithBuilding | Unknown Unknown Unknown | CString | 类别：nonconst |
| TreatyDraft | GetArticleTypeAcceptanceBreakdownWithCompany | Unknown Unknown Unknown | CString | 类别：nonconst |
| TreatyDraft | GetArticleTypeAcceptanceBreakdownWithCompanyAndBuilding | ArticleType Country Company BuildingType | CString | 类别：nonconst |
| TreatyDraft | GetArticleTypeAcceptanceBreakdownWithCountry | ArticleType Country Country | CString | 类别：nonconst |
| TreatyDraft | GetArticleTypeAcceptanceBreakdownWithGood | ArticleType Country Goods | CString | 类别：nonconst |
| TreatyDraft | GetArticleTypeAcceptanceBreakdownWithLaw | ArticleType Country LawType | CString | 类别：nonconst |
| TreatyDraft | GetArticleTypeAcceptanceBreakdownWithRegion | ArticleType Country StrategicRegion | CString | 类别：nonconst |
| TreatyDraft | GetArticleTypeAcceptanceBreakdownWithState | ArticleType Country State | CString | 类别：nonconst |
| TreatyDraft | GetArticleTypeAcceptanceWithBuilding | Unknown Unknown Unknown | int32 | 类别：nonconst |
| TreatyDraft | GetArticleTypeAcceptanceWithCompany | Unknown Unknown Unknown | int32 | 类别：nonconst |
| TreatyDraft | GetArticleTypeAcceptanceWithCompanyAndBuilding | ArticleType Country Company BuildingType | int32 | 类别：nonconst |
| TreatyDraft | GetArticleTypeAcceptanceWithCountry | ArticleType Country Country | int32 | 类别：nonconst |
| TreatyDraft | GetArticleTypeAcceptanceWithGood | ArticleType Country Goods | int32 | 类别：nonconst |
| TreatyDraft | GetArticleTypeAcceptanceWithLaw | ArticleType Country LawType | int32 | 类别：nonconst |
| TreatyDraft | GetArticleTypeAcceptanceWithRegion | ArticleType Country StrategicRegion | int32 | 类别：nonconst |
| TreatyDraft | GetArticleTypeAcceptanceWithState | ArticleType Country State | int32 | 类别：nonconst |
| TreatyDraft | GetArticleTypeInfluenceCostDesc | ArticleType Country | CString | 类别：nonconst |
| TreatyDraft | GetAskForObligationDesc | Country | CString | 类别：nonconst |
| TreatyDraft | GetBindingDays |  | int32 | 类别：nonconst |
| TreatyDraft | GetBindingPeriodDesc |  | CString | 类别：nonconst |
| TreatyDraft | GetBindingPeriodFormatted |  | CString | 类别：nonconst |
| TreatyDraft | GetBreakPenaltiesDesc |  | CString | 类别：nonconst |
| TreatyDraft | GetCallInObligationDesc | Country | CString | 类别：nonconst |
| TreatyDraft | GetCanIncludeArticleDraftDesc | ArticleDraft | CString | 类别：nonconst |
| TreatyDraft | GetCanIncludeArticleTypeDesc | ArticleType Country Country | CString | 类别：nonconst |
| TreatyDraft | GetCost | Country | CFixedPoint | 类别：nonconst |
| TreatyDraft | GetCustomName |  | CString | 类别：nonconst |
| TreatyDraft | GetFirstCountry |  | Country | 类别：nonconst |
| TreatyDraft | GetImmediateEffectsDesc |  | CString | 类别：nonconst |
| TreatyDraft | GetLeftCountry |  | Country | 类别：nonconst |
| TreatyDraft | GetName |  | CString | 类别：nonconst |
| TreatyDraft | GetNegativeAcceptanceBreakdown | Country | CString | 类别：nonconst |
| TreatyDraft | GetNumAvailableInputOptions | ArticleType Country | int32 | 类别：nonconst |
| TreatyDraft | GetOtherCountry | Unknown | Country | 类别：nonconst |
| TreatyDraft | GetOweObligationDesc | Country | CString | 类别：nonconst |
| TreatyDraft | GetPositiveAcceptanceBreakdown | Country | CString | 类别：nonconst |
| TreatyDraft | GetPotentialDemands |  | Unknown | 类别：nonconst |
| TreatyDraft | GetPotentialMutualAgreements |  | Unknown | 类别：nonconst |
| TreatyDraft | GetPotentialOffers |  | Unknown | 类别：nonconst |
| TreatyDraft | GetRelationsEffectDesc |  | CString | 类别：nonconst |
| TreatyDraft | GetRightCountry |  | Country | 类别：nonconst |
| TreatyDraft | GetSecondCountry |  | Country | 类别：nonconst |
| TreatyDraft | GetSelectedDemands |  | Unknown | 类别：nonconst |
| TreatyDraft | GetSelectedDirectedArticles | Unknown | Unknown | 类别：nonconst |
| TreatyDraft | GetSelectedMutualAgreements |  | Unknown | 类别：nonconst |
| TreatyDraft | GetSelectedOffers |  | Unknown | 类别：nonconst |
| TreatyDraft | GetUnavailableDemands |  | Unknown | 类别：nonconst |
| TreatyDraft | GetUnavailableMutualAgreements |  | Unknown | 类别：nonconst |
| TreatyDraft | GetUnavailableOffers |  | Unknown | 类别：nonconst |
| TreatyDraft | GetWithdrawPenaltiesDesc |  | CString | 类别：nonconst |
| TreatyDraft | HasSelectedArticle | ArticleType Country | bool |  |
| TreatyDraft | IsRenegotiation |  | bool |  |
| TreatyDraft | IsValidDataContext |  | bool |  |
| TreatyDraft | OnEditName |  | void |  |
| TreatyDraft | RandomizeName |  | void |  |
| TreatyDraft | RemoveArticle | ArticleDraft | void |  |
| TreatyDraft | ResetAll |  | void |  |
| TreatyDraft | ResetLeftSide |  | void |  |
| TreatyDraft | ResetRightSide |  | void |  |
| TreatyDraft | Self |  | TreatyDraft |  |
| TreatyDraft | SendProposal |  | Command |  |
| TreatyDraft | SetBindingDays | Unknown | void |  |
| TreatyDraft | ToggleAskForObligation | Country | void |  |
| TreatyDraft | ToggleCallInObligation | Country | void |  |
| TreatyDraft | ToggleOweObligation | Country | void |  |
| TreatyDraft | WillAIAccept | Country | bool |  |
| TreatyDraft | WillAIAcceptNoObligation | Unknown | bool |  |
| TreatyDraft | WillAIAcceptWithCallInObligation | Unknown | bool |  |
| TreatyDraft | WillAIAcceptWithOweObligation | Unknown | bool |  |
| TreatyDraft | WillAIMaybeAccept | Country | bool |  |
| TreatyDraft | WillAIMaybeAcceptNoObligation | Unknown | bool |  |
| TreatyDraft | WillAIMaybeAcceptWithCallInObligation | Unknown | bool |  |
| TreatyDraft | WillAIMaybeAcceptWithOweObligation | Unknown | bool |  |
| TreatyDraft | WillAskForObligation | Country | bool |  |
| TreatyDraft | WillCallInObligation | Country | bool |  |
| TreatyDraft | WillOweObligation | Country | bool |  |
| TreatyDraftPanel | AccessSelf |  | TreatyDraftPanel | 类别：const |
| TreatyDraftPanel | GetDraft |  | TreatyDraft | 类别：nonconst |
| TreatyDraftPanel | Self |  | TreatyDraftPanel |  |
| TreatyPanel | AccessSelf |  | TreatyPanel | 类别：const |
| TreatyPanel | GetTreaty |  | Treaty | 类别：nonconst |
| TreatyPanel | Self |  | TreatyPanel |  |
| Truce | AccessFirstCountry |  | Country | 类别：const |
| Truce | AccessSecondCountry |  | Country | 类别：const |
| Truce | AccessSelf |  | Truce | 类别：const |
| Truce | GetFirstCountry |  | Country | 类别：nonconst |
| Truce | GetFirstTruceDate |  | CString | 类别：nonconst |
| Truce | GetSecondCountry |  | Country | 类别：nonconst |
| Truce | GetSecondTruceDate |  | CString | 类别：nonconst |
| Truce | GetTruceExpirationDesc |  | CString | 类别：nonconst |
| Truce | Self |  | Truce |  |
| Tutorial | AccessSelf |  | Tutorial | 类别：const |
| Tutorial | CanReplayVoiceover |  | bool |  |
| Tutorial | GetReplayVoiceoverTooltip |  | CString | 类别：nonconst |
| Tutorial | GetStepHeaderInfo |  | CString | 类别：nonconst |
| Tutorial | GetStepInstructions |  | CString | 类别：nonconst |
| Tutorial | GetStepName |  | CString | 类别：nonconst |
| Tutorial | GetStepText |  | CString | 类别：nonconst |
| Tutorial | GetTransitionText | CString | CString | 类别：nonconst |
| Tutorial | GetTransitionTooltip | CString | CString | 类别：nonconst |
| Tutorial | HasStepInstructions |  | bool |  |
| Tutorial | HasTransition | CString | bool |  |
| Tutorial | IsTransitionEnabled | CString | bool |  |
| Tutorial | OnClickTransition | CString | void |  |
| Tutorial | ReplayVoiceover |  | void |  |
| Tutorial | Self |  | Tutorial |  |
| Tutorial | ShouldBeVisible |  | bool |  |
| Tweakable | AccessSelf |  | Tweakable | 类别：const |
| Tweakable | GetBool |  | bool | 类别：nonconst |
| Tweakable | GetColor |  | CVector4f | 类别：nonconst |
| Tweakable | GetDescription |  | CString | 类别：nonconst |
| Tweakable | GetEnumValueIndex |  | CVector2i | 类别：nonconst |
| Tweakable | GetEnumValues |  | Unknown | 类别：nonconst |
| Tweakable | GetGuiName |  | CString | 类别：nonconst |
| Tweakable | GetTweakableId |  | CString | 类别：nonconst |
| Tweakable | GetValue |  | CString | 类别：nonconst |
| Tweakable | OnValueEdited |  | void |  |
| Tweakable | Self |  | Tweakable |  |
| Tweakable | SetEnumValueIndex |  | void |  |
| TweakableCategory | AccessSelf |  | TweakableCategory | 类别：const |
| TweakableCategory | GetMargin |  | int32 | 类别：nonconst |
| TweakableCategory | GetName |  | CString | 类别：nonconst |
| TweakableCategory | IsExpanded |  | bool |  |
| TweakableCategory | Self |  | TweakableCategory |  |
| TweakableCategory | ToggleExpanded |  | void |  |
| TweakableCategory | ToggleTreeExpanded |  | void |  |
| TweakableUiEntry | AccessSelf |  | TweakableUiEntry | 类别：const |
| TweakableUiEntry | GetFriendlyName |  | CString | 类别：nonconst |
| TweakableUiEntry | GetMargin |  | int32 | 类别：nonconst |
| TweakableUiEntry | Self |  | TweakableUiEntry |  |
| TweakablesSnapshot | AccessSelf |  | TweakablesSnapshot | 类别：const |
| TweakablesSnapshot | Name |  | CString |  |
| TweakablesSnapshot | Self |  | TweakablesSnapshot |  |
| Tweaker | AccessSelf |  | Tweaker | 类别：const |
| Tweaker | CanResetTweakable | Tweakable | bool |  |
| Tweaker | ClearSearchString |  | void |  |
| Tweaker | GetSearchString |  | CString | 类别：nonconst |
| Tweaker | GetSelectedCategory |  | CString | 类别：nonconst |
| Tweaker | GetTweakableOriginalValue | Tweakable | CString | 类别：nonconst |
| Tweaker | GetTweakableValueColor | Tweakable | CVector4f | 类别：nonconst |
| Tweaker | OnOptionsPressed |  | void |  |
| Tweaker | OriginalSnapshotValid |  | bool |  |
| Tweaker | RebuildTree |  | void |  |
| Tweaker | RemoveSnapshot | CString | void |  |
| Tweaker | RemoveSnapshotEnabled | CString | bool |  |
| Tweaker | RenameSnapshot | CString | void |  |
| Tweaker | ResetTweakable | Tweakable | void |  |
| Tweaker | RootCategories |  | Unknown |  |
| Tweaker | SelectedSnapshot |  | CString |  |
| Tweaker | Self |  | Tweaker |  |
| Tweaker | SetSearchString |  | void |  |
| Tweaker | SnapshotVisible | CString | bool |  |
| Tweaker | TakeNewSnapshot |  | void |  |
| Tweaker | ToggleSelectedCategory | Unknown | void |  |
| Tweaker | ToggleSelectedSnapshot | CString | void |  |
| Tweaker | UpdateSnapshot | CString | void |  |
| Tweaker | UpdateSnapshotEnabled | CString | bool |  |
| Type | AccessSelf |  | Type | 类别：const |
| Type | Delete |  | void |  |
| Type | GetAssetName |  | CString | 类别：nonconst |
| Type | GetEntityIndex |  | CVector2i | 类别：nonconst |
| Type | GetInstanceCount |  | int32 | 类别：nonconst |
| Type | GetKey |  | CString | 类别：nonconst |
| Type | GetLayer |  | CString | 类别：nonconst |
| Type | GetLayerIndex |  | CVector2i | 类别：nonconst |
| Type | GetMeshIndex |  | CVector2i | 类别：nonconst |
| Type | GetTypeIndex |  | CVector2i | 类别：nonconst |
| Type | IsHidden |  | bool |  |
| Type | IsLocked |  | bool |  |
| Type | IsSelected |  | bool |  |
| Type | Rename |  | Unknown |  |
| Type | Self |  | Type |  |
| Type | SetClampToWaterLevel | Unknown | void |  |
| Type | SetEntityFromIndex |  | void |  |
| Type | SetLayerFromIndex |  | void |  |
| Type | SetMeshFromIndex |  | void |  |
| Type | SetRenderUnderwater | Unknown | void |  |
| Type | SetTypeFromIndex |  | void |  |
| Type | ShouldClampToWaterLevel |  | bool |  |
| Type | ShouldRenderUnderwater |  | bool |  |
| UndoHistoryViewerClient | AccessSelf |  | UndoHistoryViewerClient | 类别：const |
| UndoHistoryViewerClient | Self |  | UndoHistoryViewerClient |  |
| UndoHistoryViewerClient | Toggle |  | void |  |
| UndoStack | AccessSelf |  | UndoStack | 类别：const |
| UndoStack | Clear |  | void |  |
| UndoStack | IsClearable |  | bool |  |
| UndoStack | IsRedoable |  | bool |  |
| UndoStack | IsUndoable |  | bool |  |
| UndoStack | Redo |  | void |  |
| UndoStack | Self |  | UndoStack |  |
| UndoStack | Undo |  | void |  |
| UserDataNode | AccessSelf |  | UserDataNode | 类别：const |
| UserDataNode | Configure |  | void |  |
| UserDataNode | Id |  | CString |  |
| UserDataNode | Label |  | CString |  |
| UserDataNode | Self |  | UserDataNode |  |
| UserDataNode | TypeName |  | Unknown |  |
| VariableEntry | AccessSelf |  | VariableEntry | 类别：const |
| VariableEntry | Delete |  | void |  |
| VariableEntry | GetName |  | CString | 类别：nonconst |
| VariableEntry | Self |  | VariableEntry |  |
| VariableEntry | SetName |  | void |  |
| VariableInspectorEntry | AccessSelf |  | VariableInspectorEntry | 类别：const |
| VariableInspectorEntry | Delete |  | void |  |
| VariableInspectorEntry | Self |  | VariableInspectorEntry |  |
| VariableInspectorPlugin | AccessSelf |  | VariableInspectorPlugin | 类别：const |
| VariableInspectorPlugin | AccessVariables |  | Unknown | 类别：const |
| VariableInspectorPlugin | AddVariable |  | void |  |
| VariableInspectorPlugin | GetNumVariables |  | int32 | 类别：nonconst |
| VariableInspectorPlugin | Self |  | VariableInspectorPlugin |  |
| VariableInspectorVariable | AccessSelf |  | VariableInspectorVariable | 类别：const |
| VariableInspectorVariable | GetName |  | CString | 类别：nonconst |
| VariableInspectorVariable | GetRemainingTicks |  | int32 | 类别：nonconst |
| VariableInspectorVariable | Self |  | VariableInspectorVariable |  |
| VariableInspectorVariable | SetName |  | void |  |
| VariableInspectorVariable | SetRemainingTicks |  | void |  |
| VariableList | AccessEntries |  | Unknown | 类别：const |
| VariableList | AccessSelf |  | VariableList | 类别：const |
| VariableList | Delete |  | void |  |
| VariableList | GetName |  | CString | 类别：nonconst |
| VariableList | GetSize |  | int32 | 类别：nonconst |
| VariableList | Self |  | VariableList |  |
| VariableListEntry | AccessSelf |  | VariableListEntry | 类别：const |
| VariableListEntry | Delete |  | void |  |
| VariableListEntry | GetTicksRemaining |  | int32 | 类别：nonconst |
| VariableListEntry | Self |  | VariableListEntry |  |
| VariableListEntry | SetTicksRemaining |  | void |  |
| VariableListInspectorPlugin | AccessSelf |  | VariableListInspectorPlugin | 类别：const |
| VariableListInspectorPlugin | Self |  | VariableListInspectorPlugin |  |
| VariableListStore | AccessSelf |  | VariableListStore | 类别：const |
| VariableListStore | AccessVariableLists |  | Unknown | 类别：const |
| VariableListStore | AddNewEntry |  | void |  |
| VariableListStore | GetNewVariableListName |  | CString | 类别：nonconst |
| VariableListStore | GetNumVariableLists |  | int32 | 类别：nonconst |
| VariableListStore | GetVariableTicksRemaining |  | int32 | 类别：nonconst |
| VariableListStore | Self |  | VariableListStore |  |
| VariableListStore | SetNewVariableListName |  | void |  |
| VariableListStore | SetVariableTicksRemaining |  | void |  |
| VariableStore | AccessSelf |  | VariableStore | 类别：const |
| VariableStore | AccessVariables |  | Unknown | 类别：const |
| VariableStore | AddNewEntry |  | void |  |
| VariableStore | GetNewVariableName |  | CString | 类别：nonconst |
| VariableStore | GetNumVariables |  | int32 | 类别：nonconst |
| VariableStore | Self |  | VariableStore |  |
| VariableStore | SetNewVariableName |  | void |  |
| VariableSystem | AccessSelf |  | VariableSystem | 类别：const |
| VariableSystem | Clear | CString | void |  |
| VariableSystem | ClearIf | Unknown Unknown | void |  |
| VariableSystem | ClearMultiple | Unknown Unknown | void |  |
| VariableSystem | Exists | CString | bool |  |
| VariableSystem | Get | Unknown | CString |  |
| VariableSystem | HasValue | CString CString | bool |  |
| VariableSystem | Self |  | VariableSystem |  |
| VariableSystem | Set | CString Unknown | void |  |
| VariableSystem | SetIf | CString CString bool | void |  |
| VariableSystem | SetOrToggle | Unknown Unknown | void |  |
| VariableSystem | Toggle | CString | bool |  |
| VfsMountPathBrowser | AccessSelf |  | VfsMountPathBrowser | 类别：const |
| VfsMountPathBrowser | GetFilter |  | CString | 类别：nonconst |
| VfsMountPathBrowser | GetNodeTree |  | Unknown | 类别：nonconst |
| VfsMountPathBrowser | GetNumSelectedNodes |  | int32 | 类别：nonconst |
| VfsMountPathBrowser | HasDirectFilterMatch | VfsMountPathBrowserEntryNode | bool |  |
| VfsMountPathBrowser | IsNodeExpanded | VfsMountPathBrowserEntryNode | bool |  |
| VfsMountPathBrowser | IsNodeSelected | VfsMountPathBrowserEntryNode | bool |  |
| VfsMountPathBrowser | IsRefreshingDirectories |  | bool |  |
| VfsMountPathBrowser | OnCancel |  | void |  |
| VfsMountPathBrowser | OnFilterEdit |  | void |  |
| VfsMountPathBrowser | OnSelect |  | void |  |
| VfsMountPathBrowser | RefreshAllDirectories |  | void |  |
| VfsMountPathBrowser | Self |  | VfsMountPathBrowser |  |
| VfsMountPathBrowser | ToggleNodeExpanded | VfsMountPathBrowserEntryNode | void |  |
| VfsMountPathBrowser | ToggleNodeSelected | VfsMountPathBrowserEntryNode | void |  |
| VfsMountPathBrowserEntryNode | AccessSelf |  | VfsMountPathBrowserEntryNode | 类别：const |
| VfsMountPathBrowserEntryNode | GetBranchDepth | int32 int32 | CVector2f | 类别：nonconst |
| VfsMountPathBrowserEntryNode | GetFullPath |  | Unknown | 类别：nonconst |
| VfsMountPathBrowserEntryNode | GetName |  | Unknown | 类别：nonconst |
| VfsMountPathBrowserEntryNode | HasChildren |  | bool |  |
| VfsMountPathBrowserEntryNode | Self |  | VfsMountPathBrowserEntryNode |  |
| ViewerEntity | AccessSelf |  | ViewerEntity | 类别：const |
| ViewerEntity | CurrentFrame |  | int32 |  |
| ViewerEntity | CurrentTime |  | double |  |
| ViewerEntity | EntityLods |  | Unknown |  |
| ViewerEntity | HasStates |  | bool |  |
| ViewerEntity | HasUnsavedChanges |  | bool |  |
| ViewerEntity | IsLooping |  | bool |  |
| ViewerEntity | IsPlaying |  | bool |  |
| ViewerEntity | Name |  | Unknown |  |
| ViewerEntity | NumJoints |  | int32 |  |
| ViewerEntity | PauseAnimation |  | void |  |
| ViewerEntity | RollForward |  | void |  |
| ViewerEntity | Rollback |  | void |  |
| ViewerEntity | Scale |  | float |  |
| ViewerEntity | Self |  | ViewerEntity |  |
| ViewerEntity | SetCurrentFrameText | PdxGuiWidget | void |  |
| ViewerEntity | SetCurrentTimeText | PdxGuiWidget | void |  |
| ViewerEntity | State |  | ViewerEntityState |  |
| ViewerEntity | StepBackwards |  | void |  |
| ViewerEntity | StepForward |  | void |  |
| ViewerEntity | ToggleLooping |  | void |  |
| ViewerEntity | TogglePausePlay |  | void |  |
| ViewerEntityLodInfo | AccessSelf |  | ViewerEntityLodInfo | 类别：const |
| ViewerEntityLodInfo | Lod |  | int32 |  |
| ViewerEntityLodInfo | NumTriangles |  | int32 |  |
| ViewerEntityLodInfo | NumVertices |  | int32 |  |
| ViewerEntityLodInfo | Self |  | ViewerEntityLodInfo |  |
| ViewerEntityState | AccessSelf |  | ViewerEntityState | 类别：const |
| ViewerEntityState | AnimationLength |  | float |  |
| ViewerEntityState | HasAnimation |  | bool |  |
| ViewerEntityState | KeyframeLayers |  | Unknown |  |
| ViewerEntityState | Name |  | Unknown |  |
| ViewerEntityState | NumFrames |  | int32 |  |
| ViewerEntityState | Self |  | ViewerEntityState |  |
| War | AccessAttackers |  | Unknown | 类别：const |
| War | AccessDefenders |  | Unknown | 类别：const |
| War | AccessDiplomaticPlay |  | DiplomaticPlay | 类别：const |
| War | AccessFirstWarGoalsForPlayer |  | Unknown | 类别：const |
| War | AccessFronts |  | Unknown | 类别：const |
| War | AccessSecondWarGoalsForPlayer |  | Unknown | 类别：const |
| War | AccessSelf |  | War | 类别：const |
| War | AllowsNegotiatedPeace |  | bool |  |
| War | Capitulate | Country | Command |  |
| War | GetAcceptActivePeaceDealDesc |  | CString | 类别：nonconst |
| War | GetAcceptProposedPeaceDealDesc | Country | CString | 类别：nonconst |
| War | GetAcceptWhitePeaceDealDesc | Country | CString | 类别：nonconst |
| War | GetActiveBattles |  | Unknown | 类别：nonconst |
| War | GetActivePeaceDealAcceptanceScore | Country | CString | 类别：nonconst |
| War | GetActivePeaceDealAcceptanceTooltip | Country | CString | 类别：nonconst |
| War | GetAllBattles |  | Unknown | 类别：nonconst |
| War | GetAttackerLeader |  | Country | 类别：nonconst |
| War | GetAttackerListString |  | CString | 类别：nonconst |
| War | GetAttackers |  | Unknown | 类别：nonconst |
| War | GetAttackersWarGoals |  | Unknown | 类别：nonconst |
| War | GetCapitulationDesire | Country | int32 | 类别：nonconst |
| War | GetCapitulationDesireDesc | Country | CString | 类别：nonconst |
| War | GetCasualties | Country | CFixedPoint | 类别：nonconst |
| War | GetCountryProposingPeace |  | Country | 类别：nonconst |
| War | GetCustom | CustomLocalization | CString | 类别：nonconst |
| War | GetDaysUntilPeaceDealFails |  | int32 | 类别：nonconst |
| War | GetDefenderLeader |  | Country | 类别：nonconst |
| War | GetDefenderListString |  | CString | 类别：nonconst |
| War | GetDefenders |  | Unknown | 类别：nonconst |
| War | GetDefendersWarGoals |  | Unknown | 类别：nonconst |
| War | GetDiplomaticPlay |  | DiplomaticPlay | 类别：nonconst |
| War | GetEndedBattles |  | Unknown | 类别：nonconst |
| War | GetEnemyContestedWarGoalsFraction | Country | CFixedPoint | 类别：nonconst |
| War | GetInvasions |  | Unknown | 类别：nonconst |
| War | GetLeaderOfOppositeSide | Unknown | Country | 类别：nonconst |
| War | GetName |  | CString | 类别：nonconst |
| War | GetNameNoFormatting |  | CString | 类别：nonconst |
| War | GetPeaceDealValidationDesc |  | CString | 类别：nonconst |
| War | GetPressedWarGoalsString |  | CString | 类别：nonconst |
| War | GetProposedPeaceDealAcceptanceScore | Country Country | CString | 类别：nonconst |
| War | GetProposedPeaceDealAcceptanceTooltip | Country Country | CString | 类别：nonconst |
| War | GetSizeWeightedLostBattlesFraction | Country | CFixedPoint | 类别：nonconst |
| War | GetStartWarDescriptionForPlayer |  | CString | 类别：nonconst |
| War | GetStartWarTitleForPlayer |  | CString | 类别：nonconst |
| War | GetTooltipTag |  | CString | 类别：nonconst |
| War | GetTotalDeadWithWarExhaustionTooltip | Country | CString | 类别：nonconst |
| War | GetWarPtr |  | Unknown | 类别：nonconst |
| War | GetWarSupport | Country | CFixedPoint | 类别：nonconst |
| War | GetWhitePeaceDealAcceptanceScore | Unknown | CString | 类别：nonconst |
| War | GetWhitePeaceDealAcceptanceTooltip | Unknown | CString | 类别：nonconst |
| War | HasActivePeaceDeal |  | bool |  |
| War | HasActiveWhitePeaceDeal |  | bool |  |
| War | HasProposedWhitePeaceDeal | Unknown | bool |  |
| War | IsAttacker | Unknown | bool |  |
| War | IsDefender | Unknown | bool |  |
| War | IsParticipant | Country | bool |  |
| War | IsPeaceDealValid |  | bool |  |
| War | IsPeaceNegotiator | Unknown | bool |  |
| War | IsValid |  | bool |  |
| War | IsWarLeader | Country | bool |  |
| War | MakeScope |  | Scope |  |
| War | MustRatifyPeaceDeal | Unknown | bool |  |
| War | ProposePeaceDeal | Country | Command |  |
| War | Self |  | War |  |
| War | SetWhitePeace | Country | Command |  |
| War | ToggleAcceptPeace | Unknown | Command |  |
| War | WouldAcceptActivePeaceDeal | Unknown | bool |  |
| War | WouldAcceptProposedPeaceDeal | Unknown Unknown | bool |  |
| War | WouldAcceptWhitePeaceDeal | Unknown | bool |  |
| War | WouldActivePeaceDealBeAccepted |  | bool |  |
| War | WouldProposedPeaceDealBeAccepted | Country | bool |  |
| War | WouldWhitePeaceDealBeAccepted |  | bool |  |
| WarGoal | AccessSelf |  | WarGoal | 类别：const |
| WarGoal | CalcMakePrimaryDemandInfamyAmount |  | CFixedPoint |  |
| WarGoal | CalcMakePrimaryDemandManeuversCost |  | int32 |  |
| WarGoal | GetAddWarGoalDiplomaticIncidentDesc |  | CString | 类别：nonconst |
| WarGoal | GetArticleDraft |  | ArticleDraft | 类别：nonconst |
| WarGoal | GetArticleType |  | ArticleType | 类别：nonconst |
| WarGoal | GetCountryCreation |  | CountryCreation | 类别：nonconst |
| WarGoal | GetCountryFormation |  | CountryFormation | 类别：nonconst |
| WarGoal | GetCreator |  | Country | 类别：nonconst |
| WarGoal | GetCustom | CustomLocalization | CString | 类别：nonconst |
| WarGoal | GetDesc |  | CString | 类别：nonconst |
| WarGoal | GetDiplomaticPlay |  | DiplomaticPlay | 类别：nonconst |
| WarGoal | GetHolder |  | Country | 类别：nonconst |
| WarGoal | GetIcon |  | Unknown | 类别：nonconst |
| WarGoal | GetInfamyAmount |  | CFixedPoint | 类别：nonconst |
| WarGoal | GetInfamyDesc |  | CString | 类别：nonconst |
| WarGoal | GetIsContestedDesc |  | CString | 类别：nonconst |
| WarGoal | GetMakePrimaryDemandDiplomaticIncidentDesc |  | CString | 类别：nonconst |
| WarGoal | GetMakePrimaryDemandManeuversCostDesc |  | CString | 类别：nonconst |
| WarGoal | GetManeuversCostToAdd |  | int32 | 类别：nonconst |
| WarGoal | GetManeuversCostToAddDesc |  | CString | 类别：nonconst |
| WarGoal | GetName |  | CString | 类别：nonconst |
| WarGoal | GetNameNoFormatting |  | CString | 类别：nonconst |
| WarGoal | GetNameNoIcon |  | CString | 类别：nonconst |
| WarGoal | GetRegimeChangeLawsEnactedDesc |  | CString | 类别：nonconst |
| WarGoal | GetStartDiploPlayDesc |  | CString | 类别：nonconst |
| WarGoal | GetStatusString |  | CString | 类别：nonconst |
| WarGoal | GetSubjectTypeName |  | CString | 类别：nonconst |
| WarGoal | GetSwayDesc |  | CString | 类别：nonconst |
| WarGoal | GetTarget |  | Country | 类别：nonconst |
| WarGoal | GetTargetState |  | State | 类别：nonconst |
| WarGoal | GetTexture |  | Unknown | 类别：nonconst |
| WarGoal | GetTooltipTag |  | CString | 类别：nonconst |
| WarGoal | GetType |  | WarGoalType | 类别：nonconst |
| WarGoal | GetWar |  | War | 类别：nonconst |
| WarGoal | GetWarGoalStakeholder |  | Country | 类别：nonconst |
| WarGoal | HasCountryCreation |  | bool |  |
| WarGoal | HasCountryFormation |  | bool |  |
| WarGoal | HoldsArticle |  | bool |  |
| WarGoal | IsContested |  | bool |  |
| WarGoal | IsExecuted |  | bool |  |
| WarGoal | IsPartOfPlay |  | bool |  |
| WarGoal | IsPartOfWar |  | bool |  |
| WarGoal | IsPotentialWarGoal |  | bool |  |
| WarGoal | IsPressedInCurrentPeaceDeal |  | bool |  |
| WarGoal | IsPressedInPotentialPeaceDeal | Unknown | bool |  |
| WarGoal | IsPressedInShownPeaceDeal | Country | bool |  |
| WarGoal | IsPrimaryDemand |  | bool |  |
| WarGoal | IsValid |  | bool |  |
| WarGoal | IsValidDataContext |  | bool |  |
| WarGoal | MakeScope |  | Scope |  |
| WarGoal | MakeWarGoalPrimaryDemand | Country | Command |  |
| WarGoal | Self |  | WarGoal |  |
| WarGoal | SetArticleInputsFromDraft | Unknown | void |  |
| WarGoal | ShowHighlight |  | void |  |
| WarGoal | ToggleIsPressedInPotentialPeaceDeal | Country | Command |  |
| WarGoalDraft | AccessSelf |  | WarGoalDraft | 类别：const |
| WarGoalDraft | GetAddWarGoalDiplomaticIncidentDesc |  | CString | 类别：nonconst |
| WarGoalDraft | GetArticleDraft |  | ArticleDraft | 类别：nonconst |
| WarGoalDraft | GetArticleType |  | ArticleType | 类别：nonconst |
| WarGoalDraft | GetCountryCreation |  | CountryCreation | 类别：nonconst |
| WarGoalDraft | GetCountryFormation |  | CountryFormation | 类别：nonconst |
| WarGoalDraft | GetCreator |  | Country | 类别：nonconst |
| WarGoalDraft | GetDesc |  | CString | 类别：nonconst |
| WarGoalDraft | GetDiplomaticPlay |  | DiplomaticPlay | 类别：nonconst |
| WarGoalDraft | GetHolder |  | Country | 类别：nonconst |
| WarGoalDraft | GetIcon |  | Unknown | 类别：nonconst |
| WarGoalDraft | GetInfamyAmount |  | CFixedPoint | 类别：nonconst |
| WarGoalDraft | GetInfamyDesc |  | CString | 类别：nonconst |
| WarGoalDraft | GetManeuversCostToAdd |  | int32 | 类别：nonconst |
| WarGoalDraft | GetManeuversCostToAddDesc |  | CString | 类别：nonconst |
| WarGoalDraft | GetName |  | CString | 类别：nonconst |
| WarGoalDraft | GetNameNoFormatting |  | CString | 类别：nonconst |
| WarGoalDraft | GetNameNoIcon |  | CString | 类别：nonconst |
| WarGoalDraft | GetRegimeChangeLawsEnactedDesc |  | CString | 类别：nonconst |
| WarGoalDraft | GetSubjectTypeName |  | CString | 类别：nonconst |
| WarGoalDraft | GetTarget |  | Country | 类别：nonconst |
| WarGoalDraft | GetTargetRegion |  | StrategicRegion | 类别：nonconst |
| WarGoalDraft | GetTargetState |  | State | 类别：nonconst |
| WarGoalDraft | GetTexture |  | Unknown | 类别：nonconst |
| WarGoalDraft | GetTooltipTag |  | CString | 类别：nonconst |
| WarGoalDraft | GetType |  | WarGoalType | 类别：nonconst |
| WarGoalDraft | GetWarGoalStakeholder |  | Country | 类别：nonconst |
| WarGoalDraft | HasCountryCreation |  | bool |  |
| WarGoalDraft | HasCountryFormation |  | bool |  |
| WarGoalDraft | HasIncompleteSelectionData |  | bool |  |
| WarGoalDraft | HoldsArticle |  | bool |  |
| WarGoalDraft | IsValid |  | bool |  |
| WarGoalDraft | IsValidDataContext |  | bool |  |
| WarGoalDraft | Self |  | WarGoalDraft |  |
| WarGoalDraft | SetArticleInputsFromDraft | ArticleDraft | void |  |
| WarGoalDraft | ShowHighlight |  | void |  |
| WarGoalMarker | AccessSelf |  | WarGoalMarker | 类别：const |
| WarGoalMarker | AccessWarGoal |  | WarGoal | 类别：const |
| WarGoalMarker | GetWarGoal |  | WarGoal | 类别：nonconst |
| WarGoalMarker | Self |  | WarGoalMarker |  |
| WarGoalPanelPair | AccessSelf |  | WarGoalPanelPair | 类别：const |
| WarGoalPanelPair | GetWar |  | War | 类别：nonconst |
| WarGoalPanelPair | GetWarGoal |  | WarGoal | 类别：nonconst |
| WarGoalPanelPair | Self |  | WarGoalPanelPair |  |
| WarGoalType | AccessSelf |  | WarGoalType | 类别：const |
| WarGoalType | GetCustom | CustomLocalization | CString | 类别：nonconst |
| WarGoalType | GetDesc |  | CString | 类别：nonconst |
| WarGoalType | GetIcon |  | Unknown | 类别：nonconst |
| WarGoalType | GetKind |  | Unknown | 类别：nonconst |
| WarGoalType | GetName |  | CString | 类别：nonconst |
| WarGoalType | GetNameNoFormatting |  | CString | 类别：nonconst |
| WarGoalType | GetNameNoIcon |  | CString | 类别：nonconst |
| WarGoalType | GetTexture |  | Unknown | 类别：nonconst |
| WarGoalType | GetTooltipTag |  | CString | 类别：nonconst |
| WarGoalType | MakeScope |  | Scope |  |
| WarGoalType | Self |  | WarGoalType |  |
| WarGoalType | TargetsCountryCreation |  | bool |  |
| WarManager | AccessSelf |  | WarManager | 类别：const |
| WarManager | Self |  | WarManager |  |
| WarManager | ToggleWarPanel | War | void |  |
| WarPanel | AccessAttackers |  | Unknown | 类别：const |
| WarPanel | AccessAttackersWarGoals |  | Unknown | 类别：const |
| WarPanel | AccessDefenders |  | Unknown | 类别：const |
| WarPanel | AccessDefendersWarGoals |  | Unknown | 类别：const |
| WarPanel | AccessFronts |  | Unknown | 类别：const |
| WarPanel | AccessSelf |  | WarPanel | 类别：const |
| WarPanel | AccessWar |  | War | 类别：const |
| WarPanel | GetAttackersAvailableBattalionsRaw |  | int32 | 类别：nonconst |
| WarPanel | GetAttackersDeadRaw |  | int64 | 类别：nonconst |
| WarPanel | GetAttackersFlotillasRaw |  | int32 | 类别：nonconst |
| WarPanel | GetAttackersMobilizationRatioRaw |  | CFixedPoint | 类别：nonconst |
| WarPanel | GetAttackersMobilizedBattalionsRaw |  | int32 | 类别：nonconst |
| WarPanel | GetAttackersPotentialBattalionsRaw |  | int32 | 类别：nonconst |
| WarPanel | GetAttackersWarMobilizationCostRaw |  | CFixedPoint | 类别：nonconst |
| WarPanel | GetAttackersWoundedRaw |  | int64 | 类别：nonconst |
| WarPanel | GetDefendersAvailableBattalionsRaw |  | int32 | 类别：nonconst |
| WarPanel | GetDefendersDeadRaw |  | int64 | 类别：nonconst |
| WarPanel | GetDefendersFlotillasRaw |  | int32 | 类别：nonconst |
| WarPanel | GetDefendersMobilizationRatioRaw |  | CFixedPoint | 类别：nonconst |
| WarPanel | GetDefendersMobilizedBattalionsRaw |  | int32 | 类别：nonconst |
| WarPanel | GetDefendersPotentialBattalionsRaw |  | int32 | 类别：nonconst |
| WarPanel | GetDefendersWarMobilizationCostRaw |  | CFixedPoint | 类别：nonconst |
| WarPanel | GetDefendersWoundedRaw |  | int64 | 类别：nonconst |
| WarPanel | GetLeftAvailableBattalionsRaw |  | int32 | 类别：nonconst |
| WarPanel | GetLeftBattalionsBreakdown |  | CString | 类别：nonconst |
| WarPanel | GetLeftCostOfWarDesc |  | CString | 类别：nonconst |
| WarPanel | GetLeftCostOfWarRaw |  | CFixedPoint | 类别：nonconst |
| WarPanel | GetLeftDeadBreakdown |  | CString | 类别：nonconst |
| WarPanel | GetLeftDeadRaw |  | int64 | 类别：nonconst |
| WarPanel | GetLeftFlotillasBreakdown |  | CString | 类别：nonconst |
| WarPanel | GetLeftFlotillasRaw |  | int32 | 类别：nonconst |
| WarPanel | GetLeftLeader |  | Country | 类别：nonconst |
| WarPanel | GetLeftMobilizationRatioRaw |  | CFixedPoint | 类别：nonconst |
| WarPanel | GetLeftMobilizedBattalionsRaw |  | int32 | 类别：nonconst |
| WarPanel | GetLeftPotentialBattalionsRaw |  | int32 | 类别：nonconst |
| WarPanel | GetLeftWarParticipantsExcludingLeader |  | Unknown | 类别：nonconst |
| WarPanel | GetLeftWoundedBreakdown |  | CString | 类别：nonconst |
| WarPanel | GetLeftWoundedRaw |  | int64 | 类别：nonconst |
| WarPanel | GetRightAvailableBattalionsRaw |  | int32 | 类别：nonconst |
| WarPanel | GetRightBattalionsBreakdown |  | CString | 类别：nonconst |
| WarPanel | GetRightCostOfWarDesc |  | CString | 类别：nonconst |
| WarPanel | GetRightCostOfWarRaw |  | CFixedPoint | 类别：nonconst |
| WarPanel | GetRightDeadBreakdown |  | CString | 类别：nonconst |
| WarPanel | GetRightDeadRaw |  | int64 | 类别：nonconst |
| WarPanel | GetRightFlotillasBreakdown |  | CString | 类别：nonconst |
| WarPanel | GetRightFlotillasRaw |  | int32 | 类别：nonconst |
| WarPanel | GetRightLeader |  | Country | 类别：nonconst |
| WarPanel | GetRightMobilizationRatioRaw |  | CFixedPoint | 类别：nonconst |
| WarPanel | GetRightMobilizedBattalionsRaw |  | int32 | 类别：nonconst |
| WarPanel | GetRightPotentialBattalionsRaw |  | int32 | 类别：nonconst |
| WarPanel | GetRightWarParticipantsExcludingLeader |  | Unknown | 类别：nonconst |
| WarPanel | GetRightWoundedBreakdown |  | CString | 类别：nonconst |
| WarPanel | GetRightWoundedRaw |  | int64 | 类别：nonconst |
| WarPanel | GetWar |  | War | 类别：nonconst |
| WarPanel | IsShowingPeaceDeal |  | bool |  |
| WarPanel | Self |  | WarPanel |  |
| WarPanel | SortFronts | Unknown | void |  |
| WarPanel | ToggleShowPeaceDeal |  | void |  |
| WarParticipant | AccessSelf |  | WarParticipant | 类别：const |
| WarParticipant | GetCanCapitulateDesc |  | CString | 类别：nonconst |
| WarParticipant | GetCasualties |  | int64 | 类别：nonconst |
| WarParticipant | GetCountry |  | Country | 类别：nonconst |
| WarParticipant | GetExhaustionDesc |  | CString | 类别：nonconst |
| WarParticipant | GetNumDead |  | int64 | 类别：nonconst |
| WarParticipant | GetNumDeadFromAttrition |  | int64 | 类别：nonconst |
| WarParticipant | GetNumDeadFromBattle |  | int64 | 类别：nonconst |
| WarParticipant | GetNumWounded |  | int64 | 类别：nonconst |
| WarParticipant | GetNumWoundedFromAttrition |  | int64 | 类别：nonconst |
| WarParticipant | GetNumWoundedFromBattle |  | int64 | 类别：nonconst |
| WarParticipant | GetPosition | Unknown Unknown Unknown | CVector2f | 类别：nonconst |
| WarParticipant | GetWar |  | War | 类别：nonconst |
| WarParticipant | GetWarExhaustionFromAcceptanceOfDeadDesc |  | CString | 类别：nonconst |
| WarParticipant | GetWarSupportDesc |  | CString | 类别：nonconst |
| WarParticipant | GetWarSupportDescDelayed |  | CString | 类别：nonconst |
| WarParticipant | IsPeaceNegotiator |  | bool |  |
| WarParticipant | IsWarLeader |  | bool |  |
| WarParticipant | MustRatifyPeaceDeal |  | bool |  |
| WarParticipant | Self |  | WarParticipant |  |
| WarParticipant | WouldAcceptActivePeaceDeal |  | bool |  |
| WarParticipant | WouldAcceptProposedPeaceDeal | Country | bool |  |
| WarParticipant | WouldAcceptWhitePeaceDeal |  | bool |  |
| WorldMarketPanel | AccessSelf |  | WorldMarketPanel | 类别：const |
| WorldMarketPanel | Filter | CString | void |  |
| WorldMarketPanel | GetFilters |  | Unknown | 类别：nonconst |
| WorldMarketPanel | GetGoods | Unknown | Unknown | 类别：nonconst |
| WorldMarketPanel | GetMarkets |  | Unknown | 类别：nonconst |
| WorldMarketPanel | GetMarketsSortedOnExports |  | Unknown | 类别：nonconst |
| WorldMarketPanel | GetMarketsSortedOnImports |  | Unknown | 类别：nonconst |
| WorldMarketPanel | GetMaxImbalance |  | CFixedPoint | 类别：nonconst |
| WorldMarketPanel | GetMaxImbalanceScaledByBasePrice |  | CFixedPoint | 类别：nonconst |
| WorldMarketPanel | IsSelected | CString | bool |  |
| WorldMarketPanel | Self |  | WorldMarketPanel |  |
| WorldMarketPanel | SortGoods | CString | void |  |
| WorldMarketPanel | SortMarkets | Unknown | void |  |
| bool | AccessSelf |  | bool | 类别：常量 |
| bool | Self |  | bool |  |
| double | AccessSelf |  | double | 类别：常量 |
| double | Self |  | double |  |
| float | AccessSelf |  | float | 类别：常量 |
| float | Self |  | float |  |