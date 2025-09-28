from dataclasses import dataclass
from typing import TYPE_CHECKING, Dict, Optional

from typing_extensions import Self

from dbt.adapters.base.relation import Policy
from dbt.adapters.contracts.relation import ComponentName, RelationConfig
from dbt.adapters.relation_configs import RelationConfigBase
from odps.models.table import Table as MaxComputeTable

from ..utils import quote_ref
from ._policies import (
    ODPSIncludePolicy,
    ODPSQuotePolicy,
)

if TYPE_CHECKING:
    # Indirectly imported via agate_helper, which is lazy loaded further downfile.
    # Used by mypy for earlier type hints.
    import agate


@dataclass(frozen=True, eq=True, unsafe_hash=True)
class ODPSBaseRelationConfig(RelationConfigBase):
    @classmethod
    def include_policy(cls) -> Policy:
        return ODPSIncludePolicy()

    @classmethod
    def quote_policy(cls) -> Policy:
        return ODPSQuotePolicy()

    @classmethod
    def from_relation_config(cls, relation_config: RelationConfig) -> Self:
        relation_config_dict = cls.parse_relation_config(relation_config)
        relation = cls.from_dict(relation_config_dict)
        return relation

    @classmethod
    def parse_relation_config(cls, relation_config: RelationConfig) -> Dict:
        raise NotImplementedError(
            "`parse_model_node()` needs to be implemented on this RelationConfigBase instance"
        )

    @classmethod
    def from_mc_table(cls, table: MaxComputeTable) -> Self:
        relation_config = cls.parse_mc_table(table)
        relation = cls.from_dict(relation_config)
        return relation

    @classmethod
    def parse_mc_table(cls, table: MaxComputeTable) -> Dict:
        raise NotImplementedError(
            "`parse_mc_table()` is not implemented for this relation type"
        )

    @classmethod
    def _render_part(
        cls, component: ComponentName, value: Optional[str]
    ) -> Optional[str]:
        if cls.include_policy().get_part(component) and value:
            if cls.quote_policy().get_part(component):
                return quote_ref(value)
            return value.lower()
        return None

    @classmethod
    def _get_first_row(cls, results: "agate.Table") -> "agate.Row":
        try:
            return results.rows[0]
        except IndexError:
            import agate

            return agate.Row(values=set())
