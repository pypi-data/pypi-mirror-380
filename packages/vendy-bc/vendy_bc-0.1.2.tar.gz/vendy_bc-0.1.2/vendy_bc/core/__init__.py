from __future__ import annotations
from typing import Any

from requests.exceptions import ConnectionError
from requests import Response
from json.decoder import JSONDecodeError
from vendy_bc.cli import color

from vendy_bc.core import (
    country_code,
    crypto,
    game,
    game_version,
    io,
    locale_handler,
    log,
    server,
    theme_handler,
    max_value_helper,
)
from vendy_bc.core.country_code import CountryCode, CountryCodeType
from vendy_bc.core.crypto import Hash, HashAlgorithm, Hmac, NyankoSignature, Random
from vendy_bc.core.game.battle.battle_items import BattleItems
from vendy_bc.core.game.battle.cleared_slots import ClearedSlots
from vendy_bc.core.game.battle.slots import LineUps
from vendy_bc.core.game.battle.enemy import (
    Enemy,
    EnemyNames,
    EnemyDescriptions,
    EnemyDictionary,
)
from vendy_bc.core.game.catbase.beacon_base import BeaconEventListScene
from vendy_bc.core.game.catbase.cat import Cat, Cats, UnitBuy, TalentData
from vendy_bc.core.game.catbase.gambling import GamblingEvent
from vendy_bc.core.game.catbase.gatya import (
    Gatya,
    GatyaInfos,
    GatyaDataSet,
    GatyaDataOptionSet,
    GatyaDataOption,
)
from vendy_bc.core.game.catbase.gatya_item import (
    GatyaItemBuy,
    GatyaItemNames,
    GatyaItemCategory,
    GatyaItemBuyItem,
)
from vendy_bc.core.game.catbase.item_pack import (
    ItemPack,
    Purchases,
    PurchaseSet,
    PurchasedPack,
)
from vendy_bc.core.game.catbase.login_bonuses import LoginBonus
from vendy_bc.core.game.catbase.matatabi import Matatabi
from vendy_bc.core.game.catbase.drop_chara import CharaDrop
from vendy_bc.core.game.catbase.medals import Medals, MedalNames
from vendy_bc.core.game.catbase.mission import (
    Missions,
    MissionNames,
    MissionConditions,
)
from vendy_bc.core.game.catbase.my_sale import MySale
from vendy_bc.core.game.catbase.nyanko_club import NyankoClub
from vendy_bc.core.game.catbase.officer_pass import OfficerPass
from vendy_bc.core.game.catbase.powerup import PowerUpHelper
from vendy_bc.core.game.catbase.scheme_items import SchemeItems
from vendy_bc.core.game.catbase.special_skill import (
    SpecialSkills,
    SpecialSkill,
    AbilityData,
    AbilityDataItem,
)

from vendy_bc.core.game.catbase.stamp import StampData
from vendy_bc.core.game.catbase.talent_orbs import (
    TalentOrb,
    TalentOrbs,
    OrbInfo,
    OrbInfoList,
    RawOrbInfo,
    SaveOrb,
    SaveOrbs,
)
from vendy_bc.core.game.catbase.unlock_popups import UnlockPopups
from vendy_bc.core.game.catbase.upgrade import Upgrade
from vendy_bc.core.game.catbase.user_rank_rewards import (
    UserRankRewards,
    RankGifts,
    RankGiftDescriptions,
)
from vendy_bc.core.game.catbase.playtime import PlayTime
from vendy_bc.core.game.gamoto.base_materials import BaseMaterials
from vendy_bc.core.game.gamoto.cat_shrine import CatShrine, CatShrineLevels
from vendy_bc.core.game.gamoto.gamatoto import (
    Gamatoto,
    GamatotoLevels,
    GamatotoMembersName,
)
from vendy_bc.core.game.gamoto.ototo import Ototo
from vendy_bc.core.game.localizable import Localizable
from vendy_bc.core.game.map.aku import AkuChapters
from vendy_bc.core.game.map.challenge import ChallengeChapters
from vendy_bc.core.game.map.chapters import Chapters
from vendy_bc.core.game.map.dojo import Dojo
from vendy_bc.core.game.map.enigma import Enigma
from vendy_bc.core.game.map.event import EventChapters
from vendy_bc.core.game.map.ex_stage import ExChapters
from vendy_bc.core.game.map.gauntlets import GauntletChapters
from vendy_bc.core.game.map.item_reward_stage import ItemRewardChapters
from vendy_bc.core.game.map.legend_quest import LegendQuestChapters
from vendy_bc.core.game.map.map_reset import MapResets
from vendy_bc.core.game.map.outbreaks import Outbreaks
from vendy_bc.core.game.map.story import StoryChapters, TreasureText, StageNames
from vendy_bc.core.game.map.timed_score import TimedScoreChapters
from vendy_bc.core.game.map.tower import TowerChapters
from vendy_bc.core.game.map.uncanny import UncannyChapters
from vendy_bc.core.game.map.zero_legends import ZeroLegendsChapters
from vendy_bc.core.game.map.map_names import MapNames
from vendy_bc.core.game_version import GameVersion
from vendy_bc.core.io.adb_handler import AdbHandler, AdbNotInstalled
from vendy_bc.core.io.waydroid import WayDroidHandler
from vendy_bc.core.io.bc_csv import CSV, Delimeter, Row
from vendy_bc.core.io.command import Command, CommandResult
from vendy_bc.core.io.config import Config, ConfigKey
from vendy_bc.core.io.data import Data
from vendy_bc.core.io.json_file import JsonFile
from vendy_bc.core.io.path import Path
from vendy_bc.core.io.save import SaveError, SaveFile, CantDetectSaveCCError
from vendy_bc.core.io.thread_helper import thread_run_many, Thread
from vendy_bc.core.io.yaml import YamlFile
from vendy_bc.core.io.git_handler import GitHandler, Repo
from vendy_bc.core.io.root_handler import RootHandler
from vendy_bc.core.locale_handler import (
    LocalManager,
    ExternalLocaleManager,
    ExternalLocale,
)
from vendy_bc.core.log import Logger
from vendy_bc.core.server.event_data import (
    ServerItemData,
    ServerItemDataItem,
    ServerGatyaData,
    ServerGatyaDataSet,
    ServerGatyaDataItem,
)
from vendy_bc.core.server.client_info import ClientInfo
from vendy_bc.core.server.game_data_getter import GameDataGetter
from vendy_bc.core.server.headers import AccountHeaders
from vendy_bc.core.server.managed_item import (
    BackupMetaData,
    ManagedItem,
    ManagedItemType,
)
from vendy_bc.core.server.request import RequestHandler, MultiPartFile, MultipartForm
from vendy_bc.core.server.server_handler import ServerHandler
from vendy_bc.core.server.updater import Updater
from vendy_bc.core.theme_handler import (
    ThemeHandler,
    ExternalTheme,
    ExternalThemeManager,
)
from vendy_bc.core.max_value_helper import MaxValueHelper, MaxValueType


class CoreData:
    def init_data(self):
        self.config = Config(config_path, print_config_err)
        self.logger = Logger(log_path)
        self.local_manager = LocalManager()
        self.theme_manager = ThemeHandler()
        self.max_value_manager = MaxValueHelper()
        self.game_data_getter: GameDataGetter | None = None
        self.gatya_item_names: GatyaItemNames | None = None
        self.gatya_item_buy: GatyaItemBuy | None = None
        self.chara_drop: CharaDrop | None = None
        self.gamatoto_levels: GamatotoLevels | None = None
        self.gamatoto_members_name: GamatotoMembersName | None = None
        self.localizable: Localizable | None = None
        self.abilty_data: AbilityData | None = None
        self.enemy_names: EnemyNames | None = None
        self.rank_gift_descriptions: RankGiftDescriptions | None = None
        self.rank_gifts: RankGifts | None = None
        self.treasure_text: TreasureText | None = None
        self.cat_shrine_levels: CatShrineLevels | None = None
        self.medal_names: MedalNames | None = None
        self.mission_names: MissionNames | None = None
        self.mission_conditions: MissionConditions | None = None

    def get_game_data_getter(
        self,
        save: SaveFile | None = None,
        cc: CountryCode | None = None,
        gv: GameVersion | None = None,
    ) -> GameDataGetter:
        if self.game_data_getter is None:
            if cc is None and save is not None:
                cc = save.cc
            if cc is None:
                raise ValueError("cc must be provided if save is not provided")
            if gv is None and save is not None:
                gv = save.game_version
            if gv is None:
                raise ValueError("gv must be provided if save is not provided")
            self.game_data_getter = GameDataGetter(cc, gv)
        return self.game_data_getter

    def get_gatya_item_names(self, save: SaveFile) -> GatyaItemNames:
        if self.gatya_item_names is None:
            self.gatya_item_names = GatyaItemNames(save)
        return self.gatya_item_names

    def get_gatya_item_buy(self, save: SaveFile) -> GatyaItemBuy:
        if self.gatya_item_buy is None:
            self.gatya_item_buy = GatyaItemBuy(save)
        return self.gatya_item_buy

    def get_chara_drop(self, save: SaveFile) -> CharaDrop:
        if self.chara_drop is None:
            self.chara_drop = CharaDrop(save)
        return self.chara_drop

    def get_gamatoto_levels(self, save: SaveFile) -> GamatotoLevels:
        if self.gamatoto_levels is None:
            self.gamatoto_levels = GamatotoLevels(save)
        return self.gamatoto_levels

    def get_gamatoto_members_name(self, save: SaveFile) -> GamatotoMembersName:
        if self.gamatoto_members_name is None:
            self.gamatoto_members_name = GamatotoMembersName(save)
        return self.gamatoto_members_name

    def get_localizable(self, save: SaveFile) -> Localizable:
        if self.localizable is None:
            self.localizable = Localizable(save)
        return self.localizable

    def get_ability_data(self, save: SaveFile) -> AbilityData:
        if self.abilty_data is None:
            self.abilty_data = AbilityData(save)
        return self.abilty_data

    def get_enemy_names(self, save: SaveFile) -> EnemyNames:
        if self.enemy_names is None:
            self.enemy_names = EnemyNames(save)
        return self.enemy_names

    def get_rank_gift_descriptions(self, save: SaveFile) -> RankGiftDescriptions:
        if self.rank_gift_descriptions is None:
            self.rank_gift_descriptions = RankGiftDescriptions(save)
        return self.rank_gift_descriptions

    def get_rank_gifts(self, save: SaveFile) -> RankGifts:
        if self.rank_gifts is None:
            self.rank_gifts = RankGifts(save)
        return self.rank_gifts

    def get_treasure_text(self, save: SaveFile) -> TreasureText:
        if self.treasure_text is None:
            self.treasure_text = TreasureText(save)
        return self.treasure_text

    def get_cat_shrine_levels(self, save: SaveFile) -> CatShrineLevels:
        if self.cat_shrine_levels is None:
            self.cat_shrine_levels = CatShrineLevels(save)
        return self.cat_shrine_levels

    def get_medal_names(self, save: SaveFile) -> MedalNames:
        if self.medal_names is None:
            self.medal_names = MedalNames(save)
        return self.medal_names

    def get_mission_names(self, save: SaveFile) -> MissionNames:
        if self.mission_names is None:
            self.mission_names = MissionNames(save)
        return self.mission_names

    def get_mission_conditions(self, save: SaveFile) -> MissionConditions:
        if self.mission_conditions is None:
            self.mission_conditions = MissionConditions(save)
        return self.mission_conditions

    def get_lang(self, save: SaveFile) -> str:
        return self.get_localizable(save).get_lang() or "en"


config_path = None
print_config_err = True
log_path = None


def set_config_path(path: Path):
    global config_path
    config_path = path


def set_log_path(path: Path):
    global log_path
    log_path = path


def update_external_content(_: Any = None):
    """Updates external content."""

    color.ColoredText.localize("updating_external_content")
    print()
    ExternalThemeManager.update_all_external_themes()
    ExternalLocaleManager.update_all_external_locales()
    core_data.init_data()


def print_no_internet():
    color.ColoredText.localize("no_internet")



core_data = CoreData()
core_data.init_data()


def localize(key: str, escape: bool = True, **kwargs: Any) -> str:
    return core_data.local_manager.get_key(key, escape=escape, **kwargs)


__all__ = [
    "server",
    "io",
    "locale_handler",
    "country_code",
    "log",
    "game_version",
    "crypto",
    "game",
    "theme_handler",
    "max_value_helper",
    "AdbHandler",
    "AdbNotInstalled",
    "CountryCode",
    "Path",
    "Data",
    "CSV",
    "ServerHandler",
    "GameVersion",
    "SaveFile",
    "JsonFile",
    "ManagedItem",
    "ManagedItemType",
    "BackupMetaData",
    "Cat",
    "Upgrade",
    "PowerUpHelper",
    "TalentOrb",
    "TalentOrbs",
    "OrbInfo",
    "OrbInfoList",
    "RawOrbInfo",
    "SaveOrb",
    "SaveOrbs",
    "ConfigKey",
    "SpecialSkill",
    "WayDroidHandler",
    "EnemyDescriptions",
    "EnemyDictionary",
    "GatyaItemCategory",
    "ServerItemData",
    "GatyaItemBuyItem",
    "ServerItemDataItem",
    "ServerGatyaData",
    "ServerGatyaDataSet",
    "ServerGatyaDataItem",
    "GatyaDataOptionSet",
    "GatyaDataOption",
    "MaxValueType",
    "GamblingEvent",
]
