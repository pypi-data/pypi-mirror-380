import copy
import time
from typing import Protocol

from autowsgr.configs import NodeConfig
from autowsgr.constants.custom_exceptions import ImageNotFoundErr, NetworkErr
from autowsgr.constants.image_templates import IMG, MyTemplate
from autowsgr.constants.other_constants import ALL_SHIP_TYPES
from autowsgr.constants.positions import BLOOD_BAR_POSITION
from autowsgr.constants.ui import Node
from autowsgr.game.expedition import Expedition
from autowsgr.game.game_operation import (
    click_result,
    destroy_ship,
    detect_ship_stats,
    get_ship,
    match_night,
)
from autowsgr.game.get_game_info import get_enemy_condition, get_enemy_formation
from autowsgr.timer import Timer
from autowsgr.types import ConditionFlag, Formation, SearchEnemyAction
from autowsgr.utils.logger import Logger
from autowsgr.utils.math_functions import get_nearest


def start_march(timer: Timer, position: tuple[int, int] = (900, 500)) -> ConditionFlag:
    timer.click(*position, 1, delay=0)
    start_time = time.time()
    while timer.identify_page('fight_prepare_page'):
        if time.time() - start_time > 3:
            timer.click(*position, 1, delay=0)
            time.sleep(1)
        if timer.image_exist(IMG.symbol_image[3], need_screen_shot=False):
            return ConditionFlag.DOCK_FULL
        if timer.image_exist(IMG.symbol_image[9], need_screen_shot=False, confidence=0.8):
            time.sleep(1)
            return ConditionFlag.BATTLE_TIMES_EXCEED
        if time.time() - start_time > 15:
            if timer.process_bad_network():
                if timer.identify_page('fight_prepare_page'):
                    return start_march(timer, position)
                NetworkErr('stats unknown')
            else:
                raise TimeoutError('map_fight prepare timeout')
    return ConditionFlag.OPERATION_SUCCESS


class FightResultInfo:
    def __init__(self, timer: Timer, ship_stats) -> None:
        try:
            mvp_pos = timer.wait_image(IMG.fight_image[14])
            self.mvp = get_nearest((mvp_pos[0], mvp_pos[1] + 20), BLOOD_BAR_POSITION[1])
        except Exception as e:
            timer.log_screen(name='mvp_image')
            timer.logger.warning(f"can't identify mvp, error: {e}")
        self.ship_stats = detect_ship_stats(timer, 'sumup', ship_stats)

        self.result = timer.wait_images(IMG.fight_result, timeout=5)
        if timer.image_exist(IMG.fight_result['SS'], need_screen_shot=False):
            self.result = 'SS'
        if self.result is None:
            timer.log_screen()
            timer.logger.warning("can't identify fight result, screen logged")

    def __str__(self) -> str:
        return f'MVP 为 {self.mvp} 号位, 战果为 {self.result}'

    def __lt__(self, other) -> bool:  # <
        order = ['D', 'C', 'B', 'A', 'S', 'SS']
        if isinstance(other, FightResultInfo):
            other = other.result

        return order.index(self.result) < order.index(other)

    def __le__(self, other) -> bool:  # <=
        order = ['D', 'C', 'B', 'A', 'S', 'SS']
        if isinstance(other, FightResultInfo):
            other = other.result

        return order.index(self.result) <= order.index(other)

    def __gt__(self, other) -> bool:  # >
        return not (self <= other)

    def __ge__(self, other) -> bool:  # >=
        return not (self < other)


class FightEvent:
    """战斗事件类
    事件列表: 战况选择, 获取资源, 索敌成功, 迂回, 阵型选择, 进入战斗, 是否夜战, 战斗结算, 获取舰船, 继续前进, 自动回港

    状态: 一个字典, 一共三种键值
        position: 位置, 所有事件均存在

        ship_stats: 我方舰船状态(仅在 "继续前进" 事件存在)

        enemies: 敌方舰船(仅在 "索敌成功" 事件存在), 字典或 "索敌失败"

        info: 其它额外信息(仅在 "自动回港" 事件存在)

    动作: 一个字符串
        "继续": 获取资源, 迂回, 战斗结算, 获取舰船, 自动回港等不需要决策的操作

        数字字符串: 战况选择的决策

        "SL"/数字字符串: 阵型选择的决策

        "继续"/ "SL": 进入战斗后的决策

        "战斗"/"撤退"/"迂回": 索敌成功的决策

        "追击"/"撤退": 夜战的决策

        "回港/前进": 是否前进的选择(战斗结算完毕后)

    结果: 一个字符串
        "无": 战况选择, 获取资源, 索敌成功, 阵型选择, 进入战斗, 是否夜战, 继续前进, 自动回港,

        (FightResultInfo): 表示战果信息, 战果结算

        舰船名: 获取舰船
    """

    def __init__(self, event, stats, action='继续', result='无') -> None:
        self.event = event
        self.stats = stats
        self.action = action
        self.result = result

    def __str__(self) -> str:
        return f'事件:{self.event}, 状态:{self.stats}, 动作:{self.action}, 结果:{self.result!s}'

    def __repr__(self) -> str:
        return f'FightEvent({self.event}, {self.stats}, {self.action}, {self.result})'


class FightHistory:
    """记录并处理战斗历史信息"""

    def __init__(self) -> None:
        self.events: list[FightEvent] = []

    def add_event(self, event, point, action='继续', result='无'):
        self.events.append(FightEvent(event, point, action, result))

    def reset(self):
        self.events = []

    def get_fight_results(self):
        results_dict = {}
        results_list = []
        for event in self.events:
            if event.event == '战果结算':
                if event.stats['position'].isalpha():
                    results_dict[event.stats['position']] = event.result
                else:
                    results_list.append(event.result)
        return results_list if len(results_list) else results_dict

    def get_last_point(self):
        return self.events[-1].stats['position']

    def __str__(self) -> str:
        return ''.join(str(event) + '\n' for event in self.events)


class FightInfo(Protocol):
    """存储战斗中需要用到的所有状态信息, 以及更新逻辑"""

    timer: Timer
    logger: Logger
    oil: int
    ammo: int
    enemies: dict
    ship_stats: list
    fight_history: FightHistory
    enemy_formation: str
    node: str

    # =============== 静态属性 ===============
    end_page: str
    """结束战斗后的页面，用于判断是否已经返回战斗外界面"""
    successor_states: dict[str, list[str] | dict[str, list[str]]]
    """战斗流程的有向图建模。格式为:
        1. {状态名: [后继状态1, 后继状态2, ...]}
        2. {状态名: {动作1: [后继状态1, 后继状态2, ...], 动作2: [后继状态1, 后继状态2, ...]}}
    """
    state2image: dict[str, list[MyTemplate, float]]
    """所需用到的图片模板。格式为 {状态明： [模板，等待时间(秒)]}"""
    after_match_delay: dict[str, float]
    """匹配成功后的延时。格式为 {状态名: 延时时间(秒)}"""

    # =============== 运行时属性 ===============
    last_state: str
    """上一个状态 s_{t-1}"""
    last_action: str
    """上一个动作 a_{t-1}"""
    state: str
    """当前状态 s_t"""

    def __init__(self, timer: Timer) -> None:
        self.timer = timer
        self.logger = timer.logger

        self.last_state = ''
        self.last_action = ''
        self.state = ''

        self.enemies = {}  # 敌方舰船列表
        self.ship_stats = []  # 我方舰船血量列表
        self.oil = 10  # 我方剩余油量
        self.ammo = 10  # 我方剩余弹药量
        self.fight_history = FightHistory()  # 战斗结果记录

    def update_state(self):
        self.last_state = self.state

        # 计算当前可能的状态
        possible_states = copy.deepcopy(self.successor_states[self.last_state])
        if isinstance(possible_states, dict):
            possible_states = possible_states[self.last_action]
        modified_timeout = [-1 for _ in possible_states]  # 某些状态需要修改等待时间
        for i, state in enumerate(possible_states):
            if isinstance(state, list):
                state, timeout = state
                possible_states[i] = state
                modified_timeout[i] = timeout
        if self.timer.config.show_match_fight_stage:
            self.logger.debug('waiting:', possible_states, '  ')
        images = [self.state2image[state][0] for state in possible_states]
        timeout = [self.state2image[state][1] for state in possible_states]
        confidence = min(
            [0.8]
            + [
                self.state2image[state][2]
                for state in possible_states
                if len(self.state2image[state]) >= 3
            ],
        )
        timeout = [
            timeout[i] if modified_timeout[i] == -1 else modified_timeout[i]
            for i in range(len(timeout))
        ]
        timeout = max(timeout)
        # 等待其中一种出现
        fun_start_time = time.time()
        while time.time() - fun_start_time <= timeout:
            self._before_match()

            # 尝试匹配
            ret = [self.timer.image_exist(image, False, confidence=confidence) for image in images]
            if any(ret):
                self.state = possible_states[ret.index(True)]
                # 查询是否有匹配后延时
                if self.state in self.after_match_delay:
                    delay = self.after_match_delay[self.state]
                    time.sleep(delay)

                if self.timer.config.show_match_fight_stage:
                    self.logger.info(f'matched: {self.state}')
                self._after_match()

                return self.state

        # 匹配不到时报错
        self.logger.warning(
            f'匹配状态失败! state: {self.state}  last_action: {self.last_action}',
        )
        self.timer.log_screen(True)
        for image in images:
            self.logger.log_image(image, f'match_{time.time()!s}.PNG')
        raise ImageNotFoundErr

    def _before_match(self):
        """每一轮尝试匹配状态前执行的操作"""

    def _after_match(self):
        """匹配到状态后执行的操作"""
        if self.state == 'spot_enemy_success':
            self.enemies = get_enemy_condition(self.timer, 'fight')
            self.enemy_formation = get_enemy_formation(self.timer)
        if self.state == 'result':
            try:
                result = FightResultInfo(self.timer, self.ship_stats)
                self.ship_stats = result.ship_stats
                self.fight_history.add_event(
                    '战果结算',
                    {
                        'position': (
                            self.node
                            if 'node' in self.__dict__
                            else f'此类战斗({type(self)})不支持节点信息'
                        ),
                    },
                    result=result,
                )
            except Exception as e:
                self.logger.warning(f'战果结算记录失败：{e}')

    def reset(self):
        """需要记录与初始化的战斗信息"""


class FightPlan(Protocol):
    info: FightInfo
    timer: Timer
    logger: Logger
    fight_logs: list[FightHistory]

    def __init__(self, timer: Timer) -> None:
        # 把 timer 引用作为内置对象，减少函数调用的时候所需传入的参数
        self.timer = timer
        self.logger = timer.logger
        self.fight_logs = []

    def fight(self) -> ConditionFlag:
        self.info.reset()  # 初始化战斗信息
        while True:
            ret = self._make_decision()
            if ret == ConditionFlag.FIGHT_CONTINUE:
                continue
            if ret == ConditionFlag.SL:
                self._sl()
                return ConditionFlag.SL
            if ret == ConditionFlag.FIGHT_END:
                self.timer.set_page(self.info.end_page)
                self.fight_logs.append(self.info.fight_history)
                return ConditionFlag.OPERATION_SUCCESS

    def run_for_times(self, times, gap=1800) -> ConditionFlag:
        """多次执行同一任务, 自动进行远征操作
        Args:
            times (int): 任务执行总次数

            gap (int): 强制远征检查的间隔时间
        Raise:
            RuntimeError: 战斗进行时出现错误
        Returns:
            ConditionFlag
        """
        assert times >= 1
        expedition = Expedition(self.timer)
        self.timer.goto_game_page('map_page')
        for i in range(times):
            if time.time() - self.timer.last_expedition_check_time >= gap:
                expedition.run(True)
            elif isinstance(self.timer.now_page, Node) and self.timer.now_page.name == 'map_page':
                expedition.run(False)
                self.timer.goto_game_page('map_page')
            fight_flag = self.run()
            if fight_flag not in [ConditionFlag.SL, ConditionFlag.OPERATION_SUCCESS]:
                if fight_flag == ConditionFlag.DOCK_FULL:
                    return ConditionFlag.DOCK_FULL
                if fight_flag == ConditionFlag.SKIP_FIGHT:
                    return ConditionFlag.SKIP_FIGHT
                raise RuntimeError(f'战斗进行时出现异常, 信息为 {fight_flag}')
            self.timer.logger.info(f'已出击次数:{i + 1}，目标次数{times}')
        return ConditionFlag.OPERATION_SUCCESS

    def run(self, retry_times=0, max_try_times=5) -> ConditionFlag:
        """主函数，负责一次完整的战斗.
        Args:
            retry_times (int): 重试次数
            max_try_times (int): 最大尝试次数
        Returns:
            ConditionFlag
        """
        # 战斗前逻辑
        ret = self._enter_fight()

        if ret == ConditionFlag.OPERATION_SUCCESS:
            pass
        elif ret == ConditionFlag.DOCK_FULL:
            # 自动解装功能
            if self.timer.config.dock_full_destroy and retry_times < max_try_times:
                self.logger.debug(f'船坞已满, 正在解装, 尝试次数:{retry_times + 1}')
                self.timer.relative_click(0.38, 0.565)
                destroy_ship(self.timer)
                return self.run(retry_times + 1)
            return ret
        elif ret == ConditionFlag.FIGHT_END:
            self.timer.set_page(self.info.end_page)
            return ret
        elif ret == ConditionFlag.BATTLE_TIMES_EXCEED or ret == ConditionFlag.SKIP_FIGHT:
            return ret
        else:
            self.logger.error('无法进入战斗, 原因未知! 屏幕状态已记录')
            self.timer.log_screen()
            raise BaseException(str(time.time()) + 'enter fight error')

        # 战斗中逻辑
        return self.fight()

    def run_for_times_condition(
        self,
        times,
        last_point,
        result='S',
        insist_time=900,
    ) -> ConditionFlag | bool:
        """有战果要求的多次运行, 使用前务必检查参数是否有误, 防止死循环

        Args:
            times: 次数

            last_point: 最后一个点

            result: 战果要求

            insist_time: 如果大于这个时间工作量未减少则退出工作

        Returns:
            ConditionFlag
            False: 不满足预设条件, 此次战斗不计入次数
        """
        if not isinstance(result, str) or not isinstance(last_point, str):
            raise TypeError(
                f'last_point, result must be str,but is {type(last_point)}, {type(result)}',
            )
        if result not in ['S', 'A', 'B', 'C', 'D', 'SS']:
            raise ValueError(
                f"result value {result} is illegal, it should be 'A','B','C','D','S' or 'SS'",
            )
        if len(last_point) != 1 or ord(last_point) > ord('Z') or ord(last_point) < ord('A'):
            raise ValueError("last_point should be a uppercase within 'A' to 'Z'")
        import time

        result_list = ['SS', 'S', 'A', 'B', 'C', 'D']
        start_time = time.time()
        while times:
            ret = self.run()
            if ret == ConditionFlag.DOCK_FULL:
                self.timer.logger.error('船坞已满, 无法继续')
                return ret

            self.logger.info('战斗信息:\n' + str(self.info.fight_history))
            fight_results = sorted(self.info.fight_history.get_fight_results().items())
            # 根据情况截取战果，并在result_list查找索引
            if len(fight_results):
                if str(fight_results[-1][1])[-2].isalpha():
                    fight_result_index = result_list.index(
                        str(fight_results[-1][1])[-2:],
                    )
                else:
                    fight_result_index = result_list.index(
                        str(fight_results[-1][1])[-1],
                    )

            finish = (
                len(fight_results)
                and fight_results[-1][0] == last_point
                and fight_result_index <= result_list.index(result)
            )
            if not finish:
                self.timer.logger.info(
                    f'不满足预设条件, 此次战斗不计入次数, 剩余战斗次数:{times}',
                )
                if time.time() - start_time > insist_time:
                    return False
            else:
                start_time, times = time.time(), times - 1
                self.timer.logger.info(
                    f'完成了一次满足预设条件的战斗, 剩余战斗次数:{times}',
                )
        return ConditionFlag.OPERATION_SUCCESS

    def update_state(self, *args, **kwargs):
        try:
            self.info.update_state()
            state = self.info.state
            self.timer.keep_try_update_fight = 0
        except ImageNotFoundErr as _:
            # 处理点击延迟或者网络波动导致的匹配失败
            if (
                hasattr(self.timer, 'keep_try_update_fight')
                and self.timer.keep_try_update_fight > 3
            ):
                return ConditionFlag.SL
            if hasattr(self.timer, 'keep_try_update_fight'):
                self.timer.keep_try_update_fight += 1
            else:
                self.timer.keep_try_update_fight = 1
            self.logger.warning('Image Match Failed, Trying to Process')
            if self.timer.is_other_device_login():
                self.timer.process_other_device_login()  # TODO: 处理其他设备登录
            if self.timer.is_bad_network(timeout=5):
                self.timer.process_bad_network(extra_info='update_state', timeout=5)
            self._make_decision(skip_update=True)
            # if self.info.last_state == "spot_enemy_success":
            #     if self.timer.image_exist(IMG.fight_image[2]):
            #         self.timer.click(900, 500)
            # if self.info.last_state in ["proceed", "night"] and self.timer.image_exist(
            #     IMG.fight_image[5:7]
            # ):
            #     if self.info.last_action == "yes":
            #         self.timer.click(325, 350, times=1)
            #     else:
            #         self.timer.click(615, 350, times=1)

            if 'try_times' not in kwargs:
                return self.update_state(try_times=1)
            time.sleep(10 * 2.5 ** kwargs['try_times'])
            return self.update_state(try_times=kwargs['try_times'] + 1)
        return state

    def _enter_fight(self) -> ConditionFlag:
        """进入战斗前的操作"""

    def _make_decision(self, *args, **kwargs) -> str:
        """决策函数"""

    # =============== 战斗中通用的操作 ===============
    def _sl(self):
        self.timer.logger.debug('正在执行SL操作')
        # 重置地图节点信息
        self.timer.reset_chapter_map()

        self.timer.restart()
        self.timer.go_main_page()
        self.timer.set_page('main_page')


class DecisionBlock:
    """地图上一个节点的决策模块"""

    def __init__(self, timer: Timer, args) -> None:
        self.timer = timer
        self.logger = timer.logger
        self.config = NodeConfig.from_dict(args)

        # 用于根据规则设置阵型
        self.set_formation_by_rule = False
        self.formation_by_rule = Formation.double_column

    def _check_rules(self, enemies: dict) -> SearchEnemyAction | Formation:
        for rule in self.config.enemy_rules:
            condition, act = rule
            eval_condition = ''
            last = 0
            for i, ch in enumerate(condition):
                if ord(ch) > ord('Z') or ord(ch) < ord('A'):
                    if last != i:
                        if condition[last:i] in ALL_SHIP_TYPES:
                            eval_condition += str(enemies.get(condition[last:i], 0))
                        else:
                            eval_condition += condition[last:i]
                    eval_condition += ch
                    last = i + 1

            condition_result = eval(eval_condition)
            if self.timer.config.show_enemy_rules:
                act_info = f'判断敌舰规则: {condition}, 结果: {condition_result}'
                if condition_result:
                    act_info += ', 执行: '
                    act_info += act if isinstance(act, str) else f'选择阵型: {act}'
                else:
                    act_info += ', 不执行特殊操作进入战斗'
                self.logger.info(act_info)
            if condition_result:
                if isinstance(act, str):
                    return SearchEnemyAction(act)
                return Formation(act)
        return SearchEnemyAction.no_action

    def _check_formation_rules(self, formation: str) -> SearchEnemyAction | Formation:
        for rule in self.config.enemy_formation_rules:
            condition, act = rule
            condition_result = condition == formation
            act_info = f'判断敌舰阵容规则: {condition}, 结果: {condition_result}'
            if condition_result:
                act_info += f', 执行: {act}'
                if isinstance(act, str):
                    return SearchEnemyAction(act)
                return Formation(act)
            act_info += ', 不执行特殊操作进入战斗'
        return SearchEnemyAction.no_action

    def make_decision(self, state, last_state, last_action, info: FightInfo):
        # destroy_ship skip: extract-method
        """单个节点的决策"""
        enemies = info.enemies
        if state in ['fight_period', 'night_fight_period']:
            if self.config.SL_when_enter_fight:
                info.fight_history.add_event(
                    '进入战斗',
                    {
                        'position': (
                            info.node
                            if 'node' in info.__dict__
                            else f'此类战斗({type(info)})不包含节点信息'
                        ),
                    },
                    'SL',
                )
                return None, ConditionFlag.SL
            return None, ConditionFlag.FIGHT_CONTINUE

        if state == 'spot_enemy_success':
            retreat = False
            can_detour = self.timer.image_exist(
                IMG.fight_image[13],
            )  # 判断该点是否可以迂回
            detour = can_detour and self.config.detour  # 由 Node 指定是否要迂回

            # 功能, 根据敌方阵容进行选择
            act = self._check_formation_rules(info.enemy_formation)
            if act == SearchEnemyAction.no_action:
                act = self._check_rules(enemies=enemies)

            if act == SearchEnemyAction.retreat:
                retreat = True
            elif act == SearchEnemyAction.detour:
                try:
                    assert can_detour, '该点无法迂回, 但是规则中指定了迂回'
                except AssertionError:
                    raise ValueError('该点无法迂回, 但在规则中指定了迂回')
                detour = True
            elif isinstance(act, Formation):
                self.set_formation_by_rule = True
                self.formation_by_rule = act

            if retreat:
                self.timer.click(677, 492, delay=0.2)
                info.fight_history.add_event(
                    '索敌成功',
                    {
                        'position': (
                            info.node
                            if 'node' in info.__dict__
                            else f'此类战斗({type(info)})不包含节点信息'
                        ),
                    },
                    '撤退',
                )
                return 'retreat', ConditionFlag.FIGHT_END
            if detour:
                image_detour = IMG.fight_image[13]
                if self.timer.click_image(image=image_detour, timeout=2.5):
                    self.timer.logger.info('成功执行迂回操作')
                else:
                    self.timer.logger.error('未找到迂回按钮')
                    self.timer.log_screen(True)
                    raise ImageNotFoundErr("can't found image")

                # self.timer.click(540, 500, delay=0.2)
                info.fight_history.add_event(
                    '索敌成功',
                    {
                        'position': (
                            info.node
                            if 'node' in info.__dict__
                            else f'此类战斗({type(info)})不包含节点信息'
                        ),
                    },
                    '迂回',
                )
                return 'detour', ConditionFlag.FIGHT_CONTINUE

            info.fight_history.add_event(
                '索敌成功',
                {
                    'position': (
                        info.node
                        if 'node' in info.__dict__
                        else f'此类战斗({type(info)})不包含节点信息'
                    ),
                },
                '战斗',
            )
            if self.config.long_missile_support:
                image_missile_support = IMG.fight_image[17]
                if self.timer.click_image(image=image_missile_support, timeout=2.5):
                    self.timer.logger.info('成功开启远程导弹支援')
                else:
                    self.timer.logger.error('未找到远程支援按钮')
                    raise ImageNotFoundErr("can't found image of long_missile_support")
            time.sleep(0.5)
            self.timer.click(855, 501, delay=0.2)  # 0.891 0.928
            # self.timer.click(380, 520, times=2, delay=0.2) # TODO: 跳过可能的开幕支援动画，实现有问题
            return 'fight', ConditionFlag.FIGHT_CONTINUE
        if state == 'formation':
            spot_enemy = last_state == 'spot_enemy_success'
            value = self.config.formation
            if spot_enemy:
                if self.config.SL_when_detour_fails and last_action == 'detour':
                    info.fight_history.add_event(
                        '迂回',
                        {
                            'position': (
                                info.node
                                if 'node' in info.__dict__
                                else f'此类战斗({type(info)})不包含节点信息'
                            ),
                        },
                        result='失败',
                    )
                    info.fight_history.add_event(
                        '阵型选择',
                        {
                            'enemies': enemies,
                            'position': (
                                info.node
                                if 'node' in info.__dict__
                                else f'此类战斗({type(info)})不包含节点信息'
                            ),
                        },
                        action='SL',
                    )
                    return None, ConditionFlag.SL

                if self.set_formation_by_rule:
                    self.logger.debug('set formation by rule:', self.formation_by_rule)
                    value = self.formation_by_rule
                    self.set_formation_by_rule = False
            else:
                if self.config.SL_when_spot_enemy_fails:
                    info.fight_history.add_event(
                        '阵型选择',
                        {
                            'enemies': '索敌失败',
                            'position': (
                                info.node
                                if 'node' in info.__dict__
                                else f'此类战斗({type(info)})不包含节点信息'
                            ),
                        },
                        action='SL',
                    )
                    return None, ConditionFlag.SL
                if self.config.formation_when_spot_enemy_fails:
                    value = self.config.formation_when_spot_enemy_fails
            info.fight_history.add_event(
                '阵型选择',
                {
                    'enemies': (enemies if last_state == 'spot_enemy_success' else '索敌失败'),
                    'position': (
                        info.node
                        if 'node' in info.__dict__
                        else f'此类战斗({type(info)})不包含节点信息'
                    ),
                },
                action=value,
            )
            self.timer.relative_click(*value.relative_position, delay=2)
            return value, ConditionFlag.FIGHT_CONTINUE
        if state == 'night':
            is_night = self.config.night
            info.fight_history.add_event(
                '是否夜战',
                {
                    'position': (
                        info.node
                        if 'node' in info.__dict__
                        else f'此类战斗({type(info)})不包含节点信息'
                    ),
                },
                action='追击' if is_night else '撤退',
            )

            match_night(self.timer, is_night)
            if is_night:
                # self.timer.click(325, 350)
                return 'yes', ConditionFlag.FIGHT_CONTINUE
            # self.timer.click(615, 350)
            return 'no', ConditionFlag.FIGHT_CONTINUE

        if state == 'result':
            # time.sleep(1.5)
            # self.timer.click(900, 500, times=2, delay=0.2)
            click_result(self.timer)
            return None, ConditionFlag.FIGHT_CONTINUE
        if state == 'get_ship':
            get_ship(self.timer)
            return None, ConditionFlag.FIGHT_CONTINUE
        self.logger.error('Unknown State')
        raise BaseException
