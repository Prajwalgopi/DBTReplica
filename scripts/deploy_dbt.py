import snowflake.connector

conn = snowflake.connector.connect(
    account="${SNOWFLAKE_ACCOUNT}",
    user="${SNOWFLAKE_USER}",
    password="${SNOWFLAKE_PASSWORD}",
    role="DBT_DEV_ROLE",
    warehouse="DBT_WH"
)

cs = conn.cursor()

try:
    cs.execute("USE DATABASE COMMON_DB_DEV")
    cs.execute("USE SCHEMA DBT_PROJECTS")

    cs.execute("ALTER GIT REPOSITORY HAL_REPO FETCH")

    cs.execute("CREATE OR REPLACE DBT PROJECT DBTPOC FROM '@HAL_REPO/branches/main/Hal_dbt_poc'")

finally:
    cs.close()
    conn.close()
