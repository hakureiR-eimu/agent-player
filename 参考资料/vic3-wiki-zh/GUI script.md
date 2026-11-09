---
translated: 2026-10-27
translator: machine (glm-5.3)
title: GUI script
source: https://vic3.paradoxwikis.com/GUI_script
pageid: 7309
categories: [Potentially_outdated, 1.12, Expand, Modding]
fetched: 2026-10-27
---
请协助验证或更新本文中较旧的章节。至少部分章节最后验证于 [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) 1.12。

**GUI 脚本**是用于游戏 [GUI](Interface modding.md) 和 [localization](Localization.md)（本地化）中的脚本风格。它与大多数其他游戏文件中使用的脚本不同，不过两者存在一些对应的对象，例如国家（country）和变量。类似于游戏脚本的 [scope](Scope.md)，GUI 脚本使用数据类型（data type）；其中一些对应游戏 scope，另一些则仅用于 GUI 脚本。

GUI 脚本分为两类：*function*（函数）与 *promote*（提升）。

## 通用特性

所有 GUI 脚本均以"驼峰式命名"（CamelCase）书写[1]，即函数或 promote 中的每个单词首字母大写且不使用空格。每段 GUI 脚本总是由方括号包围。在方括号内，函数与 promote 可以通过"点链"（dot chaining）串联起来，例如 `[State.GetJobseekersDesc]`。从一个数据类型切换到另一个数据类型时，类似于 [scope](Scope.md) 之间的点链。

某些函数和 promote 接受参数，参数用紧跟在函数或 promote 之后的圆括号包围，例如 `[GetPopType('peasants').GetName]`。如果参数是游戏脚本对象，通常用单引号包围；如果是另一个数据类型、函数或 promote，则不需要。如果函数或 promote 接受多个参数，必须按顺序传入，各参数之间用逗号分隔。

某些函数和 promote 是"全局"的，即无需引用某个数据类型即可使用。所有其他数据类型的函数和 promote 都要求正确的数据类型处于"scope"之中。

## 数据类型列表

下表列出了 GUI 脚本中使用的所有至少拥有一个函数或 promote 的数据类型。

| 类型 | 描述 |
|---|---|
| AIAttitude |  |
| AIStrategy |  |
| AcceptanceStatus |  |
| AcceptanceStatusSegment |  |
| AccountInventory |  |
| Achievement |  |
| AchievementPopup |  |
| AchievementWindow |  |
| AddFriendWindow |  |
| AddWarGoalPanel |  |
| AgitatorSlot |  |
| Alert |  |
| AlertGroup |  |
| AlertOptionItem |  |
| AlertSettingsItem |  |
| Amendment |  |
| AmendmentType |  |
| AnchorItem |  |
| Application |  |
| Article |  |
| ArticleDraft |  |
| ArticleType |  |
| Attribute |  |
| AvailabilityEntry |  |
| Battle |  |
| BattleBuildingEntry |  |
| BattleCondition |  |
| BattleMarker |  |
| BattleMilitaryFormation |  |
| BattlePanel |  |
| BattleParticipant |  |
| BattleParticipantsPanel |  |
| BattleSide |  |
| BattleUnitType |  |
| BlurThreshold |  |
| BrushBool |  |
| BrushFloat |  |
| BrushSettings |  |
| BrushSettingsDropdown |  |
| BrushSettingsGlobal |  |
| BudgetPanel |  |
| Building |  |
| BuildingBrowserBuildingTypeItem |  |
| BuildingBrowserPanel |  |
| BuildingDetailsPanel |  |
| BuildingGroup |  |
| BuildingMarker |  |
| BuildingOwnership |  |
| BuildingPotentialMarker |  |
| BuildingProductionMethodsEntry |  |
| BuildingType |  |
| CFixedPoint |  |
| CPdxEnumValue |  |
| CPdxFloatRect |  |
| CPdxInputBindingSetting |  |
| CPdxIntRect |  |
| CString |  |
| CUTF8String |  |
| CVector2f |  |
| CVector2i |  |
| CVector3f |  |
| CVector3i |  |
| CVector4f |  |
| CVector4i |  |
| CanalType |  |
| ChangeLawPanel |  |
| ChangeProductionMethodMenuItem |  |
| ChangeProductionMethodsMenuItems |  |
| Character |  |
| CharacterInteraction |  |
| CharacterTrait |  |
| Chat |  |
| ChatMessage |  |
| ChatNotificationMessage |  |
| ChatTab |  |
| ChatWindow |  |
| ChildGenerator |  |
| ChildItem |  |
| Cities |  |
| CityMarker |  |
| CivilWar |  |
| CloudSaveData |  |
| CoatOfArms |  |
| CoatOfArmsPreviewWindow |  |
| CohesionLevel |  |
| ColonyMarker |  |
| ColorPicker |  |
| CombatUnit |  |
| CombatUnitGroup |  |
| CombatUnitType |  |
| Command |  |
| CommanderOrderType |  |
| CommanderPanel |  |
| CommanderRank |  |
| CompaniesPanel |  |
| Company |  |
| CompanyChangeNamePopup |  |
| CompanyCharter |  |
| CompanyCharterType |  |
| CompanyPanel |  |
| CompanyType |  |
| ConfirmationWindow |  |
| ConsoleMenuItem |  |
| ConsoleWindow |  |
| ConstructionPanel |  |
| ConstructionQueueElement |  |
| Container |  |
| ContextMenuItem |  |
| ContextualDiplomaticActionType |  |
| ContextualDiplomaticPact |  |
| CountriesPanel |  |
| Country |  |
| CountryCreation |  |
| CountryDefinition |  |
| CountryEntry |  |
| CountryFormation |  |
| CountryFormationPanel |  |
| CountryMarker |  |
| CountryPanel |  |
| CountryTrendPair |  |
| CreateAccount |  |
| CreateSocialProfileWindow |  |
| CreditsWindow |  |
| CulturalCommunity |  |
| Culture |  |
| CultureCasualtyStatistics |  |
| CultureInfoPanel |  |
| CurveEditor |  |
| CurvePoint |  |
| DataColorPicker |  |
| DataDynamicTrend |  |
| DataTrend |  |
| DatatypesExplorer |  |
| Date |  |
| Decision |  |
| Decree |  |
| DecreeMarker |  |
| DecreeType |  |
| DefineProxyNodeWindow |  |
| DetailData |  |
| DiplomaticAction |  |
| DiplomaticActionType |  |
| DiplomaticActionWindow |  |
| DiplomaticCatalyst |  |
| DiplomaticCatalystCategory |  |
| DiplomaticCatalystType |  |
| DiplomaticDemand |  |
| DiplomaticOverviewPanel |  |
| DiplomaticPact |  |
| DiplomaticPlay |  |
| DiplomaticPlayConfirmation |  |
| DiplomaticPlayPanel |  |
| DiplomaticPlayType |  |
| DiplomaticRelations |  |
| DiscriminationTrait |  |
| DiscriminationTraitGroup |  |
| Dlc |  |
| DockableLayout |  |
| DockableLayoutManager |  |
| DockableWindow |  |
| DrawCmdsList |  |
| DrawCmdsViewer |  |
| EditorSettingCategory |  |
| EditorSettingsPage |  |
| EditorSettingsWindow |  |
| Election |  |
| ElectionPanel |  |
| EmitterNodeWindow |  |
| EmployeeTransfer |  |
| Encyclopedia |  |
| EncyclopediaEntry |  |
| EncyclopediaEntryView |  |
| EncyclopediaPage |  |
| EndPrepConfirm |  |
| EntityEditor |  |
| EntityEditorAudioEventHandler |  |
| EntityEditorEventLayer |  |
| EntityEditorKeyframe |  |
| EntityEditorTimelineState |  |
| EntityViewerProperties |  |
| EnumSettingEntry |  |
| Era |  |
| ErrorDeer |  |
| Ethnicity |  |
| EthnicityItem |  |
| Event |  |
| EventIcon |  |
| EventLayerForEntityEditor |  |
| EventMarker |  |
| EventMarkerListItem |  |
| EventOption |  |
| EventTargetSetupContext |  |
| EventWindow |  |
| ExilePool |  |
| ExportTool |  |
| EyeDropper |  |
| EyeDropperPackedSample |  |
| FeedMessageItem |  |
| FilterablePropertyList |  |
| FoodSecurity |  |
| FoodSecurityFilter |  |
| FormationMarker |  |
| FormationPanel |  |
| Friend |  |
| FriendListWindow |  |
| FriendRequest |  |
| FriendSearchResult |  |
| Friends |  |
| Front |  |
| FrontEndCreditsView |  |
| FrontEndLoadConfirmationWindow |  |
| FrontEndLoadView |  |
| FrontEndMainView |  |
| FrontEndMultiplayerView |  |
| FrontMarker |  |
| FrontMovementMarker |  |
| FrontPanel |  |
| FrontSide |  |
| GUIAchievement |  |
| GameConceptType |  |
| GameMpSetup |  |
| GameOverScreen |  |
| GameRule |  |
| GameRuleSetting |  |
| GameSetup |  |
| GeneCategory |  |
| GeneItem |  |
| GeneTemplate |  |
| GeneralInformationWindow |  |
| GenerationItem |  |
| GeographicRegion |  |
| GfxSkin |  |
| Goods |  |
| GoodsExpenseItem |  |
| GoodsList |  |
| GoodsLocalPricesPanel |  |
| GoodsPanel |  |
| GoodsPanelChildValue |  |
| GoodsPanelValue |  |
| GoodsProductionInfo |  |
| GoodsStatePanel |  |
| GoodsUsagePanel |  |
| GoodsWorldMarketPanel |  |
| GovernmentType |  |
| Graph |  |
| GraphInterfaceNodeWindow |  |
| GraphPanel |  |
| Group |  |
| GuiAnimationCurveEditor |  |
| GuiAnimationCurveEditorControlPoint |  |
| GuiAnimationCurveEditorLine |  |
| GuiAnimationCurveEditorViewport |  |
| GuiAnimationEditor |  |
| GuiAnimationEditorAnimSetEntry |  |
| GuiAnimationEditorAnimationEntry |  |
| GuiAnimationEditorAvailableTrack |  |
| GuiAnimationEditorKeyframe |  |
| GuiAnimationEditorMetadataCtx |  |
| GuiAnimationEditorPlayer |  |
| GuiAnimationEditorPlayerSpeedMultiplierEntry |  |
| GuiAnimationEditorRuler |  |
| GuiAnimationEditorRulerResolutionEntry |  |
| GuiAnimationEditorUniversalTrack |  |
| GuiAnimationEditorViewportBase |  |
| GuiAnimationEditorViewportUserInput |  |
| GuiAnimationTimelineViewport |  |
| GuiContext |  |
| GuiCurrentDrag |  |
| GuiDataProfiler |  |
| GuiDataProfilerEntryNode |  |
| GuiEditorTooltip |  |
| GuiGameRule |  |
| GuiGameRulePreset |  |
| HQMarker |  |
| HQMovementMarker |  |
| HarvestCondition |  |
| HarvestConditionArea |  |
| HarvestConditionList |  |
| HarvestConditionRegionMarker |  |
| HarvestConditionType |  |
| Heightmap |  |
| HeightmapPainter |  |
| HeightmapPainterMode |  |
| HeightmapResolution |  |
| HighlightManager |  |
| HistoryViewer |  |
| HomelandMarker |  |
| Hq |  |
| Ideology |  |
| ImportTool |  |
| Importable |  |
| ImportableGroup |  |
| ImportantAlert |  |
| InfoboxNodeWindow |  |
| InformationPanel |  |
| InformationPanelBar |  |
| IngameHud |  |
| InputActionBinding |  |
| InspectorPanel |  |
| Institution |  |
| InstitutionInvestmentLevel |  |
| InstitutionType |  |
| Interest |  |
| InterestGroup |  |
| InterestGroupAndTraitPair |  |
| InterestGroupMarker |  |
| InterestGroupPanel |  |
| InterestGroupTrait |  |
| InterestingCountryItem |  |
| InterestingCountrySetting |  |
| Invasion |  |
| InvasionMarker |  |
| InvasionPanel |  |
| InvasionPlannerPopup |  |
| JominiGUISetting |  |
| JominiGameRules |  |
| JominiNotification |  |
| JominiNotificationOverlay |  |
| JominiPasswordPopup |  |
| JominiServer |  |
| JominiServerBrowserGui |  |
| JominiSettingsWindow |  |
| JournalEntry |  |
| JournalEntryGroup |  |
| JournalEntryPanel |  |
| JournalEntryType |  |
| JournalPanel |  |
| KeyframeEditor |  |
| KeyframeEventEditor |  |
| KeyframeWidget |  |
| Label |  |
| LabelingHelper |  |
| Law |  |
| LawGroup |  |
| LawType |  |
| Layer |  |
| LayerTreeItem |  |
| LegalDocsViewer |  |
| LegitimacyLevel |  |
| LensOption |  |
| LensTab |  |
| LensToolbar |  |
| LibertyDesireLevel |  |
| LoadIngameWindow |  |
| LoadingScreenManager |  |
| LobbyPlayer |  |
| LobbyView |  |
| Location |  |
| LocationFinder |  |
| LogEntry |  |
| LogViewer |  |
| LogViewerCategory |  |
| LogViewerEntry |  |
| LogViewerType |  |
| LoginView |  |
| LoyaltyType |  |
| MPConfig |  |
| MapContentEditorMode |  |
| MapContentEditorOptions |  |
| MapContentEditorViewport |  |
| MapContentEntryDesc |  |
| MapContentLayerDesc |  |
| MapContentPanel |  |
| MapContentPropertyGroup |  |
| MapContentPropertyGroupsGui |  |
| MapContentSelector |  |
| MapContentSelectorGui |  |
| MapEditor |  |
| MapEditorGui |  |
| MapEditorLayerBorder |  |
| MapEditorLayerBorderDockable |  |
| MapInteraction |  |
| MapInteractionManager |  |
| MapListActivateConscriptionCenterOption |  |
| MapListActivateConscriptionCenterPanel |  |
| MapListBuildingOption |  |
| MapListBuildingPanel |  |
| MapListColonyOption |  |
| MapListCountriesPanel |  |
| MapListCountryOption |  |
| MapListDecreeOption |  |
| MapListDecreePanel |  |
| MapListDeployMilitaryFormationToFrontOption |  |
| MapListDeployMilitaryFormationToFrontPanel |  |
| MapListDiploActionOption |  |
| MapListHarvestConditionAreasPanel |  |
| MapListHarvestConditionOption |  |
| MapListInterestGroupOption |  |
| MapListInterestGroupsPanel |  |
| MapListMarketOption |  |
| MapListMarketsPanel |  |
| MapListMilitaryFormationOption |  |
| MapListMilitaryFormationPanel |  |
| MapListOption |  |
| MapListPanel |  |
| MapListPanelManager |  |
| MapListPowerBlocInvitationPanel |  |
| MapListPowerBlocOption |  |
| MapListPowerBlocsPanel |  |
| MapListStateOption |  |
| MapListStatePanel |  |
| MapListStrategicRegionOption |  |
| MapListStrategicRegionsPanel |  |
| MapMode |  |
| MapModeList |  |
| MapNotification |  |
| MapObjectMask |  |
| MapObjectPainter |  |
| MapObjectPainterMode |  |
| MapObjectPainterOptions |  |
| MapObjectTool |  |
| Market |  |
| MarketGoods |  |
| MarketPanel |  |
| MarketsMarker |  |
| MarketsMarkerListItem |  |
| MaskEntry |  |
| MaskManagerEntry |  |
| MaskPainterDynamicTerrain |  |
| MaskPainterManager |  |
| MaskPainterMapContentPanel |  |
| MaskPainterMode |  |
| MaskPainterTool |  |
| MaskPainterViewport |  |
| Material |  |
| MaterialBrowser |  |
| MaterialEntry |  |
| MaterialMix |  |
| MaterialMixBrush |  |
| MaterialMixEntry |  |
| MaterialPaintingMode |  |
| Materials |  |
| MaterialsSample |  |
| MeshImporter |  |
| MeshImporterBrowser |  |
| MeshImporterBrowserEntry |  |
| MeshImporterMaterialEntry |  |
| MeshImporterMaterials |  |
| MessageFeedHandler |  |
| MessageSettingsWindow |  |
| MetadataWindow |  |
| MilitaryFormation |  |
| MilitaryFormationBorrowSetting |  |
| MilitaryFormationChangeNamePopup |  |
| MilitaryFormationColor |  |
| MilitaryFormationFlag |  |
| MilitaryFormationUnitEntry |  |
| MilitaryPanelBuildingEntry |  |
| MixBrushMode |  |
| MobilizationOption |  |
| MobilizationOptionGroup |  |
| Modifier |  |
| ModifierBreakdown |  |
| ModifierEntry |  |
| ModifierNodeData |  |
| ModifierNodeDebuggerView |  |
| ModifierNodeDetailsView |  |
| ModifierNodeGraphItem |  |
| ModifierNodeGraphLine |  |
| ModifierNodeListView |  |
| ModifiersPanel |  |
| MoveTool |  |
| MultiplayerSetupWindow |  |
| MultiplayerSynchronizationInfo |  |
| MusicPlayer |  |
| MusicPlayerCategory |  |
| MusicTrack |  |
| NationalAwakeningMarker |  |
| NationalizeBuildingGroup |  |
| NationalizeBuildingTypeGroup |  |
| NationalizeBuildingWindow |  |
| Node |  |
| NodeEditorSearch |  |
| NodeError |  |
| NodeLine |  |
| NodePin |  |
| NodeWindow |  |
| NonRegisteredDockable |  |
| NotificationDummyContext |  |
| NotificationOptionItem |  |
| NotificationSettingsItem |  |
| Nudger |  |
| NudgerLayerEntryMapObjectDesc |  |
| NudgerMapContentGui |  |
| NudgerMapObjectPropertyListDockable |  |
| NudgerMode |  |
| ObjectBrowser |  |
| ObjectBrowserView |  |
| ObjectInspector |  |
| ObjectInspectorDockable |  |
| ObjectInspectorPlugin |  |
| ObjectPreset |  |
| ObjectProvider |  |
| Objective |  |
| ObjectiveType |  |
| ObstinanceMarker |  |
| OccupationPiechartData |  |
| OosData |  |
| OosWindow |  |
| OpinionMarker |  |
| OutgoingFriendRequest |  |
| Outliner |  |
| OutlinerEntry |  |
| OutputEntry |  |
| PanelMilitary |  |
| ParametricSelect |  |
| ParticleUserData |  |
| Party |  |
| PartyPanel |  |
| PastBattleMarker |  |
| PauseMenu |  |
| PdxAccount |  |
| PdxCoreSetting |  |
| PdxEnumSetting |  |
| PdxGuiFoldOut |  |
| PdxGuiGfxVideoControl |  |
| PdxGuiTableRow |  |
| PdxGuiTreeTable |  |
| PdxGuiWidget |  |
| PdxSetting |  |
| PdxSettingsWindow |  |
| PdxSettingsWindowCategory |  |
| PdxValueSetting |  |
| PieTimer |  |
| PieTimerSlice |  |
| Playable |  |
| Player |  |
| PlayerJoinRequest |  |
| PlayerMessageItem |  |
| PlotLine |  |
| PoliticalLobby |  |
| PoliticalLobbyAppeasementFactor |  |
| PoliticalLobbyMarker |  |
| PoliticalLobbyPanel |  |
| PoliticalLobbyType |  |
| PoliticalMovement |  |
| PoliticalMovementCategory |  |
| PoliticalMovementPanel |  |
| PoliticalMovementPopSupportFactor |  |
| PoliticalMovementType |  |
| PoliticsPanel |  |
| Pop |  |
| PopBrowserPanel |  |
| PopConsumptionGoods |  |
| PopDetailsPanel |  |
| PopList |  |
| PopListItem |  |
| PopNeed |  |
| PopType |  |
| PopWithIG |  |
| PopsOverviewPanel |  |
| PopulationGrouping |  |
| PopupManager |  |
| Portrait3dView |  |
| PortraitDataContext |  |
| PortraitEditorAnimationItem |  |
| PortraitEditorWindow |  |
| PortraitTooltip |  |
| PotentialLeaderIdeology |  |
| PowerBloc |  |
| PowerBlocCoaPiece |  |
| PowerBlocCoaPieceSelector |  |
| PowerBlocCustomizationPopup |  |
| PowerBlocFormation |  |
| PowerBlocFormationPanel |  |
| PowerBlocFormationPrincipleSlot |  |
| PowerBlocIdentity |  |
| PowerBlocMapTexture |  |
| PowerBlocMapTextureSelector |  |
| PowerBlocPanel |  |
| PowerBlocPrinciple |  |
| PowerBlocPrincipleData |  |
| PowerBlocPrincipleGroup |  |
| PowerBlocPrincipleSelectionWindow |  |
| PowerBlocPrincipleSlot |  |
| PowerBlocStatue |  |
| PowerBlocStatueAccessoryType |  |
| PowerBlocStatueAccessoryTypeSelector |  |
| PowerBlocStatueHeroType |  |
| PowerBlocStatuePedestalType |  |
| PrestigeGoodChangeNamePopup |  |
| PreviewMaskTexture |  |
| ProductionMarker |  |
| ProductionMethod |  |
| ProductionMethodConfirmationPopup |  |
| ProductionMethodGroup |  |
| ProgressInterface |  |
| PropertyListCategory |  |
| Proposal |  |
| Province |  |
| RandomizableValueFloat |  |
| RandomizableValueInt |  |
| ReformGovernment |  |
| ReleaseCountryWindow |  |
| Religion |  |
| ReligionInfoPanel |  |
| RemoveFriendConfirmWindow |  |
| RepackWindow |  |
| ResignConfirmationWindow |  |
| RevolutionaryMovementMarker |  |
| RightClickMenuManager |  |
| RulerSelectionPopup |  |
| Savable |  |
| SavableGroup |  |
| SaveDialog |  |
| SaveGame |  |
| SaveGameAnalysisView |  |
| SaveGameAnalyzer |  |
| SaveGameBlockData |  |
| SaveGameConfigView |  |
| SaveGameItem |  |
| SaveGameListView |  |
| SaveGameWindow |  |
| Scope |  |
| ScopeDebugData |  |
| ScopeDebugInspectorPlugin |  |
| ScopeObjectEditor |  |
| ScopeObjectProvider |  |
| ScopeObjectType |  |
| ScopedEditorSettingsCategory |  |
| ScriptProfilerEntry |  |
| ScriptProfilerFileLine |  |
| ScriptProfilerGui |  |
| ScriptRunnerInspector |  |
| ScriptRunnerResult |  |
| ScriptedButton |  |
| ScriptedGui |  |
| ScriptedProgressBar |  |
| SeaNodeMarker |  |
| SeaNodeMovementMarker |  |
| SeaRegionInfraMarker |  |
| SeaRegionPanel |  |
| SeaRegionWar |  |
| SearchListNodeWindow |  |
| SelectFromInputNodeWindow |  |
| SelectParticleUserDataDialog |  |
| SelectTool |  |
| ServerInformation |  |
| SettingCategory |  |
| SettingsPage |  |
| ShippingLane |  |
| SkinEditor |  |
| SmartBrushHeightRange |  |
| SmartBrushPattern |  |
| SmartBrushPresetManager |  |
| SmartMaterialPaintingMode |  |
| Social |  |
| SocialClass |  |
| SocialHierarchy |  |
| SocialNotificationWindow |  |
| SocialUI |  |
| SocialWidget |  |
| SocietyPanel |  |
| SplineAdjustmentTool |  |
| SplineAdjustmentToolMode |  |
| SplineRiverInteractionMode |  |
| SplineRiverTool |  |
| SplineStripTool |  |
| SplineStripToolMode |  |
| SplineToolsMapContentPanel |  |
| SplineTypeCreateSelectionDropdown |  |
| SplineTypeItem |  |
| SplineTypeSwitchSelectionDropdown |  |
| SplineVisibilityDropdown |  |
| StagedCommanderTransfer |  |
| StagedFormation |  |
| StagedUnitsWithType |  |
| StarvationType |  |
| State |  |
| StateGoods |  |
| StateInfraMarker |  |
| StateMarker |  |
| StateNameChangePopup |  |
| StatePopulationPanel |  |
| StateRegion |  |
| StateTrait |  |
| StatesPanel |  |
| StatusWidget |  |
| StrategicRegion |  |
| StrategicRegionMarker |  |
| SubjectType |  |
| SupplyNetworkEntry |  |
| Sway |  |
| SwayCountryPanel |  |
| SwayOffer |  |
| SwayOfferType |  |
| TaxBurdenItem |  |
| TechTreeItem |  |
| TechTreeLine |  |
| TechTreePanel |  |
| Technology |  |
| TechnologyUnlock |  |
| TerrainToolButton |  |
| TextureEntry |  |
| TextureImporter |  |
| TextureList |  |
| TextureListDirectory |  |
| TextureListTexture |  |
| TextureNodeWindow |  |
| TextureViewer |  |
| Theater |  |
| Theme |  |
| ThemeBulkSelectionGroup |  |
| ThemeCategory |  |
| ThemeWindow |  |
| TickTaskData |  |
| TickTaskDebuggerView |  |
| TickTaskDetailsView |  |
| TickTaskGraphItem |  |
| TickTaskGraphLine |  |
| TickTaskListView |  |
| TimeKeeper |  |
| TimedModifier |  |
| TimelineKeyframe |  |
| ToastMessageHandler |  |
| ToolDialog |  |
| ToolDialogButton |  |
| ToolMessageDialog |  |
| ToolProgressDialog |  |
| ToolProperty |  |
| ToolProperty2SearchList |  |
| ToolPropertyAction |  |
| ToolPropertyBool |  |
| ToolPropertyCColor |  |
| ToolPropertyCString |  |
| ToolPropertyColor |  |
| ToolPropertyCurve |  |
| ToolPropertyFloat |  |
| ToolPropertyInt |  |
| ToolPropertyInt16 |  |
| ToolPropertyInt8 |  |
| ToolPropertyList |  |
| ToolPropertySearchList |  |
| ToolPropertyString |  |
| ToolPropertyUint |  |
| ToolPropertyUint16 |  |
| ToolPropertyUint8 |  |
| ToolPropertyUndoableSearchList |  |
| ToolPropertyVec1fPercent |  |
| ToolPropertyVec2f |  |
| ToolPropertyVec2fPercent |  |
| ToolPropertyVec2i |  |
| ToolPropertyVec3f |  |
| ToolPropertyVec3i |  |
| ToolPropertyVec4i |  |
| ToolsPropertyDraggableValueFloat |  |
| ToolsPropertyDraggableValueInt |  |
| ToolsPropertyDraggableValueVector2f |  |
| ToolsPropertyDraggableValueVector2i |  |
| ToolsPropertyDraggableValueVector3f |  |
| ToolsPropertyDraggableValueVector3i |  |
| ToolsPropertyDraggableValueVector4i |  |
| ToolsPropertyPath |  |
| ToolsPropertyRangedValueFloat |  |
| ToolsPropertyRangedValueInt |  |
| ToolsPropertyTextureStringValue |  |
| ToolsPropertyTextureValue |  |
| ToolsPropertyValueList |  |
| ToolsPropertyValueListEntry |  |
| ToolsPropertyVfsMountPath |  |
| ToolsSearch |  |
| ToolsSearchResult |  |
| ToolsUndoableValueBundleBool |  |
| ToolsUndoableValueBundleCColor |  |
| ToolsUndoableValueBundleCString |  |
| ToolsUndoableValueBundleColor |  |
| ToolsUndoableValueBundleFloat |  |
| ToolsUndoableValueBundleInt |  |
| ToolsUndoableValueBundleString |  |
| ToolsUndoableValueBundleUint |  |
| ToolsUndoableValueBundleUint16 |  |
| ToolsUndoableValueBundleVec2f |  |
| ToolsUndoableValueBundleVec2i |  |
| ToolsUndoableValueBundleVec3f |  |
| ToolsUndoableValueBundleVec3i |  |
| ToolsUndoableValueBundleVec4i |  |
| TooltipInfo |  |
| TopFrontend |  |
| TopScope |  |
| TransferFormationPopup |  |
| Treaty |  |
| TreatyDraft |  |
| TreatyDraftPanel |  |
| TreatyPanel |  |
| Truce |  |
| Tutorial |  |
| Tweakable |  |
| TweakableCategory |  |
| TweakableUiEntry |  |
| TweakablesSnapshot |  |
| Tweaker |  |
| Type |  |
| UndoHistoryViewerClient |  |
| UndoStack |  |
| UserDataNode |  |
| VariableEntry |  |
| VariableInspectorEntry |  |
| VariableInspectorPlugin |  |
| VariableInspectorVariable |  |
| VariableList |  |
| VariableListEntry |  |
| VariableListInspectorPlugin |  |
| VariableListStore |  |
| VariableStore |  |
| VariableSystem |  |
| VfsMountPathBrowser |  |
| VfsMountPathBrowserEntryNode |  |
| ViewerEntity |  |
| ViewerEntityLodInfo |  |
| ViewerEntityState |  |
| War |  |
| WarGoal |  |
| WarGoalDraft |  |
| WarGoalMarker |  |
| WarGoalPanelPair |  |
| WarGoalType |  |
| WarManager |  |
| WarPanel |  |
| WarParticipant |  |
| WorldMarketPanel |  |
| bool |  |
| double |  |
| float |  |
| int16 |  |
| int32 |  |
| int64 |  |
| int8 |  |
| uint16 |  |
| uint32 |  |
| uint64 |  |
| uint8 |  |
| void |  |
| 类型 | 描述 |
|---|---|
| AIAttitude |  |
| AcceptanceStatus |  |
| AcceptanceStatusSegment |  |
| AddWarGoalPanel |  |
| AgitatorSlot |  |
| AlertSettingsItem |  |
| Amendment |  |
| AmendmentType |  |
| Article |  |
| ArticleDraft |  |
| Battle |  |
| BattleBuildingEntry |  |
| BattleMarker |  |
| BattlePanel |  |
| BattleParticipant |  |
| BattleParticipantsPanel |  |
| BattleSide |  |
| BattleUnitType |  |
| BrushSettings |  |
| BrushSettingsDropdown |  |
| BudgetPanel |  |
| Building |  |
| BuildingBrowserBuildingTypeItem |  |
| BuildingBrowserPanel |  |
| BuildingDetailsPanel |  |
| BuildingGroup |  |
| BuildingMarker |  |
| BuildingOwnership |  |
| BuildingPotentialMarker |  |
| BuildingProductionMethodsEntry |  |
| BuildingType |  |
| CanalType |  |
| ChangeLawPanel |  |
| ChangeProductionMethodMenuItem |  |
| Character |  |
| Chat |  |
| ChatNotificationMessage |  |
| ChatTab |  |
| CityMarker |  |
| CivilWar |  |
| ColonyMarker |  |
| CombatUnit |  |
| CombatUnitType |  |
| CommanderOrderType |  |
| CommanderPanel |  |
| Company |  |
| CompanyChangeNamePopup |  |
| CompanyCharter |  |
| CompanyPanel |  |
| CompanyType |  |
| ConstructionPanel |  |
| ConstructionQueueElement |  |
| ContextualDiplomaticActionType |  |
| ContextualDiplomaticPact |  |
| Country |  |
| CountryCreation |  |
| CountryDefinition |  |
| CountryFormation |  |
| CountryFormationPanel |  |
| CountryMarker |  |
| CountryPanel |  |
| CountryTrendPair |  |
| CulturalCommunity |  |
| Culture |  |
| CultureCasualtyStatistics |  |
| CultureInfoPanel |  |
| Decision |  |
| Decree |  |
| DecreeMarker |  |
| DecreeType |  |
| DiplomaticAction |  |
| DiplomaticActionType |  |
| DiplomaticActionWindow |  |
| DiplomaticCatalyst |  |
| DiplomaticCatalystCategory |  |
| DiplomaticCatalystType |  |
| DiplomaticDemand |  |
| DiplomaticOverviewPanel |  |
| DiplomaticPact |  |
| DiplomaticPlay |  |
| DiplomaticPlayConfirmation |  |
| DiplomaticPlayPanel |  |
| DiplomaticPlayType |  |
| DiplomaticRelations |  |
| DiscriminationTrait |  |
| DockableLayoutManager |  |
| EditorSettingsWindow |  |
| Election |  |
| ElectionPanel |  |
| EmployeeTransfer |  |
| Encyclopedia |  |
| EncyclopediaEntryView |  |
| EntityEditor |  |
| Event |  |
| EventIcon |  |
| EventMarker |  |
| EventTargetSetupContext |  |
| EventWindow |  |
| EyeDropper |  |
| EyeDropperPackedSample |  |
| FeedMessageItem |  |
| FoodSecurityFilter |  |
| FormationMarker |  |
| FormationPanel |  |
| Front |  |
| FrontEndLoadView |  |
| FrontEndMainView |  |
| FrontMarker |  |
| FrontMovementMarker |  |
| FrontPanel |  |
| FrontSide |  |
| GUIAchievement |  |
| GameMpSetup |  |
| GameRuleSetting |  |
| GameSetup |  |
| GeographicRegion |  |
| Goods |  |
| GoodsExpenseItem |  |
| GoodsList |  |
| GoodsLocalPricesPanel |  |
| GoodsPanel |  |
| GoodsPanelValue |  |
| GoodsProductionInfo |  |
| GoodsStatePanel |  |
| GoodsUsagePanel |  |
| GoodsWorldMarketPanel |  |
| GraphPanel |  |
| GuiGameRule |  |
| GuiGameRulePreset |  |
| HQMarker |  |
| HQMovementMarker |  |
| HarvestCondition |  |
| HarvestConditionArea |  |
| HarvestConditionType |  |
| HomelandMarker |  |
| Hq |  |
| Ideology |  |
| ImportantAlert |  |
| Institution |  |
| InstitutionType |  |
| Interest |  |
| InterestGroup |  |
| InterestGroupAndTraitPair |  |
| InterestGroupMarker |  |
| InterestGroupPanel |  |
| InterestGroupTrait |  |
| InterestingCountryItem |  |
| Invasion |  |
| InvasionMarker |  |
| InvasionPanel |  |
| InvasionPlannerPopup |  |
| JominiGameRules |  |
| JominiNotification |  |
| JominiSettingsWindow |  |
| JournalEntry |  |
| JournalEntryPanel |  |
| JournalEntryType |  |
| Law |  |
| LawGroup |  |
| LawType |  |
| LayerTreeItem |  |
| LensOption |  |
| LensToolbar |  |
| LoadIngameWindow |  |
| LoadingScreenManager |  |
| LobbyPlayer |  |
| LobbyView |  |
| LogViewer |  |
| MapContentEditorViewport |  |
| MapEditor |  |
| MapEditorGui |  |
| MapListActivateConscriptionCenterOption |  |
| MapListBuildingOption |  |
| MapListBuildingPanel |  |
| MapListColonyOption |  |
| MapListCountryOption |  |
| MapListDecreeOption |  |
| MapListDecreePanel |  |
| MapListDeployMilitaryFormationToFrontOption |  |
| MapListDiploActionOption |  |
| MapListHarvestConditionOption |  |
| MapListInterestGroupOption |  |
| MapListMarketOption |  |
| MapListOption |  |
| MapListPowerBlocInvitationPanel |  |
| MapListPowerBlocOption |  |
| MapListPowerBlocsPanel |  |
| MapListStateOption |  |
| MapListStrategicRegionOption |  |
| MapModeList |  |
| MapObjectPainterOptions |  |
| MapObjectTool |  |
| Market |  |
| MarketGoods |  |
| MarketPanel |  |
| MarketsMarker |  |
| MarketsMarkerListItem |  |
| MaskPainterViewport |  |
| MaterialBrowser |  |
| MaterialEntry |  |
| MaterialMixBrush |  |
| MaterialMixEntry |  |
| MaterialPaintingMode |  |
| MeshImporter |  |
| MilitaryFormation |  |
| MilitaryFormationChangeNamePopup |  |
| MilitaryFormationUnitEntry |  |
| MilitaryPanelBuildingEntry |  |
| MobilizationOption |  |
| Modifier |  |
| ModifierBreakdown |  |
| ModifierNodeDetailsView |  |
| ModifierNodeGraphItem |  |
| ModifiersPanel |  |
| MultiplayerSetupWindow |  |
| NationalAwakeningMarker |  |
| NationalizeBuildingGroup |  |
| NationalizeBuildingTypeGroup |  |
| NotificationSettingsItem |  |
| Objective |  |
| ObstinanceMarker |  |
| OccupationPiechartData |  |
| OosData |  |
| OpinionMarker |  |
| Outliner |  |
| OutlinerEntry |  |
| PanelMilitary |  |
| Party |  |
| PartyPanel |  |
| PastBattleMarker |  |
| PdxAccount |  |
| PdxGuiWidget |  |
| PdxSetting |  |
| Playable |  |
| Player |  |
| PlayerMessageItem |  |
| PoliticalLobby |  |
| PoliticalLobbyAppeasementFactor |  |
| PoliticalLobbyMarker |  |
| PoliticalLobbyPanel |  |
| PoliticalLobbyType |  |
| PoliticalMovement |  |
| PoliticalMovementCategory |  |
| PoliticalMovementPanel |  |
| PoliticalMovementType |  |
| PoliticsPanel |  |
| Pop |  |
| PopBrowserPanel |  |
| PopConsumptionGoods |  |
| PopDetailsPanel |  |
| PopList |  |
| PopListItem |  |
| PopNeed |  |
| PopType |  |
| PopWithIG |  |
| PopsOverviewPanel |  |
| PopulationGrouping |  |
| PopupManager |  |
| PortraitEditorWindow |  |
| PotentialLeaderIdeology |  |
| PowerBloc |  |
| PowerBlocCoaPiece |  |
| PowerBlocCoaPieceSelector |  |
| PowerBlocCustomizationPopup |  |
| PowerBlocFormation |  |
| PowerBlocFormationPanel |  |
| PowerBlocFormationPrincipleSlot |  |
| PowerBlocIdentity |  |
| PowerBlocMapTextureSelector |  |
| PowerBlocPanel |  |
| PowerBlocPrinciple |  |
| PowerBlocPrincipleData |  |
| PowerBlocPrincipleGroup |  |
| PowerBlocPrincipleSelectionWindow |  |
| PowerBlocPrincipleSlot |  |
| PowerBlocStatueAccessoryTypeSelector |  |
| PrestigeGoodChangeNamePopup |  |
| ProductionMarker |  |
| Proposal |  |
| Province |  |
| ReformGovernment |  |
| ReleaseCountryWindow |  |
| Religion |  |
| ReligionInfoPanel |  |
| RevolutionaryMovementMarker |  |
| SaveGameAnalysisView |  |
| SaveGameItem |  |
| SaveGameWindow |  |
| Scope |  |
| ScopeDebugInspectorPlugin |  |
| ScopedEditorSettingsCategory |  |
| ScriptProfilerGui |  |
| ScriptRunnerInspector |  |
| SeaNodeMovementMarker |  |
| SeaRegionInfraMarker |  |
| SeaRegionPanel |  |
| SeaRegionWar |  |
| ShippingLane |  |
| SmartBrushHeightRange |  |
| SmartBrushPattern |  |
| SocialClass |  |
| SocietyPanel |  |
| StagedCommanderTransfer |  |
| StagedFormation |  |
| StagedUnitsWithType |  |
| State |  |
| StateGoods |  |
| StateInfraMarker |  |
| StateMarker |  |
| StateNameChangePopup |  |
| StatePopulationPanel |  |
| StateRegion |  |
| StateTrait |  |
| StatesPanel |  |
| StrategicRegion |  |
| StrategicRegionMarker |  |
| SubjectType |  |
| SupplyNetworkEntry |  |
| Sway |  |
| SwayCountryPanel |  |
| SwayOffer |  |
| TechTreeItem |  |
| TechTreeLine |  |
| Technology |  |
| Theater |  |
| Theme |  |
| ThemeBulkSelectionGroup |  |
| ThemeCategory |  |
| ThemeWindow |  |
| TickTaskDetailsView |  |
| TickTaskGraphItem |  |
| TimeKeeper |  |
| ToastMessageHandler |  |
| TopScope |  |
| TransferFormationPopup |  |
| Treaty |  |
| TreatyDraft |  |
| TreatyDraftPanel |  |
| TreatyPanel |  |
| Truce |  |
| VariableEntry |  |
| VariableInspectorEntry |  |
| VariableInspectorPlugin |  |
| VariableInspectorVariable |  |
| VariableListEntry |  |
| VariableListInspectorPlugin |  |
| VariableListStore |  |
| VariableStore |  |
| VfsMountPathBrowser |  |
| ViewerEntity |  |
| War |  |
| WarGoal |  |
| WarGoalDraft |  |
| WarGoalMarker |  |
| WarGoalPanelPair |  |
| WarGoalType |  |
| WarPanel |  |
| WarParticipant |  |

### 数据类型描述

|  | 请协助完善本条目或本章节：补充更多描述，请[展开此处](https://vic3.paradoxwikis.com/index.php?title=GUI_script&action=edit)。 |
|---|---|

| 类型 | 描述 | 备注 |
|---|---|---|
| CFixedValue | 64 位有符号定点数，保留 5 位小数 | 最大 92233720368547.75807，最小 -92233720368547.75808 |

## 常量（const）与非 常量（nonconst）

GUI 脚本函数与提升（promote）分为两类：*const*（常量）与 *nonconst*（非常量）。二者在功能上通常完全相同，但在某些特定用途下可能只允许使用其中之一。

一般来说，以 "Access" 开头的函数和提升用于常量类型并返回常量类型，而以 "Get" 开头的则用于非常量类型并返回非常量类型。

少数函数和提升不遵循这一惯例：

- `GetTechnology('some_tech')` 返回一个常量
- `Country.GetFleetsBreakdown` 需要常量 Country 类型

## GUI 函数

GUI 函数通常从输入类型中获取某些信息，或以某种方式对其进行转换。

| 函数 | 参数 | 输出 | 描述 |
|---|---|---|---|
| Abs_CFixedPoint | CFixedPoint | CFixedPoint |  |
| Abs_float | float | float |  |
| Abs_int32 | int32 | int32 |  |
| Abs_int64 | int64 | int64 |  |
| AccessConstructionSpeeds |  | Unknown | 类别：const |
| AccessMapEditorLayerBorders |  | Unknown | 地图编辑器——访问所有图层边界。类别：const |
| AccessMetaPlayer |  | Player | 类别：const |
| AccessPlayer |  | Player | 类别：const |
| AccessScopeReference | Scope | Unknown | 类别：const |
| AddLocalizationIf | bool CString | CString |  |
| AddTextIf | bool CString | CString |  |
| Add_CFixedPoint | CFixedPoint CFixedPoint | CFixedPoint |  |
| Add_CVector2f | CVector2f CVector2f | CVector2f |  |
| Add_float | float float | float |  |
| Add_int32 | int32 int32 | int32 |  |
| Add_int64 | int64 int64 | int64 |  |
| Add_uint32 | uint32 uint32 | uint32 |  |
| Add_uint64 | uint64 uint64 | uint64 |  |
| And | bool bool | bool |  |
| And3 | bool bool bool | bool |  |
| And4 | bool bool bool bool | bool |  |
| And5 | bool bool bool bool bool | bool |  |
| And6 | bool bool bool bool bool bool | bool |  |
| And7 | bool bool bool bool bool bool bool | bool |  |
| And8 | bool bool bool bool bool bool bool bool | bool |  |
| AndEvalAll | Unknown Unknown | bool |  |
| AreAchievementsAvailable |  | bool |  |
| BetweenInclusiveOfMax_CFixedPoint | CFixedPoint CFixedPoint CFixedPoint | bool |  |
| BetweenInclusiveOfMax_float | float float float | bool |  |
| BetweenInclusiveOfMax_int32 | int32 int32 int32 | bool |  |
| BetweenInclusiveOfMax_int64 | int64 int64 int64 | bool |  |
| BetweenInclusiveOfMax_uint32 | uint32 uint32 uint32 | bool |  |
| BetweenInclusiveOfMax_uint64 | uint64 uint64 uint64 | bool |  |
| BetweenInclusiveOfMin_CFixedPoint | CFixedPoint CFixedPoint CFixedPoint | bool |  |
| BetweenInclusiveOfMin_float | float float float | bool |  |
| BetweenInclusiveOfMin_int32 | int32 int32 int32 | bool |  |
| BetweenInclusiveOfMin_int64 | int64 int64 int64 | bool |  |
| BetweenInclusiveOfMin_uint32 | uint32 uint32 uint32 | bool |  |
| BetweenInclusiveOfMin_uint64 | uint64 uint64 uint64 | bool |  |
| BetweenInclusive_CFixedPoint | CFixedPoint CFixedPoint CFixedPoint | bool |  |
| BetweenInclusive_float | float float float | bool |  |
| BetweenInclusive_int32 | int32 int32 int32 | bool |  |
| BetweenInclusive_int64 | int64 int64 int64 | bool |  |
| BetweenInclusive_uint32 | uint32 uint32 uint32 | bool |  |
| BetweenInclusive_uint64 | uint64 uint64 uint64 | bool |  |
| Between_CFixedPoint | CFixedPoint CFixedPoint CFixedPoint | bool |  |
| Between_float | float float float | bool |  |
| Between_int32 | int32 int32 int32 | bool |  |
| Between_int64 | int64 int64 int64 | bool |  |
| Between_uint32 | uint32 uint32 uint32 | bool |  |
| Between_uint64 | uint64 uint64 uint64 | bool |  |
| BindFoldOutContext |  | void | 为控件添加一个新的 PdxGuiFoldOut 数据上下文。 |
| BoolTo1And2 | bool | int32 |  |
| BoolTo2And1 | bool | int32 |  |
| CalcDynTrendLatestDate | DataDynamicTrend | CString |  |
| CalcDynTrendOldestDate | DataDynamicTrend | CString |  |
| CanEditSettingsAfterHost |  | bool | 多人游戏——是否可以在建立主机后修改设置（取决于所用的多人平台） |
| CanGetAchievements |  | bool |  |
| CanOpenLobby |  | bool |  |
| CanOpenRightClickContextMenu |  | bool |  |
| ChangeAllConstructionSpeed | ProductionMethod | Command |  |
| ChangeAllConstructionSpeedTooltip | ProductionMethod | CString |  |
| ClearDynamicTerrainOverrideForAllProvinces |  | void |  |
| ClearHostError |  | void | 多人游戏——清除主机错误 |
| CloseAllTooltips |  | void |  |
| ColorToVector3f | CVector4f | CVector3f |  |
| ColorToVector3i | CVector4f | CVector3i |  |
| ColorToVector4i | CVector4f | CVector4i |  |
| ConcatIfNeitherEmpty | CString CString | CString |  |
| Concatenate | CString CString | CString |  |
| Concept | GameConcept CString | CString |  |
| CopyBuildVersionInfoToClipboard |  | void |  |
| CopyRNGSeedToClipboard |  | void |  |
| CopyServerID |  | void | 多人游戏——将当前会话的服务器 ID 复制到剪贴板 |
| CurrentAndMaxToProgressbarValueInt32 | int32 int32 | float | 获取当前值相对最大值的进度（0.0-100.0）。数值被限制在 0 到 100 之间。 |
| DataModelFirst | Unknown int32 | Unknown |  |
| DataModelHasItems | Unknown | bool |  |
| DataModelLast | Unknown int32 | Unknown |  |
| DataModelRepeatedItem | int32 | Unknown | 用于模拟空列表项的数据函数，需要一个 int32（项数）作为参数。示例：datamodel = [RepeatedItem( '(int32)4' )] |
| DataModelSkipFirst | Unknown int32 | Unknown |  |
| DataModelSkipLast | Unknown int32 | Unknown |  |
| DataModelSubSpan | Unknown int32 int32 | Unknown |  |
| DebugGetMapMode |  | CString |  |
| DemobilizeSelectedArmies |  | Command |  |
| Divide_CFixedPoint | CFixedPoint CFixedPoint | CFixedPoint |  |
| Divide_CVector2f | CVector2f CVector2f | CVector2f |  |
| Divide_float | float float | float |  |
| Divide_int32 | int32 int32 | int32 |  |
| Divide_int64 | int64 int64 | int64 |  |
| Divide_uint32 | uint32 uint32 | uint32 |  |
| Divide_uint64 | uint64 uint64 | uint64 |  |
| DoubleToFloat | double | float |  |
| EqualTo_CFixedPoint | CFixedPoint CFixedPoint | bool |  |
| EqualTo_CVector2f | CVector2f CVector2f | bool |  |
| EqualTo_float | float float | bool |  |
| EqualTo_int32 | int32 int32 | bool |  |
| EqualTo_int64 | int64 int64 | bool |  |
| EqualTo_string | CString CString | bool |  |
| EqualTo_uint32 | uint32 uint32 | bool |  |
| EqualTo_uint64 | uint64 uint64 | bool |  |
| Execute | Command | void |  |
| ExecuteConsoleCommand | CString | void | 使用给定命令执行单条控制台命令。 |
| ExecuteConsoleCommands | CString | void | 执行以 ';' 分隔的一系列控制台命令。若某条控制台命令执行失败，则停止执行后续命令。 |
| ExecuteConsoleCommandsForced | CString | void | 执行以 ';' 分隔的一系列控制台命令。即使某条控制台命令执行失败，也继续执行后续命令。 |
| FixedPointToFloat | CFixedPoint | float |  |
| FixedPointToInt | CFixedPoint | int32 |  |
| FixedPointToProgressbarValue | CFixedPoint | float | 转换为进度百分比值（乘以 100，不做限制）。 |
| FocusCameraOnCityOutOfState |  | void |  |
| GameHasMultiplePlayers |  | bool |  |
| GameIsMultiplayer |  | bool |  |
| GetAIStrategy | Unknown | AIStrategy | 类别：nonconst |
| GetAcceptanceStatus | AcceptanceStatus | AcceptanceStatus | 类别：nonconst |
| GetAchievementsAvailableString |  | CString | 类别：nonconst |
| GetActivismLabelsDesc |  | CString | 类别：nonconst |
| GetAllPowerBlocs |  | Unknown | 类别：nonconst |
| GetAmendmentType | Unknown | AmendmentType | 类别：nonconst |
| GetApprovalRatingFromValue | Unknown | CString | 类别：nonconst |
| GetArrowIcon_CFixedPoint | CFixedPoint | CString | 类别：nonconst |
| GetArrowIcon_int32 | int32 | CString | 类别：nonconst |
| GetArrowIcon_int64 | int64 | CString | 类别：nonconst |
| GetArticleType | TreatyArticle | ArticleType | 类别：nonconst |
| GetAutosaveName |  | CString | 类别：nonconst |
| GetBasicAdmiralOrdersBreakdown |  | CString | 类别：nonconst |
| GetBasicGeneralOrdersBreakdown |  | CString | 类别：nonconst |
| GetBattalionGroupsList |  | CString | 类别：nonconst |
| GetBattleCondition | BattleCondition | BattleCondition | 类别：nonconst |
| GetBuildVersionDescriptionWithClickToCopy |  | CString | 类别：nonconst |
| GetBuildingGroup | Unknown | BuildingGroup | 类别：nonconst |
| GetBuildingType | BuildingType | BuildingType | 类别：nonconst |
| GetCanGoToFrontend |  | bool | 多人游戏 GUI——能否返回前端主界面？ |
| GetCanGoToFrontendDesc |  | CString | 多人游戏 GUI——无法返回前端主界面时的提示信息 |
| GetCharacterTrait | CharacterTrait | CharacterTrait | 类别：nonconst |
| GetCohesionLevel | Unknown | CohesionLevel | 类别：nonconst |
| GetCohesionLevels |  | Unknown | 类别：nonconst |
| GetCombatUnitGroup | CombatUnitGroup | CombatUnitGroup | 类别：nonconst |
| GetCombatUnitType | CombatUnit | CombatUnitType | 类别：nonconst |
| GetCommanderOrderType | CommanderOrder | CommanderOrderType | 类别：nonconst |
| GetCompanyCharterType | CompanyCharterType | CompanyCharterType | 类别：nonconst |
| GetCompanyCharterTypes |  | Unknown | 类别：nonconst |
| GetConfirmationDesc | Unknown | CString | 类别：nonconst |
| GetConstructionSectorType |  | BuildingType | 类别：nonconst |
| GetCountryDiplomaticAction | DiplomaticAction Country Country | DiplomaticAction | 类别：nonconst |
| GetCountryStrategicObjectiveInStateDesc | Country State | CString | 类别：nonconst |
| GetCulture | Culture | Culture | 类别：nonconst |
| GetCurrentFps |  | float | 类别：nonconst |
| GetCurrentLoadingScreen |  | Unknown | 类别：nonconst |
| GetDataModelSize | Unknown | int32 | 类别：nonconst |
| GetDecreeType | Decree | DecreeType | 类别：nonconst |
| GetDefaultServerName |  | CUTF8String | 类别：nonconst |
| GetDefine | CString CString | Unknown | 类别：nonconst |
| GetDefineAtIndex | CString CString Unknown | Unknown | 类别：nonconst |
| GetDesc | Command | CString | 类别：nonconst |
| GetDescriptiveText | MapInteraction | CString | 类别：nonconst |
| GetDiplomaticActionType | DiplomaticAction | DiplomaticActionType | 类别：nonconst |
| GetDiplomaticPlayType | DiplomaticPlay | DiplomaticPlayType | 类别：nonconst |
| GetDiscordUrl |  | Unknown | 类别：nonconst |
| GetDlcCollection |  | Unknown | 类别：nonconst |
| GetDynTrendMax | DataDynamicTrend | CFixedPoint | 类别：nonconst |
| GetDynTrendMin | DataDynamicTrend | CFixedPoint | 类别：nonconst |
| GetDynTrendPlotPoints | DataDynamicTrend CFixedPoint CFixedPoint | Unknown | 类别：nonconst |
| GetEconomicDependenceOnLabel | CFixedPoint | CString | 类别：nonconst |
| GetEnabledDlcNames |  | Unknown | 类别：nonconst |
| GetEnumIndex | Unknown | CVector2i | 设置——获取枚举设置项的下拉菜单索引。类别：nonconst |
| GetEthnicities |  | Unknown | 肖像系统——获取所有族群 |
| GetEventOptionTextAlignment |  | Unknown | 类别：nonconst |
| GetFlotillaGroupsList |  | CString | 类别：nonconst |
| GetGameVersionDisplay |  | CString | 类别：nonconst |
| GetGameVersionInfo |  | CString | 类别：nonconst |
| GetGameVersionInfoShort |  | CString | 类别：nonconst |
| GetGeographicRegion | GeographicRegion | GeographicRegion | 类别：nonconst |
| GetGlobalList | CString | Unknown | 类别：nonconst |
| GetGlobalMaxLandDefense |  | CFixedPoint | 类别：nonconst |
| GetGlobalMaxLandOffense |  | CFixedPoint | 类别：nonconst |
| GetGlobalMaxNavalDefense |  | CFixedPoint | 类别：nonconst |
| GetGlobalMaxNavalOffense |  | CFixedPoint | 类别：nonconst |
| GetGlobalRandomSeed |  | uint32 | 类别：nonconst |
| GetGlobalRandomSeedString |  | CString | 类别：nonconst |
| GetGlobalVariable | CString | Scope | 类别：nonconst |
| GetGoods | Goods | Goods | 类别：nonconst |
| GetGuiEntityShaderRenderpass |  | Unknown | 类别：nonconst |
| GetGuiPositionFromPercentCoordinates | Unknown Unknown Unknown | Unknown | 类别：nonconst |
| GetHarvestConditionType | HarvestConditionType | HarvestConditionType | 类别：nonconst |
| GetHarvestConditionTypesList |  | CString | 类别：nonconst |
| GetHostError |  | CUTF8String | 多人游戏——获取主机错误 |
| GetIdeology | Ideology | Ideology | 类别：nonconst |
| GetInstitutionType | Institution | InstitutionType | 类别：nonconst |
| GetInteger | Unknown | int32 | 类别：nonconst |
| GetInterestGroupVariant | InterestGroup Country | InterestGroup | 类别：nonconst |
| GetInterestingCountrySettings |  | Unknown | 类别：nonconst |
| GetInvParentScale | Unknown | float | 类别：nonconst |
| GetIsChecked | Unknown | bool | 设置——布尔设置项是否被勾选。类别：nonconst |
| GetJournalEntryGroup | Unknown | JournalEntryGroup | 类别：nonconst |
| GetLabel | TerrainLabel | Label | 类别：nonconst |
| GetLargeFlagFrameSize |  | CVector2i | 类别：nonconst |
| GetLargePowerBlocCoaFrameSize |  | CVector2i | 类别：nonconst |
| GetLatestDate | DataTrend | CString | 类别：nonconst |
| GetLawGroup | LawGroup | LawGroup | 类别：nonconst |
| GetLawType | LawType | LawType | 类别：nonconst |
| GetLegitimacyLevel | LegitimacyLevel | LegitimacyLevel | 类别：nonconst |
| GetLegitimacyLevels |  | Unknown | 类别：nonconst |
| GetLensToolbar |  | LensToolbar | 类别：nonconst |
| GetLibertyDesireLevel | Unknown | LibertyDesireLevel | 类别：nonconst |
| GetLibertyDesireLevels |  | Unknown | 类别：nonconst |
| GetLoadingScreenManager |  | LoadingScreenManager | 类别：nonconst |
| GetLocalizedDefine | Unknown Unknown | CString | 类别：nonconst |
| GetLocalizedDefineAtIndex | Unknown Unknown Unknown | CString | 类别：nonconst |
| GetLoyaltyTypes |  | Unknown | 类别：nonconst |
| GetMPChecksum |  | CString | 类别：nonconst |
| GetManpowerColorVec | Unknown | CVector4f | 类别：nonconst |
| GetMapMode | Unknown | MapMode | 类别：nonconst |
| GetMapModeIcon | Unknown | Unknown | 类别：nonconst |
| GetMapModeIndices |  | Unknown | 类别：nonconst |
| GetMapModeName | Unknown | CString | 类别：nonconst |
| GetMax | DataTrend | CFixedPoint | 类别：nonconst |
| GetMediumFlagFrameSize |  | CVector2i | 类别：nonconst |
| GetMediumPowerBlocCoaFrameSize |  | CVector2i | 类别：nonconst |
| GetMetaPlayer |  | Player | 类别：nonconst |
| GetMin | DataTrend | CFixedPoint | 类别：nonconst |
| GetMobilizationOption | Unknown | MobilizationOption | 类别：nonconst |
| GetMobilizationOptionGroup | Unknown | MobilizationOptionGroup | 类别：nonconst |
| GetMobilizationOptionGroups |  | Unknown | 类别：nonconst |
| GetMoraleColorString | CFixedPoint | CString | 类别：nonconst |
| GetMoraleColorVec | CFixedPoint | CVector4f | 类别：nonconst |
| GetNumCommandersInSelectedFormations |  | int32 | 类别：nonconst |
| GetNumCommandersInSelectedFormationsWithOrderActive | CommanderOrderType | int32 | 类别：nonconst |
| GetNumCommandersInSelectedFormationsWithOrderBlocked | CommanderOrderType | int32 | 类别：nonconst |
| GetNumCommandersInSelectedFormationsWithOrderNext | CommanderOrderType | int32 | 类别：nonconst |
| GetNumCommandersInSelectedFormationsWithOrderPossible | CommanderOrderType | int32 | 类别：nonconst |
| GetNumSelectedArmies |  | int32 | 类别：nonconst |
| GetNumSelectedArmiesWithDemobilizationActive |  | int32 | 类别：nonconst |
| GetNumSelectedArmiesWithDemobilizationBlocked |  | int32 | 类别：nonconst |
| GetNumSelectedArmiesWithDemobilizationPossible |  | int32 | 类别：nonconst |
| GetNumSelectedArmiesWithMobilizationActive |  | int32 | 类别：nonconst |
| GetNumSelectedArmiesWithMobilizationBlocked |  | int32 | 类别：nonconst |
| GetNumSelectedArmiesWithMobilizationPossible |  | int32 | 类别：nonconst |
| GetNumSelectedArmiesWithRaiseConscriptsActive |  | int32 | 类别：nonconst |
| GetNumSelectedArmiesWithRaiseConscriptsBlocked |  | int32 | 类别：nonconst |
| GetNumSelectedArmiesWithRaiseConscriptsPossible |  | int32 | 类别：nonconst |
| GetNumSelectedFleets |  | int32 | 类别：nonconst |
| GetNumSelectedFormations |  | int32 | 类别：nonconst |
| GetNumberAbove_int32 | int32 int32 | int32 | 类别：nonconst |
| GetNumberOfShadersCompiled |  | int32 | 类别：nonconst |
| GetOldestDate | DataTrend | CString | 类别：nonconst |
| GetOpenLobbyTooltip |  | CString | 类别：nonconst |
| GetOrganizationColorVec | CFixedPoint | CVector4f | 类别：nonconst |
| GetPlayer |  | Country | 类别：nonconst |
| GetPlayerResourcesUrl |  | Unknown | 类别：nonconst |
| GetPlayersCount |  | int32 | 多人游戏——当前会话的玩家数量 |
| GetPopNeed | PopNeed | PopNeed | 类别：nonconst |
| GetPopType | PopType | PopType | 类别：nonconst |
| GetPortraitRenderSize | PdxGuiWidget | CVector2f | 类别：nonconst |
| GetPortraitTextureFromDna | Unknown CVector2f | Unknown | 类别：nonconst |
| GetPowerBlocIdentity | PowerBlocIdentity | PowerBlocIdentity | 类别：nonconst |
| GetPowerBlocPrincipleGroup | PrincipleGroup | PowerBlocPrincipleGroup | 类别：nonconst |
| GetPrevTrendValue | DataTrend | CFixedPoint | 类别：nonconst |
| GetPrevTrendValueFor | Unknown Unknown | CFixedPoint | 类别：nonconst |
| GetRandomLogInfo |  | CString | 类别：nonconst |
| GetRankModifier | CountryRank | Modifier | 类别：nonconst |
| GetRawTextTooltipTag | CString | CString | 类别：nonconst |
| GetRawTrendPlotRectWithFixedY | Unknown Unknown Unknown | CPdxFloatRect | 类别：nonconst |
| GetReligion | Religion | Religion | 类别：nonconst |
| GetResolutionWithAspectRatio |  | CVector2f | 类别：nonconst |
| GetRomanNumeral | int32 | CString | 类别：nonconst |
| GetSelectedFormationsList |  | CString | 类别：nonconst |
| GetSelectedMapMode |  | CVector2i | 类别：nonconst |
| GetSelectedMapModeName |  | CString | 类别：nonconst |
| GetSmallFlagFrameSize |  | CVector2i | 类别：nonconst |
| GetSmallPowerBlocCoaFrameSize |  | CVector2i | 类别：nonconst |
| GetSmartBrushInterpolationNames |  | Unknown | 地图编辑器——智能材质绘制——插值名称 |
| GetSmartBrushPatternNames |  | Unknown | 地图编辑器——智能材质绘制——图案名称 |
| GetStarvationTypes |  | Unknown | 类别：nonconst |
| GetStateRegion | StateRegion | StateRegion | 类别：nonconst |
| GetStaticModifier | Modifier | Modifier | 类别：nonconst |
| GetStrategicRegion | StrategicRegion | StrategicRegion | 类别：nonconst |
| GetStringSettingText | Unknown | CString | 设置——获取字符串设置的文本 类别：nonconst |
| GetString_CPdxFloatRect | CPdxFloatRect | CString | 类别：nonconst |
| GetString_CPdxIntRect | CPdxIntRect | CString | 类别：nonconst |
| GetString_CVector2f | CVector2f | CString | 类别：nonconst |
| GetString_CVector2i | CVector2i | CString | 类别：nonconst |
| GetString_CVector3f | CVector3f | CString | 类别：nonconst |
| GetString_CVector3i | CVector3i | CString | 类别：nonconst |
| GetString_CVector4f | CVector4f | CString | 类别：nonconst |
| GetString_CVector4i | CVector4i | CString | 类别：nonconst |
| GetSubjectType | SubjectType | SubjectType | 类别：nonconst |
| GetSubjectTypes |  | Unknown | 类别：nonconst |
| GetSubjectTypesList |  | CString | 类别：nonconst |
| GetSupplyNetworkColorstring | CFixedPoint | CString | 类别：nonconst |
| GetSupportLabelsDesc |  | CString | 类别：nonconst |
| GetTechnology | Technology | Technology | 类别：nonconst |
| GetTrendIcon | DataTrend | CString | 类别：nonconst |
| GetTrendIconFor | Unknown Unknown | CString | 类别：nonconst |
| GetTrendPlotPoints | Unknown | Unknown | 类别：nonconst |
| GetTrendPlotPointsAbsolute | Unknown | Unknown | 类别：nonconst |
| GetTrendPlotPointsNormalized | DataTrend CFixedPoint CFixedPoint | Unknown | 类别：nonconst |
| GetTrendValue | DataTrend | CFixedPoint | 类别：nonconst |
| GetTrendValueFor | Unknown Unknown | CFixedPoint | 类别：nonconst |
| GetUnitStrengthHeader | int64 int64 CString | CString | 类别：nonconst |
| GetUnitStrengthHeaderNoIcon | Unknown Unknown | CString | 类别：nonconst |
| GetVarTimeRemaining | Unknown Unknown | int32 | 类别：nonconst |
| GetVeryLargePowerBlocCoaFrameSize |  | CVector2i | 类别：nonconst |
| GetVerySmallPowerBlocCoaFrameSize |  | CVector2i | 类别：nonconst |
| GetWarGoalType | Unknown | WarGoalType | 类别：nonconst |
| GetWikiUrl |  | Unknown | 类别：nonconst |
| GetYoutubeChannelUrl |  | Unknown | 类别：nonconst |
| GfxGetSkins |  | Unknown |  |
| GfxSetActiveSkin | CString | void |  |
| GfxSkinIsActive | CString | bool |  |
| GoToFrontend |  | void | 多人游戏 GUI——返回前端界面 |
| GreaterThanOrEqualTo_CFixedPoint | CFixedPoint CFixedPoint | bool |  |
| GreaterThanOrEqualTo_float | float float | bool |  |
| GreaterThanOrEqualTo_int32 | int32 int32 | bool |  |
| GreaterThanOrEqualTo_int64 | int64 int64 | bool |  |
| GreaterThanOrEqualTo_uint32 | uint32 uint32 | bool |  |
| GreaterThanOrEqualTo_uint64 | uint64 uint64 | bool |  |
| GreaterThan_CFixedPoint | CFixedPoint CFixedPoint | bool |  |
| GreaterThan_float | float float | bool |  |
| GreaterThan_int32 | int32 int32 | bool |  |
| GreaterThan_int64 | int64 int64 | bool |  |
| GreaterThan_uint32 | uint32 uint32 | bool |  |
| GreaterThan_uint64 | uint64 uint64 | bool |  |
| HasAnyAvailableNewThemes |  | bool |  |
| HasAnySelections | Unknown | bool |  |
| HasAnyThemeIssues |  | bool |  |
| HasCitiesOutOfState |  | bool |  |
| HasDlcFeature | DlcFeature | bool |  |
| HasGameLoadedToMainMenu |  | bool |  |
| HasGameStartedForTheFirstTime |  | bool |  |
| HasGameState |  | bool |  |
| HasHostError |  | bool |  |
| HasValidSelectedFormationsToCancelStrategicObjective | Unknown | bool |  |
| HasValidSelectedFormationsToSetStrategicObjective | Unknown | bool |  |
| InDebugMode |  | bool |  |
| InReleaseMode |  | bool |  |
| IntToFixedPoint | int32 | CFixedPoint |  |
| IntToFloat | int32 | float |  |
| IntToFrameIndex | int32 | int32 | 将参数 1 加 1。 |
| IntToUnsigned | int32 | uint32 |  |
| IsCameraRestrictionsEnabled |  | bool | 地图编辑器——摄像机限制是否开启 |
| IsCurrentProductionMethod | ProductionMethod | bool |  |
| IsDataModelEmpty | Unknown | bool |  |
| IsDrawCityDebugGrid |  | bool |  |
| IsDrawCityDebugSpheres |  | bool |  |
| IsDynTrendEmpty | DataDynamicTrend | bool |  |
| IsDynamicTerrainAutoUpdate |  | bool |  |
| IsDynamicsEnabled |  | bool |  |
| IsEmpty | DataTrend | bool |  |
| IsEven_int32 | int32 | bool |  |
| IsEven_int64 | int64 | bool |  |
| IsEven_uint32 | uint32 | bool |  |
| IsEven_uint64 | uint64 | bool |  |
| IsGameChecksumOk |  | bool |  |
| IsGameOverScreenShown |  | bool |  |
| IsGamePaused |  | bool |  |
| IsHost |  | bool |  |
| IsInGame |  | bool |  |
| IsIronmanEnabled |  | bool |  |
| IsLoadedFromSave |  | bool |  |
| IsMapModeIndexSelected | Unknown | bool |  |
| IsMapModeLocked |  | bool |  |
| IsMapModeSelected | MapMode | bool |  |
| IsObserver |  | bool |  |
| IsOdd_int32 | int32 | bool |  |
| IsOdd_int64 | int64 | bool |  |
| IsOdd_uint32 | uint32 | bool |  |
| IsOdd_uint64 | uint64 | bool |  |
| IsPauseMenuShown |  | bool |  |
| IsPotential | Command | bool |  |
| IsPreparationLobby |  | bool |  |
| IsRedundant | Command | bool |  |
| IsSaving |  | bool |  |
| IsTerrainManipulatorProvincesPreview |  | bool |  |
| IsTutorialLessonActive | Unknown | bool |  |
| IsValid | Command | bool |  |
| IsZoomLevelFar |  | bool |  |
| IsZoomLevelMax |  | bool |  |
| IsZoomLevelMid |  | bool |  |
| IsZoomLevelNear |  | bool |  |
| JoinText | CString CString CString | CString |  |
| JominiAccessPlayerJoinRequests |  | Unknown |  |
| JominiAreAchievementsAvailable |  | bool |  |
| JominiGetAchievementsNotAvailableString |  | CString | Jomini 成就——获取成就不可用的原因文本 |
| JominiGetMultiplayerAccessibleString |  | CString |  |
| JominiHasPlayerJoinRequests |  | bool |  |
| JominiIsHostOrLocal |  | bool |  |
| JominiIsMultiplayerAccessible |  | bool |  |
| JominiMultiplayerIsCrossplayEnabled |  | bool |  |
| JominiMultiplayerIsCrossplayFilterAvailable |  | bool |  |
| JominiPlayer |  | Playable |  |
| LessThanOrEqualTo_CFixedPoint | CFixedPoint CFixedPoint | bool |  |
| LessThanOrEqualTo_float | float float | bool |  |
| LessThanOrEqualTo_int32 | int32 int32 | bool |  |
| LessThanOrEqualTo_int64 | int64 int64 | bool |  |
| LessThanOrEqualTo_uint32 | uint32 uint32 | bool |  |
| LessThanOrEqualTo_uint64 | uint64 uint64 | bool |  |
| LessThan_CFixedPoint | CFixedPoint CFixedPoint | bool |  |
| LessThan_float | float float | bool |  |
| LessThan_int32 | int32 int32 | bool |  |
| LessThan_int64 | int64 int64 | bool |  |
| LessThan_uint32 | uint32 uint32 | bool |  |
| LessThan_uint64 | uint64 uint64 | bool |  |
| Localize | CString | CString |  |
| LocalizeInputAction | Unknown | CString |  |
| MakeScopeBool | bool | Scope |  |
| MakeScopeFlag | Unknown | Scope |  |
| MakeScopeValue | CFixedPoint | Scope |  |
| Max_CFixedPoint | CFixedPoint CFixedPoint | CFixedPoint |  |
| Max_float | float float | float |  |
| Max_int32 | int32 int32 | int32 |  |
| Max_int64 | int64 int64 | int64 |  |
| Max_uint32 | uint32 uint32 | uint32 |  |
| Max_uint64 | uint64 uint64 | uint64 |  |
| MergeSelectedFormations |  | Command |  |
| Min_CFixedPoint | CFixedPoint CFixedPoint | CFixedPoint |  |
| Min_float | float float | float |  |
| Min_int32 | int32 int32 | int32 |  |
| Min_int64 | int64 int64 | int64 |  |
| Min_uint32 | uint32 uint32 | uint32 |  |
| Min_uint64 | uint64 uint64 | uint64 |  |
| MobilizeSelectedArmies |  | Command |  |
| Modulo_int32 | int32 int32 | int32 |  |
| Modulo_int64 | int64 int64 | int64 |  |
| Modulo_uint32 | uint32 uint32 | uint32 |  |
| Modulo_uint64 | uint64 uint64 | uint64 |  |
| Multiply_CFixedPoint | CFixedPoint CFixedPoint | CFixedPoint |  |
| Multiply_CVector2f | CVector2f CVector2f | CVector2f |  |
| Multiply_float | float float | float |  |
| Multiply_int32 | int32 int32 | int32 |  |
| Multiply_int64 | int64 int64 | int64 |  |
| Multiply_uint32 | uint32 uint32 | uint32 |  |
| Multiply_uint64 | uint64 uint64 | uint64 |  |
| NOP |  | void | 无操作（空置的回调函数） |
| Nbsp |  | CString |  |
| Negate_CFixedPoint | CFixedPoint | CFixedPoint |  |
| Negate_float | float | float |  |
| Negate_int32 | int32 | int32 |  |
| Negate_int64 | int64 | int64 |  |
| Not | bool | bool |  |
| NotEqualTo_CFixedPoint | CFixedPoint CFixedPoint | bool |  |
| NotEqualTo_CVector2f | CVector2f CVector2f | bool |  |
| NotEqualTo_float | float float | bool |  |
| NotEqualTo_int32 | int32 int32 | bool |  |
| NotEqualTo_int64 | int64 int64 | bool |  |
| NotEqualTo_uint32 | uint32 uint32 | bool |  |
| NotEqualTo_uint64 | uint64 uint64 | bool |  |
| ObjectsEqual | Unknown Unknown | bool |  |
| ObserveCountryCommand | Unknown | Command |  |
| OnCreateAccount |  | void | 启动账号创建流程 |
| OnToggleLoginWindow |  | void |  |
| OpenAchievements |  | void |  |
| OpenDiscordUrl |  | void |  |
| OpenGameRules |  | void |  |
| OpenPlayerResourcesUrl |  | void |  |
| OpenWikiUrl |  | void |  |
| OpenYoutubeChannelUrl |  | void |  |
| Or | bool bool | bool |  |
| Or3 | bool bool bool | bool |  |
| Or4 | bool bool bool bool | bool |  |
| Or5 | bool bool bool bool bool | bool |  |
| Or6 | bool bool bool bool bool bool | bool |  |
| Or7 | bool bool bool bool bool bool bool | bool |  |
| Or8 | bool bool bool bool bool bool bool bool | bool |  |
| OrEvalAll | Unknown Unknown | bool |  |
| PauseAllConstruction |  | Command |  |
| PauseAllConstructionTooltip |  | CString |  |
| PdxClearEditBoxText | Unknown | void |  |
| PdxGetProfilerNames |  | Unknown |  |
| PdxGetWidgetScreenSize | PdxGuiWidget | CVector2f |  |
| PdxGuiDestroyWidget | PdxGuiWidget | void | 销毁控件 |
| PdxGuiEditboxGetText | Unknown | CUTF8String |  |
| PdxGuiInterruptAllAnimations | CString | void |  |
| PdxGuiInterruptThenTriggerAllAnimations | CString CString | void |  |
| PdxGuiTriggerAllAnimations | CString | void |  |
| PdxProfilerFilterNext |  | void |  |
| PdxProfilerFilterPrev |  | void |  |
| PdxProfilerFilterTimers |  | void |  |
| PdxProfilerGetCurrentFrame |  | int32 |  |
| PdxProfilerGetFrameTimeMs |  | float |  |
| PdxProfilerGetNsPerTick |  | float |  |
| PdxProfilerGuiGraphLinesEnabled |  | bool |  |
| PdxProfilerGuiToggleGraphLines |  | void |  |
| PdxProfilerGuiToggleStats |  | void |  |
| PdxProfilerGuiTrackCurrentFrame |  | void |  |
| PdxProfilerGuiWriteFrameCSV |  | void |  |
| PdxProfilerIsRecording |  | bool |  |
| PdxProfilerSelectThread |  | void |  |
| PdxProfilerSetFrame |  | void |  |
| PdxProfilerToggleRecording |  | void |  |
| PlayerIsHost |  | bool | 多人游戏 GUI——当前玩家是否为主机？ |
| PopCursorOverride |  | void |  |
| PushCursorOverride | Unknown | void |  |
| RaiseConscriptsInSelectedArmies |  | Command |  |
| ReleaseMode |  | bool |  |
| RemoveTempMapMode |  | void |  |
| ResetCursorOverrides |  | void |  |
| ResumeAllConstruction |  | Command |  |
| ResumeAllConstructionTooltip |  | CString |  |
| ReturnToMenu |  | void |  |
| ScaleToFitElementInside | int32 int32 | float |  |
| ScaleToFitElementOutside | int32 int32 | float |  |
| ScrollPanelToNamedWidget | CString CString | void |  |
| ScrollPanelToTop | Unknown | void |  |
| SelectEnumWithString | CString Unknown | void | 设置——根据字符串输入选择枚举 |
| SelectLocalization | bool CString CString | CString |  |
| SelectSound | bool Sound Sound | Unknown |  |
| Select_CFixedPoint | bool CFixedPoint CFixedPoint | CFixedPoint |  |
| Select_CString | bool CString CString | CString |  |
| Select_CVector2f | bool CVector2f CVector2f | CVector2f |  |
| Select_CVector2i | bool CVector2i CVector2i | CVector2i |  |
| Select_CVector3f | bool CVector3f CVector3f | CVector3f |  |
| Select_CVector3i | bool CVector3i CVector3i | CVector3i |  |
| Select_CVector4f | bool CVector4f CVector4f | CVector4f |  |
| Select_CVector4i | bool CVector4i CVector4i | CVector4i |  |
| Select_float | bool float float | float |  |
| Select_int16 | bool int16 int16 | int16 |  |
| Select_int32 | bool int32 int32 | int32 |  |
| Select_int64 | bool int64 int64 | int64 |  |
| Select_int8 | bool int8 int8 | int8 |  |
| Select_uint16 | bool uint16 uint16 | uint16 |  |
| Select_uint32 | bool uint32 uint32 | uint32 |  |
| Select_uint64 | bool uint64 uint64 | uint64 |  |
| Select_uint8 | bool uint8 uint8 | uint8 |  |
| SetCameraRestrictionsEnabled | bool | void | 地图编辑器——设置摄像机限制开关 |
| SetCanOpenRightClickContextMenu | bool | void |  |
| SetCharacterOrderForSelectedFormations | CommanderOrderType | Command |  |
| SetDrawCityDebugGrid | bool | void |  |
| SetDrawCityDebugSpheres | bool | void |  |
| SetDynamicTerrainAutoUpdate | bool | void |  |
| SetDynamicsEnabled | bool | void |  |
| SetInteraction | Unknown | void |  |
| SetIronmanEnabledStatus | bool | void |  |
| SetLockedMapMode |  | void |  |
| SetRandomPlayableObserverCharacter |  | void |  |
| SetStrategicObjective | Unknown Unknown | Command |  |
| SetStrategicObjectiveForSelectedFormations | Unknown | Command |  |
| SetTempMapModeByKey | MapMode | void |  |
| SetTerrainManipulatorProvincesPreview | bool | void |  |
| ShouldAskConfirmation | Command | bool |  |
| ShouldShowAnimationInfo |  | bool |  |
| ShouldShowSegmentedControlForSetting | Unknown | bool | 设置——是否显示分段控件？ |
| StatusCanLogin |  | bool |  |
| StatusGetLoginStatus |  | CUTF8String |  |
| StatusGetUserEmailMasked |  | CUTF8String |  |
| StatusGetUserName |  | CUTF8String |  |
| StatusIsAccountConnected |  | bool |  |
| StatusIsLoggedIn |  | bool |  |
| StatusIsLoggingIn |  | bool |  |
| StatusIsOffline |  | bool |  |
| StatusIsSupportConnectedAccount |  | bool |  |
| StatusIsUserNameEmpty |  | bool |  |
| StringIsEmpty | CString | bool |  |
| Subtract_CFixedPoint | CFixedPoint CFixedPoint | CFixedPoint |  |
| Subtract_CVector2f | CVector2f CVector2f | CVector2f |  |
| Subtract_float | float float | float |  |
| Subtract_int32 | int32 int32 | int32 |  |
| Subtract_int64 | int64 int64 | int64 |  |
| Subtract_uint32 | uint32 uint32 | uint32 |  |
| Subtract_uint64 | uint64 uint64 | uint64 |  |
| TextureListFormatSize | uint64 | CString |  |
| TextureListFormatkB | uint64 | CString |  |
| ToString_int16 | int16 | CString |  |
| ToString_int32 | int32 | CString |  |
| ToString_int64 | int64 | CString |  |
| ToString_int8 | int8 | CString |  |
| ToString_uint16 | uint16 | CString |  |
| ToString_uint32 | uint32 | CString |  |
| ToString_uint64 | uint64 | CString |  |
| ToString_uint8 | uint8 | CString |  |
| ToggleEncyclopedia |  | void |  |
| ToggleInteraction | Unknown | void |  |
| ToggleMainMenu |  | void |  |
| ToggleMessageSettings |  | void |  |
| ToggleMessageSettingsForSingleItem | CString | void |  |
| ToggleMusicPlayer |  | void |  |
| ToggleObserveCountry | Country | void |  |
| ToggleThemeSettings |  | void |  |
| TransparentIfFalse | bool | float |  |
| TransparentIfTrue | bool | float |  |
| TransparentIfZero | CFixedPoint | float |  |
| TransparentIfZero_int32 | int32 | float |  |
| TransparentIfZero_int64 | int64 | float |  |
| Unfocus | Unknown | void | 取消控件的焦点 |
| UnlockMapMode |  | void |  |
| UpdateDynamicTerrainInAllProvinces |  | void |  |
| UsesTimerLocking |  | bool |  |
| Vector3fToColor | CVector3f | CVector4f |  |
| Vector3iToColor | CVector3i | CVector4f |  |
| Vector4iToColor | CVector4i | CVector4f |  |
| Function | Arguments | Output | Description |
|---|---|---|---|
| AccessActiveDiplomaticPactTypes |  | Unknown | 类别：const |
| AccessActiveDiplomaticPacts | ContextualDiplomaticActionType | Unknown | 类别：const |
| AccessActiveDiplomaticPlays |  | Unknown | 类别：const |
| AccessActiveEconomyLaws |  | Unknown | 类别：const |
| AccessActiveHumanRightsLaws |  | Unknown | 类别：const |
| AccessActiveInterestGroups |  | Unknown | 类别：const |
| AccessActiveJournalEntries |  | Unknown | 类别：const |
| AccessActiveLawFromGroup | LawGroup | Law | 类别：const |
| AccessActiveNonPlayerObjectiveJournalEntries |  | Unknown | 类别：const |
| AccessActiveOtherLaws |  | Unknown | 类别：const |
| AccessActiveParties |  | Unknown | 类别：const |
| AccessActivePinnedNonPlayerObjectiveJournalEntries |  | Unknown | 类别：const |
| AccessActivePinnedPlayerObjectiveJournalEntries |  | Unknown | 类别：const |
| AccessActivePlayerObjectiveJournalEntries |  | Unknown | 类别：const |
| AccessActivePowerStructureLaws |  | Unknown | 类别：const |
| AccessAdmirals |  | Unknown | 类别：const |
| AccessAdmiralsOffer |  | Unknown | 类别：const |
| AccessAllInterestGroups |  | Unknown | 类别：const |
| AccessCapital |  | State | 类别：const |
| AccessCivilWars |  | Unknown | 类别：const |
| AccessConstructionQueue |  | Unknown | 类别：const |
| AccessCurrentlyResearchedTechnology |  | Technology | 类别：const |
| AccessDefinition |  | CountryDefinition | 类别：const |
| AccessFirstMarket |  | Market | 类别：const |
| AccessFormableCountries |  | Unknown | 类别：const |
| AccessGenerals |  | Unknown | 类别：const |
| AccessGeneralsOffer |  | Unknown | 类别：const |
| AccessGovernment |  | GovernmentType | 类别：const |
| AccessGovernmentConstructionQueue |  | Unknown | 类别：const |
| AccessHeaviestJournalEntry |  | JournalEntry | 类别：const |
| AccessHeir |  | Character | 类别：const |
| AccessInactiveJournalEntries |  | Unknown | 类别：const |
| AccessInstitutions |  | Unknown | 类别：const |
| AccessInterestGroupsInGovernment |  | Unknown | 类别：const |
| AccessInterestGroupsInOpposition |  | Unknown | 类别：const |
| AccessInterests |  | Unknown | 类别：const |
| AccessLandHQs |  | Unknown | 类别：const |
| AccessLastElectionParties |  | Unknown | 类别：const |
| AccessLawBeingEnacted |  | Law | 类别：const |
| AccessLawsWithGovernmentOrMovementSupport |  | Unknown | 类别：const |
| AccessLawsWithoutGovernmentOrMovementSupport |  | Unknown | 类别：const |
| AccessMarginalInterestGroups |  | Unknown | 类别：const |
| AccessModifier |  | Modifier | 类别：const |
| AccessNavalHQs |  | Unknown | 类别：const |
| AccessNonRevolutionaryPoliticalMovements |  | Unknown | 类别：const |
| AccessNumResearchableTechnologies |  | int32 | 类别：const |
| AccessOverlord |  | Country | 类别：const |
| AccessPagedGovernmentConstructionQueue | int32 Unknown | Unknown | 类别：const |
| AccessPagedPrivateConstructionQueue | int32 Unknown | Unknown | 类别：const |
| AccessPoliticalMovements |  | Unknown | 类别：const |
| AccessPopCultures |  | Unknown | 类别：const |
| AccessPopCulturesSortedByPolStr |  | Unknown | 类别：const |
| AccessPopCulturesSortedByPopulation |  | Unknown | 类别：const |
| AccessPopReligionsSortedByPolStr |  | Unknown | 类别：const |
| AccessPopReligionsSortedByPopulation |  | Unknown | 类别：const |
| AccessPopTypes |  | Unknown | 类别：const |
| AccessPopTypesSortedOnPolStr |  | Unknown | 类别：const |
| AccessPopTypesSortedOnPopulation |  | Unknown | 类别：const |
| AccessPowerBloc |  | PowerBloc | 类别：const |
| AccessPrivateConstructionQueue |  | Unknown | 类别：const |
| AccessReleasableCountries |  | Unknown | 类别：const |
| AccessResearchableTechnologiesMilitary |  | Unknown | 类别：const |
| AccessResearchableTechnologiesOther |  | Unknown | 类别：const |
| AccessResearchableTechnologiesProduction |  | Unknown | 类别：const |
| AccessResearchableTechnologiesSociety |  | Unknown | 类别：const |
| AccessRuler |  | Character | 类别：const |
| AccessSecessions |  | Unknown | 类别：const |
| AccessSelf |  | Country | 类别：const |
| AccessShippingLanes |  | Unknown | 类别：const |
| AccessShippingOriginStates | Province | Unknown | 类别：const |
| AccessShownCurrentlyConstructingGovernmentQueue |  | Unknown | 类别：const |
| AccessShownCurrentlyConstructingPrivateQueue |  | Unknown | 类别：const |
| AccessShownCurrentlyConstructingQueue |  | Unknown | 类别：const |
| AccessStateReligion |  | Religion | 类别：const |
| AccessStates |  | Unknown | 类别：const |
| AccessStrategies |  | Unknown | 类别：const |
| AccessTopOverlord |  | Country | 类别：const |
| AccessTruces |  | Unknown | 类别：const |
| AccessVioSovInterestedCountries | Country | Unknown | 类别：const |
| AccessVioSovWars | Country | Unknown | 类别：const |
| AccessVisibleJournalEntries |  | Unknown | 类别：const |
| AccessWars |  | Unknown | 类别：const |
| CalcBaseConstructionSpeed |  | CFixedPoint |  |
| CalcConscriptableBattalions |  | int32 |  |
| CalcCulturalTurmoil | Culture | CFixedPoint |  |
| CalcLibertyDesireLevel |  | LibertyDesireLevel |  |
| CalcMaxNumDeclaredInterests |  | int32 |  |
| CalcNumStatesInTurmoil |  | int32 |  |
| CalcRelativeUsedGovernmentConstruction |  | CFixedPoint |  |
| CalcRelativeUsedPrivateConstruction |  | CFixedPoint |  |
| CalcTurmoil |  | CFixedPoint |  |
| CalcUnusedConstruction |  | CFixedPoint |  |
| CalcUsedConstruction |  | CFixedPoint |  |
| CalcUsedGovernmentConstruction |  | CFixedPoint |  |
| CalcUsedPrivateConstruction |  | CFixedPoint |  |
| CanBuildingTypeBeMonopolized | BuildingType | bool |  |
| CanSignTreatyWith | Country | bool |  |
| CanTradeGoods | Unknown | bool |  |
| CreateCompany | CompanyType | Command |  |
| DeclareBankruptcy |  | Command |  |
| DeclareInterest | StrategicRegion | Command |  |
| DemobilizeAllArmies |  | Command |  |
| EstimatedConstructionQueueDuration |  | int32 |  |
| EstimatedGovernmentConstructionQueueDuration |  | int32 |  |
| EstimatedPrivateConstructionQueueDuration |  | int32 |  |
| Exists |  | bool |  |
| GetAIStrategiesDesc |  | CString | 类别：nonconst |
| GetActiveConstructionProjectsDesc |  | CString | 类别：nonconst |
| GetActiveLawFrom | Unknown | Law | 类别：nonconst |
| GetActiveLawFromGroup | CString | Law | 类别：nonconst |
| GetActivePeaceDealDesc |  | CString | 类别：nonconst |
| GetAdditionalExpensesTrend |  | DataTrend | 类别：nonconst |
| GetAdditionalIncomeTrend |  | DataTrend | 类别：nonconst |
| GetAdditionalSOLFactorsDescAll |  | CString | 类别：nonconst |
| GetAdditionalSOLFactorsDescMiddle |  | CString | 类别：nonconst |
| GetAdditionalSOLFactorsDescPoor |  | CString | 类别：nonconst |
| GetAdditionalSOLFactorsDescRich |  | CString | 类别：nonconst |
| GetAdditionalSOLFactorsDescWithCulture | Culture | CString | 类别：nonconst |
| GetAdditionalSOLFactorsDescWithCultureMiddle | Culture | CString | 类别：nonconst |
| GetAdditionalSOLFactorsDescWithCulturePoor | Culture | CString | 类别：nonconst |
| GetAdditionalSOLFactorsDescWithCultureRich | Culture | CString | 类别：nonconst |
| GetAdjective |  | CString | 类别：nonconst |
| GetAdjectiveNoFlag |  | CString | 类别：nonconst |
| GetAdjectiveNoFormatting |  | CString | 类别：nonconst |
| GetAllAcceptanceStatusSegments |  | Unknown | 类别：nonconst |
| GetAllGeneralDiploActions |  | Unknown | 类别：nonconst |
| GetAllOverlordDiploActions |  | Unknown | 类别：nonconst |
| GetAllPowerBlocLeaderDiploActions |  | Unknown | 类别：nonconst |
| GetAllPowerBlocMemberDiploActions |  | Unknown | 类别：nonconst |
| GetAllSubjectDiploActions |  | Unknown | 类别：nonconst |
| GetAllianceLikeTreatiesBrokenDesc | Country | CString | 类别：nonconst |
| GetAllianceLikeTreatiesBrokenFromPlayDesc | DiplomaticPlay | CString | 类别：nonconst |
| GetAllianceLikeTreatiesBrokenOnWarDesc | Country | CString | 类别：nonconst |
| GetAllianceLikeTreatiesList | Unknown | CString | 类别：nonconst |
| GetAltAdjective | CString | CString | 类别：nonconst |
| GetAltAdjectiveNoFlag | CString | CString | 类别：nonconst |
| GetAltAdjectiveNoFormatting | CString | CString | 类别：nonconst |
| GetAltName | CString | CString | 类别：nonconst |
| GetAltNameNoFlag | CString | CString | 类别：nonconst |
| GetAltNameNoFormatting | CString | CString | 类别：nonconst |
| GetArableLand |  | int32 | 类别：nonconst |
| GetArableLandDesc |  | CString | 类别：nonconst |
| GetArmiesBreakdown |  | CString | 类别：nonconst |
| GetArmyPowerProjection |  | CFixedPoint | 类别：nonconst |
| GetArmyPowerProjectionDesc |  | CString | 类别：nonconst |
| GetArmyReadinessStatusDesc |  | CString | 类别：nonconst |
| GetAttainableCompanies |  | Unknown | 类别：nonconst |
| GetAttitudeColor | Unknown | CVector4f | 类别：nonconst |
| GetAttitudeTowards | Country | AIAttitude | 类别：nonconst |
| GetAvailableCompanies |  | Unknown | 类别：nonconst |
| GetAvailableGeneralDiploActions |  | Unknown | 类别：nonconst |
| GetAvailableOverlordDiploActions |  | Unknown | 类别：nonconst |
| GetAvailablePowerBlocLeaderDiploActions |  | Unknown | 类别：nonconst |
| GetAvailablePowerBlocMemberDiploActions |  | Unknown | 类别：nonconst |
| GetAvailableSubjectDiploActions |  | Unknown | 类别：nonconst |
| GetAverageExpectedStandardOfLivingWithCultureMiddle | Unknown | CFixedPoint | 类别：nonconst |
| GetAverageExpectedStandardOfLivingWithCulturePoor | Unknown | CFixedPoint | 类别：nonconst |
| GetAverageExpectedStandardOfLivingWithCultureRich | Unknown | CFixedPoint | 类别：nonconst |
| GetAverageSoLByPoliticalStrength |  | CFixedPoint | 类别：nonconst |
| GetAverageSoLByPopulation |  | CFixedPoint | 类别：nonconst |
| GetAverageSoLByPopulationTrend |  | DataTrend | 类别：nonconst |
| GetAverageSoLByPopulationWithCulture | Unknown | CFixedPoint | 类别：nonconst |
| GetAverageSoLLowerTrend |  | DataTrend | 类别：nonconst |
| GetAverageSoLMiddleTrend |  | DataTrend | 类别：nonconst |
| GetAverageSoLUpperTrend |  | DataTrend | 类别：nonconst |
| GetAverageStandardOfLivingMiddle |  | CFixedPoint | 类别：nonconst |
| GetAverageStandardOfLivingPoor |  | CFixedPoint | 类别：nonconst |
| GetAverageStandardOfLivingRich |  | CFixedPoint | 类别：nonconst |
| GetAverageStandardOfLivingWithCultureMiddle | Unknown | CFixedPoint | 类别：nonconst |
| GetAverageStandardOfLivingWithCulturePoor | Unknown | CFixedPoint | 类别：nonconst |
| GetAverageStandardOfLivingWithCultureRich | Unknown | CFixedPoint | 类别：nonconst |
| GetAverageStateTaxCollectionMult |  | CFixedPoint | 类别：nonconst |
| GetAverageStateTaxCollectionMultBreakdown |  | CString | 类别：nonconst |
| GetAverageTaxWaste |  | CFixedPoint | 类别：nonconst |
| GetAverageTaxWasteBreakdown |  | CString | 类别：nonconst |
| GetBalanceTrend |  | DataDynamicTrend | 类别：nonconst |
| GetBaseConstructionSpeedDesc |  | CString | 类别：nonconst |
| GetBaseWeeklyTechnologySpread |  | CFixedPoint | 类别：nonconst |
| GetBaseWeeklyTechnologySpreadForTech | Unknown | CFixedPoint | 类别：nonconst |
| GetBattalions |  | int32 | 类别：nonconst |
| GetBattalionsDesc |  | CString | 类别：nonconst |
| GetBattalionsMobilizing |  | int32 | 类别：nonconst |
| GetBattalionsRanking |  | CString | 类别：nonconst |
| GetBolsterDesc |  | CString | 类别：nonconst |
| GetBolsteringCostDesc |  | CString | 类别：nonconst |
| GetCanBuildingTypeBeMonopolizedDesc | BuildingType | CString | 类别：nonconst |
| GetCanSignTreatyWithDesc | Country | CString | 类别：nonconst |
| GetCapital |  | State | 类别：nonconst |
| GetColonialGrowthDetails |  | CString | 类别：nonconst |
| GetCompanies |  | Unknown | 类别：nonconst |
| GetCompanyConstructionEfficiencyBonusFormatted |  | CString | 类别：nonconst |
| GetCompanyThroughputBonusFormatted |  | CString | 类别：nonconst |
| GetConscriptedBattalions |  | int32 | 类别：nonconst |
| GetConscriptionRatio |  | CFixedPoint | 类别：nonconst |
| GetConstructionGoodsExpenseTrend |  | DataTrend | 类别：nonconst |
| GetConstructionGoodsExpenses |  | CFixedPoint | 类别：nonconst |
| GetConstructionGoodsExpensesByGoodsDesc | Unknown | CString | 类别：nonconst |
| GetConstructionGoodsExpensesDesc |  | CString | 类别：nonconst |
| GetConstructionQueueDesc |  | CString | 类别：nonconst |
| GetConstructionsInCountry | Country | Unknown | 类别：nonconst |
| GetConsumptionTaxIncome |  | CFixedPoint | 类别：nonconst |
| GetConsumptionTaxTrend |  | DataTrend | 类别：nonconst |
| GetConsumptionTaxesDesc |  | CString | 类别：nonconst |
| GetConvoyEffectDesc |  | CString | 类别：nonconst |
| GetCountriesWithTreaties |  | Unknown | 类别：nonconst |
| GetCountryScorePosition |  | int32 | 类别：nonconst |
| GetCountryScorePositionDesc |  | CString | 类别：nonconst |
| GetCreditRatio |  | CFixedPoint | 类别：nonconst |
| GetCreditTooltip |  | CString | 类别：nonconst |
| GetCulturePolStrAsPercentage | Culture | CFixedPoint | 类别：nonconst |
| GetCulturePopulation | Culture | int64 | 类别：nonconst |
| GetCurrentLeverage | Unknown | CFixedPoint | 类别：nonconst |
| GetCurrentLeverageShare | PowerBloc | CFixedPoint | 类别：nonconst |
| GetCurrentPowerStruggleMonth |  | int32 | 类别：nonconst |
| GetCurrentlyResearchedTechnology |  | Technology | 类别：nonconst |
| GetCurrentlySpreadingTechsDesc |  | CString | 类别：nonconst |
| GetCustom | CustomLocalization | CString | 类别：nonconst |
| GetDailyRelationsProgress | Country | CFixedPoint | 类别：nonconst |
| GetDaysUntilElection |  | int32 | 类别：nonconst |
| GetDaysUntilRankLoss |  | int32 | 类别：nonconst |
| GetDecisions |  | Unknown | 类别：nonconst |
| GetDeclareBankruptcyDesc |  | CString | 类别：nonconst |
| GetDecreasingInterestsDesc |  | CString | 类别：nonconst |
| GetDeficitConvoyRatio |  | CFixedPoint | 类别：nonconst |
| GetDeficitConvoyRatioForProgressBar |  | CFixedPoint | 类别：nonconst |
| GetDeficitPowerRatio | Unknown | CFixedPoint | 类别：nonconst |
| GetDeficitPowerRatioForProgressBar | CString | CFixedPoint | 类别：nonconst |
| GetDefinition |  | CountryDefinition | 类别：nonconst |
| GetDependents |  | int64 | 类别：nonconst |
| GetDiplomaticAction | Unknown Unknown | DiplomaticAction | 类别：nonconst |
| GetDiplomaticActionWithStates | Unknown Unknown Unknown Unknown | DiplomaticAction | 类别：nonconst |
| GetDiplomaticPactsExpenseTrend |  | DataTrend | 类别：nonconst |
| GetDiplomaticPactsIncomeTrend |  | DataTrend | 类别：nonconst |
| GetDiplomaticStatusColor | Country | CVector4f | 类别：nonconst |
| GetDividendsTaxTrend |  | DataTrend | 类别：nonconst |
| GetDomesticallyOwnedGDP |  | CFixedPoint | 类别：nonconst |
| GetDomesticallyOwnedGDPFraction |  | CFixedPoint | 类别：nonconst |
| GetDraftTreaties |  | Unknown | 类别：nonconst |
| GetDraftTreatiesWith | Unknown | Unknown | 类别：nonconst |
| GetEconomicDependenceOn | Country | CString | 类别：nonconst |
| GetEconomicDependenceOnDesc | Unknown | CString | 类别：nonconst |
| GetEconomicDependenceOnRaw | Unknown | CFixedPoint | 类别：nonconst |
| GetElection |  | Election | 类别：nonconst |
| GetElectionPollTooltip |  | CString | 类别：nonconst |
| GetElectoralConfidence |  | CFixedPoint | 类别：nonconst |
| GetElectoralConfidenceEffectDesc |  | CString | 类别：nonconst |
| GetEmployedWorkingAdults |  | int64 | 类别：nonconst |
| GetEmptyAgitatorSlots |  | int32 | 类别：nonconst |
| GetEnemyOccupation |  | CFixedPoint | 类别：nonconst |
| GetEnforcedTreaties |  | Unknown | 类别：nonconst |
| GetEnforcedTreatiesWith | Country | Unknown | 类别：nonconst |
| GetEnforcedTreatiesWithDesc | Unknown | CString | 类别：nonconst |
| GetEventsByCategory | CString | Unknown | 类别：nonconst |
| GetExcessConvoyRatio |  | CFixedPoint | 类别：nonconst |
| GetExcessConvoyRatioForProgressBar |  | CFixedPoint | 类别：nonconst |
| GetExcessPowerRatio | Unknown | CFixedPoint | 类别：nonconst |
| GetExcessPowerRatioForProgressBar | CString | CFixedPoint | 类别：nonconst |
| GetExpectedSOLFactorsDescAll |  | CString | 类别：nonconst |
| GetExpectedSOLFactorsDescMiddle |  | CString | 类别：nonconst |
| GetExpectedSOLFactorsDescPoor |  | CString | 类别：nonconst |
| GetExpectedSOLFactorsDescRich |  | CString | 类别：nonconst |
| GetExpectedSOLFactorsDescWithCulture | Unknown | CString | 类别：nonconst |
| GetExpectedSoLByPopulation |  | CFixedPoint | 类别：nonconst |
| GetExpectedStandardOfLivingMiddle |  | CFixedPoint | 类别：nonconst |
| GetExpectedStandardOfLivingPoor |  | CFixedPoint | 类别：nonconst |
| GetExpectedStandardOfLivingRich |  | CFixedPoint | 类别：nonconst |
| GetExpensesBreakdown |  | CString | 类别：nonconst |
| GetExportSubventionsDescHigh | Goods | CString | 类别：nonconst |
| GetExportSubventionsDescLow | Goods | CString | 类别：nonconst |
| GetExportSubventionsDescMax | Goods | CString | 类别：nonconst |
| GetExportTariffsDescHigh | Goods | CString | 类别：nonconst |
| GetExportTariffsDescLow | Goods | CString | 类别：nonconst |
| GetExportTariffsDescMax | Goods | CString | 类别：nonconst |
| GetExportTariffsDescNone | Goods | CString | 类别：nonconst |
| GetExportedAmount | Unknown | CFixedPoint | 类别：nonconst |
| GetExports |  | Unknown | 类别：nonconst |
| GetFirstPrimaryCulture |  | Culture | 类别：nonconst |
| GetFlag |  | CoatOfArms | 类别：nonconst |
| GetFlagTextIcon |  | CString | 类别：nonconst |
| GetFlavorText |  | CString | 类别：nonconst |
| GetFleetsBreakdown |  | CString | 类别：nonconst |
| GetFlotillasRanking |  | CString | 类别：nonconst |
| GetForeignOwnedGDP |  | CFixedPoint | 类别：nonconst |
| GetForeignOwnedGDPDesc |  | CString | 类别：nonconst |
| GetForeignOwnedGDPFraction |  | CFixedPoint | 类别：nonconst |
| GetFormattedStandardOfLivingAll |  | CString | 类别：nonconst |
| GetFormattedStandardOfLivingAllWithCulture | Culture | CString | 类别：nonconst |
| GetFormattedStandardOfLivingLabelAll |  | CString | 类别：nonconst |
| GetFormattedStandardOfLivingLabelAllWithCulture | Culture | CString | 类别：nonconst |
| GetFormattedStandardOfLivingLabelMiddle |  | CString | 类别：nonconst |
| GetFormattedStandardOfLivingLabelMiddleWithCulture | Culture | CString | 类别：nonconst |
| GetFormattedStandardOfLivingLabelPoor |  | CString | 类别：nonconst |
| GetFormattedStandardOfLivingLabelPoorWithCulture | Culture | CString | 类别：nonconst |
| GetFormattedStandardOfLivingLabelRich |  | CString | 类别：nonconst |
| GetFormattedStandardOfLivingLabelRichWithCulture | Culture | CString | 类别：nonconst |
| GetFormattedStandardOfLivingMiddle |  | CString | 类别：nonconst |
| GetFormattedStandardOfLivingMiddleWithCulture | Culture | CString | 类别：nonconst |
| GetFormattedStandardOfLivingPoor |  | CString | 类别：nonconst |
| GetFormattedStandardOfLivingPoorWithCulture | Culture | CString | 类别：nonconst |
| GetFormattedStandardOfLivingRich |  | CString | 类别：nonconst |
| GetFormattedStandardOfLivingRichWithCulture | Culture | CString | 类别：nonconst |
| GetFreeArableLand |  | int32 | 类别：nonconst |
| GetGDP |  | CFixedPoint | 类别：nonconst |
| GetGDPOwnedInForeignCountries |  | CFixedPoint | 类别：nonconst |
| GetGDPOwnedInForeignCountriesDesc |  | CString | 类别：nonconst |
| GetGDPPerCapita |  | CFixedPoint | 类别：nonconst |
| GetGDPPerCapitaRanking |  | CString | 类别：nonconst |
| GetGDPRanking |  | CString | 类别：nonconst |
| GetGDPTrend |  | DataTrend | 类别：nonconst |
| GetGDPWithOwnershipsInForeignCountries |  | CFixedPoint | 类别：nonconst |
| GetGameOverDateString |  | CString | 类别：nonconst |
| GetGdpRatioOwnedBy | Unknown | CString | 类别：nonconst |
| GetGdpRatioOwnedByDesc | Unknown | CString | 类别：nonconst |
| GetGdpRatioOwnedByRaw | Unknown | CFixedPoint | 类别：nonconst |
| GetGoldProgressDesc |  | CString | 类别：nonconst |
| GetGoldReserveLimit |  | CFixedPoint | 类别：nonconst |
| GetGoldReserveLimitDesc |  | CString | 类别：nonconst |
| GetGoldReserveRatio |  | CFixedPoint | 类别：nonconst |
| GetGoldReserves |  | CFixedPoint | 类别：nonconst |
| GetGoldReservesTrend |  | DataDynamicTrend | 类别：nonconst |
| GetGoodsLeaderboardDesc |  | CString | 类别：nonconst |
| GetGovernment |  | GovernmentType | 类别：nonconst |
| GetGovernmentConstructionGoodsExpenses |  | CFixedPoint | 类别：nonconst |
| GetGovernmentConstructionGoodsExpensesByGoodsDesc |  | CString | 类别：nonconst |
| GetGovernmentGoodsExpenseTrend |  | DataTrend | 类别：nonconst |
| GetGovernmentGoodsExpenses |  | CFixedPoint | 类别：nonconst |
| GetGovernmentGoodsExpensesByGoodsDesc |  | CString | 类别：nonconst |
| GetGovernmentGoodsExpensesDesc |  | CString | 类别：nonconst |
| GetGovernmentIGsDesc |  | CString | 类别：nonconst |
| GetGovernmentInterestGroupsDesc |  | CString | 类别：nonconst |
| GetGovernmentInterestGroupsPopulationDesc |  | CString | 类别：nonconst |
| GetGovernmentLegitimacy |  | int32 | 类别：nonconst |
| GetGovernmentLegitimacyDesc |  | CString | 类别：nonconst |
| GetGovernmentLegitimacyLevel |  | LegitimacyLevel | 类别：nonconst |
| GetGovernmentSelfDebt |  | CFixedPoint | 类别：nonconst |
| GetGovernmentSelfDebtFraction |  | CFixedPoint | 类别：nonconst |
| GetGovernmentShareDividendsTrend |  | DataTrend | 类别：nonconst |
| GetGovernmentShareLossesTrend |  | DataTrend | 类别：nonconst |
| GetGovernmentSlavesExpenseTrend |  | DataTrend | 类别：nonconst |
| GetGovernmentSlavesExpenses |  | CFixedPoint | 类别：nonconst |
| GetGovernmentSlavesExpensesDesc |  | CString | 类别：nonconst |
| GetGovernmentWageLevelDescHigh |  | CString | 类别：nonconst |
| GetGovernmentWageLevelDescLow |  | CString | 类别：nonconst |
| GetGovernmentWageLevelDescMedium |  | CString | 类别：nonconst |
| GetGovernmentWageLevelDescVeryHigh |  | CString | 类别：nonconst |
| GetGovernmentWageLevelDescVeryLow |  | CString | 类别：nonconst |
| GetGovernmentWagesExpenseTrend |  | DataTrend | 类别：nonconst |
| GetGovernmentWagesExpenses |  | CFixedPoint | 类别：nonconst |
| GetGovernmentWagesExpensesDesc |  | CString | 类别：nonconst |
| GetGroupsForActiveJournalEntries |  | Unknown | 类别：nonconst |
| GetGroupsForInActiveJournalEntries |  | Unknown | 类别：nonconst |
| GetGrowingCivilWars |  | Unknown | 类别：nonconst |
| GetHeir |  | Character | 类别：nonconst |
| GetHighestPossibleRank |  | CString | 类别：nonconst |
| GetID |  | int32 | 类别：nonconst |
| GetIDString |  | CString | 类别：nonconst |
| GetIGApprovalFromLoyalistsBreakdown |  | CString | 类别：nonconst |
| GetIGApprovalFromRadicalsBreakdown |  | CString | 类别：nonconst |
| GetImportSubventionsDescHigh | Goods | CString | 类别：nonconst |
| GetImportSubventionsDescLow | Goods | CString | 类别：nonconst |
| GetImportSubventionsDescMax | Goods | CString | 类别：nonconst |
| GetImportTariffsDescHigh | Goods | CString | 类别：nonconst |
| GetImportTariffsDescLow | Goods | CString | 类别：nonconst |
| GetImportTariffsDescMax | 商品 | CString | 类别：非常量 |
| GetImportTariffsDescNone | 商品 | CString | 类别：非常量 |
| GetImportedAmount | Unknown | CFixedPoint | 类别：非常量 |
| GetImports |  | Unknown | 类别：非常量 |
| GetInDefaultEffectsDesc |  | CString | 类别：非常量 |
| GetInForceTreaties |  | Unknown | 类别：非常量 |
| GetInactiveConstructionProjectsDesc |  | CString | 类别：非常量 |
| GetInactivePopulation |  | int64 | 类别：非常量 |
| GetInactivePopulationDesc |  | CString | 类别：非常量 |
| GetIncomeBreakdown |  | CString | 类别：非常量 |
| GetIncomeTaxIncome |  | CFixedPoint | 类别：非常量 |
| GetIncorporatedLiteracyRanking |  | CString | 类别：非常量 |
| GetIncorporatedLiteracyRate |  | CFixedPoint | 类别：非常量 |
| GetIncorporatedLiteracyTrend |  | DataTrend | 类别：非常量 |
| GetIncorporatedPopulation |  | int64 | 类别：非常量 |
| GetIncorporatedStatesLawCostDesc |  | CString | 类别：非常量 |
| GetIndependentInterestGroupsInGovernment |  | Unknown | 类别：非常量 |
| GetIndependentInterestGroupsInOpposition |  | Unknown | 类别：非常量 |
| GetInfamy |  | CFixedPoint | 类别：非常量 |
| GetInfamyColor |  | CVector4f | 类别：非常量 |
| GetInfamyDesc |  | CString | 类别：非常量 |
| GetInfamyIconTexture |  | Unknown | 类别：非常量 |
| GetInfamyLabel |  | CString | 类别：非常量 |
| GetInstitutionInvestment |  | CFixedPoint | 类别：非常量 |
| GetInstitutionInvestmentBureaucracyCost |  | CFixedPoint | 类别：非常量 |
| GetInstitutionInvestmentBureaucracyCostDesc |  | CString | 类别：非常量 |
| GetInstitutionInvestmentBureaucracyFactor |  | CFixedPoint | 类别：非常量 |
| GetInstitutionInvestmentBureaucracyFactorDesc |  | CString | 类别：非常量 |
| GetInstitutionInvestmentDesc |  | CString | 类别：非常量 |
| GetInstitutionsSummary |  | CString | 类别：非常量 |
| GetInsurrectionaryIGsDesc |  | CString | 类别：非常量 |
| GetInterestExpenseTrend |  | DataTrend | 类别：非常量 |
| GetInterestGroupOfType | Unknown | InterestGroup | 类别：非常量 |
| GetInterestPayment |  | CFixedPoint | 类别：非常量 |
| GetInterestRateTooltip |  | CString | 类别：非常量 |
| GetInvestmentFundTrend |  | DataTrend | 类别：非常量 |
| GetInvestmentGdpFractionInCountry | 国家 | CFixedPoint | 类别：非常量 |
| GetInvestmentIncome |  | CFixedPoint | 类别：非常量 |
| GetInvestmentIncomeTrend |  | DataTrend | 类别：非常量 |
| GetInvestmentLevelsInCountry | 国家 | int32 | 类别：非常量 |
| GetInvestmentPool |  | CFixedPoint | 类别：非常量 |
| GetInvestmentPoolChange |  | CFixedPoint | 类别：非常量 |
| GetInvestmentPoolChangeFromConstructionDesc |  | CString | 类别：非常量 |
| GetInvestmentPoolChangeFromInvestmentBreakdown |  | CString | 类别：非常量 |
| GetInvestmentPoolChangeFromInvestmentDesc |  | CString | 类别：非常量 |
| GetInvestmentPoolPredictedNextBuildingDesc |  | CString | 类别：非常量 |
| GetJournalEntry | Unknown | JournalEntry | 类别：非常量 |
| GetKillRateNavy |  | CFixedPoint | 类别：非常量 |
| GetLabel | 国家 | CString | 类别：非常量 |
| GetLackOfAutonomousInvestmentReasonDesc |  | CString | 类别：非常量 |
| GetLastCatalystExpiryDate | 国家 外交催化剂 | CString | 类别：非常量 |
| GetLastElectionResultsTooltip |  | CString | 类别：非常量 |
| GetLawBeingEnacted |  | Law | 类别：非常量 |
| GetLawBeingEnactedFromGroup | Unknown | Law | 类别：非常量 |
| GetLawEnactmentProgress |  | CFixedPoint | 类别：非常量 |
| GetLawEnactmentProgressDesc |  | CString | 类别：非常量 |
| GetLeaderReligionPercentage |  | CFixedPoint | 类别：非常量 |
| GetLeverageAdvantage | 强权集团 | CFixedPoint | 类别：非常量 |
| GetLeverageAdvantageTarget | 强权集团 | CFixedPoint | 类别：非常量 |
| GetLeverageBreakdown |  | CString | 类别：非常量 |
| GetLeverageComparisonDesc | 强权集团 | CString | 类别：非常量 |
| GetLeverageGain | 强权集团 | CFixedPoint | 类别：非常量 |
| GetLeverageGainBreakdown | 强权集团 | CString | 类别：非常量 |
| GetLeverageResistance |  | CFixedPoint | 类别：非常量 |
| GetLeverageTarget | 强权集团 | CFixedPoint | 类别：非常量 |
| GetLeverageTooltip |  | CString | 类别：非常量 |
| GetLibertyDesireLevelLabel |  | CString | 类别：非常量 |
| GetLibertyDesireRaw |  | CFixedPoint | 类别：非常量 |
| GetLimitedMassMigrationCountryAttraction |  | CFixedPoint | 类别：非常量 |
| GetLobbyJournalEntries |  | Unknown | 类别：非常量 |
| GetLowerStrataPopulationTrend |  | DataTrend | 类别：非常量 |
| GetLoyalistsChangeSummary |  | CString | 类别：非常量 |
| GetLoyalistsDecreaseBreakdown |  | CString | 类别：非常量 |
| GetLoyalistsIncreaseBreakdown |  | CString | 类别：非常量 |
| GetLoyalistsOrRadicalsGainedFromLegitimacy |  | int64 | 类别：非常量 |
| GetLoyalistsOrRadicalsGainedFromLegitimacyModifierDescription | Unknown | CString | 类别：非常量 |
| GetLoyalistsSummaryDesc |  | CString | 类别：非常量 |
| GetLoyalistsTrend |  | DataTrend | 类别：非常量 |
| GetLoyaltiesGain |  | CFixedPoint | 类别：非常量 |
| GetMapColor |  | CVector4f | 类别：非常量 |
| GetMarginalAndInactivePopulationInCountryAsPercentage |  | float | 类别：非常量 |
| GetMarginalCloutInCountryAsPercentage |  | float | 类别：非常量 |
| GetMarginalInterestGroupsDesc |  | CString | 类别：非常量 |
| GetMarginalInterestGroupsPopulationDesc |  | CString | 类别：非常量 |
| GetMarket |  | Market | 类别：非常量 |
| GetMarketOwnerName |  | CString | 类别：非常量 |
| GetMassMigrationAttractionBreakdown |  | CString | 类别：非常量 |
| GetMassMigrationAttractionDesc |  | CString | 类别：非常量 |
| GetMaxCloutOrPopulationPercentage |  | float | 类别：非常量 |
| GetMaxCredit |  | CFixedPoint | 类别：非常量 |
| GetMaxFreeCharters |  | int32 | 类别：非常量 |
| GetMaxLawEnactmentSetbacks |  | int32 | 类别：非常量 |
| GetMaxNumCompanies |  | int32 | 类别：非常量 |
| GetMaxNumCompaniesDesc |  | CString | 类别：非常量 |
| GetMaxNumDeclaredInterestsBreakdown |  | CString | 类别：非常量 |
| GetMaxPowerStruggleMonth |  | int32 | 类别：非常量 |
| GetMaxWeeklyTechnologyProgressForTech | Unknown | CFixedPoint | 类别：非常量 |
| GetMaxWeeklyTechnologySpread |  | CFixedPoint | 类别：非常量 |
| GetMaxWeeklyTechnologySpreadForTech | Unknown | CFixedPoint | 类别：非常量 |
| GetMiddleStrataPopulationTrend |  | DataTrend | 类别：非常量 |
| GetMilitaryFormationsArmy |  | Unknown | 类别：非常量 |
| GetMilitaryFormationsFleet |  | Unknown | 类别：非常量 |
| GetMilitaryGoodsExpenseTrend |  | DataTrend | 类别：非常量 |
| GetMilitaryGoodsExpenses |  | CFixedPoint | 类别：非常量 |
| GetMilitaryGoodsExpensesByGoodsDesc |  | CString | 类别：非常量 |
| GetMilitaryGoodsExpensesDesc |  | CString | 类别：非常量 |
| GetMilitaryInterfaceColor |  | CVector4f | 类别：非常量 |
| GetMilitarySlavesExpenseTrend |  | DataTrend | 类别：非常量 |
| GetMilitarySlavesExpenses |  | CFixedPoint | 类别：非常量 |
| GetMilitarySlavesExpensesDesc |  | CString | 类别：非常量 |
| GetMilitaryWageLevelDescHigh |  | CString | 类别：非常量 |
| GetMilitaryWageLevelDescLow |  | CString | 类别：非常量 |
| GetMilitaryWageLevelDescMedium |  | CString | 类别：非常量 |
| GetMilitaryWageLevelDescVeryHigh |  | CString | 类别：非常量 |
| GetMilitaryWageLevelDescVeryLow |  | CString | 类别：非常量 |
| GetMilitaryWagesExpenseTrend |  | DataTrend | 类别：非常量 |
| GetMilitaryWagesExpenses |  | CFixedPoint | 类别：非常量 |
| GetMilitaryWagesExpensesDesc |  | CString | 类别：非常量 |
| GetMinWeeklyTechnologyProgressForTech | 技术 | CFixedPoint | 类别：非常量 |
| GetMinWeeklyTechnologySpread |  | CFixedPoint | 类别：非常量 |
| GetMinWeeklyTechnologySpreadForTech | Unknown | CFixedPoint | 类别：非常量 |
| GetMintingTrend |  | DataTrend | 类别：非常量 |
| GetMobilizationRatio |  | CFixedPoint | 类别：非常量 |
| GetModifier |  | Modifier | 类别：非常量 |
| GetMoveCapitalEffectsDesc |  | CString | 类别：非常量 |
| GetMoveMarketCapitalEffectsDesc |  | CString | 类别：非常量 |
| GetName |  | CString | 类别：非常量 |
| GetNameNoFlag |  | CString | 类别：非常量 |
| GetNameNoFormatting |  | CString | 类别：非常量 |
| GetNavyPowerProjection |  | CFixedPoint | 类别：非常量 |
| GetNavyPowerProjectionDesc |  | CString | 类别：非常量 |
| GetNegotiatingInterestGroup |  | InterestGroup | 类别：非常量 |
| GetNextElectionDate |  | CString | 类别：非常量 |
| GetNextRank |  | CString | 类别：非常量 |
| GetNextRankDesc |  | CString | 类别：非常量 |
| GetNextRankNumber |  | int32 | 类别：非常量 |
| GetNextStartOfCampaignDate |  | CString | 类别：非常量 |
| GetNonPotentialDiploPlays |  | Unknown | 类别：非常量 |
| GetNonSubjectDiplomaticPactsWith | 国家 | Unknown | 类别：非常量 |
| GetNumActiveConstructionQueueElements |  | int32 | 类别：非常量 |
| GetNumActiveGovernmentConstructionQueueElements |  | int32 | 类别：非常量 |
| GetNumActivePrivateConstructionQueueElements |  | int32 | 类别：非常量 |
| GetNumActiveShownConstructionQueueElements |  | int32 | 类别：非常量 |
| GetNumActiveShownGovernmentConstructionQueueElements |  | int32 | 类别：非常量 |
| GetNumActiveShownPrivateConstructionQueueElements |  | int32 | 类别：非常量 |
| GetNumAvailableCompanies |  | int32 | 类别：非常量 |
| GetNumAvailableConvoys |  | int32 | 类别：非常量 |
| GetNumAvailableNegotiations |  | int32 | 类别：非常量 |
| GetNumBattalions |  | int32 | 类别：非常量 |
| GetNumBuildingsInConstructionQueueInState | 州 | int32 | 类别：非常量 |
| GetNumBuildingsUnderConstructionInState | 州 | int32 | 类别：非常量 |
| GetNumCombatUnits |  | int32 | 类别：非常量 |
| GetNumCompanies |  | int32 | 类别：非常量 |
| GetNumConvoys |  | int32 | 类别：非常量 |
| GetNumConvoysDamagedDesc |  | CString | 类别：非常量 |
| GetNumConvoysDesc |  | CString | 类别：非常量 |
| GetNumDamagedConvoys |  | int32 | 类别：非常量 |
| GetNumDeclaredInterests |  | int32 | 类别：非常量 |
| GetNumFlotillas |  | int32 | 类别：非常量 |
| GetNumGovernmentConstructionsInQueue |  | int32 | 类别：非常量 |
| GetNumInactiveAndNonShownGovernmentConstructionQueueElements |  | int32 | 类别：非常量 |
| GetNumInactiveAndNonShownPrivateConstructionQueueElements |  | int32 | 类别：非常量 |
| GetNumInactiveConstructionQueueElements |  | int32 | 类别：非常量 |
| GetNumInactiveGovernmentConstructionQueueElements |  | int32 | 类别：非常量 |
| GetNumInactivePrivateConstructionQueueElements |  | int32 | 类别：非常量 |
| GetNumIncorporatedLiteratePops |  | int64 | 类别：非常量 |
| GetNumIncorporatedStates |  | int32 | 类别：非常量 |
| GetNumIncorporatedStatesDesc |  | CString | 类别：非常量 |
| GetNumInsufficientTaxCapacityStates |  | int32 | 类别：非常量 |
| GetNumInterestGroupMembers |  | int64 | 类别：非常量 |
| GetNumIsolatedStates |  | int32 | 类别：非常量 |
| GetNumLowMarketAccessStates |  | int32 | 类别：非常量 |
| GetNumLoyalists |  | int64 | 类别：非常量 |
| GetNumNeutrals |  | int64 | 类别：非常量 |
| GetNumPoliticallyInactiveLoyalists |  | int64 | 类别：非常量 |
| GetNumPoliticallyInactiveNeutrals |  | int64 | 类别：非常量 |
| GetNumPoliticallyInactiveRadicals |  | int64 | 类别：非常量 |
| GetNumPrivateConstructionsInQueue |  | int32 | 类别：非常量 |
| GetNumRadicals |  | int64 | 类别：非常量 |
| GetNumStatesThatCanBeIncorporated |  | int32 | 类别：非常量 |
| GetNumStatesWithConstruction |  | int32 | 类别：非常量 |
| GetNumStatesWithoutConstruction |  | int32 | 类别：非常量 |
| GetNumTotalLiteratePops |  | int64 | 类别：非常量 |
| GetNumTurmoilStates |  | int32 | 类别：非常量 |
| GetNumUnincorporatedStates |  | int32 | 类别：非常量 |
| GetNumUnincorporatedStatesDesc |  | CString | 类别：非常量 |
| GetNumUsableConvoys |  | int32 | 类别：非常量 |
| GetNumberOfActiveConscriptionCenters |  | int32 | 类别：非常量 |
| GetNumberOfInactiveConscriptionCenters |  | int32 | 类别：非常量 |
| GetObjective |  | Objective | 类别：非常量 |
| GetObligationFromExpirationDate | 国家 | CString | 类别：非常量 |
| GetObligationFromExpirationDesc | 国家 | CString | 类别：非常量 |
| GetObligationToExpirationDate | 国家 | CString | 类别：非常量 |
| GetObligationToExpirationDesc | 国家 | CString | 类别：非常量 |
| GetObligationsOwedFrom |  | Unknown | 类别：非常量 |
| GetObligationsOwedTo |  | Unknown | 类别：非常量 |
| GetOppositionInterestGroupsDesc |  | CString | 类别：非常量 |
| GetOppositionInterestGroupsPopulationDesc |  | CString | 类别：非常量 |
| GetOtherPowerBlocWithHighestLeverage | Unknown | 强权集团 | 类别：非常量 |
| GetOverlord |  | 国家 | 类别：非常量 |
| GetOwningCompany |  | 公司 | 类别：非常量 |
| GetPartiesInGovernment |  | Unknown | 类别：非常量 |
| GetPartiesInOpposition |  | Unknown | 类别：非常量 |
| GetPeopleAbroad |  | int64 | 类别：非常量 |
| GetPlayedByDesc |  | CString | 类别：非常量 |
| GetPlayer |  | 玩家 | 类别：非常量 |
| GetPoliticalLobbies |  | Unknown | 类别：非常量 |
| GetPoliticallyInvolvedPercentage |  | CFixedPoint | 类别：非常量 |
| GetPoliticallyInvolvedPopulation |  | int64 | 类别：非常量 |
| GetPoliticallyInvolvedPopulationDesc |  | CString | 类别：非常量 |
| GetPollTaxIncome |  | CFixedPoint | 类别：非常量 |
| GetPollTaxTrend |  | DataTrend | 类别：非常量 |
| GetPopConsumptionDependenceOn | Unknown | CString | 类别：非常量 |
| GetPopConsumptionDependenceOnDesc | Unknown | CString | 类别：非常量 |
| GetPopConsumptionDependenceOnRaw | Unknown | CFixedPoint | 类别：非常量 |
| GetPopGrowthDesc |  | CString | 类别：非常量 |
| GetPopReligions |  | Unknown | 类别：非常量 |
| GetPopulationRanking |  | CString | 类别：非常量 |
| GetPopulationTrend |  | DataTrend | 类别：非常量 |
| GetPotentialCompanies |  | Unknown | 类别：非常量 |
| GetPotentialDiploPlays |  | Unknown | 类别：非常量 |
| GetPotentialGeneralDiploActions |  | Unknown | 类别：非常量 |
| GetPotentialInvestors |  | Unknown | 类别：非常量 |
| GetPotentialLabor |  | int64 | 类别：非常量 |
| GetPotentialOverlordDiploActions |  | Unknown | 类别：非常量 |
| GetPotentialPowerBlocLeaderDiploActions |  | Unknown | 类别：非常量 |
| GetPotentialPowerBlocMemberDiploActions |  | Unknown | 类别：非常量 |
| GetPotentialSubjectDiploActions |  | Unknown | 类别：非常量 |
| GetPowerBloc |  | 强权集团 | 类别：非常量 |
| GetPowerBlocExpenseDesc |  | CString | 类别：非常量 |
| GetPowerBlocExpenseRaw |  | CFixedPoint | 类别：非常量 |
| GetPowerBlocExpenseTrend |  | DataTrend | 类别：非常量 |
| GetPowerBlocIncomeDesc |  | CString | 类别：非常量 |
| GetPowerBlocIncomeRaw |  | CFixedPoint | 类别：非常量 |
| GetPowerBlocIncomeTrend |  | DataTrend | 类别：非常量 |
| GetPowerBlocNonMemberCountryTooltip |  | CString | 类别：非常量 |
| GetPowerBlocWithHighestLeverage |  | 强权集团 | 类别：非常量 |
| GetPowerBlocsTotalLeverageShare |  | CFixedPoint | 类别：非常量 |
| GetPowerBlocsWithLeverage |  | Unknown | 类别：非常量 |
| GetPowerDelta | CString | CFixedPoint | 类别：非常量 |
| GetPowerDeltaIcon | CString | CString | 类别：非常量 |
| GetPowerExpensesString | CString | CString | 类别：非常量 |
| GetPowerIncome | CString | CFixedPoint | 类别：非常量 |
| GetPowerIncomeString | CString | CString | 类别：非常量 |
| GetPowerTooltip | CString | CString | 类别：非常量 |
| GetPredictedBalanceFromBankruptcy |  | CFixedPoint | 类别：非常量 |
| GetPrestige |  | int32 | 类别：非常量 |
| GetPrestigeDesc |  | CString | 类别：非常量 |
| GetPrestigeForCurrentRank |  | int32 | 类别：非常量 |
| GetPrestigeForNextRank |  | int32 | 类别：非常量 |
| GetPrestigeGoodsLeaderboardDesc |  | CString | 类别：非常量 |
| GetPrestigeToMaintainRank |  | int32 | 类别：非常量 |
| GetPrestigeTrend |  | DataTrend | 类别：非常量 |
| GetPreviousAttitudeTowards | Unknown | AIAttitude | 类别：非常量 |
| GetPreviousAutonomousInvestmentsDesc |  | CString | 类别：非常量 |
| GetPreviousRank |  | CString | 类别：非常量 |
| GetPriceReportDesc |  | CString | 类别：非常量 |
| GetPrimaryCulturesDesc |  | CString | 类别：非常量 |
| GetPrincipal |  | CFixedPoint | 类别：非常量 |
| GetPrivateConstructionGoodsExpenses |  | CFixedPoint | 类别：非常量 |
| GetPrivateConstructionGoodsExpensesByGoodsDesc |  | CString | 类别：非常量 |
| GetPrivateConstructionQueueDesc |  | CString | 类别：非常量 |
| GetRadicalizationFromBankruptcy |  | int64 | 类别：非常量 |
| GetRadicalsChangeSummary |  | CString | 类别：非常量 |
| GetRadicalsDecreaseBreakdown |  | CString | 类别：非常量 |
| GetRadicalsIncreaseBreakdown |  | CString | 类别：非常量 |
| GetRadicalsLoyalistsChangeStartDate |  | CString | 类别：非常量 |
| GetRadicalsSummaryDesc |  | CString | 类别：非常量 |
| GetRadicalsTrend |  | DataTrend | 类别：非常量 |
| GetRank |  | CString | 类别：非常量 |
| GetRankDesc |  | CString | 类别：非常量 |
| GetRankIconIndex |  | int32 | 类别：非常量 |
| GetRankModifier |  | 修正 | 类别：非常量 |
| GetRankNumber |  | int32 | 类别：非常量 |
| GetRankProgress |  | float | 类别：非常量 |
| GetRankTooltip |  | CString | 类别：非常量 |
| GetRecentPartiesDesc |  | CString | 类别：非常量 |
| GetRegularBattalions |  | int32 | 类别：非常量 |
| GetReinforcementRateArmy |  | CFixedPoint | 类别：非常量 |
| GetReinforcementRateNavy |  | CFixedPoint | 类别：非常量 |
| GetRelationsColor | Unknown | CVector4f | 类别：非常量 |
| GetRelationsIconTexture | 国家 | Unknown | 类别：非常量 |
| GetRelationsProgress | Unknown | CFixedPoint | 类别：非常量 |
| GetRelationsProgressDesc | Unknown | CString | 类别：非常量 |
| GetRelationsTooltip | 国家 | CString | 类别：非常量 |
| GetRelationsWith | 国家 | int32 | 类别：非常量 |
| GetRelationsWithDesc | 国家 | CString | 类别：非常量 |
| GetRelativePrestige | 国家 | CFixedPoint | 类别：非常量 |
| GetRemainingCredit |  | CFixedPoint | 类别：非常量 |
| GetRemainingDaysForFreeGovernmentReformRaw |  | int32 | 类别：非常量 |
| GetRequiredConvoys |  | int32 | 类别：非常量 |
| GetRequiredConvoysBreakdown |  | CString | 类别：非常量 |
| GetResearchQueueBottom |  | Unknown | 类别：非常量 |
| GetResearchQueueTop |  | Unknown | 类别：非常量 |
| GetRuler |  | 人物 | 类别：非常量 |
| GetRulingIGsDesc |  | CString | 类别：非常量 |
| GetSOLDescForAllStratas |  | CString | 类别：非常量 |
| GetSalariedWorkingAdults |  | int64 | 类别：非常量 |
| GetSeaNodesMightBeConvoyRaidedInDesc |  | CString | 类别：非常量 |
| GetSelectedLaw |  | 法律 | 类别：非常量 |
| GetSocialHierarchy |  | 社会阶层 | 类别：非常量 |
| GetSpecialSocialHierarchy |  | 社会阶层 | 类别：非常量 |
| GetStandardOfLivingRanking |  | CString | 类别：非常量 |
| GetStateOwnedBuildingsBureaucracyCostForLevels | int32 | CFixedPoint | 类别：非常量 |
| GetStateReligion |  | 宗教 | 类别：非常量 |
| GetStatesInTurmoilBreakdown |  | CString | 类别：非常量 |
| GetStatus | 国家 | CString | 类别：非常量 |
| GetStrategicObjectives |  | Unknown | 类别：非常量 |
| GetStrategicRegions |  | Unknown | 类别：非常量 |
| GetSubjectOrPowerBlocHierarchyLabel | 国家 | CString | 类别：非常量 |
| GetSubjectPact |  | 外交条约 | 类别：非常量 |
| GetSubjectType |  | 附属国类型 | 类别：非常量 |
| GetSubjectTypeName |  | CString | 类别：非常量 |
| GetSubjects |  | Unknown | 类别：非常量 |
| GetSubjectsOfType | 附属国类型 | Unknown | 类别：非常量 |
| GetSubsidiesExpenseTrend |  | DataTrend | 类别：非常量 |
| GetSubsidiesExpenses |  | CFixedPoint | 类别：非常量 |
| GetSubsidiesExpensesDesc |  | CString | 类别：非常量 |
| GetSubsistingWorkingAdults |  | int64 | 类别：非常量 |
| GetSubventionsExpenseTrend |  | DataTrend | 类别：非常量 |
| GetSubventionsExpenses |  | CFixedPoint | 类别：非常量 |
| GetSubventionsExpensesDesc |  | CString | 类别：非常量 |
| GetSupplyNetworkNumSeaNodes |  | int32 | 类别：非常量 |
| GetSupplyNetworkNumSeaNodesDesc |  | CString | 类别：非常量 |
| GetSupplyNetworkStrength |  | CFixedPoint | 类别：非常量 |
| GetSuppressionCostDesc |  | CString | 类别：非常量 |
| GetSuppressionDesc |  | CString | 类别：非常量 |
| GetTagName |  | CString | 类别：非常量 |
| GetTargetLeverage | Unknown | CFixedPoint | 类别：非常量 |
| GetTargetLeverageShare | 强权集团 | CFixedPoint | 类别：非常量 |
| GetTargetRank |  | CString | 类别：非常量 |
| GetTariffTrend |  | DataTrend | 类别：非常量 |
| GetTaxIncomeFor | Unknown | CFixedPoint | 类别：非常量 |
| GetTaxIncomeTrend |  | DataTrend | 类别：非常量 |
| GetTaxLevelDescHigh |  | CString | 类别：非常量 |
| GetTaxLevelDescLow |  | CString | 类别：非常量 |
| GetTaxLevelDescMedium |  | CString | 类别：非常量 |
| GetTaxLevelDescVeryHigh |  | CString | 类别：非常量 |
| GetTaxLevelDescVeryLow |  | CString | 类别：非常量 |
| GetTensionIconTexture | 国家 | Unknown | 类别：非常量 |
| GetTensionTooltip | 国家 | CString | 类别：非常量 |
| GetTensionWith | 国家 | int32 | 类别：非常量 |
| GetTensionWithDesc | 国家 | CString | 类别：非常量 |
| GetTimeUntilTargetReachedArmy |  | CString | 类别：非常量 |
| GetTimeUntilTargetReachedNavy |  | CString | 类别：非常量 |
| GetTimedModifierDurationRemaining | 修正 | CString | 类别：非常量 |
| GetTimedModifiers |  | Unknown | 类别：非常量 |
| GetTooltipTag |  | CString | 类别：非常量 |
| GetTopOverlord |  | 国家 | 类别：非常量 |
| GetTotalAgitatorSlots |  | int32 | 类别：非常量 |
| GetTotalExpensesTrend |  | DataTrend | 类别：非常量 |
| GetTotalExportedAmount |  | CFixedPoint | 类别：非常量 |
| GetTotalForeignConstructions |  | int32 | 类别：非常量 |
| GetTotalGovernmentClout |  | CFixedPoint | 类别：非常量 |
| GetTotalImportedAmount |  | CFixedPoint | 类别：非常量 |
| GetTotalIncomeTrend |  | DataTrend | 类别：非常量 |
| GetTotalLeverageFactors |  | CFixedPoint | 类别：非常量 |
| GetTotalLeverageFactorsBreakdown |  | CString | 类别：非常量 |
| GetTotalLeverageFactorsWithResistance |  | CFixedPoint | 类别：非常量 |
| GetTotalLeverageFactorsWithResistanceBreakdown |  | CString | 类别：非常量 |
| GetTotalLiteracyRanking |  | CString | 类别：非常量 |
| GetTotalLiteracyRate |  | CFixedPoint | 类别：非常量 |
| GetTotalMarginalClout |  | CFixedPoint | 类别：非常量 |
| GetTotalNumLoyalistsChange |  | int64 | 类别：非常量 |
| GetTotalNumLoyalistsDecrease |  | int64 | 类别：非常量 |
| GetTotalNumLoyalistsIncrease |  | int64 | 类别：非常量 |
| GetTotalNumRadicalsChange |  | int64 | 类别：非常量 |
| GetTotalNumRadicalsDecrease |  | int64 | 类别：非常量 |
| GetTotalNumRadicalsIncrease |  | int64 | 类别：非常量 |
| GetTotalOppositionClout |  | CFixedPoint | 类别：非常量 |
| GetTotalPopulation |  | int64 | 类别：非常量 |
| GetTotalUrbanization |  | int32 | 类别：非常量 |
| GetTreatiesBrokenFromNeutralityDesc | DiplomaticPlay | CString | 类别：非常量 |
| GetTreatiesExpenseTrend |  | DataTrend | 类别：非常量 |
| GetTreatiesIncomeTrend |  | DataTrend | 类别：非常量 |
| GetTreatiesWith | Country | Unknown | 类别：非常量 |
| GetTreatiesWithDesc | Country | CString | 类别：非常量 |
| GetTruceDate | Country | CString | 类别：非常量 |
| GetUnclaimedLeverage |  | CFixedPoint | 类别：非常量 |
| GetUnclaimedLeverageFormatted |  | CString | 类别：非常量 |
| GetUnclaimedLeverageShare |  | CFixedPoint | 类别：非常量 |
| GetUnclaimedLeverageShareTarget |  | CFixedPoint | 类别：非常量 |
| GetUnclaimedLeverageTarget |  | CFixedPoint | 类别：非常量 |
| GetUnemployedWorkingAdults |  | int64 | 类别：非常量 |
| GetUnenforcedTreaties |  | Unknown | 类别：非常量 |
| GetUnenforcedTreatiesWith | Country | Unknown | 类别：非常量 |
| GetUnenforcedTreatiesWithDesc | Unknown | CString | 类别：非常量 |
| GetUnrealizedTaxes |  | CFixedPoint | 类别：非常量 |
| GetUpperStrataPopulationTrend |  | DataTrend | 类别：非常量 |
| GetUsedAgitatorSlots |  | int32 | 类别：非常量 |
| GetUsedFreeCharters |  | int32 | 类别：非常量 |
| GetWarships |  | int32 | 类别：非常量 |
| GetWeeklyBalance |  | CFixedPoint | 类别：非常量 |
| GetWeeklyCostArmy |  | CFixedPoint | 类别：非常量 |
| GetWeeklyCostNavy |  | CFixedPoint | 类别：非常量 |
| GetWeeklyExpenses |  | CFixedPoint | 类别：非常量 |
| GetWeeklyFixedExpenses |  | CFixedPoint | 类别：非常量 |
| GetWeeklyGDP |  | CFixedPoint | 类别：非常量 |
| GetWeeklyIncome |  | CFixedPoint | 类别：非常量 |
| GetWeeklyInnovation |  | CFixedPoint | 类别：非常量 |
| GetWeeklyInnovationDesc |  | CString | 类别：非常量 |
| GetWeeklyInterestRate |  | CFixedPoint | 类别：非常量 |
| GetWeeklyLeverageGain | PowerBloc | CFixedPoint | 类别：非常量 |
| GetWeeklyLibertyDesireChange |  | CFixedPoint | 类别：非常量 |
| GetWeeklyLibertyDesireChangeDesc |  | CString | 类别：非常量 |
| GetWeeklyLibertyDesireChangeFromSupportIndependence |  | CFixedPoint | 类别：非常量 |
| GetWeeklyLibertyDesireChangeFromSupportIndependenceDesc |  | CString | 类别：非常量 |
| GetWeeklyMaxInnovation |  | CFixedPoint | 类别：非常量 |
| GetWeeklyMaxInnovationDesc |  | CString | 类别：非常量 |
| GetWeeklyRawInnovation |  | CFixedPoint | 类别：非常量 |
| GetWeeklyResearchSpeed |  | CFixedPoint | 类别：非常量 |
| GetWeeklyResearchSpeedDesc |  | CString | 类别：非常量 |
| GetWeeklyTechnologyProgressDescForTech | Technology | CString | 类别：非常量 |
| GetWeeklyTechnologySpreadBreakdown |  | CString | 类别：非常量 |
| GetWeeklyTechnologySpreadDesc |  | CString | 类别：非常量 |
| GetWeeklyTechnologySpreadForTechDesc | Technology | CString | 类别：非常量 |
| GetWeeklyTemporaryExpenses |  | CFixedPoint | 类别：非常量 |
| GetWeeklyTemporaryIncome |  | CFixedPoint | 类别：非常量 |
| GetWelfarePaymentsExpenses |  | CFixedPoint | 类别：非常量 |
| GetWelfarePaymentsTrend |  | DataTrend | 类别：非常量 |
| GetWorkingAdults |  | int64 | 类别：非常量 |
| GetYearlyInterestRate |  | CFixedPoint | 类别：非常量 |
| GetYouOrCountryName |  | CString | 类别：非常量 |
| GetZeroBalancePlotPoints |  | Unknown | 类别：非常量 |
| GetZeroMoneyPlotPoints |  | Unknown | 类别：非常量 |
| HasActiveDiplomacy |  | bool |  |
| HasAnyAllianceLikeTreatiesWith | Unknown | bool |  |
| HasAnySlavery |  | bool |  |
| HasAnyTaxes |  | bool |  |
| HasConstructionQueued |  | bool |  |
| HasCurrentlyResearchedTechnology |  | bool |  |
| HasDamagedConvoys |  | bool |  |
| HasDeclaredInterest | Unknown | bool |  |
| HasDecreasingInterests |  | bool |  |
| HasDiplomaticPactWith | Unknown Unknown | bool |  |
| HasElectionTrendData |  | bool |  |
| HasElections |  | bool |  |
| HasExportSubventionsHigh | Goods | bool |  |
| HasExportSubventionsLow | Goods | bool |  |
| HasExportSubventionsMax | Goods | bool |  |
| HasExportTariffsHigh | Goods | bool |  |
| HasExportTariffsLow | Goods | bool |  |
| HasExportTariffsMax | Goods | bool |  |
| HasExportTariffsNone | Goods | bool |  |
| HasForeignInvestmentRights | Country | bool |  |
| HasGovernmentWages |  | bool |  |
| HasHeir |  | bool |  |
| HasHigherUnclaimedLeverage |  | bool |  |
| HasHigherUnclaimedLeverageTarget |  | bool |  |
| HasIGApprovalFromLoyalists |  | bool |  |
| HasIGApprovalFromRadicals |  | bool |  |
| HasImportSubventionsHigh | Goods | bool |  |
| HasImportSubventionsLow | Goods | bool |  |
| HasImportSubventionsMax | Goods | bool |  |
| HasImportTariffsHigh | Goods | bool |  |
| HasImportTariffsLow | Goods | bool |  |
| HasImportTariffsMax | Goods | bool |  |
| HasImportTariffsNone | Goods | bool |  |
| HasInterestIn | StrategicRegion | bool |  |
| HasMilitaryWages |  | bool |  |
| HasNewProductionMethodInGroup | ProductionMethodGroup | bool |  |
| HasNewProductionMethodInSameGroup | BuildingType ProductionMethod | bool |  |
| HasObjective |  | bool |  |
| HasOverlappingInterestsWith | Unknown | bool |  |
| HasOwningCompany |  | bool |  |
| HasProgressingLawEnactment |  | bool |  |
| HasRuler |  | bool |  |
| HasSelectedLaw |  | bool |  |
| HasSpecialSocialHierarchy |  | bool |  |
| InDefault |  | bool |  |
| IsAI |  | bool |  |
| IsAIOrOtherPlayer |  | bool |  |
| IsAlliedInDiploPlayWith | Country | bool |  |
| IsAnySubjectOf | Unknown | bool |  |
| IsAtWar |  | bool |  |
| IsAtWarWith | Country | bool |  |
| IsBeingHighlighted |  | bool |  |
| IsBeingTutorialHighlighted |  | bool |  |
| IsColonizable |  | bool |  |
| IsCommittedInDiplomaticPlay |  | bool |  |
| IsConscripting |  | bool |  |
| IsConstructionPaused |  | bool |  |
| IsDead |  | bool |  |
| IsDiplomaticallyRelevantCountry | Unknown | bool |  |
| IsEconomyHealthy |  | bool |  |
| IsEconomyHealthyDesc |  | CString |  |
| IsEnactingLaw |  | bool |  |
| IsHighestRank |  | bool |  |
| IsIgnoringCountryFormation | CountryFormation | bool |  |
| IsIgnoringDecision | Decision | bool |  |
| IsInElectionCampaignPeriod |  | bool |  |
| IsInPowerBloc |  | bool |  |
| IsInsurrectionary |  | bool |  |
| IsInvolvedInActiveConflict |  | bool |  |
| IsLocalPlayer |  | bool |  |
| IsLowestRank |  | bool |  |
| IsMobilized |  | bool |  |
| IsNegotiating |  | bool |  |
| IsNeighborsWith | Unknown | bool |  |
| IsNewProductionMethod | ProductionMethod | bool |  |
| IsObjectiveIdle |  | bool |  |
| IsOtherPlayer |  | bool |  |
| IsPinnedInOutliner |  | bool |  |
| IsPlayer |  | bool |  |
| IsPowerBlocLeader |  | bool |  |
| IsPowerStruggling |  | bool |  |
| IsRank | Unknown | bool |  |
| IsRevolutionary |  | bool |  |
| IsSecessionist |  | bool |  |
| IsSubject |  | bool |  |
| IsSubjectOf | Country | bool |  |
| IsTaxingAnyGood |  | bool |  |
| IsValid |  | bool |  |
| LeavePowerBloc |  | Command |  |
| MakeScope |  | Scope |  |
| MobilizeAllArmies |  | Command |  |
| OwesObligationTo | Unknown | bool |  |
| PauseConstruction |  | Command |  |
| PauseConstructionTooltip |  | CString |  |
| PredictBalanceWithoutTemporaryIncomeAndExpenses |  | CFixedPoint |  |
| PredictConsumptionTaxes |  | CFixedPoint |  |
| PredictDiplomaticPactsExpenses |  | CFixedPoint |  |
| PredictDiplomaticPactsExpensesDesc |  | CString |  |
| PredictDiplomaticPactsIncome |  | CFixedPoint |  |
| PredictDiplomaticPactsIncomeDesc |  | CString |  |
| PredictDividendsTaxes |  | CFixedPoint |  |
| PredictDividendsTaxesDesc |  | CString |  |
| PredictEconomyHealthDesc |  | CString |  |
| PredictGovernmentShareDividends |  | CFixedPoint |  |
| PredictGovernmentShareDividendsDesc |  | CString |  |
| PredictGovernmentShareLosses |  | CFixedPoint |  |
| PredictGovernmentShareLossesDesc |  | CString |  |
| PredictGovernmentWagesExpenses |  | CFixedPoint |  |
| PredictMaxWeeklyTechnologyProgressForTech | Unknown | CFixedPoint |  |
| PredictMilitaryWagesExpenses |  | CFixedPoint |  |
| PredictMinWeeklyTechnologyProgressForTech | Unknown | CFixedPoint |  |
| PredictMinting |  | CFixedPoint |  |
| PredictMintingDesc |  | CString |  |
| PredictTariffs |  | CFixedPoint |  |
| PredictTariffsDesc |  | CString |  |
| PredictTotalMilitaryExpenses |  | CFixedPoint |  |
| PredictTreatyExpenses |  | CFixedPoint |  |
| PredictTreatyExpensesDesc |  | CString |  |
| PredictTreatyIncome |  | CFixedPoint |  |
| PredictTreatyIncomeDesc |  | CString |  |
| PredictWeeklyBalance |  | CFixedPoint |  |
| PredictWeeklyBalanceWithEconomyHealthHint |  | CString |  |
| PredictWeeklyFixedIncome |  | CFixedPoint |  |
| PredictWeeklyIncome |  | CFixedPoint |  |
| RemoveCompany | CompanyType | Command |  |
| ResumeConstruction |  | Command |  |
| ResumeConstructionTooltip |  | CString |  |
| Self |  | Country |  |
| SetExportSubventionsHigh | Goods | Command |  |
| SetExportSubventionsLow | Goods | Command |  |
| SetExportSubventionsMax | Goods | Command |  |
| SetExportTariffsHigh | Goods | Command |  |
| SetExportTariffsLow | Goods | Command |  |
| SetExportTariffsMax | Goods | Command |  |
| SetExportTariffsNone | Goods | Command |  |
| SetGovernmentWageLevelHigh |  | Command |  |
| SetGovernmentWageLevelLow |  | Command |  |
| SetGovernmentWageLevelMedium |  | Command |  |
| SetGovernmentWageLevelVeryHigh |  | Command |  |
| SetGovernmentWageLevelVeryLow |  | Command |  |
| SetImportSubventionsHigh | Goods | Command |  |
| SetImportSubventionsLow | Goods | Command |  |
| SetImportSubventionsMax | Goods | Command |  |
| SetImportTariffsHigh | Goods | Command |  |
| SetImportTariffsLow | Goods | Command |  |
| SetImportTariffsMax | Goods | Command |  |
| SetImportTariffsNone | Goods | Command |  |
| SetMilitaryWageLevelHigh |  | Command |  |
| SetMilitaryWageLevelLow |  | Command |  |
| SetMilitaryWageLevelMedium |  | Command |  |
| SetMilitaryWageLevelVeryHigh |  | Command |  |
| SetMilitaryWageLevelVeryLow |  | Command |  |
| SetTaxLevelHigh |  | Command |  |
| SetTaxLevelLow |  | Command |  |
| SetTaxLevelMedium |  | Command |  |
| SetTaxLevelVeryHigh |  | Command |  |
| SetTaxLevelVeryLow |  | Command |  |
| ShowInvestmentPoolPredictedNextBuilding |  | bool |  |
| SortCompanies | Unknown | void |  |
| SortCultures | CString | void |  |
| SortReligions | CString | void |  |
| SortStates | Unknown | void |  |
| SortSubjects | CString | void |  |
| StartNegotiationWith | InterestGroup | Command |  |
| ToggleIgnoreCountryFormation | CountryFormation | Command |  |
| ToggleIgnoreDecision | Decision | Command |  |
| TogglePinInOutliner |  | void |  |
| TryGetOverlordTooltipEntry |  | CString |  |
| TryGetSubjectsTooltipEntry |  | CString |  |

| 函数 | 参数 | 输出 | 描述 |
|---|---|---|---|
| AccessSelf |  | Scope | 类别：常量 |
| GetFlagName |  | CString | 类别：非常量 |
| GetList | Unknown | Unknown | 类别：非常量 |
| GetScriptValueDesc | ScriptValue | CString | 类别：非常量 |
| GetValue |  | CFixedPoint | 类别：非常量 |
| GetValueWithDefault | Unknown | CFixedPoint | 类别：非常量 |
| IsSet |  | bool |  |
| ScriptValue | ScriptValue | CFixedPoint |  |
| Self |  | Scope |  |
| VarRemaining | Unknown | int32 |  |

| 函数 | 参数 | 输出 | 描述 |
|---|---|---|---|
| AccessSelf |  | TopScope | 类别：常量 |
| End |  | TopScope |  |
| GetFlagName | Unknown | CString | 类别：非常量 |
| GetLocalVariable | Unknown | Scope | 类别：非常量 |
| GetRootScope |  | Scope | 类别：非常量 |
| GetScriptValueDesc | ScriptValue | CString | 类别：非常量 |
| GetValue | CString | CFixedPoint | 类别：非常量 |
| ScriptValue | ScriptValue | CFixedPoint |  |
| Self |  | TopScope |  |
| gsIG | CString | InterestGroup |  |
| gsInterestGroup | CString | InterestGroup |  |
| sB | CString | Building |  |
| sBG | CString | BuildingGroup |  |
| sBT | CString | BuildingType |  |
| sBuilding | CString | Building |  |
| sBuildingGroup | CString | BuildingGroup |  |
| sBuildingType | CString | BuildingType |  |
| sC | CString | Country |  |
| sCF | CString | CountryFormation |  |
| sCM | CString | Company |  |
| sCMT | CString | CompanyType |  |
| sCOT | CString | CommanderOrderType |  |
| sCU | CString | CombatUnit |  |
| sCW | CString | CivilWar |  |
| sCha | CString | Character |  |
| sCharacter | CString | Character |  |
| sCivilWar | CString | CivilWar |  |
| sCommanderOrderType | CString | CommanderOrderType |  |
| sCompany | CString | Company |  |
| sCompanyType | CString | CompanyType |  |
| sCountry | CString | Country |  |
| sCountryFormation | CString | CountryFormation |  |
| sCulture | CString | Culture |  |
| sD | CString | Decision |  |
| sDA | CString | DiplomaticAction |  |
| sDC | CString | DiplomaticCatalyst |  |
| sDCC | CString | DiplomaticCatalystCategory |  |
| sDCT | CString | DiplomaticCatalystType |  |
| sDD | CString | DiplomaticDemand |  |
| sDP | CString | DiplomaticPlay |  |
| sDPT | CString | DiplomaticPlayType |  |
| sDR | CString | DiplomaticRelations |  |
| sDecision | CString | Decision |  |
| sDiplomaticAction | CString | DiplomaticAction |  |
| sDiplomaticCatalyst | CString | DiplomaticCatalyst |  |
| sDiplomaticCatalystCategory | CString | DiplomaticCatalystCategory |  |
| sDiplomaticCatalystType | CString | DiplomaticCatalystType |  |
| sDiplomaticDemand | CString | DiplomaticDemand |  |
| sDiplomaticPact | CString | DiplomaticPact |  |
| sDiplomaticPlay | CString | DiplomaticPlay |  |
| sDiplomaticPlayType | CString | DiplomaticPlayType |  |
| sDiplomaticRelations | CString | DiplomaticRelations |  |
| sF | CString | Front |  |
| sFront | CString | Front |  |
| sG | CString | Goods |  |
| sGoods | CString | Goods |  |
| sHC | CString | HarvestCondition |  |
| sHCA | CString | HarvestConditionArea |  |
| sHCT | CString | HarvestConditionType |  |
| sHQ | CString | Hq |  |
| sHarvestCondition | CString | HarvestCondition |  |
| sHarvestConditionArea | CString | HarvestConditionArea |  |
| sHarvestConditionType | CString | HarvestConditionType |  |
| sIGT | CString | InterestGroupTrait |  |
| sIdeology | CString | Ideology |  |
| sInstitution | CString | Institution |  |
| sInstitutionType | CString | InstitutionType |  |
| sInterestGroupTrait | CString | InterestGroupTrait |  |
| sJE | CString | JournalEntry |  |
| sJournalEntry | CString | JournalEntry |  |
| sL | CString | Law |  |
| sLaw | CString | Law |  |
| sLawType | CString | LawType |  |
| sMilitaryFormation | CString | MilitaryFormation |  |
| sP | CString | Party |  |
| sPB | CString | PowerBloc |  |
| sPBI | CString | PowerBlocIdentity |  |
| sPBP | CString | PowerBlocPrinciple |  |
| sPL | CString | PoliticalLobby |  |
| sPLA | CString | PoliticalLobbyAppeasementFactor |  |
| sPLT | CString | PoliticalLobbyType |  |
| sPM | CString | PoliticalMovement |  |
| sPMC | CString | PoliticalMovementCategory |  |
| sPMT | CString | PoliticalMovementType |  |
| sPT | CString | PopType |  |
| sPact | CString | DiplomaticPact |  |
| sParty | CString | Party |  |
| sPoliticalLobby | CString | PoliticalLobby |  |
| sPoliticalLobbyAppeasement | CString | PoliticalLobbyAppeasementFactor |  |
| sPoliticalLobbyType | CString | PoliticalLobbyType |  |
| sPoliticalMovement | CString | PoliticalMovement |  |
| sPoliticalMovementCategory | CString | PoliticalMovementCategory |  |
| sPoliticalMovementType | CString | PoliticalMovementType |  |
| sPop | CString | Pop |  |
| sPopType | CString | PopType |  |
| sPowerBloc | CString | PowerBloc |  |
| sPowerBlocIdentity | CString | PowerBlocIdentity |  |
| sPowerBlocPrinciple | CString | PowerBlocPrinciple |  |
| sPowerBlocPrincipleGroup | CString | PowerBlocPrincipleGroup |  |
| sProvince | CString | Province |  |
| sReligion | CString | Religion |  |
| sS | CString | State |  |
| sSR | CString | StrategicRegion |  |
| sSW | CString | Sway |  |
| sState | CString | State |  |
| sStateRegion | CString | StateRegion |  |
| sStrategicRegion | CString | StrategicRegion |  |
| sSway | CString | Sway |  |
| sT | CString | Technology |  |
| sTechnology | CString | Technology |  |
| sTreaty | CString | Treaty |  |
| sTreatyArticle | CString | Article |  |
| sW | CString | War |  |
| sWar | CString | War |  |
| sWarGoal | CString | WarGoal |  |
| sWarGoalType | CString | WarGoalType |  |
### 所有数据类型 function 列表

主条目：
GUI 脚本 function 列表
该列表位于单独页面上，因为篇幅过大，无法直接包含在本页中。

## GUI promote（作用域提升）

GUI promote（作用域提升）通常会将 scope（作用域）从一种类型转换为另一种类型。

| Promote | 参数 | 输出 | 说明 |
|---|---|---|---|
| ACCEPTANCE_STATUS |  | AcceptanceStatus |  |
| AIATTITUDE |  | AIAttitude |  |
| AISTRATEGY |  | AIStrategy |  |
| ALERT |  | Alert |  |
| ALERT_GROUP |  | AlertGroup |  |
| ALLY_COUNTRY |  | Country |  |
| AMENDMENT |  | Amendment |  |
| AMENDMENT_TYPE |  | AmendmentType |  |
| AccessGameRules |  | JominiGameRules | 类别：const |
| AccessHighlightManager |  | HighlightManager | 类别：const |
| AccessLogViewer |  | LogViewer | 类别：const |
| AccessMetaPlayer |  | Player | 类别：const |
| AccessPlayer |  | Country | 类别：const |
| AccessPlayerJournalEntry | 未知 | JournalEntry | 类别：const |
| AccessScopeReference | Scope | Scope | 类别：const |
| Application |  | Application |  |
| BATTLE |  | Battle |  |
| BATTLE_CONDITION |  | BattleCondition |  |
| BUILDING |  | Building |  |
| BUILDING_GROUP |  | BuildingGroup |  |
| BUILDING_OWNERSHIP |  | BuildingOwnership |  |
| BUILDING_TYPE |  | BuildingType |  |
| CANAL_TYPE |  | CanalType |  |
| CHARACTER |  | Character |  |
| CHARACTER_INTERACTION |  | CharacterInteraction |  |
| CHARACTER_TRAIT |  | CharacterTrait |  |
| CIVIL_WAR |  | CivilWar |  |
| COHESION_LEVEL |  | CohesionLevel |  |
| COMBAT_UNIT |  | CombatUnit |  |
| COMBAT_UNIT_GROUP |  | CombatUnitGroup |  |
| COMBAT_UNIT_TYPE |  | CombatUnitType |  |
| COMMANDER_ORDER_TYPE |  | CommanderOrderType |  |
| COMMANDER_RANK |  | CommanderRank |  |
| COMPANY |  | Company |  |
| COMPANY_CHARTER |  | CompanyCharter |  |
| COMPANY_CHARTER_TYPE |  | CompanyCharterType |  |
| COMPANY_TYPE |  | CompanyType |  |
| CONSTRUCTION_QUEUE_ELEMENT |  | ConstructionQueueElement |  |
| CONTEXTUAL_DIPLOMATIC_ACTION_TYPE |  | ContextualDiplomaticActionType |  |
| CONTEXTUAL_DIPLOMATIC_PACT |  | ContextualDiplomaticPact |  |
| COUNTRY |  | Country |  |
| COUNTRY_CREATION |  | CountryCreation |  |
| COUNTRY_DEFINITION |  | CountryDefinition |  |
| COUNTRY_FORMATION |  | CountryFormation |  |
| COUNTRY_THIRD_PARTY |  | Country |  |
| CULTURAL_COMMUNITY |  | CulturalCommunity |  |
| CULTURE |  | Culture |  |
| DATE |  | Date |  |
| DATE_MAX |  | Date |  |
| DATE_MIN |  | Date |  |
| DECISION_TYPE |  | Decision |  |
| DECREE |  | Decree |  |
| DECREE_TYPE |  | DecreeType |  |
| DIPLOMATIC_ACTION |  | DiplomaticAction |  |
| DIPLOMATIC_ACTION_TYPE |  | DiplomaticActionType |  |
| DIPLOMATIC_CATALYST |  | DiplomaticCatalyst |  |
| DIPLOMATIC_CATALYST_CATEGORY |  | DiplomaticCatalystCategory |  |
| DIPLOMATIC_CATALYST_TYPE |  | DiplomaticCatalystType |  |
| DIPLOMATIC_DEMAND |  | DiplomaticDemand |  |
| DIPLOMATIC_PACT |  | DiplomaticPact |  |
| DIPLOMATIC_PLAY |  | DiplomaticPlay |  |
| DIPLOMATIC_PLAY_TYPE |  | DiplomaticPlayType |  |
| DIPLOMATIC_RELATIONS |  | DiplomaticRelations |  |
| DISCRIMINATION_TRAIT |  | DiscriminationTrait |  |
| DISCRIMINATION_TRAIT_GROUP |  | DiscriminationTraitGroup |  |
| DLC_METADATA |  | Dlc |  |
| ELECTION |  | Election |  |
| EMPLOYEE_TRANSFER |  | EmployeeTransfer |  |
| ENEMY_COUNTRY |  | Country |  |
| ERA |  | Era |  |
| EVENT |  | Event |  |
| EmptyScope |  | TopScope |  |
| FIRSTMARKET |  | Market |  |
| FIRST_COUNTRY |  | Country |  |
| FRONT |  | Front |  |
| GAME_CONCEPT_TYPE |  | GameConceptType |  |
| GAME_RULE |  | GameRule |  |
| GAME_RULE_SETTING |  | GameRuleSetting |  |
| GC | 未知 | GameConceptType |  |
| GEOGRAPHIC_REGION |  | GeographicRegion |  |
| GOODS |  | Goods |  |
| GOODSPRODUCTIONINFO |  | GoodsProductionInfo |  |
| GOVERNMENT_TYPE |  | GovernmentType |  |
| GetAIStrategy | 未知 | AIStrategy | 类别：nonconst |
| GetAcceptanceStatus | AcceptanceStatus | AcceptanceStatus | 类别：nonconst |
| GetAmendmentType | 未知 | AmendmentType | 类别：nonconst |
| GetArticleType | TreatyArticle | ArticleType | 类别：nonconst |
| GetBattleCondition | BattleCondition | BattleCondition | 类别：nonconst |
| GetBuildingGroup | BuildingGroup | BuildingGroup | 类别：nonconst |
| GetBuildingType | BuildingType | BuildingType | 类别：nonconst |
| GetCharacterTrait | CharacterTrait | CharacterTrait | 类别：nonconst |
| GetCohesionLevel | CohesionLevel | CohesionLevel | 类别：nonconst |
| GetCombatUnitGroup | CombatUnitGroup | CombatUnitGroup | 类别：nonconst |
| GetCombatUnitType | CombatUnit | CombatUnitType | 类别：nonconst |
| GetCommanderOrderType | CommanderOrder | CommanderOrderType | 类别：nonconst |
| GetCompanyCharterType | CompanyCharterType | CompanyCharterType | 类别：nonconst |
| GetConstructionSectorType |  | BuildingType | 类别：nonconst |
| GetCountryDiplomaticAction | DiplomaticAction Country Country | DiplomaticAction | 类别：nonconst |
| GetCulture | Culture | Culture | 类别：nonconst |
| GetCurrentGameDate |  | Date | 类别：nonconst |
| GetDecreeType | Decree | DecreeType | 类别：nonconst |
| GetDiplomaticActionType | DiplomaticAction | DiplomaticActionType | 类别：nonconst |
| GetDiplomaticPlayType | DiplomaticPlay | DiplomaticPlayType | 类别：nonconst |
| GetExilePool |  | ExilePool | 类别：nonconst |
| GetGameEndDate |  | Date | 类别：nonconst |
| GetGameRules |  | JominiGameRules | 类别：nonconst |
| GetGameStartDate |  | Date | 类别：nonconst |
| GetGeographicRegion | GeographicRegion | GeographicRegion | 类别：nonconst |
| GetGlobalVariable | CString | Scope | 类别：nonconst |
| GetGoods | Goods | Goods | 类别：nonconst |
| GetHarvestConditionType | HarvestConditionType | HarvestConditionType | 类别：nonconst |
| GetIdeology | Ideology | Ideology | 类别：nonconst |
| GetInstitutionType | Institution | InstitutionType | 类别：nonconst |
| GetInterestGroupVariant | InterestGroup Country | InterestGroup | 类别：nonconst |
| GetJournalEntryGroup | 未知 | JournalEntryGroup | 类别：nonconst |
| GetLabel | TerrainLabel | Label | 类别：nonconst |
| GetLawGroup | LawGroup | LawGroup | 类别：nonconst |
| GetLawType | LawType | LawType | 类别：nonconst |
| GetLegitimacyLevel | LegitimacyLevel | LegitimacyLevel | 类别：nonconst |
| GetLensToolbar |  | LensToolbar | 类别：nonconst |
| GetLibertyDesireLevel | 未知 | LibertyDesireLevel | 类别：nonconst |
| GetLoadingScreenManager |  | LoadingScreenManager | 类别：nonconst |
| GetMapMode | 未知 | MapMode | 类别：nonconst |
| GetMetaPlayer |  | Player | 类别：nonconst |
| GetMobilizationOption | 未知 | MobilizationOption | 类别：nonconst |
| GetMobilizationOptionGroup | 未知 | MobilizationOptionGroup | 类别：nonconst |
| GetPlayer |  | Country | 类别：nonconst |
| GetPlayerJournalEntry | 未知 | JournalEntry | 类别：nonconst |
| GetPopNeed | PopNeed | PopNeed | 类别：nonconst |
| GetPopType | PopType | PopType | 类别：nonconst |
| GetPowerBlocIdentity | PowerBlocIdentity | PowerBlocIdentity | 类别：nonconst |
| GetPowerBlocPrincipleGroup | PrincipleGroup | PowerBlocPrincipleGroup | 类别：nonconst |
| GetRankModifier | CountryRank | Modifier | 类别：nonconst |
| GetReligion | Religion | Religion | 类别：nonconst |
| GetScriptedGui | ScriptedGui | ScriptedGui | 类别：nonconst |
| GetSelectedFormation |  | MilitaryFormation | 类别：nonconst |
| GetServerInfo |  | ServerInformation | 类别：nonconst |
| GetStateRegion | StateRegion | StateRegion | 类别：nonconst |
| GetStaticModifier | Modifier | Modifier | 类别：nonconst |
| GetStrategicObjectiveFormationInState | Country State | MilitaryFormation | 类别：nonconst |
| GetStrategicRegion | StrategicRegion | StrategicRegion | 类别：nonconst |
| GetSubjectType | SubjectType | SubjectType | 类别：nonconst |
| GetTechnology | Technology | Technology | 类别：nonconst |
| GetTutorialJournalEntry |  | JournalEntry | 类别：nonconst |
| GetVariableSystem |  | VariableSystem | 类别：nonconst |
| GetWarGoalType | 未知 | WarGoalType | 类别：nonconst |
| GuiScope |  | TopScope |  |
| HARVEST_CONDITION |  | HarvestCondition |  |
| HARVEST_CONDITION_AREA |  | HarvestConditionArea |  |
| HARVEST_CONDITION_TYPE |  | HarvestConditionType |  |
| HQ |  | Hq |  |
| IDEOLOGY |  | Ideology |  |
| INITIATOR_COUNTRY |  | Country |  |
| INITIATOR_STATE |  | State |  |
| INSTITUTION |  | Institution |  |
| INSTITUTION_TYPE |  | InstitutionType |  |
| INTEREST |  | Interest |  |
| INTEREST_GROUP |  | InterestGroup |  |
| INTEREST_GROUP_TRAIT |  | InterestGroupTrait |  |
| INVASION |  | Invasion |  |
| InformationPanelBar |  | InformationPanelBar |  |
| JOURNAL_ENTRY |  | JournalEntry |  |
| JOURNAL_ENTRY_GROUP |  | JournalEntryGroup |  |
| JOURNAL_ENTRY_TYPE |  | JournalEntryType |  |
| JominiPlayer |  | Playable |  |
| LAW |  | Law |  |
| LAW_GROUP |  | LawGroup |  |
| LAW_OTHER |  | Law |  |
| LAW_TYPE |  | LawType |  |
| LEGITIMACY_LEVEL |  | LegitimacyLevel |  |
| LIBERTY_DESIRE_LEVEL |  | LibertyDesireLevel |  |
| LabelingHelper |  | LabelingHelper |  |
| MAP_MODE |  | MapMode |  |
| MARKET |  | Market |  |
| MARKET_GOODS |  | MarketGoods |  |
| MILITARY_FORMATION |  | MilitaryFormation |  |
| MILITARY_FORMATION_FLAG |  | MilitaryFormationFlag |  |
| MOBILIZATION_OPTION |  | MobilizationOption |  |
| MOBILIZATION_OPTION_GROUP |  | MobilizationOptionGroup |  |
| MODIFIER |  | Modifier |  |
| MODIFIER_BREAKDOWN |  | ModifierBreakdown |  |
| MapInteractions |  | MapInteractionManager |  |
| MapListPanelManager |  | MapListPanelManager |  |
| MultiplayerSynchronizationInfo |  | MultiplayerSynchronizationInfo |  |
| OBJECTIVE |  | Objective |  |
| OBJECTIVE_TYPE |  | ObjectiveType |  |
| OBJECT_SCOPE |  | Scope |  |
| OTHER_COUNTRY |  | Country |  |
| Outliner |  | Outliner |  |
| PARTY |  | Party |  |
| PLAYER |  | Player |  |
| POLITICAL_LOBBY |  | PoliticalLobby |  |
| POLITICAL_LOBBY_APPEASEMENT_FACTOR |  | PoliticalLobbyAppeasementFactor |  |
| POLITICAL_LOBBY_TYPE |  | PoliticalLobbyType |  |
| POLITICAL_MOVEMENT |  | PoliticalMovement |  |
| POLITICAL_MOVEMENT_CATEGORY |  | PoliticalMovementCategory |  |
| POLITICAL_MOVEMENT_POP_SUPPORT_FACTOR |  | PoliticalMovementPopSupportFactor |  |
| POLITICAL_MOVEMENT_TYPE |  | PoliticalMovementType |  |
| POP |  | Pop |  |
| POP_GOODS_CONSUMPTION |  | PopConsumptionGoods |  |
| POP_NEED |  | PopNeed |  |
| POP_TYPE |  | PopType |  |
| POP_WITH_IG |  | PopWithIG |  |
| POWER_BLOC |  | PowerBloc |  |
| POWER_BLOC_IDENTITY |  | PowerBlocIdentity |  |
| POWER_BLOC_MAP_TEXTURE |  | PowerBlocMapTexture |  |
| POWER_BLOC_OTHER |  | PowerBloc |  |
| POWER_BLOC_PRINCIPLE |  | PowerBlocPrinciple |  |
| POWER_BLOC_PRINCIPLE_DATA |  | PowerBlocPrincipleData |  |
| POWER_BLOC_PRINCIPLE_GROUP |  | PowerBlocPrincipleGroup |  |
| POWER_BLOC_PRINCIPLE_OTHER |  | PowerBlocPrinciple |  |
| POWER_BLOC_STATUE |  | PowerBlocStatue |  |
| POWER_BLOC_STATUE_ACCESSORY_TYPE |  | PowerBlocStatueAccessoryType |  |
| POWER_BLOC_STATUE_HERO_TYPE |  | PowerBlocStatueHeroType |  |
| POWER_BLOC_STATUE_PEDESTAL_TYPE |  | PowerBlocStatuePedestalType |  |
| PREV |  | Scope |  |
| PRODUCTION_METHOD |  | ProductionMethod |  |
| PRODUCTION_METHOD_GROUP |  | ProductionMethodGroup |  |
| PROPOSAL |  | Proposal |  |
| PROVINCE |  | Province |  |
| PROVINCE_OTHER |  | Province |  |
| PdxAccount |  | PdxAccount |  |
| PopupManager |  | PopupManager |  |
| PowerBlocPanel |  | PowerBlocPanel |  |
| RELIGION |  | Religion |  |
| ROOT |  | Scope |  |
| RightClickMenuManager |  | RightClickMenuManager |  |
| Root |  | Scope |  |
| SCOPE |  | TopScope |  |
| SCRIPTED_BUTTON |  | ScriptedButton |  |
| SCRIPTED_PROGRESS_BAR |  | ScriptedProgressBar |  |
| SECONDMARKET |  | Market |  |
| SECOND_COUNTRY |  | Country |  |
| SHIPPING_LANE |  | ShippingLane |  |
| SOCIAL_CLASS |  | SocialClass |  |
| SOCIAL_HIERARCHY |  | SocialHierarchy |  |
| SOURCE_COUNTRY |  | Country |  |
| STATE |  | State |  |
| STATE_GOODS |  | StateGoods |  |
| STATE_OTHER |  | State |  |
| STATE_REGION |  | StateRegion |  |
| STATE_TRAIT |  | StateTrait |  |
| STRATEGIC_REGION |  | StrategicRegion |  |
| SUBJECT_SCOPE |  | Scope |  |
| SUBJECT_TYPE |  | SubjectType |  |
| SWAY |  | Sway |  |
| SWAY_OFFER |  | SwayOffer |  |
| SWAY_OFFER_TYPE |  | SwayOfferType |  |
| SwayCountryPanel |  | SwayCountryPanel |  |
| TARGET_ACCEPTANCE_STATUS |  | AcceptanceStatus |  |
| TARGET_AIATTITUDE |  | AIAttitude |  |
| TARGET_AISTRATEGY |  | AIStrategy |  |
| TARGET_ALERT |  | Alert |  |
| TARGET_ALERT_GROUP |  | AlertGroup |  |
| TARGET_AMENDMENT |  | Amendment |  |
| TARGET_AMENDMENT_TYPE |  | AmendmentType |  |
| TARGET_BATTLE |  | Battle |  |
| TARGET_BATTLE_CONDITION |  | BattleCondition |  |
| TARGET_BUILDING |  | Building |  |
| TARGET_BUILDING_GROUP |  | BuildingGroup |  |
| TARGET_BUILDING_OWNERSHIP |  | BuildingOwnership |  |
| TARGET_BUILDING_TYPE |  | BuildingType |  |
| TARGET_CANAL_TYPE |  | CanalType |  |
| TARGET_CHARACTER |  | Character |  |
| TARGET_CHARACTER_INTERACTION |  | CharacterInteraction |  |
| TARGET_CHARACTER_TRAIT |  | CharacterTrait |  |
| TARGET_CIVIL_WAR |  | CivilWar |  |
| TARGET_COHESION_LEVEL |  | CohesionLevel |  |
| TARGET_COMBAT_UNIT |  | CombatUnit |  |
| TARGET_COMBAT_UNIT_GROUP |  | CombatUnitGroup |  |
| TARGET_COMBAT_UNIT_TYPE |  | CombatUnitType |  |
| TARGET_COMMANDER_ORDER_TYPE |  | CommanderOrderType |  |
| TARGET_COMMANDER_RANK |  | CommanderRank |  |
| TARGET_COMPANY |  | Company |  |
| TARGET_COMPANY_CHARTER |  | CompanyCharter |  |
| TARGET_COMPANY_CHARTER_TYPE |  | CompanyCharterType |  |
| TARGET_COMPANY_TYPE |  | CompanyType |  |
| TARGET_CONSTRUCTION_QUEUE_ELEMENT |  | ConstructionQueueElement |  |
| TARGET_CONTEXTUAL_DIPLOMATIC_ACTION_TYPE |  | ContextualDiplomaticActionType |  |
| TARGET_CONTEXTUAL_DIPLOMATIC_PACT |  | ContextualDiplomaticPact |  |
| TARGET_COUNTRY |  | Country |  |
| TARGET_COUNTRY_CREATION |  | CountryCreation |  |
| TARGET_COUNTRY_DEFINITION |  | CountryDefinition |  |
| TARGET_COUNTRY_FORMATION |  | CountryFormation |  |
| TARGET_CULTURAL_COMMUNITY |  | CulturalCommunity |  |
| TARGET_CULTURE |  | Culture |  |
| TARGET_DECISION_TYPE |  | Decision |  |
| TARGET_DECREE |  | Decree |  |
| TARGET_DECREE_TYPE |  | DecreeType |  |
| TARGET_DIPLOMATIC_ACTION |  | DiplomaticAction |  |
| TARGET_DIPLOMATIC_ACTION_TYPE |  | DiplomaticActionType |  |
| TARGET_DIPLOMATIC_CATALYST |  | DiplomaticCatalyst |  |
| TARGET_DIPLOMATIC_CATALYST_CATEGORY |  | DiplomaticCatalystCategory |  |
| TARGET_DIPLOMATIC_CATALYST_TYPE |  | DiplomaticCatalystType |  |
| TARGET_DIPLOMATIC_DEMAND |  | DiplomaticDemand |  |
| TARGET_DIPLOMATIC_PACT |  | DiplomaticPact |  |
| TARGET_DIPLOMATIC_PLAY |  | DiplomaticPlay |  |
| TARGET_DIPLOMATIC_PLAY_TYPE |  | DiplomaticPlayType |  |
| TARGET_DIPLOMATIC_RELATIONS |  | DiplomaticRelations |  |
| TARGET_DISCRIMINATION_TRAIT |  | DiscriminationTrait |  |
| TARGET_DISCRIMINATION_TRAIT_GROUP |  | DiscriminationTraitGroup |  |
| TARGET_DLC_METADATA |  | Dlc |  |
| TARGET_ELECTION |  | Election |  |
| TARGET_EMPLOYEE_TRANSFER |  | EmployeeTransfer |  |
| TARGET_ERA |  | Era |  |
| TARGET_EVENT |  | Event |  |
| TARGET_FRONT |  | Front |  |
| TARGET_GAME_CONCEPT_TYPE |  | GameConceptType |  |
| TARGET_GEOGRAPHIC_REGION |  | GeographicRegion |  |
| TARGET_GOODS |  | Goods |  |
| TARGET_GOVERNMENT_TYPE |  | GovernmentType |  |
| TARGET_HARVEST_CONDITION |  | HarvestCondition |  |
| TARGET_HARVEST_CONDITION_AREA |  | HarvestConditionArea |  |
| TARGET_HARVEST_CONDITION_TYPE |  | HarvestConditionType |  |
| TARGET_HQ |  | Hq |  |
| TARGET_IDEOLOGY |  | Ideology |  |
| TARGET_INSTITUTION |  | Institution |  |
| TARGET_INSTITUTION_TYPE |  | InstitutionType |  |
| TARGET_INTEREST |  | Interest |  |
| TARGET_INTEREST_GROUP |  | InterestGroup |  |
| TARGET_INTEREST_GROUP_TRAIT |  | InterestGroupTrait |  |
| TARGET_INVASION |  | Invasion |  |
| TARGET_JOURNAL_ENTRY |  | JournalEntry |  |
| TARGET_JOURNAL_ENTRY_GROUP |  | JournalEntryGroup |  |
| TARGET_JOURNAL_ENTRY_TYPE |  | JournalEntryType |  |
| TARGET_LAW |  | Law |  |
| TARGET_LAW_GROUP |  | LawGroup |  |
| TARGET_LAW_TYPE |  | LawType |  |
| TARGET_LEGITIMACY_LEVEL |  | LegitimacyLevel |  |
| TARGET_LIBERTY_DESIRE_LEVEL |  | LibertyDesireLevel |  |
| TARGET_MAP_MODE |  | MapMode |  |
| TARGET_MARKET |  | Market |  |
| TARGET_MARKET_GOODS |  | MarketGoods |  |
| TARGET_MILITARY_FORMATION |  | MilitaryFormation |  |
| TARGET_MILITARY_FORMATION_FLAG |  | MilitaryFormationFlag |  |
| TARGET_MOBILIZATION_OPTION |  | MobilizationOption |  |
| TARGET_MOBILIZATION_OPTION_GROUP |  | MobilizationOptionGroup |  |
| TARGET_MODIFIER |  | Modifier |  |
| TARGET_MODIFIER_BREAKDOWN |  | ModifierBreakdown |  |
| TARGET_OBJECTIVE |  | Objective |  |
| TARGET_OBJECTIVE_TYPE |  | ObjectiveType |  |
| TARGET_PARTY |  | Party |  |
| TARGET_PLAYER |  | Player |  |
| TARGET_POLITICAL_LOBBY |  | PoliticalLobby |  |
| TARGET_POLITICAL_LOBBY_APPEASEMENT_FACTOR |  | PoliticalLobbyAppeasementFactor |  |
| TARGET_POLITICAL_LOBBY_TYPE |  | PoliticalLobbyType |  |
| TARGET_POLITICAL_MOVEMENT |  | PoliticalMovement |  |
| TARGET_POLITICAL_MOVEMENT_CATEGORY |  | PoliticalMovementCategory |  |
| TARGET_POLITICAL_MOVEMENT_POP_SUPPORT_FACTOR |  | PoliticalMovementPopSupportFactor |  |
| TARGET_POLITICAL_MOVEMENT_TYPE |  | PoliticalMovementType |  |
| TARGET_POP |  | Pop |  |
| TARGET_POP_GOODS_CONSUMPTION |  | PopConsumptionGoods |  |
| TARGET_POP_NEED |  | PopNeed |  |
| TARGET_POP_TYPE |  | PopType |  |
| TARGET_POP_WITH_IG |  | PopWithIG |  |
| TARGET_POWER_BLOC |  | PowerBloc |  |
| TARGET_POWER_BLOC_IDENTITY |  | PowerBlocIdentity |  |
| TARGET_POWER_BLOC_MAP_TEXTURE |  | PowerBlocMapTexture |  |
| TARGET_POWER_BLOC_PRINCIPLE |  | PowerBlocPrinciple |  |
| TARGET_POWER_BLOC_PRINCIPLE_DATA |  | PowerBlocPrincipleData |  |
| TARGET_POWER_BLOC_PRINCIPLE_GROUP |  | PowerBlocPrincipleGroup |  |
| TARGET_POWER_BLOC_STATUE |  | PowerBlocStatue |  |
| TARGET_POWER_BLOC_STATUE_ACCESSORY_TYPE |  | PowerBlocStatueAccessoryType |  |
| TARGET_POWER_BLOC_STATUE_HERO_TYPE |  | PowerBlocStatueHeroType |  |
| TARGET_POWER_BLOC_STATUE_PEDESTAL_TYPE |  | PowerBlocStatuePedestalType |  |
| TARGET_PRODUCTION_METHOD |  | ProductionMethod |  |
| TARGET_PRODUCTION_METHOD_GROUP |  | ProductionMethodGroup |  |
| TARGET_PROPOSAL |  | Proposal |  |
| TARGET_PROVINCE |  | Province |  |
| TARGET_RELIGION |  | Religion |  |
| TARGET_SCRIPTED_BUTTON |  | ScriptedButton |  |
| TARGET_SCRIPTED_PROGRESS_BAR |  | ScriptedProgressBar |  |
| TARGET_SHIPPING_LANE |  | ShippingLane |  |
| TARGET_SOCIAL_CLASS |  | SocialClass |  |
| TARGET_SOCIAL_HIERARCHY |  | SocialHierarchy |  |
| TARGET_STATE |  | State |  |
| TARGET_STATE_GOODS |  | StateGoods |  |
| TARGET_STATE_REGION |  | StateRegion |  |
| TARGET_STATE_TRAIT |  | StateTrait |  |
| TARGET_STRATEGIC_REGION |  | StrategicRegion |  |
| TARGET_SUBJECT_TYPE |  | SubjectType |  |
| TARGET_SWAY |  | Sway |  |
| TARGET_SWAY_OFFER |  | SwayOffer |  |
| TARGET_SWAY_OFFER_TYPE |  | SwayOfferType |  |
| TARGET_TECHNOLOGY |  | Technology |  |
| TARGET_THEATER |  | Theater |  |
| TARGET_THEME |  | Theme |  |
| TARGET_TIMED_MODIFIER |  | TimedModifier |  |
| TARGET_TREATY |  | Treaty |  |
| TARGET_TREATY_ARTICLE |  | Article |  |
| TARGET_TREATY_ARTICLE_TYPE |  | ArticleType |  |
| TARGET_TYPE_LABEL |  | Label |  |
| TARGET_WAR |  | War |  |
| TARGET_WAR_GOAL |  | WarGoal |  |
| TARGET_WAR_GOAL_DRAFT |  | WarGoalDraft |  |
| TARGET_WAR_GOAL_TYPE |  | WarGoalType |  |
| TECHNOLOGY |  | Technology |  |
| THEATER |  | Theater |  |
| THEME |  | Theme |  |
| THIS |  | Scope |  |
| TIMED_MODIFIER |  | TimedModifier |  |
| TREATY |  | Treaty |  |
| TREATY_ARTICLE |  | Article |  |
| TREATY_ARTICLE_TYPE |  | ArticleType |  |
| TYPE_LABEL |  | Label |  |
| TimeKeeper |  | TimeKeeper |  |
| WAR |  | War |  |
| WAR_GOAL |  | WarGoal |  |
| WAR_GOAL_DRAFT |  | WarGoalDraft |  |
| WAR_GOAL_TYPE |  | WarGoalType |  |
| WarManager |  | WarManager |  |
| Promote（提升） | Arguments（参数） | Output（输出） | Description（描述） |
|---|---|---|---|
| AccessActiveLawFromGroup | LawGroup | Law | 类别：const |
| AccessCapital |  | State | 类别：const |
| AccessCurrentlyResearchedTechnology |  | Technology | 类别：const |
| AccessDefinition |  | CountryDefinition | 类别：const |
| AccessFirstMarket |  | Market | 类别：const |
| AccessGovernment |  | GovernmentType | 类别：const |
| AccessHeaviestJournalEntry |  | JournalEntry | 类别：const |
| AccessHeir |  | Character | 类别：const |
| AccessLawBeingEnacted |  | Law | 类别：const |
| AccessModifier |  | Modifier | 类别：const |
| AccessOverlord |  | Country | 类别：const |
| AccessPowerBloc |  | PowerBloc | 类别：const |
| AccessRuler |  | Character | 类别：const |
| AccessStateReligion |  | Religion | 类别：const |
| AccessTopOverlord |  | Country | 类别：const |
| CalcLibertyDesireLevel |  | LibertyDesireLevel |  |
| GetActiveLawFrom | Unknown | Law | 类别：nonconst |
| GetActiveLawFromGroup | LawGroup | Law | 类别：nonconst |
| GetAttitudeTowards | Country | AIAttitude | 类别：nonconst |
| GetCapital |  | State | 类别：nonconst |
| GetCurrentlyResearchedTechnology |  | Technology | 类别：nonconst |
| GetDefinition |  | CountryDefinition | 类别：nonconst |
| GetDiplomaticAction | Unknown Unknown | DiplomaticAction | 类别：nonconst |
| GetDiplomaticActionWithStates | Unknown Unknown Unknown Unknown | DiplomaticAction | 类别：nonconst |
| GetElection |  | Election | 类别：nonconst |
| GetFirstPrimaryCulture |  | Culture | 类别：nonconst |
| GetFlag |  | CoatOfArms | 类别：nonconst |
| GetFoodSecurity |  | FoodSecurity | 类别：nonconst |
| GetGovernment |  | GovernmentType | 类别：nonconst |
| GetGovernmentLegitimacyLevel |  | LegitimacyLevel | 类别：nonconst |
| GetHeir |  | Character | 类别：nonconst |
| GetInterestGroupOfType | InterestGroup | InterestGroup | 类别：nonconst |
| GetJournalEntry | Unknown | JournalEntry | 类别：nonconst |
| GetLawBeingEnacted |  | Law | 类别：nonconst |
| GetLawBeingEnactedFromGroup | Unknown | Law | 类别：nonconst |
| GetMarket |  | Market | 类别：nonconst |
| GetModifier |  | Modifier | 类别：nonconst |
| GetMonopolyCountryOnBuildingType | BuildingType | Country | 类别：nonconst |
| GetNegotiatingInterestGroup |  | InterestGroup | 类别：nonconst |
| GetObjective |  | Objective | 类别：nonconst |
| GetOtherPowerBlocWithHighestLeverage | Unknown | PowerBloc | 类别：nonconst |
| GetOverlord |  | Country | 类别：nonconst |
| GetOwningCompany |  | Company | 类别：nonconst |
| GetPlayer |  | Player | 类别：nonconst |
| GetPowerBloc |  | PowerBloc | 类别：nonconst |
| GetPowerBlocWithHighestLeverage |  | PowerBloc | 类别：nonconst |
| GetPreviousAttitudeTowards | Country | AIAttitude | 类别：nonconst |
| GetRankModifier |  | Modifier | 类别：nonconst |
| GetRuler |  | Character | 类别：nonconst |
| GetSampleLowerStrataPop |  | Pop | 类别：nonconst |
| GetSampleLowerStrataPopForCulture | Unknown | Pop | 类别：nonconst |
| GetSampleMiddleStrataPop |  | Pop | 类别：nonconst |
| GetSampleMiddleStrataPopForCulture | Unknown | Pop | 类别：nonconst |
| GetSampleUpperStrataPop |  | Pop | 类别：nonconst |
| GetSampleUpperStrataPopForCulture | Unknown | Pop | 类别：nonconst |
| GetSelectedLaw |  | Law | 类别：nonconst |
| GetSocialHierarchy |  | SocialHierarchy | 类别：nonconst |
| GetSpecialSocialHierarchy |  | SocialHierarchy | 类别：nonconst |
| GetStateReligion |  | Religion | 类别：nonconst |
| GetSubjectPact |  | DiplomaticPact | 类别：nonconst |
| GetSubjectType |  | SubjectType | 类别：nonconst |
| GetTopOverlord |  | Country | 类别：nonconst |
| MakeScope |  | Scope |  |

| Promote（提升） | Arguments（参数） | Output（输出） | Description（描述） |
|---|---|---|---|
| AccessAmendment |  | Amendment | 类别：const |
| AccessAmendmentType |  | AmendmentType | 类别：const |
| AccessBattle |  | Battle | 类别：const |
| AccessBuilding |  | Building | 类别：const |
| AccessBuildingGroup |  | BuildingGroup | 类别：const |
| AccessBuildingType |  | BuildingType | 类别：const |
| AccessCanalType |  | CanalType | 类别：const |
| AccessCharacter |  | Character | 类别：const |
| AccessCivilWar |  | CivilWar | 类别：const |
| AccessCombatUnit |  | CombatUnit | 类别：const |
| AccessCombatUnitType |  | CombatUnitType | 类别：const |
| AccessCommanderOrderType |  | CommanderOrderType | 类别：const |
| AccessCompany |  | Company | 类别：const |
| AccessCompanyType |  | CompanyType | 类别：const |
| AccessCountry |  | Country | 类别：const |
| AccessCountryCreation |  | CountryCreation | 类别：const |
| AccessCountryDefinition |  | CountryDefinition | 类别：const |
| AccessCountryFormation |  | CountryFormation | 类别：const |
| AccessCulturalCommunity |  | CulturalCommunity | 类别：const |
| AccessCulture |  | Culture | 类别：const |
| AccessDecisionType |  | Decision | 类别：const |
| AccessDecree |  | Decree | 类别：const |
| AccessDiplomaticAction |  | DiplomaticAction | 类别：const |
| AccessDiplomaticCatalyst |  | DiplomaticCatalyst | 类别：const |
| AccessDiplomaticCatalystCategory |  | DiplomaticCatalystCategory | 类别：const |
| AccessDiplomaticCatalystType |  | DiplomaticCatalystType | 类别：const |
| AccessDiplomaticDemand |  | DiplomaticDemand | 类别：const |
| AccessDiplomaticPact |  | DiplomaticPact | 类别：const |
| AccessDiplomaticPlay |  | DiplomaticPlay | 类别：const |
| AccessDiplomaticPlayType |  | DiplomaticPlayType | 类别：const |
| AccessDiplomaticRelations |  | DiplomaticRelations | 类别：const |
| AccessFront |  | Front | 类别：const |
| AccessGeographicRegion |  | GeographicRegion | 类别：const |
| AccessGoods |  | Goods | 类别：const |
| AccessHQ |  | Hq | 类别：const |
| AccessHarvestCondition |  | HarvestCondition | 类别：const |
| AccessHarvestConditionArea |  | HarvestConditionArea | 类别：const |
| AccessHarvestConditionType |  | HarvestConditionType | 类别：const |
| AccessIdeology |  | Ideology | 类别：const |
| AccessInstitution |  | Institution | 类别：const |
| AccessInstitutionType |  | InstitutionType | 类别：const |
| AccessInterest |  | Interest | 类别：const |
| AccessInterestGroup |  | InterestGroup | 类别：const |
| AccessInterestGroupTrait |  | InterestGroupTrait | 类别：const |
| AccessInvasion |  | Invasion | 类别：const |
| AccessJournalEntry |  | JournalEntry | 类别：const |
| AccessLaw |  | Law | 类别：const |
| AccessLawType |  | LawType | 类别：const |
| AccessMarket |  | Market | 类别：const |
| AccessMarketGoods |  | MarketGoods | 类别：const |
| AccessMilitaryFormation |  | MilitaryFormation | 类别：const |
| AccessMobilizationOption |  | MobilizationOption | 类别：const |
| AccessObjective |  | Objective | 类别：const |
| AccessParty |  | Party | 类别：const |
| AccessPoliticalLobby |  | PoliticalLobby | 类别：const |
| AccessPoliticalLobbyAppeasementFactor |  | PoliticalLobbyAppeasementFactor | 类别：const |
| AccessPoliticalLobbyType |  | PoliticalLobbyType | 类别：const |
| AccessPoliticalMovement |  | PoliticalMovement | 类别：const |
| AccessPoliticalMovementCategory |  | PoliticalMovementCategory | 类别：const |
| AccessPoliticalMovementType |  | PoliticalMovementType | 类别：const |
| AccessPop |  | Pop | 类别：const |
| AccessPopType |  | PopType | 类别：const |
| AccessPowerBloc |  | PowerBloc | 类别：const |
| AccessPowerBlocIdentity |  | PowerBlocIdentity | 类别：const |
| AccessPowerBlocPrinciple |  | PowerBlocPrinciple | 类别：const |
| AccessPowerBlocPrincipleGroup |  | PowerBlocPrincipleGroup | 类别：const |
| AccessProvince |  | Province | 类别：const |
| AccessReligion |  | Religion | 类别：const |
| AccessShippingLane |  | ShippingLane | 类别：const |
| AccessState |  | State | 类别：const |
| AccessStateGoods |  | StateGoods | 类别：const |
| AccessStateRegion |  | StateRegion | 类别：const |
| AccessStateTrait |  | StateTrait | 类别：const |
| AccessStrategicRegion |  | StrategicRegion | 类别：const |
| AccessSway |  | Sway | 类别：const |
| AccessTechnology |  | Technology | 类别：const |
| AccessTheater |  | Theater | 类别：const |
| AccessTreaty |  | Treaty | 类别：const |
| AccessTreatyArticle |  | Article | 类别：const |
| AccessWar |  | War | 类别：const |
| AccessWarGoal |  | WarGoal | 类别：const |
| AccessWarGoalType |  | WarGoalType | 类别：const |
| GetAmendment |  | Amendment | 类别：nonconst |
| GetAmendmentType |  | AmendmentType | 类别：nonconst |
| GetBattle |  | Battle | 类别：nonconst |
| GetBuilding |  | Building | 类别：nonconst |
| GetBuildingGroup |  | BuildingGroup | 类别：nonconst |
| GetBuildingType |  | BuildingType | 类别：nonconst |
| GetCanalType |  | CanalType | 类别：nonconst |
| GetCharacter |  | Character | 类别：nonconst |
| GetCivilWar |  | CivilWar | 类别：nonconst |
| GetCombatUnit |  | CombatUnit | 类别：nonconst |
| GetCombatUnitType |  | CombatUnitType | 类别：nonconst |
| GetCommanderOrderType |  | CommanderOrderType | 类别：nonconst |
| GetCompany |  | Company | 类别：nonconst |
| GetCompanyType |  | CompanyType | 类别：nonconst |
| GetCountry |  | Country | 类别：nonconst |
| GetCountryCreation |  | CountryCreation | 类别：nonconst |
| GetCountryDefinition |  | CountryDefinition | 类别：nonconst |
| GetCountryFormation |  | CountryFormation | 类别：nonconst |
| GetCulturalCommunity |  | CulturalCommunity | 类别：nonconst |
| GetCulture |  | Culture | 类别：nonconst |
| GetDecisionType |  | Decision | 类别：nonconst |
| GetDecree |  | Decree | 类别：nonconst |
| GetDiplomaticAction |  | DiplomaticAction | 类别：nonconst |
| GetDiplomaticCatalyst |  | DiplomaticCatalyst | 类别：nonconst |
| GetDiplomaticCatalystCategory |  | DiplomaticCatalystCategory | 类别：nonconst |
| GetDiplomaticCatalystType |  | DiplomaticCatalystType | 类别：nonconst |
| GetDiplomaticDemand |  | DiplomaticDemand | 类别：nonconst |
| GetDiplomaticPact |  | DiplomaticPact | 类别：nonconst |
| GetDiplomaticPlay |  | DiplomaticPlay | 类别：nonconst |
| GetDiplomaticPlayType |  | DiplomaticPlayType | 类别：nonconst |
| GetDiplomaticRelations |  | DiplomaticRelations | 类别：nonconst |
| GetFront |  | Front | 类别：nonconst |
| GetGeographicRegion |  | GeographicRegion | 类别：nonconst |
| GetGoods |  | Goods | 类别：nonconst |
| GetHQ |  | Hq | 类别：nonconst |
| GetHarvestCondition |  | HarvestCondition | 类别：nonconst |
| GetHarvestConditionArea |  | HarvestConditionArea | 类别：nonconst |
| GetHarvestConditionType |  | HarvestConditionType | 类别：nonconst |
| GetIdeology |  | Ideology | 类别：nonconst |
| GetInstitution |  | Institution | 类别：nonconst |
| GetInstitutionType |  | InstitutionType | 类别：nonconst |
| GetInterest |  | Interest | 类别：nonconst |
| GetInterestGroup |  | InterestGroup | 类别：nonconst |
| GetInterestGroupTrait |  | InterestGroupTrait | 类别：nonconst |
| GetInvasion |  | Invasion | 类别：nonconst |
| GetJournalEntry |  | JournalEntry | 类别：nonconst |
| GetLaw |  | Law | 类别：nonconst |
| GetLawType |  | LawType | 类别：nonconst |
| GetMarket |  | Market | 类别：nonconst |
| GetMarketGoods |  | MarketGoods | 类别：nonconst |
| GetMilitaryFormation |  | MilitaryFormation | 类别：nonconst |
| GetMobilizationOption |  | MobilizationOption | 类别：nonconst |
| GetObjective |  | Objective | 类别：nonconst |
| GetParty |  | Party | 类别：nonconst |
| GetPoliticalLobby |  | PoliticalLobby | 类别：nonconst |
| GetPoliticalLobbyAppeasementFactor |  | PoliticalLobbyAppeasementFactor | 类别：nonconst |
| GetPoliticalLobbyType |  | PoliticalLobbyType | 类别：nonconst |
| GetPoliticalMovement |  | PoliticalMovement | 类别：nonconst |
| GetPoliticalMovementCategory |  | PoliticalMovementCategory | 类别：nonconst |
| GetPoliticalMovementType |  | PoliticalMovementType | 类别：nonconst |
| GetPop |  | Pop | 类别：nonconst |
| GetPopType |  | PopType | 类别：nonconst |
| GetPowerBloc |  | PowerBloc | 类别：nonconst |
| GetPowerBlocIdentity |  | PowerBlocIdentity | 类别：nonconst |
| GetPowerBlocPrinciple |  | PowerBlocPrinciple | 类别：nonconst |
| GetPowerBlocPrincipleGroup |  | PowerBlocPrincipleGroup | 类别：nonconst |
| GetProvince |  | Province | 类别：nonconst |
| GetReligion |  | Religion | 类别：nonconst |
| GetShippingLane |  | ShippingLane | 类别：nonconst |
| GetState |  | State | 类别：nonconst |
| GetStateGoods |  | StateGoods | 类别：nonconst |
| GetStateRegion |  | StateRegion | 类别：nonconst |
| GetStateTrait |  | StateTrait | 类别：nonconst |
| GetStrategicRegion |  | StrategicRegion | 类别：nonconst |
| GetSway |  | Sway | 类别：nonconst |
| GetTechnology |  | Technology | 类别：nonconst |
| GetTheater |  | Theater | 类别：nonconst |
| GetTreaty |  | Treaty | 类别：nonconst |
| GetTreatyArticle |  | Article | 类别：nonconst |
| GetVariable | Unknown | Scope | 类别：nonconst |
| GetWar |  | War | 类别：nonconst |
| GetWarGoal |  | WarGoal | 类别：nonconst |
| GetWarGoalType |  | WarGoalType | 类别：nonconst |
| Var | CString | Scope |  |

| Promote（提升） | Arguments（参数） | Output（输出） | Description（描述） |
|---|---|---|---|
| AddList | Unknown Unknown | TopScope |  |
| AddScope | Unknown Unknown | TopScope |  |
| GetLocalVariable | Unknown | Scope | 类别：nonconst |
| GetRootScope |  | Scope | 类别：nonconst |
| SetRoot | Scope | TopScope |  |
| gsIG | CString | InterestGroup |  |
| gsInterestGroup | CString | InterestGroup |  |
| sB | CString | Building |  |
| sBG | CString | BuildingGroup |  |
| sBT | CString | BuildingType |  |
| sBuilding | CString | Building |  |
| sBuildingGroup | CString | BuildingGroup |  |
| sBuildingType | CString | BuildingType |  |
| sC | CString | Country |  |
| sCF | CString | CountryFormation |  |
| sCM | CString | Company |  |
| sCMT | CString | CompanyType |  |
| sCOT | CString | CommanderOrderType |  |
| sCU | CString | Culture |  |
| sCW | CString | CivilWar |  |
| sCha | CString | Character |  |
| sCharacter | CString | Character |  |
| sCivilWar | CString | CivilWar |  |
| sCommanderOrderType | CString | CommanderOrderType |  |
| sCompany | CString | Company |  |
| sCompanyType | CString | CompanyType |  |
| sCountry | CString | Country |  |
| sCountryFormation | CString | CountryFormation |  |
| sCulture | CString | Culture |  |
| sD | CString | Decision |  |
| sDA | CString | DiplomaticAction |  |
| sDC | CString | DiplomaticCatalyst |  |
| sDCC | CString | DiplomaticCatalystCategory |  |
| sDCT | CString | DiplomaticCatalystType |  |
| sDD | CString | DiplomaticDemand |  |
| sDP | CString | DiplomaticPlay |  |
| sDPT | CString | DiplomaticPlayType |  |
| sDR | CString | DiplomaticRelations |  |
| sDecision | CString | Decision |  |
| sDiplomaticAction | CString | DiplomaticAction |  |
| sDiplomaticCatalyst | CString | DiplomaticCatalyst |  |
| sDiplomaticCatalystCategory | CString | DiplomaticCatalystCategory |  |
| sDiplomaticCatalystType | CString | DiplomaticCatalystType |  |
| sDiplomaticDemand | CString | DiplomaticDemand |  |
| sDiplomaticPact | CString | DiplomaticPact |  |
| sDiplomaticPlay | CString | DiplomaticPlay |  |
| sDiplomaticPlayType | CString | DiplomaticPlayType |  |
| sDiplomaticRelations | CString | DiplomaticRelations |  |
| sF | CString | Front |  |
| sFront | CString | Front |  |
| sG | CString | Goods |  |
| sGoods | CString | Goods |  |
| sHC | CString | HarvestCondition |  |
| sHCA | CString | HarvestConditionArea |  |
| sHCT | CString | HarvestConditionType |  |
| sHQ | CString | Hq |  |
| sHarvestCondition | CString | HarvestCondition |  |
| sHarvestConditionArea | CString | HarvestConditionArea |  |
| sHarvestConditionType | CString | HarvestConditionType |  |
| sIGT | CString | InterestGroupTrait |  |
| sIdeology | CString | Ideology |  |
| sInstitution | CString | Institution |  |
| sInstitutionType | CString | InstitutionType |  |
| sInterestGroupTrait | CString | InterestGroupTrait |  |
| sJE | CString | JournalEntry |  |
| sJournalEntry | CString | JournalEntry |  |
| sL | CString | Law |  |
| sLaw | CString | Law |  |
| sLawType | CString | LawType |  |
| sMilitaryFormation | CString | MilitaryFormation |  |
| sP | CString | Party |  |
| sPB | CString | PowerBloc |  |
| sPBI | CString | PowerBlocIdentity |  |
| sPBP | CString | PowerBlocPrinciple |  |
| sPL | CString | PoliticalLobby |  |
| sPLA | CString | PoliticalLobbyAppeasementFactor |  |
| sPLT | CString | PoliticalLobbyType |  |
| sPM | CString | PoliticalMovement |  |
| sPMC | CString | PoliticalMovementCategory |  |
| sPMT | CString | PoliticalMovementType |  |
| sPT | CString | PopType |  |
| sPact | CString | DiplomaticPact |  |
| sParty | CString | Party |  |
| sPoliticalLobby | CString | PoliticalLobby |  |
| sPoliticalLobbyAppeasement | CString | PoliticalLobbyAppeasementFactor |  |
| sPoliticalLobbyType | CString | PoliticalLobbyType |  |
| sPoliticalMovement | CString | PoliticalMovement |  |
| sPoliticalMovementCategory | CString | PoliticalMovementCategory |  |
| sPoliticalMovementType | CString | PoliticalMovementType |  |
| sPop | CString | Pop |  |
| sPopType | CString | PopType |  |
| sPowerBloc | CString | PowerBloc |  |
| sPowerBlocIdentity | CString | PowerBlocIdentity |  |
| sPowerBlocPrinciple | CString | PowerBlocPrinciple |  |
| sPowerBlocPrincipleGroup | CString | PowerBlocPrincipleGroup |  |
| sProvince | CString | Province |  |
| sReligion | CString | Religion |  |
| sS | CString | State |  |
| sSR | CString | StrategicRegion |  |
| sSW | CString | Sway |  |
| sState | CString | State |  |
| sStateRegion | CString | StateRegion |  |
| sStrategicRegion | CString | StrategicRegion |  |
| sSway | CString | Sway |  |
| sT | CString | Technology |  |
| sTechnology | CString | Technology |  |
| sTreaty | CString | Treaty |  |
| sTreatyArticle | CString | Article |  |
| sW | CString | War |  |
| sWar | CString | War |  |
| sWarGoal | CString | WarGoal |  |
| sWarGoalType | CString | WarGoalType |  |
### 所有 GUI promote 列表

| 类型 | Promote | 参数 | 输出 | 描述 |
|---|---|---|---|---|
| AIAttitude | GetFirstCountry |  | Country | 类别：nonconst |
| AIAttitude | GetSecondCountry |  | Country | 类别：nonconst |
| AcceptanceStatus | GetHigherStatus |  | AcceptanceStatus | 类别：nonconst |
| AcceptanceStatus | GetLowerStatus |  | AcceptanceStatus | 类别：nonconst |
| AcceptanceStatusSegment | GetStatus |  | AcceptanceStatus | 类别：nonconst |
| AddWarGoalPanel | AccessCountry |  | Country | 类别：const |
| AddWarGoalPanel | AccessDiplomaticPlay |  | DiplomaticPlay | 类别：const |
| AddWarGoalPanel | GetCountry |  | Country | 类别：nonconst |
| AddWarGoalPanel | GetDiplomaticPlay |  | DiplomaticPlay | 类别：nonconst |
| AgitatorSlot | GetAgitator |  | Character | 类别：nonconst |
| AlertSettingsItem | GetCurrentOption |  | AlertOptionItem | 类别：nonconst |
| Amendment | GetAttachedLaw |  | Law | 类别：nonconst |
| Amendment | GetParentLawType |  | LawType | 类别：nonconst |
| Amendment | GetSponsor |  | InterestGroup | 类别：nonconst |
| Amendment | GetType |  | AmendmentType | 类别：nonconst |
| Amendment | MakeScope |  | Scope |  |
| AmendmentType | GetModifier |  | Modifier | 类别：nonconst |
| AmendmentType | GetParentLawType |  | LawType | 类别：nonconst |
| AmendmentType | GetSponsorModifier |  | Modifier | 类别：nonconst |
| AmendmentType | MakeScope |  | Scope |  |
| Article | GetArticleType |  | ArticleType | 类别：nonconst |
| Article | GetBuildingType |  | BuildingType | 类别：nonconst |
| Article | GetCompany |  | Company | 类别：nonconst |
| Article | GetCountry |  | Country | 类别：nonconst |
| Article | GetFirstOrSourceCountry |  | Country | 类别：nonconst |
| Article | GetGoods |  | Goods | 类别：nonconst |
| Article | GetLaw |  | LawType | 类别：nonconst |
| Article | GetMaintenancePayer |  | Country | 类别：nonconst |
| Article | GetSecondOrTargetCountry |  | Country | 类别：nonconst |
| Article | GetShippingLane |  | ShippingLane | 类别：nonconst |
| Article | GetSourceCountry |  | Country | 类别：nonconst |
| Article | GetState |  | State | 类别：nonconst |
| Article | GetStrategicRegion |  | StrategicRegion | 类别：nonconst |
| Article | GetTargetCountry |  | Country | 类别：nonconst |
| Article | GetTreaty |  | Treaty | 类别：nonconst |
| Article | MakeScope |  | Scope |  |
| ArticleDraft | GetArticleType |  | ArticleType | 类别：nonconst |
| ArticleDraft | GetBuildingType |  | BuildingType | 类别：nonconst |
| ArticleDraft | GetCompany |  | Company | 类别：nonconst |
| ArticleDraft | GetCountry |  | Country | 类别：nonconst |
| ArticleDraft | GetFirstOrSource |  | Country | 类别：nonconst |
| ArticleDraft | GetGoods |  | Goods | 类别：nonconst |
| ArticleDraft | GetLawType |  | LawType | 类别：nonconst |
| ArticleDraft | GetMaintenancePayer |  | Country | 类别：nonconst |
| ArticleDraft | GetSecondOrTarget |  | Country | 类别：nonconst |
| ArticleDraft | GetState |  | State | 类别：nonconst |
| ArticleDraft | GetStrategicRegion |  | StrategicRegion | 类别：nonconst |
| Battle | AccessAttackerBattleParticipant |  | BattleParticipant | 类别：const |
| Battle | AccessAttackerModifier |  | Modifier | 类别：const |
| Battle | AccessDefenderBattleParticipant |  | BattleParticipant | 类别：const |
| Battle | AccessDefenderModifier |  | Modifier | 类别：const |
| Battle | AccessFront |  | Front | 类别：const |
| Battle | GetAttacker |  | Country | 类别：nonconst |
| Battle | GetAttackerCondition |  | BattleCondition | 类别：nonconst |
| Battle | GetAttackerModifier |  | Modifier | 类别：nonconst |
| Battle | GetAttackerSide |  | BattleSide | 类别：nonconst |
| Battle | GetBattleUnitFormation | MilitaryFormation | BattleMilitaryFormation | 类别：nonconst |
| Battle | GetCapturingCountry |  | Country | 类别：nonconst |
| Battle | GetDefender |  | Country | 类别：nonconst |
| Battle | GetDefenderCondition |  | BattleCondition | 类别：nonconst |
| Battle | GetDefenderModifier |  | Modifier | 类别：nonconst |
| Battle | GetDefenderSide |  | BattleSide | 类别：nonconst |
| Battle | GetFront |  | Front | 类别：nonconst |
| Battle | GetInvasion |  | Invasion | 类别：nonconst |
| Battle | GetLoosingProvincesCountry |  | Country | 类别：nonconst |
| Battle | GetLoser |  | Country | 类别：nonconst |
| Battle | GetProvince |  | Province | 类别：nonconst |
| Battle | GetState |  | State | 类别：nonconst |
| Battle | GetWinner |  | Country | 类别：nonconst |
| Battle | MakeScope |  | Scope |  |
| BattleBuildingEntry | GetBuilding |  | Building | 类别：nonconst |
| BattleMarker | GetBattle |  | Battle | 类别：nonconst |
| BattlePanel | GetBattle |  | Battle | 类别：nonconst |
| BattleParticipant | AccessCountry |  | Country | 类别：const |
| BattleParticipant | GetCountry |  | Country | 类别：nonconst |
| BattleParticipantsPanel | GetBattle |  | Battle | 类别：nonconst |
| BattleSide | GetCommander |  | Character | 类别：nonconst |
| BattleSide | GetCountry |  | Country | 类别：nonconst |
| BattleSide | GetFormation |  | MilitaryFormation | 类别：nonconst |
| BattleUnitType | GetCombatUnitType |  | CombatUnitType | 类别：nonconst |
| BrushSettings | Amount |  | BrushFloat |  |
| BrushSettings | Hardness |  | BrushFloat |  |
| BrushSettings | PixelSnap |  | BrushBool |  |
| BrushSettings | Radius |  | BrushFloat |  |
| BrushSettingsDropdown | Settings |  | BrushSettings |  |
| BudgetPanel | GetMapModeList |  | MapModeList | 类别：nonconst |
| Building | AccessModifier |  | Modifier | 类别：const |
| Building | AccessOwnerPopsList |  | PopList | 类别：const |
| Building | AccessPopsList |  | PopList | 类别：const |
| Building | AccessProductionMethod | ProductionMethodGroup | ProductionMethod | 类别：const |
| Building | AccessState |  | State | 类别：const |
| Building | AccessStateRegion |  | StateRegion | 类别：const |
| Building | GetBuildingType |  | BuildingType | 类别：nonconst |
| Building | GetCompany |  | Company | 类别：nonconst |
| Building | GetDefaultOutputGoods |  | Goods | 类别：nonconst |
| Building | GetHQ |  | Hq | 类别：nonconst |
| Building | GetModifier |  | Modifier | 类别：nonconst |
| Building | GetOwner |  | Country | 类别：nonconst |
| Building | GetProducedModifiers |  | Modifier | 类别：nonconst |
| Building | GetProductionMethodGroup | Unknown | ProductionMethodGroup | 类别：nonconst |
| Building | GetState |  | State | 类别：nonconst |
| Building | GetStateRegion |  | StateRegion | 类别：nonconst |
| Building | GetWorstGoodsShortage |  | Goods | 类别：nonconst |
| Building | MakeScope |  | Scope |  |
| BuildingBrowserBuildingTypeItem | GetBuildingType |  | BuildingType | 类别：nonconst |
| BuildingBrowserPanel | GetCountry |  | Country | 类别：nonconst |
| BuildingBrowserPanel | GetMapModeList |  | MapModeList | 类别：nonconst |
| BuildingDetailsPanel | AccessBuilding |  | Building | 类别：const |
| BuildingDetailsPanel | AccessState |  | State | 类别：const |
| BuildingDetailsPanel | GetBuilding |  | Building | 类别：nonconst |
| BuildingDetailsPanel | GetState |  | State | 类别：nonconst |
| BuildingGroup | MakeScope |  | Scope |  |
| BuildingMarker | AccessBuilding |  | Building | 类别：const |
| BuildingMarker | GetBuilding |  | Building | 类别：nonconst |
| BuildingOwnership | GetOwnedBuilding |  | Building | 类别：nonconst |
| BuildingOwnership | GetOwnerBuilding |  | Building | 类别：nonconst |
| BuildingOwnership | GetOwnerCountry |  | Country | 类别：nonconst |
| BuildingPotentialMarker | AccessState |  | State | 类别：const |
| BuildingPotentialMarker | GetBuildingType |  | BuildingType | 类别：nonconst |
| BuildingPotentialMarker | GetState |  | State | 类别：nonconst |
| BuildingProductionMethodsEntry | GetAllSameProductionMethod | Unknown | ProductionMethod | 类别：nonconst |
| BuildingProductionMethodsEntry | GetBuildingType |  | BuildingType | 类别：nonconst |
| BuildingType | GetBuildingGroup |  | BuildingGroup | 类别：nonconst |
| BuildingType | GetBuildingModifier |  | Modifier | 类别：nonconst |
| BuildingType | GetCountryModifier |  | Modifier | 类别：nonconst |
| BuildingType | GetMonopolyCompanyIn | Unknown | Company | 类别：nonconst |
| BuildingType | GetMonopolyCountryIn | Country | Country | 类别：nonconst |
| BuildingType | GetStateModifier |  | Modifier | 类别：nonconst |
| BuildingType | MakeScope |  | Scope |  |
| CanalType | GetBuildingType |  | BuildingType | 类别：nonconst |
| CanalType | GetStateRegion |  | StateRegion | 类别：nonconst |
| CanalType | MakeScope |  | Scope |  |
| ChangeLawPanel | GetLawGroup |  | LawGroup | 类别：nonconst |
| ChangeLawPanel | GetSelectedLaw |  | Law | 类别：nonconst |
| ChangeProductionMethodMenuItem | AccessMethod |  | ProductionMethod | 类别：const |
| ChangeProductionMethodMenuItem | GetProductionMethodGroup |  | ProductionMethodGroup | 类别：nonconst |
| Character | AccessBattle |  | Battle | 类别：const |
| Character | AccessCountry |  | Country | 类别：const |
| Character | AccessCulture |  | Culture | 类别：const |
| Character | AccessInterestGroup |  | InterestGroup | 类别：const |
| Character | AccessReligion |  | Religion | 类别：const |
| Character | GetAcceptanceStatus |  | AcceptanceStatus | 类别：nonconst |
| Character | GetAcceptanceStatusIn | Country | AcceptanceStatus | 类别：nonconst |
| Character | GetAssignedState |  | State | 类别：nonconst |
| Character | GetBattle |  | Battle | 类别：nonconst |
| Character | GetCommanderRank |  | CommanderRank | 类别：nonconst |
| Character | GetCountry |  | Country | 类别：nonconst |
| Character | GetCulture |  | Culture | 类别：nonconst |
| Character | GetFront |  | Front | 类别：nonconst |
| Character | GetHomeCountry |  | Country | 类别：nonconst |
| Character | GetHomeCountryDefinition |  | CountryDefinition | 类别：nonconst |
| Character | GetIdeology |  | Ideology | 类别：nonconst |
| Character | GetInteraction | CharacterInteraction | CharacterInteraction | 类别：nonconst |
| Character | GetInterestGroup |  | InterestGroup | 类别：nonconst |
| Character | GetInvasion |  | Invasion | 类别：nonconst |
| Character | GetMilitaryFormation |  | MilitaryFormation | 类别：nonconst |
| Character | GetNextCommanderRank |  | CommanderRank | 类别：nonconst |
| Character | GetNextOrderType |  | CommanderOrderType | 类别：nonconst |
| Character | GetOrderType |  | CommanderOrderType | 类别：nonconst |
| Character | GetPoliticalMovement |  | PoliticalMovement | 类别：nonconst |
| Character | GetReligion |  | Religion | 类别：nonconst |
| Character | MakeScope |  | Scope |  |
| Character | PredictMovementToJoin | Country | PoliticalMovement |  |
| Character | PredictMovementTypeToStart | Country | PoliticalMovementType |  |
| Chat | GetReceiver |  | Friend | 类别：nonconst |
| ChatNotificationMessage | ChatMessage |  | ChatMessage |  |
| ChatTab | GetChat |  | Chat | 类别：nonconst |
| CityMarker | GetCountry |  | Country | 类别：nonconst |
| CityMarker | GetState |  | State | 类别：nonconst |
| CivilWar | AccessOriginCountry |  | Country | 类别：const |
| CivilWar | AccessPoliticalMovement |  | PoliticalMovement | 类别：const |
| CivilWar | AccessUprisingCountry |  | Country | 类别：const |
| CivilWar | GetLeadingInsurrectionaryIG |  | InterestGroup | 类别：nonconst |
| CivilWar | GetOriginCountry |  | Country | 类别：nonconst |
| CivilWar | GetPoliticalMovement |  | PoliticalMovement | 类别：nonconst |
| CivilWar | GetUprisingCountry |  | Country | 类别：nonconst |
| CivilWar | MakeScope |  | Scope |  |
| ColonyMarker | AccessState |  | State | 类别：const |
| ColonyMarker | GetState |  | State | 类别：nonconst |
| CombatUnit | GetBattle |  | Battle | 类别：nonconst |
| CombatUnit | GetBuilding |  | Building | 类别：nonconst |
| CombatUnit | GetCountry |  | Country | 类别：nonconst |
| CombatUnit | GetCulture |  | Culture | 类别：nonconst |
| CombatUnit | GetFront |  | Front | 类别：nonconst |
| CombatUnit | GetMilitaryFormation |  | MilitaryFormation | 类别：nonconst |
| CombatUnit | GetUnitType |  | CombatUnitType | 类别：nonconst |
| CombatUnit | MakeScope |  | Scope |  |
| CombatUnitType | GetBattleModifier |  | Modifier | 类别：nonconst |
| CombatUnitType | GetFormationModifier |  | Modifier | 类别：nonconst |
| CombatUnitType | GetGroup |  | CombatUnitGroup | 类别：nonconst |
| CombatUnitType | GetUpkeepModifier |  | Modifier | 类别：nonconst |
| CombatUnitType | MakeScope |  | Scope |  |
| CommanderOrderType | GetModifier |  | Modifier | 类别：nonconst |
| CommanderOrderType | MakeScope |  | Scope |  |
| CommanderPanel | AccessCharacter |  | Character | 类别：const |
| CommanderPanel | GetCharacter |  | Character | 类别：nonconst |
| Company | AccessCompanyType |  | CompanyType | 类别：const |
| Company | AccessExecutive |  | Character | 类别：const |
| Company | GetBuilding |  | Building | 类别：nonconst |
| Company | GetCompanyType |  | CompanyType | 类别：nonconst |
| Company | GetCountry |  | Country | 类别：nonconst |
| Company | GetEstablishmentDate |  | Date | 类别：nonconst |
| Company | GetExecutive |  | Character | 类别：nonconst |
| Company | GetState |  | State | 类别：nonconst |
| Company | MakeScope |  | Scope |  |
| CompanyChangeNamePopup | GetCompany |  | Company | 类别：nonconst |
| CompanyCharter | GetBuildingType |  | BuildingType | 类别：nonconst |
| CompanyCharter | GetStateRegion |  | StateRegion | 类别：nonconst |
| CompanyCharter | GetType |  | CompanyCharterType | 类别：nonconst |
| CompanyPanel | GetCompany |  | Company | 类别：nonconst |
| CompanyType | GetPotentialState |  | State | 类别：nonconst |
| CompanyType | GetProsperityModifier |  | Modifier | 类别：nonconst |
| CompanyType | MakeScope |  | Scope |  |
| ConstructionPanel | GetCountry |  | Country | 类别：nonconst |
| ConstructionQueueElement | AccessBuilding |  | Building | 类别：const |
| ConstructionQueueElement | AccessState |  | State | 类别：const |
| ConstructionQueueElement | GetBuilding |  | Building | 类别：nonconst |
| ConstructionQueueElement | GetInvestorBuilding |  | Building | 类别：nonconst |
| ConstructionQueueElement | GetInvestorBuildingType |  | BuildingType | 类别：nonconst |
| ConstructionQueueElement | GetInvestorCountry |  | Country | 类别：nonconst |
| ConstructionQueueElement | GetInvestorState |  | State | 类别：nonconst |
| ConstructionQueueElement | GetState |  | State | 类别：nonconst |
| ContextualDiplomaticActionType | AccessCountry |  | Country | 类别：const |
| ContextualDiplomaticActionType | GetCountry |  | Country | 类别：nonconst |
| ContextualDiplomaticActionType | GetDiplomaticActionType |  | DiplomaticActionType | 类别：nonconst |
| ContextualDiplomaticPact | AccessDiplomaticPact |  | DiplomaticPact | 类别：const |
| ContextualDiplomaticPact | GetContextCountry |  | Country | 类别：nonconst |
| ContextualDiplomaticPact | GetDiplomaticActionType |  | DiplomaticActionType | 类别：nonconst |
| ContextualDiplomaticPact | GetDiplomaticPact |  | DiplomaticPact | 类别：nonconst |
| ContextualDiplomaticPact | GetOtherCountry |  | Country | 类别：nonconst |
| Country | AccessActiveLawFromGroup | LawGroup | Law | 类别：const |
| Country | AccessCapital |  | State | 类别：const |
| Country | AccessCurrentlyResearchedTechnology |  | Technology | 类别：const |
| Country | AccessDefinition |  | CountryDefinition | 类别：const |
| Country | AccessFirstMarket |  | Market | 类别：const |
| Country | AccessGovernment |  | GovernmentType | 类别：const |
| Country | AccessHeaviestJournalEntry |  | JournalEntry | 类别：const |
| Country | AccessHeir |  | Character | 类别：const |
| Country | AccessLawBeingEnacted |  | Law | 类别：const |
| Country | AccessModifier |  | Modifier | 类别：const |
| Country | AccessOverlord |  | Country | 类别：const |
| Country | AccessPowerBloc |  | PowerBloc | 类别：const |
| Country | AccessRuler |  | Character | 类别：const |
| Country | AccessStateReligion |  | Religion | 类别：const |
| Country | AccessTopOverlord |  | Country | 类别：const |
| Country | CalcLibertyDesireLevel |  | LibertyDesireLevel |  |
| Country | GetActiveLawFrom | Unknown | Law | 类别：nonconst |
| Country | GetActiveLawFromGroup | LawGroup | Law | 类别：nonconst |
| Country | GetAttitudeTowards | Country | AIAttitude | 类别：nonconst |
| Country | GetCapital |  | State | 类别：nonconst |
| Country | GetCurrentlyResearchedTechnology |  | Technology | 类别：nonconst |
| Country | GetDefinition |  | CountryDefinition | 类别：nonconst |
| Country | GetDiplomaticAction | Unknown Unknown | DiplomaticAction | 类别：nonconst |
| Country | GetDiplomaticActionWithStates | Unknown Unknown Unknown Unknown | DiplomaticAction | 类别：nonconst |
| Country | GetElection |  | Election | 类别：nonconst |
| Country | GetFirstPrimaryCulture |  | Culture | 类别：nonconst |
| Country | GetFlag |  | CoatOfArms | 类别：nonconst |
| Country | GetFoodSecurity |  | FoodSecurity | 类别：nonconst |
| Country | GetGovernment |  | GovernmentType | 类别：nonconst |
| Country | GetGovernmentLegitimacyLevel |  | LegitimacyLevel | 类别：nonconst |
| Country | GetHeir |  | Character | 类别：nonconst |
| Country | GetInterestGroupOfType | InterestGroup | InterestGroup | 类别：nonconst |
| Country | GetJournalEntry | Unknown | JournalEntry | 类别：nonconst |
| Country | GetLawBeingEnacted |  | Law | 类别：nonconst |
| Country | GetLawBeingEnactedFromGroup | Unknown | Law | 类别：nonconst |
| Country | GetMarket |  | Market | 类别：nonconst |
| Country | GetModifier |  | Modifier | 类别：nonconst |
| Country | GetMonopolyCountryOnBuildingType | BuildingType | Country | 类别：nonconst |
| Country | GetNegotiatingInterestGroup |  | InterestGroup | 类别：nonconst |
| Country | GetObjective |  | Objective | 类别：nonconst |
| Country | GetOtherPowerBlocWithHighestLeverage | Unknown | PowerBloc | 类别：nonconst |
| Country | GetOverlord |  | Country | 类别：nonconst |
| Country | GetOwningCompany |  | Company | 类别：nonconst |
| Country | GetPlayer |  | Player | 类别：nonconst |
| Country | GetPowerBloc |  | PowerBloc | 类别：nonconst |
| Country | GetPowerBlocWithHighestLeverage |  | PowerBloc | 类别：nonconst |
| Country | GetPreviousAttitudeTowards | Country | AIAttitude | 类别：nonconst |
| Country | GetRankModifier |  | Modifier | 类别：nonconst |
| Country | GetRuler |  | Character | 类别：nonconst |
| Country | GetSampleLowerStrataPop |  | Pop | 类别：nonconst |
| Country | GetSampleLowerStrataPopForCulture | Unknown | Pop | 类别：nonconst |
| Country | GetSampleMiddleStrataPop |  | Pop | 类别：nonconst |
| Country | GetSampleMiddleStrataPopForCulture | Unknown | Pop | 类别：nonconst |
| Country | GetSampleUpperStrataPop |  | Pop | 类别：nonconst |
| Country | GetSampleUpperStrataPopForCulture | Unknown | Pop | 类别：nonconst |
| Country | GetSelectedLaw |  | Law | 类别：nonconst |
| Country | GetSocialHierarchy |  | SocialHierarchy | 类别：nonconst |
| Country | GetSpecialSocialHierarchy |  | SocialHierarchy | 类别：nonconst |
| Country | GetStateReligion |  | Religion | 类别：nonconst |
| Country | GetSubjectPact |  | DiplomaticPact | 类别：nonconst |
| Country | GetSubjectType |  | SubjectType | 类别：nonconst |
| Country | GetTopOverlord |  | Country | 类别：nonconst |
| Country | MakeScope |  | Scope |  |
| CountryCreation | GetCapital |  | StateRegion | 类别：nonconst |
| CountryCreation | GetDefinition |  | CountryDefinition | 类别：nonconst |
| CountryCreation | MakeScope |  | Scope |  |
| CountryDefinition | GetBaseFlag |  | CoatOfArms | 类别：nonconst |
| CountryDefinition | GetFlag | CString | CoatOfArms | 类别：nonconst |
| CountryDefinition | GetPrimaryCulture |  | Culture | 类别：nonconst |
| CountryDefinition | MakeScope |  | Scope |  |
| CountryFormation | GetDefinition |  | CountryDefinition | 类别：nonconst |
| CountryFormation | GetSupportedCandidateCountry | Country | Country | 类别：nonconst |
| CountryFormation | MakeScope |  | Scope |  |
| CountryFormationPanel | AccessCountryFormation |  | CountryFormation | 类别：const |
| CountryFormationPanel | GetCountryFormation |  | CountryFormation | 类别：nonconst |
| CountryMarker | GetCountry |  | Country | 类别：nonconst |
| CountryPanel | GetCountry |  | Country | 类别：nonconst |
| CountryPanel | GetMapModeList |  | MapModeList | 类别：nonconst |
| CountryTrendPair | GetCountry |  | Country | 类别：nonconst |
| CulturalCommunity | GetCulture |  | Culture | 类别：nonconst |
| CulturalCommunity | GetState |  | State | 类别：nonconst |
| CulturalCommunity | MakeScope |  | Scope |  |
| Culture | AccessReligion |  | Religion | 类别：const |
| Culture | GetHeritageTrait |  | DiscriminationTrait | 类别：nonconst |
| Culture | GetLanguageTrait |  | DiscriminationTrait | 类别：nonconst |
| Culture | GetReligion |  | Religion | 类别：nonconst |
| Culture | GetSampleGlobalLowerStrataPop |  | Pop | 类别：nonconst |
| Culture | GetSampleGlobalMiddleStrataPop |  | Pop | 类别：nonconst |
| Culture | GetSampleGlobalUpperStrataPop |  | Pop | 类别：nonconst |
| Culture | MakeScope |  | Scope |  |
| CultureCasualtyStatistics | GetCulture |  | Culture | 类别：nonconst |
| CultureInfoPanel | AccessCulture |  | Culture | 类别：const |
| CultureInfoPanel | AccessPopsList |  | PopList | 类别：const |
| CultureInfoPanel | GetCulture |  | Culture | 类别：nonconst |
| Decision | MakeScope |  | Scope |  |
| Decree | GetCountry |  | Country | 类别：nonconst |
| Decree | GetModifier |  | Modifier | 类别：nonconst |
| Decree | GetState |  | State | 类别：nonconst |
| Decree | GetType |  | DecreeType | 类别：nonconst |
| Decree | MakeScope |  | Scope |  |
| DecreeMarker | AccessDecree |  | Decree | 类别：const |
| DecreeMarker | GetDecree |  | Decree | 类别：nonconst |
| DecreeType | GetModifier |  | Modifier | 类别：nonconst |
| DiplomaticAction | AccessFirstCountry |  | Country | 类别：const |
| DiplomaticAction | AccessFirstState |  | State | 类别：const |
| DiplomaticAction | AccessSecondCountry |  | Country | 类别：const |
| DiplomaticAction | AccessSecondState |  | State | 类别：const |
| DiplomaticAction | GetFirstCountry |  | Country | 类别：nonconst |
| DiplomaticAction | GetFirstState |  | State | 类别：nonconst |
| DiplomaticAction | GetSecondCountry |  | Country | 类别：nonconst |
| DiplomaticAction | GetSecondState |  | State | 类别：nonconst |
| DiplomaticAction | GetType |  | DiplomaticActionType | 类别：nonconst |
| DiplomaticAction | MakeScope |  | Scope |  |
| DiplomaticActionType | GetFirstModifier |  | Modifier | 类别：nonconst |
| DiplomaticActionType | GetModifyPactActionType |  | DiplomaticActionType | 类别：nonconst |
| DiplomaticActionType | GetSecondModifier |  | Modifier | 类别：nonconst |
| DiplomaticActionWindow | AccessDiplomaticAction |  | DiplomaticAction | 类别：const |
| DiplomaticActionWindow | AccessFirstState |  | State | 类别：const |
| DiplomaticActionWindow | AccessSecondState |  | State | 类别：const |
| DiplomaticActionWindow | AccessStateSelectionTarget |  | Country | 类别：const |
| DiplomaticActionWindow | GetDiplomaticAction |  | DiplomaticAction | 类别：nonconst |
| DiplomaticActionWindow | GetFirstState |  | State | 类别：nonconst |
| DiplomaticActionWindow | GetSecondState |  | State | 类别：nonconst |
| DiplomaticActionWindow | GetStateSelectionTarget |  | Country | 类别：nonconst |
| DiplomaticCatalyst | AccessDiplomaticCatalystType |  | DiplomaticCatalystType | 类别：const |
| DiplomaticCatalyst | GetCountry |  | Country | 类别：nonconst |
| DiplomaticCatalyst | GetDiplomaticCatalystType |  | DiplomaticCatalystType | 类别：nonconst |
| DiplomaticCatalyst | GetOccuranceDate |  | Date | 类别：nonconst |
| DiplomaticCatalyst | GetTargetCountry |  | Country | 类别：nonconst |
| DiplomaticCatalyst | MakeScope |  | Scope |  |
| DiplomaticCatalystCategory | MakeScope |  | Scope |  |
| DiplomaticCatalystType | GetCategory |  | DiplomaticCatalystCategory | 类别：nonconst |
| DiplomaticCatalystType | MakeScope |  | Scope |  |
| DiplomaticDemand | GetDemandedWarGoal |  | WarGoalDraft | 类别：nonconst |
| DiplomaticDemand | GetDiplomaticPlayType |  | DiplomaticPlayType | 类别：nonconst |
| DiplomaticDemand | GetSender |  | Country | 类别：nonconst |
| DiplomaticDemand | GetTarget |  | Country | 类别：nonconst |
| DiplomaticDemand | MakeScope |  | Scope |  |
| DiplomaticOverviewPanel | GetMapModeList |  | MapModeList | 类别：nonconst |
| DiplomaticPact | GetDiplomaticAction |  | DiplomaticAction | 类别：nonconst |
| DiplomaticPact | GetDiplomaticActionType |  | DiplomaticActionType | 类别：nonconst |
| DiplomaticPact | GetFirstCountry |  | Country | 类别：nonconst |
| DiplomaticPact | GetSecondCountry |  | Country | 类别：nonconst |
| DiplomaticPact | MakeScope |  | Scope |  |
| DiplomaticPlay | AccessInitiator |  | Country | 类别：const |
| DiplomaticPlay | AccessTarget |  | Country | 类别：const |
| DiplomaticPlay | AccessWar |  | War | 类别：const |
| DiplomaticPlay | GetAcceptedSway | Country | Sway | 类别：nonconst |
| DiplomaticPlay | GetDiplomaticPlayType |  | DiplomaticPlayType | 类别：nonconst |
| DiplomaticPlay | GetIncomingSway | Country Country | Sway | 类别：nonconst |
| DiplomaticPlay | GetIncomingSwayByTargetAndSwayer | Unknown Unknown | Sway | 类别：nonconst |
| DiplomaticPlay | GetInitiator |  | Country | 类别：nonconst |
| DiplomaticPlay | GetInterestMarker | Country | Interest | 类别：nonconst |
| DiplomaticPlay | GetOutgoingSway | Unknown Unknown | Sway | 类别：nonconst |
| DiplomaticPlay | GetStrategicRegion |  | StrategicRegion | 类别：nonconst |
| DiplomaticPlay | GetTarget |  | Country | 类别：nonconst |
| DiplomaticPlay | GetWar |  | War | 类别：nonconst |
| DiplomaticPlay | MakeScope |  | Scope |  |
| DiplomaticPlayConfirmation | GetCountryDefinition |  | CountryDefinition | 类别：nonconst |
| DiplomaticPlayConfirmation | GetInitiatorCountry |  | Country | 类别：nonconst |
| DiplomaticPlayConfirmation | GetTargetCountry |  | Country | 类别：nonconst |
| DiplomaticPlayConfirmation | GetTargetState |  | State | 类别：nonconst |
| DiplomaticPlayConfirmation | GetType |  | DiplomaticPlayType | 类别：nonconst |
| DiplomaticPlayPanel | AccessDiplomaticPlay |  | DiplomaticPlay | 类别：const |
| DiplomaticPlayPanel | GetDiplomaticPlay |  | DiplomaticPlay | 类别：nonconst |
| DiplomaticPlayType | GetWarGoalType |  | WarGoalType | 类别：nonconst |
| DiplomaticPlayType | MakeScope |  | Scope |  |
| DiplomaticRelations | GetCountryWhichNotOwesObligation |  | Country | 类别：nonconst |
| DiplomaticRelations | GetCountryWhichOwesObligation |  | Country | 类别：nonconst |
| DiplomaticRelations | GetFirstCountry |  | Country | 类别：nonconst |
| DiplomaticRelations | GetSecondCountry |  | Country | 类别：nonconst |
| DiplomaticRelations | MakeScope |  | Scope |  |
| DiscriminationTrait | GetTraitGroup |  | DiscriminationTraitGroup | 类别：nonconst |
| DockableLayoutManager | AccessActiveLayout |  | DockableLayout | 类别：const |
| DockableLayoutManager | AccessLayoutSearchList |  | ToolPropertySearchList | 类别：const |
| DockableLayoutManager | AccessSelectedLayout |  | DockableLayout | 类别：const |
| EditorSettingsWindow | AccessActivePage |  | EditorSettingsPage | 类别：const |
| Election | GetCountry |  | Country | 类别：nonconst |
| ElectionPanel | GetElection |  | Election | 类别：nonconst |
| EmployeeTransfer | GetNewEmployment |  | BuildingType | 类别：nonconst |
| EmployeeTransfer | GetNewPopType |  | PopType | 类别：nonconst |
| EmployeeTransfer | GetOldEmployment |  | BuildingType | 类别：nonconst |
| EmployeeTransfer | GetOldPopType |  | PopType | 类别：nonconst |
| Encyclopedia | AccessCurrentPage |  | EncyclopediaPage | 类别：const |
| Encyclopedia | GetAllPage |  | EncyclopediaPage | 类别：nonconst |
| Encyclopedia | GetCurrentPage |  | EncyclopediaPage | 类别：nonconst |
| EncyclopediaEntryView | Get |  | EncyclopediaEntry |  |
| EntityEditor | Entity |  | ViewerEntity |  |
| Event | AccessState |  | State | 类别：const |
| Event | GetIcon | CString | EventIcon | 类别：nonconst |
| Event | GetState |  | State | 类别：nonconst |
| Event | GetTopScope |  | TopScope | 类别：nonconst |
| EventIcon | GetCharacter |  | Character | 类别：nonconst |
| EventIcon | GetCountry |  | Country | 类别：nonconst |
| EventMarker | AccessAnyEvent |  | Event | 类别：const |
| EventMarker | GetAnyEvent |  | Event | 类别：nonconst |
| EventTargetSetupContext | AccessVariableLists |  | VariableListStore | 类别：const |
| EventTargetSetupContext | AccessVariables |  | VariableStore | 类别：const |
| EventWindow | AccessEvent |  | Event | 类别：const |
| EventWindow | GetEvent |  | Event | 类别：nonconst |
| EyeDropper | GetHoverSample |  | MaterialsSample | 类别：nonconst |
| EyeDropperPackedSample | GetSample |  | MaterialEntry | 类别：nonconst |
| FeedMessageItem | GetPlayerMessageItem |  | PlayerMessageItem | 类别：nonconst |
| FeedMessageItem | GetTimeoutTimer |  | PieTimer | 类别：nonconst |
| FoodSecurityFilter | GetFoodSecurity |  | FoodSecurity | 类别：nonconst |
| FoodSecurityFilter | GetFoodSecurityCountryOrMarket |  | FoodSecurity | 类别：nonconst |
| FoodSecurityFilter | GetMarket |  | Market | 类别：nonconst |
| FoodSecurityFilter | GetSelectedCountry |  | Country | 类别：nonconst |
| FoodSecurityFilter | GetSelectedState |  | State | 类别：nonconst |
| FormationMarker | GetFirstMilitaryFormation |  | MilitaryFormation | 类别：nonconst |
| FormationPanel | GetFormation |  | MilitaryFormation | 类别：nonconst |
| Front | AccessDiplomaticPlay |  | DiplomaticPlay | 类别：const |
| Front | GetInitiatorSide |  | FrontSide | 类别：nonconst |
| Front | GetLeftSide |  | FrontSide | 类别：nonconst |
| Front | GetPlayerEnemySide |  | FrontSide | 类别：nonconst |
| Front | GetPlayerSide |  | FrontSide | 类别：nonconst |
| Front | GetRightSide |  | FrontSide | 类别：nonconst |
| Front | GetTargetSide |  | FrontSide | 类别：nonconst |
| Front | MakeScope |  | Scope |  |
| FrontEndLoadView | GetContinueSave |  | SaveGameItem | 类别：nonconst |
| FrontEndLoadView | GetSelectedSavegame |  | SaveGameItem | 类别：nonconst |
| FrontEndMainView | AccessLoadView |  | FrontEndLoadView | 类别：const |
| FrontMarker | GetFront |  | Front | 类别：nonconst |
| FrontMovementMarker | AccessFront |  | Front | 类别：const |
| FrontMovementMarker | GetFront |  | Front | 类别：nonconst |
| FrontPanel | AccessFront |  | Front | 类别：const |
| FrontPanel | GetFront |  | Front | 类别：nonconst |
| FrontSide | GetCountry |  | Country | 类别：nonconst |
| FrontSide | GetFront |  | Front | 类别：nonconst |
| GUIAchievement | GetAchievement |  | Achievement | 类别：nonconst |
| GameMpSetup | GetSelectedSaveGame |  | SaveGameItem | 类别：nonconst |
| GameRuleSetting | GetGameRule |  | GameRule | 类别：nonconst |
| GameSetup | GetSelectedObjective |  | ObjectiveType | 类别：nonconst |
| GameSetup | GetSelectedTag |  | CountryDefinition | 类别：nonconst |
| GeographicRegion | MakeScope |  | Scope |  |
| Goods | AccessMarket |  | Market | 类别：const |
| Goods | AccessState |  | State | 类别：const |
| Goods | GetBaseGoods |  | Goods | 类别：nonconst |
| Goods | GetMarket |  | Market | 类别：nonconst |
| Goods | GetMarketWithLargestExportShare |  | Market | 类别：nonconst |
| Goods | GetMarketWithLargestImportShare |  | Market | 类别：nonconst |
| Goods | GetState |  | State | 类别：nonconst |
| Goods | MakeScope |  | Scope |  |
| Goods | WithMarketContext | Market | Goods |  |
| Goods | WithStateContext | State | Goods |  |
| GoodsExpenseItem | GetGoods |  | Goods | 类别：nonconst |
| GoodsList | GetState |  | State | 类别：nonconst |
| GoodsLocalPricesPanel | AccessGoods |  | Goods | 类别：const |
| GoodsLocalPricesPanel | GetGoods |  | Goods | 类别：nonconst |
| GoodsPanel | GetGoods |  | Goods | 类别：nonconst |
| GoodsPanel | GetMapModeList |  | MapModeList | 类别：nonconst |
| GoodsPanel | GetMarketGoods |  | MarketGoods | 类别：nonconst |
| GoodsPanelValue | GetBuilding |  | Building | 类别：nonconst |
| GoodsPanelValue | GetBuildingType |  | BuildingType | 类别：nonconst |
| GoodsPanelValue | GetMarket |  | Market | 类别：nonconst |
| GoodsPanelValue | GetState |  | State | 类别：nonconst |
| GoodsProductionInfo | AccessGoods |  | Goods | 类别：const |
| GoodsStatePanel | GetGoods |  | Goods | 类别：nonconst |
| GoodsStatePanel | GetMapModeList |  | MapModeList | 类别：nonconst |
| GoodsUsagePanel | AccessGoods |  | Goods | 类别：const |
| GoodsUsagePanel | GetGoods |  | Goods | 类别：nonconst |
| GoodsWorldMarketPanel | GetBaseGoods |  | Goods | 类别：nonconst |
| GoodsWorldMarketPanel | GetGoods |  | Goods | 类别：nonconst |
| GoodsWorldMarketPanel | GetMapModeList |  | MapModeList | 类别：nonconst |
| GraphPanel | AccessAnimationEditorSearch |  | NodeEditorSearch | 类别：const |
| GraphPanel | AccessMetadataWindow |  | MetadataWindow | 类别：const |
| GraphPanel | GetMetadataWindow |  | MetadataWindow | 类别：nonconst |
| GuiGameRule | GetRule |  | GameRule | 类别：nonconst |
| GuiGameRule | GetSetting |  | GameRuleSetting | 类别：nonconst |
| GuiGameRulePreset | GetSettingForRule | Unknown | GameRuleSetting | 类别：nonconst |
| HQMarker | GetHQ |  | Hq | 类别：nonconst |
| HQMovementMarker | GetHQ |  | Hq | 类别：nonconst |
| HarvestCondition | GetArea |  | HarvestConditionArea | 类别：nonconst |
| HarvestCondition | GetState |  | State | 类别：nonconst |
| HarvestCondition | GetType |  | HarvestConditionType | 类别：nonconst |
| HarvestCondition | MakeScope |  | Scope |  |
| HarvestConditionArea | GetEpicenter |  | HarvestCondition | 类别：nonconst |
| HarvestConditionArea | GetEpicenterRegion |  | StateRegion | 类别：nonconst |
| HarvestConditionArea | GetType |  | HarvestConditionType | 类别：nonconst |
| HarvestConditionArea | MakeScope |  | Scope |  |
| HarvestConditionType | MakeScope |  | Scope |  |
| HomelandMarker | GetCulture |  | Culture | 类别：nonconst |
| HomelandMarker | GetState |  | State | 类别：nonconst |
| Hq | GetCountry |  | Country | 类别：nonconst |
| Hq | GetStrategicRegion |  | StrategicRegion | 类别：nonconst |
| Hq | MakeScope |  | Scope |  |
| Ideology | MakeScope |  | Scope |  |
| ImportantAlert | GetAlert |  | Alert | 类别：nonconst |
| Institution | AccessModifier |  | Modifier | 类别：const |
| Institution | GetCountry |  | Country | 类别：nonconst |
| Institution | GetModifier |  | Modifier | 类别：nonconst |
| Institution | MakeScope |  | Scope |  |
| InstitutionType | GetModifier |  | Modifier | 类别：nonconst |
| InstitutionType | MakeScope |  | Scope |  |
| Interest | GetOwner |  | Country | 类别：nonconst |
| Interest | GetStrategicRegion |  | StrategicRegion | 类别：nonconst |
| Interest | MakeScope |  | Scope |  |
| InterestGroup | AccessCountry |  | Country | 类别：const |
| InterestGroup | AccessLeader |  | Character | 类别：const |
| InterestGroup | AccessModifier |  | Modifier | 类别：const |
| InterestGroup | GetCountry |  | Country | 类别：nonconst |
| InterestGroup | GetLeader |  | Character | 类别：nonconst |
| InterestGroup | GetLeaderIdeology |  | Ideology | 类别：nonconst |
| InterestGroup | GetModifier |  | Modifier | 类别：nonconst |
| InterestGroup | GetParty |  | Party | 类别：nonconst |
| InterestGroup | GetPartyAffiliationHighest |  | Party | 类别：nonconst |
| InterestGroup | GetPopWithIG | Pop | PopWithIG | 类别：nonconst |
| InterestGroup | MakeScope |  | Scope |  |
| InterestGroupAndTraitPair | AccessInterestGroup |  | InterestGroup | 类别：const |
| InterestGroupAndTraitPair | GetInterestGroup |  | InterestGroup | 类别：nonconst |
| InterestGroupAndTraitPair | GetTrait |  | InterestGroupTrait | 类别：nonconst |
| InterestGroupMarker | AccessInterestGroup |  | InterestGroup | 类别：const |
| InterestGroupMarker | GetInterestGroup |  | InterestGroup | 类别：nonconst |
| InterestGroupPanel | AccessInterestGroup |  | InterestGroup | 类别：const |
| InterestGroupPanel | AccessPopsList |  | PopList | 类别：const |
| InterestGroupPanel | GetInterestGroup |  | InterestGroup | 类别：nonconst |
| InterestGroupTrait | MakeScope |  | Scope |  |
| InterestingCountryItem | GetCountry |  | Country | 类别：nonconst |
| InterestingCountryItem | GetSetting |  | InterestingCountrySetting | 类别：nonconst |
| Invasion | GetArmy |  | MilitaryFormation | 类别：nonconst |
| Invasion | GetDefenderHQ |  | Hq | 类别：nonconst |
| Invasion | GetEnemyState |  | State | 类别：nonconst |
| Invasion | GetFleet |  | MilitaryFormation | 类别：nonconst |
| Invasion | GetFront |  | Front | 类别：nonconst |
| Invasion | GetInvadedCountry |  | Country | 类别：nonconst |
| Invasion | GetInvaderCountry |  | Country | 类别：nonconst |
| Invasion | GetSeaNode |  | Province | 类别：nonconst |
| Invasion | GetSourceState |  | State | 类别：nonconst |
| Invasion | GetTargetState |  | State | 类别：nonconst |
| Invasion | MakeScope |  | Scope |  |
| InvasionMarker | GetInvasion |  | Invasion | 类别：nonconst |
| InvasionPanel | GetInvasion |  | Invasion | 类别：nonconst |
| InvasionPlannerPopup | GetSlowestArmy |  | MilitaryFormation | 类别：nonconst |
| InvasionPlannerPopup | GetSlowestFleet |  | MilitaryFormation | 类别：nonconst |
| InvasionPlannerPopup | GetSourceState |  | State | 类别：nonconst |
| InvasionPlannerPopup | GetTargetState |  | State | 类别：nonconst |
| JominiGameRules | AccessNamedGameRule | CString | GuiGameRule | 类别：const |
| JominiGameRules | GetSelectedPreset |  | GuiGameRulePreset | 类别：nonconst |
| JominiNotification | GetDate |  | Date | 类别：nonconst |
| JominiNotification | SetupDataContexts | PdxGuiWidget | NotificationDummyContext |  |
| JominiSettingsWindow | AccessActivePage |  | SettingsPage | 类别：const |
| JournalEntry | AccessModifier |  | Modifier | 类别：const |
| JournalEntry | GetBuildingTarget |  | Building | 类别：nonconst |
| JournalEntry | GetCountry |  | Country | 类别：nonconst |
| JournalEntry | GetModifier |  | Modifier | 类别：nonconst |
| JournalEntry | GetTarget |  | Scope | 类别：nonconst |
| JournalEntry | GetTopScope |  | TopScope | 类别：nonconst |
| JournalEntry | GetType |  | JournalEntryType | 类别：nonconst |
| JournalEntry | MakeScope |  | Scope |  |
| JournalEntryPanel | AccessJournalEntry |  | JournalEntry | 类别：const |
| JournalEntryPanel | GetJournalEntry |  | JournalEntry | 类别：nonconst |
| JournalEntryType | GetGroup |  | JournalEntryGroup | 类别：nonconst |
| Law | GetActiveGroupLaw |  | Law | 类别：nonconst |
| Law | GetCheckpointEndDate |  | Date | 类别：nonconst |
| Law | GetCountry |  | Country | 类别：nonconst |
| Law | GetEnactmentLastCheckpointDate |  | Date | 类别：nonconst |
| Law | GetGroup |  | LawGroup | 类别：nonconst |
| Law | GetInstitution |  | Institution | 类别：nonconst |
| Law | GetInstitutionModifier |  | Modifier | 类别：nonconst |
| Law | GetInstitutionType |  | InstitutionType | 类别：nonconst |
| Law | GetLawType |  | LawType | 类别：nonconst |
| Law | MakeScope |  | Scope |  |
| LawGroup | GetCurrentlyActive |  | Law | 类别：nonconst |
| LawGroup | GetCurrentlyEnacting |  | Law | 类别：nonconst |
| LawGroup | GetFirstInstitutionType |  | InstitutionType | 类别：nonconst |
| LawType | GetGroup |  | LawGroup | 类别：nonconst |
| LawType | GetParentLawType |  | LawType | 类别：nonconst |
| LawType | MakeScope |  | Scope |  |
| LayerTreeItem | GetEntry |  | Type | 类别：nonconst |
| LensOption | GetDecreeType |  | DecreeType | 类别：nonconst |
| LensOption | GetDiplomaticAction |  | DiplomaticAction | 类别：nonconst |
| LensToolbar | GetCurrentTab |  | LensTab | 类别：nonconst |
| LoadIngameWindow | GetSelectedSavegame |  | SaveGameItem | 类别：nonconst |
| LoadingScreenManager | GetConceptTip |  | GameConceptType | 类别：nonconst |
| LobbyPlayer | GetLobbyView |  | LobbyView | 类别：nonconst |
| LobbyPlayer | GetPlayable |  | Playable | 类别：nonconst |
| LobbyView | AccessLocalPlayer |  | LobbyPlayer | 类别：const |
| LobbyView | AccessSelectedPlayable |  | Playable | 类别：const |
| LobbyView | GetSelectedPlayable |  | Playable | 类别：nonconst |
| LobbyView | GetServerInfo |  | ServerInformation | 类别：nonconst |
| LogViewer | GetLastLogEntry |  | LogViewerEntry | 类别：nonconst |
| LogViewer | GetSelectedLogEntry |  | LogViewerEntry | 类别：nonconst |
| MapContentEditorViewport | GetTooltip |  | GuiEditorTooltip | 类别：nonconst |
| MapEditor | AccessUndoHistoryViewerClient |  | UndoHistoryViewerClient | 类别：const |
| MapEditor | GetUndoHistoryViewerClient |  | UndoHistoryViewerClient | 类别：nonconst |
| MapEditorGui | AccessLogViewer |  | LogViewer | 类别：const |
| MapListActivateConscriptionCenterOption | GetHQ |  | Hq | 类别：nonconst |
| MapListActivateConscriptionCenterOption | GetMilitaryFormation |  | MilitaryFormation | 类别：nonconst |
| MapListActivateConscriptionCenterOption | GetState |  | State | 类别：nonconst |
| MapListBuildingOption | AccessBuilding |  | Building | 类别：const |
| MapListBuildingOption | AccessMilitaryFormation |  | MilitaryFormation | 类别：const |
| MapListBuildingOption | AccessState |  | State | 类别：const |
| MapListBuildingOption | GetBuilding |  | Building | 类别：nonconst |
| MapListBuildingOption | GetCombatUnitType |  | CombatUnitType | 类别：nonconst |
| MapListBuildingOption | GetMilitaryFormation |  | MilitaryFormation | 类别：nonconst |
| MapListBuildingOption | GetState |  | State | 类别：nonconst |
| MapListBuildingPanel | GetBuildingType |  | BuildingType | 类别：nonconst |
| MapListColonyOption | GetStateRegion |  | StateRegion | 类别：nonconst |
| MapListCountryOption | GetCountry |  | Country | 类别：nonconst |
| MapListDecreeOption | GetState |  | State | 类别：nonconst |
| MapListDecreePanel | GetDecreeType |  | DecreeType | 类别：nonconst |
| MapListDeployMilitaryFormationToFrontOption | GetFront |  | Front | 类别：nonconst |
| MapListDiploActionOption | GetCountry |  | Country | 类别：nonconst |
| MapListDiploActionOption | GetDiplomaticAction |  | DiplomaticAction | 类别：nonconst |
| MapListHarvestConditionOption | GetArea |  | HarvestConditionArea | 类别：nonconst |
| MapListInterestGroupOption | AccessInterestGroup |  | InterestGroup | 类别：const |
| MapListInterestGroupOption | GetInterestGroup |  | InterestGroup | 类别：nonconst |
| MapListMarketOption | AccessMarket |  | Market | 类别：const |
| MapListMarketOption | GetMarket |  | Market | 类别：nonconst |
| MapListOption | AccessBuildingData |  | MapListBuildingOption | 类别：const |
| MapListOption | AccessInterestGroupData |  | MapListInterestGroupOption | 类别：const |
| MapListOption | AccessMarketData |  | MapListMarketOption | 类别：const |
| MapListOption | AccessPowerBlocData |  | MapListPowerBlocOption | 类别：const |
| MapListOption | AccessStateData |  | MapListStateOption | 类别：const |
| MapListOption | AccessStrategicRegionData |  | MapListStrategicRegionOption | 类别：const |
| MapListOption | GetActivateConscriptionCenterData |  | MapListActivateConscriptionCenterOption | 类别：nonconst |
| MapListOption | GetBuildingData |  | MapListBuildingOption | 类别：nonconst |
| MapListOption | GetColonyData |  | MapListColonyOption | 类别：nonconst |
| MapListOption | GetCountryData |  | MapListCountryOption | 类别：nonconst |
| MapListOption | GetDecreeData |  | MapListDecreeOption | 类别：nonconst |
| MapListOption | GetDiploActionData |  | MapListDiploActionOption | 类别：nonconst |
| MapListOption | GetFrontData |  | MapListDeployMilitaryFormationToFrontOption | 类别：nonconst |
| MapListOption | GetHarvestConditionAreaData |  | MapListHarvestConditionOption | 类别：nonconst |
| MapListOption | GetInterestGroupData |  | MapListInterestGroupOption | 类别：nonconst |
| MapListOption | GetMarketData |  | MapListMarketOption | 类别：nonconst |
| MapListOption | GetMilitaryFormationData |  | MapListMilitaryFormationOption | 类别：nonconst |
| MapListOption | GetPowerBlocData |  | MapListPowerBlocOption | 类别：nonconst |
| MapListOption | GetStateData |  | MapListStateOption | 类别：nonconst |
| MapListOption | GetStrategicRegionData |  | MapListStrategicRegionOption | 类别：nonconst |
| MapListPowerBlocInvitationPanel | GetDiplomaticAction | Unknown | DiplomaticAction | 类别：nonconst |
| MapListPowerBlocInvitationPanel | GetPowerBloc |  | PowerBloc | 类别：nonconst |
| MapListPowerBlocOption | AccessPowerBloc |  | PowerBloc | 类别：const |
| MapListPowerBlocOption | GetPowerBloc |  | PowerBloc | 类别：nonconst |
| MapListPowerBlocsPanel | GetDiplomaticAction | Unknown | DiplomaticAction | 类别：nonconst |
| MapListStateOption | AccessState |  | State | 类别：const |
| MapListStateOption | GetState |  | State | 类别：nonconst |
| MapListStrategicRegionOption | AccessStrategicRegion |  | StrategicRegion | 类别：const |
| MapListStrategicRegionOption | GetStrategicRegion |  | StrategicRegion | 类别：nonconst |
| MapModeList | GetSelectedMapMode |  | MapMode | 类别：nonconst |
| MapObjectPainterOptions | AccessBlurThresholdCtx |  | BlurThreshold | 类别：const |
| MapObjectTool | GetTooltip |  | GuiEditorTooltip | 类别：nonconst |
| MapObjectTool | MoveTool |  | MoveTool |  |
| MapObjectTool | SelectTool |  | SelectTool |  |
| Market | AccessMarketCapital |  | State | 类别：const |
| Market | GetFoodSecurity |  | FoodSecurity | 类别：nonconst |
| Market | GetFoodSecurityFilter |  | FoodSecurityFilter | 类别：nonconst |
| Market | GetMarketCapital |  | State | 类别：nonconst |
| Market | GetModifier |  | Modifier | 类别：nonconst |
| Market | GetOwner |  | Country | 类别：nonconst |
| Market | MakeScope |  | Scope |  |
| MarketGoods | GetGoods |  | Goods | 类别：nonconst |
| MarketGoods | GetMarket |  | Market | 类别：nonconst |
| MarketGoods | MakeScope |  | Scope |  |
| MarketPanel | GetFilteredGoodsList | FoodSecurityFilter | GoodsList | 类别：nonconst |
| MarketPanel | GetHarvestConditionList | FoodSecurityFilter | HarvestConditionList | 类别：nonconst |
| MarketPanel | GetMapModeList |  | MapModeList | 类别：nonconst |
| MarketPanel | GetMarket |  | Market | 类别：nonconst |
| MarketsMarker | GetAnyMarket |  | Market | 类别：nonconst |
| MarketsMarkerListItem | GetMarket |  | Market | 类别：nonconst |
| MaskPainterViewport | GetTooltip |  | GuiEditorTooltip | 类别：nonconst |
| MaterialBrowser | GetCurrentMaterial |  | Material | 类别：nonconst |
| MaterialEntry | GetMaterial |  | Material | 类别：nonconst |
| MaterialMixBrush | GetHoverSample |  | MaterialsSample | 类别：nonconst |
| MaterialMixEntry | AccessMaterial |  | Material | 类别：const |
| MaterialMixEntry | GetMaterial |  | Material | 类别：nonconst |
| MaterialPaintingMode | AccessBlurThresholdCtx |  | BlurThreshold | 类别：const |
| MeshImporter | AccessMaterialImportSettings |  | MeshImporterMaterials | 类别：const |
| MeshImporter | AccessUndoer |  | UndoStack | 类别：const |
| MilitaryFormation | AccessCountry |  | Country | 类别：const |
| MilitaryFormation | FindLeastExperiencedConscriptUnit | 未知 | CombatUnit |  |
| MilitaryFormation | FindLeastExperiencedRegularUnit | CombatUnitType | CombatUnit |  |
| MilitaryFormation | GetCountry |  | Country | 类别：nonconst |
| MilitaryFormation | GetCurrentFront |  | Front | 类别：nonconst |
| MilitaryFormation | GetCurrentHQ |  | Hq | 类别：nonconst |
| MilitaryFormation | GetCurrentSeaNode |  | Province | 类别：nonconst |
| MilitaryFormation | GetHomeHQ |  | Hq | 类别：nonconst |
| MilitaryFormation | GetInvasion |  | Invasion | 类别：nonconst |
| MilitaryFormation | GetMobilizationModifier |  | Modifier | 类别：nonconst |
| MilitaryFormation | GetModifier |  | Modifier | 类别：nonconst |
| MilitaryFormation | GetPrimaryCultureForGroup | CombatUnitGroup | Culture | 类别：nonconst |
| MilitaryFormation | GetPrimaryCultureForType | CombatUnitType | Culture | 类别：nonconst |
| MilitaryFormation | GetSelectedUnitTypeForGroup | CombatUnitGroup | CombatUnitType | 类别：nonconst |
| MilitaryFormation | GetShippingLane |  | ShippingLane | 类别：nonconst |
| MilitaryFormation | GetStateAtPosition |  | State | 类别：nonconst |
| MilitaryFormation | GetStrategicObjective |  | State | 类别：nonconst |
| MilitaryFormation | GetTargetFront |  | Front | 类别：nonconst |
| MilitaryFormation | GetTargetHQ |  | Hq | 类别：nonconst |
| MilitaryFormation | GetTargetSeaNode |  | Province | 类别：nonconst |
| MilitaryFormation | MakeScope |  | Scope |  |
| MilitaryFormationChangeNamePopup | GetFormation |  | MilitaryFormation | 类别：nonconst |
| MilitaryFormationUnitEntry | GetUnitType |  | CombatUnitType | 类别：nonconst |
| MilitaryPanelBuildingEntry | GetBuilding |  | Building | 类别：nonconst |
| MobilizationOption | GetUnitModifier |  | Modifier | 类别：nonconst |
| MobilizationOption | GetUpkeepModifier |  | Modifier | 类别：nonconst |
| MobilizationOption | GetUpkeepUnscaledModifier |  | Modifier | 类别：nonconst |
| MobilizationOption | MakeScope |  | Scope |  |
| Modifier | GetBreakdownFor | 未知 | ModifierBreakdown | 类别：nonconst |
| ModifierBreakdown | GetModifier |  | Modifier | 类别：nonconst |
| ModifierNodeDetailsView | GetModifierNodeData |  | ModifierNodeData | 类别：nonconst |
| ModifierNodeGraphItem | GetModifierNodeData |  | ModifierNodeData | 类别：nonconst |
| ModifiersPanel | GetModifier |  | Modifier | 类别：nonconst |
| MultiplayerSetupWindow | AccessMPConfig |  | MPConfig | 类别：const |
| MultiplayerSetupWindow | GetMPConfig |  | MPConfig | 类别：nonconst |
| NationalAwakeningMarker | GetCulture |  | Culture | 类别：nonconst |
| NationalizeBuildingGroup | GetInvestor |  | Country | 类别：nonconst |
| NationalizeBuildingTypeGroup | GetBuildingType |  | BuildingType | 类别：nonconst |
| NotificationSettingsItem | GetCurrentOption |  | NotificationOptionItem | 类别：nonconst |
| Objective | GetObjectiveType |  | ObjectiveType | 类别：nonconst |
| Objective | MakeScope |  | Scope |  |
| ObstinanceMarker | GetState |  | State | 类别：nonconst |
| OccupationPiechartData | GetCountry |  | Country | 类别：nonconst |
| OosData | GetPlayable |  | Playable | 类别：nonconst |
| OpinionMarker | GetCountry |  | Country | 类别：nonconst |
| Outliner | AccessCategory | CString | OutlinerEntry | 类别：const |
| OutlinerEntry | AccessScope |  | Scope | 类别：const |
| OutlinerEntry | AccessSituation |  | Event | 类别：const |
| PanelMilitary | AccessCountry |  | Country | 类别：const |
| PanelMilitary | GetCountry |  | Country | 类别：nonconst |
| PanelMilitary | GetMapModeList |  | MapModeList | 类别：nonconst |
| Party | GetCountry |  | Country | 类别：nonconst |
| Party | GetLeader |  | InterestGroup | 类别：nonconst |
| Party | GetLeaderCharacter |  | Character | 类别：nonconst |
| Party | MakeScope |  | Scope |  |
| PartyPanel | AccessParty |  | Party | 类别：const |
| PartyPanel | GetParty |  | Party | 类别：nonconst |
| PastBattleMarker | GetBattle |  | Battle | 类别：nonconst |
| PdxAccount | GetInventory |  | AccountInventory | 类别：nonconst |
| PdxGuiWidget | AccessChild | CString | PdxGuiWidget | 类别：const |
| PdxGuiWidget | AccessParent |  | PdxGuiWidget | 类别：const |
| PdxGuiWidget | FindChild | CString | PdxGuiWidget |  |
| PdxGuiWidget | GfxVideoControl |  | PdxGuiGfxVideoControl |  |
| PdxSetting | GetSettingPromoted |  | PdxCoreSetting | 类别：nonconst |
| Playable | AccessCountry |  | Country | 类别：const |
| Playable | GetCountry |  | Country | 类别：nonconst |
| Player | AccessPlayedOrObservedCountry |  | Country | 类别：const |
| Player | GetPlayedOrObservedCountry |  | Country | 类别：nonconst |
| PlayerMessageItem | GetCountry |  | Country | 类别：nonconst |
| PlayerMessageItem | GetDiploPlay |  | DiplomaticPlay | 类别：nonconst |
| PlayerMessageItem | GetDiplomaticAction |  | DiplomaticAction | 类别：nonconst |
| PlayerMessageItem | GetInstitution |  | Institution | 类别：nonconst |
| PlayerMessageItem | GetLaw |  | Law | 类别：nonconst |
| PlayerMessageItem | GetPrevLaw |  | Law | 类别：nonconst |
| PlayerMessageItem | GetScopeActorCountry |  | Country | 类别：nonconst |
| PlayerMessageItem | GetScopeDiploPlay |  | DiplomaticPlay | 类别：nonconst |
| PlayerMessageItem | GetScopeTargetCountry |  | Country | 类别：nonconst |
| PlayerMessageItem | GetScopeTechnology |  | Technology | 类别：nonconst |
| PlayerMessageItem | GetTopScope |  | TopScope | 类别：nonconst |
| PoliticalLobby | GetCountry |  | Country | 类别：nonconst |
| PoliticalLobby | GetEstablishmentDate |  | Date | 类别：nonconst |
| PoliticalLobby | GetTargetCountry |  | Country | 类别：nonconst |
| PoliticalLobby | GetType |  | PoliticalLobbyType | 类别：nonconst |
| PoliticalLobby | MakeScope |  | Scope |  |
| PoliticalLobbyAppeasementFactor | MakeScope |  | Scope |  |
| PoliticalLobbyMarker | GetPlacementCountry |  | Country | 类别：nonconst |
| PoliticalLobbyMarker | GetPoliticalLobby |  | PoliticalLobby | 类别：nonconst |
| PoliticalLobbyPanel | GetPoliticalLobby |  | PoliticalLobby | 类别：nonconst |
| PoliticalLobbyType | MakeScope |  | Scope |  |
| PoliticalMovement | GetCivilWar |  | CivilWar | 类别：nonconst |
| PoliticalMovement | GetCoreIdeology |  | Ideology | 类别：nonconst |
| PoliticalMovement | GetCountry |  | Country | 类别：nonconst |
| PoliticalMovement | GetSupportingPops |  | PopList | 类别：nonconst |
| PoliticalMovement | GetType |  | PoliticalMovementType | 类别：nonconst |
| PoliticalMovement | GetUprisingDefinition |  | CountryDefinition | 类别：nonconst |
| PoliticalMovement | MakeScope |  | Scope |  |
| PoliticalMovementCategory | MakeScope |  | Scope |  |
| PoliticalMovementPanel | GetPoliticalMovement |  | PoliticalMovement | 类别：nonconst |
| PoliticalMovementType | GetCategory |  | PoliticalMovementCategory | 类别：nonconst |
| PoliticalMovementType | GetCoreIdeology |  | Ideology | 类别：nonconst |
| PoliticalMovementType | MakeScope |  | Scope |  |
| PoliticsPanel | AccessReformGovernment |  | ReformGovernment | 类别：const |
| PoliticsPanel | GetReformGovernment |  | ReformGovernment | 类别：nonconst |
| Pop | AccessBuilding |  | Building | 类别：const |
| Pop | AccessCulture |  | Culture | 类别：const |
| Pop | AccessLargestInterestGroup |  | InterestGroup | 类别：const |
| Pop | AccessPopType |  | PopType | 类别：const |
| Pop | AccessReligion |  | Religion | 类别：const |
| Pop | AccessState |  | State | 类别：const |
| Pop | GetAcceptanceStatus |  | AcceptanceStatus | 类别：nonconst |
| Pop | GetAssimilatingCulture |  | Culture | 类别：nonconst |
| Pop | GetBuilding |  | Building | 类别：nonconst |
| Pop | GetConvertingReligion |  | Religion | 类别：nonconst |
| Pop | GetCountry |  | Country | 类别：nonconst |
| Pop | GetCulture |  | Culture | 类别：nonconst |
| Pop | GetLargestInterestGroup |  | InterestGroup | 类别：nonconst |
| Pop | GetLargestPoliticalMovement |  | PoliticalMovement | 类别：nonconst |
| Pop | GetPopType |  | PopType | 类别：nonconst |
| Pop | GetReligion |  | Religion | 类别：nonconst |
| Pop | GetSocialClass |  | SocialClass | 类别：nonconst |
| Pop | GetState |  | State | 类别：nonconst |
| Pop | MakeScope |  | Scope |  |
| PopBrowserPanel | GetCountry |  | Country | 类别：nonconst |
| PopConsumptionGoods | GetGoods |  | Goods | 类别：nonconst |
| PopConsumptionGoods | GetPop |  | Pop | 类别：nonconst |
| PopDetailsPanel | AccessPop |  | Pop | 类别：const |
| PopList | GetBuildingContext |  | Building | 类别：nonconst |
| PopList | GetInterestGroupContext |  | InterestGroup | 类别：nonconst |
| PopList | GetItem0 |  | PopListItem | 类别：nonconst |
| PopList | GetItem1 |  | PopListItem | 类别：nonconst |
| PopList | GetItem2 |  | PopListItem | 类别：nonconst |
| PopList | GetItem3 |  | PopListItem | 类别：nonconst |
| PopList | GetPoliticalMovementContext |  | PoliticalMovement | 类别：nonconst |
| PopListItem | AccessPopType |  | PopType | 类别：const |
| PopListItem | GetFirstPop |  | Pop | 类别：nonconst |
| PopListItem | GetPopType |  | PopType | 类别：nonconst |
| PopNeed | GetDefaultGoods |  | Goods | 类别：nonconst |
| PopNeed | GetPop |  | Pop | 类别：nonconst |
| PopType | MakeScope |  | Scope |  |
| PopWithIG | GetInterestGroup |  | InterestGroup | 类别：nonconst |
| PopWithIG | GetPop |  | Pop | 类别：nonconst |
| PopsOverviewPanel | AccessPopsList |  | PopList | 类别：const |
| PopsOverviewPanel | GetMapModeList |  | MapModeList | 类别：nonconst |
| PopulationGrouping | AccessInterestGroup |  | InterestGroup | 类别：const |
| PopulationGrouping | GetInterestGroup |  | InterestGroup | 类别：nonconst |
| PopupManager | GetRecruitFormation |  | MilitaryFormation | 类别：nonconst |
| PopupManager | GetRecruitHQ |  | Hq | 类别：nonconst |
| PortraitEditorWindow | GetChildGenerator |  | ChildGenerator | 类别：nonconst |
| PortraitEditorWindow | GetPortraitDataContext |  | PortraitDataContext | 类别：nonconst |
| PortraitEditorWindow | GetSelectedEthnicityItem |  | EthnicityItem | 类别：nonconst |
| PortraitEditorWindow | GetSelectedGeneItem |  | GeneItem | 类别：nonconst |
| PotentialLeaderIdeology | GetIdeology |  | Ideology | 类别：nonconst |
| PowerBloc | GetCohesionLevel |  | CohesionLevel | 类别：nonconst |
| PowerBloc | GetFlag |  | CoatOfArms | 类别：nonconst |
| PowerBloc | GetFoundingDate |  | Date | 类别：nonconst |
| PowerBloc | GetIdentity |  | PowerBlocIdentity | 类别：nonconst |
| PowerBloc | GetLeader |  | Country | 类别：nonconst |
| PowerBloc | GetLeaderModifier |  | Modifier | 类别：nonconst |
| PowerBloc | GetMember | 未知 | Country | 类别：nonconst |
| PowerBloc | GetMemberWithUniqueHeadOfState | int32 | Country | 类别：nonconst |
| PowerBloc | GetModifier |  | Modifier | 类别：nonconst |
| PowerBloc | GetNextMandateDate |  | Date | 类别：nonconst |
| PowerBloc | GetNonLeaderModifier |  | Modifier | 类别：nonconst |
| PowerBloc | GetParticipantWithHighestInfamy |  | Country | 类别：nonconst |
| PowerBloc | GetParticipantWithHighestLeaderLawProgressivenessDifference |  | Country | 类别：nonconst |
| PowerBloc | GetParticipantWithHighestLibertyDesire |  | Country | 类别：nonconst |
| PowerBloc | GetParticipantWithLowestEconomicDependence |  | Country | 类别：nonconst |
| PowerBloc | GetParticipantWithLowestEconomicDependenceOnLeader |  | Country | 类别：nonconst |
| PowerBloc | GetParticipantWithLowestLeaderRelations |  | Country | 类别：nonconst |
| PowerBloc | GetParticipantWithLowestLeaderReligionPercentage |  | Country | 类别：nonconst |
| PowerBloc | GetPowerBlocStatue |  | PowerBlocStatue | 类别：nonconst |
| PowerBloc | GetPowerStruggleContender |  | Country | 类别：nonconst |
| PowerBloc | GetPrincipleData | PowerBlocPrinciple | PowerBlocPrincipleData | 类别：nonconst |
| PowerBloc | GetRequestToJoin | Country | DiplomaticAction | 类别：nonconst |
| PowerBloc | MakeScope |  | Scope |  |
| PowerBlocCoaPiece | GetCoa |  | CoatOfArms | 类别：nonconst |
| PowerBlocCoaPieceSelector | GetSelectedItem |  | PowerBlocCoaPiece | 类别：nonconst |
| PowerBlocCustomizationPopup | GetCustomCoaPreview |  | CoatOfArms | 类别：nonconst |
| PowerBlocCustomizationPopup | GetPowerBloc |  | PowerBloc | 类别：nonconst |
| PowerBlocCustomizationPopup | GetPowerBlocMapTextureSelector |  | PowerBlocMapTextureSelector | 类别：nonconst |
| PowerBlocCustomizationPopup | GetStatue |  | PowerBlocStatue | 类别：nonconst |
| PowerBlocCustomizationPopup | GetStatueHeroType |  | PowerBlocStatueHeroType | 类别：nonconst |
| PowerBlocCustomizationPopup | GetStatuePedestalType |  | PowerBlocStatuePedestalType | 类别：nonconst |
| PowerBlocFormation | GetConfirmedCustomCoaPreview |  | CoatOfArms | 类别：nonconst |
| PowerBlocFormation | GetPrincipleSlot | 未知 | PowerBlocFormationPrincipleSlot | 类别：nonconst |
| PowerBlocFormation | GetSelectedIdentity |  | PowerBlocIdentity | 类别：nonconst |
| PowerBlocFormation | GetStatue |  | PowerBlocStatue | 类别：nonconst |
| PowerBlocFormationPanel | GetPowerBlocFormation |  | PowerBlocFormation | 类别：nonconst |
| PowerBlocFormationPrincipleSlot | GetSelectedPrinciple |  | PowerBlocPrinciple | 类别：nonconst |
| PowerBlocIdentity | MakeScope |  | Scope |  |
| PowerBlocMapTextureSelector | GetSelectedItem |  | PowerBlocMapTexture | 类别：nonconst |
| PowerBlocPanel | GetMapModeList |  | MapModeList | 类别：nonconst |
| PowerBlocPanel | GetPrincipleSlot | int32 | PowerBlocPrincipleSlot | 类别：nonconst |
| PowerBlocPanel | GetSelectedPowerBloc |  | PowerBloc | 类别：nonconst |
| PowerBlocPrinciple | GetGroup |  | PowerBlocPrincipleGroup | 类别：nonconst |
| PowerBlocPrinciple | MakeScope |  | Scope |  |
| PowerBlocPrincipleData | GetCooldownDate |  | Date | 类别：nonconst |
| PowerBlocPrincipleData | GetSelectionDate |  | Date | 类别：nonconst |
| PowerBlocPrincipleGroup | MakeScope |  | Scope |  |
| PowerBlocPrincipleSelectionWindow | GetPowerBloc |  | PowerBloc | 类别：nonconst |
| PowerBlocPrincipleSelectionWindow | GetPowerBlocFormation |  | PowerBlocFormation | 类别：nonconst |
| PowerBlocPrincipleSelectionWindow | GetReplacedPrinciple |  | PowerBlocPrinciple | 类别：nonconst |
| PowerBlocPrincipleSelectionWindow | GetSelectedPrinciple |  | PowerBlocPrinciple | 类别：nonconst |
| PowerBlocPrincipleSlot | GetPrinciple |  | PowerBlocPrinciple | 类别：nonconst |
| PowerBlocStatueAccessoryTypeSelector | GetStatueAccessoryType |  | PowerBlocStatueAccessoryType | 类别：nonconst |
| PrestigeGoodChangeNamePopup | GetPrestigeGood |  | Goods | 类别：nonconst |
| ProductionMarker | AccessState |  | State | 类别：const |
| Proposal | AccessTimeoutTimer |  | PieTimer | 类别：const |
| Proposal | GetActor |  | Country | 类别：nonconst |
| Proposal | GetDiplomaticAction |  | DiplomaticAction | 类别：nonconst |
| Proposal | GetDiplomaticDemand |  | DiplomaticDemand | 类别：nonconst |
| Proposal | GetDiplomaticPlay |  | DiplomaticPlay | 类别：nonconst |
| Proposal | GetRecipient |  | Country | 类别：nonconst |
| Proposal | GetTarget |  | Country | 类别：nonconst |
| Proposal | GetTreaty |  | Treaty | 类别：nonconst |
| Province | AccessStateRegion |  | StateRegion | 类别：const |
| Province | GetController |  | Country | 类别：nonconst |
| Province | GetState |  | State | 类别：nonconst |
| Province | GetStateRegion |  | StateRegion | 类别：nonconst |
| Province | MakeScope |  | Scope |  |
| ReformGovernment | GetCountry |  | Country | 类别：nonconst |
| ReformGovernment | GetLegitimacyLevel |  | LegitimacyLevel | 类别：nonconst |
| ReformGovernment | GetPredictedLegitimacyLevel |  | LegitimacyLevel | 类别：nonconst |
| ReformGovernment | GetPredictedNewRuler | bool | Character | 类别：nonconst |
| ReleaseCountryWindow | AccessCountryCreation |  | CountryCreation | 类别：const |
| ReleaseCountryWindow | GetCountryCreation |  | CountryCreation | 类别：nonconst |
| Religion | MakeScope |  | Scope |  |
| ReligionInfoPanel | AccessPopsList |  | PopList | 类别：const |
| ReligionInfoPanel | AccessReligion |  | Religion | 类别：const |
| ReligionInfoPanel | GetReligion |  | Religion | 类别：nonconst |
| RevolutionaryMovementMarker | GetPoliticalMovement |  | PoliticalMovement | 类别：nonconst |
| SaveGameAnalysisView | GetSaveGame |  | SaveGame | 类别：nonconst |
| SaveGameItem | GetCountryFlag |  | CoatOfArms | 类别：nonconst |
| SaveGameItem | GetDate |  | Date | 类别：nonconst |
| SaveGameWindow | AccessCloudData |  | CloudSaveData | 类别：const |
| Scope | AccessAmendment |  | Amendment | 类别：const |
| Scope | AccessAmendmentType |  | AmendmentType | 类别：const |
| Scope | AccessBattle |  | Battle | 类别：const |
| Scope | AccessBuilding |  | Building | 类别：const |
| Scope | AccessBuildingGroup |  | BuildingGroup | 类别：const |
| Scope | AccessBuildingType |  | BuildingType | 类别：const |
| Scope | AccessCanalType |  | CanalType | 类别：const |
| Scope | AccessCharacter |  | Character | 类别：const |
| Scope | AccessCivilWar |  | CivilWar | 类别：const |
| Scope | AccessCombatUnit |  | CombatUnit | 类别：const |
| Scope | AccessCombatUnitType |  | CombatUnitType | 类别：const |
| Scope | AccessCommanderOrderType |  | CommanderOrderType | 类别：const |
| Scope | AccessCompany |  | Company | 类别：const |
| Scope | AccessCompanyType |  | CompanyType | 类别：const |
| Scope | AccessCountry |  | Country | 类别：const |
| Scope | AccessCountryCreation |  | CountryCreation | 类别：const |
| Scope | AccessCountryDefinition |  | CountryDefinition | 类别：const |
| Scope | AccessCountryFormation |  | CountryFormation | 类别：const |
| Scope | AccessCulturalCommunity |  | CulturalCommunity | 类别：const |
| Scope | AccessCulture |  | Culture | 类别：const |
| Scope | AccessDecisionType |  | Decision | 类别：const |
| Scope | AccessDecree |  | Decree | 类别：const |
| Scope | AccessDiplomaticAction |  | DiplomaticAction | 类别：const |
| Scope | AccessDiplomaticCatalyst |  | DiplomaticCatalyst | 类别：const |
| Scope | AccessDiplomaticCatalystCategory |  | DiplomaticCatalystCategory | 类别：const |
| Scope | AccessDiplomaticCatalystType |  | DiplomaticCatalystType | 类别：const |
| Scope | AccessDiplomaticDemand |  | DiplomaticDemand | 类别：const |
| Scope | AccessDiplomaticPact |  | DiplomaticPact | 类别：const |
| Scope | AccessDiplomaticPlay |  | DiplomaticPlay | 类别：const |
| Scope | AccessDiplomaticPlayType |  | DiplomaticPlayType | 类别：const |
| Scope | AccessDiplomaticRelations |  | DiplomaticRelations | 类别：const |
| Scope | AccessFront |  | Front | 类别：const |
| Scope | AccessGeographicRegion |  | GeographicRegion | 类别：const |
| Scope | AccessGoods |  | Goods | 类别：const |
| Scope | AccessHQ |  | Hq | 类别：const |
| Scope | AccessHarvestCondition |  | HarvestCondition | 类别：const |
| Scope | AccessHarvestConditionArea |  | HarvestConditionArea | 类别：const |
| Scope | AccessHarvestConditionType |  | HarvestConditionType | 类别：const |
| Scope | AccessIdeology |  | Ideology | 类别：const |
| Scope | AccessInstitution |  | Institution | 类别：const |
| Scope | AccessInstitutionType |  | InstitutionType | 类别：const |
| Scope | AccessInterest |  | Interest | 类别：const |
| Scope | AccessInterestGroup |  | InterestGroup | 类别：const |
| Scope | AccessInterestGroupTrait |  | InterestGroupTrait | 类别：const |
| Scope | AccessInvasion |  | Invasion | 类别：const |
| Scope | AccessJournalEntry |  | JournalEntry | 类别：const |
| Scope | AccessLaw |  | Law | 类别：const |
| Scope | AccessLawType |  | LawType | 类别：const |
| Scope | AccessMarket |  | Market | 类别：const |
| Scope | AccessMarketGoods |  | MarketGoods | 类别：const |
| Scope | AccessMilitaryFormation |  | MilitaryFormation | 类别：const |
| Scope | AccessMobilizationOption |  | MobilizationOption | 类别：const |
| Scope | AccessObjective |  | Objective | 类别：const |
| Scope | AccessParty |  | Party | 类别：const |
| Scope | AccessPoliticalLobby |  | PoliticalLobby | 类别：const |
| Scope | AccessPoliticalLobbyAppeasementFactor |  | PoliticalLobbyAppeasementFactor | 类别：const |
| Scope | AccessPoliticalLobbyType |  | PoliticalLobbyType | 类别：const |
| Scope | AccessPoliticalMovement |  | PoliticalMovement | 类别：const |
| Scope | AccessPoliticalMovementCategory |  | PoliticalMovementCategory | 类别：const |
| Scope | AccessPoliticalMovementType |  | PoliticalMovementType | 类别：const |
| Scope | AccessPop |  | Pop | 类别：const |
| Scope | AccessPopType |  | PopType | 类别：const |
| Scope | AccessPowerBloc |  | PowerBloc | 类别：const |
| Scope | AccessPowerBlocIdentity |  | PowerBlocIdentity | 类别：const |
| Scope | AccessPowerBlocPrinciple |  | PowerBlocPrinciple | 类别：const |
| Scope | AccessPowerBlocPrincipleGroup |  | PowerBlocPrincipleGroup | 类别：const |
| Scope | AccessProvince |  | Province | 类别：const |
| Scope | AccessReligion |  | Religion | 类别：const |
| Scope | AccessShippingLane |  | ShippingLane | 类别：const |
| Scope | AccessState |  | State | 类别：const |
| Scope | AccessStateGoods |  | StateGoods | 类别：const |
| Scope | AccessStateRegion |  | StateRegion | 类别：const |
| Scope | AccessStateTrait |  | StateTrait | 类别：const |
| Scope | AccessStrategicRegion |  | StrategicRegion | 类别：const |
| Scope | AccessSway |  | Sway | 类别：const |
| Scope | AccessTechnology |  | Technology | 类别：const |
| Scope | AccessTheater |  | Theater | 类别：const |
| Scope | AccessTreaty |  | Treaty | 类别：const |
| Scope | AccessTreatyArticle |  | Article | 类别：const |
| Scope | AccessWar |  | War | 类别：const |
| Scope | AccessWarGoal |  | WarGoal | 类别：const |
| Scope | AccessWarGoalType |  | WarGoalType | 类别：const |
| Scope | GetAmendment |  | Amendment | 类别：nonconst |
| Scope | GetAmendmentType |  | AmendmentType | 类别： nonconst |
| Scope | GetBattle |  | Battle | 类别： nonconst |
| Scope | GetBuilding |  | Building | 类别： nonconst |
| Scope | GetBuildingGroup |  | BuildingGroup | 类别： nonconst |
| Scope | GetBuildingType |  | BuildingType | 类别： nonconst |
| Scope | GetCanalType |  | CanalType | 类别： nonconst |
| Scope | GetCharacter |  | Character | 类别： nonconst |
| Scope | GetCivilWar |  | CivilWar | 类别： nonconst |
| Scope | GetCombatUnit |  | CombatUnit | 类别： nonconst |
| Scope | GetCombatUnitType |  | CombatUnitType | 类别： nonconst |
| Scope | GetCommanderOrderType |  | CommanderOrderType | 类别： nonconst |
| Scope | GetCompany |  | Company | 类别： nonconst |
| Scope | GetCompanyType |  | CompanyType | 类别： nonconst |
| Scope | GetCountry |  | Country | 类别： nonconst |
| Scope | GetCountryCreation |  | CountryCreation | 类别： nonconst |
| Scope | GetCountryDefinition |  | CountryDefinition | 类别： nonconst |
| Scope | GetCountryFormation |  | CountryFormation | 类别： nonconst |
| Scope | GetCulturalCommunity |  | CulturalCommunity | 类别： nonconst |
| Scope | GetCulture |  | Culture | 类别： nonconst |
| Scope | GetDecisionType |  | Decision | 类别： nonconst |
| Scope | GetDecree |  | Decree | 类别： nonconst |
| Scope | GetDiplomaticAction |  | DiplomaticAction | 类别： nonconst |
| Scope | GetDiplomaticCatalyst |  | DiplomaticCatalyst | 类别： nonconst |
| Scope | GetDiplomaticCatalystCategory |  | DiplomaticCatalystCategory | 类别： nonconst |
| Scope | GetDiplomaticCatalystType |  | DiplomaticCatalystType | 类别： nonconst |
| Scope | GetDiplomaticDemand |  | DiplomaticDemand | 类别： nonconst |
| Scope | GetDiplomaticPact |  | DiplomaticPact | 类别： nonconst |
| Scope | GetDiplomaticPlay |  | DiplomaticPlay | 类别： nonconst |
| Scope | GetDiplomaticPlayType |  | DiplomaticPlayType | 类别： nonconst |
| Scope | GetDiplomaticRelations |  | DiplomaticRelations | 类别： nonconst |
| Scope | GetFront |  | Front | 类别： nonconst |
| Scope | GetGeographicRegion |  | GeographicRegion | 类别： nonconst |
| Scope | GetGoods |  | Goods | 类别： nonconst |
| Scope | GetHQ |  | Hq | 类别： nonconst |
| Scope | GetHarvestCondition |  | HarvestCondition | 类别： nonconst |
| Scope | GetHarvestConditionArea |  | HarvestConditionArea | 类别： nonconst |
| Scope | GetHarvestConditionType |  | HarvestConditionType | 类别： nonconst |
| Scope | GetIdeology |  | Ideology | 类别： nonconst |
| Scope | GetInstitution |  | Institution | 类别： nonconst |
| Scope | GetInstitutionType |  | InstitutionType | 类别： nonconst |
| Scope | GetInterest |  | Interest | 类别： nonconst |
| Scope | GetInterestGroup |  | InterestGroup | 类别： nonconst |
| Scope | GetInterestGroupTrait |  | InterestGroupTrait | 类别： nonconst |
| Scope | GetInvasion |  | Invasion | 类别： nonconst |
| Scope | GetJournalEntry |  | JournalEntry | 类别： nonconst |
| Scope | GetLaw |  | Law | 类别： nonconst |
| Scope | GetLawType |  | LawType | 类别： nonconst |
| Scope | GetMarket |  | Market | 类别： nonconst |
| Scope | GetMarketGoods |  | MarketGoods | 类别： nonconst |
| Scope | GetMilitaryFormation |  | MilitaryFormation | 类别： nonconst |
| Scope | GetMobilizationOption |  | MobilizationOption | 类别： nonconst |
| Scope | GetObjective |  | Objective | 类别： nonconst |
| Scope | GetParty |  | Party | 类别： nonconst |
| Scope | GetPoliticalLobby |  | PoliticalLobby | 类别： nonconst |
| Scope | GetPoliticalLobbyAppeasementFactor |  | PoliticalLobbyAppeasementFactor | 类别： nonconst |
| Scope | GetPoliticalLobbyType |  | PoliticalLobbyType | 类别： nonconst |
| Scope | GetPoliticalMovement |  | PoliticalMovement | 类别： nonconst |
| Scope | GetPoliticalMovementCategory |  | PoliticalMovementCategory | 类别： nonconst |
| Scope | GetPoliticalMovementType |  | PoliticalMovementType | 类别： nonconst |
| Scope | GetPop |  | Pop | 类别： nonconst |
| Scope | GetPopType |  | PopType | 类别： nonconst |
| Scope | GetPowerBloc |  | PowerBloc | 类别： nonconst |
| Scope | GetPowerBlocIdentity |  | PowerBlocIdentity | 类别： nonconst |
| Scope | GetPowerBlocPrinciple |  | PowerBlocPrinciple | 类别： nonconst |
| Scope | GetPowerBlocPrincipleGroup |  | PowerBlocPrincipleGroup | 类别： nonconst |
| Scope | GetProvince |  | Province | 类别： nonconst |
| Scope | GetReligion |  | Religion | 类别： nonconst |
| Scope | GetShippingLane |  | ShippingLane | 类别： nonconst |
| Scope | GetState |  | State | 类别： nonconst |
| Scope | GetStateGoods |  | StateGoods | 类别： nonconst |
| Scope | GetStateRegion |  | StateRegion | 类别： nonconst |
| Scope | GetStateTrait |  | StateTrait | 类别： nonconst |
| Scope | GetStrategicRegion |  | StrategicRegion | 类别： nonconst |
| Scope | GetSway |  | Sway | 类别： nonconst |
| Scope | GetTechnology |  | Technology | 类别： nonconst |
| Scope | GetTheater |  | Theater | 类别： nonconst |
| Scope | GetTreaty |  | Treaty | 类别： nonconst |
| Scope | GetTreatyArticle |  | Article | 类别： nonconst |
| Scope | GetVariable | Unknown | Scope | 类别： nonconst |
| Scope | GetWar |  | War | 类别： nonconst |
| Scope | GetWarGoal |  | WarGoal | 类别： nonconst |
| Scope | GetWarGoalType |  | WarGoalType | 类别： nonconst |
| Scope | Var | CString | Scope |  |
| ScopeDebugInspectorPlugin | GetScopeData |  | ScopeDebugData | 类别： nonconst |
| ScopedEditorSettingsCategory | AccessCategory |  | EditorSettingCategory | 类别： const |
| ScopedEditorSettingsCategory | GetCategory |  | EditorSettingCategory | 类别： nonconst |
| ScriptProfilerGui | GetCurrentEntry |  | ScriptProfilerEntry | 类别： nonconst |
| ScriptProfilerGui | GetFileSearchList |  | ToolPropertySearchList | 类别： nonconst |
| ScriptProfilerGui | GetModeSearchList |  | ToolPropertySearchList | 类别： nonconst |
| ScriptRunnerInspector | AccessEffectResult |  | ScriptRunnerResult | 类别： const |
| ScriptRunnerInspector | AccessEventTargets |  | EventTargetSetupContext | 类别： const |
| ScriptRunnerInspector | AccessTriggerResult |  | ScriptRunnerResult | 类别： const |
| SeaNodeMovementMarker | GetSeaNode |  | Province | 类别： nonconst |
| SeaRegionInfraMarker | GetStateRegion |  | StateRegion | 类别： nonconst |
| SeaRegionPanel | AccessProvince |  | Province | 类别： const |
| SeaRegionPanel | GetProvince |  | Province | 类别： nonconst |
| SeaRegionWar | GetWar |  | War | 类别： nonconst |
| ShippingLane | GetBeginState |  | State | 类别： nonconst |
| ShippingLane | GetCountry |  | Country | 类别： nonconst |
| ShippingLane | GetEndState |  | State | 类别： nonconst |
| ShippingLane | GetMilitaryFormation |  | MilitaryFormation | 类别： nonconst |
| ShippingLane | GetProvince |  | Province | 类别： nonconst |
| ShippingLane | GetTreaty |  | Treaty | 类别： nonconst |
| ShippingLane | MakeScope |  | Scope |  |
| SmartBrushHeightRange | AccessPattern |  | SmartBrushPattern | 类别： const |
| SmartBrushPattern | AccessMaterialMix |  | MaterialMix | 类别： const |
| SocialClass | GetMaxAllowedStatusIn | Country | AcceptanceStatus | 类别： nonconst |
| SocialClass | GetMinAllowedStatusIn | Country | AcceptanceStatus | 类别： nonconst |
| SocialClass | GetSocialHierarchy |  | SocialHierarchy | 类别： nonconst |
| SocietyPanel | GetMapModeList |  | MapModeList | 类别： nonconst |
| SocietyPanel | GetPopList |  | PopList | 类别： nonconst |
| SocietyPanel | GetSelectedAcceptanceStatus |  | AcceptanceStatus | 类别： nonconst |
| SocietyPanel | GetSelectedAcceptanceStatusSegment |  | AcceptanceStatusSegment | 类别： nonconst |
| StagedCommanderTransfer | GetCommander |  | Character | 类别： nonconst |
| StagedFormation | GetMilitaryFormation |  | MilitaryFormation | 类别： nonconst |
| StagedUnitsWithType | GetStateFilter |  | State | 类别： nonconst |
| StagedUnitsWithType | GetUnitType |  | CombatUnitType | 类别： nonconst |
| State | AccessBuilding | BuildingType | Building | 类别： const |
| State | AccessMarket |  | Market | 类别： const |
| State | AccessModifier |  | Modifier | 类别： const |
| State | AccessOwner |  | Country | 类别： const |
| State | AccessPopsList |  | PopList | 类别： const |
| State | AccessStateRegion |  | StateRegion | 类别： const |
| State | AccessSubsistenceBuilding |  | Building | 类别： const |
| State | GetBuilding | BuildingType | Building | 类别： nonconst |
| State | GetColonyCompany |  | Company | 类别： nonconst |
| State | GetController |  | Country | 类别： nonconst |
| State | GetCountry |  | Country | 类别： nonconst |
| State | GetEnemyWithHighestOccupation |  | Country | 类别： nonconst |
| State | GetFoodSecurity |  | FoodSecurity | 类别： nonconst |
| State | GetMarket |  | Market | 类别： nonconst |
| State | GetMassMigrationCulture |  | Culture | 类别： nonconst |
| State | GetMassMigrationOriginCountry |  | Country | 类别： nonconst |
| State | GetModifier |  | Modifier | 类别： nonconst |
| State | GetNextColonyProvince |  | Province | 类别： nonconst |
| State | GetOccupant |  | Country | 类别： nonconst |
| State | GetOwner |  | Country | 类别： nonconst |
| State | GetStateRegion |  | StateRegion | 类别： nonconst |
| State | GetSubsistenceBuilding |  | Building | 类别： nonconst |
| State | GetTheater | Country | Theater | 类别： nonconst |
| State | MakeScope |  | Scope |  |
| StateGoods | GetGoods |  | Goods | 类别： nonconst |
| StateGoods | GetState |  | State | 类别： nonconst |
| StateGoods | MakeScope |  | Scope |  |
| StateInfraMarker | GetState |  | State | 类别： nonconst |
| StateMarker | GetGoods |  | Goods | 类别： nonconst |
| StateMarker | GetState |  | State | 类别： nonconst |
| StateNameChangePopup | GetState |  | State | 类别： nonconst |
| StatePopulationPanel | AccessState |  | State | 类别： const |
| StatePopulationPanel | GetState |  | State | 类别： nonconst |
| StateRegion | AccessLargestStateOwner |  | Country | 类别： const |
| StateRegion | AccessStrategicRegion |  | StrategicRegion | 类别： const |
| StateRegion | GetLargestStateInRegion |  | State | 类别： nonconst |
| StateRegion | GetLargestStateOwner |  | Country | 类别： nonconst |
| StateRegion | GetStrategicRegion |  | StrategicRegion | 类别： nonconst |
| StateRegion | MakeScope |  | Scope |  |
| StateTrait | MakeScope |  | Scope |  |
| StatesPanel | AccessBuilding | BuildingType | Building | 类别： const |
| StatesPanel | AccessState |  | State | 类别： const |
| StatesPanel | AccessSubsistenceBuilding |  | Building | 类别： const |
| StatesPanel | GetState |  | State | 类别： nonconst |
| StrategicRegion | AccessFirstDiplomaticPlay |  | DiplomaticPlay | 类别： const |
| StrategicRegion | GetFirstDiplomaticPlay |  | DiplomaticPlay | 类别： nonconst |
| StrategicRegion | GetInterest | Unknown | Interest | 类别： nonconst |
| StrategicRegion | MakeScope |  | Scope |  |
| StrategicRegionMarker | AccessStrategicRegion |  | StrategicRegion | 类别： const |
| StrategicRegionMarker | GetStrategicRegion |  | StrategicRegion | 类别： nonconst |
| SubjectType | GetDiplomaticActionType |  | DiplomaticActionType | 类别： nonconst |
| SubjectType | GetHigherAutonomySubjectType | Country | SubjectType | 类别： nonconst |
| SubjectType | GetLowerAutonomySubjectType | Country | SubjectType | 类别： nonconst |
| SupplyNetworkEntry | GetCountry |  | Country | 类别： nonconst |
| Sway | GetSwayOffer |  | SwayOffer | 类别： nonconst |
| Sway | MakeScope |  | Scope |  |
| SwayCountryPanel | AccessCountry |  | Country | 类别： const |
| SwayCountryPanel | AccessDiplomaticPlay |  | DiplomaticPlay | 类别： const |
| SwayCountryPanel | AccessOtherCountry |  | Country | 类别： const |
| SwayCountryPanel | GetCountry |  | Country | 类别： nonconst |
| SwayCountryPanel | GetDiplomaticPlay |  | DiplomaticPlay | 类别： nonconst |
| SwayCountryPanel | GetOtherCountry |  | Country | 类别： nonconst |
| SwayOffer | GetCountryForFlag | Country | Country | 类别： nonconst |
| SwayOffer | GetDiplomaticActionType |  | DiplomaticActionType | 类别： nonconst |
| SwayOffer | GetOfferedWarGoal |  | WarGoalDraft | 类别： nonconst |
| SwayOffer | GetState |  | State | 类别： nonconst |
| SwayOffer | GetSwayOfferType |  | SwayOfferType | 类别： nonconst |
| SwayOffer | GetThirdPartyCountry |  | Country | 类别： nonconst |
| TechTreeItem | GetTechnology |  | Technology | 类别： nonconst |
| TechTreeLine | GetSourceTech |  | Technology | 类别： nonconst |
| TechTreeLine | GetTargetTech |  | Technology | 类别： nonconst |
| Technology | GetEra |  | Era | 类别： nonconst |
| Technology | MakeScope |  | Scope |  |
| Theater | GetOwner |  | Country | 类别： nonconst |
| Theater | MakeScope |  | Scope |  |
| Theme | GetCategory |  | ThemeCategory | 类别： nonconst |
| Theme | GetRequiredDlc |  | Dlc | 类别： nonconst |
| ThemeBulkSelectionGroup | GetRequiredDlc |  | Dlc | 类别： nonconst |
| ThemeCategory | GetSelectedSingleChoiceTheme |  | Theme | 类别： nonconst |
| ThemeWindow | GetDayNightEnableManualTime |  | PdxSetting | 类别： nonconst |
| ThemeWindow | GetDayNightEnableSyncLocalTime |  | PdxSetting | 类别： nonconst |
| ThemeWindow | GetDayNightEnabled |  | PdxSetting | 类别： nonconst |
| ThemeWindow | GetDayNightManualTimeHour |  | PdxSetting | 类别： nonconst |
| ThemeWindow | GetDayNightSpeed |  | PdxSetting | 类别： nonconst |
| ThemeWindow | GetDayNightSunHours |  | PdxSetting | 类别： nonconst |
| ThemeWindow | GetDayNightTimeOfSunrise |  | PdxSetting | 类别： nonconst |
| ThemeWindow | GetSelectedBulkSelectionGroup |  | ThemeBulkSelectionGroup | 类别： nonconst |
| TickTaskDetailsView | GetTickTask |  | TickTaskData | 类别： nonconst |
| TickTaskGraphItem | GetTickTask |  | TickTaskData | 类别： nonconst |
| TimeKeeper | GetCurrentDate |  | Date | 类别： nonconst |
| ToastMessageHandler | GetMessageItem |  | PlayerMessageItem | 类别： nonconst |
| TopScope | AddList | Unknown Unknown | TopScope |  |
| TopScope | AddScope | Unknown Unknown | TopScope |  |
| TopScope | GetLocalVariable | Unknown | Scope | 类别： nonconst |
| TopScope | GetRootScope |  | Scope | 类别： nonconst |
| TopScope | SetRoot | Scope | TopScope |  |
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
| TopScope | sCU | CString | Culture |  |
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
| TopScope | sIdeology | CString | Ideology |  |
| TopScope | sInstitution | CString | Institution |  |
| TopScope | sInstitutionType | CString | InstitutionType |  |
| TopScope | sInterestGroupTrait | CString | InterestGroupTrait |  |
| TopScope | sJE | CString | JournalEntry |  |
| TopScope | sJournalEntry | CString | JournalEntry |  |
| TopScope | sL | CString | Law |  |
| TopScope | sLaw | CString | Law |  |
| TopScope | sLawType | CString | LawType |  |
| TopScope | sMilitaryFormation | CString | MilitaryFormation |  |
| TopScope | sP | CString | Party |  |
| TopScope | sPB | CString | PowerBloc |  |
| TopScope | sPBI | CString | PowerBlocIdentity |  |
| TopScope | sPBP | CString | PowerBlocPrinciple |  |
| TopScope | sPL | CString | PoliticalLobby |  |
| TopScope | sPLA | CString | PoliticalLobbyAppeasementFactor |  |
| TopScope | sPLT | CString | PoliticalLobbyType |  |
| TopScope | sPM | CString | PoliticalMovement |  |
| TopScope | sPMC | CString | PoliticalMovementCategory |  |
| TopScope | sPMT | CString | PoliticalMovementType |  |
| TopScope | sPT | CString | PopType |  |
| TopScope | sPact | CString | DiplomaticPact |  |
| TopScope | sParty | CString | Party |  |
| TopScope | sPoliticalLobby | CString | PoliticalLobby |  |
| TopScope | sPoliticalLobbyAppeasement | CString | PoliticalLobbyAppeasementFactor |  |
| TopScope | sPoliticalLobbyType | CString | PoliticalLobbyType |  |
| TopScope | sPoliticalMovement | CString | PoliticalMovement |  |
| TopScope | sPoliticalMovementCategory | CString | PoliticalMovementCategory |  |
| TopScope | sPoliticalMovementType | CString | PoliticalMovementType |  |
| TopScope | sPop | CString | Pop |  |
| TopScope | sPopType | CString | PopType |  |
| TopScope | sPowerBloc | CString | PowerBloc |  |
| TopScope | sPowerBlocIdentity | CString | PowerBlocIdentity |  |
| TopScope | sPowerBlocPrinciple | CString | PowerBlocPrinciple |  |
| TopScope | sPowerBlocPrincipleGroup | CString | PowerBlocPrincipleGroup |  |
| TopScope | sProvince | CString | Province |  |
| TopScope | sReligion | CString | Religion |  |
| TopScope | sS | CString | State |  |
| TopScope | sSR | CString | StrategicRegion |  |
| TopScope | sSW | CString | Sway |  |
| TopScope | sState | CString | State |  |
| TopScope | sStateRegion | CString | StateRegion |  |
| TopScope | sStrategicRegion | CString | StrategicRegion |  |
| TopScope | sSway | CString | Sway |  |
| TopScope | sT | CString | Technology |  |
| TopScope | sTechnology | CString | Technology |  |
| TopScope | sTreaty | CString | Treaty |  |
| TopScope | sTreatyArticle | CString | Article |  |
| TopScope | sW | CString | War |  |
| TopScope | sWar | CString | War |  |
| TopScope | sWarGoal | CString | WarGoal |  |
| TopScope | sWarGoalType | CString | WarGoalType |  |
| TransferFormationPopup | GetLeftFormation |  | MilitaryFormation | 类别： nonconst |
| TransferFormationPopup | GetLeftStagedFormation |  | StagedFormation | 类别： nonconst |
| TransferFormationPopup | GetRightFormation |  | MilitaryFormation | 类别： nonconst |
| TransferFormationPopup | GetRightStagedFormation |  | StagedFormation | 类别： nonconst |
| Treaty | GetBindingPeriodEndGameDate |  | Date | 类别： nonconst |
| Treaty | GetEnforcedOnCountry |  | Country | 类别： nonconst |
| Treaty | GetEnforcerCountry |  | Country | 类别： nonconst |
| Treaty | GetFirstCountry |  | Country | 类别： nonconst |
| Treaty | GetLeftCountry |  | Country | 类别： nonconst |
| Treaty | GetOtherCountry | Country | Country | 类别： nonconst |
| Treaty | GetRightCountry |  | Country | 类别： nonconst |
| Treaty | GetSecondCountry |  | Country | 类别： nonconst |
| Treaty | GetShippingLaneOf | Unknown | ShippingLane | 类别： nonconst |
| Treaty | GetStartGameDate |  | Date | 类别： nonconst |
| Treaty | MakeScope |  | Scope |  |
| TreatyDraft | GetAmendedTreaty |  | Treaty | 类别： nonconst |
| TreatyDraft | GetFirstCountry |  | Country | 类别： nonconst |
| TreatyDraft | GetLeftCountry |  | Country | 类别： nonconst |
| TreatyDraft | GetOtherCountry | Country | Country | 类别： nonconst |
| TreatyDraft | GetRightCountry |  | Country | 类别： nonconst |
| TreatyDraft | GetSecondCountry |  | Country | 类别： nonconst |
| TreatyDraftPanel | GetDraft |  | TreatyDraft | 类别： nonconst |
| TreatyPanel | GetTreaty |  | Treaty | 类别： nonconst |
| Truce | AccessFirstCountry |  | Country | 类别： const |
| Truce | AccessSecondCountry |  | Country | 类别： const |
| Truce | GetFirstCountry |  | Country | 类别： nonconst |
| Truce | GetSecondCountry |  | Country | 类别： nonconst |
| VariableEntry | AccessScopeEditor |  | ScopeObjectEditor | 类别： const |
| VariableInspectorEntry | AccessVariable |  | VariableInspectorVariable | 类别： const |
| VariableInspectorPlugin | AccessSetupVariable |  | VariableInspectorVariable | 类别： const |
| VariableInspectorVariable | AccessScopeEditor |  | ScopeObjectEditor | 类别： const |
| VariableListEntry | AccessScopeEditor |  | ScopeObjectEditor | 类别： const |
| VariableListInspectorPlugin | AccessListStore |  | VariableListStore | 类别： const |
| VariableListStore | AccessNewEntryEditor |  | ScopeObjectEditor | 类别： const |
| VariableStore | AccessNewEntryEditor |  | ScopeObjectEditor | 类别： const |
| VfsMountPathBrowser | GetFirstSelectedNode |  | VfsMountPathBrowserEntryNode | 类别： nonconst |
| ViewerEntity | State |  | ViewerEntityState |  |
| War | AccessAttackerLeaderParticipant |  | WarParticipant | 类别： const |
| War | AccessDefenderLeaderParticipant |  | WarParticipant | 类别： const |
| War | AccessDiplomaticPlay |  | DiplomaticPlay | 类别： const |
| War | AccessLeftSideLeaderParticipant |  | WarParticipant | 类别： const |
| War | AccessParticipant | Country | WarParticipant | 类别： const |
| War | AccessRightSideLeaderParticipant |  | WarParticipant | 类别： const |
| War | GetAttackerLeader |  | Country | 类别： nonconst |
| War | GetCountryProposingPeace |  | Country | 类别： nonconst |
| War | GetDefenderLeader |  | Country | 类别： nonconst |
| War | GetDiplomaticPlay |  | DiplomaticPlay | 类别： nonconst |
| War | GetLeaderOfOppositeSide | Country | Country | 类别： nonconst |
| War | MakeScope |  | Scope |  |
| WarGoal | GetArticleDraft |  | ArticleDraft | 类别：非常量 |
| WarGoal | GetArticleType |  | ArticleType | 类别：非常量 |
| WarGoal | GetCountryCreation |  | CountryCreation | 类别：非常量 |
| WarGoal | GetCountryFormation |  | CountryFormation | 类别：非常量 |
| WarGoal | GetCreator |  | Country | 类别：非常量 |
| WarGoal | GetDiplomaticPlay |  | DiplomaticPlay | 类别：非常量 |
| WarGoal | GetHolder |  | Country | 类别：非常量 |
| WarGoal | GetTarget |  | Country | 类别：非常量 |
| WarGoal | GetTargetState |  | State | 类别：非常量 |
| WarGoal | GetType |  | WarGoalType | 类别：非常量 |
| WarGoal | GetWar |  | War | 类别：非常量 |
| WarGoal | GetWarGoalStakeholder |  | Country | 类别：非常量 |
| WarGoal | MakeScope |  | Scope |  |
| WarGoalDraft | GetArticleDraft |  | ArticleDraft | 类别：非常量 |
| WarGoalDraft | GetArticleType |  | ArticleType | 类别：非常量 |
| WarGoalDraft | GetCountryCreation |  | CountryCreation | 类别：非常量 |
| WarGoalDraft | GetCountryFormation |  | CountryFormation | 类别：非常量 |
| WarGoalDraft | GetCreator |  | Country | 类别：非常量 |
| WarGoalDraft | GetDiplomaticPlay |  | DiplomaticPlay | 类别：非常量 |
| WarGoalDraft | GetHolder |  | Country | 类别：非常量 |
| WarGoalDraft | GetTarget |  | Country | 类别：非常量 |
| WarGoalDraft | GetTargetRegion |  | StrategicRegion | 类别：非常量 |
| WarGoalDraft | GetTargetState |  | State | 类别：非常量 |
| WarGoalDraft | GetType |  | WarGoalType | 类别：非常量 |
| WarGoalDraft | GetWarGoalStakeholder |  | Country | 类别：非常量 |
| WarGoalMarker | AccessWarGoal |  | WarGoal | 类别：常量 |
| WarGoalMarker | GetWarGoal |  | WarGoal | 类别：非常量 |
| WarGoalPanelPair | AccessPanel |  | WarPanel | 类别：常量 |
| WarGoalPanelPair | AccessWarGoal |  | WarGoal | 类别：常量 |
| WarGoalPanelPair | GetWar |  | War | 类别：非常量 |
| WarGoalPanelPair | GetWarGoal |  | WarGoal | 类别：非常量 |
| WarGoalType | MakeScope |  | Scope |  |
| WarPanel | AccessWar |  | War | 类别：常量 |
| WarPanel | GetLeftLeader |  | Country | 类别：非常量 |
| WarPanel | GetRightLeader |  | Country | 类别：非常量 |
| WarPanel | GetWar |  | War | 类别：非常量 |
| WarParticipant | AccessCountry |  | Country | 类别：常量 |
| WarParticipant | GetCountry |  | Country | 类别：非常量 |
| WarParticipant | GetWar |  | War | 类别：非常量 |

## 参考资料

1. ↑ 更准确地说，是“UpperCamelCase”或“PascalCase”（首字母大写的驼峰命名法）

---

- 如需更新表格，参见 [Module:GUI script/Functions](https://vic3.paradoxwikis.com/Module:GUI_script/Functions) 和 [Module:GUI script/Promotes](https://vic3.paradoxwikis.com/Module:GUI_script/Promotes)

Modding
返回顶部
| 文档 | [Defines](Defines.md) • [Effects](Effect.md) • [Event targets](Event target.md) • [Scopes](Scope.md) • [Triggers](Trigger.md) [Macros](Macro.md) • [Modifier types](Modifier types.md) • [On actions](https://vic3.paradoxwikis.com/On_actions) • [Script value](Script value.md) • [Variables](Variable.md) |
|---|---|

| 脚本化内容 | [Decisions](Decision modding.md) • [Events](Event modding.md) • [History](History modding.md) • [Journal](Journal modding.md) • [Modifiers](Modifier modding.md) • Objectives • [Scripted gui](Scripted gui.md) |
|---|---|

| 脚本化类型 | [Buildings](Building modding.md) • [Characters](Character modding.md) • Concepts • [Countries](Country modding.md) • [Culture](Culture modding.md) • [Decrees](Decree modding.md) • [Diplomacy](Diplomacy modding.md) • [Goods](Goods modding.md) • [Institutions](Institution modding.md) • [Interest groups](Interest group modding.md) • [Laws](Law modding.md) • Parties • [Pops](Pop modding.md) • [Power blocs](Power bloc modding.md) • [Religion](Religion modding.md) • Subject types • [Technology](Technology modding.md) • [Treaties](Treaty modding.md) • [War goals](War goal modding.md) |
|---|---|

| 地图 | [Map](Map modding.md) • [Geographic regions](Geographic region modding.md) • [States](State modding.md) |
|---|---|

| 界面 | [Interface](Interface modding.md) • GUI script • [Localization](Localization.md) • [Customizable localization](Localization.md) • [Script localization](Script localization.md) |
|---|---|

| 图形 | [3D Models](Model modding.md) • [Event images](Event images.md) • [Graphical Assets](Graphical asset modding.md) • Fonts • [Flags](Flag modding.md) |
|---|---|

| 音频 | Music • [Sound](Sound modding.md) |
|---|---|

| 其他 | [AI](AI modding.md) • [Console commands](Console commands.md) • [Checksum](https://vic3.paradoxwikis.com/Checksum) • [Mods](Mod.md) • [Mod compatibility](Mod compatibility.md) • [Mod structure](Mod structure.md) • [Scripted tests](Scripted test.md) • [Troubleshooting](Troubleshooting.md) |
|---|---|

| 指南 | [Mod translation](Mod translation.md) • [New country modding](New country modding.md) • [Save-game editing](Save-game editing.md) • [State modding guide](State modding guide.md) |
|---|---|