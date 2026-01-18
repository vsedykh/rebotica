import pyautogui
import time
import keyboard
from PIL import ImageGrab
import cv2
import numpy as np
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('ksp_docking.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


class KSPDockingAutopilot:
    def __init__(self):
        self.screen_width, self.screen_height = pyautogui.size()
        self.docking_ui_regions = self.detect_ui_regions()
        self.is_running = False

        # Настройки чувствительности
        self.rotation_threshold = 0.1
        self.translation_threshold = 0.5
        self.max_speed = 2.0  # м/с
        self.approach_speed = 1.0  # м/с
        self.final_approach_speed = 0.2  # м/с

        logger.info("Инициализация автопилота стыковки KSP")

    def detect_ui_regions(self):
        regions = {
            'navball': (self.screen_width // 2 - 100, self.screen_height - 200, 200, 200),
            'speed_indicator': (self.screen_width - 200, self.screen_height // 2 - 100, 150, 200),
            'target_marker': (self.screen_width // 2 - 25, self.screen_height // 2 - 25, 50, 50),
            'docking_port': (self.screen_width // 2 - 10, self.screen_height // 2 - 10, 20, 20)
        }
        return regions

    def take_screenshot(self, region=None):
        if region:
            screenshot = ImageGrab.grab(bbox=region)
        else:
            screenshot = ImageGrab.grab()
        return cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    def find_docking_port(self):
        try:
            region = (
                self.screen_width // 2 - 100,
                self.screen_height // 2 - 100,
                self.screen_width // 2 + 100,
                self.screen_height // 2 + 100
            )
            screenshot = self.take_screenshot(region)

            hsv = cv2.cvtColor(screenshot, cv2.COLOR_BGR2HSV)
            lower_white = np.array([0, 0, 200])
            upper_white = np.array([180, 50, 255])

            mask = cv2.inRange(hsv, lower_white, upper_white)
            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            if contours:
                # Находим самый большой контур
                largest_contour = max(contours, key=cv2.contourArea)
                x, y, w, h = cv2.boundingRect(largest_contour)

                # Центр стыковочного порта
                port_x = region[0] + x + w // 2
                port_y = region[1] + y + h // 2

                logger.info(f"Стыковочный порт найден в позиции: ({port_x}, {port_y})")
                return (port_x, port_y)

            return None

        except Exception as e:
            logger.error(f"Ошибка при поиске стыковочного порта: {e}")
            return None

    def get_navball_orientation(self):
        """Анализ ориентации по навболу (упрощенная версия)"""
        try:
            navball_region = self.docking_ui_regions['navball']
            screenshot = self.take_screenshot(navball_region)

            # Простой анализ цвета для определения ориентации
            # В реальной реализации нужна более сложная компьютерное зрение
            center_x, center_y = navball_region[2] // 2, navball_region[3] // 2

            # Здесь должна быть сложная логика анализа навбола
            # Возвращаем фиктивные значения для демонстрации
            return {'pitch': 0, 'yaw': 0, 'roll': 0}

        except Exception as e:
            logger.error(f"Ошибка анализа навбола: {e}")
            return {'pitch': 0, 'yaw': 0, 'roll': 0}

    def set_sas_mode(self, mode='target'):
        """Установка режима SAS"""
        try:
            # Нажатие T для включения SAS
            pyautogui.press('t')
            time.sleep(0.5)

            if mode == 'target':
                # Установка SAS на удержание ориентации на цель
                pyautogui.press('f')
            elif mode == 'stability':
                # Режим стабилизации
                pyautogui.press('f')

            logger.info(f"SAS установлен в режим: {mode}")
            time.sleep(1)

        except Exception as e:
            logger.error(f"Ошибка установки SAS: {e}")

    def set_rcs_mode(self, enabled=True):
        """Включение/выключение RCS"""
        try:
            pyautogui.press('r')
            logger.info(f"RCS {'включен' if enabled else 'выключен'}")
            time.sleep(0.5)
        except Exception as e:
            logger.error(f"Ошибка переключения RCS: {e}")

    def control_rotation(self, target_orientation):
        """Управление вращением корабля"""
        try:
            current_orientation = self.get_navball_orientation()

            # Вычисление ошибки ориентации
            pitch_error = target_orientation['pitch'] - current_orientation['pitch']
            yaw_error = target_orientation['yaw'] - current_orientation['yaw']
            roll_error = target_orientation['roll'] - current_orientation['roll']

            # Управление с пороговым значением
            if abs(pitch_error) > self.rotation_threshold:
                if pitch_error > 0:
                    pyautogui.keyDown('s')  # Нос вниз
                else:
                    pyautogui.keyDown('w')  # Нос вверх
                time.sleep(0.1)
                pyautogui.keyUp('w')
                pyautogui.keyUp('s')

            if abs(yaw_error) > self.rotation_threshold:
                if yaw_error > 0:
                    pyautogui.keyDown('a')  # Влево
                else:
                    pyautogui.keyDown('d')  # Вправо
                time.sleep(0.1)
                pyautogui.keyUp('a')
                pyautogui.keyUp('d')

            if abs(roll_error) > self.rotation_threshold:
                if roll_error > 0:
                    pyautogui.keyDown('q')  # Крен влево
                else:
                    pyautogui.keyDown('e')  # Крен вправо
                time.sleep(0.1)
                pyautogui.keyUp('q')
                pyautogui.keyUp('e')

        except Exception as e:
            logger.error(f"Ошибка управления вращением: {e}")

    def control_translation(self, direction, duration=0.1):
        """Управление поступательным движением"""
        try:
            translation_keys = {
                'forward': 'h',
                'backward': 'n',
                'left': 'j',
                'right': 'l',
                'up': 'i',
                'down': 'k'
            }

            if direction in translation_keys:
                pyautogui.keyDown(translation_keys[direction])
                time.sleep(duration)
                pyautogui.keyUp(translation_keys[direction])
                logger.debug(f"Движение: {direction}, длительность: {duration}")

        except Exception as e:
            logger.error(f"Ошибка управления движением: {e}")

    def align_with_target(self):
        """Выравнивание с целью"""
        logger.info("Начало выравнивания с целью")

        # Включение необходимых систем
        self.set_sas_mode('target')
        self.set_rcs_mode(True)

        # Выравнивание по курсу
        for _ in range(50):  # Ограничение итераций
            self.control_rotation({'pitch': 0, 'yaw': 0, 'roll': 0})
            time.sleep(0.1)

        logger.info("Выравнивание завершено")

    def approach_target(self, final_distance=5.0):
        """Сближение с целью"""
        logger.info("Начало сближения с целью")

        distance = 1700000

        while distance > final_distance:
            try:
                # Поиск стыковочного порта
                port_position = self.find_docking_port()

                if port_position:
                    screen_center_x = self.screen_width // 2
                    screen_center_y = self.screen_height // 2

                    # Вычисление смещения от центра
                    dx = port_position[0] - screen_center_x
                    dy = port_position[1] - screen_center_y

                    # Коррекция положения
                    if abs(dx) > 10:
                        if dx > 0:
                            self.control_translation('right', 0.05)
                        else:
                            self.control_translation('left', 0.05)

                    if abs(dy) > 10:
                        if dy > 0:
                            self.control_translation('down', 0.05)
                        else:
                            self.control_translation('up', 0.05)

                    # Определение скорости сближения
                    if distance > 20:
                        current_speed = self.approach_speed
                    else:
                        current_speed = self.final_approach_speed

                    # Движение вперед
                    self.control_translation('forward', 0.1)

                    # Уменьшение расстояния (имитация)
                    distance -= current_speed
                    logger.info(f"Расстояние до цели: {distance:.1f} м")

                time.sleep(0.5)

            except Exception as e:
                logger.error(f"Ошибка при сближении: {e}")
                break

        logger.info("Сближение завершено")

    def final_docking_sequence(self):
        """Финальная последовательность стыковки"""
        logger.info("Запуск финальной последовательности стыковки")

        try:
            # Точное выравнивание
            for _ in range(20):
                port_position = self.find_docking_port()
                if port_position:
                    screen_center_x = self.screen_width // 2
                    screen_center_y = self.screen_height // 2

                    dx = port_position[0] - screen_center_x
                    dy = port_position[1] - screen_center_y

                    # Мелкие корректировки
                    if abs(dx) > 2:
                        self.control_translation('right' if dx > 0 else 'left', 0.02)
                    if abs(dy) > 2:
                        self.control_translation('down' if dy > 0 else 'up', 0.02)

                # Очень медленное движение вперед
                self.control_translation('forward', 0.05)
                time.sleep(0.2)

            # Завершающее движение
            for _ in range(10):
                self.control_translation('forward', 0.1)
                time.sleep(0.3)

            logger.info("✅ Стыковка завершена!")

        except Exception as e:
            logger.error(f"Ошибка в финальной последовательности: {e}")

    def emergency_stop(self):
        """Аварийная остановка"""
        logger.warning("АВАРИЙНАЯ ОСТАНОВКА!")

        try:
            # Быстрая остановка движения назад
            self.control_translation('backward', 1.0)

            # Выключение RCS
            self.set_rcs_mode(False)

            # Стабилизация
            self.set_sas_mode('stability')

            logger.info("Аварийная остановка выполнена")

        except Exception as e:
            logger.error(f"Ошибка при аварийной остановке: {e}")

    def run_docking_sequence(self):
        """Запуск полной последовательности стыковки"""
        if self.is_running:
            logger.warning("Автопилот уже запущен")
            return

        self.is_running = True
        logger.info("🚀 ЗАПУСК АВТОПИЛОТА СТЫКОВКИ KSP")

        try:
            # Этап 1: Подготовка систем
            logger.info("Этап 1: Подготовка систем")
            time.sleep(2)

            # Этап 2: Выравнивание с целью
            logger.info("Этап 2: Выравнивание с целью")
            self.align_with_target()
            time.sleep(1)

            # Этап 3: Сближение
            logger.info("Этап 3: Сближение")
            self.approach_target(final_distance=10.0)
            time.sleep(1)

            # Этап 4: Финальная стыковка
            logger.info("Этап 4: Финальная стыковка")
            self.final_docking_sequence()

            logger.info("🎉 СТЫКОВКА УСПЕШНО ЗАВЕРШЕНА!")

        except KeyboardInterrupt:
            logger.info("Стыковка прервана пользователем")
            self.emergency_stop()
        except Exception as e:
            logger.error(f"Критическая ошибка автопилота: {e}")
            self.emergency_stop()
        finally:
            self.is_running = False

    def start_monitoring(self):
        """Запуск мониторинга горячих клавиш"""
        logger.info("Запуск мониторинга горячих клавиш")

        def start_docking():
            if not self.is_running:
                import threading
                thread = threading.Thread(target=self.run_docking_sequence)
                thread.daemon = True
                thread.start()

        def emergency_stop():
            if self.is_running:
                self.emergency_stop()
                self.is_running = False

        # Регистрация горячих клавиш
        keyboard.add_hotkey('f10', start_docking)
        keyboard.add_hotkey('f12', emergency_stop)

        print("\n" + "=" * 50)
        print("АВТОПИЛОТ СТЫКОВКИ KSP")
        print("=" * 50)
        print("Горячие клавиши:")
        print("F10 - Запуск автопилота стыковки")
        print("F12 - Аварийная остановка")
        print("Ctrl+C - Выход из программы")
        print("=" * 50)

        try:
            keyboard.wait()  # Ожидание горячих клавиш
        except KeyboardInterrupt:
            logger.info("Программа завершена пользователем")


def main():
    """Главная функция"""
    try:
        # Проверка наличия необходимых модулей
        try:
            import pyautogui
            import keyboard
            import cv2
            import numpy as np
        except ImportError as e:
            print(f"❌ Отсутствуют необходимые модули: {e}")
            print("Установите их: pip install pyautogui keyboard opencv-python pillow")
            return

        # Инициализация автопилота
        autopilot = KSPDockingAutopilot()

        # Запуск мониторинга
        autopilot.start_monitoring()

    except Exception as e:
        logger.critical(f"Критическая ошибка: {e}")
        print("❌ Программа завершена с ошибкой")


if __name__ == "__main__":
    main()