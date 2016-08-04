# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class SurveyStart (Page):
    form_model = models.Player
    form_fields = ['survey_response']

    def before_next_page(self):
        print('got to player response')
        print(self.player.survey_response)


class SurveyWaitPage (WaitPage):
    pass


class Part1 (Page):
    pass


class Video(Page):
    pass


class Part1Game(Page):
    print('got to part1')
    form_model = models.Player
    form_fields = ['task_reward']

    def before_next_page(self):
        print('got to before')
        self.player.final_reward = self.player.task_reward + models.Constants.endowment


class Part1Result(Page):
    pass


class Part1Wait(WaitPage):
    pass


class Part2 (Page):
    pass


class Roles (Page):
    def vars_for_template(self):
        return {
            'partner': self.player.get_partner()
        }


class TakeA(Page):

    form_model = models.Group
    form_fields = ['a_takes']

    def is_displayed(self):
        return self.player.id_in_group == 1

    def vars_for_template(self):
        return {
            'partner': self.player.get_partner()
        }


class TakeWaitPage(WaitPage):
    pass


class PredictB(Page):
    form_model = models.Group
    form_fields = ['b_predicts']

    def is_displayed(self):
        return self.player.id_in_group == 2

    def vars_for_template(self):
        return {
            'partner': self.player.get_partner()
        }


class WillingnessB(Page):
    def is_displayed(self):
        return self.player.id_in_group == 2

    form_model = models.Group
    form_fields = ['b_willing']

    def b_willing_max(self):
        return self.player.task_reward - self.player.task_reward * self.group.a_takes * .01

    def vars_for_template(self):
        return {
            'partner': self.player.get_partner(),
            'taken_amount': self.player.task_reward * self.group.a_takes * .01,
            'available_earnings': self.player.task_reward - self.player.task_reward * self.group.a_takes * .01
        }


class SendMessage(Page):
    form_model = models.Group
    form_fields = ['b_message']

    def is_displayed(self):
        return self.player.id_in_group == 2


class WaitForMessage(WaitPage):
    pass


class DisplayMessage(Page):
    def is_displayed(self):
        return self.player.id_in_group == 1


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


class SurveyEnd (Page):
    pass


class ThankYou (Page):
    pass


page_sequence = [
    SurveyStart,
    # SurveyWaitPage,
    # Part1,
    Video,
    Part1Game,
    Part1Result,
    Part1Wait,
    Part2,
    Roles,
    TakeA,
    TakeWaitPage,
    PredictB,
    WillingnessB,
    SendMessage,
    WaitForMessage,
    DisplayMessage,
    Results,
    SurveyEnd,
]
