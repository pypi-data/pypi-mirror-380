import time

from autowsgr.fight.battle import BattlePlan
from autowsgr.fight.exercise import NormalExercisePlan
from autowsgr.fight.normal_fight import NormalFightPlan
from autowsgr.game.expedition import Expedition
from autowsgr.game.game_operation import get_rewards, repair_by_bath, set_support
from autowsgr.game.get_game_info import get_loot_and_ship, get_resources
from autowsgr.notification import miao_alert
from autowsgr.timer import Timer
from autowsgr.types import ConditionFlag


class DailyOperation:
    def __init__(self, timer: Timer, gap=300) -> None:
        self.timer = timer
        if timer.config.daily_automation is None:
            raise ValueError('未设置日常任务，请检查配置文件')
        self.config = timer.config.daily_automation
        self.gap = gap

        if self.config.auto_expedition:
            self.expedition_plan = Expedition(self.timer)

        if self.config.auto_battle:
            if not self.config.battle_type:
                raise ValueError('未设置战役类型，请检查配置文件')
            self.battle_plan = BattlePlan(
                self.timer,
                plan_path=self.config.battle_type,
            )
        if self.config.auto_exercise:
            self.exercise_plan = NormalExercisePlan(
                self.timer,
                plan_path='plan_1',
                fleet_id=self.config.exercise_fleet_id,
            )
            self.complete_time = None

        if self.config.auto_normal_fight:
            self.fight_plans: list[NormalFightPlan] = []
            self.fight_complete_times = []
            for plan in self.config.normal_fight_tasks if self.config.normal_fight_tasks else []:
                self.fight_plans.append(
                    NormalFightPlan(
                        self.timer,
                        plan_path=plan[0],
                        fleet_id=plan[1],
                    ),
                )
                self.fight_complete_times.append(
                    [0, plan[2], plan[0]],
                )  # 二元组， [已完成次数, 目标次数, 任务名称]

        self.start_time = self.last_time = time.time()

    def run(self):
        # 自动战役，直到超过次数
        if self.config.auto_battle:
            ret = ConditionFlag.OPERATION_SUCCESS
            cnt = 0
            while ret is not ConditionFlag.BATTLE_TIMES_EXCEED:
                ret = self.battle_plan.run()
                cnt += 1
                if cnt > 13:
                    self.timer.logger.warning('战役没能正常执行完毕, 请检查日志排查原因')
                    break

        # 自动开启战役支援
        if self.config.auto_set_support:
            set_support(self.timer, True)

        get_loot_and_ship(self.timer)  # 获取胖次掉落和船只掉落数据
        get_resources(self.timer)

        # 自动演习
        if self.config.auto_exercise:
            self.check_exercise()

        # 自动出征
        if self.config.auto_normal_fight:
            while self._has_unfinished() and self._ship_max() and self._loot_max():
                task_id = self._get_unfinished()

                plan = self.fight_plans[task_id]
                ret = plan.run()

                if ret == ConditionFlag.OPERATION_SUCCESS or ret == ConditionFlag.SL:
                    self.fight_complete_times[task_id][0] += 1
                elif ret == ConditionFlag.DOCK_FULL:
                    miao_alert.miao_alert(0, self.timer.logger)
                    break  # 不解装则结束出征

                if self.config.quick_repair_limit and self.timer.quick_repaired_cost >= int(
                    self.config.quick_repair_limit,
                ):
                    self.timer.logger.info(
                        f'快修消耗达到上限:{self.config.quick_repair_limit}，结束出征',
                    )
                    break

                if time.time() - self.last_time >= self.gap:
                    self._expedition()
                    self._gain_bonus()
                    if self.config.auto_exercise:
                        self.check_exercise()
                    self.last_time = time.time()

        # 自动远征
        while True:
            if self.config.auto_exercise:
                self.check_exercise()
            self._bath_repair()
            self._expedition()
            self._gain_bonus()
            time.sleep(self.gap)

    def _has_unfinished(self) -> bool:
        return any(times[0] < times[1] for times in self.fight_complete_times)

    def _get_unfinished_plan_description(self, i: int) -> str:
        plan_str = ''
        plan_str += f'正在执行的PLAN: {self.fight_complete_times[i][2]}, '
        plan_str += f'已出击次数/目标次数: {self.fight_complete_times[i][0]}/{self.fight_complete_times[i][1]}, '
        plan_str += f'消耗快修数量: {self.timer.quick_repaired_cost}, '
        plan_str += f'已掉落船数量: {self.timer.got_ship_num}'
        if self.timer.can_get_loot:
            plan_str += f', 已掉落胖次数量: {self.timer.got_loot_num}'
        return plan_str

    def _get_unfinished(self) -> int:
        for i, times in enumerate(self.fight_complete_times):
            if times[0] < times[1]:
                self.timer.logger.info(self._get_unfinished_plan_description(i))
                return i
        raise ValueError('没有未完成的任务')

    def _expedition(self) -> None:
        if self.config.auto_expedition:
            self.expedition_plan.run(True)

    def _gain_bonus(self) -> None:
        if self.config.auto_gain_bonus:
            get_rewards(self.timer)
            self.timer.go_main_page()

    def _bath_repair(self) -> None:
        if self.config.auto_bath_repair:
            repair_by_bath(self.timer)

    def _ship_max(self) -> bool:
        if not self.config.stop_max_ship:
            return True
        if self.timer.got_ship_num < 500:
            return True
        self.timer.logger.info('船只数量已达到上限，结束出征')
        return False

    def _loot_max(self) -> bool:
        if not self.config.stop_max_loot:
            return True
        if self.timer.got_loot_num < 50:
            return True
        self.timer.logger.info('胖次数量已达到上限，结束出征')
        return False

    def check_exercise(self) -> None:
        # 判断在哪个时间段
        now_time = time.localtime(time.time())
        hour = now_time.tm_hour
        if 0 <= hour < 12:
            self.new_time_period = '0:00-12:00'
        elif 12 <= hour < 18:
            self.new_time_period = '12:00-18:00'
        else:
            self.new_time_period = '18:00-23:59'

        if self.new_time_period != self.complete_time:
            self.timer.logger.info('即将执行演习任务')
            self.exercise_plan.run()
            self.complete_time = self.new_time_period
        else:
            self.timer.logger.debug('当前时间段演习已完成')
