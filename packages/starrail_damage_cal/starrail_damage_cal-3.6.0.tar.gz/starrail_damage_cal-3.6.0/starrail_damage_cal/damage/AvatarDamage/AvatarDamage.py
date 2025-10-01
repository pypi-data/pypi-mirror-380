import copy
from typing import Dict, List

from ...damage.Base.AvatarBase import BaseAvatar, BaseAvatarBuff
from ...damage.Base.model import (
    DamageInstanceAvatar,
)
from ...damage.Role import (
    break_damage,
    calculate_damage,
    calculate_heal,
    calculate_shield,
)
from ...logger import logger
from ...model import MihomoAvatarSkill


class Seele(BaseAvatar):
    Buff: BaseAvatarBuff

    def __init__(self, char: DamageInstanceAvatar, skills: List[MihomoAvatarSkill]):
        super().__init__(char=char, skills=skills)
        self.eidolon_attribute: Dict[str, float] = {}
        self.extra_ability_attribute: Dict[str, float] = {}
        self.eidolons()
        self.extra_ability()

    def Technique(self):
        pass

    def eidolons(self):
        if self.avatar_rank < 2:
            self.eidolon_attribute["SpeedAddedRatio"] = 0.25
        if self.avatar_rank >= 1:
            self.eidolon_attribute["CriticalChanceBase"] = 0.15
        if self.avatar_rank >= 2:
            self.eidolon_attribute["SpeedAddedRatio"] = 0.5

    def extra_ability(self):
        # 额外能力 割裂 抗性穿透提高20
        self.extra_ability_attribute["QuantumResistancePenetration"] = 0.2

    async def getdamage(
        self,
        base_attr: Dict[str, float],
        attribute_bonus: Dict[str, float],
    ):
        # logger.info(base_attr)
        # logger.info(self.avatar_rank)

        # 希尔天赋再现加伤害
        attribute_bonus["AllDamageAddedRatio"] = self.Skill_num(
            "Talent",
            "Talent",
        ) + attribute_bonus.get("AllDamageAddedRatio", 0)

        skill_info_list = []
        # 计算普攻伤害
        skill_multiplier = self.Skill_num("Normal", "Normal")
        damagelist1 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Normal",
            "Normal",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "普攻", "damagelist": damagelist1})

        # 计算战技伤害
        skill_multiplier = self.Skill_num("BPSkill", "BPSkill")
        damagelist2 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "BPSkill",
            "BPSkill",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "战技", "damagelist": damagelist2})

        # 计算大招伤害
        skill_multiplier = self.Skill_num("Ultra", "Ultra")
        damagelist3 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Ultra",
            "Ultra",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "终结技", "damagelist": damagelist3})

        # 银狼降防终结技伤害
        skill_multiplier = self.Skill_num("Ultra", "Ultra")
        add_attr_bonus = copy.deepcopy(attribute_bonus)
        add_attr_bonus["ignore_defence"] = 0.45 + add_attr_bonus.get(
            "ignore_defence", 0
        )
        damagelist4 = await calculate_damage(
            base_attr,
            add_attr_bonus,
            "Ultra",
            "Ultra",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "银狼降防终结技", "damagelist": damagelist4})

        logger.info(skill_info_list)
        return skill_info_list


class JingYuan(BaseAvatar):
    Buff: BaseAvatarBuff

    def __init__(self, char: DamageInstanceAvatar, skills: List[MihomoAvatarSkill]):
        super().__init__(char=char, skills=skills)
        self.eidolon_attribute: Dict[str, float] = {}
        self.extra_ability_attribute: Dict[str, float] = {}
        self.eidolons()
        self.extra_ability()

    def Technique(self):
        pass

    def eidolons(self):
        if self.avatar_rank >= 2:
            self.eidolon_attribute["NormalDmgAdd"] = 0.2
            self.eidolon_attribute["BPSkillDmgAdd"] = 0.2
            self.eidolon_attribute["UltraDmgAdd"] = 0.2
        if self.avatar_rank >= 6:
            self.eidolon_attribute["Talent_DmgRatio"] = 0.288

    def extra_ability(self):
        logger.info("额外能力")
        logger.info(
            "【神君】下回合的攻击段数大于等于6段, 则其下回合的暴击伤害提高25%。",
        )
        self.extra_ability_attribute["CriticalDamageBase"] = 0.25
        logger.info("施放战技后, 暴击率提升10%")
        self.extra_ability_attribute["CriticalChanceBase"] = 0.1

    async def getdamage(
        self,
        base_attr: Dict[str, float],
        attribute_bonus: Dict[str, float],
    ):
        skill_info_list = []
        # 计算普攻伤害
        skill_multiplier = self.Skill_num("Normal", "Normal")
        damagelist1 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Normal",
            "Normal",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "普攻", "damagelist": damagelist1})

        # 计算战技伤害
        skill_multiplier = self.Skill_num("BPSkill", "BPSkill")
        damagelist2 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "BPSkill",
            "BPSkill",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "战技", "damagelist": damagelist2})

        # 计算大招伤害
        skill_multiplier = self.Skill_num("Ultra", "Ultra")
        damagelist3 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Ultra",
            "Ultra",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "终结技", "damagelist": damagelist3})

        # 神君
        skill_multiplier = self.Skill_num("Talent", "Talent")
        damagelist4 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Talent",
            "Talent",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "10层神君伤害", "damagelist": damagelist4})

        logger.info(skill_info_list)
        return skill_info_list


class Welt(BaseAvatar):
    Buff: BaseAvatarBuff

    def __init__(self, char: DamageInstanceAvatar, skills: List[MihomoAvatarSkill]):
        super().__init__(char=char, skills=skills)
        self.eidolon_attribute: Dict[str, float] = {}
        self.extra_ability_attribute: Dict[str, float] = {}
        self.eidolons()
        self.extra_ability()

    def Technique(self):
        pass

    def eidolons(self):
        pass

    def extra_ability(self):
        logger.info("额外能力")
        logger.info("施放终结技时, 有100%基础概率使目标受到的伤害提高12%, 持续2回合。")
        self.extra_ability_attribute["DmgRatio"] = 0.12
        logger.info("对被弱点击破的敌方目标造成的伤害提高20")
        self.extra_ability_attribute["AllDamageAddedRatio"] = 0.20

    async def getdamage(
        self,
        base_attr: Dict[str, float],
        attribute_bonus: Dict[str, float],
    ):
        skill_info_list = []
        # 计算普攻伤害
        skill_multiplier = self.Skill_num("Normal", "Normal")
        damagelist1 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Normal",
            "Normal",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "普攻", "damagelist": damagelist1})

        # 计算战技伤害
        attnum = 3
        skill_multiplier = self.Skill_num("BPSkill", "BPSkill") / attnum
        damagelist2 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "BPSkill",
            "BPSkill",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        if self.avatar_rank >= 6:
            attnum = 4
        damagelist2[0] = damagelist2[0] * attnum
        damagelist2[1] = damagelist2[1] * attnum
        damagelist2[2] = damagelist2[2] * attnum
        skill_info_list.append({"name": "战技", "damagelist": damagelist2})

        # 计算大招伤害
        skill_multiplier = self.Skill_num("Ultra", "Ultra")
        damagelist3 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Ultra",
            "Ultra",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "终结技", "damagelist": damagelist3})

        if self.avatar_rank >= 1:
            skill_multiplier = self.Skill_num("Normal", "Normal") * 0.5
            damagelist4 = await calculate_damage(
                base_attr,
                attribute_bonus,
                "Normal",
                "Normal",
                self.avatar_element,
                skill_multiplier,
                self.avatar_level,
            )
            damagelist4[0] = damagelist1[0] + damagelist4[0]
            damagelist4[1] = damagelist1[1] + damagelist4[1]
            damagelist4[2] = damagelist1[2] + damagelist4[2]
            skill_info_list.append({"name": "强化普攻", "damagelist": damagelist4})

            skill_multiplier = (self.Skill_num("BPSkill", "BPSkill") / 3) * 0.8
            damagelist5 = await calculate_damage(
                base_attr,
                attribute_bonus,
                "BPSkill",
                "BPSkill",
                self.avatar_element,
                skill_multiplier,
                self.avatar_level,
            )
            damagelist5[0] = damagelist2[0] + damagelist5[0]
            damagelist5[1] = damagelist2[1] + damagelist5[1]
            damagelist5[2] = damagelist2[2] + damagelist5[2]
            skill_info_list.append({"name": "强化战技", "damagelist": damagelist5})

        logger.info(skill_info_list)
        return skill_info_list


class Danhengil(BaseAvatar):
    Buff: BaseAvatarBuff

    def __init__(self, char: DamageInstanceAvatar, skills: List[MihomoAvatarSkill]):
        super().__init__(char=char, skills=skills)
        self.eidolon_attribute: Dict[str, float] = {}
        self.extra_ability_attribute: Dict[str, float] = {}
        self.eidolons()
        self.extra_ability()

    def Technique(self):
        pass

    def eidolons(self):
        if self.avatar_rank >= 6:
            self.extra_ability_attribute["Normal3_ImaginaryResistancePenetration"] = 0.6

    def extra_ability(self):
        logger.info("额外能力")
        logger.info("对拥有虚数属性弱点的敌方目标造成伤害时, 暴击伤害提高24%。")
        self.extra_ability_attribute["CriticalDamageBase"] = 0.24

    async def getdamage(
        self,
        base_attr: Dict[str, float],
        attribute_bonus: Dict[str, float],
    ):
        start_buff = 3
        add_buff = 1
        max_buff = 6
        if self.avatar_rank >= 1:
            start_buff = 6
            add_buff = 2
            max_buff = 10

        injury_add = self.Skill_num("Talent", "Talent")
        critical_damage_add = self.Skill_num("BPSkill", "BPSkill")
        critical_buff = 0
        if self.avatar_rank >= 4:
            critical_buff = critical_damage_add * 4

        skill_info_list = []
        # 计算普攻1伤害
        skill_multiplier = self.Skill_num("Normal", "Normal") / 2
        damage_c = 0
        damage_e = 0
        damage_a = 0
        add_attr_bonus: Dict[str, float] = {}
        for i in range(1, 3):
            add_attr_bonus = copy.deepcopy(attribute_bonus)
            damage_buff = min(max_buff, start_buff + (i - 1) * add_buff)
            add_attr_bonus["AllDamageAddedRatio"] = (
                damage_buff * injury_add + add_attr_bonus.get("AllDamageAddedRatio", 0)
            )
            if self.avatar_rank >= 4:
                add_attr_bonus["CriticalDamageBase"] = (
                    critical_buff + add_attr_bonus.get("CriticalDamageBase", 0)
                )
            damage1, damage2, damage3 = await calculate_damage(
                base_attr,
                add_attr_bonus,
                "Normal",
                "Normal",
                self.avatar_element,
                skill_multiplier,
                self.avatar_level,
            )
            damage_c += damage1
            damage_e += damage2
            damage_a += damage3
        skill_info_list.append(
            {"name": "普攻", "damagelist": [damage_c, damage_e, damage_a]},
        )

        # 计算瞬华伤害
        skill_multiplier = self.Skill_num("Normal", "Normal1") / 3
        damage_c = 0
        damage_e = 0
        damage_a = 0
        add_attr_bonus: Dict[str, float] = {}
        for i in range(1, 4):
            add_attr_bonus = copy.deepcopy(attribute_bonus)
            damage_buff = min(max_buff, start_buff + (i - 1) * add_buff)
            add_attr_bonus["AllDamageAddedRatio"] = (
                damage_buff * injury_add + add_attr_bonus.get("AllDamageAddedRatio", 0)
            )
            if self.avatar_rank >= 4:
                add_attr_bonus["CriticalDamageBase"] = (
                    critical_buff + add_attr_bonus.get("CriticalDamageBase", 0)
                )
            damage1, damage2, damage3 = await calculate_damage(
                base_attr,
                add_attr_bonus,
                "Normal",
                "Normal1",
                self.avatar_element,
                skill_multiplier,
                self.avatar_level,
            )
            damage_c += damage1
            damage_e += damage2
            damage_a += damage3
        skill_info_list.append(
            {"name": "瞬华", "damagelist": [damage_c, damage_e, damage_a]},
        )

        # 计算天矢阴伤害
        skill_multiplier = self.Skill_num("Normal", "Normal2") / 5
        damage_c = 0
        damage_e = 0
        damage_a = 0
        add_attr_bonus: Dict[str, float] = {}
        for i in range(1, 6):
            add_attr_bonus = copy.deepcopy(attribute_bonus)
            damage_buff = min(max_buff, start_buff + (i - 1) * add_buff)
            add_attr_bonus["AllDamageAddedRatio"] = (
                damage_buff * injury_add + add_attr_bonus.get("AllDamageAddedRatio", 0)
            )
            if self.avatar_rank >= 4:
                add_attr_bonus["CriticalDamageBase"] = (
                    critical_buff + add_attr_bonus.get("CriticalDamageBase", 0)
                )
            elif i >= 4:
                critical_buff = (i - 3) * critical_damage_add
                add_attr_bonus["CriticalDamageBase"] = (
                    critical_buff + add_attr_bonus.get("CriticalDamageBase", 0)
                )
            damage1, damage2, damage3 = await calculate_damage(
                base_attr,
                add_attr_bonus,
                "Normal",
                "Normal2",
                self.avatar_element,
                skill_multiplier,
                self.avatar_level,
            )
            damage_c += damage1
            damage_e += damage2
            damage_a += damage3
        skill_info_list.append(
            {"name": "天矢阴", "damagelist": [damage_c, damage_e, damage_a]},
        )

        # 计算盘拏耀跃伤害
        skill_multiplier = self.Skill_num("Normal", "Normal3") / 7
        damage_c = 0
        damage_e = 0
        damage_a = 0
        add_attr_bonus: Dict[str, float] = {}
        for i in range(1, 8):
            add_attr_bonus = copy.deepcopy(attribute_bonus)
            damage_buff = min(max_buff, start_buff + (i - 1) * add_buff)
            add_attr_bonus["AllDamageAddedRatio"] = (
                damage_buff * injury_add + add_attr_bonus.get("AllDamageAddedRatio", 0)
            )
            if self.avatar_rank >= 4:
                add_attr_bonus["CriticalDamageBase"] = (
                    critical_buff + add_attr_bonus.get("CriticalDamageBase", 0)
                )
            elif i >= 4:
                critical_buff = (i - 3) * critical_damage_add
                add_attr_bonus["CriticalDamageBase"] = (
                    critical_buff + add_attr_bonus.get("CriticalDamageBase", 0)
                )
            damage1, damage2, damage3 = await calculate_damage(
                base_attr,
                add_attr_bonus,
                "Normal",
                "Normal3",
                self.avatar_element,
                skill_multiplier,
                self.avatar_level,
            )
            damage_c += damage1
            damage_e += damage2
            damage_a += damage3
        skill_info_list.append(
            {"name": "盘拏耀跃", "damagelist": [damage_c, damage_e, damage_a]},
        )

        # 计算大招伤害
        skill_multiplier = self.Skill_num("Ultra", "Ultra") / 3
        damage_c = 0
        damage_e = 0
        damage_a = 0
        add_attr_bonus: Dict[str, float] = {}
        for _ in range(1, 4):
            add_attr_bonus = copy.deepcopy(attribute_bonus)
            damage_buff = min(max_buff, 10)
            add_attr_bonus["AllDamageAddedRatio"] = (
                damage_buff * injury_add + add_attr_bonus.get("AllDamageAddedRatio", 0)
            )
            critical_buff = 4 * critical_damage_add
            add_attr_bonus["CriticalDamageBase"] = critical_buff + add_attr_bonus.get(
                "CriticalDamageBase", 0
            )
            damage1, damage2, damage3 = await calculate_damage(
                base_attr,
                add_attr_bonus,
                "Ultra",
                "Ultra",
                self.avatar_element,
                skill_multiplier,
                self.avatar_level,
            )
            damage_c += damage1
            damage_e += damage2
            damage_a += damage3
        skill_info_list.append(
            {"name": "终结技", "damagelist": [damage_c, damage_e, damage_a]},
        )
        logger.info(skill_info_list)
        return skill_info_list


class Argenti(BaseAvatar):
    Buff: BaseAvatarBuff

    def __init__(self, char: DamageInstanceAvatar, skills: List[MihomoAvatarSkill]):
        super().__init__(char=char, skills=skills)
        self.eidolon_attribute: Dict[str, float] = {}
        self.extra_ability_attribute: Dict[str, float] = {}
        self.eidolons()
        self.extra_ability()

    def Technique(self):
        pass

    def eidolons(self):
        if self.avatar_rank >= 1:
            self.eidolon_attribute["CriticalDamageBase"] = 0.4
        if self.avatar_rank >= 2:
            self.eidolon_attribute["AttackAddedRatio"] = 0.4
        if self.avatar_rank >= 6:
            self.eidolon_attribute["Ultra_PhysicalResistancePenetration"] = 0.3

    def extra_ability(self):
        self.extra_ability_attribute["AllDamageAddedRatio"] = 0.15

    async def getdamage(
        self,
        base_attr: Dict[str, float],
        attribute_bonus: Dict[str, float],
    ):
        talent_cc_add = self.Skill_num("Talent", "Talent")
        attribute_bonus["CriticalChanceBase"] = (
            talent_cc_add * 10 + attribute_bonus.get("CriticalChanceBase", 0)
        )
        if self.avatar_rank >= 4:
            attribute_bonus["CriticalDamageBase"] = 0.08 + attribute_bonus.get(
                "CriticalDamageBase", 0
            )
            attribute_bonus["CriticalChanceBase"] = (
                talent_cc_add * 2 + attribute_bonus.get("CriticalChanceBase", 0)
            )

        skill_info_list = []
        # 计算普攻伤害
        skill_multiplier = self.Skill_num("Normal", "Normal")
        damagelist1 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Normal",
            "Normal",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "普攻", "damagelist": damagelist1})

        # 计算战技伤害
        skill_multiplier = self.Skill_num("BPSkill", "BPSkill")
        damagelist2 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "BPSkill",
            "BPSkill",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "战技", "damagelist": damagelist2})

        # 计算大招1伤害
        skill_multiplier = self.Skill_num("Ultra", "Ultra")
        damagelist3 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Ultra",
            "Ultra",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "终结技(90耗能)", "damagelist": damagelist3})

        # 计算大招2伤害
        skill_multiplier = self.Skill_num("Ultra", "Ultra1")
        damagelist4 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Ultra",
            "Ultra",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        # 计算大招2额外伤害
        skill_multiplier = self.Skill_num("Ultra", "Ultra_add")
        damagelist5 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Ultra",
            "Ultra",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        damagelist5[0] = damagelist5[0] * 6 + damagelist4[0]
        damagelist5[1] = damagelist5[1] * 6 + damagelist4[1]
        damagelist5[2] = damagelist5[2] * 6 + damagelist4[2]
        skill_info_list.append(
            {"name": "强化终结技(180耗能)", "damagelist": damagelist5},
        )
        return skill_info_list


class Clara(BaseAvatar):
    Buff: BaseAvatarBuff

    def __init__(self, char: DamageInstanceAvatar, skills: List[MihomoAvatarSkill]):
        super().__init__(char=char, skills=skills)
        self.eidolon_attribute: Dict[str, float] = {}
        self.extra_ability_attribute: Dict[str, float] = {}
        self.eidolons()
        self.extra_ability()

    def Technique(self):
        pass

    def eidolons(self):
        if self.avatar_rank >= 2:
            self.eidolon_attribute["AttackAddedRatio"] = 0.2

    def extra_ability(self):
        logger.info("额外能力")
        logger.info("史瓦罗的反击造成的伤害提高30%")
        self.extra_ability_attribute["TalentDmgAdd"] = 0.3

    async def getdamage(
        self,
        base_attr: Dict[str, float],
        attribute_bonus: Dict[str, float],
    ):
        skill_info_list = []
        # 计算普攻伤害
        skill_multiplier = self.Skill_num("Normal", "Normal")
        damagelist1 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Normal",
            "Normal",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "普攻", "damagelist": damagelist1})

        # 计算战技伤害
        skill_multiplier = self.Skill_num("BPSkill", "BPSkill")
        damagelist2 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "BPSkill",
            "BPSkill",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "战技", "damagelist": damagelist2})

        # 计算反击伤害
        skill_multiplier = self.Skill_num("Talent", "Talent")
        damagelist3 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Talent",
            "Talent",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "反击", "damagelist": damagelist3})

        # 计算强化反击伤害
        skill_multiplier = self.Skill_num("Talent", "Talent") + self.Skill_num(
            "Ultra",
            "Talent1",
        )
        damagelist4 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Talent",
            "Talent",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "强化反击", "damagelist": damagelist4})

        # 计算1+1托帕反击伤害
        skill_multiplier = self.Skill_num("Talent", "Talent")
        add_attr_bonus = copy.deepcopy(attribute_bonus)
        add_attr_bonus["Talent_DmgRatio"] = (
            add_attr_bonus.get("Talent_DmgRatio", 0) + 0.5
        )
        add_attr_bonus["Talent_CriticalDamageBase"] = (
            add_attr_bonus.get("Talent_CriticalDamageBase", 0) + 0.74
        )
        damagelist5 = await calculate_damage(
            base_attr,
            add_attr_bonus,
            "Talent",
            "Talent",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "(1+1托帕)反击", "damagelist": damagelist5})

        # 计算反击伤害
        skill_multiplier = self.Skill_num("Talent", "Talent") + self.Skill_num(
            "Ultra",
            "Talent1",
        )
        add_attr_bonus = copy.deepcopy(attribute_bonus)
        add_attr_bonus["Talent_DmgRatio"] = (
            add_attr_bonus.get("Talent_DmgRatio", 0) + 0.5
        )
        add_attr_bonus["Talent_CriticalDamageBase"] = (
            add_attr_bonus.get("Talent_CriticalDamageBase", 0) + 0.74
        )
        damagelist6 = await calculate_damage(
            base_attr,
            add_attr_bonus,
            "Talent",
            "Talent",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "(1+1托帕)强化反击", "damagelist": damagelist6})

        return skill_info_list


class Silverwolf(BaseAvatar):
    Buff: BaseAvatarBuff

    def __init__(self, char: DamageInstanceAvatar, skills: List[MihomoAvatarSkill]):
        super().__init__(char=char, skills=skills)
        self.eidolon_attribute: Dict[str, float] = {}
        self.extra_ability_attribute: Dict[str, float] = {}
        self.eidolons()
        self.extra_ability()

    def Technique(self):
        pass

    def eidolons(self):
        if self.avatar_rank >= 6:
            self.extra_ability_attribute["AllDamageAddedRatio"] = 1

    def extra_ability(self):
        logger.info("额外能力")
        logger.info("战技降抗")
        logger.info("战技使目标全属性抗性降低的效果额外降低3%")
        enemy_status_resistance = self.Skill_num("BPSkill", "BPSkill_D") + 0.03
        self.extra_ability_attribute["QuantumResistancePenetration"] = (
            enemy_status_resistance
        )
        logger.info("终结技降防")
        ultra_defence = self.Skill_num("Ultra", "Ultra_D")
        logger.info("天赋降防")
        talent_defence = self.Skill_num("Talent", "Talent")
        ignore_defence = ultra_defence + talent_defence
        self.extra_ability_attribute["ignore_defence"] = ignore_defence

    async def getdamage(
        self,
        base_attr: Dict[str, float],
        attribute_bonus: Dict[str, float],
    ):
        skill_info_list = []
        # 计算普攻伤害
        skill_multiplier = self.Skill_num("Normal", "Normal")
        damagelist1 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Normal",
            "Normal",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "普攻", "damagelist": damagelist1})

        # 计算战技伤害
        skill_multiplier = self.Skill_num("BPSkill", "BPSkill")
        damagelist2 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "BPSkill",
            "BPSkill",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "战技", "damagelist": damagelist2})

        # 计算终结技伤害
        skill_multiplier = self.Skill_num("Ultra", "Ultra")
        if self.avatar_rank >= 4:
            skill_multiplier += 1
        damagelist3 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Ultra",
            "Ultra",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "终结技", "damagelist": damagelist3})

        return skill_info_list


class Kafka(BaseAvatar):
    Buff: BaseAvatarBuff

    def __init__(self, char: DamageInstanceAvatar, skills: List[MihomoAvatarSkill]):
        super().__init__(char=char, skills=skills)
        self.eidolon_attribute: Dict[str, float] = {}
        self.extra_ability_attribute: Dict[str, float] = {}
        self.eidolons()
        self.extra_ability()

    def Technique(self):
        pass

    def eidolons(self):
        if self.avatar_rank >= 1:
            self.extra_ability_attribute["DOTDmgAdd"] = 0.3
        if self.avatar_rank >= 2:
            self.extra_ability_attribute["DOTDmgAdd"] = 0.55

    def extra_ability(self):
        pass

    async def getdamage(
        self,
        base_attr: Dict[str, float],
        attribute_bonus: Dict[str, float],
    ):
        skill_info_list = []
        # 计算普攻伤害
        skill_multiplier = self.Skill_num("Normal", "Normal")
        damagelist1 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Normal",
            "Normal",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "普攻", "damagelist": damagelist1})

        # 计算战技伤害
        skill_multiplier = self.Skill_num("BPSkill", "BPSkill")
        damagelist2 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "BPSkill",
            "BPSkill",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "战技", "damagelist": damagelist2})

        # 计算终结技伤害
        skill_multiplier = self.Skill_num("Ultra", "Ultra")
        damagelist3 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Ultra",
            "Ultra",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "终结技", "damagelist": damagelist3})

        # 计算持续伤害
        skill_multiplier = self.Skill_num("Ultra", "DOT")
        if self.avatar_rank >= 6:
            skill_multiplier += 1.56
        damagelist4 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "DOT",
            "DOT",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "单次持续伤害", "damagelist": damagelist4})

        # 计算追加攻击伤害
        skill_multiplier = self.Skill_num("Talent", "Talent")
        damagelist5 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Talent",
            "Talent",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "追加攻击", "damagelist": damagelist5})

        return skill_info_list


class Blade(BaseAvatar):
    Buff: BaseAvatarBuff

    def __init__(self, char: DamageInstanceAvatar, skills: List[MihomoAvatarSkill]):
        super().__init__(char=char, skills=skills)
        self.eidolon_attribute: Dict[str, float] = {}
        self.extra_ability_attribute: Dict[str, float] = {}
        self.eidolons()
        self.extra_ability()

    def Technique(self):
        pass

    def eidolons(self):
        if self.avatar_rank >= 2:
            self.eidolon_attribute["CriticalChanceBase"] = 0.15
        if self.avatar_rank >= 4:
            self.eidolon_attribute["HPAddedRatio"] = 0.4

    def extra_ability(self):
        logger.info("额外能力")
        logger.info("天赋施放的追加攻击伤害提高20%")
        self.extra_ability_attribute["TalentDmgAdd"] = 0.2
        logger.info("战技加伤")
        self.extra_ability_attribute["AllDamageAddedRatio"] = self.Skill_num(
            "BPSkill",
            "BPSkill",
        )

    async def getdamage(
        self,
        base_attr: Dict[str, float],
        attribute_bonus: Dict[str, float],
    ):
        skill_info_list = []
        # 计算普攻伤害
        skill_multiplier = self.Skill_num("Normal", "Normal")
        damagelist1 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Normal",
            "Normal",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "普攻", "damagelist": damagelist1})

        # 计算强化普攻伤害
        skill_multiplier = self.Skill_num("Normal", "Normal1")
        damagelist2 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Normal",
            "Normal",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )

        skill_multiplier = self.Skill_num("Normal", "Normal1_HP")
        damagelist3 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Normal",
            "Normal",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
            1,
        )
        damagelist3[0] += damagelist2[0]
        damagelist3[1] += damagelist2[1]
        damagelist3[2] += damagelist2[2]
        skill_info_list.append({"name": "无间剑树", "damagelist": damagelist3})

        # 计算终结技伤害
        skill_multiplier = self.Skill_num("Ultra", "Ultra")
        damagelist4 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Ultra",
            "Ultra",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )

        skill_multiplier = self.Skill_num("Ultra", "Ultra_HP")
        if self.avatar_rank >= 1:
            skill_multiplier += 0.9
        damagelist5 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Ultra",
            "Ultra",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
            1,
        )
        damagelist5[0] += damagelist4[0]
        damagelist5[1] += damagelist4[1]
        damagelist5[2] += damagelist4[2]
        skill_info_list.append({"name": "终结技", "damagelist": damagelist5})

        # 计算追加攻击伤害
        skill_multiplier = self.Skill_num("Talent", "Talent")
        damagelist6 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Talent",
            "Talent",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )

        skill_multiplier = self.Skill_num("Talent", "Talent_HP")
        damagelist7 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Talent",
            "Talent",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
            1,
        )
        damagelist7[0] += damagelist6[0]
        damagelist7[1] += damagelist6[1]
        damagelist7[2] += damagelist6[2]
        if self.avatar_rank >= 6:
            hp = base_attr["hp"] * (
                1 + attribute_bonus.get("HPAddedRatio", 0)
            ) + attribute_bonus.get("HPDelta", 0)
            damage_add = hp * 0.5
            damagelist7[0] += damage_add
            damagelist7[1] += damage_add
            damagelist7[2] += damage_add
        skill_info_list.append({"name": "追加攻击", "damagelist": damagelist7})

        return skill_info_list


class Fuxuan(BaseAvatar):
    Buff: BaseAvatarBuff

    def __init__(self, char: DamageInstanceAvatar, skills: List[MihomoAvatarSkill]):
        super().__init__(char=char, skills=skills)
        self.eidolon_attribute: Dict[str, float] = {}
        self.extra_ability_attribute: Dict[str, float] = {}
        self.eidolons()
        self.extra_ability()

    def Technique(self):
        pass

    def eidolons(self):
        if self.avatar_rank >= 1:
            self.eidolon_attribute["CriticalDamageBase"] = 0.3

    def extra_ability(self):
        logger.info("符玄战技【穷观阵】属性加成")
        self.extra_ability_attribute["CriticalChanceBase"] = self.Skill_num(
            "BPSkill",
            "BPSkill_CC",
        )
        self.extra_ability_attribute["HPAddedRatio"] = self.Skill_num(
            "BPSkill",
            "BPSkill_HP",
        )

    async def getdamage(
        self,
        base_attr: Dict[str, float],
        attribute_bonus: Dict[str, float],
    ):
        skill_info_list = []
        # 计算普攻伤害
        skill_multiplier = self.Skill_num("Normal", "Normal_HP")
        damagelist1 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Normal",
            "Normal",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
            1,
        )
        skill_info_list.append({"name": "普攻", "damagelist": damagelist1})

        # 计算终结技伤害
        skill_multiplier = self.Skill_num("Ultra", "Ultra_HP")
        if self.avatar_rank >= 6:
            skill_multiplier += 1.2
        damagelist2 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Ultra",
            "Ultra",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
            1,
        )
        skill_info_list.append({"name": "终结技", "damagelist": damagelist2})

        # 计算终结技治疗
        damagelist3 = await calculate_heal(
            base_attr,
            attribute_bonus,
            "Ultra",
            0.05,
            133,
        )
        skill_info_list.append({"name": "终结技治疗", "damagelist": damagelist3})

        return skill_info_list


class Yanqing(BaseAvatar):
    Buff: BaseAvatarBuff

    def __init__(self, char: DamageInstanceAvatar, skills: List[MihomoAvatarSkill]):
        super().__init__(char=char, skills=skills)
        self.eidolon_attribute: Dict[str, float] = {}
        self.extra_ability_attribute: Dict[str, float] = {}
        self.eidolons()
        self.extra_ability()

    def Technique(self):
        pass

    def eidolons(self):
        if self.avatar_rank >= 4:
            self.eidolon_attribute["IceResistancePenetration"] = 0.15

    def extra_ability(self):
        logger.info("额外能力")
        logger.info("触发暴击时, 速度提高10%")
        self.extra_ability_attribute["SpeedAddedRatio"] = 0.1
        logger.info("【智剑连心】增益")
        critical_damage_base_t = self.Skill_num("Talent", "Talent_CD")
        critical_damage_base_u = self.Skill_num("Ultra", "Ultra_CD")
        self.extra_ability_attribute["CriticalDamageBase"] = (
            critical_damage_base_t + critical_damage_base_u
        )
        critical_chance_base = self.Skill_num("Talent", "Talent_CC")
        self.extra_ability_attribute["CriticalChanceBase"] = critical_chance_base + 0.6

    async def getdamage(
        self,
        base_attr: Dict[str, float],
        attribute_bonus: Dict[str, float],
    ):
        skill_info_list = []
        # 计算普攻伤害
        skill_multiplier = self.Skill_num("Normal", "Normal")
        damagelist1 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Normal",
            "Normal",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "普攻", "damagelist": damagelist1})

        # 计算战技伤害
        skill_multiplier = self.Skill_num("BPSkill", "BPSkill")
        damagelist2 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "BPSkill",
            "BPSkill",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "战技", "damagelist": damagelist2})

        # 计算终结技伤害
        skill_multiplier = self.Skill_num("Ultra", "Ultra")
        damagelist3 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Ultra",
            "Ultra",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "终结技", "damagelist": damagelist3})

        # 计算附加伤害
        skill_multiplier = self.Skill_num("Talent", "Talent")
        if self.avatar_rank >= 1:
            skill_multiplier += 0.9
        else:
            skill_multiplier += 0.3
        damagelist4 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Talent",
            "Talent",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "附加伤害", "damagelist": damagelist4})

        return skill_info_list


class Himeko(BaseAvatar):
    Buff: BaseAvatarBuff

    def __init__(self, char: DamageInstanceAvatar, skills: List[MihomoAvatarSkill]):
        super().__init__(char=char, skills=skills)
        self.eidolon_attribute: Dict[str, float] = {}
        self.extra_ability_attribute: Dict[str, float] = {}
        self.eidolons()
        self.extra_ability()

    def Technique(self):
        pass

    def eidolons(self):
        if self.avatar_rank >= 1:
            self.eidolon_attribute["SpeedAddedRatio"] = 0.1
        if self.avatar_rank >= 2:
            self.eidolon_attribute["AllDamageAddedRatio"] = 0.15

    def extra_ability(self):
        logger.info("额外能力")
        logger.info("战技对灼烧状态下的敌方目标造成的伤害提高20%。")
        self.extra_ability_attribute["BPSkillDmgAdd"] = 0.2
        logger.info("若当前生命值百分比大于等于80%, 则暴击率提高15%。")
        self.extra_ability_attribute["CriticalChanceBase"] = 0.15

    async def getdamage(
        self,
        base_attr: Dict[str, float],
        attribute_bonus: Dict[str, float],
    ):
        skill_info_list = []
        # 计算普攻伤害
        skill_multiplier = self.Skill_num("Normal", "Normal")
        damagelist1 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Normal",
            "Normal",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "普攻", "damagelist": damagelist1})

        # 计算战技伤害
        skill_multiplier = self.Skill_num("BPSkill", "BPSkill")
        damagelist2 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "BPSkill",
            "BPSkill",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "战技", "damagelist": damagelist2})

        # 计算终结技伤害
        skill_multiplier = self.Skill_num("Ultra", "Ultra")
        damagelist3 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Ultra",
            "Ultra",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "终结技", "damagelist": damagelist3})

        # 计算追加攻击伤害
        skill_multiplier = self.Skill_num("Talent", "Talent")
        damagelist4 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Talent",
            "Talent",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "追加攻击", "damagelist": damagelist4})

        return skill_info_list


class Qingque(BaseAvatar):
    Buff: BaseAvatarBuff

    def __init__(self, char: DamageInstanceAvatar, skills: List[MihomoAvatarSkill]):
        super().__init__(char=char, skills=skills)
        self.eidolon_attribute: Dict[str, float] = {}
        self.extra_ability_attribute: Dict[str, float] = {}
        self.eidolons()
        self.extra_ability()

    def Technique(self):
        pass

    def eidolons(self):
        if self.avatar_rank >= 1:
            self.eidolon_attribute["UltraDmgAdd"] = 0.1

    def extra_ability(self):
        logger.info("额外能力")
        logger.info("施放强化普攻后, 青雀的速度提高10%, 持续1回合。")
        self.extra_ability_attribute["SpeedAddedRatio"] = 0.1
        logger.info("默认4层战技加伤害")
        all_damage_added_ratio = self.Skill_num("BPSkill", "BPSkill") + 0.1
        self.extra_ability_attribute["AllDamageAddedRatio"] = all_damage_added_ratio * 4
        logger.info("默认暗杠加攻")
        self.extra_ability_attribute["AttackAddedRatio"] = self.Skill_num(
            "Talent",
            "Talent",
        )

    async def getdamage(
        self,
        base_attr: Dict[str, float],
        attribute_bonus: Dict[str, float],
    ):
        skill_info_list = []
        # 计算普攻伤害
        skill_multiplier = self.Skill_num("Normal", "Normal")
        damagelist1 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Normal",
            "Normal",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "普攻", "damagelist": damagelist1})

        # 计算杠上开花伤害
        skill_multiplier = self.Skill_num("Normal", "Normal1")
        damagelist2 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Normal",
            "Normal",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "杠上开花！", "damagelist": damagelist2})  # noqa: RUF001

        # 计算终结技伤害
        skill_multiplier = self.Skill_num("Ultra", "Ultra")
        damagelist3 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Ultra",
            "Ultra",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "终结技", "damagelist": damagelist3})

        return skill_info_list


class Jingliu(BaseAvatar):
    Buff: BaseAvatarBuff

    def __init__(self, char: DamageInstanceAvatar, skills: List[MihomoAvatarSkill]):
        super().__init__(char=char, skills=skills)
        self.eidolon_attribute: Dict[str, float] = {}
        self.extra_ability_attribute: Dict[str, float] = {}
        self.eidolons()
        self.extra_ability()

    def Technique(self):
        pass

    def eidolons(self):
        if self.avatar_rank >= 1:
            self.eidolon_attribute["CriticalDamageBase"] = 0.24
        if self.avatar_rank >= 2:
            self.eidolon_attribute["BPSkill1DmgAdd"] = 0.8
        if self.avatar_rank >= 4:
            self.eidolon_attribute["BPSkill1AttackAddedRatio"] = 0.3
            self.eidolon_attribute["UltraAttackAddedRatio"] = 0.3
        if self.avatar_rank >= 6:
            self.eidolon_attribute["Ultra_CriticalDamageBase"] = 0.5
            self.eidolon_attribute["BPSkill1_CriticalDamageBase"] = 0.5

    def extra_ability(self):
        logger.info("额外能力")
        logger.info("【转魄】状态下, 终结技造成的伤害提高20%。")
        logger.info("【转魄】状态下, 暴击率提高。")
        logger.info("【转魄】状态下, 攻击力提高。")
        self.extra_ability_attribute["UltraDmgAdd"] = 0.2
        critical_chance_base = self.Skill_num("Talent", "Talent_CC")
        self.extra_ability_attribute["Ultra_CriticalChanceBase"] = critical_chance_base
        self.extra_ability_attribute["BPSkill1_CriticalChanceBase"] = (
            critical_chance_base
        )
        attack_added_ratio = self.Skill_num("Talent", "Talent_atk")
        self.extra_ability_attribute["BPSkill1AttackAddedRatio"] = attack_added_ratio
        self.extra_ability_attribute["UltraAttackAddedRatio"] = attack_added_ratio

    async def getdamage(
        self,
        base_attr: Dict[str, float],
        attribute_bonus: Dict[str, float],
    ):
        skill_info_list = []
        # 计算普攻伤害
        skill_multiplier = self.Skill_num("Normal", "Normal")
        damagelist1 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Normal",
            "Normal",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "普攻", "damagelist": damagelist1})

        # 计算战技伤害
        skill_multiplier = self.Skill_num("BPSkill", "BPSkill")
        damagelist2 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "BPSkill",
            "BPSkill",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "战技", "damagelist": damagelist2})

        # 计算寒川映月伤害
        skill_multiplier = self.Skill_num("BPSkill", "BPSkill1")
        if self.avatar_rank >= 1:
            skill_multiplier += 1
        damagelist3 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "BPSkill",
            "BPSkill1",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "寒川映月", "damagelist": damagelist3})

        # 计算终结技伤害
        skill_multiplier = self.Skill_num("Ultra", "Ultra")
        if self.avatar_rank >= 1:
            skill_multiplier += 1
        damagelist4 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Ultra",
            "Ultra",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "终结技", "damagelist": damagelist4})

        return skill_info_list


class Topaz(BaseAvatar):
    Buff: BaseAvatarBuff

    def __init__(self, char: DamageInstanceAvatar, skills: List[MihomoAvatarSkill]):
        super().__init__(char=char, skills=skills)
        self.eidolon_attribute: Dict[str, float] = {}
        self.extra_ability_attribute: Dict[str, float] = {}
        self.eidolons()
        self.extra_ability()

    def Technique(self):
        pass

    def eidolons(self):
        if self.avatar_rank >= 1:
            self.eidolon_attribute["Talent_CriticalDamageBase"] = 0.5
        if self.avatar_rank >= 6:
            self.eidolon_attribute["Talent1_FireResistancePenetration"] = 0.1

    def extra_ability(self):
        logger.info("额外能力")
        logger.info("托帕和账账对拥有火属性弱点的敌方目标造成的伤害提高15%。")
        self.extra_ability_attribute["AllDamageAddedRatio"] = 0.15
        logger.info("涨幅惊人暴击伤害提高")
        self.extra_ability_attribute["Talent1_CriticalDamageBase"] = self.Skill_num(
            "Ultra",
            "Ultra_CD",
        )
        logger.info("【负债证明】状态,使其受到的追加攻击伤害提高")
        self.extra_ability_attribute["Talent_DmgRatio"] = self.Skill_num(
            "BPSkill",
            "BPSkill_add",
        )

    async def getdamage(
        self,
        base_attr: Dict[str, float],
        attribute_bonus: Dict[str, float],
    ):
        skill_info_list = []
        # 计算普攻伤害
        skill_multiplier = self.Skill_num("Normal", "Normal")
        damagelist1 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Normal",
            "Talent",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "普攻", "damagelist": damagelist1})

        # 计算账账伤害
        skill_multiplier = self.Skill_num("Talent", "Talent")
        damagelist2 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Talent",
            "Talent",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "账账", "damagelist": damagelist2})

        # 计算强化账账伤害
        skill_multiplier = self.Skill_num("Talent", "Talent") + self.Skill_num(
            "Ultra",
            "Talent1",
        )
        damagelist3 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Talent",
            "Talent1",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "强化账账", "damagelist": damagelist3})

        return skill_info_list


class Guinaifen(BaseAvatar):
    Buff: BaseAvatarBuff

    def __init__(self, char: DamageInstanceAvatar, skills: List[MihomoAvatarSkill]):
        super().__init__(char=char, skills=skills)
        self.eidolon_attribute: Dict[str, float] = {}
        self.extra_ability_attribute: Dict[str, float] = {}
        self.eidolons()
        self.extra_ability()

    def Technique(self):
        pass

    def eidolons(self):
        pass

    def extra_ability(self):
        self.extra_ability_attribute["AllDamageAddedRatio"] = 0.2
        if self.avatar_rank >= 6:
            self.extra_ability_attribute["DmgRatio"] = (
                self.Skill_num("Talent", "Talent") * 4
            )
        else:
            self.extra_ability_attribute["DmgRatio"] = (
                self.Skill_num("Talent", "Talent") * 3
            )

    async def getdamage(
        self,
        base_attr: Dict[str, float],
        attribute_bonus: Dict[str, float],
    ):
        skill_info_list = []
        # 计算普攻伤害
        skill_multiplier = self.Skill_num("Normal", "Normal")
        damagelist1 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Normal",
            "Normal",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "普攻", "damagelist": damagelist1})

        # 计算战技伤害
        skill_multiplier = self.Skill_num("BPSkill", "BPSkill")
        damagelist2 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "BPSkill",
            "BPSkill",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "战技", "damagelist": damagelist2})

        # 计算终结技伤害
        skill_multiplier = self.Skill_num("Ultra", "Ultra")
        damagelist3 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Ultra",
            "Ultra",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "终结技", "damagelist": damagelist3})

        # 计算持续伤害
        skill_multiplier = self.Skill_num("BPSkill", "DOT")
        if self.avatar_rank >= 2:
            skill_multiplier += 0.4
        damagelist4 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "DOT",
            "DOT",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "单次持续伤害", "damagelist": damagelist4})

        return skill_info_list


class Gepard(BaseAvatar):
    Buff: BaseAvatarBuff

    def __init__(self, char: DamageInstanceAvatar, skills: List[MihomoAvatarSkill]):
        super().__init__(char=char, skills=skills)
        self.eidolon_attribute: Dict[str, float] = {}
        self.extra_ability_attribute: Dict[str, float] = {}
        self.eidolons()
        self.extra_ability()

    def Technique(self):
        pass

    def eidolons(self):
        pass

    def extra_ability(self):
        pass

    async def getdamage(
        self,
        base_attr: Dict[str, float],
        attribute_bonus: Dict[str, float],
    ):
        skill_info_list = []
        # 计算普攻伤害
        skill_multiplier = self.Skill_num("Normal", "Normal")
        damagelist1 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Normal",
            "Normal",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "普攻", "damagelist": damagelist1})

        # 计算战技伤害
        skill_multiplier = self.Skill_num("BPSkill", "BPSkill")
        damagelist2 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "BPSkill",
            "BPSkill",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "战技", "damagelist": damagelist2})

        # 计算终结技护盾
        skill_multiplier = self.Skill_num("Ultra", "Ultra")
        skill_num = self.Skill_num("Ultra", "Ultra_G")
        damagelist3 = await calculate_shield(
            base_attr,
            attribute_bonus,
            skill_multiplier,
            skill_num,
        )
        skill_info_list.append({"name": "终结技(护盾)", "damagelist": damagelist3})

        return skill_info_list


class Luocha(BaseAvatar):
    Buff: BaseAvatarBuff

    def __init__(self, char: DamageInstanceAvatar, skills: List[MihomoAvatarSkill]):
        super().__init__(char=char, skills=skills)
        self.eidolon_attribute: Dict[str, float] = {}
        self.extra_ability_attribute: Dict[str, float] = {}
        self.eidolons()
        self.extra_ability()

    def Technique(self):
        pass

    def eidolons(self):
        if self.avatar_rank >= 1:
            self.eidolon_attribute["AttackAddedRatio"] = 0.2
        if self.avatar_rank >= 6:
            self.eidolon_attribute["ResistancePenetration"] = 0.2

    def extra_ability(self):
        pass

    async def getdamage(
        self,
        base_attr: Dict[str, float],
        attribute_bonus: Dict[str, float],
    ):
        skill_info_list = []
        # 计算普攻伤害
        skill_multiplier = self.Skill_num("Normal", "Normal")
        damagelist1 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Normal",
            "Normal",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "普攻", "damagelist": damagelist1})

        # 计算终结技伤害
        skill_multiplier = self.Skill_num("Ultra", "Ultra")
        damagelist2 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Ultra",
            "Ultra",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "终结技", "damagelist": damagelist2})

        # 计算战技治疗
        skill_multiplier = self.Skill_num("BPSkill", "BPSkill")
        skill_num = self.Skill_num("BPSkill", "BPSkill_G")
        damagelist3 = await calculate_heal(
            base_attr,
            attribute_bonus,
            "BPSkill",
            skill_multiplier,
            skill_num,
            1,
        )
        skill_info_list.append({"name": "战技治疗量", "damagelist": damagelist3})
        if self.avatar_rank >= 2:
            add_attr_bonus = copy.deepcopy(attribute_bonus)
            add_attr_bonus["HealRatioBase"] = (
                add_attr_bonus.get("HealRatioBase", 0) + 0.3
            )
            damagelist4 = await calculate_heal(
                base_attr,
                add_attr_bonus,
                "BPSkill",
                skill_multiplier,
                skill_num,
                1,
            )
            skill_info_list.append(
                {
                    "name": "战技治疗量(生命<50%)(2魂)",
                    "damagelist": damagelist4,
                },
            )

            damagelist5 = await calculate_shield(
                base_attr,
                attribute_bonus,
                0.18,
                240,
                1,
            )
            skill_info_list.append(
                {
                    "name": "战技护盾量(生命>50%)(2魂)",
                    "damagelist": damagelist5,
                },
            )

        # 计算天赋治疗量
        skill_multiplier = self.Skill_num("Talent", "Talent")
        skill_num = self.Skill_num("Talent", "Talent_G")
        damagelist6 = await calculate_heal(
            base_attr,
            attribute_bonus,
            "BPSkill",
            skill_multiplier,
            skill_num,
            1,
        )
        skill_info_list.append({"name": "天赋治疗量", "damagelist": damagelist6})

        # 计算技能树额外能力治疗量
        damagelist7 = await calculate_heal(
            base_attr,
            attribute_bonus,
            "BPSkill",
            0.07,
            93,
            1,
        )
        skill_info_list.append({"name": "技能树治疗量", "damagelist": damagelist7})

        return skill_info_list


class Bailu(BaseAvatar):
    Buff: BaseAvatarBuff

    def __init__(self, char: DamageInstanceAvatar, skills: List[MihomoAvatarSkill]):
        super().__init__(char=char, skills=skills)
        self.eidolon_attribute: Dict[str, float] = {}
        self.extra_ability_attribute: Dict[str, float] = {}
        self.eidolons()
        self.extra_ability()

    def Technique(self):
        pass

    def eidolons(self):
        if self.avatar_rank >= 2:
            self.eidolon_attribute["HealRatioBase"] = 0.15
        if self.avatar_rank >= 4:
            self.eidolon_attribute["AllDamageAddedRatio"] = 0.3

    def extra_ability(self):
        self.extra_ability_attribute["HPAddedRatio"] = 0.10

    async def getdamage(
        self,
        base_attr: Dict[str, float],
        attribute_bonus: Dict[str, float],
    ):
        skill_info_list = []
        # 计算普攻伤害
        skill_multiplier = self.Skill_num("Normal", "Normal")
        damagelist1 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Normal",
            "Normal",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "普攻", "damagelist": damagelist1})

        # 计算战技治疗
        skill_multiplier = self.Skill_num("BPSkill", "BPSkill")
        skill_num = self.Skill_num("BPSkill", "BPSkill_G")
        damagelist2 = await calculate_heal(
            base_attr,
            attribute_bonus,
            "BPSkill",
            skill_multiplier,
            skill_num,
        )
        heal_num = damagelist2[0]
        for i in range(1, 3):
            beilv = 1 - (i * 0.15)
            damagelist2[0] = damagelist2[0] + heal_num * beilv
        skill_info_list.append({"name": "战技治疗量", "damagelist": damagelist2})

        # 计算终结技治疗量
        skill_multiplier = self.Skill_num("Ultra", "Ultra")
        skill_num = self.Skill_num("Ultra", "Ultra_G")
        damagelist3 = await calculate_heal(
            base_attr,
            attribute_bonus,
            "Ultra",
            skill_multiplier,
            skill_num,
        )
        skill_info_list.append({"name": "终结技治疗量", "damagelist": damagelist3})

        # 计算天赋生息治疗量
        skill_multiplier = self.Skill_num("Talent", "Talent")
        skill_num = self.Skill_num("Talent", "Talent_G")
        damagelist4 = await calculate_heal(
            base_attr,
            attribute_bonus,
            "Talent",
            skill_multiplier,
            skill_num,
        )
        skill_info_list.append({"name": "天赋[生息]治疗量", "damagelist": damagelist4})

        # 计算天赋复活治疗量
        skill_multiplier = self.Skill_num("Talent", "Talent1")
        skill_num = self.Skill_num("Talent", "Talent1_G")
        damagelist5 = await calculate_heal(
            base_attr,
            attribute_bonus,
            "Talent",
            skill_multiplier,
            skill_num,
        )
        skill_info_list.append({"name": "天赋[复活]治疗量", "damagelist": damagelist5})

        return skill_info_list


class Lynx(BaseAvatar):
    Buff: BaseAvatarBuff

    def __init__(self, char: DamageInstanceAvatar, skills: List[MihomoAvatarSkill]):
        super().__init__(char=char, skills=skills)
        self.eidolon_attribute: Dict[str, float] = {}
        self.extra_ability_attribute: Dict[str, float] = {}
        self.eidolons()
        self.extra_ability()

    def Technique(self):
        pass

    def eidolons(self):
        if self.avatar_rank >= 1:
            self.eidolon_attribute["HealRatioBase"] = 0.2

    def extra_ability(self):
        pass

    async def getdamage(
        self,
        base_attr: Dict[str, float],
        attribute_bonus: Dict[str, float],
    ):
        # 计算战技生命上限
        skill_multiplier = self.Skill_num("BPSkill", "BPSkill_HP")
        skill_num = self.Skill_num("BPSkill", "BPSkill_HP_G")
        if self.avatar_rank >= 6:
            skill_multiplier += 0.06
        hp = base_attr["hp"] * (
            1 + attribute_bonus.get("HPAddedRatio", 0)
        ) + attribute_bonus.get("HPDelta", 0)
        hp_add = hp * skill_multiplier + skill_num
        attribute_bonus["HPDelta"] = attribute_bonus.get("HPDelta", 0) + hp_add

        skill_info_list = []
        # 计算普攻伤害
        skill_multiplier = self.Skill_num("Normal", "Normal_HP")
        damagelist1 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Normal",
            "Normal",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
            1,
        )
        skill_info_list.append({"name": "普攻", "damagelist": damagelist1})

        # 计算战技治疗
        skill_multiplier = self.Skill_num("BPSkill", "BPSkill")
        skill_num = self.Skill_num("BPSkill", "BPSkill_G")
        damagelist2 = await calculate_heal(
            base_attr,
            attribute_bonus,
            "BPSkill",
            skill_multiplier,
            skill_num,
        )
        skill_info_list.append({"name": "战技治疗量", "damagelist": damagelist2})
        damagelist3 = []
        damagelist3.append(hp_add)
        skill_info_list.append(
            {"name": "[求生反应]生命上限", "damagelist": damagelist3},
        )

        # 计算终结技治疗量
        skill_multiplier = self.Skill_num("Ultra", "Ultra")
        skill_num = self.Skill_num("Ultra", "Ultra_G")
        damagelist4 = await calculate_heal(
            base_attr,
            attribute_bonus,
            "Ultra",
            skill_multiplier,
            skill_num,
        )
        skill_info_list.append({"name": "终结技治疗量", "damagelist": damagelist4})

        # 计算天赋治疗量
        skill_multiplier = self.Skill_num("Talent", "Talent")
        skill_num = self.Skill_num("Talent", "Talent_G")
        damagelist5 = await calculate_heal(
            base_attr,
            attribute_bonus,
            "Talent",
            skill_multiplier,
            skill_num,
        )
        skill_info_list.append({"name": "天赋缓回治疗量", "damagelist": damagelist5})

        # 计算天赋求生反应治疗量
        skill_multiplier = self.Skill_num("Talent", "Talent1") + self.Skill_num(
            "Talent",
            "Talent",
        )
        skill_num = self.Skill_num("Talent", "Talent1_G") + self.Skill_num(
            "Talent",
            "Talent_G",
        )
        damagelist6 = await calculate_heal(
            base_attr,
            attribute_bonus,
            "Talent",
            skill_multiplier,
            skill_num,
        )
        skill_info_list.append(
            {"name": "天赋[求生反应]缓回治疗量", "damagelist": damagelist6},
        )

        return skill_info_list


class Natasha(BaseAvatar):
    Buff: BaseAvatarBuff

    def __init__(self, char: DamageInstanceAvatar, skills: List[MihomoAvatarSkill]):
        super().__init__(char=char, skills=skills)
        self.eidolon_attribute: Dict[str, float] = {}
        self.extra_ability_attribute: Dict[str, float] = {}
        self.eidolons()
        self.extra_ability()

    def Technique(self):
        pass

    def eidolons(self):
        pass

    def extra_ability(self):
        self.extra_ability_attribute["HealRatioBase"] = 0.1 + self.Skill_num(
            "Talent",
            "Talent",
        )

    async def getdamage(
        self,
        base_attr: Dict[str, float],
        attribute_bonus: Dict[str, float],
    ):
        skill_info_list = []
        # 计算普攻伤害
        skill_multiplier = self.Skill_num("Normal", "Normal")
        damagelist1 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Normal",
            "Normal",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        if self.avatar_rank >= 6:
            damagelist_add = await calculate_damage(
                base_attr,
                attribute_bonus,
                "Normal",
                "Normal",
                self.avatar_element,
                0.4,
                self.avatar_level,
                1,
            )
            damagelist1[0] += damagelist_add[0]
            damagelist1[1] += damagelist_add[1]
            damagelist1[2] += damagelist_add[2]
        skill_info_list.append({"name": "普攻", "damagelist": damagelist1})

        # 计算战技治疗
        skill_multiplier = self.Skill_num("BPSkill", "BPSkill")
        skill_num = self.Skill_num("BPSkill", "BPSkill_G")
        damagelist2 = await calculate_heal(
            base_attr,
            attribute_bonus,
            "BPSkill",
            skill_multiplier,
            skill_num,
        )
        skill_info_list.append({"name": "战技治疗量", "damagelist": damagelist2})

        # 计算战技缓回治疗量
        skill_multiplier = self.Skill_num("BPSkill", "BPSkill1")
        skill_num = self.Skill_num("BPSkill", "BPSkill1_G")
        damagelist3 = await calculate_heal(
            base_attr,
            attribute_bonus,
            "BPSkill",
            skill_multiplier,
            skill_num,
        )
        skill_info_list.append({"name": "战技缓回治疗量", "damagelist": damagelist3})

        # 计算终结技治疗量
        skill_multiplier = self.Skill_num("Ultra", "Ultra")
        skill_num = self.Skill_num("Ultra", "Ultra_G")
        damagelist4 = await calculate_heal(
            base_attr,
            attribute_bonus,
            "Ultra",
            skill_multiplier,
            skill_num,
        )
        skill_info_list.append({"name": "终结技治疗量", "damagelist": damagelist4})

        return skill_info_list


class Mar7th(BaseAvatar):
    Buff: BaseAvatarBuff

    def __init__(self, char: DamageInstanceAvatar, skills: List[MihomoAvatarSkill]):
        super().__init__(char=char, skills=skills)
        self.eidolon_attribute: Dict[str, float] = {}
        self.extra_ability_attribute: Dict[str, float] = {}
        self.eidolons()
        self.extra_ability()

    def Technique(self):
        pass

    def eidolons(self):
        pass

    def extra_ability(self):
        pass

    async def getdamage(
        self,
        base_attr: Dict[str, float],
        attribute_bonus: Dict[str, float],
    ):
        skill_info_list = []
        # 计算普攻伤害
        skill_multiplier = self.Skill_num("Normal", "Normal")
        damagelist1 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Normal",
            "Normal",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "普攻", "damagelist": damagelist1})

        # 计算战技护盾
        skill_multiplier = self.Skill_num("BPSkill", "BPSkill")
        skill_num = self.Skill_num("BPSkill", "BPSkill_G")
        damagelist2 = await calculate_shield(
            base_attr,
            attribute_bonus,
            skill_multiplier,
            skill_num,
        )
        skill_info_list.append({"name": "战技护盾量", "damagelist": damagelist2})

        # 计算终结技
        skill_multiplier = self.Skill_num("Ultra", "Ultra")
        damagelist3 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Ultra",
            "Ultra",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "终结技", "damagelist": damagelist3})

        # 计算追加攻击
        skill_multiplier = self.Skill_num("Talent", "Talent")
        damagelist4 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Talent",
            "Talent",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        if self.avatar_rank >= 4:
            defence = base_attr.get("defence", 0) * (
                1 + attribute_bonus.get("DefenceAddedRatio", 0)
            ) + attribute_bonus.get("DefenceDelta", 0)
            damage_add = defence * 0.3
            damagelist4[0] += damage_add
            damagelist4[1] += damage_add
            damagelist4[2] += damage_add
        skill_info_list.append({"name": "追加攻击", "damagelist": damagelist4})

        # 计算2命护盾
        if self.avatar_rank >= 2:
            damagelist5 = await calculate_shield(
                base_attr,
                attribute_bonus,
                0.24,
                320,
            )
            skill_info_list.append({"name": "开场护盾(2命)", "damagelist": damagelist5})

        return skill_info_list


class Bronya(BaseAvatar):
    Buff: BaseAvatarBuff

    def __init__(self, char: DamageInstanceAvatar, skills: List[MihomoAvatarSkill]):
        super().__init__(char=char, skills=skills)
        self.eidolon_attribute: Dict[str, float] = {}
        self.extra_ability_attribute: Dict[str, float] = {}
        self.eidolons()
        self.extra_ability()

    def Technique(self):
        pass

    def eidolons(self):
        if self.avatar_rank >= 2:
            self.eidolon_attribute["SpeedAddedRatio"] = 0.3

    def extra_ability(self):
        self.extra_ability_attribute["AllDamageAddedRatio"] = 0.1
        self.extra_ability_attribute["Normal_CriticalChance"] = 1
        self.extra_ability_attribute["DefenceAddedRatio"] = 0.2

    async def getdamage(
        self,
        base_attr: Dict[str, float],
        attribute_bonus: Dict[str, float],
    ):
        # 终结技增加伤害
        attribute_bonus["AttackAddedRatio"] = attribute_bonus.get(
            "AttackAddedRatio", 0
        ) + self.Skill_num("Ultra", "Ultra_A")

        add_critical_damage_base = (
            attribute_bonus.get("CriticalDamageBase", 0)
            * self.Skill_num("Ultra", "Ultra")
        ) + self.Skill_num("Ultra", "Ultra_G")

        attribute_bonus["CriticalDamageBase"] = (
            attribute_bonus.get("CriticalDamageBase", 0) + add_critical_damage_base
        )

        skill_info_list = []
        # 计算普攻伤害
        skill_multiplier = self.Skill_num("Normal", "Normal")
        damagelist1 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Normal",
            "Normal",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "普攻", "damagelist": damagelist1})

        # 计算终结技
        critical_damage_base_str = add_critical_damage_base * 100
        damagelist2 = []
        damagelist2.append(critical_damage_base_str)
        skill_info_list.append({"name": "终结技提升爆伤(%)", "damagelist": damagelist2})

        return skill_info_list


class Yukong(BaseAvatar):
    Buff: BaseAvatarBuff

    def __init__(self, char: DamageInstanceAvatar, skills: List[MihomoAvatarSkill]):
        super().__init__(char=char, skills=skills)
        self.eidolon_attribute: Dict[str, float] = {}
        self.extra_ability_attribute: Dict[str, float] = {}
        self.eidolons()
        self.extra_ability()

    def Technique(self):
        pass

    def eidolons(self):
        if self.avatar_rank >= 1:
            self.eidolon_attribute["SpeedAddedRatio"] = 0.1
        if self.avatar_rank >= 4:
            self.eidolon_attribute["AllDamageAddedRatio"] = 0.3

    def extra_ability(self):
        self.extra_ability_attribute["ImaginaryAddedRatio"] = 0.15

    async def getdamage(
        self,
        base_attr: Dict[str, float],
        attribute_bonus: Dict[str, float],
    ):
        # 终结技增加伤害
        attribute_bonus["AttackAddedRatio"] = attribute_bonus.get(
            "AttackAddedRatio", 0
        ) + self.Skill_num("BPSkill", "BPSkill")
        attribute_bonus["CriticalChanceBase"] = attribute_bonus.get(
            "CriticalChanceBase", 0
        ) + self.Skill_num("Ultra", "Ultra_CC")
        attribute_bonus["CriticalDamageBase"] = attribute_bonus.get(
            "CriticalDamageBase", 0
        ) + self.Skill_num("Ultra", "Ultra_CD")

        skill_info_list = []
        # 计算普攻伤害
        skill_multiplier = self.Skill_num("Normal", "Normal")
        damagelist1 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Normal",
            "Normal",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_multiplier = self.Skill_num("Talent", "Normal_add")
        damagelist2 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Normal",
            "Normal",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        damagelist2[0] += damagelist1[0]
        damagelist2[1] += damagelist1[1]
        damagelist2[2] += damagelist1[2]
        skill_info_list.append({"name": "普攻", "damagelist": damagelist2})

        # 计算终结技
        skill_multiplier = self.Skill_num("Ultra", "Ultra")
        damagelist3 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Ultra",
            "Ultra",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "终结技", "damagelist": damagelist3})

        return skill_info_list


class Sushang(BaseAvatar):
    Buff: BaseAvatarBuff

    def __init__(self, char: DamageInstanceAvatar, skills: List[MihomoAvatarSkill]):
        super().__init__(char=char, skills=skills)
        self.eidolon_attribute: Dict[str, float] = {}
        self.extra_ability_attribute: Dict[str, float] = {}
        self.eidolons()
        self.extra_ability()

    def Technique(self):
        pass

    def eidolons(self):
        self.eidolon_attribute["SpeedAddedRatio"] = self.Skill_num("Talent", "Talent")
        if self.avatar_rank >= 6:
            self.eidolon_attribute["SpeedAddedRatio"] = (
                self.Skill_num("Talent", "Talent") * 2
            )

    def extra_ability(self):
        self.extra_ability_attribute["jianshiDmgAdd"] = 0.2

    async def getdamage(
        self,
        base_attr: Dict[str, float],
        attribute_bonus: Dict[str, float],
    ):
        skill_info_list = []
        # 计算普攻伤害
        skill_multiplier = self.Skill_num("Normal", "Normal")
        damagelist1 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Normal",
            "Normal",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "普攻", "damagelist": damagelist1})

        # 计算剑势附加伤害
        skill_multiplier = self.Skill_num("BPSkill", "BPSkill_F")
        damagelist2 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "BPSkill",
            "jianshi",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )

        # 计算战技伤害
        skill_multiplier = self.Skill_num("BPSkill", "BPSkill")
        damagelist3 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "BPSkill",
            "BPSkill",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        damagelist3[0] += damagelist2[0]
        damagelist3[1] += damagelist2[1]
        damagelist3[2] += damagelist2[2]
        skill_info_list.append({"name": "战技", "damagelist": damagelist3})

        # 计算强化战技伤害
        skill_multiplier = self.Skill_num("BPSkill", "BPSkill")
        damagelist4 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "BPSkill",
            "BPSkill",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        damagelist4[0] += damagelist2[0] * 3
        damagelist4[1] += damagelist2[1] * 3
        damagelist4[2] += damagelist2[2] * 3
        skill_info_list.append({"name": "强化战技", "damagelist": damagelist4})

        skill_info_list.append({"name": "剑势附加伤害", "damagelist": damagelist2})

        # 计算终结技伤害
        skill_multiplier = self.Skill_num("Ultra", "Ultra")
        damagelist5 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Ultra",
            "Ultra",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "终结技", "damagelist": damagelist5})

        return skill_info_list


class Luka(BaseAvatar):
    Buff: BaseAvatarBuff

    def __init__(self, char: DamageInstanceAvatar, skills: List[MihomoAvatarSkill]):
        super().__init__(char=char, skills=skills)
        self.eidolon_attribute: Dict[str, float] = {}
        self.extra_ability_attribute: Dict[str, float] = {}
        self.eidolons()
        self.extra_ability()

    def Technique(self):
        pass

    def eidolons(self):
        if self.avatar_rank >= 1:
            self.eidolon_attribute["AllDamageAddedRatio"] = 0.15

    def extra_ability(self):
        pass

    async def getdamage(
        self,
        base_attr: Dict[str, float],
        attribute_bonus: Dict[str, float],
    ):
        # 计算终结技提供的易伤加成
        attribute_bonus["DmgRatio"] = attribute_bonus.get(
            "DmgRatio", 0
        ) + self.Skill_num("Ultra", "Ultra_d")

        skill_info_list = []
        # 计算普攻伤害
        skill_multiplier = self.Skill_num("Normal", "Normal")
        damagelist1 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Normal",
            "Normal",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "普攻", "damagelist": damagelist1})

        # 计算强化普攻伤害
        skill_multiplier = self.Skill_num("Normal", "Normal1")
        damagelist2 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Normal",
            "Normal",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        damagelist2[0] += damagelist2[0] * 5
        damagelist2[1] += damagelist2[1] * 5
        damagelist2[2] += damagelist2[2] * 5
        skill_multiplier = self.Skill_num("Normal", "Normal2")
        damagelist3 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Normal",
            "Normal",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        damagelist3[0] += damagelist2[0]
        damagelist3[1] += damagelist2[1]
        damagelist3[2] += damagelist2[2]
        skill_info_list.append({"name": "强化普攻(满段数)", "damagelist": damagelist3})

        # 计算战技伤害
        skill_multiplier = self.Skill_num("BPSkill", "BPSkill")
        damagelist4 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "BPSkill",
            "BPSkill",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "战技", "damagelist": damagelist4})

        # 计算DOT伤害
        skill_multiplier = self.Skill_num("BPSkill", "DOT")
        damagelist5 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "DOT",
            "DOT",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "持续伤害(最大值)", "damagelist": damagelist5})

        # 计算终结技伤害
        skill_multiplier = self.Skill_num("Ultra", "Ultra")
        damagelist6 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Ultra",
            "Ultra",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "终结技", "damagelist": damagelist6})

        return skill_info_list


class DanHeng(BaseAvatar):
    Buff: BaseAvatarBuff

    def __init__(self, char: DamageInstanceAvatar, skills: List[MihomoAvatarSkill]):
        super().__init__(char=char, skills=skills)
        self.eidolon_attribute: Dict[str, float] = {}
        self.extra_ability_attribute: Dict[str, float] = {}
        self.eidolons()
        self.extra_ability()

    def Technique(self):
        pass

    def eidolons(self):
        if self.avatar_rank >= 1:
            self.eidolon_attribute["CriticalChanceBase"] = 0.12

    def extra_ability(self):
        self.extra_ability_attribute["SpeedAddedRatio"] = 0.2
        self.extra_ability_attribute["NormalDmgAdd"] = 0.4

    async def getdamage(
        self,
        base_attr: Dict[str, float],
        attribute_bonus: Dict[str, float],
    ):
        # 计算穿透加成
        attribute_bonus["WindResistancePenetration"] = attribute_bonus.get(
            "WindResistancePenetration", 0
        ) + self.Skill_num("Talent", "Talent")

        skill_info_list = []
        # 计算普攻伤害
        skill_multiplier = self.Skill_num("Normal", "Normal")
        damagelist1 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Normal",
            "Normal",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "普攻", "damagelist": damagelist1})

        # 计算战技伤害
        skill_multiplier = self.Skill_num("BPSkill", "BPSkill")
        damagelist2 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "BPSkill",
            "BPSkill",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "战技", "damagelist": damagelist2})

        # 计算终结技伤害
        skill_multiplier = self.Skill_num("Ultra", "Ultra") + self.Skill_num(
            "Ultra",
            "Ultra_d",
        )
        damagelist3 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Ultra",
            "Ultra",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "终结技", "damagelist": damagelist3})

        return skill_info_list


class Arlan(BaseAvatar):
    Buff: BaseAvatarBuff

    def __init__(self, char: DamageInstanceAvatar, skills: List[MihomoAvatarSkill]):
        super().__init__(char=char, skills=skills)
        self.eidolon_attribute: Dict[str, float] = {}
        self.extra_ability_attribute: Dict[str, float] = {}
        self.eidolons()
        self.extra_ability()

    def Technique(self):
        pass

    def eidolons(self):
        if self.avatar_rank >= 1:
            self.eidolon_attribute["BPSkillDmgAdd"] = 0.12
        if self.avatar_rank >= 6:
            self.eidolon_attribute["UltraDmgAdd"] = 0.12

    def extra_ability(self):
        pass

    async def getdamage(
        self,
        base_attr: Dict[str, float],
        attribute_bonus: Dict[str, float],
    ):
        # 计算天赋伤害加成
        attribute_bonus["AllDamageAddedRatio"] = attribute_bonus.get(
            "AllDamageAddedRatio", 0
        ) + self.Skill_num("Talent", "Talent")

        skill_info_list = []
        # 计算普攻伤害
        skill_multiplier = self.Skill_num("Normal", "Normal")
        damagelist1 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Normal",
            "Normal",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "普攻", "damagelist": damagelist1})

        # 计算战技伤害
        skill_multiplier = self.Skill_num("BPSkill", "BPSkill")
        damagelist2 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "BPSkill",
            "BPSkill",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "战技", "damagelist": damagelist2})

        # 计算终结技伤害
        skill_multiplier = self.Skill_num("Ultra", "Ultra")
        damagelist3 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Ultra",
            "Ultra",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "终结技", "damagelist": damagelist3})

        return skill_info_list


class Asta(BaseAvatar):
    Buff: BaseAvatarBuff

    def __init__(self, char: DamageInstanceAvatar, skills: List[MihomoAvatarSkill]):
        super().__init__(char=char, skills=skills)
        self.eidolon_attribute: Dict[str, float] = {}
        self.extra_ability_attribute: Dict[str, float] = {}
        self.eidolons()
        self.extra_ability()

    def Technique(self):
        pass

    def eidolons(self):
        pass

    def extra_ability(self):
        self.eidolon_attribute["FireAddedRatio"] = 0.18

    async def getdamage(
        self,
        base_attr: Dict[str, float],
        attribute_bonus: Dict[str, float],
    ):
        # 计算天赋加成
        attribute_bonus["AttackAddedRatio"] = (
            attribute_bonus.get("AttackAddedRatio", 0)
            + self.Skill_num("Talent", "Talent") * 5
        )
        attribute_bonus["SpeedDelta"] = attribute_bonus.get(
            "SpeedDelta", 0
        ) + self.Skill_num("Ultra", "Ultra")

        skill_info_list = []
        # 计算普攻伤害
        skill_multiplier = self.Skill_num("Normal", "Normal")
        damagelist1 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Normal",
            "Normal",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "普攻", "damagelist": damagelist1})

        # 计算战技伤害
        skill_multiplier = self.Skill_num("BPSkill", "BPSkill")
        damagelist2 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "BPSkill",
            "BPSkill",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_num = 5
        if self.avatar_rank >= 1:
            skill_num += 1
        damagelist2[0] = damagelist2[0] * skill_num
        damagelist2[1] = damagelist2[1] * skill_num
        damagelist2[2] = damagelist2[2] * skill_num
        skill_info_list.append({"name": "战技", "damagelist": damagelist2})

        return skill_info_list


class Herta(BaseAvatar):
    Buff: BaseAvatarBuff

    def __init__(self, char: DamageInstanceAvatar, skills: List[MihomoAvatarSkill]):
        super().__init__(char=char, skills=skills)
        self.eidolon_attribute: Dict[str, float] = {}
        self.extra_ability_attribute: Dict[str, float] = {}
        self.eidolons()
        self.extra_ability()

    def Technique(self):
        pass

    def eidolons(self):
        if self.avatar_rank >= 2:
            self.eidolon_attribute["CriticalChanceBase"] = 0.15
        if self.avatar_rank >= 4:
            self.eidolon_attribute["TalentDmgAdd"] = 0.12
        if self.avatar_rank >= 6:
            self.eidolon_attribute["AttackAddedRatio"] = 0.25

    def extra_ability(self):
        self.extra_ability_attribute["BPSkillDmgAdd"] = 0.25
        self.extra_ability_attribute["UltraDmgAdd"] = 0.2

    async def getdamage(
        self,
        base_attr: Dict[str, float],
        attribute_bonus: Dict[str, float],
    ):
        skill_info_list = []
        # 计算普攻伤害
        skill_multiplier = self.Skill_num("Normal", "Normal")
        if self.avatar_rank >= 1:
            skill_multiplier += 0.4
        damagelist1 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Normal",
            "Normal",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "普攻", "damagelist": damagelist1})

        # 计算战技伤害
        attribute_bonus["BPSkillDmgAdd"] = attribute_bonus.get("BPSkillDmgAdd", 0) + 0.2
        skill_multiplier = self.Skill_num("BPSkill", "BPSkill")
        damagelist2 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "BPSkill",
            "BPSkill",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "战技", "damagelist": damagelist2})

        # 计算终结技伤害
        skill_multiplier = self.Skill_num("Ultra", "Ultra")
        damagelist3 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Ultra",
            "Ultra",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "终结技", "damagelist": damagelist3})

        # 计算追加攻击伤害
        skill_multiplier = self.Skill_num("Talent", "Talent")
        damagelist4 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Talent",
            "Talent",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "追加攻击", "damagelist": damagelist4})

        return skill_info_list


class Serval(BaseAvatar):
    Buff: BaseAvatarBuff

    def __init__(self, char: DamageInstanceAvatar, skills: List[MihomoAvatarSkill]):
        super().__init__(char=char, skills=skills)
        self.eidolon_attribute: Dict[str, float] = {}
        self.extra_ability_attribute: Dict[str, float] = {}
        self.eidolons()
        self.extra_ability()

    def Technique(self):
        pass

    def eidolons(self):
        if self.avatar_rank >= 6:
            self.eidolon_attribute["AllDamageAddedRatio"] = 0.3

    def extra_ability(self):
        self.extra_ability_attribute["AttackAddedRatio"] = 0.2

    async def getdamage(
        self,
        base_attr: Dict[str, float],
        attribute_bonus: Dict[str, float],
    ):
        skill_info_list = []
        # 计算普攻伤害
        skill_multiplier = self.Skill_num("Normal", "Normal")
        damagelist1 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Normal",
            "Normal",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "普攻", "damagelist": damagelist1})

        # 计算战技伤害
        skill_multiplier = self.Skill_num("BPSkill", "BPSkill")
        damagelist2 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "BPSkill",
            "BPSkill",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "战技", "damagelist": damagelist2})

        # 计算DOT伤害
        skill_multiplier = self.Skill_num("BPSkill", "DOT")
        damagelist5 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "DOT",
            "DOT",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "持续伤害", "damagelist": damagelist5})

        # 计算终结技伤害
        skill_multiplier = self.Skill_num("Ultra", "Ultra")
        damagelist3 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Ultra",
            "Ultra",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "终结技", "damagelist": damagelist3})

        # 计算追加攻击伤害
        skill_multiplier = self.Skill_num("Talent", "Talent")
        damagelist4 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Talent",
            "Talent",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "追加攻击", "damagelist": damagelist4})

        return skill_info_list


class Pela(BaseAvatar):
    Buff: BaseAvatarBuff

    def __init__(self, char: DamageInstanceAvatar, skills: List[MihomoAvatarSkill]):
        super().__init__(char=char, skills=skills)
        self.eidolon_attribute: Dict[str, float] = {}
        self.extra_ability_attribute: Dict[str, float] = {}
        self.eidolons()
        self.extra_ability()

    def Technique(self):
        pass

    def eidolons(self):
        if self.avatar_rank >= 2:
            self.eidolon_attribute["SpeedAddedRatio"] = 0.1
        if self.avatar_rank >= 4:
            self.eidolon_attribute["IceResistancePenetration"] = 0.12

    def extra_ability(self):
        self.extra_ability_attribute["AllDamageAddedRatio"] = 0.4
        self.extra_ability_attribute["StatusProbabilityBase"] = 0.1

    async def getdamage(
        self,
        base_attr: Dict[str, float],
        attribute_bonus: Dict[str, float],
    ):
        # 计算终结技降防
        attribute_bonus["ignore_defence"] = attribute_bonus.get(
            "ignore_defence", 0
        ) + self.Skill_num("Ultra", "Ultra_d")

        skill_info_list = []
        # 计算普攻伤害
        skill_multiplier = self.Skill_num("Normal", "Normal")
        damagelist1 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Normal",
            "Normal",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "普攻", "damagelist": damagelist1})

        # 计算战技伤害
        skill_multiplier = self.Skill_num("BPSkill", "BPSkill")
        damagelist2 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "BPSkill",
            "BPSkill",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "战技", "damagelist": damagelist2})

        # 计算终结技伤害
        skill_multiplier = self.Skill_num("Ultra", "Ultra")
        damagelist3 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Ultra",
            "Ultra",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "终结技", "damagelist": damagelist3})

        if self.avatar_rank >= 6:
            # 计算命座附加伤害
            damagelist4 = await calculate_damage(
                base_attr,
                attribute_bonus,
                "fujia",
                "fujia",
                self.avatar_element,
                0.4,
                self.avatar_level,
            )
            skill_info_list.append({"name": "6命追加伤害", "damagelist": damagelist4})

        return skill_info_list


class Sampo(BaseAvatar):
    Buff: BaseAvatarBuff

    def __init__(self, char: DamageInstanceAvatar, skills: List[MihomoAvatarSkill]):
        super().__init__(char=char, skills=skills)
        self.eidolon_attribute: Dict[str, float] = {}
        self.extra_ability_attribute: Dict[str, float] = {}
        self.eidolons()
        self.extra_ability()

    def Technique(self):
        pass

    def eidolons(self):
        pass

    def extra_ability(self):
        pass

    async def getdamage(
        self,
        base_attr: Dict[str, float],
        attribute_bonus: Dict[str, float],
    ):
        # 计算终结技持续伤害加成
        attribute_bonus["DOTDmgAdd"] = attribute_bonus.get(
            "DOTDmgAdd", 0
        ) + self.Skill_num("Ultra", "Ultra_d")

        skill_info_list = []
        # 计算普攻伤害
        skill_multiplier = self.Skill_num("Normal", "Normal")
        damagelist1 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Normal",
            "Normal",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "普攻", "damagelist": damagelist1})

        # 计算战技伤害
        skill_multiplier = self.Skill_num("BPSkill", "BPSkill")
        damagelist2 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "BPSkill",
            "BPSkill",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        damagelist2[0] = damagelist2[0] * 5
        damagelist2[1] = damagelist2[1] * 5
        damagelist2[2] = damagelist2[2] * 5
        skill_info_list.append({"name": "战技", "damagelist": damagelist2})

        # 计算终结技伤害
        skill_multiplier = self.Skill_num("Ultra", "Ultra")
        damagelist3 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Ultra",
            "Ultra",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "终结技", "damagelist": damagelist3})

        # 计算持续伤害
        skill_multiplier = self.Skill_num("Talent", "DOT")
        if self.avatar_rank >= 6:
            skill_multiplier += 0.15
        damagelist4 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "DOT",
            "DOT",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "单层持续伤害", "damagelist": damagelist4})

        return skill_info_list


class Hook(BaseAvatar):
    Buff: BaseAvatarBuff

    def __init__(self, char: DamageInstanceAvatar, skills: List[MihomoAvatarSkill]):
        super().__init__(char=char, skills=skills)
        self.eidolon_attribute: Dict[str, float] = {}
        self.extra_ability_attribute: Dict[str, float] = {}
        self.eidolons()
        self.extra_ability()

    def Technique(self):
        pass

    def eidolons(self):
        if self.avatar_rank >= 2:
            self.eidolon_attribute["BPSkill1DmgAdd"] = 0.2
        if self.avatar_rank >= 6:
            self.eidolon_attribute["AllDamageAddedRatio"] = 0.2

    def extra_ability(self):
        pass

    async def getdamage(
        self,
        base_attr: Dict[str, float],
        attribute_bonus: Dict[str, float],
    ):
        skill_info_list = []
        # 计算普攻伤害
        skill_multiplier = self.Skill_num("Normal", "Normal")
        damagelist1 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Normal",
            "Normal",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "普攻", "damagelist": damagelist1})

        # 计算战技伤害
        skill_multiplier = self.Skill_num("BPSkill", "BPSkill")
        damagelist2 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "BPSkill",
            "BPSkill",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "战技", "damagelist": damagelist2})

        # 计算强化战技伤害
        skill_multiplier = self.Skill_num("BPSkill", "BPSkill1")
        damagelist3 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "BPSkill",
            "BPSkill1",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "强化战技", "damagelist": damagelist3})

        # 计算持续伤害
        skill_multiplier = self.Skill_num("BPSkill", "DOT")
        damagelist5 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "DOT",
            "DOT",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "灼烧伤害", "damagelist": damagelist5})

        # 计算终结技伤害
        skill_multiplier = self.Skill_num("Ultra", "Ultra")
        damagelist4 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Ultra",
            "Ultra",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "终结技", "damagelist": damagelist4})

        # 计算终结技伤害
        skill_multiplier = self.Skill_num("Talent", "Talent")
        damagelist6 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "fujia",
            "fujia",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "附加伤害", "damagelist": damagelist6})

        return skill_info_list


class Tingyun(BaseAvatar):
    Buff: BaseAvatarBuff

    def __init__(self, char: DamageInstanceAvatar, skills: List[MihomoAvatarSkill]):
        super().__init__(char=char, skills=skills)
        self.eidolon_attribute: Dict[str, float] = {}
        self.extra_ability_attribute: Dict[str, float] = {}
        self.eidolons()
        self.extra_ability()

    def Technique(self):
        pass

    def eidolons(self):
        if self.avatar_rank >= 1:
            self.eidolon_attribute["SpeedAddedRatio"] = 0.2

    def extra_ability(self):
        self.eidolon_attribute["SpeedAddedRatio"] = 0.2
        self.eidolon_attribute["NormalDmgAdd"] = 0.4

    async def getdamage(
        self,
        base_attr: Dict[str, float],
        attribute_bonus: Dict[str, float],
    ):
        skill_info_list = []
        # 计算普攻伤害
        skill_multiplier = self.Skill_num("Normal", "Normal")
        damagelist1 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Normal",
            "Normal",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "普攻", "damagelist": damagelist1})

        # 计算战技伤害
        skill_multiplier = self.Skill_num("BPSkill", "BPSkill_M")
        attack = (
            base_attr["attack"] * (1 + attribute_bonus["AttackAddedRatio"])
            + attribute_bonus["AttackDelta"]
        )
        add_atk = attack * skill_multiplier
        damagelist2 = []
        damagelist2.append(add_atk)
        skill_info_list.append({"name": "战技提升攻击力", "damagelist": damagelist2})

        return skill_info_list


class Trailblazer(BaseAvatar):
    Buff: BaseAvatarBuff

    def __init__(self, char: DamageInstanceAvatar, skills: List[MihomoAvatarSkill]):
        super().__init__(char=char, skills=skills)
        self.eidolon_attribute: Dict[str, float] = {}
        self.extra_ability_attribute: Dict[str, float] = {}
        self.eidolons()
        self.extra_ability()

    def Technique(self):
        pass

    def eidolons(self):
        if self.avatar_rank >= 4:
            self.eidolon_attribute["CriticalChanceBase"] = 0.25

    def extra_ability(self):
        self.extra_ability_attribute["BPSkillDmgAdd"] = 0.25
        self.extra_ability_attribute["Ultra1DmgAdd"] = 0.25

    async def getdamage(
        self,
        base_attr: Dict[str, float],
        attribute_bonus: Dict[str, float],
    ):
        # 计算天赋攻击加成
        attribute_bonus["AttackAddedRatio"] = (
            attribute_bonus.get("AttackAddedRatio", 0)
            + self.Skill_num("Talent", "Talent") * 2
        )

        skill_info_list = []
        # 计算普攻伤害
        skill_multiplier = self.Skill_num("Normal", "Normal")
        damagelist1 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Normal",
            "Normal",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "普攻", "damagelist": damagelist1})

        # 计算战技伤害
        skill_multiplier = self.Skill_num("BPSkill", "BPSkill")
        damagelist2 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "BPSkill",
            "BPSkill",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "战技", "damagelist": damagelist2})

        # 计算终结技1伤害
        skill_multiplier = self.Skill_num("Ultra", "Ultra")
        damagelist3 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Ultra",
            "Ultra",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "全胜•再见安打", "damagelist": damagelist3})

        # 计算终结技2伤害
        skill_multiplier = self.Skill_num("Ultra", "Ultra1")
        damagelist4 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Ultra",
            "Ultra1",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "全胜•安息全垒打", "damagelist": damagelist4})

        return skill_info_list


class Trailblazer_K(BaseAvatar):
    Buff: BaseAvatarBuff

    def __init__(self, char: DamageInstanceAvatar, skills: List[MihomoAvatarSkill]):
        super().__init__(char=char, skills=skills)
        self.eidolon_attribute: Dict[str, float] = {}
        self.extra_ability_attribute: Dict[str, float] = {}
        self.eidolons()
        self.extra_ability()

    def Technique(self):
        pass

    def eidolons(self):
        if self.avatar_rank >= 6:
            self.eidolon_attribute["DefenceAddedRatio"] = 0.3

    def extra_ability(self):
        self.extra_ability_attribute["AttackAddedRatio"] = 0.15

    async def getdamage(
        self,
        base_attr: Dict[str, float],
        attribute_bonus: Dict[str, float],
    ):
        skill_info_list = []
        # 计算普攻伤害
        skill_multiplier = self.Skill_num("Normal", "Normal")
        damagelist1 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Normal",
            "Normal",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        if self.avatar_rank >= 1:
            damagelist1_f = await calculate_damage(
                base_attr,
                attribute_bonus,
                "Normal",
                "Normal",
                self.avatar_element,
                0.25,
                self.avatar_level,
                2,
            )
            damagelist1[0] += damagelist1_f[0]
            damagelist1[1] += damagelist1_f[1]
            damagelist1[2] += damagelist1_f[2]
        skill_info_list.append({"name": "普攻", "damagelist": damagelist1})

        # 计算强化普攻伤害
        skill_multiplier = self.Skill_num("Normal", "Normal1")
        damagelist2 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Normal",
            "Normal",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        if self.avatar_rank >= 1:
            damagelist2_f = await calculate_damage(
                base_attr,
                attribute_bonus,
                "Normal",
                "Normal",
                self.avatar_element,
                0.5,
                self.avatar_level,
                2,
            )
            damagelist2[0] += damagelist2_f[0]
            damagelist2[1] += damagelist2_f[1]
            damagelist2[2] += damagelist2_f[2]
        skill_info_list.append({"name": "强化普攻", "damagelist": damagelist2})

        # 计算终结技伤害
        skill_multiplier = self.Skill_num("Ultra", "Ultra")
        damagelist3 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Ultra",
            "Ultra",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )

        skill_multiplier = self.Skill_num("Ultra", "Ultra1")
        damagelist3_f = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Ultra",
            "Ultra",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
            2,
        )
        damagelist3[0] += damagelist3_f[0]
        damagelist3[1] += damagelist3_f[1]
        damagelist3[2] += damagelist3_f[2]
        skill_info_list.append({"name": "终结技", "damagelist": damagelist3})

        # 计算天赋提供护盾
        skill_multiplier = self.Skill_num("Talent", "Talent")
        skill_multiplier_g = self.Skill_num("Talent", "Talent_G")
        if self.avatar_rank >= 2:
            skill_multiplier += 0.02
            skill_multiplier_g += 27
        damagelist4 = await calculate_shield(
            base_attr,
            attribute_bonus,
            skill_multiplier,
            skill_multiplier_g,
        )
        skill_info_list.append({"name": "天赋护盾", "damagelist": damagelist4})

        return skill_info_list


class Huohuo(BaseAvatar):
    Buff: BaseAvatarBuff

    def __init__(self, char: DamageInstanceAvatar, skills: List[MihomoAvatarSkill]):
        super().__init__(char=char, skills=skills)
        self.eidolon_attribute: Dict[str, float] = {}
        self.extra_ability_attribute: Dict[str, float] = {}
        self.eidolons()
        self.extra_ability()

    def Technique(self):
        pass

    def eidolons(self):
        if self.avatar_rank >= 1:
            self.eidolon_attribute["SpeedAddedRatio"] = 0.12
        if self.avatar_rank >= 6:
            self.eidolon_attribute["AllDamageAddedRatio"] = 0.5

    def extra_ability(self):
        pass

    async def getdamage(
        self,
        base_attr: Dict[str, float],
        attribute_bonus: Dict[str, float],
    ):
        skill_info_list = []
        # 计算普攻伤害
        skill_multiplier = self.Skill_num("Normal", "Normal")
        damagelist1 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Normal",
            "Normal",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
            1,
        )
        skill_info_list.append({"name": "普攻", "damagelist": damagelist1})

        # 计算战技治疗
        skill_multiplier = self.Skill_num("BPSkill", "BPSkill")
        skill_num = self.Skill_num("BPSkill", "BPSkill_G")
        damagelist2 = await calculate_heal(
            base_attr,
            attribute_bonus,
            "BPSkill",
            skill_multiplier,
            skill_num,
        )
        skill_info_list.append({"name": "战技治疗量", "damagelist": damagelist2})

        if self.avatar_rank >= 4:
            # 计算战技治疗
            skill_multiplier = self.Skill_num("BPSkill", "BPSkill")
            skill_num = self.Skill_num("BPSkill", "BPSkill_G")
            add_attr_bonus = copy.deepcopy(attribute_bonus)
            add_attr_bonus["HealRatioBase"] = (
                add_attr_bonus.get("HealRatioBase", 0) + 0.8
            )
            damagelist2_max = await calculate_heal(
                base_attr,
                add_attr_bonus,
                "BPSkill",
                skill_multiplier,
                skill_num,
            )
            skill_info_list.append(
                {"name": "战技最高治疗量(4魂)", "damagelist": damagelist2_max},
            )

        # 计算天赋治疗量
        skill_multiplier = self.Skill_num("Talent", "Talent")
        skill_num = self.Skill_num("Talent", "Talent_G")
        damagelist5 = await calculate_heal(
            base_attr,
            attribute_bonus,
            "Talent",
            skill_multiplier,
            skill_num,
        )
        skill_info_list.append({"name": "天赋治疗量", "damagelist": damagelist5})

        if self.avatar_rank >= 4:
            skill_multiplier = self.Skill_num("Talent", "Talent")
            skill_num = self.Skill_num("Talent", "Talent_G")
            add_attr_bonus = copy.deepcopy(attribute_bonus)
            add_attr_bonus["HealRatioBase"] = (
                add_attr_bonus.get("HealRatioBase", 0) + 0.8
            )
            damagelist5 = await calculate_heal(
                base_attr,
                add_attr_bonus,
                "Talent",
                skill_multiplier,
                skill_num,
            )
            skill_info_list.append({"name": "天赋治疗量", "damagelist": damagelist5})

        return skill_info_list


class Hanya(BaseAvatar):
    Buff: BaseAvatarBuff

    def __init__(self, char: DamageInstanceAvatar, skills: List[MihomoAvatarSkill]):
        super().__init__(char=char, skills=skills)
        self.eidolon_attribute: Dict[str, float] = {}
        self.extra_ability_attribute: Dict[str, float] = {}
        self.eidolons()
        self.extra_ability()

    def Technique(self):
        pass

    def eidolons(self):
        if self.avatar_rank >= 2:
            self.eidolon_attribute["SpeedAddedRatio"] = 0.2

    def extra_ability(self):
        self.extra_ability_attribute["AttackAddedRatio"] = 0.1

    async def getdamage(
        self,
        base_attr: Dict[str, float],
        attribute_bonus: Dict[str, float],
    ):
        # 计算天赋易伤加成
        attribute_bonus["DmgRatio"] = attribute_bonus.get(
            "DmgRatio", 0
        ) + self.Skill_num("Talent", "Talent")
        if self.avatar_rank >= 6:
            attribute_bonus["DmgRatio"] = attribute_bonus.get("DmgRatio", 0) + 0.1

        attribute_bonus["AttackAddedRatio"] = attribute_bonus.get(
            "AttackAddedRatio", 0
        ) + self.Skill_num("Ultra", "Ultra_A")

        skill_info_list = []
        # 计算普攻伤害
        skill_multiplier = self.Skill_num("Normal", "Normal")
        damagelist1 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Normal",
            "Normal",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "普攻", "damagelist": damagelist1})

        # 计算战技伤害
        skill_multiplier = self.Skill_num("BPSkill", "BPSkill")
        damagelist2 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "BPSkill",
            "BPSkill",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "战技", "damagelist": damagelist2})

        # 计算终结技提升速度
        speed = (
            base_attr["speed"] * (1 + attribute_bonus["SpeedAddedRatio"])
            + attribute_bonus["SpeedDelta"]
        )
        skill_multiplier = self.Skill_num("Ultra", "Ultra_S")
        add_speed = speed * skill_multiplier
        damagelist3 = []
        damagelist3.append(add_speed)
        skill_info_list.append({"name": "终结技增加速度", "damagelist": damagelist3})

        return skill_info_list


class DrRatio(BaseAvatar):
    Buff: BaseAvatarBuff

    def __init__(self, char: DamageInstanceAvatar, skills: List[MihomoAvatarSkill]):
        super().__init__(char=char, skills=skills)
        self.eidolon_attribute: Dict[str, float] = {}
        self.extra_ability_attribute: Dict[str, float] = {}
        self.eidolons()
        self.extra_ability()

    def Technique(self):
        pass

    def eidolons(self):
        if self.avatar_rank >= 1:
            self.eidolon_attribute["CriticalChanceBase"] = 0.1
            self.eidolon_attribute["CriticalDamageBase"] = 0.2
        if self.avatar_rank >= 6:
            self.eidolon_attribute["TalentDmgAdd"] = 0.5

    def extra_ability(self):
        self.extra_ability_attribute["AllDamageAddedRatio"] = 0.5
        self.extra_ability_attribute["CriticalChanceBase"] = 0.15
        self.extra_ability_attribute["CriticalDamageBase"] = 0.3

    async def getdamage(
        self,
        base_attr: Dict[str, float],
        attribute_bonus: Dict[str, float],
    ):
        skill_info_list = []
        # 计算普攻伤害
        skill_multiplier = self.Skill_num("Normal", "Normal")
        damagelist1 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Normal",
            "Normal",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "普攻", "damagelist": damagelist1})

        # 计算战技伤害
        skill_multiplier = self.Skill_num("BPSkill", "BPSkill")
        damagelist2 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "BPSkill",
            "BPSkill",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "战技", "damagelist": damagelist2})

        # 计算终结技1伤害
        skill_multiplier = self.Skill_num("Ultra", "Ultra")
        damagelist3 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Ultra",
            "Ultra",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "终结技", "damagelist": damagelist3})

        # 计算天赋追伤伤害
        skill_multiplier = self.Skill_num("Talent", "Talent")
        damagelist4 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Talent",
            "Talent",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        if self.avatar_rank >= 2:
            damagelist5 = await calculate_damage(
                base_attr,
                attribute_bonus,
                "fujia",
                "fujia",
                self.avatar_element,
                0.2,
                self.avatar_level,
            )
            damagelist4[0] += damagelist5[0] * 4
            damagelist4[1] += damagelist5[1] * 4
            damagelist4[2] += damagelist5[2] * 4
        skill_info_list.append({"name": "协同攻击", "damagelist": damagelist4})

        return skill_info_list


class RuanMei(BaseAvatar):
    Buff: BaseAvatarBuff

    def __init__(self, char: DamageInstanceAvatar, skills: List[MihomoAvatarSkill]):
        super().__init__(char=char, skills=skills)
        self.eidolon_attribute: Dict[str, float] = {}
        self.extra_ability_attribute: Dict[str, float] = {}
        self.eidolons()
        self.extra_ability()

    def Technique(self):
        pass

    def eidolons(self):
        if self.avatar_rank >= 1:
            self.eidolon_attribute["ignore_defence"] = 0.2
        if self.avatar_rank >= 2:
            self.eidolon_attribute["AttackAddedRatio"] = 0.4
        if self.avatar_rank >= 4:
            self.eidolon_attribute["BreakDamageAddedRatioBase"] = 1

    def extra_ability(self):
        self.extra_ability_attribute["BreakDamageAddedRatioBase"] = 0.2

    async def getdamage(
        self,
        base_attr: Dict[str, float],
        attribute_bonus: Dict[str, float],
    ):
        # 计算属性加成
        attribute_bonus["AllDamageAddedRatio"] = attribute_bonus.get(
            "AllDamageAddedRatio", 0
        ) + self.Skill_num("BPSkill", "BPSkill")
        attribute_bonus["BreakDamageAddedRatioBase"] = (
            attribute_bonus.get("BreakDamageAddedRatioBase", 0) + 0.5
        )
        attribute_bonus["ResistancePenetration"] = attribute_bonus.get(
            "ResistancePenetration", 0
        ) + self.Skill_num("Ultra", "Ultra_P")
        attribute_bonus["SpeedAddedRatio"] = attribute_bonus.get(
            "SpeedAddedRatio", 0
        ) + self.Skill_num("Talent", "Talent_S")

        # 战斗中阮•梅的击破特攻大于120%时, 每超过10%, 则战技使我方全体伤害提高的效果额外提高6%, 最高不超过36%。
        Break_Damage_Added_Ratio = attribute_bonus.get("BreakDamageAddedRatioBase", 0)
        if Break_Damage_Added_Ratio > 1.2:
            add_all_damage_added_ratio = ((Break_Damage_Added_Ratio - 1.2) / 0.1) * 0.06
            add_all_damage_added_ratio = min(0.36, add_all_damage_added_ratio)
            attribute_bonus["AllDamageAddedRatio"] = (
                attribute_bonus.get("AllDamageAddedRatio", 0)
                + add_all_damage_added_ratio
            )

        skill_info_list = []
        # 计算普攻伤害
        skill_multiplier = self.Skill_num("Normal", "Normal")
        damagelist1 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Normal",
            "Normal",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "普攻", "damagelist": damagelist1})

        # 计算终结技伤害
        skill_multiplier = self.Skill_num("Ultra", "Ultra")
        jipodamage1 = await break_damage(
            base_attr,
            attribute_bonus,
            "jipo",
            "jipo",
            self.avatar_element,
            self.avatar_level,
        )
        jipodamage1[0] = jipodamage1[0] * skill_multiplier
        skill_info_list.append({"name": "残梅绽附加伤害", "damagelist": jipodamage1})

        # 计算天赋追伤伤害
        skill_multiplier = self.Skill_num("Talent", "Talent")
        if self.avatar_rank >= 6:
            skill_multiplier += 2
        jipodamage2 = await break_damage(
            base_attr,
            attribute_bonus,
            "jipo",
            "jipo",
            self.avatar_element,
            self.avatar_level,
        )
        jipodamage2[0] = jipodamage2[0] * skill_multiplier
        skill_info_list.append({"name": "天赋附加击破伤害", "damagelist": jipodamage2})

        return skill_info_list


class XueYi(BaseAvatar):
    Buff: BaseAvatarBuff

    def __init__(self, char: DamageInstanceAvatar, skills: List[MihomoAvatarSkill]):
        super().__init__(char=char, skills=skills)
        self.eidolon_attribute: Dict[str, float] = {}
        self.extra_ability_attribute: Dict[str, float] = {}
        self.eidolons()
        self.extra_ability()

    def Technique(self):
        pass

    def eidolons(self):
        if self.avatar_rank >= 1:
            self.eidolon_attribute["TalentDmgAdd"] = 0.4
        if self.avatar_rank >= 4:
            self.eidolon_attribute["BreakDamageAddedRatioBase"] = 0.4

    def extra_ability(self):
        self.extra_ability_attribute["UltraDmgAdd"] = 0.1 + self.Skill_num(
            "Ultra", "Ultra_A"
        )

    async def getdamage(
        self,
        base_attr: Dict[str, float],
        attribute_bonus: Dict[str, float],
    ):
        # 使自身造成的伤害提高, 提高数值等同于击破特攻的100%, 最多使造成的伤害提高240%。
        Break_Damage_Added_Ratio = attribute_bonus.get("BreakDamageAddedRatioBase", 0)
        attribute_bonus["AllDamageAddedRatio"] = attribute_bonus.get(
            "AllDamageAddedRatio", 0
        ) + min(2.4, Break_Damage_Added_Ratio)

        skill_info_list = []
        # 计算普攻伤害
        skill_multiplier = self.Skill_num("Normal", "Normal")
        damagelist1 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Normal",
            "Normal",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "普攻", "damagelist": damagelist1})

        # 计算战技伤害
        skill_multiplier = self.Skill_num("BPSkill", "BPSkill")
        damagelist2 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "BPSkill",
            "BPSkill",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "战技", "damagelist": damagelist2})

        # 计算终结技伤害
        skill_multiplier = self.Skill_num("Ultra", "Ultra")
        damagelist3 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Ultra",
            "Ultra",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "终结技", "damagelist": damagelist3})

        # 计算天赋追伤伤害
        skill_multiplier = self.Skill_num("Talent", "Talent")
        damagelist4 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Talent",
            "Talent",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        damagelist4[0] += damagelist4[0] * 3
        damagelist4[1] += damagelist4[1] * 3
        damagelist4[2] += damagelist4[2] * 3
        skill_info_list.append({"name": "天赋追加攻击", "damagelist": damagelist4})

        return skill_info_list


class BlackSwan(BaseAvatar):
    Buff: BaseAvatarBuff

    def __init__(self, char: DamageInstanceAvatar, skills: List[MihomoAvatarSkill]):
        super().__init__(char=char, skills=skills)
        self.eidolon_attribute: Dict[str, float] = {}
        self.extra_ability_attribute: Dict[str, float] = {}
        self.eidolons()
        self.extra_ability()

    def Technique(self):
        pass

    def eidolons(self):
        if self.avatar_rank >= 1:
            self.eidolon_attribute["WindResistancePenetration"] = 0.25
            self.eidolon_attribute["PhysicalResistancePenetration"] = 0.25
            self.eidolon_attribute["FireResistancePenetration"] = 0.25
            self.eidolon_attribute["ThunderResistancePenetration"] = 0.25

    def extra_ability(self):
        # 战技降防计算
        bpskill_defence = self.Skill_num("BPSkill", "BPSkill_D")
        self.extra_ability_attribute["ignore_defence"] = bpskill_defence
        # 终结技加伤害
        self.extra_ability_attribute["AllDamageAddedRatio"] = self.Skill_num(
            "Ultra", "Ultra_A"
        )

    async def getdamage(
        self,
        base_attr: Dict[str, float],
        attribute_bonus: Dict[str, float],
    ):
        # 使自身造成的伤害提高, 提高数值等同于效果命中的60%, 最多使造成的伤害提高72%。
        Break_Damage_Added_Ratio = attribute_bonus.get("StatusProbabilityBase", 0) * 0.6
        attribute_bonus["AllDamageAddedRatio"] = attribute_bonus.get(
            "AllDamageAddedRatio", 0
        ) + min(0.72, Break_Damage_Added_Ratio)

        skill_info_list = []
        # 计算普攻伤害
        skill_multiplier = self.Skill_num("Normal", "Normal")
        damagelist1 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Normal",
            "Normal",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "普攻", "damagelist": damagelist1})

        # 计算战技伤害
        skill_multiplier = self.Skill_num("BPSkill", "BPSkill")
        damagelist2 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "BPSkill",
            "BPSkill",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "战技", "damagelist": damagelist2})

        # 计算终结技伤害
        skill_multiplier = self.Skill_num("Ultra", "Ultra")
        damagelist3 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Ultra",
            "Ultra",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "终结技", "damagelist": damagelist3})

        # 计算1层奥迹持续伤害
        skill_multiplier = self.Skill_num("Talent", "Talent")
        skill_multiplier += self.Skill_num("Talent", "Talent_UP")
        damagelist4 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "DOT",
            "DOT",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "1层奥迹伤害", "damagelist": damagelist4})

        # 计算50层奥迹持续伤害
        skill_multiplier = self.Skill_num("Talent", "Talent")
        skill_multiplier += self.Skill_num("Talent", "Talent_UP") * 50
        add_attr_bonus = copy.deepcopy(attribute_bonus)
        add_attr_bonus["ignore_defence"] = add_attr_bonus.get("ignore_defence", 0) + 0.2
        damagelist5 = await calculate_damage(
            base_attr,
            add_attr_bonus,
            "DOT",
            "DOT",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "50层奥迹伤害", "damagelist": damagelist5})
        return skill_info_list


class Sparkle(BaseAvatar):
    Buff: BaseAvatarBuff

    def __init__(self, char: DamageInstanceAvatar, skills: List[MihomoAvatarSkill]):
        super().__init__(char=char, skills=skills)
        self.eidolon_attribute: Dict[str, float] = {}
        self.extra_ability_attribute: Dict[str, float] = {}
        self.eidolons()
        self.extra_ability()

    def Technique(self):
        pass

    def eidolons(self):
        pass

    def extra_ability(self):
        self.extra_ability_attribute["AttackAddedRatio"] = 0.45

    async def getdamage(
        self,
        base_attr: Dict[str, float],
        attribute_bonus: Dict[str, float],
    ):
        # 终结技天赋增加伤害
        All_Damage_Add = (
            self.Skill_num("Talent", "Talent") + self.Skill_num("Ultra", "Ultra")
        ) * 3
        attribute_bonus["AllDamageAddedRatio"] = (
            attribute_bonus.get("AllDamageAddedRatio", 0) + All_Damage_Add
        )

        # 战技增加暴击伤害
        if self.avatar_rank >= 6:
            add_critical_damage_base = attribute_bonus.get("CriticalDamageBase", 0) * (
                self.Skill_num("BPSkill", "BPSkill") + 0.3
            ) + self.Skill_num("BPSkill", "BPSkill_G")
        else:
            add_critical_damage_base = attribute_bonus.get(
                "CriticalDamageBase", 0
            ) * self.Skill_num("BPSkill", "BPSkill") + self.Skill_num(
                "BPSkill", "BPSkill_G"
            )
        attribute_bonus["CriticalDamageBase"] = (
            attribute_bonus.get("CriticalDamageBase", 0) + add_critical_damage_base
        )

        skill_info_list = []
        # 计算普攻伤害
        skill_multiplier = self.Skill_num("Normal", "Normal")
        damagelist1 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Normal",
            "Normal",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "普攻", "damagelist": damagelist1})

        # 计算终结技
        critical_damage_base_str = add_critical_damage_base * 100
        damagelist2 = []
        damagelist2.append(critical_damage_base_str)
        skill_info_list.append({"name": "战技提升爆伤(%)", "damagelist": damagelist2})

        return skill_info_list


class Acheron(BaseAvatar):
    Buff: BaseAvatarBuff

    def __init__(self, char: DamageInstanceAvatar, skills: List[MihomoAvatarSkill]):
        super().__init__(char=char, skills=skills)
        self.eidolon_attribute: Dict[str, float] = {}
        self.extra_ability_attribute: Dict[str, float] = {}
        self.eidolons()
        self.extra_ability()

    def Technique(self):
        pass

    def eidolons(self):
        if self.avatar_rank >= 1:
            self.eidolon_attribute["CriticalChanceBase"] = 0.18
        if self.avatar_rank >= 4:
            self.eidolon_attribute["Ultra_DmgRatio"] = 0.08
        if self.avatar_rank >= 6:
            self.eidolon_attribute["Ultra_AllDamageResistancePenetration"] = 0.2

    def extra_ability(self):
        self.extra_ability_attribute["AttackAddedRatio"] = 0.45

    async def getdamage(
        self,
        base_attr: Dict[str, float],
        attribute_bonus: Dict[str, float],
    ):
        attribute_bonus["AllDamageAddedRatio"] = (
            attribute_bonus.get("AllDamageAddedRatio", 0) + 0.9
        )

        skill_info_list = []
        # 计算普攻伤害
        skill_multiplier = self.Skill_num("Normal", "Normal")
        if self.avatar_rank >= 6:
            damagelist1 = await calculate_damage(
                base_attr,
                attribute_bonus,
                "Normal",
                "Ultra",
                self.avatar_element,
                skill_multiplier,
                self.avatar_level,
            )
        else:
            damagelist1 = await calculate_damage(
                base_attr,
                attribute_bonus,
                "Normal",
                "Normal",
                self.avatar_element,
                skill_multiplier,
                self.avatar_level,
            )
        damagelist1[0] = damagelist1[0] * 1.6
        damagelist1[1] = damagelist1[1] * 1.6
        damagelist1[2] = damagelist1[2] * 1.6
        skill_info_list.append({"name": "普攻", "damagelist": damagelist1})

        # 计算战技伤害
        skill_multiplier = self.Skill_num("BPSkill", "BPSkill")
        if self.avatar_rank >= 6:
            damagelist2 = await calculate_damage(
                base_attr,
                attribute_bonus,
                "BPSkill",
                "Ultra",
                self.avatar_element,
                skill_multiplier,
                self.avatar_level,
            )
        else:
            damagelist2 = await calculate_damage(
                base_attr,
                attribute_bonus,
                "BPSkill",
                "Normal",
                self.avatar_element,
                skill_multiplier,
                self.avatar_level,
            )
        damagelist2[0] = damagelist2[0] * 1.6
        damagelist2[1] = damagelist2[1] * 1.6
        damagelist2[2] = damagelist2[2] * 1.6
        skill_info_list.append({"name": "战技", "damagelist": damagelist2})

        # 计算终结技
        add_attr_bonus = copy.deepcopy(attribute_bonus)
        add_attr_bonus["AllDamageResistancePenetration"] = (
            add_attr_bonus.get("AllDamageResistancePenetration", 0) + 0.2
        )
        # 啼泽雨斩
        skill_multiplier = self.Skill_num("Ultra", "Ultra_1_d")
        damagelist_u_1_d = await calculate_damage(
            base_attr,
            add_attr_bonus,
            "Ultra",
            "Ultra",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        damagelist_u_2_d = await calculate_damage(
            base_attr,
            add_attr_bonus,
            "Ultra",
            "Ultra",
            self.avatar_element,
            0.6,
            self.avatar_level,
        )
        damagelist_u_1_d[0] = damagelist_u_1_d[0] * 1.6 + damagelist_u_2_d[0] * 1.6
        damagelist_u_1_d[1] = damagelist_u_1_d[1] * 1.6 + damagelist_u_2_d[1] * 1.6
        damagelist_u_1_d[2] = damagelist_u_1_d[2] * 1.6 + damagelist_u_2_d[2] * 1.6
        skill_info_list.append({"name": "啼泽雨斩", "damagelist": damagelist_u_1_d})
        # 黄泉返渡
        skill_multiplier = self.Skill_num("Ultra", "Ultra_1_a")
        damagelist_u_1_a = await calculate_damage(
            base_attr,
            add_attr_bonus,
            "Ultra",
            "Ultra",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        damagelist_u_1_a_e = await calculate_damage(
            base_attr,
            add_attr_bonus,
            "Ultra",
            "Ultra",
            self.avatar_element,
            0.25,
            self.avatar_level,
        )
        damagelist_u_1_a[0] = (
            damagelist_u_1_a[0] * 1.6 + (damagelist_u_1_a_e[0] * 1.6) * 6
        )
        damagelist_u_1_a[1] = (
            damagelist_u_1_a[1] * 1.6 + (damagelist_u_1_a_e[1] * 1.6) * 6
        )
        damagelist_u_1_a[2] = (
            damagelist_u_1_a[2] * 1.6 + (damagelist_u_1_a_e[2] * 1.6) * 6
        )
        skill_info_list.append({"name": "黄泉返渡", "damagelist": damagelist_u_1_a})

        # 总伤害
        damagelist_u = {}
        damagelist_u[0] = damagelist_u_1_d[0] * 3 + damagelist_u_1_a[0]
        damagelist_u[1] = damagelist_u_1_d[1] * 3 + damagelist_u_1_a[1]
        damagelist_u[2] = damagelist_u_1_d[2] * 3 + damagelist_u_1_a[2]
        skill_info_list.append({"name": "终结技总伤", "damagelist": damagelist_u})
        return skill_info_list


class Aventurine(BaseAvatar):
    Buff: BaseAvatarBuff

    def __init__(self, char: DamageInstanceAvatar, skills: List[MihomoAvatarSkill]):
        super().__init__(char=char, skills=skills)
        self.eidolon_attribute: Dict[str, float] = {}
        self.extra_ability_attribute: Dict[str, float] = {}
        self.eidolons()
        self.extra_ability()

    def Technique(self):
        pass

    def eidolons(self):
        if self.avatar_rank >= 1:
            self.eidolon_attribute["CriticalDamageBase"] = 0.2
        if self.avatar_rank >= 2:
            self.eidolon_attribute["AllDamageResistancePenetration"] = 0.12
        if self.avatar_rank >= 4:
            self.eidolon_attribute["DefenceAddedRatio"] = 0.4
        if self.avatar_rank >= 6:
            self.eidolon_attribute["AllDamageAddedRatio"] = 1.5

    def extra_ability(self):
        pass

    async def getdamage(
        self,
        base_attr: Dict[str, float],
        attribute_bonus: Dict[str, float],
    ):
        # 天赋增加暴击
        defence = base_attr["defence"] * (
            1 + attribute_bonus.get("DefenceAddedRatio", 0)
        ) + attribute_bonus.get("DefenceDelta", 0)
        if defence > 1600:
            adddefrnce = defence - 1600
            Critical_Chance_Base = (defence / 100) * 0.02
            Critical_Chance_Base = min(Critical_Chance_Base, 0.48)
            attribute_bonus["CriticalChanceBase"] = (
                attribute_bonus.get("CriticalChanceBase", 0) + Critical_Chance_Base
            )

        # 终结技增加暴击伤害
        attribute_bonus["CriticalDamageBase"] = attribute_bonus.get(
            "CriticalDamageBase", 0
        ) + self.Skill_num("Ultra", "Ultra_CD")

        skill_info_list = []
        # 计算普攻伤害
        skill_multiplier = self.Skill_num("Normal", "Normal")
        damagelist1 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Normal",
            "Normal",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
            2,
        )
        skill_info_list.append({"name": "普攻", "damagelist": damagelist1})

        # 计算战技护盾
        skill_multiplier = self.Skill_num("BPSkill", "BPSkill")
        skill_num = self.Skill_num("BPSkill", "BPSkill_G")
        damagelist2 = await calculate_shield(
            base_attr,
            attribute_bonus,
            skill_multiplier,
            skill_num,
        )
        skill_info_list.append({"name": "战技(护盾)", "damagelist": damagelist2})

        # 计算终结技伤害
        skill_multiplier = self.Skill_num("Ultra", "Ultra")
        damagelist3 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Ultra",
            "Ultra",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
            2,
        )
        skill_info_list.append({"name": "终结技", "damagelist": damagelist3})

        duanshu = 7
        if self.avatar_rank >= 4:
            duanshu = 10
        damagelist5 = {}
        # 计算天赋追加攻击伤害
        skill_multiplier = self.Skill_num("Talent", "Talent")
        damagelist4 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Talent",
            "Talent",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
            2,
        )
        damagelist5[0] = damagelist4[0] * duanshu
        damagelist5[1] = damagelist4[1] * duanshu
        damagelist5[2] = damagelist4[2] * duanshu
        skill_info_list.append({"name": "单层【盲注】追击", "damagelist": damagelist4})
        skill_info_list.append({"name": "满层【盲注】追击", "damagelist": damagelist5})

        return skill_info_list


class Gallagher(BaseAvatar):
    Buff: BaseAvatarBuff

    def __init__(self, char: DamageInstanceAvatar, skills: List[MihomoAvatarSkill]):
        super().__init__(char=char, skills=skills)
        self.eidolon_attribute: Dict[str, float] = {}
        self.extra_ability_attribute: Dict[str, float] = {}
        self.eidolons()
        self.extra_ability()

    def Technique(self):
        pass

    def eidolons(self):
        if self.avatar_rank >= 6:
            self.eidolon_attribute["BreakDamageAddedRatioBase"] = 0.2

    def extra_ability(self):
        pass

    async def getdamage(
        self,
        base_attr: Dict[str, float],
        attribute_bonus: Dict[str, float],
    ):
        # 使自身提供的治疗量提高, 提高数值等同于击破特攻的50%, 最多使提供的治疗量提高75%
        Break_Damage_Added_Ratio_Base = attribute_bonus.get(
            "BreakDamageAddedRatioBase", 0
        )
        Heal_Ratio_Base = Break_Damage_Added_Ratio_Base * 0.5
        Heal_Ratio_Base = min(0.75, Heal_Ratio_Base)
        attribute_bonus["HealRatioBase"] = (
            attribute_bonus.get("HealRatioBase", 0) + Heal_Ratio_Base
        )

        skill_info_list = []
        # 计算普攻伤害
        skill_multiplier = self.Skill_num("Normal", "Normal")
        damagelist1 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Normal",
            "Normal",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "普攻", "damagelist": damagelist1})

        # 计算强化普攻伤害
        skill_multiplier = self.Skill_num("Normal", "Normal1")
        damagelist2 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Normal",
            "Normal1",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "强化普攻", "damagelist": damagelist2})

        # 计算战技治疗量
        skill_num = self.Skill_num("BPSkill", "BPSkill")
        damagelist3 = await calculate_heal(
            base_attr,
            attribute_bonus,
            "BPSkill",
            0,
            skill_num,
        )
        skill_info_list.append({"name": "战技治疗量", "damagelist": damagelist3})

        # 计算终结技伤害
        skill_multiplier = self.Skill_num("Ultra", "Ultra")
        damagelist4 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Ultra",
            "Ultra",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "结技", "damagelist": damagelist4})

        # 计算天赋治疗量
        skill_num = self.Skill_num("Talent", "Talent")
        damagelist5 = await calculate_heal(
            base_attr,
            attribute_bonus,
            "Talent",
            0,
            skill_num,
        )
        skill_info_list.append({"name": "天赋治疗量", "damagelist": damagelist5})

        return skill_info_list


class Robin(BaseAvatar):
    Buff: BaseAvatarBuff

    def __init__(self, char: DamageInstanceAvatar, skills: List[MihomoAvatarSkill]):
        super().__init__(char=char, skills=skills)
        self.eidolon_attribute: Dict[str, float] = {}
        self.extra_ability_attribute: Dict[str, float] = {}
        self.eidolons()
        self.extra_ability()

    def Technique(self):
        pass

    def eidolons(self):
        if self.avatar_rank >= 1:
            self.eidolon_attribute["AllDamageResistancePenetration"] = 0.24

    def extra_ability(self):
        self.extra_ability_attribute["Talent_CriticalDamageBase"] = 0.25

    async def getdamage(
        self,
        base_attr: Dict[str, float],
        attribute_bonus: Dict[str, float],
    ):
        # 战技伤害加成
        all_damage_added_ratio = attribute_bonus.get("AllDamageAddedRatio", 0)
        attribute_bonus["AllDamageAddedRatio"] = (
            all_damage_added_ratio + self.Skill_num("BPSkill", "BPSkill")
        )

        # 终结技攻击加成计算
        attack = base_attr["attack"] * (
            1 + attribute_bonus.get("AttackAddedRatio", 0)
        ) + attribute_bonus.get("AttackDelta", 0)
        add_attack = (attack * self.Skill_num("Ultra", "Ultra_A")) + self.Skill_num(
            "Ultra", "Ultra_G"
        )
        attribute_bonus["AttackDelta"] = (
            attribute_bonus.get("AttackDelta", 0) + add_attack
        )

        # 天赋爆伤加成
        Critical_Damage_Base = attribute_bonus.get("CriticalDamageBase", 0)
        attribute_bonus["CriticalDamageBase"] = Critical_Damage_Base + self.Skill_num(
            "Talent", "Talent"
        )

        skill_info_list = []
        # 计算普攻伤害
        skill_multiplier = self.Skill_num("Normal", "Normal")
        damagelist1 = await calculate_damage(
            base_attr,
            attribute_bonus,
            "Normal",
            "Normal",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "普攻", "damagelist": damagelist1})

        # 计算战技治疗量
        skill_num = self.Skill_num("BPSkill", "BPSkill")
        damagelist2 = {}
        damagelist2[0] = add_attack
        skill_info_list.append({"name": "终结技攻击提高", "damagelist": damagelist2})

        # 计算追击伤害
        skill_multiplier = self.Skill_num("Ultra", "Ultra")
        add_attr_bonus = copy.deepcopy(attribute_bonus)
        add_attr_bonus["CriticalDamageBase"] = 1
        add_attr_bonus["CriticalChanceBase"] = 0.95
        if self.avatar_rank >= 6:
            add_attr_bonus["CriticalDamageBase"] = 5.5
        damagelist4 = await calculate_damage(
            base_attr,
            add_attr_bonus,
            "fujia",
            "fujia",
            self.avatar_element,
            skill_multiplier,
            self.avatar_level,
        )
        skill_info_list.append({"name": "【协奏】附加伤害", "damagelist": damagelist4})

        return skill_info_list


class AvatarDamage:
    @classmethod
    def create(cls, char: DamageInstanceAvatar, skills: List[MihomoAvatarSkill]):
        if char.id_ == 1214:
            return XueYi(char, skills)
        if char.id_ == 1306:
            return Sparkle(char, skills)
        if char.id_ == 1308:
            return Acheron(char, skills)
        if char.id_ == 1309:
            return Robin(char, skills)
        if char.id_ == 1303:
            return RuanMei(char, skills)
        if char.id_ == 1304:
            return Aventurine(char, skills)
        if char.id_ == 1301:
            return Gallagher(char, skills)
        if char.id_ == 1307:
            return BlackSwan(char, skills)
        if char.id_ == 1305:
            return DrRatio(char, skills)
        if char.id_ == 1215:
            return Hanya(char, skills)
        if char.id_ == 1217:
            return Huohuo(char, skills)
        if char.id_ == 8003 or char.id_ == 8004:
            return Trailblazer_K(char, skills)
        if char.id_ == 8002 or char.id_ == 8001:
            return Trailblazer(char, skills)
        if char.id_ == 1202:
            return Tingyun(char, skills)
        if char.id_ == 1109:
            return Hook(char, skills)
        if char.id_ == 1108:
            return Sampo(char, skills)
        if char.id_ == 1106:
            return Pela(char, skills)
        if char.id_ == 1103:
            return Serval(char, skills)
        if char.id_ == 1013:
            return Herta(char, skills)
        if char.id_ == 1009:
            return Asta(char, skills)
        if char.id_ == 1008:
            return Arlan(char, skills)
        if char.id_ == 1002:
            return DanHeng(char, skills)
        if char.id_ == 1111:
            return Luka(char, skills)
        if char.id_ == 1206:
            return Sushang(char, skills)
        if char.id_ == 1101:
            return Bronya(char, skills)
        if char.id_ == 1207:
            return Yukong(char, skills)
        if char.id_ == 1001:
            return Mar7th(char, skills)
        if char.id_ == 1105:
            return Natasha(char, skills)
        if char.id_ == 1110:
            return Lynx(char, skills)
        if char.id_ == 1211:
            return Bailu(char, skills)
        if char.id_ == 1203:
            return Luocha(char, skills)
        if char.id_ == 1210:
            return Guinaifen(char, skills)
        if char.id_ == 1302:
            return Argenti(char, skills)
        if char.id_ == 1112:
            return Topaz(char, skills)
        if char.id_ == 1104:
            return Gepard(char, skills)
        if char.id_ == 1005:
            return Kafka(char, skills)
        if char.id_ == 1201:
            return Qingque(char, skills)
        if char.id_ == 1212:
            return Jingliu(char, skills)
        if char.id_ == 1107:
            return Clara(char, skills)
        if char.id_ == 1205:
            return Blade(char, skills)
        if char.id_ == 1003:
            return Himeko(char, skills)
        if char.id_ == 1209:
            return Yanqing(char, skills)
        if char.id_ == 1102:
            return Seele(char, skills)
        if char.id_ == 1208:
            return Fuxuan(char, skills)
        if char.id_ == 1006:
            return Silverwolf(char, skills)
        if char.id_ == 1204:
            return JingYuan(char, skills)
        if char.id_ == 1004:
            return Welt(char, skills)
        if char.id_ == 1213:
            return Danhengil(char, skills)
        return None
