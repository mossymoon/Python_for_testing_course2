from model.group import Group
from random import randrange


def test_modify_group(app, db, check_ui):
    group = Group(name="test222")
    if len(db.get_group_list()) == 0:
        app.contact.create_new_group(Group(name="test22"))
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    app.group.modify_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_contact_list()
    old_groups[index] = []
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(),
                                                                     key=Group.id_or_max)

