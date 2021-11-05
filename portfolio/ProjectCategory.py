from django.db import models

from treebeard.mp_tree import MP_Node


class ProjectCategory(MP_Node):
    name = models.CharField(max_length=30)

    node_order_by = ['name']

    def __str__(self):
        return 'Project Category: {}'.format(self.name)

    class Meta:
        verbose_name = "Project Category"
        verbose_name_plural = "Project Categories"