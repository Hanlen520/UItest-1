# -*- coding: utf-8 -*-
"""预览页面的theme测试用例."""
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from Android_old import script_ultils as sc


class TestPreviewTheme(object):
    """预览页面的theme测试类."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_theme_ui(self):
        """预览页-切换到主题页面."""
        sc.logger.info('预览页-切换到主题页面')
        start_x = self.width // 2
        start_bottom = self.height // 3
        fun_name = 'test_theme_ui'

        sc.logger.info('点击创作中心主按钮')
        c_btn = 'com.quvideo.xiaoying:id/img_creation'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(c_btn)).click()

        sc.logger.info('点击“剪辑”')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/icon1').click()

        click_mask = 'com.quvideo.xiaoying:id/img_click_mask'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(click_mask)).click()

        sc.logger.info('点击“添加”')
        import_btn = 'com.quvideo.xiaoying:id/imgbtn_import'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(import_btn)).click()

        try:
            WebDriverWait(sc.driver, 60).until(
                lambda el: el.find_element_by_android_uiautomator(
                    'text("下一步")')).click()
        except TimeoutError as t:
            sc.logger.error('导入视频超时', t)
            return False
        except Exception as e:
            sc.logger.error('导入视频出错', e)
            return False

        time.sleep(1)
        sc.driver.swipe(start_x, start_bottom, start_x, start_bottom, 1000)

        sc.logger.info('点击“主题”按钮')
        WebDriverWait(sc.driver, 60).until(
            lambda el: el.find_element_by_android_uiautomator(
                'text("主题")')).click()
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('预览页-切换到主题页面')

    def test_theme_download(self):
        """预览页-主题下载."""
        sc.logger.info('预览页-主题下载')
        fun_name = 'test_theme_download'
        start_x = self.width // 4
        start_bottom = self.height - self.height // 10
        start_y = self.height // 3

        time.sleep(1)
        sc.swipe_by_ratio(start_x, start_bottom, 'right', 0.5, 500)

        sc.logger.info('点击“下载更多”')
        thumb_bg = 'com.quvideo.xiaoying:id/imgview_get_more_thumbnail_bg'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(thumb_bg)).click()

        try:
            sc.logger.info('点击“使用”按钮')
            u_btn = 'com.quvideo.xiaoying:id/template_caption_grid_btn_update'
            WebDriverWait(sc.driver, 10, 1).until(
                lambda el: el.find_element_by_id(u_btn)).click()
            time.sleep(1)
            sc.driver.swipe(start_x, start_y, start_x, start_y, 1000)
        except TimeoutException:
            sc.logger.info('点击下载按钮')
            sc.capture_screen(fun_name, self.img_path)
            down_btn = 'com.quvideo.xiaoying:id/imgbtn_download'
            WebDriverWait(sc.driver, 10, 1).until(
                lambda el: el.find_element_by_id(down_btn)).click()

            try:
                WebDriverWait(sc.driver, 30).until(
                    lambda el: el.find_element_by_android_uiautomator(
                        'text("使用")')).click()
                time.sleep(1)
                sc.driver.swipe(start_x, start_y, start_x, start_y, 1000)
            except TimeoutError as t:
                sc.logger.error('素材下载超时', t)
                sc.logger.info('返回创作中心主界面')
                for i in range(4):
                    time.sleep(1)
                    sc.driver.press_keycode(4)
                return False
            except Exception as e:
                sc.logger.info('返回创作中心主界面')
                for i in range(4):
                    time.sleep(1)
                    sc.driver.press_keycode(4)
                sc.logger.error('素材下载失败', e)
                return False

        sc.logger.info('返回创作中心主界面')
        for i in range(3):
            time.sleep(1)
            sc.driver.press_keycode(4)
        sc.logger.info('预览页-主题测试完成')
