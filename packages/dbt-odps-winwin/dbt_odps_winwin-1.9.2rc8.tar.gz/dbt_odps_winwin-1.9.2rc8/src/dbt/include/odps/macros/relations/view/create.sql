{% macro odps__create_view_as(relation, sql) -%}
  {%- set sql_hints = config.get('sql_hints', none) -%}
  {%- set sql_header = merge_sql_hints_and_header(sql_hints, config.get('sql_header', none)) -%}

  {{ sql_header if sql_header is not none }}
  create or replace view {{ relation.render() }}
    {% set contract_config = config.get('contract') %}
    {% if contract_config.enforced %}
      {{ get_assert_columns_equivalent(sql) }}
    {%- endif %}
  as (
    {{ sql }}
  );
{%- endmacro %}
