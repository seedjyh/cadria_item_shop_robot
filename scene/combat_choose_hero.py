#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2019/2/6
from pywindow import Position
from .scene import Scene, MatchRule


class Slot:
    def __init__(self, center):
        self._center = center

    def rules_for_idle(self):
        return [
            MatchRule(self._center, "18B27B")
        ]

    def center(self):
        return self._center


class CombatChooseHero(Scene):
    def __init__(self, window):
        Scene.__init__(self, window)
        self._append_rule(1220, 493, "98DFFF")
        self._append_rule(1220, 495, "161E23")
        self._append_rule(1220, 695, "52769C")
        self._append_rule(1220, 696, "A5D3F7")
        self._slots = [
            Slot(Position(355, 492)),
            Slot(Position(499, 492)),
            Slot(Position(643, 492)),
            Slot(Position(787, 492)),
        ]

    def banner_is_hidden(self):
        rules = [
            MatchRule(Position(1206, 107), "004BFF")
        ]
        return self.match_with_rules(rules)

    def show_banner(self):
        if not self.banner_is_hidden():
            return True
        for slot in self._slots:
            if self.match_with_rules(slot.rules_for_idle()):
                self._actor.left_click(slot.center())
                self._wait_after_action()
                return True
        return False

    def hide_banner(self):
        self._actor.left_click(Position(1000, 400))
        self._wait_after_action()

    def move_to_banner(self):
        self._window.move_to(Position(135, 125))

    def scroll_banner_most_left(self):
        self._window.scroll(vertical=-100)

    def scroll_right_one_step(self):
        self._window.scroll(vertical=1)
        self._wait_after_action()

    def select_free_heroes(self, required_count):
        """
        select heroes in banner, up to required_count
        :param required_count: max number of heroes required
        :return: count of heroes selected
        """
        selected_count = 0
        rules = [MatchRule(Position(24 + 147 * i, 209), "E7F3F7") for i in range(8)]
        for rule in rules:
            if selected_count >= required_count:
                break
            if self.match_with_rules([rule,]):
                self._actor.left_click(rule.position)
                self._wait_after_action()
                selected_count += 1
        return selected_count

    def required_heroes_count(self):
        count = 0
        for slot in self._slots:
            if self.match_with_rules(slot.rules_for_idle()):
                count = count + 1
        return count

    def go_combat(self):
        self._window.tap_letter("g")
        self._wait_after_action()

    def exit(self):
        self._window.tap_escape()
        self._wait_after_action()


if __name__ == "__main__":
    pass
