import os

from autowsgr.constants.data_roots import MAP_ROOT
from autowsgr.fight.event.event import Event
from autowsgr.fight.normal_fight import NormalFightInfo, NormalFightPlan
from autowsgr.timer import Timer


NODE_POSITION = [
    None,
    (112, 180),
    (407, 275),
    (248, 111),
    (505, 136),
    (686, 209),
    (835, 305),
]


class EventFightPlan20230809(Event, NormalFightPlan):
    def __init__(self, timer: Timer, plan_path, fleet_id=None, event='20230809') -> None:
        """
        Args:
            fleet_id : 新的舰队参数, 如果为 None 则使用计划参数.
        """
        self.event_name = event
        NormalFightPlan.__init__(self, timer, plan_path, fleet_id=fleet_id)
        Event.__init__(self, timer, event)

    def _load_fight_info(self):
        self.info = EventFightInfo20230809(self.timer, self.chapter, self.map)
        self.info.load_point_positions(os.path.join(MAP_ROOT, 'event', self.event_name))

    def _change_fight_map(self, chapter_id, map_id):
        """选择并进入战斗地图(chapter-map)"""
        self.change_difficulty(chapter_id)

    def _go_fight_prepare_page(self) -> None:
        if not self.timer.image_exist(self.info.event_image[1], need_screen_shot=0):
            self.timer.click(*NODE_POSITION[self.map])
        self.timer.wait_image(self.event_image[1])
        self.timer.click(850, 490)
        self.timer.wait_pages('fight_prepare_page', after_wait=0.15)


class EventFightInfo20230809(Event, NormalFightInfo):
    def __init__(self, timer: Timer, chapter_id, map_id, event='20230809') -> None:
        NormalFightInfo.__init__(self, timer, chapter_id, map_id)
        Event.__init__(self, timer, event)
        self.map_image = (
            self.common_image['easy'] + self.common_image['hard'] + [self.event_image[1]]
        )
        self.end_page = 'unknown_page'
        self.state2image['map_page'] = [self.map_image, 5]
