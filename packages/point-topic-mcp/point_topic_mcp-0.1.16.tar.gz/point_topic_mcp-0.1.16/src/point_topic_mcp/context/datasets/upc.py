
def get_dataset_summary():
    """This will be visible to the agent at all times, so keep it short, but let the agent know if the dataset can answer the question of the user."""
    return """
    UK broadband infrastructure availability data at postcode level. 
    Monthly snapshots showing operator footprint and premises coverage (not subscriber numbers). 
    UPC_OUTPUT table has a row for each postcode, with geographic, demograpgic and broadband availability data.
    FACT_OPERATOR table has a row for each postcode, operator and technology, with the fastest up and down speeds.
    """


def get_db_info():
    return f"""
    {DB_INFO}

    {DB_SCHEMA}

    {SQL_EXAMPLES}
    """

DB_INFO = """

Broadband availability datasets for the UK at postcode granularity. Monthly snapshots.

UPC stands for unit post code, so all UPC tables are at postcode granularity

The reported_at field always lands on the first day of the month.

Remember that footprint/premises passed is not the same as market share. 
The market share would be the number of subscribers (paying customers), 
wheras the footprint is the number of premises that have availability

Key UK Broadband Market Facts (for sanity checking):
- Total UK premises: approximately 33 million
- Total UK households: approximately 30 million  
- Total UK population: approximately 67 million
- If your query results show significantly different totals, double-check your calculations

Always sanity check your results against these known facts.

CRITICAL: Market Share and Total Premises Calculations

upc_core.reports.fact_operator is unique per postcode,operator,tech and reported_at
so when getting sums of premises by joining upc on postcode,reported_at you must
get the distinct list of postcodes, as there can be duplicates when an operator has multiple technology

MARKET SHARE CALCULATIONS:
- For calculating TOTAL UK premises or market denominators, ALWAYS use upc_core.reports.upc_output directly
- Careful when summing premises from upc_core.reports.fact_operator joins as this can creates duplicates for shared postcodes
- Individual operator footprints: Use distinct postcodes from upc_core.reports.fact_operator joined to upc_output
- Total market size: Use SUM(premises) FROM upc_core.reports.upc_output directly

Make a note that this is AVAILABILITY market share, not based on Subscribers

Example pattern for market share:
1. Operator footprint: select sum(premises) from upc_core.reports.fact_operator f join upc_core.reports.upc_output u USING(postcode) WHERE f.operator = 'X' GROUP BY postcode
2. Total market: select sum(premises) from upc_core.reports.upc_output (separate query, not derived from operator data)

Note the virgin media isps are as follows:
'Virgin Media RFOG'
'Virgin Cable'

For altnet queries we exclude Openreach ops and virgin media ops 

for example:
where operator not in ('BT','Sky','TalkTalk','Vodafone','Virgin Cable','Virgin Media RFOG')

we also group together the CityFibre ops:
when operator like '%CityFibre%' then 'CityFibre'

To see the full list of operators available in the database, use the get_distinct_value_list('upc','operator') tool.

Tips for UPC tables:
1. You can use the upc_core.utils.commaify() UDF in the final results to format large numbers with commas - but then you can not order by the column as its a string! you must order by the unformatted column. Only works in UPC_CORE.REPORTS schema
2. For fttp queries to fact_operator, you can use the tech like '%fttp%' filter because there is one type of value 'fttponly'
3. If the answer only requires current data then use the upc_output or fact_operator tables directly. No need to use the time series tables.
4. CRITICAL FOR MARKET SHARE AND AVAILABILITY SUMS: Total UK premises must come from upc_output directly. Never derive totals from fact_operator joins.
5. If the question is about how many homes were passed by an operator - Then use the households metric in the upc output table.
"""

DB_SCHEMA = """
upc_core.reports.fact_operator_time_series (
	postcode varchar(16777216) comment 'name of postcode',
	operator varchar(16777216) comment 'name of operator',
	tech varchar(16777216) comment 'technology',
	fastest_up number(38,2) comment 'fastest upload speed',
	fastest_down number(38,0) comment 'fastest download speed',
	activated_date date comment 'date when this footprint happenws',
	reported_at date comment 'represent for version of postcode (vtable-tbb)'
)

upc_core.reports.fact_operator (
    # this is the same as upc_core.reports.fact_operator_time_series but with only the most recent snapshot of data
)

upc_core.reports.upc_output_time_series (
	postcode varchar(16777216) comment 'key for upc_output, unique per reporting month',
	mapinfo_id number(18,0) comment 'map information identification code',
	post_sector varchar(16777216) comment 'higher level postcode grouping',
	northings number(38,0) comment 'distance in metres north of national grid origin',
	eastings number(38,0) comment 'distance in metres east of national grid origin',
	coa_code varchar(16777216) comment 'ons-defined code for the census output area in which the upc is located',
	lsoa varchar(16777216) comment 'ons-defined code for the lower super output area in which the upc is located',
	msoa_and_im varchar(16777216) comment 'ons-defined code for the middle super output area or intermediate zone in scotland in which the upc is located',
	la_code varchar(16777216) comment 'local authority area code',
	la_name varchar(16777216) comment 'local authority area name',
	government_region varchar(16777216) comment 'government region',
	country varchar(16777216) comment 'name of the nation in which the upc is located',
	population number(38,2) comment 'estimated population of the upc',
	premises number(38,2) comment 'total number of households and business premises (sites or workplaces) in the upc',
	households number(38,0) comment 'estimated number of households in the upc',
	bus_sites_total number(38,2) comment 'estimated number of business premises (sites or workplaces) in the upc',
	mdfcode varchar(16777216) comment 'identifier for bt/openreach exchange serving the upc',
	exchange_name varchar(16777216) comment 'name of exchange serving the upc',
	cityfibre_postcode_passed varchar(1) comment 'whether the upc is within cityfibre halo (200m-500m)',
)

upc_core.reports.upc_output (
    # this is the same as upc_core.reports.upc_output_time_series but with only the most recent snapshot of data
)

"""

SQL_EXAMPLES = [
    {
        'request': 'Can you show me which local authorities have seen the highest growth in FTTP coverage over the last 6 months?',
        'response': """
-- Get current FTTP coverage and total premises for each local authority
with 

    current_coverage as (
    select 
        la_name,
        reported_at,
        sum(premises) as total_premises,
        sum(case when tech like '%fttp%' then premises else 0 end) as fttp_premises
    from upc_core.reports.fact_operator_time_series
    join upc_core.reports.upc_output_time_series using (postcode, reported_at)
    where reported_at = (select max(reported_at) from upc_core.reports.fact_operator_time_series)
    group by la_name, reported_at
    ),

    -- Get FTTP coverage from 6 months ago for comparison
    six_months_ago as (
    select 
        la_name,
        reported_at,
        sum(case when tech like '%fttp%' then premises else 0 end) as fttp_premises_old
    from upc_core.reports.fact_operator_time_series
    join upc_core.reports.upc_output_time_series using (postcode, reported_at)
    where reported_at = dateadd(month, -6, (select max(reported_at) from upc_core.reports.fact_operator_time_series))
    group by la_name, reported_at
    )

select 
    c.la_name,
    round((c.fttp_premises - o.fttp_premises_old) / c.total_premises * 100, 2) as fttp_growth_percentage,
    c.fttp_premises - o.fttp_premises_old as absolute_premise_growth
from current_coverage c
join six_months_ago o using (la_name)
order by fttp_growth_percentage desc
limit 20
""",
    },
    {
        'request': 'Which alternative network operators have the fastest growing footprint in terms of premises passed in the last quarter?',
        'response': """


with 

    -- Get current quarter premises passed for each altnet operator
    current_quarter as (
    select 
        operator,
        sum(premises) as current_premises
    from upc_core.reports.fact_operator_time_series
    join upc_core.reports.upc_output_time_series using (postcode, reported_at)
    where reported_at = (select max(reported_at) from upc_core.reports.fact_operator_time_series)
    and operator not in ('BT', 'Virgin Media', 'Sky', 'TalkTalk')
    group by operator
    ),

    -- Get previous quarter premises passed for comparison
    previous_quarter as (
    select 
        operator,
        sum(premises) as previous_premises
    from upc_core.reports.fact_operator_time_series
    join upc_core.reports.upc_output_time_series using (postcode, reported_at)
    where reported_at = dateadd(month, -3, (select max(reported_at) from upc_core.reports.fact_operator_time_series))
    and operator not in ('BT', 'Virgin Media', 'Sky', 'TalkTalk')
    group by operator
    )

select 
    c.operator,
    c.current_premises,
    p.previous_premises,
    c.current_premises - p.previous_premises as absolute_growth,
    round((c.current_premises - p.previous_premises) / p.previous_premises * 100, 2) as growth_percentage
from current_quarter c
join previous_quarter p using (operator)
where p.previous_premises > 0
order by growth_percentage desc
            """,
    },
    {
        'request': 'Show me areas where theres high competition between FTTP providers - specifically postcodes with 3 or more operators',
        'response': """

with 

    -- Count number of FTTP operators per postcode and create list of operators
    operator_count as (
    select 
        postcode,
        count(distinct operator) as operator_count,
        listagg(distinct operator, ', ') as operators
    from upc_core.reports.fact_operator_time_series
    where reported_at = (select max(reported_at) from upc_core.reports.fact_operator_time_series)
    and tech like '%fttp%'
    group by postcode
    )

select 
    u.la_name,
    sum(u.premises) as total_premises_affected,
    count(distinct u.postcode) as postcode_count,
    round(sum(u.premises) / sum(sum(u.premises)) over () * 100, 2) as percentage_of_total_premises
from operator_count o
join upc_core.reports.upc_output_time_series u using (postcode)
where o.operator_count >= 3
and u.reported_at = (select max(reported_at) from upc_core.reports.upc_output_time_series)
group by u.la_name
order by total_premises_affected desc


            """,    
    },
    {
        'request': 'Show me the top 10 operators by premises passed in the last quarter',
        'response': """
with

    -- get the current premises from upc_core.reports.upc_output_time_series
    upc as (
    select 
        postcode,
        premises
    from upc_core.reports.upc_core.reports.upc_output_time_series
    -- get the most recent snapshot
    where reported_at = (select max(reported_at) from upc_core.reports.upc_core.reports.upc_output_time_series)
    ),

    -- get the operator footprint from upc_core.reports.fact_operator_time_series
    -- making sure to get the distinct list of postcodes
    total_operator_footprint as (
    select
        postcode,
        operator
    from upc_core.reports.upc_core.reports.fact_operator_time_series
    where reported_at = (select max(reported_at) from upc_core.reports.upc_core.reports.fact_operator_time_series)
    -- need this to remove duplicates as there are multiple techs per operator per postcode in some cases
    group by 1,2
    ),

    -- get the total premises
    agg as (
    select 
        operator,
        sum(premises) as total_premises
    from upc
    left join total_operator_footprint total using (postcode)
    group by 1
    )

select
    operator,
    total_premises
from agg
order by total_premises desc
limit 10

        """
    },
    {
        'request': 'What is the market share of Hyperoptic in the UK FTTP market?',
        'response': """

-- Calculate Hyperoptic's market share of UK FTTP market
with 

    -- Get all FTTP operators and their premises passed (ensuring distinct postcodes per operator)
    fttp_operators as (
    select 
        operator,
        postcode
    from fact_operator
    where tech like '%fttp%'
    group by operator, postcode
    ),
    
    -- Calculate total premises passed by each operator
    operator_premises as (
    select 
        f.operator,
        sum(u.premises) as premises_passed
    from fttp_operators f
    join upc_core.reports.upc_output u using (postcode)
    group by f.operator
    ),
    
    -- Calculate total FTTP market size
    total_fttp_market as (
    select 
        sum(premises) as total_premises
    from upc_output
    where postcode in (select distinct postcode from fttp_operators)
    )

select 
    operator,
    upc_core.utils.commaify(coalesce(o.premises_passed, 0)) as premises_passed,
    upc_core.utils.commaify(t.total_premises) as total_premises,
    round((coalesce(o.premises_passed, 0) / t.total_premises) * 100,2) as market_share_percentage
from total_fttp_market t
left join operator_premises o on o.operator = 'Hyperoptic'
        """
    },
    {
        'request': 'As of Q2-25 how much B2B FTTP overbuild does Toob have relative to Virgin Media? Also, in which regions of the UK are toob based?',
        'response': """
-- Answer both questions: Toob vs Virgin Media B2B FTTP overbuild + Toob's UK regions
with 

    -- Get postcodes where both Toob and Virgin Media have FTTP (overbuild areas)
    overbuild_postcodes as (
        select distinct f1.postcode
        from upc_core.reports.fact_operator f1
        where f1.operator = 'toob'
        and f1.tech like '%fttp%'
        and exists (
            select 1 from upc_core.reports.fact_operator f2 
            where f2.postcode = f1.postcode 
            and f2.operator in ('Virgin Cable', 'Virgin Media RFOG')
            and f2.tech like '%fttp%'
        )
    ),
    
    -- Calculate overbuild metrics in those postcodes
    overbuild_metrics as (
        select 
            upc_core.utils.commaify(round(sum(u.bus_sites_total), 0)) as overbuild_b2b_sites,
            upc_core.utils.commaify(round(sum(u.households), 0)) as overbuild_households,
            upc_core.utils.commaify(round(sum(u.premises), 0)) as overbuild_total_premises,
            count(distinct o.postcode) as overbuild_postcodes
        from overbuild_postcodes o
        join upc_core.reports.upc_output u using (postcode)
    ),
    
    -- Get all regions where Toob operates
    toob_regions as (
        select listagg(distinct u.government_region, ', ') as regions_list
        from upc_core.reports.fact_operator f
        join upc_core.reports.upc_output u using (postcode)
        where f.operator = 'toob'
    ),
    
    -- Get total Toob footprint for context (ensuring distinct postcodes)
    toob_total as (
        select 
            upc_core.utils.commaify(round(sum(u.bus_sites_total), 0)) as total_b2b_sites,
            upc_core.utils.commaify(round(sum(u.premises), 0)) as total_premises
        from (
            select distinct f.postcode
            from upc_core.reports.fact_operator f
            where f.operator = 'toob'
        ) f
        join upc_core.reports.upc_output u using (postcode)
    )

-- Create readable two-column output format
select metric_description, metric_value
from (
    select 1 as sort_order, 'B2B Sites in Virgin Media Overbuild Areas' as metric_description, o.overbuild_b2b_sites as metric_value
    from overbuild_metrics o
    
    union all
    
    select 2, 'Households in Overbuild Areas', o.overbuild_households
    from overbuild_metrics o
    
    union all
    
    select 3, 'Overbuild Postcodes Count', o.overbuild_postcodes::varchar
    from overbuild_metrics o
    
    union all
    
    select 4, 'Toob Total B2B Sites (for context)', t.total_b2b_sites
    from toob_total t
    
    union all
    
    select 5, 'Toob Total Premises (for context)', t.total_premises
    from toob_total t
    
    union all
    
    select 6, 'UK Regions Where Toob Operates', r.regions_list
    from toob_regions r
)
order by sort_order
        """
    }
]
