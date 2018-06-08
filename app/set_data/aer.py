
import sys
from app.models.card import Card
from app.models.set import Set
import inspect


AerialModification = Card("aerial_modification", "Aerial Modification", ['4', 'W'], ['W'], "Enchantment", "Aura", "AER", 1, 66561)
AeronautAdmiral = Card("aeronaut_admiral", "Aeronaut Admiral", ['3', 'W'], ['W'], "Creature", "Human Pilot", "AER", 2, 66562)
AetherInspector = Card("aether_inspector", "Aether Inspector", ['3', 'W'], ['W'], "Creature", "Dwarf Artificer", "AER", 3, 66563)
AethergeodeMiner = Card("aethergeode_miner", "Aethergeode Miner", ['1', 'W'], ['W'], "Creature", "Dwarf Scout", "AER", 4, 64543)
AirdropAeronauts = Card("airdrop_aeronauts", "Airdrop Aeronauts", ['3', 'W', 'W'], ['W'], "Creature", "Dwarf Scout", "AER", 5, 64211)
AlleyEvasion = Card("alley_evasion", "Alley Evasion", ['W'], ['W'], "Instant", "", "AER", 6, 64545)
AudaciousInfiltrator = Card("audacious_infiltrator", "Audacious Infiltrator", ['1', 'W'], ['W'], "Creature", "Dwarf Rogue", "AER", 7, 64547)
BastionEnforcer = Card("bastion_enforcer", "Bastion Enforcer", ['2', 'W'], ['W'], "Creature", "Dwarf Soldier", "AER", 8, 64187)
CallforUnity = Card("call_for_unity", "Call for Unity", ['3', 'W', 'W'], ['W'], "Enchantment", "", "AER", 9, 64219)
CaughtintheBrights = Card("caught_in_the_brights", "Caught in the Brights", ['2', 'W'], ['W'], "Enchantment", "Aura", "AER", 10, 64197)
ConsulateCrackdown = Card("consulate_crackdown", "Consulate Crackdown", ['3', 'W', 'W'], ['W'], "Enchantment", "", "AER", 11, 64549)
Conviction = Card("conviction", "Conviction", ['1', 'W'], ['W'], "Enchantment", "Aura", "AER", 12, 64181)
CountlessGearsRenegade = Card("countless_gears_renegade", "Countless Gears Renegade", ['1', 'W'], ['W'], "Creature", "Dwarf Artificer", "AER", 13, 64183)
DawnfeatherEagle = Card("dawnfeather_eagle", "Dawnfeather Eagle", ['4', 'W'], ['W'], "Creature", "Bird", "AER", 14, 64193)
DeadeyeHarpooner = Card("deadeye_harpooner", "Deadeye Harpooner", ['2', 'W'], ['W'], "Creature", "Dwarf Warrior", "AER", 15, 64203)
Decommission = Card("decommission", "Decommission", ['2', 'W'], ['W'], "Instant", "", "AER", 16, 64189)
DeftDismissal = Card("deft_dismissal", "Deft Dismissal", ['3', 'W'], ['W'], "Instant", "", "AER", 17, 64209)
ExquisiteArchangel = Card("exquisite_archangel", "Exquisite Archangel", ['5', 'W', 'W'], ['W'], "Creature", "Angel", "AER", 18, 64551)
FelidarGuardian = Card("felidar_guardian", "Felidar Guardian", ['3', 'W'], ['W'], "Creature", "Cat Beast", "AER", 19, 64205)
GhirapurOsprey = Card("ghirapur_osprey", "Ghirapur Osprey", ['2', 'W'], ['W'], "Creature", "Bird", "AER", 20, 64185)
RestorationSpecialist = Card("restoration_specialist", "Restoration Specialist", ['1', 'W'], ['W'], "Creature", "Dwarf Artificer", "AER", 21, 64199)
SolemnRecruit = Card("solemn_recruit", "Solemn Recruit", ['1', 'W', 'W'], ['W'], "Creature", "Dwarf Warrior", "AER", 22, 64217)
SramSeniorEdificer = Card("sram_senior_edificer", "Sram, Senior Edificer", ['1', 'W'], ['W'], "Legendary Creature", "Dwarf Advisor", "AER", 23, 64215)
SramsExpertise = Card("srams_expertise", "Sram's Expertise", ['2', 'W', 'W'], ['W'], "Sorcery", "", "AER", 24, 64553)
ThopterArrest = Card("thopter_arrest", "Thopter Arrest", ['2', 'W'], ['W'], "Enchantment", "", "AER", 25, 64201)
AetherSwooper = Card("aether_swooper", "Aether Swooper", ['1', 'U'], ['U'], "Creature", "Vedalken Artificer", "AER", 26, 64555)
AethertideWhale = Card("aethertide_whale", "Aethertide Whale", ['4', 'U', 'U'], ['U'], "Creature", "Whale", "AER", 27, 64271)
BaralChiefofCompliance = Card("baral_chief_of_compliance", "Baral, Chief of Compliance", ['1', 'U'], ['U'], "Legendary Creature", "Human Wizard", "AER", 28, 64273)
BaralsExpertise = Card("barals_expertise", "Baral's Expertise", ['3', 'U', 'U'], ['U'], "Sorcery", "", "AER", 29, 64557)
BastionInventor = Card("bastion_inventor", "Bastion Inventor", ['5', 'U'], ['U'], "Creature", "Vedalken Artificer", "AER", 30, 64559)
Disallow = Card("disallow", "Disallow", ['1', 'U', 'U'], ['U'], "Instant", "", "AER", 31, 64679)
DispersalTechnician = Card("dispersal_technician", "Dispersal Technician", ['4', 'U'], ['U'], "Creature", "Vedalken Artificer", "AER", 32, 64237)
EfficientConstruction = Card("efficient_construction", "Efficient Construction", ['3', 'U'], ['U'], "Enchantment", "", "AER", 33, 64561)
HinterlandDrake = Card("hinterland_drake", "Hinterland Drake", ['2', 'U'], ['U'], "Creature", "Drake", "AER", 34, 64233)
IceOver = Card("ice_over", "Ice Over", ['1', 'U'], ['U'], "Enchantment", "Aura", "AER", 35, 64231)
IllusionistsStratagem = Card("illusionists_stratagem", "Illusionist's Stratagem", ['3', 'U'], ['U'], "Instant", "", "AER", 36, 64563)
LeaveintheDust = Card("leave_in_the_dust", "Leave in the Dust", ['3', 'U'], ['U'], "Instant", "", "AER", 37, 64245)
MechanizedProduction = Card("mechanized_production", "Mechanized Production", ['2', 'U', 'U'], ['U'], "Enchantment", "Aura", "AER", 38, 64265)
MetallicRebuke = Card("metallic_rebuke", "Metallic Rebuke", ['2', 'U'], ['U'], "Instant", "", "AER", 39, 64239)
Negate = Card("negate", "Negate", ['1', 'U'], ['U'], "Instant", "", "AER", 40, 64235)
QuicksmithSpy = Card("quicksmith_spy", "Quicksmith Spy", ['3', 'U'], ['U'], "Creature", "Human Artificer", "AER", 41, 64267)
ReverseEngineer = Card("reverse_engineer", "Reverse Engineer", ['3', 'U', 'U'], ['U'], "Sorcery", "", "AER", 42, 64261)
SalvageScuttler = Card("salvage_scuttler", "Salvage Scuttler", ['4', 'U'], ['U'], "Creature", "Crab", "AER", 43, 64565)
ShieldedAetherThief = Card("shielded_aether_thief", "Shielded Aether Thief", ['1', 'U'], ['U'], "Creature", "Vedalken Rogue", "AER", 44, 64567)
ShipwreckMoray = Card("shipwreck_moray", "Shipwreck Moray", ['3', 'U'], ['U'], "Creature", "Fish", "AER", 45, 64681)
SkyshipPlunderer = Card("skyship_plunderer", "Skyship Plunderer", ['1', 'U'], ['U'], "Creature", "Human Pirate", "AER", 46, 64249)
TakeintoCustody = Card("take_into_custody", "Take into Custody", ['U'], ['U'], "Instant", "", "AER", 47, 64569)
TrophyMage = Card("trophy_mage", "Trophy Mage", ['2', 'U'], ['U'], "Creature", "Human Wizard", "AER", 48, 64571)
WhirofInvention = Card("whir_of_invention", "Whir of Invention", ['X', 'U', 'U', 'U'], ['U'], "Instant", "", "AER", 49, 64275)
WindKinRaiders = Card("windkin_raiders", "Wind-Kin Raiders", ['4', 'U', 'U'], ['U'], "Creature", "Human Artificer", "AER", 50, 64573)
AetherPoisoner = Card("aether_poisoner", "Aether Poisoner", ['1', 'B'], ['B'], "Creature", "Human Artificer", "AER", 51, 64575)
AlleyStrangler = Card("alley_strangler", "Alley Strangler", ['2', 'B'], ['B'], "Creature", "Aetherborn Rogue", "AER", 52, 64281)
BattleattheBridge = Card("battle_at_the_bridge", "Battle at the Bridge", ['X', 'B'], ['B'], "Sorcery", "", "AER", 53, 64319)
CruelFinality = Card("cruel_finality", "Cruel Finality", ['2', 'B'], ['B'], "Instant", "", "AER", 54, 64577)
DaringDemolition = Card("daring_demolition", "Daring Demolition", ['2', 'B', 'B'], ['B'], "Sorcery", "", "AER", 55, 64579)
DefiantSalvager = Card("defiant_salvager", "Defiant Salvager", ['2', 'B'], ['B'], "Creature", "Aetherborn Artificer", "AER", 56, 64285)
FatalPush = Card("fatal_push", "Fatal Push", ['B'], ['B'], "Instant", "", "AER", 57, 64311)
FenHauler = Card("fen_hauler", "Fen Hauler", ['6', 'B'], ['B'], "Creature", "Insect", "AER", 58, 64293)
FoundryHornet = Card("foundry_hornet", "Foundry Hornet", ['3', 'B'], ['B'], "Creature", "Insect", "AER", 59, 64299)
FourthBridgeProwler = Card("fourth_bridge_prowler", "Fourth Bridge Prowler", ['B'], ['B'], "Creature", "Human Rogue", "AER", 60, 64297)
GiftedAetherborn = Card("gifted_aetherborn", "Gifted Aetherborn", ['B', 'B'], ['B'], "Creature", "Aetherborn Vampire", "AER", 61, 64581)
GlintSleeveSiphoner = Card("glintsleeve_siphoner", "Glint-Sleeve Siphoner", ['1', 'B'], ['B'], "Creature", "Human Rogue", "AER", 62, 64325)
GontisMachinations = Card("gontis_machinations", "Gonti's Machinations", ['B'], ['B'], "Enchantment", "", "AER", 63, 64583)
HeraldofAnguish = Card("herald_of_anguish", "Herald of Anguish", ['5', 'B', 'B'], ['B'], "Creature", "Demon", "AER", 64, 64585)
IroncladRevolutionary = Card("ironclad_revolutionary", "Ironclad Revolutionary", ['4', 'B', 'B'], ['B'], "Creature", "Aetherborn Artificer", "AER", 65, 64317)
MidnightEntourage = Card("midnight_entourage", "Midnight Entourage", ['2', 'B', 'B'], ['B'], "Creature", "Aetherborn Rogue", "AER", 66, 64323)
NightMarketAeronaut = Card("night_market_aeronaut", "Night Market Aeronaut", ['3', 'B'], ['B'], "Creature", "Aetherborn Warrior", "AER", 67, 64289)
PerilousPredicament = Card("perilous_predicament", "Perilous Predicament", ['4', 'B'], ['B'], "Instant", "", "AER", 68, 64301)
RenegadesGetaway = Card("renegades_getaway", "Renegade's Getaway", ['2', 'B'], ['B'], "Instant", "", "AER", 69, 64587)
ResourcefulReturn = Card("resourceful_return", "Resourceful Return", ['1', 'B'], ['B'], "Sorcery", "", "AER", 70, 64683)
SecretSalvage = Card("secret_salvage", "Secret Salvage", ['3', 'B', 'B'], ['B'], "Sorcery", "", "AER", 71, 64589)
SlyRequisitioner = Card("sly_requisitioner", "Sly Requisitioner", ['4', 'B'], ['B'], "Creature", "Human Artificer", "AER", 72, 64591)
VengefulRebel = Card("vengeful_rebel", "Vengeful Rebel", ['2', 'B'], ['B'], "Creature", "Aetherborn Warrior", "AER", 73, 64303)
YahenniUndyingPartisan = Card("yahenni_undying_partisan", "Yahenni, Undying Partisan", ['2', 'B'], ['B'], "Legendary Creature", "Aetherborn Vampire", "AER", 74, 64315)
YahennisExpertise = Card("yahennis_expertise", "Yahenni's Expertise", ['2', 'B', 'B'], ['B'], "Sorcery", "", "AER", 75, 64593)
AetherChaser = Card("aether_chaser", "Aether Chaser", ['1', 'R'], ['R'], "Creature", "Human Artificer", "AER", 76, 64595)
ChandrasRevolution = Card("chandras_revolution", "Chandra's Revolution", ['3', 'R'], ['R'], "Sorcery", "", "AER", 77, 64597)
DestructiveTampering = Card("destructive_tampering", "Destructive Tampering", ['2', 'R'], ['R'], "Sorcery", "", "AER", 78, 64335)
EmbraalGearSmasher = Card("embraal_gearsmasher", "Embraal Gear-Smasher", ['2', 'R'], ['R'], "Creature", "Human Warrior", "AER", 79, 64601)
EnragedGiant = Card("enraged_giant", "Enraged Giant", ['5', 'R'], ['R'], "Creature", "Giant", "AER", 80, 64361)
FreejamRegent = Card("freejam_regent", "Freejam Regent", ['4', 'R', 'R'], ['R'], "Creature", "Dragon", "AER", 81, 64367)
FrontlineRebel = Card("frontline_rebel", "Frontline Rebel", ['2', 'R'], ['R'], "Creature", "Human Warrior", "AER", 82, 64603)
GremlinInfestation = Card("gremlin_infestation", "Gremlin Infestation", ['3', 'R'], ['R'], "Enchantment", "Aura", "AER", 83, 64357)
HungryFlames = Card("hungry_flames", "Hungry Flames", ['2', 'R'], ['R'], "Instant", "", "AER", 84, 64347)
IndomitableCreativity = Card("indomitable_creativity", "Indomitable Creativity", ['X', 'R', 'R', 'R'], ['R'], "Sorcery", "", "AER", 85, 64605)
InvigoratedRampage = Card("invigorated_rampage", "Invigorated Rampage", ['1', 'R'], ['R'], "Instant", "", "AER", 86, 64351)
KariZevSkyshipRaider = Card("kari_zev_skyship_raider", "Kari Zev, Skyship Raider", ['1', 'R'], ['R'], "Legendary Creature", "Human Pirate", "AER", 87, 64607)
KariZevsExpertise = Card("kari_zevs_expertise", "Kari Zev's Expertise", ['1', 'R', 'R'], ['R'], "Sorcery", "", "AER", 88, 64609)
LathnuSailback = Card("lathnu_sailback", "Lathnu Sailback", ['4', 'R'], ['R'], "Creature", "Lizard", "AER", 89, 64343)
LightningRunner = Card("lightning_runner", "Lightning Runner", ['3', 'R', 'R'], ['R'], "Creature", "Human Warrior", "AER", 90, 64375)
PiasRevolution = Card("pias_revolution", "Pia's Revolution", ['2', 'R'], ['R'], "Enchantment", "", "AER", 91, 64611)
PreciseStrike = Card("precise_strike", "Precise Strike", ['R'], ['R'], "Instant", "", "AER", 92, 64333)
QuicksmithRebel = Card("quicksmith_rebel", "Quicksmith Rebel", ['3', 'R'], ['R'], "Creature", "Human Artificer", "AER", 93, 64613)
RavenousIntruder = Card("ravenous_intruder", "Ravenous Intruder", ['1', 'R'], ['R'], "Creature", "Gremlin", "AER", 94, 64685)
RecklessRacer = Card("reckless_racer", "Reckless Racer", ['2', 'R'], ['R'], "Creature", "Human Pilot", "AER", 95, 64615)
ReleasetheGremlins = Card("release_the_gremlins", "Release the Gremlins", ['X', 'X', 'R'], ['R'], "Sorcery", "", "AER", 96, 64373)
ScrapperChampion = Card("scrapper_champion", "Scrapper Champion", ['3', 'R'], ['R'], "Creature", "Human Artificer", "AER", 97, 64617)
Shock = Card("shock", "Shock", ['R'], ['R'], "Instant", "", "AER", 98, 64173)
SiegeModification = Card("siege_modification", "Siege Modification", ['1', 'R', 'R'], ['R'], "Enchantment", "Aura", "AER", 99, 64355)
SweatworksBrawler = Card("sweatworks_brawler", "Sweatworks Brawler", ['3', 'R'], ['R'], "Creature", "Human Artificer", "AER", 100, 64339)
Wrangle = Card("wrangle", "Wrangle", ['1', 'R'], ['R'], "Sorcery", "", "AER", 101, 64345)
AetherHerder = Card("aether_herder", "Aether Herder", ['3', 'G'], ['G'], "Creature", "Elf Artificer Druid", "AER", 102, 64619)
AetherstreamLeopard = Card("aetherstream_leopard", "Aetherstream Leopard", ['2', 'G'], ['G'], "Creature", "Cat", "AER", 103, 64621)
AetherwindBasker = Card("aetherwind_basker", "Aetherwind Basker", ['4', 'G', 'G', 'G'], ['G'], "Creature", "Lizard", "AER", 104, 64687)
AidfromtheCowl = Card("aid_from_the_cowl", "Aid from the Cowl", ['3', 'G', 'G'], ['G'], "Enchantment", "", "AER", 105, 64427)
DruidoftheCowl = Card("druid_of_the_cowl", "Druid of the Cowl", ['1', 'G'], ['G'], "Creature", "Elf Druid", "AER", 106, 64381)
GreenbeltRampager = Card("greenbelt_rampager", "Greenbelt Rampager", ['G'], ['G'], "Creature", "Elephant", "AER", 107, 64623)
GreenwheelLiberator = Card("greenwheel_liberator", "Greenwheel Liberator", ['1', 'G'], ['G'], "Creature", "Elf Warrior", "AER", 108, 64421)
HeroicIntervention = Card("heroic_intervention", "Heroic Intervention", ['1', 'G'], ['G'], "Instant", "", "AER", 109, 64415)
HiddenHerbalists = Card("hidden_herbalists", "Hidden Herbalists", ['1', 'G'], ['G'], "Creature", "Human Druid", "AER", 110, 64625)
HighspireInfusion = Card("highspire_infusion", "Highspire Infusion", ['1', 'G'], ['G'], "Instant", "", "AER", 111, 64379)
LifecraftAwakening = Card("lifecraft_awakening", "Lifecraft Awakening", ['X', 'G'], ['G'], "Instant", "", "AER", 112, 64413)
LifecraftCavalry = Card("lifecraft_cavalry", "Lifecraft Cavalry", ['4', 'G'], ['G'], "Creature", "Elf Warrior", "AER", 113, 64391)
LifecraftersGift = Card("lifecrafters_gift", "Lifecrafter's Gift", ['3', 'G'], ['G'], "Instant", "", "AER", 114, 64627)
MaulfistRevolutionary = Card("maulfist_revolutionary", "Maulfist Revolutionary", ['1', 'G', 'G'], ['G'], "Creature", "Human Warrior", "AER", 115, 64399)
MonstrousOnslaught = Card("monstrous_onslaught", "Monstrous Onslaught", ['3', 'G', 'G'], ['G'], "Sorcery", "", "AER", 116, 64405)
NarnamRenegade = Card("narnam_renegade", "Narnam Renegade", ['G'], ['G'], "Creature", "Elf Warrior", "AER", 117, 64629)
NaturalObsolescence = Card("natural_obsolescence", "Natural Obsolescence", ['1', 'G'], ['G'], "Instant", "", "AER", 118, 64383)
PeemaAetherSeer = Card("peema_aetherseer", "Peema Aether-Seer", ['3', 'G'], ['G'], "Creature", "Elf Druid", "AER", 119, 64401)
PreyUpon = Card("prey_upon", "Prey Upon", ['G'], ['G'], "Sorcery", "", "AER", 120, 64631)
RidgescaleTusker = Card("ridgescale_tusker", "Ridgescale Tusker", ['3', 'G', 'G'], ['G'], "Creature", "Beast", "AER", 121, 64633)
RishkarPeemaRenegade = Card("rishkar_peema_renegade", "Rishkar, Peema Renegade", ['2', 'G'], ['G'], "Legendary Creature", "Elf Druid", "AER", 122, 64417)
RishkarsExpertise = Card("rishkars_expertise", "Rishkar's Expertise", ['4', 'G', 'G'], ['G'], "Sorcery", "", "AER", 123, 64635)
ScroungingBandar = Card("scrounging_bandar", "Scrounging Bandar", ['1', 'G'], ['G'], "Creature", "Cat Monkey", "AER", 124, 64637)
SilkweaverElite = Card("silkweaver_elite", "Silkweaver Elite", ['2', 'G'], ['G'], "Creature", "Elf Archer", "AER", 125, 64403)
UnbridledGrowth = Card("unbridled_growth", "Unbridled Growth", ['G'], ['G'], "Enchantment", "Aura", "AER", 126, 64387)
AjaniUnyielding = Card("ajani_unyielding", "Ajani Unyielding", ['4', 'G', 'W'], ['W', 'G'], "Legendary Planeswalker", "Ajani", "AER", 127, 64455)
DarkIntimations = Card("dark_intimations", "Dark Intimations", ['2', 'U', 'B', 'R'], ['U', 'B', 'R'], "Sorcery", "", "AER", 128, 64639)
HiddenStockpile = Card("hidden_stockpile", "Hidden Stockpile", ['W', 'B'], ['W', 'B'], "Enchantment", "", "AER", 129, 64443)
MaverickThopterist = Card("maverick_thopterist", "Maverick Thopterist", ['3', 'U', 'R'], ['U', 'R'], "Creature", "Human Artificer", "AER", 130, 64641)
OathofAjani = Card("oath_of_ajani", "Oath of Ajani", ['G', 'W'], ['W', 'G'], "Legendary Enchantment", "", "AER", 131, 64449)
OutlandBoar = Card("outland_boar", "Outland Boar", ['2', 'R', 'G'], ['R', 'G'], "Creature", "Boar", "AER", 132, 64437)
RenegadeRallier = Card("renegade_rallier", "Renegade Rallier", ['1', 'G', 'W'], ['W', 'G'], "Creature", "Human Warrior", "AER", 133, 64435)
RenegadeWheelsmith = Card("renegade_wheelsmith", "Renegade Wheelsmith", ['1', 'R', 'W'], ['W', 'R'], "Creature", "Dwarf Pilot", "AER", 134, 64643)
RogueRefiner = Card("rogue_refiner", "Rogue Refiner", ['1', 'G', 'U'], ['U', 'G'], "Creature", "Human Rogue", "AER", 135, 64645)
SpirePatrol = Card("spire_patrol", "Spire Patrol", ['2', 'W', 'U'], ['W', 'U'], "Creature", "Human Soldier", "AER", 136, 64445)
TezzerettheSchemer = Card("tezzeret_the_schemer", "Tezzeret the Schemer", ['2', 'U', 'B'], ['U', 'B'], "Legendary Planeswalker", "Tezzeret", "AER", 137, 64647)
TezzeretsTouch = Card("tezzerets_touch", "Tezzeret's Touch", ['1', 'U', 'B'], ['U', 'B'], "Enchantment", "Aura", "AER", 138, 64649)
WeldfastEngineer = Card("weldfast_engineer", "Weldfast Engineer", ['1', 'B', 'R'], ['B', 'R'], "Creature", "Human Artificer", "AER", 139, 64431)
WindingConstrictor = Card("winding_constrictor", "Winding Constrictor", ['B', 'G'], ['B', 'G'], "Creature", "Snake", "AER", 140, 64651)
AegisAutomaton = Card("aegis_automaton", "Aegis Automaton", ['2'], ['W'], "Artifact Creature", "Construct", "AER", 141, 64467)
AethersphereHarvester = Card("aethersphere_harvester", "Aethersphere Harvester", ['3'], [], "Artifact", "Vehicle", "AER", 142, 64689)
AugmentingAutomaton = Card("augmenting_automaton", "Augmenting Automaton", ['1'], ['B'], "Artifact Creature", "Construct", "AER", 143, 64481)
BarricadeBreaker = Card("barricade_breaker", "Barricade Breaker", ['7'], [], "Artifact Creature", "Juggernaut", "AER", 144, 64515)
CogworkAssembler = Card("cogwork_assembler", "Cogwork Assembler", ['3'], [], "Artifact Creature", "Assembly-Worker", "AER", 145, 64509)
ConsulateDreadnought = Card("consulate_dreadnought", "Consulate Dreadnought", ['1'], [], "Artifact", "Vehicle", "AER", 146, 64501)
ConsulateTurret = Card("consulate_turret", "Consulate Turret", ['3'], [], "Artifact", "", "AER", 147, 64507)
CrackdownConstruct = Card("crackdown_construct", "Crackdown Construct", ['4'], [], "Artifact Creature", "Construct", "AER", 148, 64655)
DaredevilDragster = Card("daredevil_dragster", "Daredevil Dragster", ['3'], [], "Artifact", "Vehicle", "AER", 149, 64523)
FiligreeCrawler = Card("filigree_crawler", "Filigree Crawler", ['4'], [], "Artifact Creature", "Insect", "AER", 150, 64657)
FoundryAssembler = Card("foundry_assembler", "Foundry Assembler", ['5'], [], "Artifact Creature", "Assembly-Worker", "AER", 151, 64495)
GontisAetherHeart = Card("gontis_aether_heart", "Gonti's Aether Heart", ['6'], [], "Legendary Artifact", "", "AER", 152, 64659)
HeartofKiran = Card("heart_of_kiran", "Heart of Kiran", ['2'], [], "Legendary Artifact", "Vehicle", "AER", 153, 64535)
HopeofGhirapur = Card("hope_of_ghirapur", "Hope of Ghirapur", ['1'], [], "Legendary Artifact Creature", "Thopter", "AER", 154, 64661)
ImplementofCombustion = Card("implement_of_combustion", "Implement of Combustion", ['1'], ['R'], "Artifact", "", "AER", 155, 64461)
ImplementofExamination = Card("implement_of_examination", "Implement of Examination", ['3'], ['U'], "Artifact", "", "AER", 156, 64479)
ImplementofFerocity = Card("implement_of_ferocity", "Implement of Ferocity", ['1'], ['G'], "Artifact", "", "AER", 157, 64469)
ImplementofImprovement = Card("implement_of_improvement", "Implement of Improvement", ['1'], ['W'], "Artifact", "", "AER", 158, 64691)
ImplementofMalice = Card("implement_of_malice", "Implement of Malice", ['2'], ['B'], "Artifact", "", "AER", 159, 64475)
InspiringStatuary = Card("inspiring_statuary", "Inspiring Statuary", ['3'], [], "Artifact", "", "AER", 160, 64663)
IrontreadCrusher = Card("irontread_crusher", "Irontread Crusher", ['4'], [], "Artifact", "Vehicle", "AER", 161, 64485)
LifecraftersBestiary = Card("lifecrafters_bestiary", "Lifecrafter's Bestiary", ['3'], ['G'], "Artifact", "", "AER", 162, 64665)
MerchantsDockhand = Card("merchants_dockhand", "Merchant's Dockhand", ['1'], ['U'], "Artifact Creature", "Construct", "AER", 163, 64667)
MetallicMimic = Card("metallic_mimic", "Metallic Mimic", ['2'], [], "Artifact Creature", "Shapeshifter", "AER", 164, 64669)
MobileGarrison = Card("mobile_garrison", "Mobile Garrison", ['3'], [], "Artifact", "Vehicle", "AER", 165, 64473)
NightMarketGuard = Card("night_market_guard", "Night Market Guard", ['3'], [], "Artifact Creature", "Construct", "AER", 166, 64477)
Ornithopter = Card("ornithopter", "Ornithopter", ['0'], [], "Artifact Creature", "Thopter", "AER", 167, 64497)
PacificationArray = Card("pacification_array", "Pacification Array", ['1'], [], "Artifact", "", "AER", 168, 64503)
ParadoxEngine = Card("paradox_engine", "Paradox Engine", ['5'], [], "Legendary Artifact", "", "AER", 169, 64533)
PeacewalkerColossus = Card("peacewalker_colossus", "Peacewalker Colossus", ['3'], ['W'], "Artifact", "Vehicle", "AER", 170, 64527)
PlanarBridge = Card("planar_bridge", "Planar Bridge", ['6'], [], "Legendary Artifact", "", "AER", 171, 64539)
PrizefighterConstruct = Card("prizefighter_construct", "Prizefighter Construct", ['5'], [], "Artifact Creature", "Construct", "AER", 172, 64671)
RenegadeMap = Card("renegade_map", "Renegade Map", ['1'], [], "Artifact", "", "AER", 173, 64459)
ReservoirWalker = Card("reservoir_walker", "Reservoir Walker", ['5'], [], "Artifact Creature", "Construct", "AER", 174, 64491)
ScrapTrawler = Card("scrap_trawler", "Scrap Trawler", ['3'], [], "Artifact Creature", "Construct", "AER", 175, 64521)
ServoSchematic = Card("servo_schematic", "Servo Schematic", ['2'], [], "Artifact", "", "AER", 176, 64673)
TreasureKeeper = Card("treasure_keeper", "Treasure Keeper", ['4'], [], "Artifact Creature", "Construct", "AER", 177, 64513)
UniversalSolvent = Card("universal_solvent", "Universal Solvent", ['1'], [], "Artifact", "", "AER", 178, 64463)
UntetheredExpress = Card("untethered_express", "Untethered Express", ['4'], [], "Artifact", "Vehicle", "AER", 179, 64505)
VerdantAutomaton = Card("verdant_automaton", "Verdant Automaton", ['2'], ['G'], "Artifact Creature", "Construct", "AER", 180, 64487)
WalkingBallista = Card("walking_ballista", "Walking Ballista", ['X', 'X'], [], "Artifact Creature", "Construct", "AER", 181, 64675)
WatchfulAutomaton = Card("watchful_automaton", "Watchful Automaton", ['3'], ['U'], "Artifact Creature", "Construct", "AER", 182, 64483)
WelderAutomaton = Card("welder_automaton", "Welder Automaton", ['2'], ['R'], "Artifact Creature", "Construct", "AER", 183, 64677)
SpireofIndustry = Card("spire_of_industry", "Spire of Industry", [], [], "Land", "", "AER", 184, 64531)
AjaniValiantProtector = Card("ajani_valiant_protector", "Ajani, Valiant Protector", ['4', 'G', 'W'], ['W', 'G'], "Legendary Planeswalker", "Ajani", "AER", 185, 65917)
InspiringRoar = Card("inspiring_roar", "Inspiring Roar", ['3', 'W'], ['W'], "Sorcery", "", "AER", 186, 65919)
AjanisComrade = Card("ajanis_comrade", "Ajani's Comrade", ['1', 'G'], ['G'], "Creature", "Elf Soldier", "AER", 187, 65921)
AjanisAid = Card("ajanis_aid", "Ajani's Aid", ['2', 'G', 'W'], ['W', 'G'], "Enchantment", "", "AER", 188, 65923)
TranquilExpanse = Card("tranquil_expanse", "Tranquil Expanse", [], ['G', 'W'], "Land", "", "AER", 189, 65925)
TezzeretMasterofMetal = Card("tezzeret_master_of_metal", "Tezzeret, Master of Metal", ['4', 'U', 'B'], ['U', 'B'], "Legendary Planeswalker", "Tezzeret", "AER", 190, 65927)
TezzeretsBetrayal = Card("tezzerets_betrayal", "Tezzeret's Betrayal", ['3', 'U', 'B'], ['U', 'B'], "Sorcery", "", "AER", 191, 65929)
PendulumofPatterns = Card("pendulum_of_patterns", "Pendulum of Patterns", ['2'], [], "Artifact", "", "AER", 192, 65931)
TezzeretsSimulacrum = Card("tezzerets_simulacrum", "Tezzeret's Simulacrum", ['3'], [], "Artifact Creature", "Golem", "AER", 193, 65933)
SubmergedBoneyard = Card("submerged_boneyard", "Submerged Boneyard", [], ['U', 'B'], "Land", "", "AER", 194, 65935)

clsmembers = [card for name, card in inspect.getmembers(sys.modules[__name__]) if isinstance(card, Card)]
AetherRevolt = Set("aether_revolt", cards=clsmembers)

