import json
from abc import abstractmethod
from pathlib import Path
from typing import List, Tuple, Union

import msgspec
from msgspec import Struct

from ...damage.Base.model import (
    DamageInstanceAvatar,
)
from ...damage.Base.SkillBase import BaseSkills
from ...excel.model import AvatarPromotionConfig
from ...model import MihomoAvatarSkill

path = Path(__file__).parent.parent
with Path.open(path / "Excel" / "SkillData.json", encoding="utf-8") as f:
    skill_dict = json.load(f)


class BaseAvatarAttribute(Struct):
    attack: float
    defence: float
    hp: float
    speed: float
    CriticalChanceBase: float
    CriticalDamageBase: float
    BaseAggro: float

    def items(self) -> List[Tuple[str, float]]:
        return [
            ("attack", self.attack),
            ("defence", self.defence),
            ("hp", self.hp),
            ("speed", self.speed),
            ("CriticalChanceBase", self.CriticalChanceBase),
            ("CriticalDamageBase", self.CriticalDamageBase),
            ("BaseAggro", self.BaseAggro),
        ]


class BaseAvatarBuff:
    @classmethod
    def create(cls, char: DamageInstanceAvatar, skills: List[MihomoAvatarSkill]):
        cls.extra_ability_id: List[int] = []
        if char.extra_ability:
            for extra_ability in char.extra_ability:
                cls.extra_ability_id.append(extra_ability.extraAbilityId)
        return cls

    @abstractmethod
    async def Technique(self): ...

    @abstractmethod
    async def eidolons(self): ...

    @abstractmethod
    async def extra_ability(self): ...


class BaseAvatarinfo:
    def __init__(self, char: DamageInstanceAvatar):
        self.avatar_id = char.id_
        self.avatar_level = char.level
        self.avatar_rank = char.rank
        self.avatar_element = char.element
        self.avatar_promotion = char.promotion
        self.avatar_attribute_bonus = char.attribute_bonus
        self.avatar_extra_ability = char.extra_ability
        self.avatar_attribute = self.get_attribute()

    def get_attribute(self):
        promotion = None

        for avatar in AvatarPromotionConfig:
            if avatar.AvatarID == self.avatar_id:
                promotion = avatar
                break
        if not promotion:
            msg = f"AvatarPromotionConfig not found: {self.avatar_id}"
            raise ValueError(msg)

        return BaseAvatarAttribute(
            # 攻击力
            attack=(
                promotion.AttackBase.Value
                + promotion.AttackAdd.Value * (self.avatar_level - 1)
            ),
            # 防御力
            defence=(
                promotion.DefenceBase.Value
                + promotion.DefenceAdd.Value * (self.avatar_level - 1)
            ),
            # 血量
            hp=(
                promotion.HPBase.Value + promotion.HPAdd.Value * (self.avatar_level - 1)
            ),
            # 速度
            speed=promotion.SpeedBase.Value,
            # 暴击率
            CriticalChanceBase=promotion.CriticalChance.Value,
            # 暴击伤害
            CriticalDamageBase=promotion.CriticalDamage.Value,
            # 嘲讽
            BaseAggro=promotion.BaseAggro.Value,
        )

    def Ultra_Use(self):
        skill_info = skill_dict[str(self.avatar_id)]["Ultra_Use"][0]
        return msgspec.convert(skill_info, type=float)


class BaseAvatar:
    def __init__(self, char: DamageInstanceAvatar, skills: List[MihomoAvatarSkill]):
        self.Skill = BaseSkills.create(char=char, skills=skills)
        self.Buff = BaseAvatarBuff.create(char=char, skills=skills)
        self.avatar_id = char.id_
        self.avatar_level = char.level
        self.avatar_rank = char.rank
        self.avatar_element = char.element
        self.avatar_promotion = char.promotion
        self.avatar_attribute_bonus = char.attribute_bonus
        self.avatar_extra_ability = char.extra_ability
        self.avatar_attribute = self.get_attribute()

    def get_attribute(self):
        promotion = None

        for avatar in AvatarPromotionConfig:
            if avatar.AvatarID == self.avatar_id:
                promotion = avatar
                break
        if not promotion:
            msg = f"AvatarPromotionConfig not found: {self.avatar_id}"
            raise ValueError(msg)

        return BaseAvatarAttribute(
            # 攻击力
            attack=(
                promotion.AttackBase.Value
                + promotion.AttackAdd.Value * (self.avatar_level - 1)
            ),
            # 防御力
            defence=(
                promotion.DefenceBase.Value
                + promotion.DefenceAdd.Value * (self.avatar_level - 1)
            ),
            # 血量
            hp=(
                promotion.HPBase.Value + promotion.HPAdd.Value * (self.avatar_level - 1)
            ),
            # 速度
            speed=promotion.SpeedBase.Value,
            # 暴击率
            CriticalChanceBase=promotion.CriticalChance.Value,
            # 暴击伤害
            CriticalDamageBase=promotion.CriticalDamage.Value,
            # 嘲讽
            BaseAggro=promotion.BaseAggro.Value,
        )

    def Skill_Info(self, skill_type: str):
        skill_info = skill_dict[str(self.avatar_id)]["skillList"][skill_type]
        return msgspec.convert(skill_info, type=List[Union[str, int]])

    def Skill_num(self, skill: Union[str, int], skill_type: str):
        skill_level = 0
        if skill == "Normal":
            skill_level = self.Skill.Normal_.level - 1
        if skill == "BPSkill":
            skill_level = self.Skill.BPSkill_.level - 1
        if skill == "Ultra":
            skill_level = self.Skill.Ultra_.level - 1
        if skill == "Talent":
            skill_level = self.Skill.Talent_.level - 1
        skill_info = skill_dict[str(self.avatar_id)][skill_type][skill_level]
        return msgspec.convert(skill_info, type=float)
