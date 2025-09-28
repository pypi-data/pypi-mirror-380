from .utils import dbt_odps_version

GLOBAL_SQL_HINTS = {
    "dbt.odps.version": dbt_odps_version(),
    "odps.sql.type.system.odps2": "true",
    "odps.sql.decimal.odps2": "true",
    "odps.sql.hive.compatible": "true",
    "odps.sql.allow.fullscan": "true",
    "odps.sql.select.output.format": "csv",
    "odps.sql.submit.mode": "script",
    "odps.sql.allow.cartesian": "true",
    "odps.sql.timezone": "Asia/Shanghai",
    "odps.sql.allow.schema.evolution": "true",
    "odps.sql.python.version": "cp37"
}
