from app.objects.secondclass.c_goal import Goal
from app.objects.c_goals import Goals
from app.objects.secondclass.c_fact import Fact


class TestGoal:

    def test_satisfied(self):
        test_goal = Goal(target='target', value='value', count=1)
        assert test_goal.satisfied() is False
        assert test_goal.satisfied(all_facts=[Fact(trait='target', value='value')]) is True

    def test_multi_satisfied(self):
        test_goal = Goal(target='target', value='value', count=3)
        test_fact = Fact(trait='target', value='value')
        assert test_goal.satisfied(all_facts=[test_fact]) is False
        assert test_goal.satisfied(all_facts=[test_fact, test_fact, test_fact]) is True

    def test_operators(self):
        test_goal1 = Goal(target='target', value=2, count=1, operator='>')
        test_goal2 = Goal(target='target', value=2, count=1, operator='<=')
        test_goal3 = Goal(target='target', value='tes', count=1, operator='in')
        test_facta = Fact(trait='target', value=1)
        test_factb = Fact(trait='target', value=2)
        test_factc = Fact(trait='target', value='test')
        assert test_goal1.satisfied(all_facts=[test_facta]) is True
        assert test_goal2.satisfied(all_facts=[test_facta]) is False
        assert test_goal2.satisfied(all_facts=[test_facta, test_factb]) is True
        assert test_goal3.satisfied(all_facts=[test_factc]) is True

    def test_goals_satisfied(self):
        test_goal1 = Goal(target='target', value='value', count=1)
        test_goal2 = Goal(target='target2', value='value2', count=1)
        test_facta = Fact(trait='target', value='value')
        test_factb = Fact(trait='target2', value='value2')
        multi = Goals([test_goal1, test_goal2])
        assert multi.satisfied([test_facta]) is False
        assert multi.satisfied([test_facta, test_factb]) is True

    def test_goals_percent(self):
        test_goal1 = Goal(target='target', value='value', count=1)
        test_goal2 = Goal(target='target2', value='value2', count=1)
        test_fact = Fact(trait='target', value='value')
        multi = Goals([test_goal1, test_goal2])
        assert multi.satisfied([test_fact]) is False
        assert multi.percentage == 50
