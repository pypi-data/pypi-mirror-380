import time

from autowsgr.constants.custom_exceptions import ImageNotFoundErr, ShipNotFoundErr
from autowsgr.constants.image_templates import IMG, MyTemplate
from autowsgr.constants.positions import BLOOD_BAR_POSITION
from autowsgr.game.get_game_info import check_support_stats, detect_ship_stats
from autowsgr.timer import Timer
from autowsgr.types import DestroyShipWorkMode, RepairMode, ShipType
from autowsgr.utils.api_image import absolute_to_relative, crop_image


def get_ship(timer: Timer):
    """获取掉落舰船"""

    def recognize_get_ship(timer: Timer):
        """识别获取 舰船/装备 页面斜着的文字，对原始图片进行旋转裁切"""
        NAME_POSITION = [(0.754, 0.268), (0.983, 0.009), 25]
        ship_name_recognize_result = timer.recognize(
            crop_image(timer.screen, *NAME_POSITION),
            candidates=timer.ship_names,
        )
        assert ship_name_recognize_result is not None
        ship_name = ship_name_recognize_result[1]

        TYPE_POSITION = [(0.79, 0.29), (0.95, 0.1), 25]
        ship_type_recognize_result = timer.recognize(crop_image(timer.screen, *TYPE_POSITION))
        # 因为 allow_nan 为 False, 所以肯定不是 None
        assert ship_type_recognize_result is not None
        ship_type = ship_type_recognize_result[1]

        return ship_name, ship_type

    ship_name = None
    ship_type = None
    timer.got_ship_num += 1
    if timer.port.ship_factory.capacity is not None:
        timer.logger.info(
            f'当前船坞容量 {timer.port.ship_factory.occupation}/{timer.port.ship_factory.capacity}',
        )
        timer.port.ship_factory.occupation += 1
    symbol_images: list[MyTemplate] = [IMG.symbol_image[8], IMG.symbol_image[13]]
    while timer.wait_image(symbol_images, timeout=1):
        try:
            ship_name, ship_type = recognize_get_ship(timer)
            timer.logger.info(f'获取舰船: {ship_name} {ship_type}')
        except Exception as e:
            timer.logger.warning(f'识别获取舰船内容失败: {e}')
        timer.click(915, 515, delay=0.5, times=1)
        timer.confirm_operation()
    return ship_name, ship_type


def match_night(timer: Timer, is_night):
    """匹配夜战按钮并点击"""
    timer.wait_image(IMG.fight_image[6])
    while timer.wait_image(IMG.fight_image[6], timeout=0.5):
        if is_night:
            timer.click(325, 350, delay=0.5, times=1)
        else:
            timer.click(615, 350, delay=0.5, times=1)


def click_result(timer: Timer, max_times=1):
    """点击加速两页战果界面"""
    timer.wait_images(IMG.fight_image[14])
    looted = False
    while timer.wait_image(IMG.fight_image[14], timeout=0.5):
        if timer.can_get_loot and not looted:
            if timer.image_exist(IMG.fight_result['LOOT'], need_screen_shot=True):
                timer.got_loot_num += 1
                timer.logger.info(f'捞到胖次! 当前胖次数:{timer.got_loot_num}')
                looted = True
            else:
                timer.logger.debug('没有识别到胖次')
        timer.click(915, 515, delay=0.25, times=1)


def destroy_ship(timer: Timer, ship_types: list[ShipType] | None = None):
    """解装舰船，目前仅支持：全部解装+保留装备
    Args:
        timer (Timer): _description_
        ship_types (list[ShipType], optional): Override Config 里面的解装舰船类型. Defaults to None. 若为 None 则使用 Config 中的配置
    """

    timer.go_main_page()
    timer.goto_game_page('destroy_page')
    timer.set_page('destroy_page')

    timer.click(90, 206, delay=1.5)  # 点添加

    # 选择舰船类型
    if timer.config.destroy_ship_work_mode is not DestroyShipWorkMode.disable:
        destroy_types = ship_types if ship_types is not None else timer.config.destroy_ship_types

        if timer.config.destroy_ship_work_mode is DestroyShipWorkMode.exclude:
            intended_destroy_types: list[ShipType] = [
                x for x in ShipType.enum() if x not in destroy_types
            ]
        elif timer.config.destroy_ship_work_mode is DestroyShipWorkMode.include:
            intended_destroy_types = destroy_types
        else:
            raise ValueError('不支持的解装模式')

        if intended_destroy_types is not None:
            timer.relative_click(0.912, 0.681)
            for ship_type in intended_destroy_types:
                timer.relative_click(*ship_type.relative_position_in_destroy, times=1, delay=0.8)
            timer.relative_click(0.9, 0.85, delay=1.5)

    timer.relative_click(0.91, 0.3, delay=1.5)  # 快速选择
    timer.relative_click(0.915, 0.906, delay=1.5)  # 确定
    timer.relative_click(0.837, 0.646, delay=1.5)  # 卸下装备
    timer.relative_click(0.9, 0.9, delay=1.5)  # 解装
    timer.relative_click(0.38, 0.567, delay=1.5)  # 四星确认

    # 识别船坞容量
    timer.click(90, 206, delay=1.5)  # 点添加
    # occupation, capacity = (crop_rectangle_relative(timer.get_screen(), 0.873, 0.035, 0.102, 0.038))
    # timer.port.ship_factory.update_capacity(capacity, occupation)
    # timer.logger.info(f"舰船容量: {occupation}/{capacity}")
    timer.go_main_page()


def verify_team(timer: Timer):
    """检验目前是哪一个队伍(1~4)
    含网络状况处理
    Args:
        timer (Timer): _description_

    Raises:
        ImageNotFoundErr: 未找到队伍标志
        ImageNotFoundErr: 不在相关界面

    Returns:
        int: 队伍编号(1~4)
    """
    if not timer.identify_page('fight_prepare_page'):
        raise ImageNotFoundErr('not on fight_prepare_page')

    for _ in range(5):
        for i, position in enumerate([(64, 83), (186, 83), (310, 83), (430, 83)]):
            if timer.check_pixel(position, bgr_color=(228, 132, 16)):
                return i + 1
        time.sleep(0.2)
        timer.update_screen()

    if timer.process_bad_network():
        return verify_team(timer)

    timer.log_screen()
    raise ImageNotFoundErr


def move_team(timer: Timer, target, try_times=0):
    """切换队伍
    Args:
        timer (Timer): _description_
        target (_type_): 目标队伍
        try_times: 尝试次数
    Raise:
        ValueError: 切换失败
        ImageNotFoundErr: 不在相关界面
    """
    if try_times > 3:
        raise ValueError("can't change team")

    if not timer.identify_page('fight_prepare_page'):
        timer.log_screen()
        raise ImageNotFoundErr("not on 'fight_prepare_page' ")

    if verify_team(timer) == target:
        return
    timer.logger.info('正在切换队伍到:' + str(target))
    timer.click(110 * target, 81)
    if verify_team(timer) != target:
        move_team(timer, target, try_times + 1)


def set_support(timer: Timer, target, try_times=0):
    """启用战役支援
    Args:
        timer (Timer): _description_
        target (bool, int): 目标状态
    Raise:
        ValueError: 未能成功切换战役支援状态
    """
    target = bool(target)
    timer.goto_game_page('fight_prepare_page')

    if check_support_stats(timer) != target:
        timer.click(628, 82, delay=1)
        timer.click(760, 273, delay=1)
        timer.click(480, 270, delay=1)
        timer.logger.info('开启支援状态成功')

    if timer.is_bad_network(0) or check_support_stats(timer) != target:
        if timer.process_bad_network('set_support'):
            set_support(timer, target)
        else:
            raise ValueError("can't set right support")


def quick_repair(
    timer: Timer,
    repair_mode: int | RepairMode | list[RepairMode] = RepairMode.severe_damage,
    ship_stats=None,
    switch_back=False,
    *args,
    **kwargs,
):
    """战斗界面的快速修理
    Args:
        timer (Timer): _description_
        repair_mode: int
            1: 快修, 修中破
            2: 快修, 修大破
            3: 快修, 修复所有正在修理中的船
    """
    repair_mode_list: list[RepairMode] = []
    if isinstance(repair_mode, int) and repair_mode in [1, 2, 3]:
        repair_mode = RepairMode(repair_mode)
    try:
        if ship_stats is None:
            ship_stats = detect_ship_stats(timer)
        if not any(x in ship_stats for x in [0, 1, 2]):
            time.sleep(1)
            ship_stats = detect_ship_stats(timer)
        if not any(x in ship_stats for x in [0, 1, 2]):
            timer.logger.warning('执行修理操作时没有成功检测到舰船')
            raise ValueError('没有成功检测到舰船，请检查是否正确编队')

        if isinstance(repair_mode, RepairMode):
            repair_mode_list = [repair_mode for _ in range(6)]
        else:
            repair_mode_list = repair_mode
        assert len(repair_mode_list) == 6

        need_repair = [False for _ in range(6)]
        for i, x in enumerate(repair_mode_list):
            assert x in [RepairMode.moderate_damage, RepairMode.severe_damage, RepairMode.repairing]
            if x is RepairMode.moderate_damage:
                need_repair[i] = ship_stats[i + 1] in [1, 2, 3]
            elif x is RepairMode.severe_damage:
                need_repair[i] = ship_stats[i + 1] in [2, 3]
            # 好像修理中的是直接修, 无需通过这个逻辑
            # elif x is RepairMode.repairing:
            #     need_repair[i] = ship_stats[i + 1] in [3]
            else:
                need_repair[i] = False

        if timer.config.debug:
            timer.logger.debug('ship_stats:', ship_stats)
        if any(need_repair) or timer.image_exist(IMG.repair_image[1]):
            if timer.config.repair_manually:
                timer.logger.info('需要手动修理舰船')
                raise BaseException('需要手动修理舰船')
            timer.click(420, 420, times=2, delay=0.8)
            # 快修已经开始泡澡的船
            pos = timer.get_image_position(IMG.repair_image[1])
            while pos is not None:
                timer.port.bathroom.available_time = None
                timer.click(pos[0], pos[1], delay=1)
                pos = timer.get_image_position(IMG.repair_image[1])
            # 按逻辑修理
            for i in range(1, 7):
                if need_repair[i - 1]:
                    timer.logger.info('WorkInfo:' + str(kwargs))
                    timer.logger.info(str(i) + ' Repaired')
                    timer.quick_repaired_cost += 1
                    timer.click(
                        BLOOD_BAR_POSITION[0][i][0],
                        BLOOD_BAR_POSITION[0][i][1],
                        delay=1.5,
                    )
            if switch_back:
                timer.click(200, 420, times=2, delay=1.5)  # 返回正常切换页面
    except AssertionError:
        raise ValueError(f'修理舰船的参数不合法, 请检查你的参数:{repair_mode}')


def get_rewards(timer: Timer):
    """检查任务情况,如果可以领取奖励则领取"""
    timer.go_main_page()
    if not timer.check_pixel((694, 457), bgr_color=(45, 89, 255)):
        return 'no'
    timer.goto_game_page('mission_page')
    if timer.click_image(IMG.game_ui[15]):
        timer.relative_click(0.5, 0.5)
        timer.confirm_operation(must_confirm=True, timeout=5)
        return 'ok'
    if timer.click_image(IMG.game_ui[12]):
        timer.confirm_operation(must_confirm=True)
        return 'ok'
    return 'no'
    # timer.click(774, 502)


def repair_by_bath(timer: Timer):
    """使用浴室修理修理时间最长的单位
    Args:
        timer (Timer): _description_
    """
    timer.goto_game_page('choose_repair_page')
    timer.click(115, 233)
    if not timer.identify_page('choose_repair_page'):
        if timer.identify_page('bath_page'):
            timer.set_page('bath_page')
        else:
            timer.set_page()


def set_auto_supply(timer: Timer, type=1):
    """设置自动补给
    Args:
        timer (Timer): _description_
        type (int, optional): 1: 自动补给, 0: 不自动补给. Defaults to 1.
    """
    timer.update_screen()
    NowType = int(timer.check_pixel((48, 508), (224, 135, 35)))
    if NowType != type:
        timer.click(44, 503, delay=0.33)


def supply(timer: Timer, ship_ids=None, try_times=0):
    """补给指定舰船

    Args:
        timer (Timer): _description_
        ship_ids (list, optional): 补给舰船列表, 可以为单个整数表示单艘舰船. Defaults to [1, 2, 3, 4, 5, 6].

    Raises:
        ValueError: 补给失败
        TypeError: ship_ids 参数有误
    """
    if ship_ids is None:
        ship_ids = [1, 2, 3, 4, 5, 6]
    if try_times > 3:
        raise ValueError("can't supply ship")

    if isinstance(ship_ids, int):
        ship_ids = [ship_ids]

    timer.click(293, 420)
    for x in ship_ids:
        if not isinstance(x, int):
            raise TypeError('ship must be represent as a int but get' + str(ship_ids))
        timer.click(110 * x, 241)

    if timer.is_bad_network(0):
        timer.process_bad_network('supply ships')
        supply(timer, ship_ids, try_times + 1)


def change_ship(
    timer: Timer,
    fleet_id,
    ship_id: int,
    name=None,
    pre=None,
    ship_stats=None,
):
    """切换舰船(不支持第一舰队)"""
    if fleet_id is not None and not timer.identify_page('fight_prepare_page'):
        timer.goto_game_page('fight_prepare_page')
        move_team(timer, fleet_id)
        if fleet_id >= 5:
            # 切换为预设编队
            # 暂不支持
            return

    # 切换单船
    if ship_stats is None:
        ship_stats = detect_ship_stats(timer)
    if name is None and ship_stats[ship_id] == -1:
        return
    timer.click(110 * ship_id, 250, delay=0)
    res = timer.wait_images(
        [IMG.choose_ship_image[1], IMG.choose_ship_image[2]],
        after_get_delay=0.4,
        gap=0,
    )
    if res == 1:
        timer.click(839, 113)

    if name is None:
        timer.click(83, 167, delay=0)
        timer.wait_pages('fight_prepare_page', gap=0)
        return

    timer.click(700, 30, delay=0)
    # 等待输入框出现
    start_time = time.time()
    while not timer.check_pixel((955, 500), (255, 255, 255), screen_shot=True):
        time.sleep(0.2)
        if time.time() - start_time > 10:
            timer.log_screen(True)
            raise TimeoutError('等待输入框出现时超时')
    timer.logger.debug('输入框已经出现')
    # 输入名字检索
    timer.text(name)
    # 输入后随便点击获得检索结果
    timer.click(50, 50, delay=0.5)
    time.sleep(0.5)
    # OCR识别舰船
    if name not in timer.ship_names:
        timer.ship_names.append(name)
    ship_info = timer.recognize_ship(timer.get_screen()[:, :1048], timer.ship_names)

    # 查找识别结果中要选的舰船
    found_ship = next((ship for ship in ship_info if ship[1] == name), None)
    # 点击舰船
    if found_ship is None:
        timer.logger.error(f"Can't find ship {name}, ocr result:{ship_info}")
        if len(ship_info) == 0:
            timer.logger.warning('无法查找到任何舰船, 请检查舰船名是否有错误')
            raise ShipNotFoundErr
        timer.logger.debug('Try to click the first ship')
        if ship_stats[ship_id] == -1:
            timer.click(83, 167, delay=0)
        else:
            timer.click(183, 167, delay=0)
    else:
        center = found_ship[0]
        rel_center = absolute_to_relative(center, timer.resolution)
        timer.relative_click(*rel_center)

    timer.wait_pages('fight_prepare_page', gap=0)


def change_ships(timer: Timer, fleet_id, ship_names):
    """更换编队舰船

    Args:
        fleet_id (int): 2~4,表示舰队编号

        ship_names (舰船名称列表):

    For example:
        change_ships(timer, 2, [None, "萤火虫", "伏尔塔", "吹雪", "明斯克", None, None])

    """
    timer.logger.info(f'Change Fleet {fleet_id} to {ship_names}')
    if fleet_id is not None and not timer.identify_page('fight_prepare_page'):
        timer.goto_game_page('fight_prepare_page')
        move_team(timer, fleet_id)
    if fleet_id == 1:
        raise ValueError('change member of fleet 1 is unsupported')
    ship_stats = detect_ship_stats(timer)
    for i in range(1, 7):
        if ship_stats[i] != -1:
            change_ship(timer, fleet_id, 1, None, ship_stats=ship_stats)
    ship_names = ship_names + [None] * 6
    for i in range(len(ship_names)):
        if ship_names[i] == '':
            ship_names[i] = None
    time.sleep(0.3)
    ship_stats = detect_ship_stats(timer)
    for i in range(1, 7):
        change_ship(timer, fleet_id, i, ship_names[i], ship_stats=ship_stats)


def get_new_things(timer: Timer, lock=0):
    pass


# 是否强制点击
def cook(timer: Timer, position: int, force_click=False):
    """食堂做菜
    Args:
        position (int): 第几个菜谱
        force_click (bool, optional): 当有菜正在生效时是否继续做菜. Defaults to False.
    """
    if position < 1 or position > 3:
        raise ValueError(f'不支持的菜谱编号:{position}')
    POSITION = [None, (318, 276), (420, 140), (556, 217)]
    timer.goto_game_page('canteen_page')
    timer.click(*POSITION[position])
    try:
        timer.click_image(IMG.restaurant_image.cook, timeout=7.5, must_click=True)
        if timer.image_exist(IMG.restaurant_image.have_cook):
            timer.logger.info('当前菜的效果正在生效')
            if force_click:
                timer.relative_click(0.414, 0.628)
                if timer.image_exist(IMG.restaurant_image.no_times):
                    timer.logger.info('今日用餐次数已经用尽')
                    timer.relative_click(0.788, 0.207)
                    return False
                timer.logger.info('做菜成功')
            else:
                timer.relative_click(0.65, 0.628)
                timer.logger.info('取消做菜')
                timer.relative_click(0.788, 0.207)
        return True

    except:
        timer.logger.warning(
            f'不支持的菜谱编号:{position}, 请检查该菜谱是否有效, 或者检查今日用餐次数是否已经用尽',
        )
        return False
