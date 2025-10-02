from gitlabform.gitlab import GitLab
from gitlabform.processors.defining_keys import Key, And
from gitlabform.processors.multiple_entities_processor import MultipleEntitiesProcessor


class GroupVariablesProcessor(MultipleEntitiesProcessor):
    def __init__(self, gitlab: GitLab):
        super().__init__(
            "group_variables",
            gitlab,
            list_method_name="get_group_variables",
            add_method_name="post_group_variable",
            delete_method_name="delete_group_variable",
            defining=Key("key"),
            required_to_create_or_update=And(Key("key"), Key("value")),
            edit_method_name="put_group_variable",
        )
