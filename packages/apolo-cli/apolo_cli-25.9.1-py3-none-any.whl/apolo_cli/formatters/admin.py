import operator
from typing import Iterable, List, Mapping, Optional, Tuple

from rich import box
from rich.console import Group as RichGroup
from rich.console import RenderableType
from rich.rule import Rule
from rich.styled import Styled
from rich.table import Table

from apolo_sdk import (
    _Cluster,
    _ClusterUser,
    _ClusterUserWithInfo,
    _ConfigCluster,
    _Org,
    _OrgCluster,
    _OrgUserWithInfo,
    _Project,
    _ProjectUserWithInfo,
    _ResourcePoolType,
)

from apolo_cli.formatters.config import format_quota_details
from apolo_cli.formatters.utils import format_datetime_iso, format_multiple_gpus
from apolo_cli.utils import format_size


class ClusterUserWithInfoFormatter:
    def __call__(
        self, clusters_users: Iterable[_ClusterUserWithInfo]
    ) -> RenderableType:
        table = Table(box=box.MINIMAL_HEAVY_HEAD)
        table.add_column("Name", style="bold", max_width=None, no_wrap=True)
        table.add_column("Org")
        table.add_column("Role")
        table.add_column("Email")
        table.add_column("Full name")
        table.add_column("Registered")
        table.add_column("Max jobs", max_width=10, overflow="fold")
        rows = []

        for user in clusters_users:
            rows.append(
                (
                    user.user_name,
                    user.org_name or "",
                    user.role.value if user.role else "",
                    user.user_info.email,
                    user.user_info.full_name,
                    format_datetime_iso(user.user_info.created_at),
                    format_quota_details(user.quota.total_running_jobs),
                )
            )
        rows.sort(key=operator.itemgetter(0))

        for row in rows:
            table.add_row(*row)
        return table


class ClusterUserFormatter:
    def __call__(self, clusters_users: Iterable[_ClusterUser]) -> RenderableType:
        table = Table(box=box.MINIMAL_HEAVY_HEAD)
        table.add_column("Name", style="bold")
        table.add_column("Org")
        rows = []

        for user in clusters_users:
            rows.append((user.user_name, user.org_name or ""))
        rows.sort(key=operator.itemgetter(0))

        for row in rows:
            table.add_row(*row)
        return table


class OrgUserFormatter:
    def __call__(self, org_users: Iterable[_OrgUserWithInfo]) -> RenderableType:
        table = Table(box=box.MINIMAL_HEAVY_HEAD)
        table.add_column("Name", style="bold")
        table.add_column("Role")
        table.add_column("Email")
        table.add_column("Full name")
        table.add_column("Registered")
        table.add_column("Credits", max_width=10, overflow="fold")
        table.add_column("Spent credits", max_width=14, overflow="fold")
        rows = []

        for user in org_users:
            rows.append(
                (
                    user.user_name,
                    user.role.value,
                    user.user_info.email,
                    user.user_info.full_name,
                    format_datetime_iso(user.user_info.created_at),
                    format_quota_details(user.balance.credits),
                    format_quota_details(user.balance.spent_credits),
                )
            )
        rows.sort(key=operator.itemgetter(0))

        for row in rows:
            table.add_row(*row)
        return table


class OrgClustersFormatter:
    def __call__(self, org_clusters: Iterable[_OrgCluster]) -> RenderableType:
        table = Table(box=box.MINIMAL_HEAVY_HEAD)
        table.add_column("Org name", style="bold")
        table.add_column("Cluster name")
        table.add_column("Credits")
        table.add_column("Spent credits")
        table.add_column("Max jobs")
        table.add_column("Default credits")
        table.add_column("Default max jobs")
        table.add_column("Default role")
        rows = []

        for org_cluster in org_clusters:
            rows.append(
                (
                    org_cluster.org_name,
                    org_cluster.cluster_name,
                    format_quota_details(org_cluster.balance.credits),
                    format_quota_details(org_cluster.balance.spent_credits),
                    format_quota_details(org_cluster.quota.total_running_jobs),
                    format_quota_details(org_cluster.default_credits),
                    format_quota_details(org_cluster.default_quota.total_running_jobs),
                    org_cluster.default_role.value,
                )
            )
        rows.sort(key=operator.itemgetter(0))

        for row in rows:
            table.add_row(*row)
        return table


class OrgClusterFormatter:
    def __call__(
        self, org_cluster: _OrgCluster, *, skip_cluster_org: bool = False
    ) -> RenderableType:
        table = Table(box=None, show_header=False, show_edge=False)
        table.add_column()
        table.add_column(style="bold")
        if not skip_cluster_org:
            table.add_row("Org name", org_cluster.org_name)
            table.add_row("Cluster name", org_cluster.cluster_name)
        table.add_row("Credits", format_quota_details(org_cluster.balance.credits))
        table.add_row(
            "Spent credits", format_quota_details(org_cluster.balance.spent_credits)
        )
        table.add_row(
            "Max jobs", format_quota_details(org_cluster.quota.total_running_jobs)
        )
        table.add_row(
            "Default credits", format_quota_details(org_cluster.default_credits)
        )
        table.add_row(
            "Default max jobs",
            format_quota_details(org_cluster.default_quota.total_running_jobs),
        )
        table.add_row(
            "Default role",
            org_cluster.default_role.value,
        )
        return table


class ClustersFormatter:
    def __call__(
        self,
        clusters: Mapping[str, Tuple[Optional[_Cluster], Optional[_ConfigCluster]]],
    ) -> RenderableType:
        out: List[RenderableType] = []
        for cluster_name, (admin_cluster, config_cluster) in clusters.items():
            table = Table(
                title=cluster_name,
                title_justify="left",
                title_style="bold italic",
                box=None,
                show_header=False,
                show_edge=False,
                min_width=len(cluster_name),
            )
            table.add_column()
            table.add_column(style="bold")
            if (
                config_cluster
                and config_cluster.orchestrator
                and config_cluster.orchestrator.resource_pool_types
            ):
                table.add_row(
                    "Node pools",
                    Styled(
                        _format_node_pools(
                            config_cluster.orchestrator.resource_pool_types
                        ),
                        style="reset",
                    ),
                )
            if admin_cluster:
                if admin_cluster.default_credits:
                    table.add_row(
                        "Default credits",
                        format_quota_details(admin_cluster.default_credits),
                    )
                if admin_cluster.default_quota.total_running_jobs:
                    table.add_row(
                        "Default max jobs",
                        format_quota_details(
                            admin_cluster.default_quota.total_running_jobs
                        ),
                    )
                table.add_row("Default role", admin_cluster.default_role.value)
            out.append(table)
            out.append(Rule())
        return RichGroup(*out)


def _format_node_pools(node_pools: Iterable[_ResourcePoolType]) -> Table:
    is_scalable = _is_scalable(node_pools)
    has_preemptible = _has_preemptible(node_pools)
    has_idle = _has_idle(node_pools)

    table = Table(
        box=box.SIMPLE_HEAVY,
        show_edge=True,
    )
    table.add_column("Name", style="bold", justify="left", max_width=None, no_wrap=True)
    table.add_column("CPU", justify="right")
    table.add_column("Memory", justify="right")
    table.add_column("Disk", justify="right")
    if has_preemptible:
        table.add_column("Preemptible", justify="center")
    table.add_column("GPU", justify="right")
    if is_scalable:
        table.add_column("Min", justify="right")
        table.add_column("Max", justify="right")
    else:
        table.add_column("Size", justify="right")
    if has_idle:
        table.add_column("Idle", justify="right")

    for node_pool in node_pools:
        row = [node_pool.name]
        row.append(str(node_pool.available_cpu))
        row.append(format_size(node_pool.available_memory))
        row.append(format_size(node_pool.disk_size))
        if has_preemptible:
            row.append("√" if node_pool.is_preemptible else "×")
        row.append(format_multiple_gpus(node_pool))
        if is_scalable:
            row.append(str(node_pool.min_size))
        row.append(str(node_pool.max_size))
        if has_idle:
            row.append(str(node_pool.idle_size or 0))
        table.add_row(*row)

    return table


def _is_scalable(node_pools: Iterable[_ResourcePoolType]) -> bool:
    for node_pool in node_pools:
        if node_pool.min_size != node_pool.max_size:
            return True
    return False


def _has_preemptible(node_pools: Iterable[_ResourcePoolType]) -> bool:
    for node_pool in node_pools:
        if node_pool.is_preemptible:
            return True
    return False


def _has_idle(node_pools: Iterable[_ResourcePoolType]) -> bool:
    for node_pool in node_pools:
        if node_pool.idle_size:
            return True
    return False


class OrgFormatter:
    def __call__(self, org: _Org) -> RenderableType:
        table = Table(box=None, show_header=False, show_edge=False)
        table.add_column()
        table.add_column(style="bold")
        table.add_row("Name", org.name)
        table.add_row("Credits", format_quota_details(org.balance.credits))
        table.add_row("Spent credits", format_quota_details(org.balance.spent_credits))
        table.add_row(
            "User default credits", format_quota_details(org.user_default_credits)
        )
        return table


class OrgsFormatter:
    def __call__(self, orgs: Iterable[_Org]) -> RenderableType:
        table = Table(box=box.SIMPLE_HEAVY)
        table.add_column("Name")
        for org in orgs:
            table.add_row(org.name)
        return table


class ProjectsFormatter:
    def __call__(self, projects: Iterable[_Project]) -> RenderableType:
        table = Table(box=box.SIMPLE_HEAVY)
        table.add_column("Project name", style="bold")
        table.add_column("Cluster name")
        table.add_column("Org name")
        table.add_column("Default role")
        table.add_column("Is default project")
        rows = []

        for project in projects:
            rows.append(
                (
                    project.name,
                    project.cluster_name,
                    project.org_name,
                    project.default_role.value,
                    str(project.is_default),
                )
            )
        rows.sort(key=operator.itemgetter(0))

        for row in rows:
            table.add_row(*row)
        return table


class ProjectFormatter:
    def __call__(
        self, project: _Project, *, skip_cluster_org: bool = False
    ) -> RenderableType:
        table = Table(box=None, show_header=False, show_edge=False)
        table.add_column()
        table.add_column(style="bold")
        table.add_row("Name", project.name)
        if not skip_cluster_org:
            table.add_row("Cluster name", project.cluster_name)
            table.add_row("Org name", project.org_name)
        table.add_row(
            "Default role",
            project.default_role.value,
        )
        table.add_row(
            "Is default project",
            str(project.is_default),
        )
        return table


class ProjectUserFormatter:
    def __call__(self, project_users: Iterable[_ProjectUserWithInfo]) -> RenderableType:
        table = Table(box=box.MINIMAL_HEAVY_HEAD)
        table.add_column("Name", style="bold")
        table.add_column("Role")
        table.add_column("Email")
        table.add_column("Full name")
        table.add_column("Registered")
        rows = []

        for user in project_users:
            rows.append(
                (
                    user.user_name,
                    user.role.value,
                    user.user_info.email,
                    user.user_info.full_name,
                    format_datetime_iso(user.user_info.created_at),
                )
            )
        rows.sort(key=operator.itemgetter(0))

        for row in rows:
            table.add_row(*row)
        return table
